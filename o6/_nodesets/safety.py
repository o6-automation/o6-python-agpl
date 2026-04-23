# AUTO-GENERATED — DO NOT EDIT
# source-sha256: dcc9d20b0c928f4f4a5fe60daa98ee14d820803e48a936216d8b445469f50c43
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/Safety"
_VERSION: str = "1.05.04"
_REQUIRED: list = [{"uri": "http://opcfoundation.org/UA/", "version": "1.05.01"}]
_STRUCTURES: list = [
    (
        "ns=1;i=3002",
        "NonSafetyDataPlaceholderDataType",
        "ns=1;i=5003",
        {
            "structure_type": 0,
            "fields": [{"name": "Dummy", "data_type": "i=1", "value_rank": -1}],
        },
    ),
    (
        "ns=1;i=3003",
        "RequestSPDUDataType",
        "ns=1;i=5010",
        {
            "structure_type": 0,
            "fields": [
                {"name": "InSafetyConsumerID", "data_type": "i=7", "value_rank": -1},
                {"name": "InMonitoringNumber", "data_type": "i=7", "value_rank": -1},
                {"name": "InFlags", "data_type": "ns=1;i=3005", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3004",
        "ResponseSPDUDataType",
        "i=0",
        {
            "structure_type": 0,
            "fields": [
                {"name": "OutFlags", "data_type": "ns=1;i=3006", "value_rank": -1},
                {"name": "OutSPDU_ID_1", "data_type": "i=7", "value_rank": -1},
                {"name": "OutSPDU_ID_2", "data_type": "i=7", "value_rank": -1},
                {"name": "OutSPDU_ID_3", "data_type": "i=7", "value_rank": -1},
                {"name": "OutSafetyConsumerID", "data_type": "i=7", "value_rank": -1},
                {"name": "OutMonitoringNumber", "data_type": "i=7", "value_rank": -1},
                {"name": "OutCRC", "data_type": "i=7", "value_rank": -1},
            ],
        },
    ),
]
_ENUMS: list = [
    (
        "ns=1;i=3005",
        "InFlagsType",
        {
            "fields": [
                {
                    "name": "CommunicationError",
                    "value": 0,
                    "display_name": "CommunicationError",
                },
                {
                    "name": "OperatorAckRequested",
                    "value": 1,
                    "display_name": "OperatorAckRequested",
                },
                {"name": "FSV_Activated", "value": 2, "display_name": "FSV_Activated"},
            ]
        },
    ),
    (
        "ns=1;i=3006",
        "OutFlagsType",
        {
            "fields": [
                {
                    "name": "OperatorAckProvider",
                    "value": 0,
                    "display_name": "OperatorAckProvider",
                },
                {"name": "ActivateFSV", "value": 1, "display_name": "ActivateFSV"},
                {
                    "name": "TestModeActivated",
                    "value": 2,
                    "display_name": "TestModeActivated",
                },
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = (
    [
        ("ns=1;i=3002", "ns=1;i=5003", ["i=1"]),
        ("ns=1;i=3003", "ns=1;i=5010", ["i=7", "i=7", "ns=1;i=3005"]),
        (
            "ns=1;i=3004",
            "i=0",
            ["ns=1;i=3006", "i=7", "i=7", "i=7", "i=7", "i=7", "i=7"],
        ),
    ],
    ["ns=1;i=3005", "ns=1;i=3006"],
)
_NODES: dict = {
    "datatypes": {
        "InFlagsType": (
            "D",
            "ns=1;i=3005",
            {"OptionSetValues": ("V", "ns=1;i=6059", {})},
        ),
        "NonSafetyDataPlaceholderDataType": ("D", "ns=1;i=3002", {}),
        "OutFlagsType": (
            "D",
            "ns=1;i=3006",
            {"OptionSetValues": ("V", "ns=1;i=6060", {})},
        ),
        "RequestSPDUDataType": ("D", "ns=1;i=3003", {}),
        "ResponseSPDUDataType": ("D", "ns=1;i=3004", {}),
    },
    "objects": {
        "Default Binary": ("O", "ns=1;i=5010", {}),
        "Default JSON": ("O", "ns=1;i=5012", {}),
        "Default XML": ("O", "ns=1;i=5011", {}),
        "SafetyACSet": ("O", "ns=1;i=5002", {}),
        "http://opcfoundation.org/UA/Safety": (
            "O",
            "ns=1;i=5006",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=6022", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=6023", {}),
                "NamespaceUri": ("V", "ns=1;i=6024", {}),
                "NamespaceVersion": ("V", "ns=1;i=6025", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=6026", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=6027", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=6028", {}),
            },
        ),
    },
    "objtypes": {
        "SafetyConsumerParametersType": (
            "OT",
            "ns=1;i=1006",
            {
                "SafetyBaseIDActive": ("V", "ns=1;i=6063", {}),
                "SafetyBaseIDConfigured": ("V", "ns=1;i=6042", {}),
                "SafetyClientImplemented": ("V", "ns=1;i=6068", {}),
                "SafetyConsumerIDActive": ("V", "ns=1;i=6067", {}),
                "SafetyConsumerIDConfigured": ("V", "ns=1;i=6043", {}),
                "SafetyConsumerTimeout": ("V", "ns=1;i=6048", {}),
                "SafetyErrorIntervalLimit": ("V", "ns=1;i=6050", {}),
                "SafetyOperatorAckNecessary": ("V", "ns=1;i=6049", {}),
                "SafetyProviderIDActive": ("V", "ns=1;i=6066", {}),
                "SafetyProviderIDConfigured": ("V", "ns=1;i=6041", {}),
                "SafetyProviderLevel": ("V", "ns=1;i=6044", {}),
                "SafetyPubSubImplemented": ("V", "ns=1;i=6069", {}),
                "SafetyStructureIdentifier": ("V", "ns=1;i=6047", {}),
                "SafetyStructureSignature": ("V", "ns=1;i=6045", {}),
                "SafetyStructureSignatureVersion": ("V", "ns=1;i=6046", {}),
            },
        ),
        "SafetyObjectsType": (
            "OT",
            "ns=1;i=1004",
            {
                "SafetyConsumerType": (
                    "OT",
                    "ns=1;i=1005",
                    {
                        "Parameters": (
                            "O",
                            "ns=1;i=5009",
                            {
                                "SafetyBaseIDActive": ("V", "ns=1;i=6072", {}),
                                "SafetyBaseIDConfigured": ("V", "ns=1;i=6073", {}),
                                "SafetyClientImplemented": ("V", "ns=1;i=6074", {}),
                                "SafetyConsumerIDActive": ("V", "ns=1;i=6075", {}),
                                "SafetyConsumerIDConfigured": ("V", "ns=1;i=6076", {}),
                                "SafetyConsumerTimeout": ("V", "ns=1;i=6077", {}),
                                "SafetyErrorIntervalLimit": ("V", "ns=1;i=6078", {}),
                                "SafetyOperatorAckNecessary": ("V", "ns=1;i=6079", {}),
                                "SafetyProviderIDActive": ("V", "ns=1;i=6080", {}),
                                "SafetyProviderIDConfigured": ("V", "ns=1;i=6081", {}),
                                "SafetyProviderLevel": ("V", "ns=1;i=6082", {}),
                                "SafetyPubSubImplemented": ("V", "ns=1;i=6083", {}),
                                "SafetyStructureIdentifier": ("V", "ns=1;i=6084", {}),
                                "SafetyStructureSignature": ("V", "ns=1;i=6085", {}),
                                "SafetyStructureSignatureVersion": (
                                    "V",
                                    "ns=1;i=6086",
                                    {},
                                ),
                            },
                        ),
                        "SafetyPDUs": ("O", "ns=1;i=5007", {}),
                    },
                ),
                "SafetyProviderType": (
                    "OT",
                    "ns=1;i=1003",
                    {
                        "Parameters": (
                            "O",
                            "ns=1;i=5001",
                            {
                                "SafetyBaseIDActive": ("V", "ns=1;i=6019", {}),
                                "SafetyBaseIDConfigured": ("V", "ns=1;i=6020", {}),
                                "SafetyProviderDelay": ("V", "ns=1;i=6021", {}),
                                "SafetyProviderIDActive": ("V", "ns=1;i=6031", {}),
                                "SafetyProviderIDConfigured": ("V", "ns=1;i=6032", {}),
                                "SafetyProviderLevel": ("V", "ns=1;i=6033", {}),
                                "SafetyPubSubImplemented": ("V", "ns=1;i=6034", {}),
                                "SafetyServerImplemented": ("V", "ns=1;i=6040", {}),
                                "SafetyStructureIdentifier": ("V", "ns=1;i=6061", {}),
                                "SafetyStructureSignature": ("V", "ns=1;i=6070", {}),
                                "SafetyStructureSignatureVersion": (
                                    "V",
                                    "ns=1;i=6071",
                                    {},
                                ),
                            },
                        ),
                        "ReadSafetyData": (
                            "M",
                            "ns=1;i=7001",
                            {
                                "InputArguments": ("V", "ns=1;i=6007", {}),
                                "OutputArguments": ("V", "ns=1;i=6008", {}),
                            },
                        ),
                        "ReadSafetyDiagnostics": (
                            "M",
                            "ns=1;i=7002",
                            {"OutputArguments": ("V", "ns=1;i=6009", {})},
                        ),
                        "SafetyPDUs": ("O", "ns=1;i=5000", {}),
                    },
                ),
            },
        ),
        "SafetyPDUsType": (
            "OT",
            "ns=1;i=1007",
            {
                "<RequestSPDU>": ("V", "ns=1;i=6029", {}),
                "<ResponseSPDU>": ("V", "ns=1;i=6030", {}),
            },
        ),
        "SafetyProviderParametersType": (
            "OT",
            "ns=1;i=1002",
            {
                "SafetyBaseIDActive": ("V", "ns=1;i=6000", {}),
                "SafetyBaseIDConfigured": ("V", "ns=1;i=6005", {}),
                "SafetyProviderDelay": ("V", "ns=1;i=6002", {}),
                "SafetyProviderIDActive": ("V", "ns=1;i=6062", {}),
                "SafetyProviderIDConfigured": ("V", "ns=1;i=6006", {}),
                "SafetyProviderLevel": ("V", "ns=1;i=6001", {}),
                "SafetyPubSubImplemented": ("V", "ns=1;i=6065", {}),
                "SafetyServerImplemented": ("V", "ns=1;i=6064", {}),
                "SafetyStructureIdentifier": ("V", "ns=1;i=6004", {}),
                "SafetyStructureSignature": ("V", "ns=1;i=6039", {}),
                "SafetyStructureSignatureVersion": ("V", "ns=1;i=6003", {}),
            },
        ),
    },
}
