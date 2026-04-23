# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 3e67454155a9618e0981aa8b3ee248f7a9ee216f9f915b53eb26a69533c0cc62
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/MachineVision"
_VERSION: str = "1.0.0"
_REQUIRED: list = [{"uri": "http://opcfoundation.org/UA/", "version": "1.04"}]
_STRUCTURES: list = [
    (
        "ns=1;i=3019",
        "BinaryIdBaseDataType",
        "ns=1;i=5027",
        {
            "structure_type": 1,
            "fields": [
                {"name": "Id", "data_type": "i=12", "value_rank": -1},
                {
                    "name": "Version",
                    "data_type": "i=12",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "Hash",
                    "data_type": "i=15",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "HashAlgorithm",
                    "data_type": "i=12",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "Description",
                    "data_type": "i=21",
                    "value_rank": -1,
                    "is_optional": True,
                },
            ],
        },
    ),
    (
        "ns=1;i=3008",
        "ConfigurationIdDataType",
        "ns=1;i=5090",
        {"structure_type": 0, "fields": []},
    ),
    (
        "ns=1;i=3002",
        "RecipeIdExternalDataType",
        "ns=1;i=5002",
        {"structure_type": 0, "fields": []},
    ),
    (
        "ns=1;i=3013",
        "RecipeIdInternalDataType",
        "ns=1;i=5268",
        {"structure_type": 0, "fields": []},
    ),
    (
        "ns=1;i=3007",
        "ConfigurationDataType",
        "ns=1;i=5088",
        {
            "structure_type": 1,
            "fields": [
                {
                    "name": "HasTransferableDataOnFile",
                    "data_type": "i=1",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "ExternalId",
                    "data_type": "ns=1;i=3008",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {"name": "InternalId", "data_type": "ns=1;i=3008", "value_rank": -1},
                {"name": "LastModified", "data_type": "i=294", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3011",
        "ConfigurationTransferOptions",
        "ns=1;i=5246",
        {
            "structure_type": 0,
            "fields": [
                {"name": "InternalId", "data_type": "ns=1;i=3008", "value_rank": -1}
            ],
        },
    ),
    (
        "ns=1;i=3016",
        "JobIdDataType",
        "ns=1;i=5008",
        {
            "structure_type": 0,
            "fields": [{"name": "Id", "data_type": "i=12", "value_rank": -1}],
        },
    ),
    (
        "ns=1;i=3015",
        "MeasIdDataType",
        "ns=1;i=5006",
        {
            "structure_type": 1,
            "fields": [
                {"name": "Id", "data_type": "i=12", "value_rank": -1},
                {
                    "name": "Description",
                    "data_type": "i=21",
                    "value_rank": -1,
                    "is_optional": True,
                },
            ],
        },
    ),
    (
        "ns=1;i=3004",
        "PartIdDataType",
        "ns=1;i=5013",
        {
            "structure_type": 1,
            "fields": [
                {"name": "Id", "data_type": "i=12", "value_rank": -1},
                {
                    "name": "Description",
                    "data_type": "i=21",
                    "value_rank": -1,
                    "is_optional": True,
                },
            ],
        },
    ),
    (
        "ns=1;i=3005",
        "ProcessingTimesDataType",
        "ns=1;i=5016",
        {
            "structure_type": 1,
            "fields": [
                {"name": "StartTime", "data_type": "i=294", "value_rank": -1},
                {"name": "EndTime", "data_type": "i=294", "value_rank": -1},
                {
                    "name": "AcquisitionDuration",
                    "data_type": "i=290",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "ProcessingDuration",
                    "data_type": "i=290",
                    "value_rank": -1,
                    "is_optional": True,
                },
            ],
        },
    ),
    (
        "ns=1;i=3020",
        "ProductDataType",
        "ns=1;i=5272",
        {
            "structure_type": 0,
            "fields": [
                {"name": "ExternalId", "data_type": "ns=1;i=3003", "value_rank": -1}
            ],
        },
    ),
    (
        "ns=1;i=3003",
        "ProductIdDataType",
        "ns=1;i=5224",
        {
            "structure_type": 1,
            "fields": [
                {"name": "Id", "data_type": "i=12", "value_rank": -1},
                {
                    "name": "Description",
                    "data_type": "i=21",
                    "value_rank": -1,
                    "is_optional": True,
                },
            ],
        },
    ),
    (
        "ns=1;i=3012",
        "RecipeTransferOptions",
        "ns=1;i=5248",
        {
            "structure_type": 0,
            "fields": [
                {"name": "InternalId", "data_type": "ns=1;i=3013", "value_rank": -1}
            ],
        },
    ),
    (
        "ns=1;i=3006",
        "ResultDataType",
        "ns=1;i=5018",
        {
            "structure_type": 1,
            "fields": [
                {"name": "ResultId", "data_type": "ns=1;i=3021", "value_rank": -1},
                {
                    "name": "HasTransferableDataOnFile",
                    "data_type": "i=1",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {"name": "IsPartial", "data_type": "i=1", "value_rank": -1},
                {
                    "name": "IsSimulated",
                    "data_type": "i=1",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {"name": "ResultState", "data_type": "i=6", "value_rank": -1},
                {
                    "name": "MeasId",
                    "data_type": "ns=1;i=3015",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "PartId",
                    "data_type": "ns=1;i=3004",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "ExternalRecipeId",
                    "data_type": "ns=1;i=3002",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "InternalRecipeId",
                    "data_type": "ns=1;i=3013",
                    "value_rank": -1,
                },
                {
                    "name": "ProductId",
                    "data_type": "ns=1;i=3003",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "ExternalConfigurationId",
                    "data_type": "ns=1;i=3008",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "InternalConfigurationId",
                    "data_type": "ns=1;i=3008",
                    "value_rank": -1,
                },
                {"name": "JobId", "data_type": "ns=1;i=3016", "value_rank": -1},
                {"name": "CreationTime", "data_type": "i=294", "value_rank": -1},
                {
                    "name": "ProcessingTimes",
                    "data_type": "ns=1;i=3005",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "ResultContent",
                    "data_type": "i=24",
                    "value_rank": 1,
                    "is_optional": True,
                },
            ],
        },
    ),
    (
        "ns=1;i=3021",
        "ResultIdDataType",
        "ns=1;i=5274",
        {
            "structure_type": 0,
            "fields": [{"name": "Id", "data_type": "i=12", "value_rank": -1}],
        },
    ),
    (
        "ns=1;i=3022",
        "ResultTransferOptions",
        "ns=1;i=5276",
        {
            "structure_type": 0,
            "fields": [{"name": "Id", "data_type": "ns=1;i=3021", "value_rank": -1}],
        },
    ),
    (
        "ns=1;i=3024",
        "SystemStateDescriptionDataType",
        "ns=1;i=5278",
        {
            "structure_type": 1,
            "fields": [
                {"name": "State", "data_type": "ns=1;i=3023", "value_rank": -1},
                {
                    "name": "StateDescription",
                    "data_type": "i=12",
                    "value_rank": -1,
                    "is_optional": True,
                },
            ],
        },
    ),
]
_ENUMS: list = [
    (
        "ns=1;i=3023",
        "SystemStateDataType",
        {
            "fields": [
                {"name": "PRD_1", "value": 1, "display_name": "PRD_1"},
                {"name": "SBY_2", "value": 2, "display_name": "SBY_2"},
                {"name": "ENG_3", "value": 3, "display_name": "ENG_3"},
                {"name": "SDT_4", "value": 4, "display_name": "SDT_4"},
                {"name": "UDT_5", "value": 5, "display_name": "UDT_5"},
                {"name": "NST_6", "value": 6, "display_name": "NST_6"},
            ]
        },
    ),
    (
        "ns=1;i=3014",
        "TriStateBooleanDataType",
        {
            "fields": [
                {"name": "FALSE_0", "value": 0, "display_name": "FALSE_0"},
                {"name": "TRUE_1", "value": 1, "display_name": "TRUE_1"},
                {"name": "DONTCARE_2", "value": 2, "display_name": "DONTCARE_2"},
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = (
    [
        ("ns=1;i=3019", "ns=1;i=5027", ["i=12", "i=12", "i=15", "i=12", "i=21"]),
        ("ns=1;i=3008", "ns=1;i=5090", []),
        ("ns=1;i=3002", "ns=1;i=5002", []),
        ("ns=1;i=3013", "ns=1;i=5268", []),
        ("ns=1;i=3007", "ns=1;i=5088", ["i=1", "ns=1;i=3008", "ns=1;i=3008", "i=294"]),
        ("ns=1;i=3011", "ns=1;i=5246", ["ns=1;i=3008"]),
        ("ns=1;i=3016", "ns=1;i=5008", ["i=12"]),
        ("ns=1;i=3015", "ns=1;i=5006", ["i=12", "i=21"]),
        ("ns=1;i=3004", "ns=1;i=5013", ["i=12", "i=21"]),
        ("ns=1;i=3005", "ns=1;i=5016", ["i=294", "i=294", "i=290", "i=290"]),
        ("ns=1;i=3020", "ns=1;i=5272", ["ns=1;i=3003"]),
        ("ns=1;i=3003", "ns=1;i=5224", ["i=12", "i=21"]),
        ("ns=1;i=3012", "ns=1;i=5248", ["ns=1;i=3013"]),
        (
            "ns=1;i=3006",
            "ns=1;i=5018",
            [
                "ns=1;i=3021",
                "i=1",
                "i=1",
                "i=1",
                "i=6",
                "ns=1;i=3015",
                "ns=1;i=3004",
                "ns=1;i=3002",
                "ns=1;i=3013",
                "ns=1;i=3003",
                "ns=1;i=3008",
                "ns=1;i=3008",
                "ns=1;i=3016",
                "i=294",
                "ns=1;i=3005",
                "i=24",
            ],
        ),
        ("ns=1;i=3021", "ns=1;i=5274", ["i=12"]),
        ("ns=1;i=3022", "ns=1;i=5276", ["ns=1;i=3021"]),
        ("ns=1;i=3024", "ns=1;i=5278", ["ns=1;i=3023", "i=12"]),
    ],
    ["ns=1;i=3023", "ns=1;i=3014"],
)
_NODES: dict = {
    "datatypes": {
        "BinaryIdBaseDataType": (
            "D",
            "ns=1;i=3019",
            {
                "ConfigurationIdDataType": ("D", "ns=1;i=3008", {}),
                "RecipeIdExternalDataType": ("D", "ns=1;i=3002", {}),
                "RecipeIdInternalDataType": ("D", "ns=1;i=3013", {}),
            },
        ),
        "ConfigurationDataType": ("D", "ns=1;i=3007", {}),
        "ConfigurationTransferOptions": ("D", "ns=1;i=3011", {}),
        "Handle": ("D", "ns=1;i=3018", {}),
        "JobIdDataType": ("D", "ns=1;i=3016", {}),
        "MeasIdDataType": ("D", "ns=1;i=3015", {}),
        "PartIdDataType": ("D", "ns=1;i=3004", {}),
        "ProcessingTimesDataType": ("D", "ns=1;i=3005", {}),
        "ProductDataType": ("D", "ns=1;i=3020", {}),
        "ProductIdDataType": ("D", "ns=1;i=3003", {}),
        "RecipeTransferOptions": ("D", "ns=1;i=3012", {}),
        "ResultDataType": ("D", "ns=1;i=3006", {}),
        "ResultIdDataType": ("D", "ns=1;i=3021", {}),
        "ResultStateDataType": ("D", "ns=1;i=3009", {}),
        "ResultTransferOptions": ("D", "ns=1;i=3022", {}),
        "SystemStateDataType": (
            "D",
            "ns=1;i=3023",
            {"EnumValues": ("V", "ns=1;i=6032", {})},
        ),
        "SystemStateDescriptionDataType": ("D", "ns=1;i=3024", {}),
        "TriStateBooleanDataType": (
            "D",
            "ns=1;i=3014",
            {"EnumValues": ("V", "ns=1;i=6367", {})},
        ),
        "TrimmedString": ("D", "ns=1;i=3017", {}),
    },
    "eventtypes": {
        "AcquisitionDoneEventType": (
            "OT",
            "ns=1;i=1025",
            {"JobId": ("V", "ns=1;i=6308", {})},
        ),
        "EnterStepSequenceEventType": (
            "OT",
            "ns=1;i=1027",
            {"Steps": ("V", "ns=1;i=6322", {})},
        ),
        "ErrorEventType": ("OT", "ns=1;i=1019", {}),
        "ErrorResolvedEventType": ("OT", "ns=1;i=1020", {}),
        "JobStartedEventType": (
            "OT",
            "ns=1;i=1013",
            {"JobId": ("V", "ns=1;i=6141", {})},
        ),
        "LeaveStepSequenceEventType": ("OT", "ns=1;i=1029", {}),
        "NextStepEventType": ("OT", "ns=1;i=1028", {"Step": ("V", "ns=1;i=6324", {})}),
        "ReadyEventType": ("OT", "ns=1;i=1023", {"JobId": ("V", "ns=1;i=6294", {})}),
        "RecipePreparedEventType": (
            "OT",
            "ns=1;i=1022",
            {
                "ExternalId": ("V", "ns=1;i=6291", {}),
                "InternalId": ("V", "ns=1;i=6140", {}),
                "ProductId": ("V", "ns=1;i=6292", {}),
            },
        ),
        "ResultReadyEventType": (
            "OT",
            "ns=1;i=1024",
            {
                "CreationTime": ("V", "ns=1;i=6303", {}),
                "ExternalConfigurationId": ("V", "ns=1;i=6045", {}),
                "ExternalRecipeId": ("V", "ns=1;i=6301", {}),
                "InternalConfigurationId": ("V", "ns=1;i=6142", {}),
                "InternalRecipeId": ("V", "ns=1;i=6302", {}),
                "IsPartial": ("V", "ns=1;i=6296", {}),
                "IsSimulated": ("V", "ns=1;i=6297", {}),
                "JobId": ("V", "ns=1;i=6300", {}),
                "MeasId": ("V", "ns=1;i=6299", {}),
                "PartId": ("V", "ns=1;i=6304", {}),
                "ProcessingTimes": ("V", "ns=1;i=6305", {}),
                "ProductId": ("V", "ns=1;i=6143", {}),
                "ResultContent": ("V", "ns=1;i=6306", {}),
                "ResultId": ("V", "ns=1;i=6295", {}),
                "ResultState": ("V", "ns=1;i=6298", {}),
            },
        ),
        "StateChangedEventType": ("OT", "ns=1;i=1018", {}),
        "VisionEventType": (
            "OT",
            "ns=1;i=1015",
            {
                "CausePath": ("V", "ns=1;i=6193", {}),
                "ExternalConfigurationId": ("V", "ns=1;i=6550", {}),
                "ExternalRecipeId": ("V", "ns=1;i=6195", {}),
                "InternalConfigurationId": ("V", "ns=1;i=6200", {}),
                "InternalRecipeId": ("V", "ns=1;i=6198", {}),
                "JobId": ("V", "ns=1;i=6203", {}),
                "MeasId": ("V", "ns=1;i=6194", {}),
                "PartId": ("V", "ns=1;i=6201", {}),
                "ProductId": ("V", "ns=1;i=6199", {}),
                "ResultId": ("V", "ns=1;i=6204", {}),
                "VisionDiagnosticInfoEventType": ("OT", "ns=1;i=1037", {}),
                "VisionInformationEventType": ("OT", "ns=1;i=1038", {}),
            },
        ),
        "VisionSafetyEventType": (
            "OT",
            "ns=1;i=1030",
            {
                "VisionSafetyInformation": ("V", "ns=1;i=6050", {}),
                "VisionSafetyTriggered": ("V", "ns=1;i=6051", {}),
            },
        ),
    },
    "objects": {
        "Default Binary": ("O", "ns=1;i=5278", {}),
        "Default XML": ("O", "ns=1;i=5279", {}),
        "TypeDictionary": (
            "V",
            "ns=1;i=6003",
            {
                "BinaryIdBaseDataType": ("V", "ns=1;i=6034", {}),
                "ConfigurationDataType": ("V", "ns=1;i=6353", {}),
                "ConfigurationIdDataType": ("V", "ns=1;i=6355", {}),
                "ConfigurationTransferOptions": ("V", "ns=1;i=6126", {}),
                "JobIdDataType": ("V", "ns=1;i=6031", {}),
                "MeasIdDataType": ("V", "ns=1;i=6029", {}),
                "NamespaceUri": ("V", "ns=1;i=6020", {}),
                "PartIdDataType": ("V", "ns=1;i=6073", {}),
                "ProcessingTimesDataType": ("V", "ns=1;i=6075", {}),
                "ProductDataType": ("V", "ns=1;i=6038", {}),
                "ProductIdDataType": ("V", "ns=1;i=6093", {}),
                "RecipeIdExternalDataType": ("V", "ns=1;i=6022", {}),
                "RecipeIdInternalDataType": ("V", "ns=1;i=6036", {}),
                "RecipeTransferOptions": ("V", "ns=1;i=6189", {}),
                "ResultDataType": ("V", "ns=1;i=6077", {}),
                "ResultIdDataType": ("V", "ns=1;i=6040", {}),
                "ResultTransferOptions": ("V", "ns=1;i=6128", {}),
                "SystemStateDescriptionDataType": ("V", "ns=1;i=6131", {}),
            },
        ),
        "http://opcfoundation.org/UA/MachineVision": (
            "O",
            "ns=1;i=5009",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=6549", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=6552", {}),
                "NamespaceUri": ("V", "ns=1;i=6553", {}),
                "NamespaceVersion": ("V", "ns=1;i=6554", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=6556", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=6558", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=6559", {}),
            },
        ),
    },
    "objtypes": {
        "ConfigurationFolderType": (
            "OT",
            "ns=1;i=1011",
            {"<Configuration>": ("V", "ns=1;i=6120", {})},
        ),
        "ConfigurationManagementType": (
            "OT",
            "ns=1;i=1006",
            {
                "ActivateConfiguration": (
                    "M",
                    "ns=1;i=7048",
                    {
                        "InputArguments": ("V", "ns=1;i=6116", {}),
                        "OutputArguments": ("V", "ns=1;i=6117", {}),
                    },
                ),
                "ActiveConfiguration": ("V", "ns=1;i=6132", {}),
                "AddConfiguration": (
                    "M",
                    "ns=1;i=7025",
                    {
                        "InputArguments": ("V", "ns=1;i=6096", {}),
                        "OutputArguments": ("V", "ns=1;i=6097", {}),
                    },
                ),
                "ConfigurationTransfer": (
                    "O",
                    "ns=1;i=5266",
                    {
                        "ClientProcessingTimeout": ("V", "ns=1;i=6599", {}),
                        "CloseAndCommit": (
                            "M",
                            "ns=1;i=7113",
                            {
                                "InputArguments": ("V", "ns=1;i=6600", {}),
                                "OutputArguments": ("V", "ns=1;i=6601", {}),
                            },
                        ),
                        "GenerateFileForRead": (
                            "M",
                            "ns=1;i=7012",
                            {
                                "InputArguments": ("V", "ns=1;i=6337", {}),
                                "OutputArguments": ("V", "ns=1;i=6338", {}),
                            },
                        ),
                        "GenerateFileForWrite": (
                            "M",
                            "ns=1;i=7029",
                            {
                                "InputArguments": ("V", "ns=1;i=6339", {}),
                                "OutputArguments": ("V", "ns=1;i=6340", {}),
                            },
                        ),
                    },
                ),
                "Configurations": ("O", "ns=1;i=5010", {}),
                "GetConfigurationById": (
                    "M",
                    "ns=1;i=7041",
                    {
                        "InputArguments": ("V", "ns=1;i=6100", {}),
                        "OutputArguments": ("V", "ns=1;i=6101", {}),
                    },
                ),
                "GetConfigurationList": (
                    "M",
                    "ns=1;i=7045",
                    {
                        "InputArguments": ("V", "ns=1;i=6104", {}),
                        "OutputArguments": ("V", "ns=1;i=6105", {}),
                    },
                ),
                "ReleaseConfigurationHandle": (
                    "M",
                    "ns=1;i=7046",
                    {
                        "InputArguments": ("V", "ns=1;i=6108", {}),
                        "OutputArguments": ("V", "ns=1;i=6109", {}),
                    },
                ),
                "RemoveConfiguration": (
                    "M",
                    "ns=1;i=7047",
                    {
                        "InputArguments": ("V", "ns=1;i=6112", {}),
                        "OutputArguments": ("V", "ns=1;i=6113", {}),
                    },
                ),
            },
        ),
        "ConfigurationTransferType": (
            "OT",
            "ns=1;i=1012",
            {
                "GenerateFileForRead": (
                    "M",
                    "ns=1;i=7129",
                    {
                        "InputArguments": ("V", "ns=1;i=6617", {}),
                        "OutputArguments": ("V", "ns=1;i=6618", {}),
                    },
                ),
                "GenerateFileForWrite": (
                    "M",
                    "ns=1;i=7130",
                    {
                        "InputArguments": ("V", "ns=1;i=6121", {}),
                        "OutputArguments": ("V", "ns=1;i=6122", {}),
                    },
                ),
            },
        ),
        "ProductFolderType": (
            "OT",
            "ns=1;i=1010",
            {"<Product>": ("V", "ns=1;i=6621", {})},
        ),
        "RecipeFolderType": (
            "OT",
            "ns=1;i=1008",
            {
                "<Recipe>": (
                    "O",
                    "ns=1;i=5270",
                    {
                        "ExternalId": ("V", "ns=1;i=6608", {}),
                        "InternalId": ("V", "ns=1;i=6609", {}),
                        "IsPrepared": ("V", "ns=1;i=6610", {}),
                        "LastModified": ("V", "ns=1;i=6611", {}),
                        "LinkProduct": (
                            "M",
                            "ns=1;i=7076",
                            {
                                "InputArguments": ("V", "ns=1;i=6613", {}),
                                "OutputArguments": ("V", "ns=1;i=6614", {}),
                            },
                        ),
                        "LinkedProducts": ("V", "ns=1;i=6612", {}),
                        "Prepare": (
                            "M",
                            "ns=1;i=7114",
                            {"OutputArguments": ("V", "ns=1;i=6615", {})},
                        ),
                        "UnlinkProduct": (
                            "M",
                            "ns=1;i=7120",
                            {
                                "InputArguments": ("V", "ns=1;i=6616", {}),
                                "OutputArguments": ("V", "ns=1;i=6619", {}),
                            },
                        ),
                        "Unprepare": (
                            "M",
                            "ns=1;i=7121",
                            {"OutputArguments": ("V", "ns=1;i=6620", {})},
                        ),
                    },
                )
            },
        ),
        "RecipeManagementType": (
            "OT",
            "ns=1;i=1004",
            {
                "AddRecipe": (
                    "M",
                    "ns=1;i=7013",
                    {
                        "InputArguments": ("V", "ns=1;i=6144", {}),
                        "OutputArguments": ("V", "ns=1;i=6145", {}),
                    },
                ),
                "GetRecipeListFiltered": (
                    "M",
                    "ns=1;i=7014",
                    {
                        "InputArguments": ("V", "ns=1;i=6156", {}),
                        "OutputArguments": ("V", "ns=1;i=6157", {}),
                    },
                ),
                "PrepareProduct": (
                    "M",
                    "ns=1;i=7060",
                    {
                        "InputArguments": ("V", "ns=1;i=6172", {}),
                        "OutputArguments": ("V", "ns=1;i=6173", {}),
                    },
                ),
                "PrepareRecipe": (
                    "M",
                    "ns=1;i=7015",
                    {
                        "InputArguments": ("V", "ns=1;i=6148", {}),
                        "OutputArguments": ("V", "ns=1;i=6149", {}),
                    },
                ),
                "Products": (
                    "O",
                    "ns=1;i=5022",
                    {"<Product>": ("V", "ns=1;i=6622", {})},
                ),
                "RecipeTransfer": (
                    "O",
                    "ns=1;i=5264",
                    {
                        "ClientProcessingTimeout": ("V", "ns=1;i=6585", {}),
                        "CloseAndCommit": (
                            "M",
                            "ns=1;i=7115",
                            {
                                "InputArguments": ("V", "ns=1;i=6586", {}),
                                "OutputArguments": ("V", "ns=1;i=6587", {}),
                            },
                        ),
                        "GenerateFileForRead": (
                            "M",
                            "ns=1;i=7118",
                            {
                                "InputArguments": ("V", "ns=1;i=6186", {}),
                                "OutputArguments": ("V", "ns=1;i=6187", {}),
                            },
                        ),
                        "GenerateFileForWrite": (
                            "M",
                            "ns=1;i=7119",
                            {
                                "InputArguments": ("V", "ns=1;i=6588", {}),
                                "OutputArguments": ("V", "ns=1;i=6589", {}),
                            },
                        ),
                    },
                ),
                "Recipes": ("O", "ns=1;i=5005", {}),
                "ReleaseRecipeHandle": (
                    "M",
                    "ns=1;i=7056",
                    {
                        "InputArguments": ("V", "ns=1;i=6160", {}),
                        "OutputArguments": ("V", "ns=1;i=6161", {}),
                    },
                ),
                "RemoveRecipe": (
                    "M",
                    "ns=1;i=7057",
                    {
                        "InputArguments": ("V", "ns=1;i=6164", {}),
                        "OutputArguments": ("V", "ns=1;i=6165", {}),
                    },
                ),
                "UnlinkProduct": (
                    "M",
                    "ns=1;i=7061",
                    {
                        "InputArguments": ("V", "ns=1;i=6180", {}),
                        "OutputArguments": ("V", "ns=1;i=6181", {}),
                    },
                ),
                "UnprepareProduct": (
                    "M",
                    "ns=1;i=7059",
                    {
                        "InputArguments": ("V", "ns=1;i=6176", {}),
                        "OutputArguments": ("V", "ns=1;i=6177", {}),
                    },
                ),
                "UnprepareRecipe": (
                    "M",
                    "ns=1;i=7055",
                    {
                        "InputArguments": ("V", "ns=1;i=6152", {}),
                        "OutputArguments": ("V", "ns=1;i=6153", {}),
                    },
                ),
            },
        ),
        "RecipeTransferType": (
            "OT",
            "ns=1;i=1014",
            {
                "GenerateFileForRead": (
                    "M",
                    "ns=1;i=7123",
                    {
                        "InputArguments": ("V", "ns=1;i=6184", {}),
                        "OutputArguments": ("V", "ns=1;i=6185", {}),
                    },
                ),
                "GenerateFileForWrite": (
                    "M",
                    "ns=1;i=7124",
                    {
                        "InputArguments": ("V", "ns=1;i=6583", {}),
                        "OutputArguments": ("V", "ns=1;i=6584", {}),
                    },
                ),
            },
        ),
        "RecipeType": (
            "OT",
            "ns=1;i=1002",
            {
                "ExternalId": ("V", "ns=1;i=6023", {}),
                "Handle": (
                    "O",
                    "ns=1;i=5001",
                    {
                        "Close": (
                            "M",
                            "ns=1;i=7001",
                            {"InputArguments": ("V", "ns=1;i=6004", {})},
                        ),
                        "GetPosition": (
                            "M",
                            "ns=1;i=7002",
                            {
                                "InputArguments": ("V", "ns=1;i=6005", {}),
                                "OutputArguments": ("V", "ns=1;i=6006", {}),
                            },
                        ),
                        "Open": (
                            "M",
                            "ns=1;i=7003",
                            {
                                "InputArguments": ("V", "ns=1;i=6007", {}),
                                "OutputArguments": ("V", "ns=1;i=6008", {}),
                            },
                        ),
                        "OpenCount": ("V", "ns=1;i=6009", {}),
                        "Read": (
                            "M",
                            "ns=1;i=7004",
                            {
                                "InputArguments": ("V", "ns=1;i=6010", {}),
                                "OutputArguments": ("V", "ns=1;i=6011", {}),
                            },
                        ),
                        "SetPosition": (
                            "M",
                            "ns=1;i=7005",
                            {"InputArguments": ("V", "ns=1;i=6012", {})},
                        ),
                        "Size": ("V", "ns=1;i=6013", {}),
                        "UserWritable": ("V", "ns=1;i=6014", {}),
                        "Writable": ("V", "ns=1;i=6015", {}),
                        "Write": (
                            "M",
                            "ns=1;i=7006",
                            {"InputArguments": ("V", "ns=1;i=6016", {})},
                        ),
                    },
                ),
                "InternalId": ("V", "ns=1;i=6019", {}),
                "IsPrepared": ("V", "ns=1;i=6605", {}),
                "LastModified": ("V", "ns=1;i=6017", {}),
                "LinkProduct": (
                    "M",
                    "ns=1;i=7062",
                    {
                        "InputArguments": ("V", "ns=1;i=6190", {}),
                        "OutputArguments": ("V", "ns=1;i=6191", {}),
                    },
                ),
                "LinkedProducts": ("V", "ns=1;i=6018", {}),
                "Prepare": (
                    "M",
                    "ns=1;i=7064",
                    {"OutputArguments": ("V", "ns=1;i=6202", {})},
                ),
                "UnlinkProduct": (
                    "M",
                    "ns=1;i=7063",
                    {
                        "InputArguments": ("V", "ns=1;i=6196", {}),
                        "OutputArguments": ("V", "ns=1;i=6197", {}),
                    },
                ),
                "Unprepare": (
                    "M",
                    "ns=1;i=7065",
                    {"OutputArguments": ("V", "ns=1;i=6205", {})},
                ),
            },
        ),
        "ResultFolderType": (
            "OT",
            "ns=1;i=1016",
            {
                "<ResultVariable>": (
                    "V",
                    "ns=1;i=6168",
                    {
                        "CreationTime": ("V", "ns=1;i=6334", {}),
                        "InternalConfigurationId": ("V", "ns=1;i=6335", {}),
                        "InternalRecipeId": ("V", "ns=1;i=6336", {}),
                        "IsPartial": ("V", "ns=1;i=6356", {}),
                        "JobId": ("V", "ns=1;i=6357", {}),
                        "ResultId": ("V", "ns=1;i=6379", {}),
                        "ResultState": ("V", "ns=1;i=6548", {}),
                    },
                )
            },
        ),
        "ResultManagementType": (
            "OT",
            "ns=1;i=1007",
            {
                "GetResultById": (
                    "M",
                    "ns=1;i=7026",
                    {
                        "InputArguments": ("V", "ns=1;i=6209", {}),
                        "OutputArguments": ("V", "ns=1;i=6210", {}),
                    },
                ),
                "GetResultComponentsById": (
                    "M",
                    "ns=1;i=7007",
                    {
                        "InputArguments": ("V", "ns=1;i=6024", {}),
                        "OutputArguments": ("V", "ns=1;i=6025", {}),
                    },
                ),
                "GetResultListFiltered": (
                    "M",
                    "ns=1;i=7089",
                    {
                        "InputArguments": ("V", "ns=1;i=6213", {}),
                        "OutputArguments": ("V", "ns=1;i=6214", {}),
                    },
                ),
                "ReleaseResultHandle": (
                    "M",
                    "ns=1;i=7090",
                    {
                        "InputArguments": ("V", "ns=1;i=6217", {}),
                        "OutputArguments": ("V", "ns=1;i=6218", {}),
                    },
                ),
                "ResultTransfer": (
                    "O",
                    "ns=1;i=5251",
                    {
                        "ClientProcessingTimeout": ("V", "ns=1;i=6543", {}),
                        "CloseAndCommit": (
                            "M",
                            "ns=1;i=7071",
                            {
                                "InputArguments": ("V", "ns=1;i=6544", {}),
                                "OutputArguments": ("V", "ns=1;i=6545", {}),
                            },
                        ),
                        "GenerateFileForRead": (
                            "M",
                            "ns=1;i=7067",
                            {
                                "InputArguments": ("V", "ns=1;i=6541", {}),
                                "OutputArguments": ("V", "ns=1;i=6542", {}),
                            },
                        ),
                        "GenerateFileForWrite": (
                            "M",
                            "ns=1;i=7077",
                            {
                                "InputArguments": ("V", "ns=1;i=6546", {}),
                                "OutputArguments": ("V", "ns=1;i=6547", {}),
                            },
                        ),
                    },
                ),
                "Results": ("O", "ns=1;i=5245", {}),
            },
        ),
        "ResultTransferType": (
            "OT",
            "ns=1;i=1039",
            {
                "GenerateFileForRead": (
                    "M",
                    "ns=1;i=7058",
                    {
                        "InputArguments": ("V", "ns=1;i=6169", {}),
                        "OutputArguments": ("V", "ns=1;i=6170", {}),
                    },
                )
            },
        ),
        "SafetyStateManagementType": (
            "OT",
            "ns=1;i=1009",
            {
                "ReportSafetyState": (
                    "M",
                    "ns=1;i=7043",
                    {
                        "InputArguments": ("V", "ns=1;i=6222", {}),
                        "OutputArguments": ("V", "ns=1;i=6223", {}),
                    },
                ),
                "VisionSafetyInformation": ("V", "ns=1;i=6042", {}),
                "VisionSafetyTriggered": ("V", "ns=1;i=6041", {}),
            },
        ),
        "VisionAutomaticModeStateMachineType": (
            "OT",
            "ns=1;i=1021",
            {
                "Abort": (
                    "M",
                    "ns=1;i=7097",
                    {
                        "InputArguments": ("V", "ns=1;i=6285", {}),
                        "OutputArguments": ("V", "ns=1;i=6286", {}),
                    },
                ),
                "ContinuousExecution": (
                    "O",
                    "ns=1;i=5059",
                    {"StateNumber": ("V", "ns=1;i=6262", {})},
                ),
                "ContinuousExecutionStepModel": (
                    "O",
                    "ns=1;i=5021",
                    {
                        "CurrentState": (
                            "V",
                            "ns=1;i=6085",
                            {"Id": ("V", "ns=1;i=6088", {})},
                        ),
                        "Sync": (
                            "M",
                            "ns=1;i=7024",
                            {
                                "InputArguments": ("V", "ns=1;i=6059", {}),
                                "OutputArguments": ("V", "ns=1;i=6083", {}),
                            },
                        ),
                    },
                ),
                "ContinuousExecutionToReadyAbort": (
                    "O",
                    "ns=1;i=5072",
                    {"TransitionNumber": ("V", "ns=1;i=6275", {})},
                ),
                "ContinuousExecutionToReadyAuto": (
                    "O",
                    "ns=1;i=5073",
                    {"TransitionNumber": ("V", "ns=1;i=6276", {})},
                ),
                "ContinuousExecutionToReadyStop": (
                    "O",
                    "ns=1;i=5071",
                    {"TransitionNumber": ("V", "ns=1;i=6274", {})},
                ),
                "Initialized": (
                    "O",
                    "ns=1;i=5056",
                    {"StateNumber": ("V", "ns=1;i=6259", {})},
                ),
                "InitializedStepModel": (
                    "O",
                    "ns=1;i=5043",
                    {
                        "CurrentState": (
                            "V",
                            "ns=1;i=6091",
                            {"Id": ("V", "ns=1;i=6092", {})},
                        ),
                        "Sync": (
                            "M",
                            "ns=1;i=7027",
                            {
                                "InputArguments": ("V", "ns=1;i=6089", {}),
                                "OutputArguments": ("V", "ns=1;i=6090", {}),
                            },
                        ),
                    },
                ),
                "InitializedToReadyAuto": (
                    "O",
                    "ns=1;i=5061",
                    {"TransitionNumber": ("V", "ns=1;i=6264", {})},
                ),
                "InitializedToReadyProduct": (
                    "O",
                    "ns=1;i=5045",
                    {"TransitionNumber": ("V", "ns=1;i=6084", {})},
                ),
                "InitializedToReadyRecipe": (
                    "O",
                    "ns=1;i=5060",
                    {"TransitionNumber": ("V", "ns=1;i=6263", {})},
                ),
                "Ready": (
                    "O",
                    "ns=1;i=5057",
                    {"StateNumber": ("V", "ns=1;i=6260", {})},
                ),
                "ReadyStepModel": (
                    "O",
                    "ns=1;i=5046",
                    {
                        "CurrentState": (
                            "V",
                            "ns=1;i=6135",
                            {"Id": ("V", "ns=1;i=6136", {})},
                        ),
                        "Sync": (
                            "M",
                            "ns=1;i=7028",
                            {
                                "InputArguments": ("V", "ns=1;i=6129", {}),
                                "OutputArguments": ("V", "ns=1;i=6134", {}),
                            },
                        ),
                    },
                ),
                "ReadyToContinuousExecution": (
                    "O",
                    "ns=1;i=5066",
                    {"TransitionNumber": ("V", "ns=1;i=6269", {})},
                ),
                "ReadyToContinuousExecutionAuto": (
                    "O",
                    "ns=1;i=5067",
                    {"TransitionNumber": ("V", "ns=1;i=6270", {})},
                ),
                "ReadyToInitializedAuto": (
                    "O",
                    "ns=1;i=5063",
                    {"TransitionNumber": ("V", "ns=1;i=6266", {})},
                ),
                "ReadyToInitializedProduct": (
                    "O",
                    "ns=1;i=5044",
                    {"TransitionNumber": ("V", "ns=1;i=6243", {})},
                ),
                "ReadyToInitializedRecipe": (
                    "O",
                    "ns=1;i=5062",
                    {"TransitionNumber": ("V", "ns=1;i=6265", {})},
                ),
                "ReadyToSingleExecution": (
                    "O",
                    "ns=1;i=5064",
                    {"TransitionNumber": ("V", "ns=1;i=6267", {})},
                ),
                "ReadyToSingleExecutionAuto": (
                    "O",
                    "ns=1;i=5065",
                    {"TransitionNumber": ("V", "ns=1;i=6268", {})},
                ),
                "SimulationMode": (
                    "M",
                    "ns=1;i=7100",
                    {
                        "InputArguments": ("V", "ns=1;i=6289", {}),
                        "OutputArguments": ("V", "ns=1;i=6290", {}),
                    },
                ),
                "SingleExecution": (
                    "O",
                    "ns=1;i=5058",
                    {"StateNumber": ("V", "ns=1;i=6261", {})},
                ),
                "SingleExecutionStepModel": (
                    "O",
                    "ns=1;i=5052",
                    {
                        "CurrentState": (
                            "V",
                            "ns=1;i=6139",
                            {"Id": ("V", "ns=1;i=6242", {})},
                        ),
                        "Sync": (
                            "M",
                            "ns=1;i=7030",
                            {
                                "InputArguments": ("V", "ns=1;i=6137", {}),
                                "OutputArguments": ("V", "ns=1;i=6138", {}),
                            },
                        ),
                    },
                ),
                "SingleExecutionToReadyAbort": (
                    "O",
                    "ns=1;i=5069",
                    {"TransitionNumber": ("V", "ns=1;i=6272", {})},
                ),
                "SingleExecutionToReadyAuto": (
                    "O",
                    "ns=1;i=5070",
                    {"TransitionNumber": ("V", "ns=1;i=6273", {})},
                ),
                "SingleExecutionToReadyStop": (
                    "O",
                    "ns=1;i=5068",
                    {"TransitionNumber": ("V", "ns=1;i=6271", {})},
                ),
                "StartContinuous": (
                    "M",
                    "ns=1;i=7009",
                    {
                        "InputArguments": ("V", "ns=1;i=6086", {}),
                        "OutputArguments": ("V", "ns=1;i=6087", {}),
                    },
                ),
                "StartSingleJob": (
                    "M",
                    "ns=1;i=7098",
                    {
                        "InputArguments": ("V", "ns=1;i=6281", {}),
                        "OutputArguments": ("V", "ns=1;i=6282", {}),
                    },
                ),
                "Stop": (
                    "M",
                    "ns=1;i=7096",
                    {
                        "InputArguments": ("V", "ns=1;i=6287", {}),
                        "OutputArguments": ("V", "ns=1;i=6288", {}),
                    },
                ),
            },
        ),
        "VisionConditionType": (
            "OT",
            "ns=1;i=1033",
            {
                "BlockReaction": ("V", "ns=1;i=6206", {}),
                "CausePath": ("V", "ns=1;i=6207", {}),
                "ErrorCode": ("V", "ns=1;i=6208", {}),
                "ErrorString": ("V", "ns=1;i=6283", {}),
                "ExternalConfigurationId": ("V", "ns=1;i=6347", {}),
                "ExternalRecipeId": ("V", "ns=1;i=6346", {}),
                "InternalConfigurationId": ("V", "ns=1;i=6192", {}),
                "InternalRecipeId": ("V", "ns=1;i=6321", {}),
                "JobId": ("V", "ns=1;i=6343", {}),
                "MeasId": ("V", "ns=1;i=6344", {}),
                "PartId": ("V", "ns=1;i=6307", {}),
                "ProductId": ("V", "ns=1;i=6323", {}),
                "ResultId": ("V", "ns=1;i=6345", {}),
                "StopReaction": ("V", "ns=1;i=6293", {}),
                "VisionErrorConditionType": ("OT", "ns=1;i=1035", {}),
                "VisionPersistentErrorConditionType": ("OT", "ns=1;i=1036", {}),
                "VisionWarningConditionType": ("OT", "ns=1;i=1034", {}),
            },
        ),
        "VisionStateMachineType": (
            "OT",
            "ns=1;i=1017",
            {
                "AutomaticModeStateMachine": (
                    "O",
                    "ns=1;i=5024",
                    {
                        "Abort": (
                            "M",
                            "ns=1;i=7020",
                            {
                                "InputArguments": ("V", "ns=1;i=6065", {}),
                                "OutputArguments": ("V", "ns=1;i=6066", {}),
                            },
                        ),
                        "ContinuousExecutionStepModel": (
                            "O",
                            "ns=1;i=5025",
                            {
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=6082",
                                    {"Id": ("V", "ns=1;i=6166", {})},
                                ),
                                "Sync": (
                                    "M",
                                    "ns=1;i=7039",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6167", {}),
                                        "OutputArguments": ("V", "ns=1;i=6174", {}),
                                    },
                                ),
                            },
                        ),
                        "CurrentState": (
                            "V",
                            "ns=1;i=6080",
                            {"Id": ("V", "ns=1;i=6081", {})},
                        ),
                        "InitializedStepModel": (
                            "O",
                            "ns=1;i=5055",
                            {
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=6175",
                                    {"Id": ("V", "ns=1;i=6178", {})},
                                ),
                                "Sync": (
                                    "M",
                                    "ns=1;i=7040",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6179", {}),
                                        "OutputArguments": ("V", "ns=1;i=6182", {}),
                                    },
                                ),
                            },
                        ),
                        "ReadyStepModel": (
                            "O",
                            "ns=1;i=5074",
                            {
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=6183",
                                    {"Id": ("V", "ns=1;i=6211", {})},
                                ),
                                "Sync": (
                                    "M",
                                    "ns=1;i=7042",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6212", {}),
                                        "OutputArguments": ("V", "ns=1;i=6215", {}),
                                    },
                                ),
                            },
                        ),
                        "SimulationMode": (
                            "M",
                            "ns=1;i=7044",
                            {
                                "InputArguments": ("V", "ns=1;i=6326", {}),
                                "OutputArguments": ("V", "ns=1;i=6400", {}),
                            },
                        ),
                        "SingleExecutionStepModel": (
                            "O",
                            "ns=1;i=5092",
                            {
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=6401",
                                    {"Id": ("V", "ns=1;i=6402", {})},
                                ),
                                "Sync": (
                                    "M",
                                    "ns=1;i=7091",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6403", {}),
                                        "OutputArguments": ("V", "ns=1;i=6404", {}),
                                    },
                                ),
                            },
                        ),
                        "StartContinuous": (
                            "M",
                            "ns=1;i=7021",
                            {
                                "InputArguments": ("V", "ns=1;i=6067", {}),
                                "OutputArguments": ("V", "ns=1;i=6068", {}),
                            },
                        ),
                        "StartSingleJob": (
                            "M",
                            "ns=1;i=7022",
                            {
                                "InputArguments": ("V", "ns=1;i=6069", {}),
                                "OutputArguments": ("V", "ns=1;i=6070", {}),
                            },
                        ),
                        "Stop": (
                            "M",
                            "ns=1;i=7023",
                            {
                                "InputArguments": ("V", "ns=1;i=6078", {}),
                                "OutputArguments": ("V", "ns=1;i=6079", {}),
                            },
                        ),
                    },
                ),
                "ConfirmAll": (
                    "M",
                    "ns=1;i=7066",
                    {"InputArguments": ("V", "ns=1;i=6241", {})},
                ),
                "Error": (
                    "O",
                    "ns=1;i=5030",
                    {"StateNumber": ("V", "ns=1;i=6228", {})},
                ),
                "ErrorStepModel": (
                    "O",
                    "ns=1;i=5054",
                    {
                        "CurrentState": (
                            "V",
                            "ns=1;i=6358",
                            {"Id": ("V", "ns=1;i=6390", {})},
                        ),
                        "Sync": (
                            "M",
                            "ns=1;i=7019",
                            {
                                "InputArguments": ("V", "ns=1;i=6252", {}),
                                "OutputArguments": ("V", "ns=1;i=6349", {}),
                            },
                        ),
                    },
                ),
                "ErrorToHalted": (
                    "O",
                    "ns=1;i=5041",
                    {"TransitionNumber": ("V", "ns=1;i=6239", {})},
                ),
                "ErrorToHaltedAuto": (
                    "O",
                    "ns=1;i=5042",
                    {"TransitionNumber": ("V", "ns=1;i=6240", {})},
                ),
                "ErrorToOperationalAuto": (
                    "O",
                    "ns=1;i=5255",
                    {"TransitionNumber": ("V", "ns=1;i=6341", {})},
                ),
                "ErrorToPreoperational": (
                    "O",
                    "ns=1;i=5039",
                    {"TransitionNumber": ("V", "ns=1;i=6237", {})},
                ),
                "ErrorToPreoperationalAuto": (
                    "O",
                    "ns=1;i=5040",
                    {"TransitionNumber": ("V", "ns=1;i=6238", {})},
                ),
                "Halt": (
                    "M",
                    "ns=1;i=7094",
                    {
                        "InputArguments": ("V", "ns=1;i=6254", {}),
                        "OutputArguments": ("V", "ns=1;i=6255", {}),
                    },
                ),
                "Halted": (
                    "O",
                    "ns=1;i=5029",
                    {"StateNumber": ("V", "ns=1;i=6227", {})},
                ),
                "HaltedStepModel": (
                    "O",
                    "ns=1;i=5011",
                    {
                        "CurrentState": (
                            "V",
                            "ns=1;i=6058",
                            {"Id": ("V", "ns=1;i=6060", {})},
                        ),
                        "Sync": (
                            "M",
                            "ns=1;i=7010",
                            {
                                "InputArguments": ("V", "ns=1;i=6056", {}),
                                "OutputArguments": ("V", "ns=1;i=6057", {}),
                            },
                        ),
                    },
                ),
                "HaltedToPreoperational": (
                    "O",
                    "ns=1;i=5037",
                    {"TransitionNumber": ("V", "ns=1;i=6235", {})},
                ),
                "HaltedToPreoperationalAuto": (
                    "O",
                    "ns=1;i=5038",
                    {"TransitionNumber": ("V", "ns=1;i=6236", {})},
                ),
                "Operational": (
                    "O",
                    "ns=1;i=5031",
                    {"StateNumber": ("V", "ns=1;i=6229", {})},
                ),
                "OperationalToErrorAuto": (
                    "O",
                    "ns=1;i=5051",
                    {"TransitionNumber": ("V", "ns=1;i=6249", {})},
                ),
                "OperationalToHalted": (
                    "O",
                    "ns=1;i=5049",
                    {"TransitionNumber": ("V", "ns=1;i=6247", {})},
                ),
                "OperationalToHaltedAuto": (
                    "O",
                    "ns=1;i=5050",
                    {"TransitionNumber": ("V", "ns=1;i=6248", {})},
                ),
                "OperationalToPreoperational": (
                    "O",
                    "ns=1;i=5047",
                    {"TransitionNumber": ("V", "ns=1;i=6245", {})},
                ),
                "OperationalToPreoperationalAuto": (
                    "O",
                    "ns=1;i=5048",
                    {"TransitionNumber": ("V", "ns=1;i=6246", {})},
                ),
                "Preoperational": (
                    "O",
                    "ns=1;i=5028",
                    {"StateNumber": ("V", "ns=1;i=6226", {})},
                ),
                "PreoperationalStepModel": (
                    "O",
                    "ns=1;i=5012",
                    {
                        "CurrentState": (
                            "V",
                            "ns=1;i=6063",
                            {"Id": ("V", "ns=1;i=6064", {})},
                        ),
                        "Sync": (
                            "M",
                            "ns=1;i=7011",
                            {
                                "InputArguments": ("V", "ns=1;i=6061", {}),
                                "OutputArguments": ("V", "ns=1;i=6062", {}),
                            },
                        ),
                    },
                ),
                "PreoperationalToErrorAuto": (
                    "O",
                    "ns=1;i=5034",
                    {"TransitionNumber": ("V", "ns=1;i=6232", {})},
                ),
                "PreoperationalToHalted": (
                    "O",
                    "ns=1;i=5032",
                    {"TransitionNumber": ("V", "ns=1;i=6230", {})},
                ),
                "PreoperationalToHaltedAuto": (
                    "O",
                    "ns=1;i=5033",
                    {"TransitionNumber": ("V", "ns=1;i=6231", {})},
                ),
                "PreoperationalToInitialized": (
                    "O",
                    "ns=1;i=5035",
                    {"TransitionNumber": ("V", "ns=1;i=6233", {})},
                ),
                "PreoperationalToInitializedAuto": (
                    "O",
                    "ns=1;i=5036",
                    {"TransitionNumber": ("V", "ns=1;i=6234", {})},
                ),
                "PreoperationalToOperational": (
                    "O",
                    "ns=1;i=5253",
                    {"TransitionNumber": ("V", "ns=1;i=6171", {})},
                ),
                "PreoperationalToOperationalAuto": (
                    "O",
                    "ns=1;i=5254",
                    {"TransitionNumber": ("V", "ns=1;i=6221", {})},
                ),
                "Reset": (
                    "M",
                    "ns=1;i=7093",
                    {
                        "InputArguments": ("V", "ns=1;i=6256", {}),
                        "OutputArguments": ("V", "ns=1;i=6257", {}),
                    },
                ),
                "SelectModeAutomatic": (
                    "M",
                    "ns=1;i=7095",
                    {"OutputArguments": ("V", "ns=1;i=6258", {})},
                ),
            },
        ),
        "VisionStepModelStateMachineType": (
            "OT",
            "ns=1;i=1026",
            {
                "Entry": (
                    "O",
                    "ns=1;i=5078",
                    {"StateNumber": ("V", "ns=1;i=6309", {})},
                ),
                "EntryToExitAuto": (
                    "O",
                    "ns=1;i=5082",
                    {"TransitionNumber": ("V", "ns=1;i=6313", {})},
                ),
                "EntryToWaitAuto": (
                    "O",
                    "ns=1;i=5083",
                    {"TransitionNumber": ("V", "ns=1;i=6314", {})},
                ),
                "Exit": ("O", "ns=1;i=5079", {"StateNumber": ("V", "ns=1;i=6310", {})}),
                "Step": ("O", "ns=1;i=5081", {"StateNumber": ("V", "ns=1;i=6312", {})}),
                "StepToExitAuto": (
                    "O",
                    "ns=1;i=5087",
                    {"TransitionNumber": ("V", "ns=1;i=6318", {})},
                ),
                "StepToWaitAuto": (
                    "O",
                    "ns=1;i=5086",
                    {"TransitionNumber": ("V", "ns=1;i=6317", {})},
                ),
                "Sync": (
                    "M",
                    "ns=1;i=7101",
                    {
                        "InputArguments": ("V", "ns=1;i=6319", {}),
                        "OutputArguments": ("V", "ns=1;i=6320", {}),
                    },
                ),
                "Wait": ("O", "ns=1;i=5080", {"StateNumber": ("V", "ns=1;i=6311", {})}),
                "WaitToStep": (
                    "O",
                    "ns=1;i=5084",
                    {"TransitionNumber": ("V", "ns=1;i=6315", {})},
                ),
                "WaitToStepAuto": (
                    "O",
                    "ns=1;i=5085",
                    {"TransitionNumber": ("V", "ns=1;i=6316", {})},
                ),
            },
        ),
        "VisionSystemType": (
            "OT",
            "ns=1;i=1003",
            {
                "ConfigurationManagement": (
                    "O",
                    "ns=1;i=5004",
                    {
                        "ActivateConfiguration": (
                            "M",
                            "ns=1;i=7008",
                            {
                                "InputArguments": ("V", "ns=1;i=6026", {}),
                                "OutputArguments": ("V", "ns=1;i=6027", {}),
                            },
                        ),
                        "ActiveConfiguration": ("V", "ns=1;i=6043", {}),
                        "AddConfiguration": (
                            "M",
                            "ns=1;i=7054",
                            {
                                "InputArguments": ("V", "ns=1;i=6342", {}),
                                "OutputArguments": ("V", "ns=1;i=6348", {}),
                            },
                        ),
                        "ConfigurationTransfer": (
                            "O",
                            "ns=1;i=5093",
                            {
                                "ClientProcessingTimeout": ("V", "ns=1;i=6350", {}),
                                "CloseAndCommit": (
                                    "M",
                                    "ns=1;i=7068",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6351", {}),
                                        "OutputArguments": ("V", "ns=1;i=6359", {}),
                                    },
                                ),
                                "GenerateFileForRead": (
                                    "M",
                                    "ns=1;i=7069",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6360", {}),
                                        "OutputArguments": ("V", "ns=1;i=6361", {}),
                                    },
                                ),
                                "GenerateFileForWrite": (
                                    "M",
                                    "ns=1;i=7070",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6362", {}),
                                        "OutputArguments": ("V", "ns=1;i=6363", {}),
                                    },
                                ),
                            },
                        ),
                        "Configurations": ("O", "ns=1;i=5094", {}),
                        "GetConfigurationById": (
                            "M",
                            "ns=1;i=7016",
                            {
                                "InputArguments": ("V", "ns=1;i=6044", {}),
                                "OutputArguments": ("V", "ns=1;i=6098", {}),
                            },
                        ),
                        "GetConfigurationList": (
                            "M",
                            "ns=1;i=7017",
                            {
                                "InputArguments": ("V", "ns=1;i=6099", {}),
                                "OutputArguments": ("V", "ns=1;i=6102", {}),
                            },
                        ),
                        "ReleaseConfigurationHandle": (
                            "M",
                            "ns=1;i=7072",
                            {
                                "InputArguments": ("V", "ns=1;i=6364", {}),
                                "OutputArguments": ("V", "ns=1;i=6365", {}),
                            },
                        ),
                        "RemoveConfiguration": (
                            "M",
                            "ns=1;i=7073",
                            {
                                "InputArguments": ("V", "ns=1;i=6366", {}),
                                "OutputArguments": ("V", "ns=1;i=6368", {}),
                            },
                        ),
                    },
                ),
                "DiagnosticLevel": ("V", "ns=1;i=6048", {}),
                "RecipeManagement": (
                    "O",
                    "ns=1;i=5015",
                    {
                        "AddRecipe": (
                            "M",
                            "ns=1;i=7074",
                            {
                                "InputArguments": ("V", "ns=1;i=6369", {}),
                                "OutputArguments": ("V", "ns=1;i=6370", {}),
                            },
                        ),
                        "GetRecipeListFiltered": (
                            "M",
                            "ns=1;i=7018",
                            {
                                "InputArguments": ("V", "ns=1;i=6103", {}),
                                "OutputArguments": ("V", "ns=1;i=6106", {}),
                            },
                        ),
                        "PrepareProduct": (
                            "M",
                            "ns=1;i=7075",
                            {
                                "InputArguments": ("V", "ns=1;i=6371", {}),
                                "OutputArguments": ("V", "ns=1;i=6372", {}),
                            },
                        ),
                        "PrepareRecipe": (
                            "M",
                            "ns=1;i=7031",
                            {
                                "InputArguments": ("V", "ns=1;i=6107", {}),
                                "OutputArguments": ("V", "ns=1;i=6110", {}),
                            },
                        ),
                        "Products": (
                            "O",
                            "ns=1;i=5095",
                            {"<Product>": ("V", "ns=1;i=6373", {})},
                        ),
                        "RecipeTransfer": (
                            "O",
                            "ns=1;i=5096",
                            {
                                "ClientProcessingTimeout": ("V", "ns=1;i=6374", {}),
                                "CloseAndCommit": (
                                    "M",
                                    "ns=1;i=7078",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6375", {}),
                                        "OutputArguments": ("V", "ns=1;i=6376", {}),
                                    },
                                ),
                                "GenerateFileForRead": (
                                    "M",
                                    "ns=1;i=7079",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6377", {}),
                                        "OutputArguments": ("V", "ns=1;i=6378", {}),
                                    },
                                ),
                                "GenerateFileForWrite": (
                                    "M",
                                    "ns=1;i=7080",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6380", {}),
                                        "OutputArguments": ("V", "ns=1;i=6381", {}),
                                    },
                                ),
                            },
                        ),
                        "Recipes": ("O", "ns=1;i=5097", {}),
                        "ReleaseRecipeHandle": (
                            "M",
                            "ns=1;i=7081",
                            {
                                "InputArguments": ("V", "ns=1;i=6382", {}),
                                "OutputArguments": ("V", "ns=1;i=6383", {}),
                            },
                        ),
                        "RemoveRecipe": (
                            "M",
                            "ns=1;i=7082",
                            {
                                "InputArguments": ("V", "ns=1;i=6384", {}),
                                "OutputArguments": ("V", "ns=1;i=6385", {}),
                            },
                        ),
                        "UnlinkProduct": (
                            "M",
                            "ns=1;i=7083",
                            {
                                "InputArguments": ("V", "ns=1;i=6386", {}),
                                "OutputArguments": ("V", "ns=1;i=6387", {}),
                            },
                        ),
                        "UnprepareProduct": (
                            "M",
                            "ns=1;i=7084",
                            {
                                "InputArguments": ("V", "ns=1;i=6388", {}),
                                "OutputArguments": ("V", "ns=1;i=6389", {}),
                            },
                        ),
                        "UnprepareRecipe": (
                            "M",
                            "ns=1;i=7032",
                            {
                                "InputArguments": ("V", "ns=1;i=6111", {}),
                                "OutputArguments": ("V", "ns=1;i=6114", {}),
                            },
                        ),
                    },
                ),
                "ResultManagement": (
                    "O",
                    "ns=1;i=5020",
                    {
                        "GetResultById": (
                            "M",
                            "ns=1;i=7033",
                            {
                                "InputArguments": ("V", "ns=1;i=6115", {}),
                                "OutputArguments": ("V", "ns=1;i=6118", {}),
                            },
                        ),
                        "GetResultComponentsById": (
                            "M",
                            "ns=1;i=7034",
                            {
                                "InputArguments": ("V", "ns=1;i=6119", {}),
                                "OutputArguments": ("V", "ns=1;i=6123", {}),
                            },
                        ),
                        "GetResultListFiltered": (
                            "M",
                            "ns=1;i=7035",
                            {
                                "InputArguments": ("V", "ns=1;i=6124", {}),
                                "OutputArguments": ("V", "ns=1;i=6133", {}),
                            },
                        ),
                        "ReleaseResultHandle": (
                            "M",
                            "ns=1;i=7085",
                            {
                                "InputArguments": ("V", "ns=1;i=6391", {}),
                                "OutputArguments": ("V", "ns=1;i=6392", {}),
                            },
                        ),
                        "ResultTransfer": (
                            "O",
                            "ns=1;i=5098",
                            {
                                "ClientProcessingTimeout": ("V", "ns=1;i=6393", {}),
                                "CloseAndCommit": (
                                    "M",
                                    "ns=1;i=7086",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6394", {}),
                                        "OutputArguments": ("V", "ns=1;i=6395", {}),
                                    },
                                ),
                                "GenerateFileForRead": (
                                    "M",
                                    "ns=1;i=7087",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6396", {}),
                                        "OutputArguments": ("V", "ns=1;i=6397", {}),
                                    },
                                ),
                                "GenerateFileForWrite": (
                                    "M",
                                    "ns=1;i=7088",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6398", {}),
                                        "OutputArguments": ("V", "ns=1;i=6399", {}),
                                    },
                                ),
                            },
                        ),
                        "Results": ("O", "ns=1;i=5099", {}),
                    },
                ),
                "SafetyStateManagement": (
                    "O",
                    "ns=1;i=5023",
                    {
                        "ReportSafetyState": (
                            "M",
                            "ns=1;i=7036",
                            {
                                "InputArguments": ("V", "ns=1;i=6146", {}),
                                "OutputArguments": ("V", "ns=1;i=6147", {}),
                            },
                        ),
                        "VisionSafetyInformation": ("V", "ns=1;i=6150", {}),
                        "VisionSafetyTriggered": ("V", "ns=1;i=6151", {}),
                    },
                ),
                "SystemState": ("V", "ns=1;i=6049", {}),
                "VisionStateMachine": (
                    "O",
                    "ns=1;i=5053",
                    {
                        "AutomaticModeStateMachine": (
                            "O",
                            "ns=1;i=5100",
                            {
                                "Abort": (
                                    "M",
                                    "ns=1;i=7092",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6405", {}),
                                        "OutputArguments": ("V", "ns=1;i=6406", {}),
                                    },
                                ),
                                "ContinuousExecutionStepModel": (
                                    "O",
                                    "ns=1;i=5102",
                                    {
                                        "CurrentState": (
                                            "V",
                                            "ns=1;i=6416",
                                            {"Id": ("V", "ns=1;i=6417", {})},
                                        ),
                                        "Sync": (
                                            "M",
                                            "ns=1;i=7104",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=6418",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=6419",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=6407",
                                    {"Id": ("V", "ns=1;i=6408", {})},
                                ),
                                "InitializedStepModel": (
                                    "O",
                                    "ns=1;i=5103",
                                    {
                                        "CurrentState": (
                                            "V",
                                            "ns=1;i=6420",
                                            {"Id": ("V", "ns=1;i=6421", {})},
                                        ),
                                        "Sync": (
                                            "M",
                                            "ns=1;i=7105",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=6422",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=6423",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "ReadyStepModel": (
                                    "O",
                                    "ns=1;i=5104",
                                    {
                                        "CurrentState": (
                                            "V",
                                            "ns=1;i=6424",
                                            {"Id": ("V", "ns=1;i=6425", {})},
                                        ),
                                        "Sync": (
                                            "M",
                                            "ns=1;i=7106",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=6426",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=6427",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "SimulationMode": (
                                    "M",
                                    "ns=1;i=7107",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6428", {}),
                                        "OutputArguments": ("V", "ns=1;i=6429", {}),
                                    },
                                ),
                                "SingleExecutionStepModel": (
                                    "O",
                                    "ns=1;i=5105",
                                    {
                                        "CurrentState": (
                                            "V",
                                            "ns=1;i=6430",
                                            {"Id": ("V", "ns=1;i=6431", {})},
                                        ),
                                        "Sync": (
                                            "M",
                                            "ns=1;i=7108",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=6432",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=6433",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "StartContinuous": (
                                    "M",
                                    "ns=1;i=7099",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6409", {}),
                                        "OutputArguments": ("V", "ns=1;i=6410", {}),
                                    },
                                ),
                                "StartSingleJob": (
                                    "M",
                                    "ns=1;i=7102",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6411", {}),
                                        "OutputArguments": ("V", "ns=1;i=6412", {}),
                                    },
                                ),
                                "Stop": (
                                    "M",
                                    "ns=1;i=7103",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6413", {}),
                                        "OutputArguments": ("V", "ns=1;i=6414", {}),
                                    },
                                ),
                            },
                        ),
                        "ConfirmAll": (
                            "M",
                            "ns=1;i=7049",
                            {"InputArguments": ("V", "ns=1;i=6216", {})},
                        ),
                        "CurrentState": (
                            "V",
                            "ns=1;i=6162",
                            {"Id": ("V", "ns=1;i=6163", {})},
                        ),
                        "Error": (
                            "O",
                            "ns=1;i=5107",
                            {"StateNumber": ("V", "ns=1;i=6435", {})},
                        ),
                        "ErrorStepModel": (
                            "O",
                            "ns=1;i=5075",
                            {
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=6219",
                                    {"Id": ("V", "ns=1;i=6220", {})},
                                ),
                                "Sync": (
                                    "M",
                                    "ns=1;i=7050",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6224", {}),
                                        "OutputArguments": ("V", "ns=1;i=6225", {}),
                                    },
                                ),
                            },
                        ),
                        "Halt": (
                            "M",
                            "ns=1;i=7037",
                            {
                                "InputArguments": ("V", "ns=1;i=6154", {}),
                                "OutputArguments": ("V", "ns=1;i=6155", {}),
                            },
                        ),
                        "Halted": (
                            "O",
                            "ns=1;i=5106",
                            {"StateNumber": ("V", "ns=1;i=6434", {})},
                        ),
                        "HaltedStepModel": (
                            "O",
                            "ns=1;i=5076",
                            {
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=6244",
                                    {"Id": ("V", "ns=1;i=6250", {})},
                                ),
                                "Sync": (
                                    "M",
                                    "ns=1;i=7051",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6251", {}),
                                        "OutputArguments": ("V", "ns=1;i=6253", {}),
                                    },
                                ),
                            },
                        ),
                        "Operational": (
                            "O",
                            "ns=1;i=5108",
                            {"StateNumber": ("V", "ns=1;i=6436", {})},
                        ),
                        "Preoperational": (
                            "O",
                            "ns=1;i=5101",
                            {"StateNumber": ("V", "ns=1;i=6415", {})},
                        ),
                        "PreoperationalStepModel": (
                            "O",
                            "ns=1;i=5077",
                            {
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=6277",
                                    {"Id": ("V", "ns=1;i=6278", {})},
                                ),
                                "Sync": (
                                    "M",
                                    "ns=1;i=7052",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6279", {}),
                                        "OutputArguments": ("V", "ns=1;i=6280", {}),
                                    },
                                ),
                            },
                        ),
                        "Reset": (
                            "M",
                            "ns=1;i=7038",
                            {
                                "InputArguments": ("V", "ns=1;i=6158", {}),
                                "OutputArguments": ("V", "ns=1;i=6159", {}),
                            },
                        ),
                        "SelectModeAutomatic": (
                            "M",
                            "ns=1;i=7053",
                            {"OutputArguments": ("V", "ns=1;i=6325", {})},
                        ),
                    },
                ),
            },
        ),
    },
    "reftypes": {
        "FromTransition": ("RT", "ns=1;i=4002", {}),
        "ToTransition": ("RT", "ns=1;i=4003", {}),
    },
    "vartypes": {
        "ResultType": (
            "VT",
            "ns=1;i=2002",
            {
                "CreationTime": ("V", "ns=1;i=6331", {}),
                "ExternalConfigurationId": ("V", "ns=1;i=6328", {}),
                "ExternalRecipeId": ("V", "ns=1;i=6095", {}),
                "HasTransferableDataOnFile": ("V", "ns=1;i=6047", {}),
                "InternalConfigurationId": ("V", "ns=1;i=6329", {}),
                "InternalRecipeId": ("V", "ns=1;i=6284", {}),
                "IsPartial": ("V", "ns=1;i=6052", {}),
                "IsSimulated": ("V", "ns=1;i=6053", {}),
                "JobId": ("V", "ns=1;i=6330", {}),
                "MeasId": ("V", "ns=1;i=6055", {}),
                "PartId": ("V", "ns=1;i=6094", {}),
                "ProcessingTimes": ("V", "ns=1;i=6332", {}),
                "ProductId": ("V", "ns=1;i=6327", {}),
                "ResultContent": ("V", "ns=1;i=6333", {}),
                "ResultId": ("V", "ns=1;i=6046", {}),
                "ResultState": ("V", "ns=1;i=6054", {}),
            },
        )
    },
}
