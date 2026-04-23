# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 723252a7c49e47e86263ca454985e9f170cdbd34de6a5d90e0105e8365ff2c1e
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/POWERLINK/"
_VERSION: str = "1.0.0"
_REQUIRED: list = [
    {"uri": "http://opcfoundation.org/UA/", "version": "1.03"},
    {"uri": "http://opcfoundation.org/UA/DI/", "version": "1.01"},
]
_STRUCTURES: list = [
    (
        "ns=1;i=27",
        "PowerlinkErrorEntryDataType",
        "ns=1;i=53",
        {
            "structure_type": 0,
            "fields": [
                {"name": "entryType", "data_type": "i=5", "value_rank": -1},
                {"name": "errorCode", "data_type": "i=5", "value_rank": -1},
                {"name": "timeStamp", "data_type": "i=9", "value_rank": -1},
                {"name": "additionalInformation", "data_type": "i=9", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=29",
        "PowerlinkIpAddressDataType",
        "ns=1;i=32",
        {
            "structure_type": 0,
            "fields": [
                {"name": "b1", "data_type": "i=3", "value_rank": -1},
                {"name": "b2", "data_type": "i=3", "value_rank": -1},
                {"name": "b3", "data_type": "i=3", "value_rank": -1},
                {"name": "b4", "data_type": "i=3", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=30",
        "PowerlinkPDOMappingEntryDataType",
        "ns=1;i=40",
        {
            "structure_type": 0,
            "fields": [
                {"name": "length", "data_type": "i=5", "value_rank": -1},
                {"name": "offset", "data_type": "i=5", "value_rank": -1},
                {"name": "reserved", "data_type": "i=3", "value_rank": -1},
                {"name": "subIndex", "data_type": "i=3", "value_rank": -1},
                {"name": "index", "data_type": "i=5", "value_rank": -1},
            ],
        },
    ),
]
_ENUMS: list = [
    (
        "ns=1;i=28",
        "PowerlinkNMTResetCmdEnumeration",
        {
            "fields": [
                {"name": "NMTResetNode", "value": 40, "display_name": "NMTResetNode"},
                {
                    "name": "NMTResetCommunication",
                    "value": 41,
                    "display_name": "NMTResetCommunication",
                },
                {
                    "name": "NMTResetConfiguration",
                    "value": 42,
                    "display_name": "NMTResetConfiguration",
                },
                {"name": "NMTSwReset", "value": 43, "display_name": "NMTSwReset"},
                {
                    "name": "NMTInvalidService",
                    "value": 255,
                    "display_name": "NMTInvalidService",
                },
            ]
        },
    ),
    (
        "ns=1;i=24",
        "PowerlinkNMTStateEnumeration",
        {
            "fields": [
                {"name": "NMT_GS_OFF ", "value": 0, "display_name": "NMT_GS_OFF "},
                {
                    "name": "NMT_GS_INITIALISING",
                    "value": 25,
                    "display_name": "NMT_GS_INITIALISING",
                },
                {
                    "name": "NMT_GS_RESET_APPLICATION",
                    "value": 41,
                    "display_name": "NMT_GS_RESET_APPLICATION",
                },
                {
                    "name": "NMT_GS_RESET_COMMUNICATION",
                    "value": 57,
                    "display_name": "NMT_GS_RESET_COMMUNICATION",
                },
                {
                    "name": "NMT_GS_RESET_CONFIGURATION",
                    "value": 121,
                    "display_name": "NMT_GS_RESET_CONFIGURATION",
                },
                {
                    "name": "NMT_XS_NOT_ACTIVE",
                    "value": 28,
                    "display_name": "NMT_XS_NOT_ACTIVE",
                },
                {
                    "name": "NMT_XS_PRE_OPERATIONAL_1",
                    "value": 29,
                    "display_name": "NMT_XS_PRE_OPERATIONAL_1",
                },
                {
                    "name": "NMT_XS_PRE_OPERATIONAL_2",
                    "value": 93,
                    "display_name": "NMT_XS_PRE_OPERATIONAL_2",
                },
                {
                    "name": "NMT_XS_READY_TO_OPERATE",
                    "value": 109,
                    "display_name": "NMT_XS_READY_TO_OPERATE",
                },
                {
                    "name": "NMT_XS_OPERATIONAL",
                    "value": 253,
                    "display_name": "NMT_XS_OPERATIONAL",
                },
                {
                    "name": "NMT_CS_STOPPED",
                    "value": 77,
                    "display_name": "NMT_CS_STOPPED",
                },
                {
                    "name": "NMT_XS_BASIC_ETHERNET",
                    "value": 30,
                    "display_name": "NMT_XS_BASIC_ETHERNET",
                },
            ]
        },
    ),
    (
        "ns=1;i=26",
        "ErrorRegisterBits",
        {
            "fields": [
                {"name": "Generic_error", "value": 0, "display_name": "Generic_error"},
                {"name": "Current", "value": 1, "display_name": "Current"},
                {"name": "Voltage", "value": 2, "display_name": "Voltage"},
                {"name": "Temperature", "value": 3, "display_name": "Temperature"},
                {
                    "name": "Communication_error",
                    "value": 4,
                    "display_name": "Communication_error",
                },
                {
                    "name": "Device_profile_specific",
                    "value": 5,
                    "display_name": "Device_profile_specific",
                },
                {"name": "Reserved", "value": 6, "display_name": "Reserved"},
                {
                    "name": "Manufacturer_specific",
                    "value": 7,
                    "display_name": "Manufacturer_specific",
                },
            ]
        },
    ),
    (
        "ns=1;i=25",
        "PowerlinkAttribute",
        {
            "fields": [
                {"name": "Const", "value": 0, "display_name": "Const"},
                {"name": "Read", "value": 1, "display_name": "Read"},
                {"name": "Write", "value": 2, "display_name": "Write"},
                {"name": "Input", "value": 3, "display_name": "Input"},
                {"name": "Output", "value": 4, "display_name": "Output"},
                {"name": "Store", "value": 5, "display_name": "Store"},
                {"name": "ValidOnReset", "value": 6, "display_name": "ValidOnReset"},
                {
                    "name": "DefaultMapping",
                    "value": 7,
                    "display_name": "DefaultMapping",
                },
                {"name": "RPDO", "value": 8, "display_name": "RPDO"},
                {"name": "TPDO", "value": 9, "display_name": "TPDO"},
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = (
    [
        ("ns=1;i=27", "ns=1;i=53", ["i=5", "i=5", "i=9", "i=9"]),
        ("ns=1;i=29", "ns=1;i=32", ["i=3", "i=3", "i=3", "i=3"]),
        ("ns=1;i=30", "ns=1;i=40", ["i=5", "i=5", "i=3", "i=3", "i=5"]),
    ],
    ["ns=1;i=28", "ns=1;i=24", "ns=1;i=26", "ns=1;i=25"],
)
_NODES: dict = {
    "datatypes": {
        "ErrorRegisterBits": (
            "D",
            "ns=1;i=26",
            {"OptionSetValues": ("V", "ns=1;i=96", {})},
        ),
        "PowerlinkAttribute": (
            "D",
            "ns=1;i=25",
            {"OptionSetValues": ("V", "ns=1;i=90", {})},
        ),
        "PowerlinkErrorEntryDataType": ("D", "ns=1;i=27", {}),
        "PowerlinkIpAddressDataType": ("D", "ns=1;i=29", {}),
        "PowerlinkNMTResetCmdEnumeration": (
            "D",
            "ns=1;i=28",
            {"EnumValues": ("V", "ns=1;i=132", {})},
        ),
        "PowerlinkNMTStateEnumeration": (
            "D",
            "ns=1;i=24",
            {"EnumValues": ("V", "ns=1;i=139", {})},
        ),
        "PowerlinkPDOMappingEntryDataType": ("D", "ns=1;i=30", {}),
    },
    "objects": {
        "Default Binary": ("O", "ns=1;i=53", {}),
        "Default XML": ("O", "ns=1;i=54", {}),
        "TypeDictionary": (
            "V",
            "ns=1;i=83",
            {
                "ErrorRegisterBits": ("V", "ns=1;i=98", {}),
                "NamespaceUri": ("V", "ns=1;i=84", {}),
                "PowerlinkAttribute": ("V", "ns=1;i=92", {}),
                "PowerlinkErrorEntryDataType": ("V", "ns=1;i=218", {}),
                "PowerlinkIpAddressDataType": ("V", "ns=1;i=153", {}),
                "PowerlinkPDOMappingEntryDataType": ("V", "ns=1;i=155", {}),
            },
        ),
        "http://opcfoundation.org/UA/POWERLINK/": (
            "O",
            "ns=1;i=31",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=135", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=146", {}),
                "NamespaceUri": ("V", "ns=1;i=147", {}),
                "NamespaceVersion": ("V", "ns=1;i=148", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=149", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=150", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=151", {}),
            },
        ),
    },
    "objtypes": {
        "PowerlinkConnectionPointType": (
            "OT",
            "ns=1;i=3",
            {
                "<ProfileId>": ("O", "ns=1;i=59", {}),
                "Configuration": ("O", "ns=1;i=63", {}),
                "Control": ("O", "ns=1;i=65", {}),
                "Diagnostics": ("O", "ns=1;i=60", {}),
                "Identification": ("O", "ns=1;i=58", {}),
                "MethodSet": (
                    "O",
                    "ns=1;i=46",
                    {
                        "ReadByIndex": (
                            "M",
                            "ns=1;i=1366",
                            {
                                "InputArguments": ("V", "ns=1;i=1369", {}),
                                "OutputArguments": ("V", "ns=1;i=1372", {}),
                            },
                        ),
                        "WriteByIndex": (
                            "M",
                            "ns=1;i=1081",
                            {
                                "InputArguments": ("V", "ns=1;i=1375", {}),
                                "OutputArguments": ("V", "ns=1;i=1376", {}),
                            },
                        ),
                    },
                ),
                "NetworkAddress": ("O", "ns=1;i=57", {}),
                "ParameterSet": (
                    "O",
                    "ns=1;i=47",
                    {
                        "INP_ProcessImage_REC": (
                            "V",
                            "ns=1;i=1321",
                            {
                                "Index": ("V", "ns=1;i=1330", {}),
                                "NumberOfEntries": ("V", "ns=1;i=1331", {}),
                                "ProcessImageDomain_DOM": (
                                    "V",
                                    "ns=1;i=1322",
                                    {
                                        "Index": ("V", "ns=1;i=1323", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1324", {}),
                                        "SubIndex": ("V", "ns=1;i=1325", {}),
                                    },
                                ),
                                "SelectedRange_U32": (
                                    "V",
                                    "ns=1;i=1326",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2627", {}),
                                        "Index": ("V", "ns=1;i=1327", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1328", {}),
                                        "SubIndex": ("V", "ns=1;i=1329", {}),
                                    },
                                ),
                            },
                        ),
                        "NMT_ChildIdentList_AU16": (
                            "V",
                            "ns=1;i=538",
                            {
                                "Index": ("V", "ns=1;i=539", {}),
                                "NumberOfEntries": ("V", "ns=1;i=540", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=541", {}),
                                "Range": ("V", "ns=1;i=2727", {}),
                            },
                        ),
                        "NMT_CurrNMTState_U8": (
                            "V",
                            "ns=1;i=1162",
                            {
                                "DefaultValue": ("V", "ns=1;i=2731", {}),
                                "Index": ("V", "ns=1;i=1163", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=1164", {}),
                                "SubIndex": ("V", "ns=1;i=1165", {}),
                            },
                        ),
                        "NMT_DeviceType_U32": (
                            "V",
                            "ns=1;i=550",
                            {
                                "Index": ("V", "ns=1;i=551", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=552", {}),
                                "SubIndex": ("V", "ns=1;i=553", {}),
                            },
                        ),
                        "NMT_EPLNodeID_REC": (
                            "V",
                            "ns=1;i=138",
                            {
                                "Index": ("V", "ns=1;i=447", {}),
                                "NodeIDByHW_BOOL": (
                                    "V",
                                    "ns=1;i=102",
                                    {
                                        "Index": ("V", "ns=1;i=456", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=457", {}),
                                        "SubIndex": ("V", "ns=1;i=458", {}),
                                    },
                                ),
                                "NodeID_U8": (
                                    "V",
                                    "ns=1;i=88",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2901", {}),
                                        "Index": ("V", "ns=1;i=141", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=142", {}),
                                        "SubIndex": ("V", "ns=1;i=143", {}),
                                    },
                                ),
                                "NumberOfEntries": ("V", "ns=1;i=448", {}),
                                "SWNodeID_U8": (
                                    "V",
                                    "ns=1;i=111",
                                    {
                                        "Index": ("V", "ns=1;i=112", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2906", {}),
                                        "SubIndex": ("V", "ns=1;i=2907", {}),
                                    },
                                ),
                            },
                        ),
                        "NMT_EPLVersion_U8": (
                            "V",
                            "ns=1;i=682",
                            {
                                "Index": ("V", "ns=1;i=683", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=684", {}),
                                "SubIndex": ("V", "ns=1;i=685", {}),
                            },
                        ),
                        "NMT_FeatureFlags_U32": (
                            "V",
                            "ns=1;i=562",
                            {
                                "Index": ("V", "ns=1;i=563", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=564", {}),
                                "SubIndex": ("V", "ns=1;i=565", {}),
                            },
                        ),
                        "NMT_HostName_VSTR": (
                            "V",
                            "ns=1;i=686",
                            {
                                "Index": ("V", "ns=1;i=687", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=688", {}),
                                "SubIndex": ("V", "ns=1;i=689", {}),
                            },
                        ),
                        "NMT_IdentityObject_REC": (
                            "V",
                            "ns=1;i=702",
                            {
                                "Index": ("V", "ns=1;i=707", {}),
                                "NumberOfEntries": ("V", "ns=1;i=708", {}),
                                "ProductCode_U32": (
                                    "V",
                                    "ns=1;i=2588",
                                    {
                                        "Index": ("V", "ns=1;i=2589", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2590", {}),
                                        "SubIndex": ("V", "ns=1;i=2591", {}),
                                    },
                                ),
                                "RevisionNo_U32": (
                                    "V",
                                    "ns=1;i=2592",
                                    {
                                        "Index": ("V", "ns=1;i=2593", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2594", {}),
                                        "SubIndex": ("V", "ns=1;i=2595", {}),
                                    },
                                ),
                                "SerialNo_U32": (
                                    "V",
                                    "ns=1;i=2596",
                                    {
                                        "Index": ("V", "ns=1;i=2597", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2598", {}),
                                        "SubIndex": ("V", "ns=1;i=2599", {}),
                                    },
                                ),
                                "VendorId_U32": (
                                    "V",
                                    "ns=1;i=703",
                                    {
                                        "Index": ("V", "ns=1;i=704", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=705", {}),
                                        "SubIndex": ("V", "ns=1;i=706", {}),
                                    },
                                ),
                            },
                        ),
                        "NMT_InterfaceGroup_0h_REC": (
                            "V",
                            "ns=1;i=1204",
                            {
                                "Index": ("V", "ns=1;i=1241", {}),
                                "InterfaceAdminState_U8": (
                                    "V",
                                    "ns=1;i=1205",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2925", {}),
                                        "Index": ("V", "ns=1;i=1206", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1207", {}),
                                        "Range": ("V", "ns=1;i=2926", {}),
                                        "SubIndex": ("V", "ns=1;i=1208", {}),
                                    },
                                ),
                                "InterfaceDescription_VSTR": (
                                    "V",
                                    "ns=1;i=1209",
                                    {
                                        "Index": ("V", "ns=1;i=1210", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1211", {}),
                                        "SubIndex": ("V", "ns=1;i=1212", {}),
                                    },
                                ),
                                "InterfaceIndex_U16": (
                                    "V",
                                    "ns=1;i=1213",
                                    {
                                        "Index": ("V", "ns=1;i=1214", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1215", {}),
                                        "Range": ("V", "ns=1;i=2918", {}),
                                        "SubIndex": ("V", "ns=1;i=1216", {}),
                                    },
                                ),
                                "InterfaceMtu_U16": (
                                    "V",
                                    "ns=1;i=1217",
                                    {
                                        "Index": ("V", "ns=1;i=1218", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1219", {}),
                                        "SubIndex": ("V", "ns=1;i=1220", {}),
                                    },
                                ),
                                "InterfaceName_VSTR": (
                                    "V",
                                    "ns=1;i=1221",
                                    {
                                        "Index": ("V", "ns=1;i=1222", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1223", {}),
                                        "SubIndex": ("V", "ns=1;i=1224", {}),
                                    },
                                ),
                                "InterfaceOperStatus_U8": (
                                    "V",
                                    "ns=1;i=1225",
                                    {
                                        "Index": ("V", "ns=1;i=1226", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1227", {}),
                                        "Range": ("V", "ns=1;i=2936", {}),
                                        "SubIndex": ("V", "ns=1;i=1228", {}),
                                    },
                                ),
                                "InterfacePhysAddress_OSTR": (
                                    "V",
                                    "ns=1;i=1229",
                                    {
                                        "Index": ("V", "ns=1;i=1230", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1231", {}),
                                        "SubIndex": ("V", "ns=1;i=1232", {}),
                                    },
                                ),
                                "InterfaceType_U8": (
                                    "V",
                                    "ns=1;i=1233",
                                    {
                                        "Index": ("V", "ns=1;i=1234", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1235", {}),
                                        "SubIndex": ("V", "ns=1;i=1236", {}),
                                    },
                                ),
                                "NumberOfEntries": ("V", "ns=1;i=1242", {}),
                                "PortEnableMask_U64": (
                                    "V",
                                    "ns=1;i=2941",
                                    {
                                        "Index": ("V", "ns=1;i=2942", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2945", {}),
                                        "SubIndex": ("V", "ns=1;i=2946", {}),
                                    },
                                ),
                                "Valid_BOOL": (
                                    "V",
                                    "ns=1;i=1237",
                                    {
                                        "Index": ("V", "ns=1;i=1238", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1239", {}),
                                        "SubIndex": ("V", "ns=1;i=1240", {}),
                                    },
                                ),
                            },
                        ),
                        "NMT_ManufactDevName_VS": (
                            "V",
                            "ns=1;i=690",
                            {
                                "Index": ("V", "ns=1;i=691", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=692", {}),
                                "SubIndex": ("V", "ns=1;i=693", {}),
                            },
                        ),
                        "NMT_ManufactHwVers_VS": (
                            "V",
                            "ns=1;i=694",
                            {
                                "Index": ("V", "ns=1;i=695", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=696", {}),
                                "SubIndex": ("V", "ns=1;i=697", {}),
                            },
                        ),
                        "NMT_ManufactSwVers_VS": (
                            "V",
                            "ns=1;i=698",
                            {
                                "Index": ("V", "ns=1;i=699", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=700", {}),
                                "SubIndex": ("V", "ns=1;i=701", {}),
                            },
                        ),
                        "NMT_RelativeLatencyDiff_AU32": (
                            "V",
                            "ns=1;i=594",
                            {
                                "Index": ("V", "ns=1;i=595", {}),
                                "NumberOfEntries": ("V", "ns=1;i=596", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=597", {}),
                            },
                        ),
                        "NMT_ResetCmd_U8": (
                            "V",
                            "ns=1;i=1332",
                            {
                                "DefaultValue": ("V", "ns=1;i=3252", {}),
                                "Index": ("V", "ns=1;i=1333", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=1334", {}),
                                "SubIndex": ("V", "ns=1;i=1335", {}),
                            },
                        ),
                        "NWL_IpAddrTable_0h_REC": (
                            "V",
                            "ns=1;i=468",
                            {
                                "Addr_IPAD": (
                                    "V",
                                    "ns=1;i=469",
                                    {
                                        "Index": ("V", "ns=1;i=471", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=472", {}),
                                        "SubIndex": ("V", "ns=1;i=473", {}),
                                    },
                                ),
                                "DefaultGateway_IPAD": (
                                    "V",
                                    "ns=1;i=474",
                                    {
                                        "Index": ("V", "ns=1;i=475", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=476", {}),
                                        "SubIndex": ("V", "ns=1;i=477", {}),
                                    },
                                ),
                                "IfIndex_U16": (
                                    "V",
                                    "ns=1;i=478",
                                    {
                                        "Index": ("V", "ns=1;i=479", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=480", {}),
                                        "Range": ("V", "ns=1;i=2965", {}),
                                        "SubIndex": ("V", "ns=1;i=481", {}),
                                    },
                                ),
                                "Index": ("V", "ns=1;i=490", {}),
                                "NetMask_IPAD": (
                                    "V",
                                    "ns=1;i=482",
                                    {
                                        "Index": ("V", "ns=1;i=483", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=484", {}),
                                        "SubIndex": ("V", "ns=1;i=485", {}),
                                    },
                                ),
                                "NumberOfEntries": ("V", "ns=1;i=491", {}),
                                "ReasmMaxSize_U16": (
                                    "V",
                                    "ns=1;i=486",
                                    {
                                        "Index": ("V", "ns=1;i=487", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=488", {}),
                                        "SubIndex": ("V", "ns=1;i=489", {}),
                                    },
                                ),
                            },
                        ),
                    },
                ),
                "PowerlinkCnConnectionPointType": (
                    "OT",
                    "ns=1;i=4",
                    {
                        "<DeviceProfileIdentifier>": (
                            "O",
                            "ns=1;i=52",
                            {
                                "IndexRangeSize": ("V", "ns=1;i=1381", {}),
                                "IndexRangeStart": ("V", "ns=1;i=1382", {}),
                            },
                        ),
                        "Configuration": (
                            "O",
                            "ns=1;i=41",
                            {
                                "DLL_CNSoCJitterRange_U32": (
                                    "V",
                                    "ns=1;i=1687",
                                    {
                                        "Index": ("V", "ns=1;i=1688", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1689", {}),
                                        "SubIndex": ("V", "ns=1;i=1690", {}),
                                    },
                                ),
                                "NMT_CNBasicEthernetTimeout_U32": (
                                    "V",
                                    "ns=1;i=1683",
                                    {
                                        "Index": ("V", "ns=1;i=1684", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1685", {}),
                                        "SubIndex": ("V", "ns=1;i=1686", {}),
                                    },
                                ),
                                "NMT_ConsumerHeartbeatTime_AU32": (
                                    "V",
                                    "ns=1;i=590",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2730", {}),
                                        "Index": ("V", "ns=1;i=591", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=592", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=593", {}),
                                    },
                                ),
                                "NMT_CycleLen_U32": (
                                    "V",
                                    "ns=1;i=574",
                                    {
                                        "Index": ("V", "ns=1;i=575", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=576", {}),
                                        "SubIndex": ("V", "ns=1;i=577", {}),
                                    },
                                ),
                                "NMT_CycleTiming_REC": (
                                    "V",
                                    "ns=1;i=785",
                                    {
                                        "ASndMaxLatency_U32": (
                                            "V",
                                            "ns=1;i=2762",
                                            {
                                                "Index": ("V", "ns=1;i=2763", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2764",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2765", {}),
                                            },
                                        ),
                                        "AsyncMTU_U16": (
                                            "V",
                                            "ns=1;i=786",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2748",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=787", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=788",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=2749", {}),
                                                "SubIndex": ("V", "ns=1;i=789", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=802", {}),
                                        "IsochrRxMaxPayload_U16": (
                                            "V",
                                            "ns=1;i=790",
                                            {
                                                "Index": ("V", "ns=1;i=791", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=792",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=2741", {}),
                                                "SubIndex": ("V", "ns=1;i=793", {}),
                                            },
                                        ),
                                        "IsochrTxMaxPayload_U16": (
                                            "V",
                                            "ns=1;i=794",
                                            {
                                                "Index": ("V", "ns=1;i=795", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=796",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=2735", {}),
                                                "SubIndex": ("V", "ns=1;i=797", {}),
                                            },
                                        ),
                                        "LeaseTime_U32": (
                                            "V",
                                            "ns=1;i=2766",
                                            {
                                                "Index": ("V", "ns=1;i=2767", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2768",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2769", {}),
                                            },
                                        ),
                                        "MultiplCycleCnt_U8": (
                                            "V",
                                            "ns=1;i=798",
                                            {
                                                "Index": ("V", "ns=1;i=799", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=800",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=801", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=803", {}),
                                        "PReqActPayloadLimit_U16": (
                                            "V",
                                            "ns=1;i=2770",
                                            {
                                                "Index": ("V", "ns=1;i=2771", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2772",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2773", {}),
                                            },
                                        ),
                                        "PResActPayloadLimit_U16": (
                                            "V",
                                            "ns=1;i=2774",
                                            {
                                                "Index": ("V", "ns=1;i=2775", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2776",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2777", {}),
                                            },
                                        ),
                                        "PResMaxLatency_U32": (
                                            "V",
                                            "ns=1;i=2778",
                                            {
                                                "Index": ("V", "ns=1;i=2779", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2780",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2781", {}),
                                            },
                                        ),
                                        "PResMode_U8": (
                                            "V",
                                            "ns=1;i=2782",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2981",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2783", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2784",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=2982", {}),
                                                "SubIndex": ("V", "ns=1;i=2785", {}),
                                            },
                                        ),
                                        "PResTimeFirst_U32": (
                                            "V",
                                            "ns=1;i=2786",
                                            {
                                                "Index": ("V", "ns=1;i=2787", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2788",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2789", {}),
                                            },
                                        ),
                                        "PResTimeSecond_U32": (
                                            "V",
                                            "ns=1;i=2790",
                                            {
                                                "Index": ("V", "ns=1;i=2791", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2792",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2793", {}),
                                            },
                                        ),
                                        "Prescaler_U16": (
                                            "V",
                                            "ns=1;i=2794",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2983",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2795", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2796",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=2984", {}),
                                                "SubIndex": ("V", "ns=1;i=2797", {}),
                                            },
                                        ),
                                        "SyncMNDelayFirst_U32": (
                                            "V",
                                            "ns=1;i=2798",
                                            {
                                                "Index": ("V", "ns=1;i=2799", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2800",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2801", {}),
                                            },
                                        ),
                                        "SyncMNDelaySecond_U32": (
                                            "V",
                                            "ns=1;i=2802",
                                            {
                                                "Index": ("V", "ns=1;i=2803", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2804",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2805", {}),
                                            },
                                        ),
                                    },
                                ),
                                "NMT_IsochrSlotAssign_AU8": (
                                    "V",
                                    "ns=1;i=804",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2943", {}),
                                        "Index": ("V", "ns=1;i=805", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=806", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=807", {}),
                                        "Range": ("V", "ns=1;i=2944", {}),
                                    },
                                ),
                                "NMT_MultiplCycleAssign_AU8": (
                                    "V",
                                    "ns=1;i=808",
                                    {
                                        "Index": ("V", "ns=1;i=809", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=810", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=811", {}),
                                    },
                                ),
                                "NMT_NodeAssignment_AU32": (
                                    "V",
                                    "ns=1;i=606",
                                    {
                                        "Index": ("V", "ns=1;i=607", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=608", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=609", {}),
                                    },
                                ),
                                "NMT_PResPayloadLimitList_AU16": (
                                    "V",
                                    "ns=1;i=910",
                                    {
                                        "Index": ("V", "ns=1;i=911", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=912", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=913", {}),
                                    },
                                ),
                                "NMT_RestoreDefParam_REC": (
                                    "V",
                                    "ns=1;i=922",
                                    {
                                        "AllParam_U32": (
                                            "V",
                                            "ns=1;i=923",
                                            {
                                                "Index": ("V", "ns=1;i=924", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=925",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=926", {}),
                                            },
                                        ),
                                        "ApplicationParam_U32": (
                                            "V",
                                            "ns=1;i=2947",
                                            {
                                                "Index": ("V", "ns=1;i=2948", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2949",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2950", {}),
                                            },
                                        ),
                                        "CommunicationParam_U32": (
                                            "V",
                                            "ns=1;i=2951",
                                            {
                                                "Index": ("V", "ns=1;i=2952", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2953",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2954", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=927", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=928", {}),
                                    },
                                ),
                                "NMT_StoreParam_REC": (
                                    "V",
                                    "ns=1;i=943",
                                    {
                                        "AllParam_U32": (
                                            "V",
                                            "ns=1;i=944",
                                            {
                                                "Index": ("V", "ns=1;i=945", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=946",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=947", {}),
                                            },
                                        ),
                                        "ApplicationParam_U32": (
                                            "V",
                                            "ns=1;i=2955",
                                            {
                                                "Index": ("V", "ns=1;i=2956", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2957",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2958", {}),
                                            },
                                        ),
                                        "CommunicationParam_U32": (
                                            "V",
                                            "ns=1;i=2959",
                                            {
                                                "Index": ("V", "ns=1;i=2960", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2961",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2962", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=948", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=949", {}),
                                    },
                                ),
                                "PDL_MnExpAppSwDateList_AU32": (
                                    "V",
                                    "ns=1;i=602",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2968", {}),
                                        "Index": ("V", "ns=1;i=603", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=604", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=605", {}),
                                    },
                                ),
                                "PDL_MnExpAppSwTimeList_AU32": (
                                    "V",
                                    "ns=1;i=598",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2969", {}),
                                        "Index": ("V", "ns=1;i=599", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=600", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=601", {}),
                                    },
                                ),
                                "PDO_RxCommParam_00h_REC": (
                                    "V",
                                    "ns=1;i=964",
                                    {
                                        "Index": ("V", "ns=1;i=973", {}),
                                        "MappingVersion_U8": (
                                            "V",
                                            "ns=1;i=965",
                                            {
                                                "Index": ("V", "ns=1;i=966", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=967",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=968", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=969",
                                            {
                                                "Index": ("V", "ns=1;i=970", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=971",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=972", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=974", {}),
                                    },
                                ),
                                "PDO_RxCommParam_01h_REC": (
                                    "V",
                                    "ns=1;i=975",
                                    {
                                        "Index": ("V", "ns=1;i=984", {}),
                                        "MappingVersion_U8": (
                                            "V",
                                            "ns=1;i=976",
                                            {
                                                "Index": ("V", "ns=1;i=977", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=978",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=979", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=980",
                                            {
                                                "Index": ("V", "ns=1;i=981", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=982",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=983", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=985", {}),
                                    },
                                ),
                                "PDO_RxCommParam_02h_REC": (
                                    "V",
                                    "ns=1;i=986",
                                    {
                                        "Index": ("V", "ns=1;i=995", {}),
                                        "MappingVersion_U8": (
                                            "V",
                                            "ns=1;i=987",
                                            {
                                                "Index": ("V", "ns=1;i=988", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=989",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=990", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=991",
                                            {
                                                "Index": ("V", "ns=1;i=992", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=993",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=994", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=996", {}),
                                    },
                                ),
                                "PDO_RxCommParam_03h_REC": (
                                    "V",
                                    "ns=1;i=997",
                                    {
                                        "Index": ("V", "ns=1;i=1006", {}),
                                        "MappingVersion_U8": (
                                            "V",
                                            "ns=1;i=998",
                                            {
                                                "Index": ("V", "ns=1;i=999", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1000",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1001", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=1002",
                                            {
                                                "Index": ("V", "ns=1;i=1003", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1004",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1005", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=1007", {}),
                                    },
                                ),
                                "PDO_RxMappParam_00h_AU64": (
                                    "V",
                                    "ns=1;i=1008",
                                    {
                                        "Index": ("V", "ns=1;i=1009", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1010", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1011", {}),
                                    },
                                ),
                                "PDO_RxMappParam_01h_AU64": (
                                    "V",
                                    "ns=1;i=1111",
                                    {
                                        "Index": ("V", "ns=1;i=1112", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1113", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1114", {}),
                                    },
                                ),
                                "PDO_RxMappParam_02h_AU64": (
                                    "V",
                                    "ns=1;i=1123",
                                    {
                                        "Index": ("V", "ns=1;i=1124", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1125", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1126", {}),
                                    },
                                ),
                                "PDO_RxMappParam_03h_AU64": (
                                    "V",
                                    "ns=1;i=1127",
                                    {
                                        "Index": ("V", "ns=1;i=1128", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1129", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1130", {}),
                                    },
                                ),
                                "PDO_TxCommParam_00h_REC": (
                                    "V",
                                    "ns=1;i=1147",
                                    {
                                        "Index": ("V", "ns=1;i=1156", {}),
                                        "MappingVersion_U8": (
                                            "V",
                                            "ns=1;i=1148",
                                            {
                                                "Index": ("V", "ns=1;i=1149", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1150",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1151", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=1152",
                                            {
                                                "Index": ("V", "ns=1;i=1153", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1154",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1155", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=1157", {}),
                                    },
                                ),
                                "PDO_TxMappParam_00h_AU64": (
                                    "V",
                                    "ns=1;i=1158",
                                    {
                                        "Index": ("V", "ns=1;i=1159", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1160", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1161", {}),
                                    },
                                ),
                                "SDO_CmdLayerTimeout_U32": (
                                    "V",
                                    "ns=1;i=586",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2971", {}),
                                        "Index": ("V", "ns=1;i=587", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=588", {}),
                                        "Range": ("V", "ns=1;i=2972", {}),
                                        "SubIndex": ("V", "ns=1;i=589", {}),
                                    },
                                ),
                                "SDO_SequLayerNoAck_U32": (
                                    "V",
                                    "ns=1;i=582",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2973", {}),
                                        "Index": ("V", "ns=1;i=583", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=584", {}),
                                        "Range": ("V", "ns=1;i=2974", {}),
                                        "SubIndex": ("V", "ns=1;i=585", {}),
                                    },
                                ),
                                "SDO_SequLayerTimeout_U32": (
                                    "V",
                                    "ns=1;i=578",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2975", {}),
                                        "Index": ("V", "ns=1;i=579", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=580", {}),
                                        "Range": ("V", "ns=1;i=2976", {}),
                                        "SubIndex": ("V", "ns=1;i=581", {}),
                                    },
                                ),
                            },
                        ),
                        "Diagnostics": (
                            "O",
                            "ns=1;i=38",
                            {
                                "DIA_ERRStatistics_REC": (
                                    "V",
                                    "ns=1;i=763",
                                    {
                                        "EmergencyQueueOverflow_U32": (
                                            "V",
                                            "ns=1;i=2288",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2316",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2289", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2290",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2291", {}),
                                            },
                                        ),
                                        "EmergencyQueueWrite_U32": (
                                            "V",
                                            "ns=1;i=2292",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2317",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2293", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2294",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2295", {}),
                                            },
                                        ),
                                        "ExceptionNewEdge_U32": (
                                            "V",
                                            "ns=1;i=2296",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2318",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2297", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2298",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2299", {}),
                                            },
                                        ),
                                        "ExceptionResetEdgePos_U32": (
                                            "V",
                                            "ns=1;i=2300",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2319",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2301", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2302",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2303", {}),
                                            },
                                        ),
                                        "HistoryEntryWrite_U32": (
                                            "V",
                                            "ns=1;i=2304",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2320",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2305", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2306",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2307", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=764", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=765", {}),
                                        "StaticErrorBitFieldChanged_U32": (
                                            "V",
                                            "ns=1;i=2308",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2321",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2309", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2310",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2311", {}),
                                            },
                                        ),
                                        "StatusEntryChanged_U32": (
                                            "V",
                                            "ns=1;i=2312",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2322",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2313", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2314",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2315", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DIA_NMTTelegrCount_REC": (
                                    "V",
                                    "ns=1;i=766",
                                    {
                                        "AsyncRx_U32": (
                                            "V",
                                            "ns=1;i=2353",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2500",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2354", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2383",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2384", {}),
                                            },
                                        ),
                                        "AsyncTx_U32": (
                                            "V",
                                            "ns=1;i=2385",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2501",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2386", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2387",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2388", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=767", {}),
                                        "IsochrCyc_U32": (
                                            "V",
                                            "ns=1;i=2323",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2338",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2324", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2325",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2326", {}),
                                            },
                                        ),
                                        "IsochrRx_U32": (
                                            "V",
                                            "ns=1;i=2389",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2498",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2390", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2391",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2392", {}),
                                            },
                                        ),
                                        "IsochrTx_U32": (
                                            "V",
                                            "ns=1;i=2393",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2499",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2394", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2395",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2396", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=768", {}),
                                        "SdoRx_U32": (
                                            "V",
                                            "ns=1;i=2397",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2502",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2398", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2399",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2400", {}),
                                            },
                                        ),
                                        "SdoTx_U32": (
                                            "V",
                                            "ns=1;i=2401",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2503",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2402", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2403",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2404", {}),
                                            },
                                        ),
                                        "Status_U32": (
                                            "V",
                                            "ns=1;i=2405",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2504",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2406", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2407",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2408", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DLL_CNCRCError_REC": (
                                    "V",
                                    "ns=1;i=1506",
                                    {
                                        "CumulativeCnt_U32": (
                                            "V",
                                            "ns=1;i=1507",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2439",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1508", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1509",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1510", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=1519", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1520", {}),
                                        "ThresholdCnt_U32": (
                                            "V",
                                            "ns=1;i=1515",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2477",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1516", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1517",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1518", {}),
                                            },
                                        ),
                                        "Threshold_U32": (
                                            "V",
                                            "ns=1;i=1511",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2458",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1512", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1513",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1514", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DLL_CNCollision_REC": (
                                    "V",
                                    "ns=1;i=1491",
                                    {
                                        "CumulativeCnt_U32": (
                                            "V",
                                            "ns=1;i=1492",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2438",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1493", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1494",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1495", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=1504", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1505", {}),
                                        "ThresholdCnt_U32": (
                                            "V",
                                            "ns=1;i=1500",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2476",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1501", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1502",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1503", {}),
                                            },
                                        ),
                                        "Threshold_U32": (
                                            "V",
                                            "ns=1;i=1496",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2457",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1497", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1498",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1499", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DLL_CNLossOfLinkCum_U32": (
                                    "V",
                                    "ns=1;i=1581",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2977", {}),
                                        "Index": ("V", "ns=1;i=1582", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1583", {}),
                                        "SubIndex": ("V", "ns=1;i=1584", {}),
                                    },
                                ),
                                "DLL_CNLossOfSocTolerance_U32": (
                                    "V",
                                    "ns=1;i=1679",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2979", {}),
                                        "Index": ("V", "ns=1;i=1680", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1681", {}),
                                        "SubIndex": ("V", "ns=1;i=1682", {}),
                                    },
                                ),
                                "DLL_CNLossPReq_REC": (
                                    "V",
                                    "ns=1;i=1521",
                                    {
                                        "CumulativeCnt_U32": (
                                            "V",
                                            "ns=1;i=1522",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2440",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1523", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1524",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1525", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=1534", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1535", {}),
                                        "ThresholdCnt_U32": (
                                            "V",
                                            "ns=1;i=1530",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2478",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1531", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1532",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1533", {}),
                                            },
                                        ),
                                        "Threshold_U32": (
                                            "V",
                                            "ns=1;i=1526",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2459",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1527", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1528",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1529", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DLL_CNLossSoA_REC": (
                                    "V",
                                    "ns=1;i=1536",
                                    {
                                        "CumulativeCnt_U32": (
                                            "V",
                                            "ns=1;i=1537",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2441",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1538", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1539",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1540", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=1549", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1550", {}),
                                        "ThresholdCnt_U32": (
                                            "V",
                                            "ns=1;i=1545",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2479",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1546", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1547",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1548", {}),
                                            },
                                        ),
                                        "Threshold_U32": (
                                            "V",
                                            "ns=1;i=1541",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2460",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1542", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1543",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1544", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DLL_CNLossSoC_REC": (
                                    "V",
                                    "ns=1;i=1551",
                                    {
                                        "CumulativeCnt_U32": (
                                            "V",
                                            "ns=1;i=1552",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2442",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1553", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1554",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1555", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=1564", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1565", {}),
                                        "ThresholdCnt_U32": (
                                            "V",
                                            "ns=1;i=1560",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2480",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1561", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1562",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1563", {}),
                                            },
                                        ),
                                        "Threshold_U32": (
                                            "V",
                                            "ns=1;i=1556",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2461",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1557", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1558",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1559", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DLL_CNSoCJitter_REC": (
                                    "V",
                                    "ns=1;i=1566",
                                    {
                                        "CumulativeCnt_U32": (
                                            "V",
                                            "ns=1;i=1567",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2443",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1568", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1569",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1570", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=1579", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1580", {}),
                                        "ThresholdCnt_U32": (
                                            "V",
                                            "ns=1;i=1575",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2481",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1576", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1577",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1578", {}),
                                            },
                                        ),
                                        "Threshold_U32": (
                                            "V",
                                            "ns=1;i=1571",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2462",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1572", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1573",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1574", {}),
                                            },
                                        ),
                                    },
                                ),
                                "ERR_ErrorRegister_U8": (
                                    "V",
                                    "ns=1;i=769",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2513", {}),
                                        "Index": ("V", "ns=1;i=770", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=771", {}),
                                        "SubIndex": ("V", "ns=1;i=772", {}),
                                    },
                                ),
                                "ERR_History_ADOM": (
                                    "V",
                                    "ns=1;i=773",
                                    {
                                        "Index": ("V", "ns=1;i=774", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=775", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=776", {}),
                                    },
                                ),
                                "PDO_ErrMapVers_OSTR": (
                                    "V",
                                    "ns=1;i=777",
                                    {
                                        "Index": ("V", "ns=1;i=778", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=779", {}),
                                        "SubIndex": ("V", "ns=1;i=780", {}),
                                    },
                                ),
                                "PDO_ErrShort_RX_OSTR": (
                                    "V",
                                    "ns=1;i=781",
                                    {
                                        "Index": ("V", "ns=1;i=782", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=783", {}),
                                        "SubIndex": ("V", "ns=1;i=784", {}),
                                    },
                                ),
                            },
                        ),
                        "ParameterSet": (
                            "O",
                            "ns=1;i=55",
                            {
                                "ERR_ErrorRegister_U8": (
                                    "V",
                                    "ns=1;i=1383",
                                    {
                                        "Index": ("V", "ns=1;i=1384", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1385", {}),
                                        "SubIndex": ("V", "ns=1;i=1386", {}),
                                    },
                                ),
                                "NMT_CurrNMTState_U8": (
                                    "V",
                                    "ns=1;i=1387",
                                    {
                                        "Index": ("V", "ns=1;i=1388", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1389", {}),
                                        "SubIndex": ("V", "ns=1;i=1390", {}),
                                    },
                                ),
                                "NMT_CycleLen_U32": (
                                    "V",
                                    "ns=1;i=1391",
                                    {
                                        "Index": ("V", "ns=1;i=1392", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1393", {}),
                                        "SubIndex": ("V", "ns=1;i=1394", {}),
                                    },
                                ),
                                "NMT_CycleTiming_REC": (
                                    "V",
                                    "ns=1;i=1395",
                                    {
                                        "ASndMaxLatency_U32": (
                                            "V",
                                            "ns=1;i=2985",
                                            {
                                                "Index": ("V", "ns=1;i=2986", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2987",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2988", {}),
                                            },
                                        ),
                                        "AsyncMTU_U16": (
                                            "V",
                                            "ns=1;i=1396",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2754",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1397", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1398",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=2755", {}),
                                                "SubIndex": ("V", "ns=1;i=1399", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=1400", {}),
                                        "IsochrRxMaxPayload_U16": (
                                            "V",
                                            "ns=1;i=1401",
                                            {
                                                "Index": ("V", "ns=1;i=1402", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1403",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=2744", {}),
                                                "SubIndex": ("V", "ns=1;i=1404", {}),
                                            },
                                        ),
                                        "IsochrTxMaxPayload_U16": (
                                            "V",
                                            "ns=1;i=1405",
                                            {
                                                "Index": ("V", "ns=1;i=1406", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1407",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=2738", {}),
                                                "SubIndex": ("V", "ns=1;i=1408", {}),
                                            },
                                        ),
                                        "LeaseTime_U32": (
                                            "V",
                                            "ns=1;i=2989",
                                            {
                                                "Index": ("V", "ns=1;i=2990", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2991",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2992", {}),
                                            },
                                        ),
                                        "MultiplCycleCnt_U8": (
                                            "V",
                                            "ns=1;i=1409",
                                            {
                                                "Index": ("V", "ns=1;i=1410", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1411",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1412", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=1413", {}),
                                        "PReqActPayloadLimit_U16": (
                                            "V",
                                            "ns=1;i=2993",
                                            {
                                                "Index": ("V", "ns=1;i=2994", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2995",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2996", {}),
                                            },
                                        ),
                                        "PResActPayloadLimit_U16": (
                                            "V",
                                            "ns=1;i=2997",
                                            {
                                                "Index": ("V", "ns=1;i=2998", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2999",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3000", {}),
                                            },
                                        ),
                                        "PResMaxLatency_U32": (
                                            "V",
                                            "ns=1;i=3001",
                                            {
                                                "Index": ("V", "ns=1;i=3002", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3003",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3004", {}),
                                            },
                                        ),
                                        "PResMode_U8": (
                                            "V",
                                            "ns=1;i=3005",
                                            {
                                                "Index": ("V", "ns=1;i=3006", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3007",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3008", {}),
                                            },
                                        ),
                                        "PResTimeFirst_U32": (
                                            "V",
                                            "ns=1;i=3009",
                                            {
                                                "Index": ("V", "ns=1;i=3010", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3011",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3012", {}),
                                            },
                                        ),
                                        "PResTimeSecond_U32": (
                                            "V",
                                            "ns=1;i=3013",
                                            {
                                                "Index": ("V", "ns=1;i=3014", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3015",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3016", {}),
                                            },
                                        ),
                                        "Prescaler_U16": (
                                            "V",
                                            "ns=1;i=3017",
                                            {
                                                "Index": ("V", "ns=1;i=3018", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3019",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3020", {}),
                                            },
                                        ),
                                        "SyncMNDelayFirst_U32": (
                                            "V",
                                            "ns=1;i=3021",
                                            {
                                                "Index": ("V", "ns=1;i=3022", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3023",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3024", {}),
                                            },
                                        ),
                                        "SyncMNDelaySecond_U32": (
                                            "V",
                                            "ns=1;i=3025",
                                            {
                                                "Index": ("V", "ns=1;i=3026", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3027",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3028", {}),
                                            },
                                        ),
                                    },
                                ),
                                "NMT_DeviceType_U32": (
                                    "V",
                                    "ns=1;i=1414",
                                    {
                                        "Index": ("V", "ns=1;i=1415", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1416", {}),
                                        "SubIndex": ("V", "ns=1;i=1417", {}),
                                    },
                                ),
                                "NMT_EPLNodeID_REC": (
                                    "V",
                                    "ns=1;i=1418",
                                    {
                                        "Index": ("V", "ns=1;i=1419", {}),
                                        "NodeIDByHW_BOOL": (
                                            "V",
                                            "ns=1;i=1424",
                                            {
                                                "Index": ("V", "ns=1;i=1425", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1426",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1427", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=1420",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2904",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1421", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1422",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1423", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=1428", {}),
                                        "SWNodeID_U8": (
                                            "V",
                                            "ns=1;i=3029",
                                            {
                                                "Index": ("V", "ns=1;i=3030", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3031",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3032", {}),
                                            },
                                        ),
                                    },
                                ),
                                "NMT_EPLVersion_U8": (
                                    "V",
                                    "ns=1;i=1429",
                                    {
                                        "Index": ("V", "ns=1;i=1430", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1431", {}),
                                        "SubIndex": ("V", "ns=1;i=1432", {}),
                                    },
                                ),
                                "NMT_FeatureFlags_U32": (
                                    "V",
                                    "ns=1;i=1433",
                                    {
                                        "Index": ("V", "ns=1;i=1434", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1435", {}),
                                        "SubIndex": ("V", "ns=1;i=1436", {}),
                                    },
                                ),
                                "NMT_IdentityObject_REC": (
                                    "V",
                                    "ns=1;i=1437",
                                    {
                                        "Index": ("V", "ns=1;i=1438", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1439", {}),
                                        "ProductCode_U32": (
                                            "V",
                                            "ns=1;i=3033",
                                            {
                                                "Index": ("V", "ns=1;i=3034", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3035",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3036", {}),
                                            },
                                        ),
                                        "RevisionNo_U32": (
                                            "V",
                                            "ns=1;i=3037",
                                            {
                                                "Index": ("V", "ns=1;i=3038", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3039",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3040", {}),
                                            },
                                        ),
                                        "SerialNo_U32": (
                                            "V",
                                            "ns=1;i=3041",
                                            {
                                                "Index": ("V", "ns=1;i=3042", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3043",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3044", {}),
                                            },
                                        ),
                                        "VendorId_U32": (
                                            "V",
                                            "ns=1;i=1440",
                                            {
                                                "Index": ("V", "ns=1;i=1441", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1442",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1443", {}),
                                            },
                                        ),
                                    },
                                ),
                                "NMT_InterfaceGroup_0h_REC": (
                                    "V",
                                    "ns=1;i=1444",
                                    {
                                        "Index": ("V", "ns=1;i=1445", {}),
                                        "InterfaceAdminState_U8": (
                                            "V",
                                            "ns=1;i=1446",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3181",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1447", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1448",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=3182", {}),
                                                "SubIndex": ("V", "ns=1;i=1449", {}),
                                            },
                                        ),
                                        "InterfaceDescription_VSTR": (
                                            "V",
                                            "ns=1;i=1450",
                                            {
                                                "Index": ("V", "ns=1;i=1451", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1452",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1453", {}),
                                            },
                                        ),
                                        "InterfaceIndex_U16": (
                                            "V",
                                            "ns=1;i=1454",
                                            {
                                                "Index": ("V", "ns=1;i=1455", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1456",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=2921", {}),
                                                "SubIndex": ("V", "ns=1;i=1457", {}),
                                            },
                                        ),
                                        "InterfaceMtu_U16": (
                                            "V",
                                            "ns=1;i=1458",
                                            {
                                                "Index": ("V", "ns=1;i=1459", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1460",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1461", {}),
                                            },
                                        ),
                                        "InterfaceName_VSTR": (
                                            "V",
                                            "ns=1;i=1462",
                                            {
                                                "Index": ("V", "ns=1;i=1463", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1464",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1465", {}),
                                            },
                                        ),
                                        "InterfaceOperStatus_U8": (
                                            "V",
                                            "ns=1;i=1466",
                                            {
                                                "Index": ("V", "ns=1;i=1467", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1468",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=2939", {}),
                                                "SubIndex": ("V", "ns=1;i=1469", {}),
                                            },
                                        ),
                                        "InterfacePhysAddress_OSTR": (
                                            "V",
                                            "ns=1;i=1470",
                                            {
                                                "Index": ("V", "ns=1;i=1471", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1472",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1473", {}),
                                            },
                                        ),
                                        "InterfaceType_U8": (
                                            "V",
                                            "ns=1;i=1474",
                                            {
                                                "Index": ("V", "ns=1;i=1475", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1476",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1477", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=1478", {}),
                                        "PortEnableMask_U64": (
                                            "V",
                                            "ns=1;i=2931",
                                            {
                                                "Index": ("V", "ns=1;i=2932", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3045",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3046", {}),
                                            },
                                        ),
                                        "Valid_BOOL": (
                                            "V",
                                            "ns=1;i=1479",
                                            {
                                                "Index": ("V", "ns=1;i=1480", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1481",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1482", {}),
                                            },
                                        ),
                                    },
                                ),
                                "NMT_ResetCmd_U8": (
                                    "V",
                                    "ns=1;i=1483",
                                    {
                                        "Index": ("V", "ns=1;i=1484", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1485", {}),
                                        "SubIndex": ("V", "ns=1;i=1486", {}),
                                    },
                                ),
                                "SDO_SequLayerTimeout_U32": (
                                    "V",
                                    "ns=1;i=1487",
                                    {
                                        "Index": ("V", "ns=1;i=1488", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1489", {}),
                                        "SubIndex": ("V", "ns=1;i=1490", {}),
                                    },
                                ),
                            },
                        ),
                    },
                ),
                "PowerlinkMnConnectionPointType": (
                    "OT",
                    "ns=1;i=5",
                    {
                        "Configuration": (
                            "O",
                            "ns=1;i=42",
                            {
                                "CFM_ExpConfDateList_AU32": (
                                    "V",
                                    "ns=1;i=2027",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3051", {}),
                                        "Index": ("V", "ns=1;i=2028", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2029", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2030", {}),
                                    },
                                ),
                                "CFM_ExpConfIdList_AU32": (
                                    "V",
                                    "ns=1;i=2031",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3053", {}),
                                        "Index": ("V", "ns=1;i=2032", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2033", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2034", {}),
                                    },
                                ),
                                "CFM_ExpConfTimeList_AU32": (
                                    "V",
                                    "ns=1;i=2035",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3055", {}),
                                        "Index": ("V", "ns=1;i=2036", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2037", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2038", {}),
                                    },
                                ),
                                "DLL_MNCycleSuspendNumber_U32": (
                                    "V",
                                    "ns=1;i=2067",
                                    {
                                        "Index": ("V", "ns=1;i=2068", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2069", {}),
                                        "SubIndex": ("V", "ns=1;i=2070", {}),
                                    },
                                ),
                                "NMT_BootTime_REC": (
                                    "V",
                                    "ns=1;i=2115",
                                    {
                                        "Index": ("V", "ns=1;i=2132", {}),
                                        "MNConfigurationTimeout_U32": (
                                            "V",
                                            "ns=1;i=2661",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3087",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2662", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2663",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2664", {}),
                                            },
                                        ),
                                        "MNIdentificationTimeout_U32": (
                                            "V",
                                            "ns=1;i=2665",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3089",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2666", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2667",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2668", {}),
                                            },
                                        ),
                                        "MNSoftwareTimeout_U32": (
                                            "V",
                                            "ns=1;i=2669",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3090",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2670", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2671",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2672", {}),
                                            },
                                        ),
                                        "MNStartCNTimeout_U32": (
                                            "V",
                                            "ns=1;i=2673",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3091",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2674", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2675",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2676", {}),
                                            },
                                        ),
                                        "MNSwitchOverCycleDivider_U32": (
                                            "V",
                                            "ns=1;i=2677",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3092",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2678", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2679",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2680", {}),
                                            },
                                        ),
                                        "MNSwitchOverDelay_U32": (
                                            "V",
                                            "ns=1;i=2681",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3093",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2682", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2683",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2684", {}),
                                            },
                                        ),
                                        "MNSwitchOverPriority_U32": (
                                            "V",
                                            "ns=1;i=2685",
                                            {
                                                "Index": ("V", "ns=1;i=2686", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2687",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2688", {}),
                                            },
                                        ),
                                        "MNTimeoutPreOp1_U32": (
                                            "V",
                                            "ns=1;i=2116",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2640",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2117", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2118",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=2641", {}),
                                                "SubIndex": ("V", "ns=1;i=2119", {}),
                                            },
                                        ),
                                        "MNTimeoutPreOp2_U32": (
                                            "V",
                                            "ns=1;i=2120",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2646",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2121", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2122",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2123", {}),
                                            },
                                        ),
                                        "MNTimeoutReadyToOp_U32": (
                                            "V",
                                            "ns=1;i=2124",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2651",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2125", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2126",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=2652", {}),
                                                "SubIndex": ("V", "ns=1;i=2127", {}),
                                            },
                                        ),
                                        "MNWaitNotAct_U32": (
                                            "V",
                                            "ns=1;i=2128",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2634",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2129", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2130",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=2635", {}),
                                                "SubIndex": ("V", "ns=1;i=2131", {}),
                                            },
                                        ),
                                        "MNWaitPreOp1_U32": (
                                            "V",
                                            "ns=1;i=2689",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3094",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2690", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2691",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=3095", {}),
                                                "SubIndex": ("V", "ns=1;i=2692", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=2133", {}),
                                    },
                                ),
                                "NMT_MNCNPResTimeout_AU32": (
                                    "V",
                                    "ns=1;i=2039",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3183", {}),
                                        "Index": ("V", "ns=1;i=2040", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2041", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2042", {}),
                                    },
                                ),
                                "NMT_MNCycleTiming_REC": (
                                    "V",
                                    "ns=1;i=2134",
                                    {
                                        "ASndMaxNumber": (
                                            "V",
                                            "ns=1;i=3185",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3222",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=3186", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3187",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=3223", {}),
                                                "SubIndex": ("V", "ns=1;i=3188", {}),
                                            },
                                        ),
                                        "AsyncSlotTimeout_U32": (
                                            "V",
                                            "ns=1;i=3189",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3216",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=3190", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3191",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=3217", {}),
                                                "SubIndex": ("V", "ns=1;i=3192", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=2139", {}),
                                        "MinRedCycleTime_U32": (
                                            "V",
                                            "ns=1;i=3193",
                                            {
                                                "Index": ("V", "ns=1;i=3194", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3195",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3196", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=2140", {}),
                                        "WaitSoCPReq_U32": (
                                            "V",
                                            "ns=1;i=2135",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3212",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2136", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2137",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2138", {}),
                                            },
                                        ),
                                    },
                                ),
                                "NMT_MNDeviceTypeIdList_AU32": (
                                    "V",
                                    "ns=1;i=2043",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3226", {}),
                                        "Index": ("V", "ns=1;i=2044", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2045", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2046", {}),
                                    },
                                ),
                                "NMT_MNProductCodeList_AU32": (
                                    "V",
                                    "ns=1;i=2051",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3236", {}),
                                        "Index": ("V", "ns=1;i=2052", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2053", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2054", {}),
                                    },
                                ),
                                "NMT_MNRevisionNoList_AU32": (
                                    "V",
                                    "ns=1;i=2055",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3238", {}),
                                        "Index": ("V", "ns=1;i=2056", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2057", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2058", {}),
                                    },
                                ),
                                "NMT_MNSerialNoList_AU32": (
                                    "V",
                                    "ns=1;i=2059",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3240", {}),
                                        "Index": ("V", "ns=1;i=2060", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2061", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2062", {}),
                                    },
                                ),
                                "NMT_MNVendorIdList_AU32": (
                                    "V",
                                    "ns=1;i=2063",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3242", {}),
                                        "Index": ("V", "ns=1;i=2064", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2065", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2066", {}),
                                    },
                                ),
                                "NMT_StartUp_U32": (
                                    "V",
                                    "ns=1;i=2148",
                                    {
                                        "Index": ("V", "ns=1;i=2149", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2150", {}),
                                        "SubIndex": ("V", "ns=1;i=2151", {}),
                                    },
                                ),
                                "PDO_TxCommParam_01h_REC": (
                                    "V",
                                    "ns=1;i=2152",
                                    {
                                        "Index": ("V", "ns=1;i=2180", {}),
                                        "MappingVersion_U8": (
                                            "V",
                                            "ns=1;i=2172",
                                            {
                                                "Index": ("V", "ns=1;i=2173", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2174",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2175", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=2176",
                                            {
                                                "Index": ("V", "ns=1;i=2177", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2178",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2179", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=2181", {}),
                                    },
                                ),
                                "PDO_TxCommParam_02h_REC": (
                                    "V",
                                    "ns=1;i=2182",
                                    {
                                        "Index": ("V", "ns=1;i=2207", {}),
                                        "MappingVersion_U8": (
                                            "V",
                                            "ns=1;i=2183",
                                            {
                                                "Index": ("V", "ns=1;i=2184", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2185",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2186", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=2187",
                                            {
                                                "Index": ("V", "ns=1;i=2188", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2189",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2190", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=2208", {}),
                                    },
                                ),
                                "PDO_TxCommParam_03h_REC": (
                                    "V",
                                    "ns=1;i=2209",
                                    {
                                        "Index": ("V", "ns=1;i=2218", {}),
                                        "MappingVersion_U8": (
                                            "V",
                                            "ns=1;i=2210",
                                            {
                                                "Index": ("V", "ns=1;i=2211", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2212",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2213", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=2214",
                                            {
                                                "Index": ("V", "ns=1;i=2215", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2216",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2217", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=2219", {}),
                                    },
                                ),
                                "PDO_TxMappParam_01h_AU64": (
                                    "V",
                                    "ns=1;i=2220",
                                    {
                                        "Index": ("V", "ns=1;i=2221", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2222", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2223", {}),
                                    },
                                ),
                                "PDO_TxMappParam_02h_AU64": (
                                    "V",
                                    "ns=1;i=2265",
                                    {
                                        "Index": ("V", "ns=1;i=2266", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2267", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2268", {}),
                                    },
                                ),
                                "PDO_TxMappParam_03h_AU64": (
                                    "V",
                                    "ns=1;i=2269",
                                    {
                                        "Index": ("V", "ns=1;i=2270", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2271", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2272", {}),
                                    },
                                ),
                            },
                        ),
                        "Diagnostics": (
                            "O",
                            "ns=1;i=39",
                            {
                                "DLL_MNCNLatePResCumCnt_AU32": (
                                    "V",
                                    "ns=1;i=1811",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3057", {}),
                                        "Index": ("V", "ns=1;i=1812", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1813", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1814", {}),
                                    },
                                ),
                                "DLL_MNCNLatePResThrCnt_AU32": (
                                    "V",
                                    "ns=1;i=1815",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3059", {}),
                                        "Index": ("V", "ns=1;i=1816", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1817", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1818", {}),
                                    },
                                ),
                                "DLL_MNCNLatePResThreshold_AU32": (
                                    "V",
                                    "ns=1;i=1819",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3061", {}),
                                        "Index": ("V", "ns=1;i=1820", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1821", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1822", {}),
                                    },
                                ),
                                "DLL_MNCNLossPResCumCnt_AU32": (
                                    "V",
                                    "ns=1;i=1823",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3063", {}),
                                        "Index": ("V", "ns=1;i=1824", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1825", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1826", {}),
                                    },
                                ),
                                "DLL_MNCNLossPResThrCnt_AU32": (
                                    "V",
                                    "ns=1;i=1827",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3065", {}),
                                        "Index": ("V", "ns=1;i=1828", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1829", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1830", {}),
                                    },
                                ),
                                "DLL_MNCNLossPResThreshold_AU32": (
                                    "V",
                                    "ns=1;i=1831",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3067", {}),
                                        "Index": ("V", "ns=1;i=1832", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1833", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1834", {}),
                                    },
                                ),
                                "DLL_MNCRCError_REC": (
                                    "V",
                                    "ns=1;i=1874",
                                    {
                                        "CumulativeCnt_U32": (
                                            "V",
                                            "ns=1;i=1875",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2451",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1876", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1877",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1878", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=1887", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1888", {}),
                                        "ThresholdCnt_U32": (
                                            "V",
                                            "ns=1;i=1883",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2489",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1884", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1885",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1886", {}),
                                            },
                                        ),
                                        "Threshold_U32": (
                                            "V",
                                            "ns=1;i=1879",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2470",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1880", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1881",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1882", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DLL_MNCollision_REC": (
                                    "V",
                                    "ns=1;i=1859",
                                    {
                                        "CumulativeCnt_U32": (
                                            "V",
                                            "ns=1;i=1860",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2450",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1861", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1862",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1863", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=1872", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1873", {}),
                                        "ThresholdCnt_U32": (
                                            "V",
                                            "ns=1;i=1868",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2488",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1869", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1870",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1871", {}),
                                            },
                                        ),
                                        "Threshold_U32": (
                                            "V",
                                            "ns=1;i=1864",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2469",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1865", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1866",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1867", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DLL_MNCycTimeExceed_REC": (
                                    "V",
                                    "ns=1;i=1889",
                                    {
                                        "CumulativeCnt_U32": (
                                            "V",
                                            "ns=1;i=1890",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2452",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1891", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1892",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1893", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=1902", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1903", {}),
                                        "ThresholdCnt_U32": (
                                            "V",
                                            "ns=1;i=1898",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2490",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1899", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1900",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1901", {}),
                                            },
                                        ),
                                        "Threshold_U32": (
                                            "V",
                                            "ns=1;i=1894",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2471",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1895", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1896",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1897", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DLL_MNLossOfLinkCum_U32": (
                                    "V",
                                    "ns=1;i=1949",
                                    {
                                        "Index": ("V", "ns=1;i=1950", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1951", {}),
                                        "SubIndex": ("V", "ns=1;i=1952", {}),
                                    },
                                ),
                                "DLL_MNLossStatusResCumCnt_AU32": (
                                    "V",
                                    "ns=1;i=1953",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3080", {}),
                                        "Index": ("V", "ns=1;i=1954", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1955", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1956", {}),
                                    },
                                ),
                                "DLL_MNLossStatusResThrCnt_AU32": (
                                    "V",
                                    "ns=1;i=1957",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3082", {}),
                                        "Index": ("V", "ns=1;i=1958", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1959", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1960", {}),
                                    },
                                ),
                                "DLL_MNLossStatusResThreshold_AU32": (
                                    "V",
                                    "ns=1;i=1961",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3084", {}),
                                        "Index": ("V", "ns=1;i=1962", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1963", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1964", {}),
                                    },
                                ),
                                "NMT_MNNodeCurrState_AU8": (
                                    "V",
                                    "ns=1;i=1965",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3228", {}),
                                        "Index": ("V", "ns=1;i=1966", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1967", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1968", {}),
                                    },
                                ),
                                "NMT_MNNodeExpState_AU8": (
                                    "V",
                                    "ns=1;i=1969",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3230", {}),
                                        "Index": ("V", "ns=1;i=1970", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1971", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1972", {}),
                                    },
                                ),
                                "NMT_RequestCmd_REC": (
                                    "V",
                                    "ns=1;i=1997",
                                    {
                                        "CmdData_DOM": (
                                            "V",
                                            "ns=1;i=3244",
                                            {
                                                "Index": ("V", "ns=1;i=3245", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3246",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3247", {}),
                                            },
                                        ),
                                        "CmdID_U8": (
                                            "V",
                                            "ns=1;i=1998",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3072",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1999", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2000",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2001", {}),
                                            },
                                        ),
                                        "CmdTarget_U8": (
                                            "V",
                                            "ns=1;i=2002",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3075",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2003", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2004",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2005", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=2010", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2011", {}),
                                        "Release_BOOL": (
                                            "V",
                                            "ns=1;i=2006",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3078",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2007", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2008",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2009", {}),
                                            },
                                        ),
                                    },
                                ),
                            },
                        ),
                        "ParameterSet": (
                            "O",
                            "ns=1;i=56",
                            {
                                "ERR_ErrorRegister_U8": (
                                    "V",
                                    "ns=1;i=1703",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3086", {}),
                                        "Index": ("V", "ns=1;i=1704", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1705", {}),
                                        "SubIndex": ("V", "ns=1;i=1706", {}),
                                    },
                                ),
                                "NMT_CurrNMTState_U8": (
                                    "V",
                                    "ns=1;i=1707",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3103", {}),
                                        "Index": ("V", "ns=1;i=1708", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1709", {}),
                                        "SubIndex": ("V", "ns=1;i=1710", {}),
                                    },
                                ),
                                "NMT_CycleLen_U32": (
                                    "V",
                                    "ns=1;i=1711",
                                    {
                                        "Index": ("V", "ns=1;i=1712", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1713", {}),
                                        "SubIndex": ("V", "ns=1;i=1714", {}),
                                    },
                                ),
                                "NMT_CycleTiming_REC": (
                                    "V",
                                    "ns=1;i=1715",
                                    {
                                        "ASndMaxLatency_U32": (
                                            "V",
                                            "ns=1;i=3104",
                                            {
                                                "Index": ("V", "ns=1;i=3105", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3106",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3107", {}),
                                            },
                                        ),
                                        "AsyncMTU_U16": (
                                            "V",
                                            "ns=1;i=1716",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2756",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1717", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1718",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=2757", {}),
                                                "SubIndex": ("V", "ns=1;i=1719", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=1720", {}),
                                        "IsochrRxMaxPayload_U16": (
                                            "V",
                                            "ns=1;i=1721",
                                            {
                                                "Index": ("V", "ns=1;i=1722", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1723",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=2745", {}),
                                                "SubIndex": ("V", "ns=1;i=1724", {}),
                                            },
                                        ),
                                        "IsochrTxMaxPayload_U16": (
                                            "V",
                                            "ns=1;i=1725",
                                            {
                                                "Index": ("V", "ns=1;i=1726", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1727",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=2739", {}),
                                                "SubIndex": ("V", "ns=1;i=1728", {}),
                                            },
                                        ),
                                        "LeaseTime_U32": (
                                            "V",
                                            "ns=1;i=3108",
                                            {
                                                "Index": ("V", "ns=1;i=3109", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3110",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3111", {}),
                                            },
                                        ),
                                        "MultiplCycleCnt_U8": (
                                            "V",
                                            "ns=1;i=1729",
                                            {
                                                "Index": ("V", "ns=1;i=1730", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1731",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1732", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=1733", {}),
                                        "PReqActPayloadLimit_U16": (
                                            "V",
                                            "ns=1;i=3112",
                                            {
                                                "Index": ("V", "ns=1;i=3113", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3114",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3115", {}),
                                            },
                                        ),
                                        "PResActPayloadLimit_U16": (
                                            "V",
                                            "ns=1;i=3116",
                                            {
                                                "Index": ("V", "ns=1;i=3117", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3118",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3119", {}),
                                            },
                                        ),
                                        "PResMaxLatency_U32": (
                                            "V",
                                            "ns=1;i=3120",
                                            {
                                                "Index": ("V", "ns=1;i=3121", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3122",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3123", {}),
                                            },
                                        ),
                                        "PResMode_U8": (
                                            "V",
                                            "ns=1;i=3124",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3148",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=3125", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3126",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=3149", {}),
                                                "SubIndex": ("V", "ns=1;i=3127", {}),
                                            },
                                        ),
                                        "PResTimeFirst_U32": (
                                            "V",
                                            "ns=1;i=3128",
                                            {
                                                "Index": ("V", "ns=1;i=3129", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3130",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3131", {}),
                                            },
                                        ),
                                        "PResTimeSecond_U32": (
                                            "V",
                                            "ns=1;i=3132",
                                            {
                                                "Index": ("V", "ns=1;i=3133", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3134",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3135", {}),
                                            },
                                        ),
                                        "Prescaler_U16": (
                                            "V",
                                            "ns=1;i=3136",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3150",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=3137", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3138",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=3151", {}),
                                                "SubIndex": ("V", "ns=1;i=3139", {}),
                                            },
                                        ),
                                        "SyncMNDelayFirst_U32": (
                                            "V",
                                            "ns=1;i=3140",
                                            {
                                                "Index": ("V", "ns=1;i=3141", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3142",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3143", {}),
                                            },
                                        ),
                                        "SyncMNDelaySecond_U32": (
                                            "V",
                                            "ns=1;i=3144",
                                            {
                                                "Index": ("V", "ns=1;i=3145", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3146",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3147", {}),
                                            },
                                        ),
                                    },
                                ),
                                "NMT_DeviceType_U32": (
                                    "V",
                                    "ns=1;i=1734",
                                    {
                                        "Index": ("V", "ns=1;i=1735", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1736", {}),
                                        "SubIndex": ("V", "ns=1;i=1737", {}),
                                    },
                                ),
                                "NMT_EPLNodeID_REC": (
                                    "V",
                                    "ns=1;i=1738",
                                    {
                                        "Index": ("V", "ns=1;i=1739", {}),
                                        "NodeIDByHW_BOOL": (
                                            "V",
                                            "ns=1;i=1744",
                                            {
                                                "Index": ("V", "ns=1;i=1745", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1746",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1747", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=1740",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2905",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1741", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1742",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1743", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=1748", {}),
                                        "SWNodeID_U8": (
                                            "V",
                                            "ns=1;i=3156",
                                            {
                                                "Index": ("V", "ns=1;i=3157", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3158",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3159", {}),
                                            },
                                        ),
                                    },
                                ),
                                "NMT_EPLVersion_U8": (
                                    "V",
                                    "ns=1;i=1749",
                                    {
                                        "Index": ("V", "ns=1;i=1750", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1751", {}),
                                        "SubIndex": ("V", "ns=1;i=1752", {}),
                                    },
                                ),
                                "NMT_FeatureFlags_U32": (
                                    "V",
                                    "ns=1;i=1753",
                                    {
                                        "Index": ("V", "ns=1;i=1754", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1755", {}),
                                        "SubIndex": ("V", "ns=1;i=1756", {}),
                                    },
                                ),
                                "NMT_IdentityObject_REC": (
                                    "V",
                                    "ns=1;i=1757",
                                    {
                                        "Index": ("V", "ns=1;i=1758", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1759", {}),
                                        "ProductCode_U32": (
                                            "V",
                                            "ns=1;i=3160",
                                            {
                                                "Index": ("V", "ns=1;i=3161", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3162",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3163", {}),
                                            },
                                        ),
                                        "RevisionNo_U32": (
                                            "V",
                                            "ns=1;i=3164",
                                            {
                                                "Index": ("V", "ns=1;i=3165", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3166",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3167", {}),
                                            },
                                        ),
                                        "SerialNo_U32": (
                                            "V",
                                            "ns=1;i=3168",
                                            {
                                                "Index": ("V", "ns=1;i=3169", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3170",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3171", {}),
                                            },
                                        ),
                                        "VendorId_U32": (
                                            "V",
                                            "ns=1;i=1760",
                                            {
                                                "Index": ("V", "ns=1;i=1761", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1762",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1763", {}),
                                            },
                                        ),
                                    },
                                ),
                                "NMT_InterfaceGroup_0h_REC": (
                                    "V",
                                    "ns=1;i=1764",
                                    {
                                        "Index": ("V", "ns=1;i=1765", {}),
                                        "InterfaceAdminState_U8": (
                                            "V",
                                            "ns=1;i=1766",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2933",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1767", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1768",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=2934", {}),
                                                "SubIndex": ("V", "ns=1;i=1769", {}),
                                            },
                                        ),
                                        "InterfaceDescription_VSTR": (
                                            "V",
                                            "ns=1;i=1770",
                                            {
                                                "Index": ("V", "ns=1;i=1771", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1772",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1773", {}),
                                            },
                                        ),
                                        "InterfaceIndex_U16": (
                                            "V",
                                            "ns=1;i=1774",
                                            {
                                                "Index": ("V", "ns=1;i=1775", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1776",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=2922", {}),
                                                "SubIndex": ("V", "ns=1;i=1777", {}),
                                            },
                                        ),
                                        "InterfaceMtu_U16": (
                                            "V",
                                            "ns=1;i=1778",
                                            {
                                                "Index": ("V", "ns=1;i=1779", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1780",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1781", {}),
                                            },
                                        ),
                                        "InterfaceName_VSTR": (
                                            "V",
                                            "ns=1;i=1782",
                                            {
                                                "Index": ("V", "ns=1;i=1783", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1784",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1785", {}),
                                            },
                                        ),
                                        "InterfaceOperStatus_U8": (
                                            "V",
                                            "ns=1;i=1786",
                                            {
                                                "Index": ("V", "ns=1;i=1787", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1788",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=2940", {}),
                                                "SubIndex": ("V", "ns=1;i=1789", {}),
                                            },
                                        ),
                                        "InterfacePhysAddress_OSTR": (
                                            "V",
                                            "ns=1;i=1790",
                                            {
                                                "Index": ("V", "ns=1;i=1791", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1792",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1793", {}),
                                            },
                                        ),
                                        "InterfaceType_U8": (
                                            "V",
                                            "ns=1;i=1794",
                                            {
                                                "Index": ("V", "ns=1;i=1795", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1796",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1797", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=1798", {}),
                                        "PortEnableMask_U64": (
                                            "V",
                                            "ns=1;i=3172",
                                            {
                                                "Index": ("V", "ns=1;i=3173", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3174",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3175", {}),
                                            },
                                        ),
                                        "Valid_BOOL": (
                                            "V",
                                            "ns=1;i=1799",
                                            {
                                                "Index": ("V", "ns=1;i=1800", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1801",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1802", {}),
                                            },
                                        ),
                                    },
                                ),
                                "NMT_MNPReqPayloadLimitList_AU16": (
                                    "V",
                                    "ns=1;i=2047",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3232", {}),
                                        "Index": ("V", "ns=1;i=2048", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2049", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2050", {}),
                                        "Range": ("V", "ns=1;i=3233", {}),
                                    },
                                ),
                                "NMT_ResetCmd_U8": (
                                    "V",
                                    "ns=1;i=1803",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3253", {}),
                                        "Index": ("V", "ns=1;i=1804", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1805", {}),
                                        "SubIndex": ("V", "ns=1;i=1806", {}),
                                    },
                                ),
                                "SDO_SequLayerTimeout_U32": (
                                    "V",
                                    "ns=1;i=1807",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3255", {}),
                                        "Index": ("V", "ns=1;i=1808", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1809", {}),
                                        "Range": ("V", "ns=1;i=3257", {}),
                                        "SubIndex": ("V", "ns=1;i=1810", {}),
                                    },
                                ),
                            },
                        ),
                    },
                ),
                "SdoServices": ("O", "ns=1;i=66", {}),
                "Status": ("O", "ns=1;i=64", {}),
            },
        ),
        "PowerlinkDeviceProfileType": (
            "OT",
            "ns=1;i=1",
            {
                "IndexRangeSize": ("V", "ns=1;i=444", {}),
                "IndexRangeStart": ("V", "ns=1;i=443", {}),
            },
        ),
        "PowerlinkDeviceType": (
            "OT",
            "ns=1;i=2",
            {
                "<CNIdentifier>": (
                    "O",
                    "ns=1;i=43",
                    {
                        "Configuration": (
                            "O",
                            "ns=1;i=44",
                            {
                                "DLL_CNSoCJitterRange_U32": (
                                    "V",
                                    "ns=1;i=1119",
                                    {
                                        "Index": ("V", "ns=1;i=1120", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1121", {}),
                                        "SubIndex": ("V", "ns=1;i=1122", {}),
                                    },
                                ),
                                "NMT_CNBasicEthernetTimeout_U32": (
                                    "V",
                                    "ns=1;i=492",
                                    {
                                        "Index": ("V", "ns=1;i=493", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=494", {}),
                                        "SubIndex": ("V", "ns=1;i=495", {}),
                                    },
                                ),
                                "NMT_ConsumerHeartbeatTime_AU32": (
                                    "V",
                                    "ns=1;i=1185",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=1186", {}),
                                        "Index": ("V", "ns=1;i=1187", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1188", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1189", {}),
                                    },
                                ),
                                "NMT_CycleLen_U32": (
                                    "V",
                                    "ns=1;i=500",
                                    {
                                        "Index": ("V", "ns=1;i=501", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=502", {}),
                                        "SubIndex": ("V", "ns=1;i=503", {}),
                                    },
                                ),
                                "NMT_CycleTiming_REC": (
                                    "V",
                                    "ns=1;i=504",
                                    {
                                        "ASndMaxLatency_U32": (
                                            "V",
                                            "ns=1;i=1672",
                                            {
                                                "Index": ("V", "ns=1;i=1673", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1674",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1675", {}),
                                            },
                                        ),
                                        "AsyncMTU_U16": (
                                            "V",
                                            "ns=1;i=505",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1986",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=506", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=507",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=1987", {}),
                                                "SubIndex": ("V", "ns=1;i=508", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=509", {}),
                                        "IsochrRxMaxPayload_U16": (
                                            "V",
                                            "ns=1;i=510",
                                            {
                                                "Index": ("V", "ns=1;i=511", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=512",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=1988", {}),
                                                "SubIndex": ("V", "ns=1;i=513", {}),
                                            },
                                        ),
                                        "IsochrTxMaxPayload_U16": (
                                            "V",
                                            "ns=1;i=514",
                                            {
                                                "Index": ("V", "ns=1;i=515", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=516",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=1989", {}),
                                                "SubIndex": ("V", "ns=1;i=517", {}),
                                            },
                                        ),
                                        "LeaseTime_U32": (
                                            "V",
                                            "ns=1;i=1676",
                                            {
                                                "Index": ("V", "ns=1;i=1677", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1678",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1691", {}),
                                            },
                                        ),
                                        "MultiplCycleCnt_U8": (
                                            "V",
                                            "ns=1;i=518",
                                            {
                                                "Index": ("V", "ns=1;i=519", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=520",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=521", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=522", {}),
                                        "PReqActPayloadLimit_U16": (
                                            "V",
                                            "ns=1;i=1692",
                                            {
                                                "Index": ("V", "ns=1;i=1693", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1694",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1695", {}),
                                            },
                                        ),
                                        "PResActPayloadLimit_U16": (
                                            "V",
                                            "ns=1;i=1696",
                                            {
                                                "Index": ("V", "ns=1;i=1697", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1698",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1699", {}),
                                            },
                                        ),
                                        "PResMaxLatency_U32": (
                                            "V",
                                            "ns=1;i=1700",
                                            {
                                                "Index": ("V", "ns=1;i=1701", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1702",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1835", {}),
                                            },
                                        ),
                                        "PResMode_U8": (
                                            "V",
                                            "ns=1;i=1836",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1837",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1838", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1839",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=1840", {}),
                                                "SubIndex": ("V", "ns=1;i=1841", {}),
                                            },
                                        ),
                                        "PResTimeFirst_U32": (
                                            "V",
                                            "ns=1;i=1842",
                                            {
                                                "Index": ("V", "ns=1;i=1843", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1844",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1845", {}),
                                            },
                                        ),
                                        "PResTimeSecond_U32": (
                                            "V",
                                            "ns=1;i=1846",
                                            {
                                                "Index": ("V", "ns=1;i=1847", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1848",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1849", {}),
                                            },
                                        ),
                                        "Prescaler_U16": (
                                            "V",
                                            "ns=1;i=1850",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1851",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1852", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1853",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=1854", {}),
                                                "SubIndex": ("V", "ns=1;i=1855", {}),
                                            },
                                        ),
                                        "SyncMNDelayFirst_U32": (
                                            "V",
                                            "ns=1;i=1856",
                                            {
                                                "Index": ("V", "ns=1;i=1857", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1858",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1904", {}),
                                            },
                                        ),
                                        "SyncMNDelaySecond_U32": (
                                            "V",
                                            "ns=1;i=1905",
                                            {
                                                "Index": ("V", "ns=1;i=1906", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1907",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1908", {}),
                                            },
                                        ),
                                    },
                                ),
                                "NMT_IsochrSlotAssign_AU8": (
                                    "V",
                                    "ns=1;i=1194",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=1195", {}),
                                        "Index": ("V", "ns=1;i=1196", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1197", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1198", {}),
                                        "Range": ("V", "ns=1;i=1199", {}),
                                    },
                                ),
                                "NMT_MultiplCycleAssign_AU8": (
                                    "V",
                                    "ns=1;i=1251",
                                    {
                                        "Index": ("V", "ns=1;i=1252", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1253", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1254", {}),
                                    },
                                ),
                                "NMT_NodeAssignment_AU32": (
                                    "V",
                                    "ns=1;i=1255",
                                    {
                                        "Index": ("V", "ns=1;i=1256", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1257", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1258", {}),
                                    },
                                ),
                                "NMT_PResPayloadLimitList_AU16": (
                                    "V",
                                    "ns=1;i=1259",
                                    {
                                        "Index": ("V", "ns=1;i=1260", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1261", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1262", {}),
                                    },
                                ),
                                "NMT_RestoreDefParam_REC": (
                                    "V",
                                    "ns=1;i=1267",
                                    {
                                        "AllParam_U32": (
                                            "V",
                                            "ns=1;i=1268",
                                            {
                                                "Index": ("V", "ns=1;i=1269", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1270",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1271", {}),
                                            },
                                        ),
                                        "ApplicationParam_U32": (
                                            "V",
                                            "ns=1;i=1272",
                                            {
                                                "Index": ("V", "ns=1;i=1273", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1274",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1275", {}),
                                            },
                                        ),
                                        "CommunicationParam_U32": (
                                            "V",
                                            "ns=1;i=1276",
                                            {
                                                "Index": ("V", "ns=1;i=1277", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1278",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1279", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=1280", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1281", {}),
                                    },
                                ),
                                "NMT_StoreParam_REC": (
                                    "V",
                                    "ns=1;i=1282",
                                    {
                                        "AllParam_U32": (
                                            "V",
                                            "ns=1;i=1283",
                                            {
                                                "Index": ("V", "ns=1;i=1284", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1285",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1286", {}),
                                            },
                                        ),
                                        "ApplicationParam_U32": (
                                            "V",
                                            "ns=1;i=1287",
                                            {
                                                "Index": ("V", "ns=1;i=1288", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1289",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1290", {}),
                                            },
                                        ),
                                        "CommunicationParam_U32": (
                                            "V",
                                            "ns=1;i=1291",
                                            {
                                                "Index": ("V", "ns=1;i=1292", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1293",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1294", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=1295", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1296", {}),
                                    },
                                ),
                                "PDL_MnExpAppSwDateList_AU32": (
                                    "V",
                                    "ns=1;i=1320",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=1336", {}),
                                        "Index": ("V", "ns=1;i=1337", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1338", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1339", {}),
                                    },
                                ),
                                "PDL_MnExpAppSwTimeList_AU32": (
                                    "V",
                                    "ns=1;i=1340",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=1341", {}),
                                        "Index": ("V", "ns=1;i=1342", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1343", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1344", {}),
                                    },
                                ),
                                "PDO_RxCommParam_00h_REC": (
                                    "V",
                                    "ns=1;i=1353",
                                    {
                                        "Index": ("V", "ns=1;i=1354", {}),
                                        "MappingVersion_U8": (
                                            "V",
                                            "ns=1;i=1355",
                                            {
                                                "Index": ("V", "ns=1;i=1356", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1357",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1358", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=1359",
                                            {
                                                "Index": ("V", "ns=1;i=1360", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1361",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1362", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=1363", {}),
                                    },
                                ),
                                "PDO_RxCommParam_01h_REC": (
                                    "V",
                                    "ns=1;i=1364",
                                    {
                                        "Index": ("V", "ns=1;i=1365", {}),
                                        "MappingVersion_U8": (
                                            "V",
                                            "ns=1;i=1367",
                                            {
                                                "Index": ("V", "ns=1;i=1368", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1370",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1371", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=1373",
                                            {
                                                "Index": ("V", "ns=1;i=1374", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1377",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1378", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=1379", {}),
                                    },
                                ),
                                "PDO_RxCommParam_02h_REC": (
                                    "V",
                                    "ns=1;i=1380",
                                    {
                                        "Index": ("V", "ns=1;i=1585", {}),
                                        "MappingVersion_U8": (
                                            "V",
                                            "ns=1;i=1586",
                                            {
                                                "Index": ("V", "ns=1;i=1587", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1588",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1589", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=1590",
                                            {
                                                "Index": ("V", "ns=1;i=1591", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1592",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1593", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=1594", {}),
                                    },
                                ),
                                "PDO_RxCommParam_03h_REC": (
                                    "V",
                                    "ns=1;i=1595",
                                    {
                                        "Index": ("V", "ns=1;i=1596", {}),
                                        "MappingVersion_U8": (
                                            "V",
                                            "ns=1;i=1597",
                                            {
                                                "Index": ("V", "ns=1;i=1598", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1599",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1600", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=1601",
                                            {
                                                "Index": ("V", "ns=1;i=1602", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1603",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1604", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=1605", {}),
                                    },
                                ),
                                "PDO_RxMappParam_00h_AU64": (
                                    "V",
                                    "ns=1;i=1606",
                                    {
                                        "Index": ("V", "ns=1;i=1607", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1608", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1609", {}),
                                    },
                                ),
                                "PDO_RxMappParam_01h_AU64": (
                                    "V",
                                    "ns=1;i=1610",
                                    {
                                        "Index": ("V", "ns=1;i=1611", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1612", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1613", {}),
                                    },
                                ),
                                "PDO_RxMappParam_02h_AU64": (
                                    "V",
                                    "ns=1;i=1614",
                                    {
                                        "Index": ("V", "ns=1;i=1615", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1616", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1617", {}),
                                    },
                                ),
                                "PDO_RxMappParam_03h_AU64": (
                                    "V",
                                    "ns=1;i=1618",
                                    {
                                        "Index": ("V", "ns=1;i=1619", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1620", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1621", {}),
                                    },
                                ),
                                "PDO_TxCommParam_00h_REC": (
                                    "V",
                                    "ns=1;i=1622",
                                    {
                                        "Index": ("V", "ns=1;i=1623", {}),
                                        "MappingVersion_U8": (
                                            "V",
                                            "ns=1;i=1624",
                                            {
                                                "Index": ("V", "ns=1;i=1625", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1626",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1627", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=1628",
                                            {
                                                "Index": ("V", "ns=1;i=1629", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1630",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1631", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=1632", {}),
                                    },
                                ),
                                "PDO_TxMappParam_00h_AU64": (
                                    "V",
                                    "ns=1;i=1633",
                                    {
                                        "Index": ("V", "ns=1;i=1634", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1635", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1636", {}),
                                    },
                                ),
                                "SDO_CmdLayerTimeout_U32": (
                                    "V",
                                    "ns=1;i=1637",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=1638", {}),
                                        "Index": ("V", "ns=1;i=1639", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1640", {}),
                                        "Range": ("V", "ns=1;i=1641", {}),
                                        "SubIndex": ("V", "ns=1;i=1642", {}),
                                    },
                                ),
                                "SDO_SequLayerNoAck_U32": (
                                    "V",
                                    "ns=1;i=1643",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=1644", {}),
                                        "Index": ("V", "ns=1;i=1645", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1646", {}),
                                        "Range": ("V", "ns=1;i=1647", {}),
                                        "SubIndex": ("V", "ns=1;i=1648", {}),
                                    },
                                ),
                                "SDO_SequLayerTimeout_U32": (
                                    "V",
                                    "ns=1;i=644",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=1930", {}),
                                        "Index": ("V", "ns=1;i=645", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=646", {}),
                                        "Range": ("V", "ns=1;i=1931", {}),
                                        "SubIndex": ("V", "ns=1;i=647", {}),
                                    },
                                ),
                            },
                        ),
                        "Control": ("O", "ns=1;i=51", {}),
                        "Diagnostics": (
                            "O",
                            "ns=1;i=48",
                            {
                                "DIA_ERRStatistics_REC": (
                                    "V",
                                    "ns=1;i=939",
                                    {
                                        "EmergencyQueueOverflow_U32": (
                                            "V",
                                            "ns=1;i=940",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1932",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=941", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=942",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=950", {}),
                                            },
                                        ),
                                        "EmergencyQueueWrite_U32": (
                                            "V",
                                            "ns=1;i=951",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1933",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=952", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=953",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=954", {}),
                                            },
                                        ),
                                        "ExceptionNewEdge_U32": (
                                            "V",
                                            "ns=1;i=955",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1934",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=956", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=957",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=958", {}),
                                            },
                                        ),
                                        "ExceptionResetEdgePos_U32": (
                                            "V",
                                            "ns=1;i=959",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1935",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=960", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=961",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=962", {}),
                                            },
                                        ),
                                        "HistoryEntryWrite_U32": (
                                            "V",
                                            "ns=1;i=963",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1936",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1012", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1013",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1014", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=1015", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1016", {}),
                                        "StaticErrorBitFieldChanged_U32": (
                                            "V",
                                            "ns=1;i=1017",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1937",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1018", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1019",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1020", {}),
                                            },
                                        ),
                                        "StatusEntryChanged_U32": (
                                            "V",
                                            "ns=1;i=1021",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1938",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1022", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1023",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1024", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DIA_NMTTelegrCount_REC": (
                                    "V",
                                    "ns=1;i=1025",
                                    {
                                        "AsyncRx_U32": (
                                            "V",
                                            "ns=1;i=1026",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1939",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1027", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1028",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1029", {}),
                                            },
                                        ),
                                        "AsyncTx_U32": (
                                            "V",
                                            "ns=1;i=1030",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1940",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1031", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1032",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1033", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=1034", {}),
                                        "IsochrCyc_U32": (
                                            "V",
                                            "ns=1;i=1035",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1941",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1036", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1037",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1038", {}),
                                            },
                                        ),
                                        "IsochrRx_U32": (
                                            "V",
                                            "ns=1;i=1039",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1942",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1040", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1041",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1042", {}),
                                            },
                                        ),
                                        "IsochrTx_U32": (
                                            "V",
                                            "ns=1;i=1043",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1943",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1044", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1045",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1046", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=1047", {}),
                                        "SdoRx_U32": (
                                            "V",
                                            "ns=1;i=1048",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1944",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1049", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1050",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1051", {}),
                                            },
                                        ),
                                        "SdoTx_U32": (
                                            "V",
                                            "ns=1;i=1052",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1945",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1053", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1054",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1055", {}),
                                            },
                                        ),
                                        "Status_U32": (
                                            "V",
                                            "ns=1;i=1056",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1946",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1057", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1058",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1059", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DLL_CNCRCError_REC": (
                                    "V",
                                    "ns=1;i=89",
                                    {
                                        "CumulativeCnt_U32": (
                                            "V",
                                            "ns=1;i=94",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1947",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=103", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=104",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=144", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=145", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=445", {}),
                                        "ThresholdCnt_U32": (
                                            "V",
                                            "ns=1;i=1649",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1650",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1651", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1652",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1653", {}),
                                            },
                                        ),
                                        "Threshold_U32": (
                                            "V",
                                            "ns=1;i=1654",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1655",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1656", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1657",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1658", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DLL_CNCollision_REC": (
                                    "V",
                                    "ns=1;i=1060",
                                    {
                                        "CumulativeCnt_U32": (
                                            "V",
                                            "ns=1;i=1061",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1948",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1062", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1063",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1064", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=1065", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1066", {}),
                                        "ThresholdCnt_U32": (
                                            "V",
                                            "ns=1;i=1071",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1973",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1072", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1073",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1074", {}),
                                            },
                                        ),
                                        "Threshold_U32": (
                                            "V",
                                            "ns=1;i=1067",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1974",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1068", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1069",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1070", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DLL_CNLossOfLinkCum_U32": (
                                    "V",
                                    "ns=1;i=1075",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=1076", {}),
                                        "Index": ("V", "ns=1;i=1077", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1078", {}),
                                        "SubIndex": ("V", "ns=1;i=1079", {}),
                                    },
                                ),
                                "DLL_CNLossOfSocTolerance_U32": (
                                    "V",
                                    "ns=1;i=446",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=1659", {}),
                                        "Index": ("V", "ns=1;i=449", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=450", {}),
                                        "SubIndex": ("V", "ns=1;i=451", {}),
                                    },
                                ),
                                "DLL_CNLossPReq_REC": (
                                    "V",
                                    "ns=1;i=1080",
                                    {
                                        "CumulativeCnt_U32": (
                                            "V",
                                            "ns=1;i=1086",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1975",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1087", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1088",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1089", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=1090", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1091", {}),
                                        "ThresholdCnt_U32": (
                                            "V",
                                            "ns=1;i=1096",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1976",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1097", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1098",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1099", {}),
                                            },
                                        ),
                                        "Threshold_U32": (
                                            "V",
                                            "ns=1;i=1092",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1977",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1093", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1094",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1095", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DLL_CNLossSoA_REC": (
                                    "V",
                                    "ns=1;i=1100",
                                    {
                                        "CumulativeCnt_U32": (
                                            "V",
                                            "ns=1;i=1101",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1978",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1102", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1103",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1104", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=1105", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1106", {}),
                                        "ThresholdCnt_U32": (
                                            "V",
                                            "ns=1;i=1115",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1979",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1116", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1117",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1118", {}),
                                            },
                                        ),
                                        "Threshold_U32": (
                                            "V",
                                            "ns=1;i=1107",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1980",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1108", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1109",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1110", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DLL_CNLossSoC_REC": (
                                    "V",
                                    "ns=1;i=452",
                                    {
                                        "CumulativeCnt_U32": (
                                            "V",
                                            "ns=1;i=459",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1981",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=460", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=461",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=462", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=463", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=464", {}),
                                        "ThresholdCnt_U32": (
                                            "V",
                                            "ns=1;i=1660",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1661",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1662", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1663",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1664", {}),
                                            },
                                        ),
                                        "Threshold_U32": (
                                            "V",
                                            "ns=1;i=1665",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1666",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1667", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1668",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1669", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DLL_CNSoCJitter_REC": (
                                    "V",
                                    "ns=1;i=1131",
                                    {
                                        "CumulativeCnt_U32": (
                                            "V",
                                            "ns=1;i=1132",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1982",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1133", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1134",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1135", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=1136", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1137", {}),
                                        "ThresholdCnt_U32": (
                                            "V",
                                            "ns=1;i=1142",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1983",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1143", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1144",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1145", {}),
                                            },
                                        ),
                                        "Threshold_U32": (
                                            "V",
                                            "ns=1;i=1138",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1984",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1139", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1140",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1141", {}),
                                            },
                                        ),
                                    },
                                ),
                                "ERR_ErrorRegister_U8": (
                                    "V",
                                    "ns=1;i=465",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=1670", {}),
                                        "Index": ("V", "ns=1;i=466", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=467", {}),
                                        "SubIndex": ("V", "ns=1;i=470", {}),
                                    },
                                ),
                                "ERR_History_ADOM": (
                                    "V",
                                    "ns=1;i=1146",
                                    {
                                        "Index": ("V", "ns=1;i=1166", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1167", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1168", {}),
                                    },
                                ),
                                "PDO_ErrMapVers_OSTR": (
                                    "V",
                                    "ns=1;i=1345",
                                    {
                                        "Index": ("V", "ns=1;i=1346", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1347", {}),
                                        "SubIndex": ("V", "ns=1;i=1348", {}),
                                    },
                                ),
                                "PDO_ErrShort_RX_OSTR": (
                                    "V",
                                    "ns=1;i=1349",
                                    {
                                        "Index": ("V", "ns=1;i=1350", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1351", {}),
                                        "SubIndex": ("V", "ns=1;i=1352", {}),
                                    },
                                ),
                            },
                        ),
                        "Identification": ("O", "ns=1;i=61", {}),
                        "MethodSet": (
                            "O",
                            "ns=1;i=62",
                            {
                                "ReadByIndex": (
                                    "M",
                                    "ns=1;i=1082",
                                    {
                                        "InputArguments": ("V", "ns=1;i=648", {}),
                                        "OutputArguments": ("V", "ns=1;i=649", {}),
                                    },
                                ),
                                "WriteByIndex": (
                                    "M",
                                    "ns=1;i=1083",
                                    {
                                        "InputArguments": ("V", "ns=1;i=650", {}),
                                        "OutputArguments": ("V", "ns=1;i=651", {}),
                                    },
                                ),
                            },
                        ),
                        "NetworkAddress": ("O", "ns=1;i=67", {}),
                        "ParameterSet": (
                            "O",
                            "ns=1;i=49",
                            {
                                "INP_ProcessImage_REC": (
                                    "V",
                                    "ns=1;i=1169",
                                    {
                                        "Index": ("V", "ns=1;i=1170", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1171", {}),
                                        "ProcessImageDomain_DOM": (
                                            "V",
                                            "ns=1;i=1172",
                                            {
                                                "Index": ("V", "ns=1;i=1173", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1174",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1175", {}),
                                            },
                                        ),
                                        "SelectedRange_U32": (
                                            "V",
                                            "ns=1;i=1176",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1985",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=1177", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1178",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1179", {}),
                                            },
                                        ),
                                    },
                                ),
                                "NMT_ChildIdentList_AU16": (
                                    "V",
                                    "ns=1;i=1180",
                                    {
                                        "Index": ("V", "ns=1;i=1181", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1182", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1183", {}),
                                        "Range": ("V", "ns=1;i=1184", {}),
                                    },
                                ),
                                "NMT_CurrNMTState_U8": (
                                    "V",
                                    "ns=1;i=496",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=1671", {}),
                                        "Index": ("V", "ns=1;i=497", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=498", {}),
                                        "SubIndex": ("V", "ns=1;i=499", {}),
                                    },
                                ),
                                "NMT_DeviceType_U32": (
                                    "V",
                                    "ns=1;i=523",
                                    {
                                        "Index": ("V", "ns=1;i=524", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=525", {}),
                                        "SubIndex": ("V", "ns=1;i=526", {}),
                                    },
                                ),
                                "NMT_EPLNodeID_REC": (
                                    "V",
                                    "ns=1;i=527",
                                    {
                                        "Index": ("V", "ns=1;i=528", {}),
                                        "NodeIDByHW_BOOL": (
                                            "V",
                                            "ns=1;i=533",
                                            {
                                                "Index": ("V", "ns=1;i=534", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=535",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=536", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=529",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1990",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=530", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=531",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=532", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=537", {}),
                                        "SWNodeID_U8": (
                                            "V",
                                            "ns=1;i=1909",
                                            {
                                                "Index": ("V", "ns=1;i=1910", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1911",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1912", {}),
                                            },
                                        ),
                                    },
                                ),
                                "NMT_EPLVersion_U8": (
                                    "V",
                                    "ns=1;i=542",
                                    {
                                        "Index": ("V", "ns=1;i=543", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=544", {}),
                                        "SubIndex": ("V", "ns=1;i=545", {}),
                                    },
                                ),
                                "NMT_FeatureFlags_U32": (
                                    "V",
                                    "ns=1;i=546",
                                    {
                                        "Index": ("V", "ns=1;i=547", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=548", {}),
                                        "SubIndex": ("V", "ns=1;i=549", {}),
                                    },
                                ),
                                "NMT_HostName_VSTR": (
                                    "V",
                                    "ns=1;i=1190",
                                    {
                                        "Index": ("V", "ns=1;i=1191", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1192", {}),
                                        "SubIndex": ("V", "ns=1;i=1193", {}),
                                    },
                                ),
                                "NMT_IdentityObject_REC": (
                                    "V",
                                    "ns=1;i=554",
                                    {
                                        "Index": ("V", "ns=1;i=555", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=556", {}),
                                        "ProductCode_U32": (
                                            "V",
                                            "ns=1;i=1913",
                                            {
                                                "Index": ("V", "ns=1;i=1914", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1915",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1916", {}),
                                            },
                                        ),
                                        "RevisionNo_U32": (
                                            "V",
                                            "ns=1;i=1917",
                                            {
                                                "Index": ("V", "ns=1;i=1918", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1919",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1920", {}),
                                            },
                                        ),
                                        "SerialNo_U32": (
                                            "V",
                                            "ns=1;i=1921",
                                            {
                                                "Index": ("V", "ns=1;i=1922", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1923",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1924", {}),
                                            },
                                        ),
                                        "VendorId_U32": (
                                            "V",
                                            "ns=1;i=557",
                                            {
                                                "Index": ("V", "ns=1;i=558", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=559",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=560", {}),
                                            },
                                        ),
                                    },
                                ),
                                "NMT_InterfaceGroup_0h_REC": (
                                    "V",
                                    "ns=1;i=561",
                                    {
                                        "Index": ("V", "ns=1;i=566", {}),
                                        "InterfaceAdminState_U8": (
                                            "V",
                                            "ns=1;i=567",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=1991",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=568", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=569",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=1992", {}),
                                                "SubIndex": ("V", "ns=1;i=570", {}),
                                            },
                                        ),
                                        "InterfaceDescription_VSTR": (
                                            "V",
                                            "ns=1;i=571",
                                            {
                                                "Index": ("V", "ns=1;i=572", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=573",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=610", {}),
                                            },
                                        ),
                                        "InterfaceIndex_U16": (
                                            "V",
                                            "ns=1;i=611",
                                            {
                                                "Index": ("V", "ns=1;i=612", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=613",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=1993", {}),
                                                "SubIndex": ("V", "ns=1;i=614", {}),
                                            },
                                        ),
                                        "InterfaceMtu_U16": (
                                            "V",
                                            "ns=1;i=615",
                                            {
                                                "Index": ("V", "ns=1;i=616", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=617",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=618", {}),
                                            },
                                        ),
                                        "InterfaceName_VSTR": (
                                            "V",
                                            "ns=1;i=619",
                                            {
                                                "Index": ("V", "ns=1;i=620", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=621",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=622", {}),
                                            },
                                        ),
                                        "InterfaceOperStatus_U8": (
                                            "V",
                                            "ns=1;i=623",
                                            {
                                                "Index": ("V", "ns=1;i=624", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=625",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=1994", {}),
                                                "SubIndex": ("V", "ns=1;i=626", {}),
                                            },
                                        ),
                                        "InterfacePhysAddress_OSTR": (
                                            "V",
                                            "ns=1;i=627",
                                            {
                                                "Index": ("V", "ns=1;i=628", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=629",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=630", {}),
                                            },
                                        ),
                                        "InterfaceType_U8": (
                                            "V",
                                            "ns=1;i=631",
                                            {
                                                "Index": ("V", "ns=1;i=632", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=633",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=634", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=635", {}),
                                        "PortEnableMask_U64": (
                                            "V",
                                            "ns=1;i=1925",
                                            {
                                                "Index": ("V", "ns=1;i=1926", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1927",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1928", {}),
                                            },
                                        ),
                                        "Valid_BOOL": (
                                            "V",
                                            "ns=1;i=636",
                                            {
                                                "Index": ("V", "ns=1;i=637", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=638",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=639", {}),
                                            },
                                        ),
                                    },
                                ),
                                "NMT_ManufactDevName_VS": (
                                    "V",
                                    "ns=1;i=1200",
                                    {
                                        "Index": ("V", "ns=1;i=1201", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1202", {}),
                                        "SubIndex": ("V", "ns=1;i=1203", {}),
                                    },
                                ),
                                "NMT_ManufactHwVers_VS": (
                                    "V",
                                    "ns=1;i=1243",
                                    {
                                        "Index": ("V", "ns=1;i=1244", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1245", {}),
                                        "SubIndex": ("V", "ns=1;i=1246", {}),
                                    },
                                ),
                                "NMT_ManufactSwVers_VS": (
                                    "V",
                                    "ns=1;i=1247",
                                    {
                                        "Index": ("V", "ns=1;i=1248", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1249", {}),
                                        "SubIndex": ("V", "ns=1;i=1250", {}),
                                    },
                                ),
                                "NMT_RelativeLatencyDiff_AU32": (
                                    "V",
                                    "ns=1;i=1263",
                                    {
                                        "Index": ("V", "ns=1;i=1264", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=1265", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=1266", {}),
                                    },
                                ),
                                "NMT_ResetCmd_U8": (
                                    "V",
                                    "ns=1;i=640",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=1929", {}),
                                        "Index": ("V", "ns=1;i=641", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=642", {}),
                                        "SubIndex": ("V", "ns=1;i=643", {}),
                                    },
                                ),
                                "NWL_IpAddrTable_0h_REC": (
                                    "V",
                                    "ns=1;i=1297",
                                    {
                                        "Addr_IPAD": (
                                            "V",
                                            "ns=1;i=1298",
                                            {
                                                "Index": ("V", "ns=1;i=1299", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1300",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1301", {}),
                                            },
                                        ),
                                        "DefaultGateway_IPAD": (
                                            "V",
                                            "ns=1;i=1302",
                                            {
                                                "Index": ("V", "ns=1;i=1303", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1304",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1305", {}),
                                            },
                                        ),
                                        "IfIndex_U16": (
                                            "V",
                                            "ns=1;i=1306",
                                            {
                                                "Index": ("V", "ns=1;i=1307", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1308",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=1995", {}),
                                                "SubIndex": ("V", "ns=1;i=1309", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=1310", {}),
                                        "NetMask_IPAD": (
                                            "V",
                                            "ns=1;i=1311",
                                            {
                                                "Index": ("V", "ns=1;i=1312", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1313",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1314", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=1315", {}),
                                        "ReasmMaxSize_U16": (
                                            "V",
                                            "ns=1;i=1316",
                                            {
                                                "Index": ("V", "ns=1;i=1317", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=1318",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=1319", {}),
                                            },
                                        ),
                                    },
                                ),
                            },
                        ),
                        "ProfileId": ("O", "ns=1;i=50", {}),
                        "SdoServices": ("O", "ns=1;i=68", {}),
                        "Status": ("O", "ns=1;i=69", {}),
                    },
                ),
                "<MNIdentifier>": (
                    "O",
                    "ns=1;i=70",
                    {
                        "Configuration": (
                            "O",
                            "ns=1;i=71",
                            {
                                "CFM_ExpConfDateList_AU32": (
                                    "V",
                                    "ns=1;i=1996",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2012", {}),
                                        "Index": ("V", "ns=1;i=2013", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2014", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2015", {}),
                                    },
                                ),
                                "CFM_ExpConfIdList_AU32": (
                                    "V",
                                    "ns=1;i=2016",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2017", {}),
                                        "Index": ("V", "ns=1;i=2018", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2019", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2020", {}),
                                    },
                                ),
                                "CFM_ExpConfTimeList_AU32": (
                                    "V",
                                    "ns=1;i=2021",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2022", {}),
                                        "Index": ("V", "ns=1;i=2023", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2024", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2025", {}),
                                    },
                                ),
                                "DLL_MNCycleSuspendNumber_U32": (
                                    "V",
                                    "ns=1;i=667",
                                    {
                                        "Index": ("V", "ns=1;i=668", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=669", {}),
                                        "SubIndex": ("V", "ns=1;i=670", {}),
                                    },
                                ),
                                "NMT_BootTime_REC": (
                                    "V",
                                    "ns=1;i=710",
                                    {
                                        "Index": ("V", "ns=1;i=711", {}),
                                        "MNConfigurationTimeout_U32": (
                                            "V",
                                            "ns=1;i=2863",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2864",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2865", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2866",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2867", {}),
                                            },
                                        ),
                                        "MNIdentificationTimeout_U32": (
                                            "V",
                                            "ns=1;i=2868",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2869",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2870", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2871",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2872", {}),
                                            },
                                        ),
                                        "MNSoftwareTimeout_U32": (
                                            "V",
                                            "ns=1;i=2873",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2874",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2875", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2876",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2877", {}),
                                            },
                                        ),
                                        "MNStartCNTimeout_U32": (
                                            "V",
                                            "ns=1;i=2878",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2879",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2880", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2881",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2882", {}),
                                            },
                                        ),
                                        "MNSwitchOverCycleDivider_U32": (
                                            "V",
                                            "ns=1;i=2883",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2884",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2885", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2886",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2887", {}),
                                            },
                                        ),
                                        "MNSwitchOverDelay_U32": (
                                            "V",
                                            "ns=1;i=2888",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2889",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2890", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2891",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2892", {}),
                                            },
                                        ),
                                        "MNSwitchOverPriority_U32": (
                                            "V",
                                            "ns=1;i=2893",
                                            {
                                                "Index": ("V", "ns=1;i=2894", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2895",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2896", {}),
                                            },
                                        ),
                                        "MNTimeoutPreOp1_U32": (
                                            "V",
                                            "ns=1;i=712",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3293",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=713", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=714",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=3294", {}),
                                                "SubIndex": ("V", "ns=1;i=715", {}),
                                            },
                                        ),
                                        "MNTimeoutPreOp2_U32": (
                                            "V",
                                            "ns=1;i=716",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3295",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=717", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=718",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=719", {}),
                                            },
                                        ),
                                        "MNTimeoutReadyToOp_U32": (
                                            "V",
                                            "ns=1;i=720",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3296",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=721", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=722",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=3297", {}),
                                                "SubIndex": ("V", "ns=1;i=723", {}),
                                            },
                                        ),
                                        "MNWaitNotAct_U32": (
                                            "V",
                                            "ns=1;i=724",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3298",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=725", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=726",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=3299", {}),
                                                "SubIndex": ("V", "ns=1;i=727", {}),
                                            },
                                        ),
                                        "MNWaitPreOp1_U32": (
                                            "V",
                                            "ns=1;i=2897",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2902",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2903", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2908",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=2909", {}),
                                                "SubIndex": ("V", "ns=1;i=2910", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=728", {}),
                                    },
                                ),
                                "NMT_ConsumerHeartbeatTime_AU32": (
                                    "V",
                                    "ns=1;i=2363",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2364", {}),
                                        "Index": ("V", "ns=1;i=2365", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2366", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2367", {}),
                                    },
                                ),
                                "NMT_CycleLen_U32": (
                                    "V",
                                    "ns=1;i=733",
                                    {
                                        "Index": ("V", "ns=1;i=734", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=735", {}),
                                        "SubIndex": ("V", "ns=1;i=736", {}),
                                    },
                                ),
                                "NMT_CycleTiming_REC": (
                                    "V",
                                    "ns=1;i=737",
                                    {
                                        "ASndMaxLatency_U32": (
                                            "V",
                                            "ns=1;i=2912",
                                            {
                                                "Index": ("V", "ns=1;i=2913", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2914",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2915", {}),
                                            },
                                        ),
                                        "AsyncMTU_U16": (
                                            "V",
                                            "ns=1;i=738",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3300",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=739", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=740",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=3301", {}),
                                                "SubIndex": ("V", "ns=1;i=741", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=742", {}),
                                        "IsochrRxMaxPayload_U16": (
                                            "V",
                                            "ns=1;i=743",
                                            {
                                                "Index": ("V", "ns=1;i=744", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=745",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=3302", {}),
                                                "SubIndex": ("V", "ns=1;i=746", {}),
                                            },
                                        ),
                                        "IsochrTxMaxPayload_U16": (
                                            "V",
                                            "ns=1;i=747",
                                            {
                                                "Index": ("V", "ns=1;i=748", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=749",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=3303", {}),
                                                "SubIndex": ("V", "ns=1;i=750", {}),
                                            },
                                        ),
                                        "LeaseTime_U32": (
                                            "V",
                                            "ns=1;i=2919",
                                            {
                                                "Index": ("V", "ns=1;i=2920", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2927",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2928", {}),
                                            },
                                        ),
                                        "MultiplCycleCnt_U8": (
                                            "V",
                                            "ns=1;i=751",
                                            {
                                                "Index": ("V", "ns=1;i=752", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=753",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=754", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=755", {}),
                                        "PReqActPayloadLimit_U16": (
                                            "V",
                                            "ns=1;i=2929",
                                            {
                                                "Index": ("V", "ns=1;i=2930", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2937",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2938", {}),
                                            },
                                        ),
                                        "PResActPayloadLimit_U16": (
                                            "V",
                                            "ns=1;i=2966",
                                            {
                                                "Index": ("V", "ns=1;i=2967", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2978",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2980", {}),
                                            },
                                        ),
                                        "PResMaxLatency_U32": (
                                            "V",
                                            "ns=1;i=3047",
                                            {
                                                "Index": ("V", "ns=1;i=3048", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3049",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3050", {}),
                                            },
                                        ),
                                        "PResMode_U8": (
                                            "V",
                                            "ns=1;i=3052",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3054",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=3056", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3058",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=3060", {}),
                                                "SubIndex": ("V", "ns=1;i=3062", {}),
                                            },
                                        ),
                                        "PResTimeFirst_U32": (
                                            "V",
                                            "ns=1;i=3064",
                                            {
                                                "Index": ("V", "ns=1;i=3066", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3068",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3073", {}),
                                            },
                                        ),
                                        "PResTimeSecond_U32": (
                                            "V",
                                            "ns=1;i=3076",
                                            {
                                                "Index": ("V", "ns=1;i=3079", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3081",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3083", {}),
                                            },
                                        ),
                                        "Prescaler_U16": (
                                            "V",
                                            "ns=1;i=3085",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3088",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=3096", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3097",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=3098", {}),
                                                "SubIndex": ("V", "ns=1;i=3099", {}),
                                            },
                                        ),
                                        "SyncMNDelayFirst_U32": (
                                            "V",
                                            "ns=1;i=3100",
                                            {
                                                "Index": ("V", "ns=1;i=3101", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3102",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3152", {}),
                                            },
                                        ),
                                        "SyncMNDelaySecond_U32": (
                                            "V",
                                            "ns=1;i=3153",
                                            {
                                                "Index": ("V", "ns=1;i=3154", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3155",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3176", {}),
                                            },
                                        ),
                                    },
                                ),
                                "NMT_IsochrSlotAssign_AU8": (
                                    "V",
                                    "ns=1;i=2372",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2373", {}),
                                        "Index": ("V", "ns=1;i=2374", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2375", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2376", {}),
                                        "Range": ("V", "ns=1;i=2377", {}),
                                    },
                                ),
                                "NMT_MNCNPResTimeout_AU32": (
                                    "V",
                                    "ns=1;i=874",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3225", {}),
                                        "Index": ("V", "ns=1;i=875", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=876", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=877", {}),
                                    },
                                ),
                                "NMT_MNCycleTiming_REC": (
                                    "V",
                                    "ns=1;i=878",
                                    {
                                        "ASndMaxNumber": (
                                            "V",
                                            "ns=1;i=3227",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3229",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=3231", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3234",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=3235", {}),
                                                "SubIndex": ("V", "ns=1;i=3237", {}),
                                            },
                                        ),
                                        "AsyncSlotTimeout_U32": (
                                            "V",
                                            "ns=1;i=3239",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3241",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=3243", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3248",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=3249", {}),
                                                "SubIndex": ("V", "ns=1;i=3250", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=879", {}),
                                        "MinRedCycleTime_U32": (
                                            "V",
                                            "ns=1;i=3251",
                                            {
                                                "Index": ("V", "ns=1;i=3254", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3256",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3258", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=880", {}),
                                        "WaitSoCPReq_U32": (
                                            "V",
                                            "ns=1;i=881",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3309",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=882", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=883",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=884", {}),
                                            },
                                        ),
                                    },
                                ),
                                "NMT_MNDeviceTypeIdList_AU32": (
                                    "V",
                                    "ns=1;i=885",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3259", {}),
                                        "Index": ("V", "ns=1;i=886", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=887", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=888", {}),
                                    },
                                ),
                                "NMT_MNProductCodeList_AU32": (
                                    "V",
                                    "ns=1;i=2409",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2410", {}),
                                        "Index": ("V", "ns=1;i=2411", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2412", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2413", {}),
                                    },
                                ),
                                "NMT_MNRevisionNoList_AU32": (
                                    "V",
                                    "ns=1;i=2414",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2415", {}),
                                        "Index": ("V", "ns=1;i=2416", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2417", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2418", {}),
                                    },
                                ),
                                "NMT_MNSerialNoList_AU32": (
                                    "V",
                                    "ns=1;i=2419",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2420", {}),
                                        "Index": ("V", "ns=1;i=2421", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2422", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2423", {}),
                                    },
                                ),
                                "NMT_MNVendorIdList_AU32": (
                                    "V",
                                    "ns=1;i=2424",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2425", {}),
                                        "Index": ("V", "ns=1;i=2426", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2427", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2428", {}),
                                    },
                                ),
                                "NMT_MultiplCycleAssign_AU8": (
                                    "V",
                                    "ns=1;i=2448",
                                    {
                                        "Index": ("V", "ns=1;i=2449", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2453", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2454", {}),
                                    },
                                ),
                                "NMT_NodeAssignment_AU32": (
                                    "V",
                                    "ns=1;i=2455",
                                    {
                                        "Index": ("V", "ns=1;i=2463", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2464", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2465", {}),
                                    },
                                ),
                                "NMT_PResPayloadLimitList_AU16": (
                                    "V",
                                    "ns=1;i=2466",
                                    {
                                        "Index": ("V", "ns=1;i=2467", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2468", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2472", {}),
                                    },
                                ),
                                "NMT_RestoreDefParam_REC": (
                                    "V",
                                    "ns=1;i=2484",
                                    {
                                        "AllParam_U32": (
                                            "V",
                                            "ns=1;i=2485",
                                            {
                                                "Index": ("V", "ns=1;i=2486", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2487",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2491", {}),
                                            },
                                        ),
                                        "ApplicationParam_U32": (
                                            "V",
                                            "ns=1;i=2492",
                                            {
                                                "Index": ("V", "ns=1;i=2493", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2505",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2506", {}),
                                            },
                                        ),
                                        "CommunicationParam_U32": (
                                            "V",
                                            "ns=1;i=2507",
                                            {
                                                "Index": ("V", "ns=1;i=2508", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2509",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2510", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=2511", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2514", {}),
                                    },
                                ),
                                "NMT_StartUp_U32": (
                                    "V",
                                    "ns=1;i=920",
                                    {
                                        "Index": ("V", "ns=1;i=921", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=929", {}),
                                        "SubIndex": ("V", "ns=1;i=930", {}),
                                    },
                                ),
                                "NMT_StoreParam_REC": (
                                    "V",
                                    "ns=1;i=2515",
                                    {
                                        "AllParam_U32": (
                                            "V",
                                            "ns=1;i=2516",
                                            {
                                                "Index": ("V", "ns=1;i=2517", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2518",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2519", {}),
                                            },
                                        ),
                                        "ApplicationParam_U32": (
                                            "V",
                                            "ns=1;i=2520",
                                            {
                                                "Index": ("V", "ns=1;i=2521", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2522",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2523", {}),
                                            },
                                        ),
                                        "CommunicationParam_U32": (
                                            "V",
                                            "ns=1;i=2524",
                                            {
                                                "Index": ("V", "ns=1;i=2525", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2526",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2527", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=2528", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2529", {}),
                                    },
                                ),
                                "PDL_MnExpAppSwDateList_AU32": (
                                    "V",
                                    "ns=1;i=2553",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2554", {}),
                                        "Index": ("V", "ns=1;i=2555", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2556", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2557", {}),
                                    },
                                ),
                                "PDL_MnExpAppSwTimeList_AU32": (
                                    "V",
                                    "ns=1;i=2558",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2559", {}),
                                        "Index": ("V", "ns=1;i=2560", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2561", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2562", {}),
                                    },
                                ),
                                "PDO_RxCommParam_00h_REC": (
                                    "V",
                                    "ns=1;i=2571",
                                    {
                                        "Index": ("V", "ns=1;i=2572", {}),
                                        "MappingVersion_U8": (
                                            "V",
                                            "ns=1;i=2573",
                                            {
                                                "Index": ("V", "ns=1;i=2574", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2575",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2576", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=2577",
                                            {
                                                "Index": ("V", "ns=1;i=2578", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2579",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2580", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=2581", {}),
                                    },
                                ),
                                "PDO_RxCommParam_01h_REC": (
                                    "V",
                                    "ns=1;i=2582",
                                    {
                                        "Index": ("V", "ns=1;i=2583", {}),
                                        "MappingVersion_U8": (
                                            "V",
                                            "ns=1;i=2584",
                                            {
                                                "Index": ("V", "ns=1;i=2585", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2600",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2601", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=2602",
                                            {
                                                "Index": ("V", "ns=1;i=2603", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2604",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2605", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=2606", {}),
                                    },
                                ),
                                "PDO_RxCommParam_02h_REC": (
                                    "V",
                                    "ns=1;i=2607",
                                    {
                                        "Index": ("V", "ns=1;i=2608", {}),
                                        "MappingVersion_U8": (
                                            "V",
                                            "ns=1;i=2609",
                                            {
                                                "Index": ("V", "ns=1;i=2610", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2611",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2612", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=2613",
                                            {
                                                "Index": ("V", "ns=1;i=2614", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2615",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2616", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=2617", {}),
                                    },
                                ),
                                "PDO_RxCommParam_03h_REC": (
                                    "V",
                                    "ns=1;i=2618",
                                    {
                                        "Index": ("V", "ns=1;i=2619", {}),
                                        "MappingVersion_U8": (
                                            "V",
                                            "ns=1;i=2620",
                                            {
                                                "Index": ("V", "ns=1;i=2621", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2622",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2623", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=2628",
                                            {
                                                "Index": ("V", "ns=1;i=2629", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2636",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2637", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=2642", {}),
                                    },
                                ),
                                "PDO_RxMappParam_00h_AU64": (
                                    "V",
                                    "ns=1;i=2643",
                                    {
                                        "Index": ("V", "ns=1;i=2648", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2653", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2654", {}),
                                    },
                                ),
                                "PDO_RxMappParam_01h_AU64": (
                                    "V",
                                    "ns=1;i=2693",
                                    {
                                        "Index": ("V", "ns=1;i=2694", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2695", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2696", {}),
                                    },
                                ),
                                "PDO_RxMappParam_02h_AU64": (
                                    "V",
                                    "ns=1;i=2697",
                                    {
                                        "Index": ("V", "ns=1;i=2698", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2699", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2700", {}),
                                    },
                                ),
                                "PDO_RxMappParam_03h_AU64": (
                                    "V",
                                    "ns=1;i=2701",
                                    {
                                        "Index": ("V", "ns=1;i=2702", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2703", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2704", {}),
                                    },
                                ),
                                "PDO_TxCommParam_00h_REC": (
                                    "V",
                                    "ns=1;i=2705",
                                    {
                                        "Index": ("V", "ns=1;i=2706", {}),
                                        "MappingVersion_U8": (
                                            "V",
                                            "ns=1;i=2707",
                                            {
                                                "Index": ("V", "ns=1;i=2708", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2709",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2710", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=2711",
                                            {
                                                "Index": ("V", "ns=1;i=2712", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2713",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2714", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=2715", {}),
                                    },
                                ),
                                "PDO_TxCommParam_01h_REC": (
                                    "V",
                                    "ns=1;i=2716",
                                    {
                                        "Index": ("V", "ns=1;i=2717", {}),
                                        "MappingVersion_U8": (
                                            "V",
                                            "ns=1;i=2718",
                                            {
                                                "Index": ("V", "ns=1;i=2719", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2720",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2721", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=2722",
                                            {
                                                "Index": ("V", "ns=1;i=2723", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2724",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2728", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=2729", {}),
                                    },
                                ),
                                "PDO_TxCommParam_02h_REC": (
                                    "V",
                                    "ns=1;i=2736",
                                    {
                                        "Index": ("V", "ns=1;i=2737", {}),
                                        "MappingVersion_U8": (
                                            "V",
                                            "ns=1;i=2742",
                                            {
                                                "Index": ("V", "ns=1;i=2743", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2750",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2751", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=2752",
                                            {
                                                "Index": ("V", "ns=1;i=2753", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2806",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2807", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=2808", {}),
                                    },
                                ),
                                "PDO_TxCommParam_03h_REC": (
                                    "V",
                                    "ns=1;i=2809",
                                    {
                                        "Index": ("V", "ns=1;i=2810", {}),
                                        "MappingVersion_U8": (
                                            "V",
                                            "ns=1;i=2811",
                                            {
                                                "Index": ("V", "ns=1;i=2812", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2813",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2814", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=2815",
                                            {
                                                "Index": ("V", "ns=1;i=2816", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2817",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2818", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=2819", {}),
                                    },
                                ),
                                "PDO_TxMappParam_00h_AU64": (
                                    "V",
                                    "ns=1;i=2820",
                                    {
                                        "Index": ("V", "ns=1;i=2821", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2822", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2823", {}),
                                    },
                                ),
                                "PDO_TxMappParam_01h_AU64": (
                                    "V",
                                    "ns=1;i=2824",
                                    {
                                        "Index": ("V", "ns=1;i=2825", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2826", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2827", {}),
                                    },
                                ),
                                "PDO_TxMappParam_02h_AU64": (
                                    "V",
                                    "ns=1;i=2828",
                                    {
                                        "Index": ("V", "ns=1;i=2829", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2830", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2831", {}),
                                    },
                                ),
                                "PDO_TxMappParam_03h_AU64": (
                                    "V",
                                    "ns=1;i=2832",
                                    {
                                        "Index": ("V", "ns=1;i=2833", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2834", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2835", {}),
                                    },
                                ),
                                "SDO_CmdLayerTimeout_U32": (
                                    "V",
                                    "ns=1;i=2836",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2837", {}),
                                        "Index": ("V", "ns=1;i=2838", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2839", {}),
                                        "Range": ("V", "ns=1;i=2840", {}),
                                        "SubIndex": ("V", "ns=1;i=2841", {}),
                                    },
                                ),
                                "SDO_SequLayerNoAck_U32": (
                                    "V",
                                    "ns=1;i=2842",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2843", {}),
                                        "Index": ("V", "ns=1;i=2844", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2845", {}),
                                        "Range": ("V", "ns=1;i=2846", {}),
                                        "SubIndex": ("V", "ns=1;i=2847", {}),
                                    },
                                ),
                                "SDO_SequLayerTimeout_U32": (
                                    "V",
                                    "ns=1;i=931",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3268", {}),
                                        "Index": ("V", "ns=1;i=932", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=933", {}),
                                        "Range": ("V", "ns=1;i=3269", {}),
                                        "SubIndex": ("V", "ns=1;i=934", {}),
                                    },
                                ),
                            },
                        ),
                        "Control": ("O", "ns=1;i=75", {}),
                        "Diagnostics": (
                            "O",
                            "ns=1;i=72",
                            {
                                "DIA_ERRStatistics_REC": (
                                    "V",
                                    "ns=1;i=2026",
                                    {
                                        "EmergencyQueueOverflow_U32": (
                                            "V",
                                            "ns=1;i=2071",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3270",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2072", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2073",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2074", {}),
                                            },
                                        ),
                                        "EmergencyQueueWrite_U32": (
                                            "V",
                                            "ns=1;i=2075",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3271",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2076", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2077",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2078", {}),
                                            },
                                        ),
                                        "ExceptionNewEdge_U32": (
                                            "V",
                                            "ns=1;i=2079",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3272",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2080", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2081",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2082", {}),
                                            },
                                        ),
                                        "ExceptionResetEdgePos_U32": (
                                            "V",
                                            "ns=1;i=2083",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3273",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2084", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2085",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2086", {}),
                                            },
                                        ),
                                        "HistoryEntryWrite_U32": (
                                            "V",
                                            "ns=1;i=2087",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3274",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2088", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2089",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2090", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=2091", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2092", {}),
                                        "StaticErrorBitFieldChanged_U32": (
                                            "V",
                                            "ns=1;i=2093",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3275",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2094", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2095",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2096", {}),
                                            },
                                        ),
                                        "StatusEntryChanged_U32": (
                                            "V",
                                            "ns=1;i=2097",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3276",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2098", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2099",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2100", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DIA_NMTTelegrCount_REC": (
                                    "V",
                                    "ns=1;i=2101",
                                    {
                                        "AsyncRx_U32": (
                                            "V",
                                            "ns=1;i=2102",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3277",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2103", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2104",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2105", {}),
                                            },
                                        ),
                                        "AsyncTx_U32": (
                                            "V",
                                            "ns=1;i=2106",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3278",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2107", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2108",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2109", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=2110", {}),
                                        "IsochrCyc_U32": (
                                            "V",
                                            "ns=1;i=2111",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3279",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2112", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2113",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2114", {}),
                                            },
                                        ),
                                        "IsochrRx_U32": (
                                            "V",
                                            "ns=1;i=2141",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3280",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2142", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2143",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2144", {}),
                                            },
                                        ),
                                        "IsochrTx_U32": (
                                            "V",
                                            "ns=1;i=2145",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3281",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2146", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2147",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2153", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=2154", {}),
                                        "SdoRx_U32": (
                                            "V",
                                            "ns=1;i=2155",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3282",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2156", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2157",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2158", {}),
                                            },
                                        ),
                                        "SdoTx_U32": (
                                            "V",
                                            "ns=1;i=2159",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3283",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2160", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2161",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2162", {}),
                                            },
                                        ),
                                        "Status_U32": (
                                            "V",
                                            "ns=1;i=2163",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3284",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2164", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2165",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2166", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DLL_MNCNLatePResCumCnt_AU32": (
                                    "V",
                                    "ns=1;i=2167",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2168", {}),
                                        "Index": ("V", "ns=1;i=2169", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2170", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2171", {}),
                                    },
                                ),
                                "DLL_MNCNLatePResThrCnt_AU32": (
                                    "V",
                                    "ns=1;i=2224",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2225", {}),
                                        "Index": ("V", "ns=1;i=2226", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2227", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2228", {}),
                                    },
                                ),
                                "DLL_MNCNLatePResThreshold_AU32": (
                                    "V",
                                    "ns=1;i=2229",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2230", {}),
                                        "Index": ("V", "ns=1;i=2231", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2232", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2233", {}),
                                    },
                                ),
                                "DLL_MNCNLossPResCumCnt_AU32": (
                                    "V",
                                    "ns=1;i=2234",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2235", {}),
                                        "Index": ("V", "ns=1;i=2236", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2237", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2238", {}),
                                    },
                                ),
                                "DLL_MNCNLossPResThrCnt_AU32": (
                                    "V",
                                    "ns=1;i=652",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2848", {}),
                                        "Index": ("V", "ns=1;i=653", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=654", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=655", {}),
                                    },
                                ),
                                "DLL_MNCNLossPResThreshold_AU32": (
                                    "V",
                                    "ns=1;i=656",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2849", {}),
                                        "Index": ("V", "ns=1;i=657", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=658", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=659", {}),
                                    },
                                ),
                                "DLL_MNCRCError_REC": (
                                    "V",
                                    "ns=1;i=660",
                                    {
                                        "CumulativeCnt_U32": (
                                            "V",
                                            "ns=1;i=661",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3285",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=662", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=663",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=664", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=665", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=666", {}),
                                        "ThresholdCnt_U32": (
                                            "V",
                                            "ns=1;i=2850",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2851",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2852", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2853",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2854", {}),
                                            },
                                        ),
                                        "Threshold_U32": (
                                            "V",
                                            "ns=1;i=2855",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=2856",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2857", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2858",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2859", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DLL_MNCollision_REC": (
                                    "V",
                                    "ns=1;i=2239",
                                    {
                                        "CumulativeCnt_U32": (
                                            "V",
                                            "ns=1;i=2240",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3286",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2241", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2242",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2243", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=2244", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2245", {}),
                                        "ThresholdCnt_U32": (
                                            "V",
                                            "ns=1;i=2250",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3287",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2251", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2252",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2253", {}),
                                            },
                                        ),
                                        "Threshold_U32": (
                                            "V",
                                            "ns=1;i=2246",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3288",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2247", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2248",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2249", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DLL_MNCycTimeExceed_REC": (
                                    "V",
                                    "ns=1;i=2254",
                                    {
                                        "CumulativeCnt_U32": (
                                            "V",
                                            "ns=1;i=2255",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3289",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2256", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2257",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2258", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=2259", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2260", {}),
                                        "ThresholdCnt_U32": (
                                            "V",
                                            "ns=1;i=2273",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3290",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2274", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2275",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2276", {}),
                                            },
                                        ),
                                        "Threshold_U32": (
                                            "V",
                                            "ns=1;i=2261",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3291",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2262", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2263",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2264", {}),
                                            },
                                        ),
                                    },
                                ),
                                "DLL_MNLossOfLinkCum_U32": (
                                    "V",
                                    "ns=1;i=2277",
                                    {
                                        "Index": ("V", "ns=1;i=2278", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2279", {}),
                                        "SubIndex": ("V", "ns=1;i=2280", {}),
                                    },
                                ),
                                "DLL_MNLossStatusResCumCnt_AU32": (
                                    "V",
                                    "ns=1;i=2327",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2328", {}),
                                        "Index": ("V", "ns=1;i=2329", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2330", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2331", {}),
                                    },
                                ),
                                "DLL_MNLossStatusResThrCnt_AU32": (
                                    "V",
                                    "ns=1;i=671",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2860", {}),
                                        "Index": ("V", "ns=1;i=672", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=673", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=674", {}),
                                    },
                                ),
                                "DLL_MNLossStatusResThreshold_AU32": (
                                    "V",
                                    "ns=1;i=675",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2861", {}),
                                        "Index": ("V", "ns=1;i=676", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=677", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=678", {}),
                                    },
                                ),
                                "ERR_ErrorRegister_U8": (
                                    "V",
                                    "ns=1;i=679",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2862", {}),
                                        "Index": ("V", "ns=1;i=680", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=681", {}),
                                        "SubIndex": ("V", "ns=1;i=709", {}),
                                    },
                                ),
                                "ERR_History_ADOM": (
                                    "V",
                                    "ns=1;i=2332",
                                    {
                                        "Index": ("V", "ns=1;i=2333", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2334", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2339", {}),
                                    },
                                ),
                                "NMT_MNNodeCurrState_AU8": (
                                    "V",
                                    "ns=1;i=889",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3260", {}),
                                        "Index": ("V", "ns=1;i=890", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=891", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=892", {}),
                                    },
                                ),
                                "NMT_MNNodeExpState_AU8": (
                                    "V",
                                    "ns=1;i=2378",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2379", {}),
                                        "Index": ("V", "ns=1;i=2380", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2381", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2382", {}),
                                    },
                                ),
                                "NMT_RequestCmd_REC": (
                                    "V",
                                    "ns=1;i=897",
                                    {
                                        "CmdData_DOM": (
                                            "V",
                                            "ns=1;i=3263",
                                            {
                                                "Index": ("V", "ns=1;i=3264", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3265",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3266", {}),
                                            },
                                        ),
                                        "CmdID_U8": (
                                            "V",
                                            "ns=1;i=898",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3310",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=899", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=900",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=901", {}),
                                            },
                                        ),
                                        "CmdTarget_U8": (
                                            "V",
                                            "ns=1;i=902",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3311",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=903", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=904",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=905", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=906", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=907", {}),
                                        "Release_BOOL": (
                                            "V",
                                            "ns=1;i=908",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3312",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=909", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=914",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=915", {}),
                                            },
                                        ),
                                    },
                                ),
                                "PDO_ErrMapVers_OSTR": (
                                    "V",
                                    "ns=1;i=2563",
                                    {
                                        "Index": ("V", "ns=1;i=2564", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2565", {}),
                                        "SubIndex": ("V", "ns=1;i=2566", {}),
                                    },
                                ),
                                "PDO_ErrShort_RX_OSTR": (
                                    "V",
                                    "ns=1;i=2567",
                                    {
                                        "Index": ("V", "ns=1;i=2568", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2569", {}),
                                        "SubIndex": ("V", "ns=1;i=2570", {}),
                                    },
                                ),
                            },
                        ),
                        "Identification": ("O", "ns=1;i=76", {}),
                        "MethodSet": (
                            "O",
                            "ns=1;i=77",
                            {
                                "ReadByIndex": (
                                    "M",
                                    "ns=1;i=1084",
                                    {
                                        "InputArguments": ("V", "ns=1;i=935", {}),
                                        "OutputArguments": ("V", "ns=1;i=936", {}),
                                    },
                                ),
                                "WriteByIndex": (
                                    "M",
                                    "ns=1;i=1085",
                                    {
                                        "InputArguments": ("V", "ns=1;i=937", {}),
                                        "OutputArguments": ("V", "ns=1;i=938", {}),
                                    },
                                ),
                            },
                        ),
                        "NetworkAddress": ("O", "ns=1;i=78", {}),
                        "ParameterSet": (
                            "O",
                            "ns=1;i=73",
                            {
                                "INP_ProcessImage_REC": (
                                    "V",
                                    "ns=1;i=2340",
                                    {
                                        "Index": ("V", "ns=1;i=2346", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2347", {}),
                                        "ProcessImageDomain_DOM": (
                                            "V",
                                            "ns=1;i=2348",
                                            {
                                                "Index": ("V", "ns=1;i=2349", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2350",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2351", {}),
                                            },
                                        ),
                                        "SelectedRange_U32": (
                                            "V",
                                            "ns=1;i=2352",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3292",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=2355", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2356",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2357", {}),
                                            },
                                        ),
                                    },
                                ),
                                "NMT_ChildIdentList_AU16": (
                                    "V",
                                    "ns=1;i=2358",
                                    {
                                        "Index": ("V", "ns=1;i=2359", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2360", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2361", {}),
                                        "Range": ("V", "ns=1;i=2362", {}),
                                    },
                                ),
                                "NMT_CurrNMTState_U8": (
                                    "V",
                                    "ns=1;i=729",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=2911", {}),
                                        "Index": ("V", "ns=1;i=730", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=731", {}),
                                        "SubIndex": ("V", "ns=1;i=732", {}),
                                    },
                                ),
                                "NMT_DeviceType_U32": (
                                    "V",
                                    "ns=1;i=756",
                                    {
                                        "Index": ("V", "ns=1;i=757", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=758", {}),
                                        "SubIndex": ("V", "ns=1;i=759", {}),
                                    },
                                ),
                                "NMT_EPLNodeID_REC": (
                                    "V",
                                    "ns=1;i=760",
                                    {
                                        "Index": ("V", "ns=1;i=761", {}),
                                        "NodeIDByHW_BOOL": (
                                            "V",
                                            "ns=1;i=815",
                                            {
                                                "Index": ("V", "ns=1;i=816", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=817",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=818", {}),
                                            },
                                        ),
                                        "NodeID_U8": (
                                            "V",
                                            "ns=1;i=762",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3304",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=812", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=813",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=814", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=819", {}),
                                        "SWNodeID_U8": (
                                            "V",
                                            "ns=1;i=3177",
                                            {
                                                "Index": ("V", "ns=1;i=3178", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3179",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3184", {}),
                                            },
                                        ),
                                    },
                                ),
                                "NMT_EPLVersion_U8": (
                                    "V",
                                    "ns=1;i=820",
                                    {
                                        "Index": ("V", "ns=1;i=821", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=822", {}),
                                        "SubIndex": ("V", "ns=1;i=823", {}),
                                    },
                                ),
                                "NMT_FeatureFlags_U32": (
                                    "V",
                                    "ns=1;i=824",
                                    {
                                        "Index": ("V", "ns=1;i=825", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=826", {}),
                                        "SubIndex": ("V", "ns=1;i=827", {}),
                                    },
                                ),
                                "NMT_HostName_VSTR": (
                                    "V",
                                    "ns=1;i=2368",
                                    {
                                        "Index": ("V", "ns=1;i=2369", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2370", {}),
                                        "SubIndex": ("V", "ns=1;i=2371", {}),
                                    },
                                ),
                                "NMT_IdentityObject_REC": (
                                    "V",
                                    "ns=1;i=828",
                                    {
                                        "Index": ("V", "ns=1;i=829", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=830", {}),
                                        "ProductCode_U32": (
                                            "V",
                                            "ns=1;i=3197",
                                            {
                                                "Index": ("V", "ns=1;i=3198", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3199",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3200", {}),
                                            },
                                        ),
                                        "RevisionNo_U32": (
                                            "V",
                                            "ns=1;i=3201",
                                            {
                                                "Index": ("V", "ns=1;i=3202", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3203",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3204", {}),
                                            },
                                        ),
                                        "SerialNo_U32": (
                                            "V",
                                            "ns=1;i=3205",
                                            {
                                                "Index": ("V", "ns=1;i=3206", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3207",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3208", {}),
                                            },
                                        ),
                                        "VendorId_U32": (
                                            "V",
                                            "ns=1;i=831",
                                            {
                                                "Index": ("V", "ns=1;i=832", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=833",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=834", {}),
                                            },
                                        ),
                                    },
                                ),
                                "NMT_InterfaceGroup_0h_REC": (
                                    "V",
                                    "ns=1;i=835",
                                    {
                                        "Index": ("V", "ns=1;i=836", {}),
                                        "InterfaceAdminState_U8": (
                                            "V",
                                            "ns=1;i=837",
                                            {
                                                "DefaultValue": (
                                                    "V",
                                                    "ns=1;i=3305",
                                                    {},
                                                ),
                                                "Index": ("V", "ns=1;i=838", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=839",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=3306", {}),
                                                "SubIndex": ("V", "ns=1;i=840", {}),
                                            },
                                        ),
                                        "InterfaceDescription_VSTR": (
                                            "V",
                                            "ns=1;i=841",
                                            {
                                                "Index": ("V", "ns=1;i=842", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=843",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=844", {}),
                                            },
                                        ),
                                        "InterfaceIndex_U16": (
                                            "V",
                                            "ns=1;i=845",
                                            {
                                                "Index": ("V", "ns=1;i=846", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=847",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=3307", {}),
                                                "SubIndex": ("V", "ns=1;i=848", {}),
                                            },
                                        ),
                                        "InterfaceMtu_U16": (
                                            "V",
                                            "ns=1;i=849",
                                            {
                                                "Index": ("V", "ns=1;i=850", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=851",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=852", {}),
                                            },
                                        ),
                                        "InterfaceName_VSTR": (
                                            "V",
                                            "ns=1;i=853",
                                            {
                                                "Index": ("V", "ns=1;i=854", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=855",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=856", {}),
                                            },
                                        ),
                                        "InterfaceOperStatus_U8": (
                                            "V",
                                            "ns=1;i=857",
                                            {
                                                "Index": ("V", "ns=1;i=858", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=859",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=3308", {}),
                                                "SubIndex": ("V", "ns=1;i=860", {}),
                                            },
                                        ),
                                        "InterfacePhysAddress_OSTR": (
                                            "V",
                                            "ns=1;i=861",
                                            {
                                                "Index": ("V", "ns=1;i=862", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=863",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=864", {}),
                                            },
                                        ),
                                        "InterfaceType_U8": (
                                            "V",
                                            "ns=1;i=865",
                                            {
                                                "Index": ("V", "ns=1;i=866", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=867",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=868", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=869", {}),
                                        "PortEnableMask_U64": (
                                            "V",
                                            "ns=1;i=3213",
                                            {
                                                "Index": ("V", "ns=1;i=3218", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=3219",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=3224", {}),
                                            },
                                        ),
                                        "Valid_BOOL": (
                                            "V",
                                            "ns=1;i=870",
                                            {
                                                "Index": ("V", "ns=1;i=871", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=872",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=873", {}),
                                            },
                                        ),
                                    },
                                ),
                                "NMT_MNPReqPayloadLimitList_AU16": (
                                    "V",
                                    "ns=1;i=893",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3261", {}),
                                        "Index": ("V", "ns=1;i=894", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=895", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=896", {}),
                                        "Range": ("V", "ns=1;i=3262", {}),
                                    },
                                ),
                                "NMT_ManufactDevName_VS": (
                                    "V",
                                    "ns=1;i=2429",
                                    {
                                        "Index": ("V", "ns=1;i=2430", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2431", {}),
                                        "SubIndex": ("V", "ns=1;i=2432", {}),
                                    },
                                ),
                                "NMT_ManufactHwVers_VS": (
                                    "V",
                                    "ns=1;i=2433",
                                    {
                                        "Index": ("V", "ns=1;i=2434", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2435", {}),
                                        "SubIndex": ("V", "ns=1;i=2436", {}),
                                    },
                                ),
                                "NMT_ManufactSwVers_VS": (
                                    "V",
                                    "ns=1;i=2444",
                                    {
                                        "Index": ("V", "ns=1;i=2445", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2446", {}),
                                        "SubIndex": ("V", "ns=1;i=2447", {}),
                                    },
                                ),
                                "NMT_RelativeLatencyDiff_AU32": (
                                    "V",
                                    "ns=1;i=2473",
                                    {
                                        "Index": ("V", "ns=1;i=2474", {}),
                                        "NumberOfEntries": ("V", "ns=1;i=2482", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=2483", {}),
                                    },
                                ),
                                "NMT_ResetCmd_U8": (
                                    "V",
                                    "ns=1;i=916",
                                    {
                                        "DefaultValue": ("V", "ns=1;i=3267", {}),
                                        "Index": ("V", "ns=1;i=917", {}),
                                        "PowerlinkAttributes": ("V", "ns=1;i=918", {}),
                                        "SubIndex": ("V", "ns=1;i=919", {}),
                                    },
                                ),
                                "NWL_IpAddrTable_0h_REC": (
                                    "V",
                                    "ns=1;i=2530",
                                    {
                                        "Addr_IPAD": (
                                            "V",
                                            "ns=1;i=2531",
                                            {
                                                "Index": ("V", "ns=1;i=2532", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2533",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2534", {}),
                                            },
                                        ),
                                        "DefaultGateway_IPAD": (
                                            "V",
                                            "ns=1;i=2535",
                                            {
                                                "Index": ("V", "ns=1;i=2536", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2537",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2538", {}),
                                            },
                                        ),
                                        "IfIndex_U16": (
                                            "V",
                                            "ns=1;i=2539",
                                            {
                                                "Index": ("V", "ns=1;i=2540", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2541",
                                                    {},
                                                ),
                                                "Range": ("V", "ns=1;i=3313", {}),
                                                "SubIndex": ("V", "ns=1;i=2542", {}),
                                            },
                                        ),
                                        "Index": ("V", "ns=1;i=2543", {}),
                                        "NetMask_IPAD": (
                                            "V",
                                            "ns=1;i=2544",
                                            {
                                                "Index": ("V", "ns=1;i=2545", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2546",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2547", {}),
                                            },
                                        ),
                                        "NumberOfEntries": ("V", "ns=1;i=2548", {}),
                                        "ReasmMaxSize_U16": (
                                            "V",
                                            "ns=1;i=2549",
                                            {
                                                "Index": ("V", "ns=1;i=2550", {}),
                                                "PowerlinkAttributes": (
                                                    "V",
                                                    "ns=1;i=2551",
                                                    {},
                                                ),
                                                "SubIndex": ("V", "ns=1;i=2552", {}),
                                            },
                                        ),
                                    },
                                ),
                            },
                        ),
                        "ProfileId": ("O", "ns=1;i=74", {}),
                        "SdoServices": ("O", "ns=1;i=79", {}),
                        "Status": ("O", "ns=1;i=80", {}),
                    },
                ),
            },
        ),
        "PowerlinkProtocolType": ("OT", "ns=1;i=6", {}),
    },
    "vartypes": {
        "PowerlinkArrayType": (
            "VT",
            "ns=1;i=11",
            {
                "DefaultValue": ("V", "ns=1;i=2725", {}),
                "Index": ("V", "ns=1;i=99", {}),
                "NumberOfEntries": ("V", "ns=1;i=100", {}),
                "PowerlinkAttributes": ("V", "ns=1;i=101", {}),
                "Range": ("V", "ns=1;i=2726", {}),
            },
        ),
        "PowerlinkRecordType": (
            "VT",
            "ns=1;i=7",
            {
                "DIA_ERRStatistics_Type": (
                    "VT",
                    "ns=1;i=22",
                    {
                        "EmergencyQueueOverflow_U32": (
                            "V",
                            "ns=1;i=423",
                            {
                                "DefaultValue": ("V", "ns=1;i=2283", {}),
                                "Index": ("V", "ns=1;i=424", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=425", {}),
                                "SubIndex": ("V", "ns=1;i=426", {}),
                            },
                        ),
                        "EmergencyQueueWrite_U32": (
                            "V",
                            "ns=1;i=419",
                            {
                                "DefaultValue": ("V", "ns=1;i=2282", {}),
                                "Index": ("V", "ns=1;i=420", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=421", {}),
                                "SubIndex": ("V", "ns=1;i=422", {}),
                            },
                        ),
                        "ExceptionNewEdge_U32": (
                            "V",
                            "ns=1;i=439",
                            {
                                "DefaultValue": ("V", "ns=1;i=2287", {}),
                                "Index": ("V", "ns=1;i=440", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=441", {}),
                                "SubIndex": ("V", "ns=1;i=442", {}),
                            },
                        ),
                        "ExceptionResetEdgePos_U32": (
                            "V",
                            "ns=1;i=435",
                            {
                                "DefaultValue": ("V", "ns=1;i=2286", {}),
                                "Index": ("V", "ns=1;i=436", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=437", {}),
                                "SubIndex": ("V", "ns=1;i=438", {}),
                            },
                        ),
                        "HistoryEntryWrite_U32": (
                            "V",
                            "ns=1;i=415",
                            {
                                "DefaultValue": ("V", "ns=1;i=2281", {}),
                                "Index": ("V", "ns=1;i=416", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=417", {}),
                                "SubIndex": ("V", "ns=1;i=418", {}),
                            },
                        ),
                        "Index": ("V", "ns=1;i=2494", {}),
                        "NumberOfEntries": ("V", "ns=1;i=2495", {}),
                        "StaticErrorBitFieldChanged_U32": (
                            "V",
                            "ns=1;i=431",
                            {
                                "DefaultValue": ("V", "ns=1;i=2285", {}),
                                "Index": ("V", "ns=1;i=432", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=433", {}),
                                "SubIndex": ("V", "ns=1;i=434", {}),
                            },
                        ),
                        "StatusEntryChanged_U32": (
                            "V",
                            "ns=1;i=427",
                            {
                                "DefaultValue": ("V", "ns=1;i=2284", {}),
                                "Index": ("V", "ns=1;i=428", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=429", {}),
                                "SubIndex": ("V", "ns=1;i=430", {}),
                            },
                        ),
                    },
                ),
                "DIA_NMTTelegrCount_Type": (
                    "VT",
                    "ns=1;i=21",
                    {
                        "AsyncRx_U32": (
                            "V",
                            "ns=1;i=395",
                            {
                                "DefaultValue": ("V", "ns=1;i=2335", {}),
                                "Index": ("V", "ns=1;i=396", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=397", {}),
                                "SubIndex": ("V", "ns=1;i=398", {}),
                            },
                        ),
                        "AsyncTx_U32": (
                            "V",
                            "ns=1;i=399",
                            {
                                "DefaultValue": ("V", "ns=1;i=2336", {}),
                                "Index": ("V", "ns=1;i=400", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=401", {}),
                                "SubIndex": ("V", "ns=1;i=402", {}),
                            },
                        ),
                        "Index": ("V", "ns=1;i=2496", {}),
                        "IsochrCyc_U32": (
                            "V",
                            "ns=1;i=383",
                            {
                                "DefaultValue": ("V", "ns=1;i=2337", {}),
                                "Index": ("V", "ns=1;i=384", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=385", {}),
                                "SubIndex": ("V", "ns=1;i=386", {}),
                            },
                        ),
                        "IsochrRx_U32": (
                            "V",
                            "ns=1;i=387",
                            {
                                "DefaultValue": ("V", "ns=1;i=2341", {}),
                                "Index": ("V", "ns=1;i=388", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=389", {}),
                                "SubIndex": ("V", "ns=1;i=390", {}),
                            },
                        ),
                        "IsochrTx_U32": (
                            "V",
                            "ns=1;i=391",
                            {
                                "DefaultValue": ("V", "ns=1;i=2342", {}),
                                "Index": ("V", "ns=1;i=392", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=393", {}),
                                "SubIndex": ("V", "ns=1;i=394", {}),
                            },
                        ),
                        "NumberOfEntries": ("V", "ns=1;i=2497", {}),
                        "SdoRx_U32": (
                            "V",
                            "ns=1;i=403",
                            {
                                "DefaultValue": ("V", "ns=1;i=2343", {}),
                                "Index": ("V", "ns=1;i=404", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=405", {}),
                                "SubIndex": ("V", "ns=1;i=406", {}),
                            },
                        ),
                        "SdoTx_U32": (
                            "V",
                            "ns=1;i=407",
                            {
                                "DefaultValue": ("V", "ns=1;i=2344", {}),
                                "Index": ("V", "ns=1;i=408", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=409", {}),
                                "SubIndex": ("V", "ns=1;i=410", {}),
                            },
                        ),
                        "Status_U32": (
                            "V",
                            "ns=1;i=411",
                            {
                                "DefaultValue": ("V", "ns=1;i=2345", {}),
                                "Index": ("V", "ns=1;i=412", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=413", {}),
                                "SubIndex": ("V", "ns=1;i=414", {}),
                            },
                        ),
                    },
                ),
                "DLL_ErrorCntRec_Type": (
                    "VT",
                    "ns=1;i=20",
                    {
                        "CumulativeCnt_U32": (
                            "V",
                            "ns=1;i=371",
                            {
                                "DefaultValue": ("V", "ns=1;i=2437", {}),
                                "Index": ("V", "ns=1;i=372", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=373", {}),
                                "SubIndex": ("V", "ns=1;i=374", {}),
                            },
                        ),
                        "NumberOfEntries": ("V", "ns=1;i=2512", {}),
                        "ThresholdCnt_U32": (
                            "V",
                            "ns=1;i=379",
                            {
                                "DefaultValue": ("V", "ns=1;i=2475", {}),
                                "Index": ("V", "ns=1;i=380", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=381", {}),
                                "SubIndex": ("V", "ns=1;i=382", {}),
                            },
                        ),
                        "Threshold_U32": (
                            "V",
                            "ns=1;i=375",
                            {
                                "DefaultValue": ("V", "ns=1;i=2456", {}),
                                "Index": ("V", "ns=1;i=376", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=377", {}),
                                "SubIndex": ("V", "ns=1;i=378", {}),
                            },
                        ),
                    },
                ),
                "IDENTITY_Type": (
                    "VT",
                    "ns=1;i=19",
                    {
                        "Index": ("V", "ns=1;i=2586", {}),
                        "NumberOfEntries": ("V", "ns=1;i=2587", {}),
                        "ProductCode_U32": (
                            "V",
                            "ns=1;i=359",
                            {
                                "Index": ("V", "ns=1;i=360", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=361", {}),
                                "SubIndex": ("V", "ns=1;i=362", {}),
                            },
                        ),
                        "RevisionNo_U32": (
                            "V",
                            "ns=1;i=363",
                            {
                                "Index": ("V", "ns=1;i=364", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=365", {}),
                                "SubIndex": ("V", "ns=1;i=366", {}),
                            },
                        ),
                        "SerialNo_U32": (
                            "V",
                            "ns=1;i=367",
                            {
                                "Index": ("V", "ns=1;i=368", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=369", {}),
                                "SubIndex": ("V", "ns=1;i=370", {}),
                            },
                        ),
                        "VendorId_U32": (
                            "V",
                            "ns=1;i=355",
                            {
                                "Index": ("V", "ns=1;i=356", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=357", {}),
                                "SubIndex": ("V", "ns=1;i=358", {}),
                            },
                        ),
                    },
                ),
                "INP_ProcessImage_Type": (
                    "VT",
                    "ns=1;i=18",
                    {
                        "Index": ("V", "ns=1;i=2624", {}),
                        "NumberOfEntries": ("V", "ns=1;i=2625", {}),
                        "ProcessImageDomain_DOM": (
                            "V",
                            "ns=1;i=351",
                            {
                                "Index": ("V", "ns=1;i=352", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=353", {}),
                                "SubIndex": ("V", "ns=1;i=354", {}),
                            },
                        ),
                        "SelectedRange_U32": (
                            "V",
                            "ns=1;i=347",
                            {
                                "DefaultValue": ("V", "ns=1;i=2626", {}),
                                "Index": ("V", "ns=1;i=348", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=349", {}),
                                "SubIndex": ("V", "ns=1;i=350", {}),
                            },
                        ),
                    },
                ),
                "Index": ("V", "ns=1;i=85", {}),
                "NMT_BootTime_Type": (
                    "VT",
                    "ns=1;i=16",
                    {
                        "Index": ("V", "ns=1;i=2630", {}),
                        "MNConfigurationTimeout_U32": (
                            "V",
                            "ns=1;i=263",
                            {
                                "DefaultValue": ("V", "ns=1;i=2657", {}),
                                "Index": ("V", "ns=1;i=264", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=265", {}),
                                "SubIndex": ("V", "ns=1;i=266", {}),
                            },
                        ),
                        "MNIdentificationTimeout_U32": (
                            "V",
                            "ns=1;i=255",
                            {
                                "DefaultValue": ("V", "ns=1;i=2655", {}),
                                "Index": ("V", "ns=1;i=256", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=257", {}),
                                "SubIndex": ("V", "ns=1;i=258", {}),
                            },
                        ),
                        "MNSoftwareTimeout_U32": (
                            "V",
                            "ns=1;i=259",
                            {
                                "DefaultValue": ("V", "ns=1;i=2656", {}),
                                "Index": ("V", "ns=1;i=260", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=261", {}),
                                "SubIndex": ("V", "ns=1;i=262", {}),
                            },
                        ),
                        "MNStartCNTimeout_U32": (
                            "V",
                            "ns=1;i=267",
                            {
                                "DefaultValue": ("V", "ns=1;i=2658", {}),
                                "Index": ("V", "ns=1;i=268", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=269", {}),
                                "SubIndex": ("V", "ns=1;i=270", {}),
                            },
                        ),
                        "MNSwitchOverCycleDivider_U32": (
                            "V",
                            "ns=1;i=283",
                            {
                                "DefaultValue": ("V", "ns=1;i=2660", {}),
                                "Index": ("V", "ns=1;i=284", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=285", {}),
                                "SubIndex": ("V", "ns=1;i=286", {}),
                            },
                        ),
                        "MNSwitchOverDelay_U32": (
                            "V",
                            "ns=1;i=275",
                            {
                                "DefaultValue": ("V", "ns=1;i=2659", {}),
                                "Index": ("V", "ns=1;i=276", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=281", {}),
                                "SubIndex": ("V", "ns=1;i=282", {}),
                            },
                        ),
                        "MNSwitchOverPriority_U32": (
                            "V",
                            "ns=1;i=271",
                            {
                                "Index": ("V", "ns=1;i=272", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=273", {}),
                                "SubIndex": ("V", "ns=1;i=274", {}),
                            },
                        ),
                        "MNTimeoutPreOp1_U32": (
                            "V",
                            "ns=1;i=239",
                            {
                                "DefaultValue": ("V", "ns=1;i=2638", {}),
                                "Index": ("V", "ns=1;i=240", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=241", {}),
                                "Range": ("V", "ns=1;i=2639", {}),
                                "SubIndex": ("V", "ns=1;i=242", {}),
                            },
                        ),
                        "MNTimeoutPreOp2_U32": (
                            "V",
                            "ns=1;i=243",
                            {
                                "DefaultValue": ("V", "ns=1;i=2644", {}),
                                "Index": ("V", "ns=1;i=244", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=245", {}),
                                "SubIndex": ("V", "ns=1;i=246", {}),
                            },
                        ),
                        "MNTimeoutReadyToOp_U32": (
                            "V",
                            "ns=1;i=247",
                            {
                                "DefaultValue": ("V", "ns=1;i=2649", {}),
                                "Index": ("V", "ns=1;i=248", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=249", {}),
                                "Range": ("V", "ns=1;i=2650", {}),
                                "SubIndex": ("V", "ns=1;i=250", {}),
                            },
                        ),
                        "MNWaitNotAct_U32": (
                            "V",
                            "ns=1;i=235",
                            {
                                "DefaultValue": ("V", "ns=1;i=2632", {}),
                                "Index": ("V", "ns=1;i=236", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=237", {}),
                                "Range": ("V", "ns=1;i=2633", {}),
                                "SubIndex": ("V", "ns=1;i=238", {}),
                            },
                        ),
                        "MNWaitPreOp1_U32": (
                            "V",
                            "ns=1;i=251",
                            {
                                "DefaultValue": ("V", "ns=1;i=2645", {}),
                                "Index": ("V", "ns=1;i=252", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=253", {}),
                                "Range": ("V", "ns=1;i=2647", {}),
                                "SubIndex": ("V", "ns=1;i=254", {}),
                            },
                        ),
                        "NumberOfEntries": ("V", "ns=1;i=2631", {}),
                    },
                ),
                "NMT_CycleTiming_Type": (
                    "VT",
                    "ns=1;i=17",
                    {
                        "ASndMaxLatency_U32": (
                            "V",
                            "ns=1;i=307",
                            {
                                "Index": ("V", "ns=1;i=308", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=309", {}),
                                "SubIndex": ("V", "ns=1;i=310", {}),
                            },
                        ),
                        "AsyncMTU_U16": (
                            "V",
                            "ns=1;i=295",
                            {
                                "DefaultValue": ("V", "ns=1;i=2746", {}),
                                "Index": ("V", "ns=1;i=296", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=297", {}),
                                "Range": ("V", "ns=1;i=2747", {}),
                                "SubIndex": ("V", "ns=1;i=298", {}),
                            },
                        ),
                        "Index": ("V", "ns=1;i=2732", {}),
                        "IsochrRxMaxPayload_U16": (
                            "V",
                            "ns=1;i=291",
                            {
                                "Index": ("V", "ns=1;i=292", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=293", {}),
                                "Range": ("V", "ns=1;i=2740", {}),
                                "SubIndex": ("V", "ns=1;i=294", {}),
                            },
                        ),
                        "IsochrTxMaxPayload_U16": (
                            "V",
                            "ns=1;i=287",
                            {
                                "Index": ("V", "ns=1;i=288", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=289", {}),
                                "Range": ("V", "ns=1;i=2734", {}),
                                "SubIndex": ("V", "ns=1;i=290", {}),
                            },
                        ),
                        "LeaseTime_U32": (
                            "V",
                            "ns=1;i=327",
                            {
                                "Index": ("V", "ns=1;i=328", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=329", {}),
                                "SubIndex": ("V", "ns=1;i=330", {}),
                            },
                        ),
                        "MultiplCycleCnt_U8": (
                            "V",
                            "ns=1;i=299",
                            {
                                "Index": ("V", "ns=1;i=300", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=301", {}),
                                "SubIndex": ("V", "ns=1;i=302", {}),
                            },
                        ),
                        "NumberOfEntries": ("V", "ns=1;i=2733", {}),
                        "PReqActPayloadLimit_U16": (
                            "V",
                            "ns=1;i=331",
                            {
                                "Index": ("V", "ns=1;i=332", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=333", {}),
                                "SubIndex": ("V", "ns=1;i=334", {}),
                            },
                        ),
                        "PResActPayloadLimit_U16": (
                            "V",
                            "ns=1;i=335",
                            {
                                "Index": ("V", "ns=1;i=336", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=337", {}),
                                "SubIndex": ("V", "ns=1;i=338", {}),
                            },
                        ),
                        "PResMaxLatency_U32": (
                            "V",
                            "ns=1;i=303",
                            {
                                "Index": ("V", "ns=1;i=304", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=305", {}),
                                "SubIndex": ("V", "ns=1;i=306", {}),
                            },
                        ),
                        "PResMode_U8": (
                            "V",
                            "ns=1;i=343",
                            {
                                "DefaultValue": ("V", "ns=1;i=2760", {}),
                                "Index": ("V", "ns=1;i=344", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=345", {}),
                                "Range": ("V", "ns=1;i=2761", {}),
                                "SubIndex": ("V", "ns=1;i=346", {}),
                            },
                        ),
                        "PResTimeFirst_U32": (
                            "V",
                            "ns=1;i=311",
                            {
                                "Index": ("V", "ns=1;i=312", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=313", {}),
                                "SubIndex": ("V", "ns=1;i=314", {}),
                            },
                        ),
                        "PResTimeSecond_U32": (
                            "V",
                            "ns=1;i=315",
                            {
                                "Index": ("V", "ns=1;i=316", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=317", {}),
                                "SubIndex": ("V", "ns=1;i=318", {}),
                            },
                        ),
                        "Prescaler_U16": (
                            "V",
                            "ns=1;i=339",
                            {
                                "DefaultValue": ("V", "ns=1;i=2758", {}),
                                "Index": ("V", "ns=1;i=340", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=341", {}),
                                "Range": ("V", "ns=1;i=2759", {}),
                                "SubIndex": ("V", "ns=1;i=342", {}),
                            },
                        ),
                        "SyncMNDelayFirst_U32": (
                            "V",
                            "ns=1;i=319",
                            {
                                "Index": ("V", "ns=1;i=320", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=321", {}),
                                "SubIndex": ("V", "ns=1;i=322", {}),
                            },
                        ),
                        "SyncMNDelaySecond_U32": (
                            "V",
                            "ns=1;i=323",
                            {
                                "Index": ("V", "ns=1;i=324", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=325", {}),
                                "SubIndex": ("V", "ns=1;i=326", {}),
                            },
                        ),
                    },
                ),
                "NMT_EPLNodeID_Type": (
                    "VT",
                    "ns=1;i=9",
                    {
                        "Index": ("V", "ns=1;i=2898", {}),
                        "NodeIDByHW_BOOL": (
                            "V",
                            "ns=1;i=95",
                            {
                                "Index": ("V", "ns=1;i=453", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=454", {}),
                                "SubIndex": ("V", "ns=1;i=455", {}),
                            },
                        ),
                        "NodeID_U8": (
                            "V",
                            "ns=1;i=87",
                            {
                                "DefaultValue": ("V", "ns=1;i=2900", {}),
                                "Index": ("V", "ns=1;i=109", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=110", {}),
                                "SubIndex": ("V", "ns=1;i=140", {}),
                            },
                        ),
                        "NumberOfEntries": ("V", "ns=1;i=2899", {}),
                        "SWNodeID_U8": (
                            "V",
                            "ns=1;i=105",
                            {
                                "Index": ("V", "ns=1;i=106", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=107", {}),
                                "SubIndex": ("V", "ns=1;i=108", {}),
                            },
                        ),
                    },
                ),
                "NMT_InterfaceGroup_Type": (
                    "VT",
                    "ns=1;i=15",
                    {
                        "Index": ("V", "ns=1;i=3180", {}),
                        "InterfaceAdminState_U8": (
                            "V",
                            "ns=1;i=219",
                            {
                                "DefaultValue": ("V", "ns=1;i=2923", {}),
                                "Index": ("V", "ns=1;i=220", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=221", {}),
                                "Range": ("V", "ns=1;i=2924", {}),
                                "SubIndex": ("V", "ns=1;i=222", {}),
                            },
                        ),
                        "InterfaceDescription_VSTR": (
                            "V",
                            "ns=1;i=201",
                            {
                                "Index": ("V", "ns=1;i=202", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=203", {}),
                                "SubIndex": ("V", "ns=1;i=204", {}),
                            },
                        ),
                        "InterfaceIndex_U16": (
                            "V",
                            "ns=1;i=193",
                            {
                                "Index": ("V", "ns=1;i=194", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=195", {}),
                                "Range": ("V", "ns=1;i=2917", {}),
                                "SubIndex": ("V", "ns=1;i=196", {}),
                            },
                        ),
                        "InterfaceMtu_U16": (
                            "V",
                            "ns=1;i=197",
                            {
                                "Index": ("V", "ns=1;i=198", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=199", {}),
                                "SubIndex": ("V", "ns=1;i=200", {}),
                            },
                        ),
                        "InterfaceName_VSTR": (
                            "V",
                            "ns=1;i=205",
                            {
                                "Index": ("V", "ns=1;i=206", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=207", {}),
                                "SubIndex": ("V", "ns=1;i=208", {}),
                            },
                        ),
                        "InterfaceOperStatus_U8": (
                            "V",
                            "ns=1;i=213",
                            {
                                "Index": ("V", "ns=1;i=214", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=215", {}),
                                "Range": ("V", "ns=1;i=2935", {}),
                                "SubIndex": ("V", "ns=1;i=216", {}),
                            },
                        ),
                        "InterfacePhysAddress_OSTR": (
                            "V",
                            "ns=1;i=223",
                            {
                                "Index": ("V", "ns=1;i=224", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=225", {}),
                                "SubIndex": ("V", "ns=1;i=226", {}),
                            },
                        ),
                        "InterfaceType_U8": (
                            "V",
                            "ns=1;i=209",
                            {
                                "Index": ("V", "ns=1;i=210", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=211", {}),
                                "SubIndex": ("V", "ns=1;i=212", {}),
                            },
                        ),
                        "NumberOfEntries": ("V", "ns=1;i=2916", {}),
                        "PortEnableMask_U64": (
                            "V",
                            "ns=1;i=227",
                            {
                                "Index": ("V", "ns=1;i=228", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=229", {}),
                                "SubIndex": ("V", "ns=1;i=230", {}),
                            },
                        ),
                        "Valid_BOOL": (
                            "V",
                            "ns=1;i=231",
                            {
                                "Index": ("V", "ns=1;i=232", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=233", {}),
                                "SubIndex": ("V", "ns=1;i=234", {}),
                            },
                        ),
                    },
                ),
                "NMT_MNCycleTiming_Type": (
                    "VT",
                    "ns=1;i=23",
                    {
                        "ASndMaxNumber": (
                            "V",
                            "ns=1;i=2199",
                            {
                                "DefaultValue": ("V", "ns=1;i=3220", {}),
                                "Index": ("V", "ns=1;i=2200", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=2201", {}),
                                "Range": ("V", "ns=1;i=3221", {}),
                                "SubIndex": ("V", "ns=1;i=2202", {}),
                            },
                        ),
                        "AsyncSlotTimeout_U32": (
                            "V",
                            "ns=1;i=2195",
                            {
                                "DefaultValue": ("V", "ns=1;i=3214", {}),
                                "Index": ("V", "ns=1;i=2196", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=2197", {}),
                                "Range": ("V", "ns=1;i=3215", {}),
                                "SubIndex": ("V", "ns=1;i=2198", {}),
                            },
                        ),
                        "Index": ("V", "ns=1;i=3209", {}),
                        "MinRedCycleTime_U32": (
                            "V",
                            "ns=1;i=2203",
                            {
                                "Index": ("V", "ns=1;i=2204", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=2205", {}),
                                "SubIndex": ("V", "ns=1;i=2206", {}),
                            },
                        ),
                        "NumberOfEntries": ("V", "ns=1;i=3210", {}),
                        "WaitSoCPReq_U32": (
                            "V",
                            "ns=1;i=2191",
                            {
                                "DefaultValue": ("V", "ns=1;i=3211", {}),
                                "Index": ("V", "ns=1;i=2192", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=2193", {}),
                                "SubIndex": ("V", "ns=1;i=2194", {}),
                            },
                        ),
                    },
                ),
                "NMT_ParameterStorage_Type": (
                    "VT",
                    "ns=1;i=14",
                    {
                        "<ManufacturerParam_XXh_U32>": (
                            "V",
                            "ns=1;i=189",
                            {
                                "Index": ("V", "ns=1;i=190", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=191", {}),
                                "SubIndex": ("V", "ns=1;i=192", {}),
                            },
                        ),
                        "AllParam_U32": (
                            "V",
                            "ns=1;i=177",
                            {
                                "Index": ("V", "ns=1;i=178", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=179", {}),
                                "SubIndex": ("V", "ns=1;i=180", {}),
                            },
                        ),
                        "ApplicationParam_U32": (
                            "V",
                            "ns=1;i=185",
                            {
                                "Index": ("V", "ns=1;i=186", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=187", {}),
                                "SubIndex": ("V", "ns=1;i=188", {}),
                            },
                        ),
                        "CommunicationParam_U32": (
                            "V",
                            "ns=1;i=181",
                            {
                                "Index": ("V", "ns=1;i=182", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=183", {}),
                                "SubIndex": ("V", "ns=1;i=184", {}),
                            },
                        ),
                    },
                ),
                "NMT_RequestCmd_Type": (
                    "VT",
                    "ns=1;i=13",
                    {
                        "CmdData_DOM": (
                            "V",
                            "ns=1;i=173",
                            {
                                "Index": ("V", "ns=1;i=174", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=175", {}),
                                "SubIndex": ("V", "ns=1;i=176", {}),
                            },
                        ),
                        "CmdID_U8": (
                            "V",
                            "ns=1;i=165",
                            {
                                "DefaultValue": ("V", "ns=1;i=3071", {}),
                                "Index": ("V", "ns=1;i=166", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=167", {}),
                                "SubIndex": ("V", "ns=1;i=168", {}),
                            },
                        ),
                        "CmdTarget_U8": (
                            "V",
                            "ns=1;i=169",
                            {
                                "DefaultValue": ("V", "ns=1;i=3074", {}),
                                "Index": ("V", "ns=1;i=170", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=171", {}),
                                "SubIndex": ("V", "ns=1;i=172", {}),
                            },
                        ),
                        "Index": ("V", "ns=1;i=3069", {}),
                        "NumberOfEntries": ("V", "ns=1;i=3070", {}),
                        "Release_BOOL": (
                            "V",
                            "ns=1;i=134",
                            {
                                "DefaultValue": ("V", "ns=1;i=3077", {}),
                                "Index": ("V", "ns=1;i=136", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=137", {}),
                                "SubIndex": ("V", "ns=1;i=164", {}),
                            },
                        ),
                    },
                ),
                "NWL_IpAddrTable_Type": (
                    "VT",
                    "ns=1;i=12",
                    {
                        "Addr_IPAD": (
                            "V",
                            "ns=1;i=117",
                            {
                                "Index": ("V", "ns=1;i=118", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=119", {}),
                                "SubIndex": ("V", "ns=1;i=120", {}),
                            },
                        ),
                        "DefaultGateway_IPAD": (
                            "V",
                            "ns=1;i=125",
                            {
                                "Index": ("V", "ns=1;i=126", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=127", {}),
                                "SubIndex": ("V", "ns=1;i=128", {}),
                            },
                        ),
                        "IfIndex_U16": (
                            "V",
                            "ns=1;i=113",
                            {
                                "Index": ("V", "ns=1;i=114", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=115", {}),
                                "Range": ("V", "ns=1;i=2964", {}),
                                "SubIndex": ("V", "ns=1;i=116", {}),
                            },
                        ),
                        "NetMask_IPAD": (
                            "V",
                            "ns=1;i=121",
                            {
                                "Index": ("V", "ns=1;i=122", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=123", {}),
                                "SubIndex": ("V", "ns=1;i=124", {}),
                            },
                        ),
                        "NumberOfEntries": ("V", "ns=1;i=2963", {}),
                        "ReasmMaxSize_U16": (
                            "V",
                            "ns=1;i=129",
                            {
                                "Index": ("V", "ns=1;i=130", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=131", {}),
                                "SubIndex": ("V", "ns=1;i=133", {}),
                            },
                        ),
                    },
                ),
                "NumberOfEntries": ("V", "ns=1;i=86", {}),
                "PDO_CommParamRecord_Type": (
                    "VT",
                    "ns=1;i=10",
                    {
                        "MappingVersion_U8": (
                            "V",
                            "ns=1;i=160",
                            {
                                "Index": ("V", "ns=1;i=161", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=162", {}),
                                "SubIndex": ("V", "ns=1;i=163", {}),
                            },
                        ),
                        "NodeID_U8": (
                            "V",
                            "ns=1;i=156",
                            {
                                "Index": ("V", "ns=1;i=157", {}),
                                "PowerlinkAttributes": ("V", "ns=1;i=158", {}),
                                "SubIndex": ("V", "ns=1;i=159", {}),
                            },
                        ),
                        "NumberOfEntries": ("V", "ns=1;i=2970", {}),
                    },
                ),
            },
        ),
        "PowerlinkVariableType": (
            "VT",
            "ns=1;i=8",
            {
                "DefaultValue": ("V", "ns=1;i=280", {}),
                "Index": ("V", "ns=1;i=277", {}),
                "PowerlinkAttributes": ("V", "ns=1;i=93", {}),
                "Range": ("V", "ns=1;i=279", {}),
                "SubIndex": ("V", "ns=1;i=278", {}),
            },
        ),
    },
}
