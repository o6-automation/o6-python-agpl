# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 21626755812780eecbc6e6e074979a0f12612baf7f63692cad905e75128001fc
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/OPENSCS-SER/"
_VERSION: str = "1.00"
_REQUIRED: list = [{"uri": "http://opcfoundation.org/UA/", "version": "1.04.3"}]
_STRUCTURES: list = [
    (
        "ns=1;i=3002",
        "OPENSCSAggregationDataType",
        "ns=1;i=5002",
        {
            "structure_type": 0,
            "fields": [
                {"name": "ParentElement", "data_type": "ns=1;i=3003", "value_rank": -1},
                {
                    "name": "ParentElementCollection",
                    "data_type": "ns=1;i=15006",
                    "value_rank": -1,
                },
            ],
        },
    ),
    (
        "ns=1;i=15005",
        "OPENSCSCollectionDataType",
        "ns=1;i=15188",
        {
            "structure_type": 0,
            "fields": [
                {"name": "ID", "data_type": "i=12", "value_rank": -1},
                {"name": "Description", "data_type": "i=12", "value_rank": -1},
                {"name": "State", "data_type": "ns=1;i=15143", "value_rank": -1},
                {"name": "AssociatedPoolID", "data_type": "i=12", "value_rank": -1},
                {"name": "SerialNumbers", "data_type": "i=12", "value_rank": 1},
            ],
        },
    ),
    (
        "ns=1;i=15006",
        "OPENSCSLabelCollectionDataType",
        "ns=1;i=15189",
        {
            "structure_type": 1,
            "fields": [
                {
                    "name": "LabelCollection",
                    "data_type": "ns=1;i=3003",
                    "value_rank": 1,
                },
                {
                    "name": "LabelCollectionProperties",
                    "data_type": "ns=1;i=15010",
                    "value_rank": 1,
                    "is_optional": True,
                },
            ],
        },
    ),
    (
        "ns=1;i=3005",
        "OPENSCSEventStreamArgumentDataType",
        "ns=1;i=5008",
        {
            "structure_type": 0,
            "fields": [
                {"name": "SNFormat", "data_type": "i=12", "value_rank": -1},
                {"name": "ParentSNFormat", "data_type": "i=12", "value_rank": -1},
                {
                    "name": "PackedElementSNFormat",
                    "data_type": "i=12",
                    "value_rank": -1,
                },
                {"name": "EventContext", "data_type": "ns=1;i=15010", "value_rank": 1},
            ],
        },
    ),
    (
        "ns=1;i=15010",
        "OPENSCSKeyValueDataType",
        "ns=1;i=15193",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Key", "data_type": "i=12", "value_rank": -1},
                {"name": "Value", "data_type": "i=12", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3003",
        "OPENSCSLabelDataType",
        "ns=1;i=5005",
        {
            "structure_type": 0,
            "fields": [
                {"name": "ID", "data_type": "i=12", "value_rank": -1},
                {
                    "name": "LabelProperties",
                    "data_type": "ns=1;i=15010",
                    "value_rank": 1,
                },
            ],
        },
    ),
    (
        "ns=1;i=15007",
        "OPENSCSLabelPropertyDataType",
        "ns=1;i=15190",
        {
            "structure_type": 0,
            "fields": [
                {"name": "PropertyID", "data_type": "i=12", "value_rank": -1},
                {"name": "PropertyDescription", "data_type": "i=12", "value_rank": -1},
                {"name": "PropertyValue", "data_type": "i=12", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=15009",
        "OPENSCSSIDClassPropertyDataType",
        "ns=1;i=15192",
        {
            "structure_type": 0,
            "fields": [
                {"name": "PropertyID", "data_type": "i=12", "value_rank": -1},
                {"name": "PropertyDescription", "data_type": "i=12", "value_rank": -1},
                {"name": "PropertyValue", "data_type": "i=12", "value_rank": -1},
                {"name": "LabelProperty", "data_type": "ns=1;i=15007", "value_rank": 1},
            ],
        },
    ),
]
_ENUMS: list = [
    (
        "ns=1;i=3006",
        "JobOrderCommandEnum",
        {
            "fields": [
                {"name": "Undefined_0", "value": 0, "display_name": "Undefined_0"},
                {"name": "Store_1", "value": 1, "display_name": "Store_1"},
                {
                    "name": "StoreAndStart_2",
                    "value": 2,
                    "display_name": "StoreAndStart_2",
                },
                {"name": "Start_3", "value": 3, "display_name": "Start_3"},
                {"name": "Update_4", "value": 4, "display_name": "Update_4"},
                {"name": "Stop_5", "value": 5, "display_name": "Stop_5"},
                {"name": "Cancel_6", "value": 6, "display_name": "Cancel_6"},
                {"name": "Clear_7", "value": 7, "display_name": "Clear_7"},
            ]
        },
    ),
    (
        "ns=1;i=3009",
        "JobOrderStateEnum",
        {
            "fields": [
                {"name": "Undefined_0", "value": 0, "display_name": "Undefined_0"},
                {"name": "Waiting_1", "value": 1, "display_name": "Waiting_1"},
                {"name": "Ready_2", "value": 2, "display_name": "Ready_2"},
                {"name": "Loaded_3", "value": 3, "display_name": "Loaded_3"},
                {"name": "Running_4", "value": 4, "display_name": "Running_4"},
                {"name": "Completed_5", "value": 5, "display_name": "Completed_5"},
                {"name": "Aborted_6", "value": 6, "display_name": "Aborted_6"},
                {"name": "Held_7", "value": 7, "display_name": "Held_7"},
                {"name": "Suspended_8", "value": 8, "display_name": "Suspended_8"},
                {"name": "Closed_9", "value": 9, "display_name": "Closed_9"},
            ]
        },
    ),
    (
        "ns=1;i=15001",
        "OPENSCSReturnEnum",
        {
            "fields": [
                {"name": "Undefined0", "value": 0, "display_name": "Undefined0"},
                {"name": "NoError1", "value": 1, "display_name": "NoError1"},
                {
                    "name": "InvalidSerialNumberCollection2",
                    "value": 2,
                    "display_name": "InvalidSerialNumberCollection2",
                },
                {
                    "name": "InsufficientSerialNumbers3",
                    "value": 3,
                    "display_name": "InsufficientSerialNumbers3",
                },
                {
                    "name": "InvalidSerialNumbersFormat4",
                    "value": 4,
                    "display_name": "InvalidSerialNumbersFormat4",
                },
                {
                    "name": "InvalidRequestToken5",
                    "value": 5,
                    "display_name": "InvalidRequestToken5",
                },
                {
                    "name": "InvalidSelectionCriteria6",
                    "value": 6,
                    "display_name": "InvalidSelectionCriteria6",
                },
                {
                    "name": "UnableToAcceptSerialNumberEvents7",
                    "value": 7,
                    "display_name": "UnableToAcceptSerialNumberEvents7",
                },
                {
                    "name": "UnableToAcceptLabelEvents8",
                    "value": 8,
                    "display_name": "UnableToAcceptLabelEvents8",
                },
                {
                    "name": "UnableToAcceptSIDEvents9",
                    "value": 9,
                    "display_name": "UnableToAcceptSIDEvents9",
                },
                {
                    "name": "UnknownAggregationSID10",
                    "value": 10,
                    "display_name": "UnknownAggregationSID10",
                },
                {
                    "name": "InsufficientPrivilegeToExecute11",
                    "value": 11,
                    "display_name": "InsufficientPrivilegeToExecute11",
                },
            ]
        },
    ),
    (
        "ns=1;i=15143",
        "OPENSCSSerialNumberStateEnum",
        {
            "fields": [
                {"name": "Unassigned0", "value": 0, "display_name": "Unassigned0"},
                {"name": "Unallocated1", "value": 1, "display_name": "Unallocated1"},
                {"name": "Allocated2", "value": 2, "display_name": "Allocated2"},
                {"name": "SNInvalid3", "value": 3, "display_name": "SNInvalid3"},
                {"name": "Encoded4", "value": 4, "display_name": "Encoded4"},
                {"name": "LabelSampled5", "value": 5, "display_name": "LabelSampled5"},
                {
                    "name": "LabelScrapped6",
                    "value": 6,
                    "display_name": "LabelScrapped6",
                },
                {"name": "Commissioned7", "value": 7, "display_name": "Commissioned7"},
                {"name": "Sampled8", "value": 8, "display_name": "Sampled8"},
                {"name": "Inactive9", "value": 9, "display_name": "Inactive9"},
                {"name": "Destroyed10", "value": 10, "display_name": "Destroyed10"},
                {"name": "Released11", "value": 11, "display_name": "Released11"},
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = (
    [
        ("ns=1;i=3002", "ns=1;i=5002", ["ns=1;i=3003", "ns=1;i=15006"]),
        (
            "ns=1;i=15005",
            "ns=1;i=15188",
            ["i=12", "i=12", "ns=1;i=15143", "i=12", "i=12"],
        ),
        ("ns=1;i=15006", "ns=1;i=15189", ["ns=1;i=3003", "ns=1;i=15010"]),
        ("ns=1;i=3005", "ns=1;i=5008", ["i=12", "i=12", "i=12", "ns=1;i=15010"]),
        ("ns=1;i=15010", "ns=1;i=15193", ["i=12", "i=12"]),
        ("ns=1;i=3003", "ns=1;i=5005", ["i=12", "ns=1;i=15010"]),
        ("ns=1;i=15007", "ns=1;i=15190", ["i=12", "i=12", "i=12"]),
        ("ns=1;i=15009", "ns=1;i=15192", ["i=12", "i=12", "i=12", "ns=1;i=15007"]),
    ],
    ["ns=1;i=3006", "ns=1;i=3009", "ns=1;i=15001", "ns=1;i=15143"],
)
_NODES: dict = {
    "datatypes": {
        "JobOrderCommandEnum": (
            "D",
            "ns=1;i=3006",
            {"EnumValues": ("V", "ns=1;i=6015", {})},
        ),
        "JobOrderStateEnum": (
            "D",
            "ns=1;i=3009",
            {"EnumValues": ("V", "ns=1;i=6020", {})},
        ),
        "OPENSCSAggregationDataType": ("D", "ns=1;i=3002", {}),
        "OPENSCSCollectionDataType": (
            "D",
            "ns=1;i=15005",
            {
                "OPENSCSLabelCollectionDataType": ("D", "ns=1;i=15006", {}),
                "OPENSCSSNCollectionDataType": ("D", "ns=1;i=15008", {}),
            },
        ),
        "OPENSCSEventStreamArgumentDataType": ("D", "ns=1;i=3005", {}),
        "OPENSCSKeyValueDataType": ("D", "ns=1;i=15010", {}),
        "OPENSCSLabelDataType": ("D", "ns=1;i=3003", {}),
        "OPENSCSLabelPropertyDataType": ("D", "ns=1;i=15007", {}),
        "OPENSCSReturnEnum": (
            "D",
            "ns=1;i=15001",
            {"EnumValues": ("V", "ns=1;i=6008", {})},
        ),
        "OPENSCSSIDClassPropertyDataType": ("D", "ns=1;i=15009", {}),
        "OPENSCSSerialNumberStateEnum": (
            "D",
            "ns=1;i=15143",
            {"EnumValues": ("V", "ns=1;i=6022", {})},
        ),
    },
    "objects": {
        "Default Binary": ("O", "ns=1;i=15193", {}),
        "Default JSON": ("O", "ns=1;i=15249", {}),
        "Default XML": ("O", "ns=1;i=15221", {}),
        "OpenSCS": (
            "V",
            "ns=1;i=15222",
            {
                "Deprecated": ("V", "ns=1;i=15225", {}),
                "NamespaceUri": ("V", "ns=1;i=15224", {}),
                "OPENSCSAggregationDataType": ("V", "ns=1;i=6016", {}),
                "OPENSCSCollectionDataType": ("V", "ns=1;i=15226", {}),
                "OPENSCSEventStreamArgumentDataType": ("V", "ns=1;i=6021", {}),
                "OPENSCSKeyValueDataType": ("V", "ns=1;i=15241", {}),
                "OPENSCSLabelCollectionDataType": ("V", "ns=1;i=15229", {}),
                "OPENSCSLabelDataType": ("V", "ns=1;i=6018", {}),
                "OPENSCSLabelPropertyDataType": ("V", "ns=1;i=15232", {}),
                "OPENSCSSIDClassPropertyDataType": ("V", "ns=1;i=15238", {}),
                "OPENSCSSNCollectionDataType": ("V", "ns=1;i=15235", {}),
            },
        ),
        "http://opcfoundation.org/UA/OPENSCS-SER/": (
            "O",
            "ns=1;i=15011",
            {
                "DefaultAccessRestrictions": ("V", "ns=1;i=15121", {}),
                "DefaultRolePermissions": ("V", "ns=1;i=15119", {}),
                "DefaultUserRolePermissions": ("V", "ns=1;i=15120", {}),
                "IsNamespaceSubset": ("V", "ns=1;i=15015", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=15014", {}),
                "NamespaceUri": ("V", "ns=1;i=15012", {}),
                "NamespaceVersion": ("V", "ns=1;i=15013", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=15016", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=15017", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=15018", {}),
            },
        ),
    },
    "objtypes": {
        "OPENSCSAggregationManagerObjectType": (
            "OT",
            "ns=1;i=15094",
            {
                "AggregationPackingEvent": (
                    "M",
                    "ns=1;i=15099",
                    {
                        "InputArguments": ("V", "ns=1;i=15100", {}),
                        "OutputArguments": ("V", "ns=1;i=15101", {}),
                    },
                ),
                "AggregationUnpackingEvent": (
                    "M",
                    "ns=1;i=7004",
                    {
                        "InputArguments": ("V", "ns=1;i=6011", {}),
                        "OutputArguments": ("V", "ns=1;i=6013", {}),
                    },
                ),
                "MaxAggregationEvents": ("V", "ns=1;i=15095", {}),
            },
        ),
        "OPENSCSEventManagerObjectType": (
            "OT",
            "ns=1;i=15062",
            {
                "EPCISStream": (
                    "O",
                    "ns=1;i=5001",
                    {
                        "ClientProcessingTimeout": ("V", "ns=1;i=6001", {}),
                        "CloseAndCommit": (
                            "M",
                            "ns=1;i=7001",
                            {
                                "InputArguments": ("V", "ns=1;i=6002", {}),
                                "OutputArguments": ("V", "ns=1;i=6003", {}),
                            },
                        ),
                        "GenerateFileForRead": (
                            "M",
                            "ns=1;i=7002",
                            {
                                "InputArguments": ("V", "ns=1;i=6004", {}),
                                "OutputArguments": ("V", "ns=1;i=6005", {}),
                            },
                        ),
                        "GenerateFileForWrite": (
                            "M",
                            "ns=1;i=7003",
                            {
                                "InputArguments": ("V", "ns=1;i=6006", {}),
                                "OutputArguments": ("V", "ns=1;i=6007", {}),
                            },
                        ),
                    },
                ),
                "LabelsEncodingEvent": (
                    "M",
                    "ns=1;i=15088",
                    {
                        "InputArguments": ("V", "ns=1;i=15089", {}),
                        "OutputArguments": ("V", "ns=1;i=15090", {}),
                    },
                ),
                "LabelsInspectingEvent": (
                    "M",
                    "ns=1;i=15082",
                    {
                        "InputArguments": ("V", "ns=1;i=15083", {}),
                        "OutputArguments": ("V", "ns=1;i=15084", {}),
                    },
                ),
                "LabelsSamplingEvent": (
                    "M",
                    "ns=1;i=15079",
                    {
                        "InputArguments": ("V", "ns=1;i=15080", {}),
                        "OutputArguments": ("V", "ns=1;i=15081", {}),
                    },
                ),
                "LabelsScrappingEvent": (
                    "M",
                    "ns=1;i=15085",
                    {
                        "InputArguments": ("V", "ns=1;i=15086", {}),
                        "OutputArguments": ("V", "ns=1;i=15087", {}),
                    },
                ),
                "MaxEPCISObjectEventSIDs": ("V", "ns=1;i=6009", {}),
                "MaxEPCISaggregationEvents": ("V", "ns=1;i=6010", {}),
                "MaxEvents": ("V", "ns=1;i=15063", {}),
                "SIDCommissioningEvent": (
                    "M",
                    "ns=1;i=15076",
                    {
                        "InputArguments": ("V", "ns=1;i=15077", {}),
                        "OutputArguments": ("V", "ns=1;i=15078", {}),
                    },
                ),
                "SIDDecommissioningEvent": (
                    "M",
                    "ns=1;i=15064",
                    {
                        "InputArguments": ("V", "ns=1;i=15065", {}),
                        "OutputArguments": ("V", "ns=1;i=15066", {}),
                    },
                ),
                "SIDDestroyingEvent": (
                    "M",
                    "ns=1;i=15073",
                    {
                        "InputArguments": ("V", "ns=1;i=15074", {}),
                        "OutputArguments": ("V", "ns=1;i=15075", {}),
                    },
                ),
                "SIDInspectingEvent": (
                    "M",
                    "ns=1;i=15067",
                    {
                        "InputArguments": ("V", "ns=1;i=15068", {}),
                        "OutputArguments": ("V", "ns=1;i=15069", {}),
                    },
                ),
                "SIDShippingEvent": (
                    "M",
                    "ns=1;i=15070",
                    {
                        "InputArguments": ("V", "ns=1;i=15071", {}),
                        "OutputArguments": ("V", "ns=1;i=15072", {}),
                    },
                ),
                "SNInvalidatingEvent": (
                    "M",
                    "ns=1;i=15091",
                    {
                        "InputArguments": ("V", "ns=1;i=15092", {}),
                        "OutputArguments": ("V", "ns=1;i=15093", {}),
                    },
                ),
            },
        ),
        "OPENSCSPoolManagerObjectType": (
            "OT",
            "ns=1;i=15032",
            {
                "MaxSNPushable": ("V", "ns=1;i=15034", {}),
                "MaxSNRequestable": ("V", "ns=1;i=15036", {}),
                "MaxSNReturnable": ("V", "ns=1;i=15035", {}),
                "PoolSelectionCriteria": ("V", "ns=1;i=15033", {}),
                "SNFormat": ("V", "ns=1;i=15037", {}),
                "SNRequestAllocated": (
                    "M",
                    "ns=1;i=15053",
                    {
                        "InputArguments": ("V", "ns=1;i=15054", {}),
                        "OutputArguments": ("V", "ns=1;i=15055", {}),
                    },
                ),
                "SNRequestUnallocated": (
                    "M",
                    "ns=1;i=15056",
                    {
                        "InputArguments": ("V", "ns=1;i=15057", {}),
                        "OutputArguments": ("V", "ns=1;i=15058", {}),
                    },
                ),
                "SNRequestUnassigned": (
                    "M",
                    "ns=1;i=15059",
                    {
                        "InputArguments": ("V", "ns=1;i=15060", {}),
                        "OutputArguments": ("V", "ns=1;i=15061", {}),
                    },
                ),
                "SNReturnAllocated": (
                    "M",
                    "ns=1;i=15047",
                    {
                        "InputArguments": ("V", "ns=1;i=15048", {}),
                        "OutputArguments": ("V", "ns=1;i=15049", {}),
                    },
                ),
                "SNReturnUnallocated": (
                    "M",
                    "ns=1;i=15050",
                    {
                        "InputArguments": ("V", "ns=1;i=15051", {}),
                        "OutputArguments": ("V", "ns=1;i=15052", {}),
                    },
                ),
                "SNtoAllocated": (
                    "M",
                    "ns=1;i=15110",
                    {
                        "InputArguments": ("V", "ns=1;i=15111", {}),
                        "OutputArguments": ("V", "ns=1;i=15112", {}),
                    },
                ),
                "SNtoEncoded": (
                    "M",
                    "ns=1;i=15038",
                    {
                        "InputArguments": ("V", "ns=1;i=15039", {}),
                        "OutputArguments": ("V", "ns=1;i=15040", {}),
                    },
                ),
                "SNtoUnallocated": (
                    "M",
                    "ns=1;i=15044",
                    {
                        "InputArguments": ("V", "ns=1;i=15045", {}),
                        "OutputArguments": ("V", "ns=1;i=15046", {}),
                    },
                ),
            },
        ),
        "OPENSCSSIDClassObjectType": (
            "OT",
            "ns=1;i=15102",
            {
                "AllowedCharacterSet": ("V", "ns=1;i=15105", {}),
                "IntendedUse": ("V", "ns=1;i=15104", {}),
                "SIDClassDescription": ("V", "ns=1;i=15107", {}),
                "SIDClassID": ("V", "ns=1;i=15109", {}),
                "SIDClassOwner": ("V", "ns=1;i=15108", {}),
                "SIDClassProperty": ("V", "ns=1;i=6012", {}),
                "SyntaxSpecification": ("V", "ns=1;i=15106", {}),
            },
        ),
    },
}
