# AUTO-GENERATED — DO NOT EDIT
# source-sha256: d2ea805b6f799589156c85ffc7799b5d296a68f4d7cace3a5ffb40a0fd1f065c
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/AMB/"
_VERSION: str = "1.01.1"
_REQUIRED: list = [{"uri": "http://opcfoundation.org/UA/", "version": "1.05.02"}]
_STRUCTURES: list = [
    (
        "ns=1;i=3003",
        "NameNodeIdDataType",
        "ns=1;i=5012",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Name", "data_type": "i=21", "value_rank": -1},
                {"name": "NodeId", "data_type": "i=17", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3002",
        "RootCauseDataType",
        "ns=1;i=5001",
        {
            "structure_type": 0,
            "fields": [
                {"name": "RootCauseId", "data_type": "i=17", "value_rank": -1},
                {"name": "RootCause", "data_type": "i=21", "value_rank": -1},
            ],
        },
    ),
]
_ENUMS: list = [
    (
        "ns=1;i=3004",
        "MaintenanceMethodEnum",
        {
            "fields": [
                {"name": "Local", "value": 0, "display_name": "Local"},
                {"name": "Remote", "value": 1, "display_name": "Remote"},
            ]
        },
    )
]
_ORIGINAL_NODEIDS: tuple = (
    [
        ("ns=1;i=3003", "ns=1;i=5012", ["i=21", "i=17"]),
        ("ns=1;i=3002", "ns=1;i=5001", ["i=17", "i=21"]),
    ],
    ["ns=1;i=3004"],
)
_NODES: dict = {
    "datatypes": {
        "MaintenanceMethodEnum": (
            "D",
            "ns=1;i=3004",
            {"EnumValues": ("V", "ns=1;i=6029", {})},
        ),
        "NameNodeIdDataType": ("D", "ns=1;i=3003", {}),
        "RootCauseDataType": ("D", "ns=1;i=3002", {}),
    },
    "ifacetypes": {
        "IMaintenanceEventType": (
            "OT",
            "ns=1;i=1012",
            {
                "ConfigurationChanged": ("V", "ns=1;i=6042", {}),
                "EstimatedDowntime": ("V", "ns=1;i=6036", {}),
                "MaintenanceMethod": ("V", "ns=1;i=6041", {}),
                "MaintenanceState": (
                    "O",
                    "ns=1;i=5014",
                    {
                        "CurrentState": (
                            "V",
                            "ns=1;i=6033",
                            {"Id": ("V", "ns=1;i=6034", {})},
                        )
                    },
                ),
                "MaintenanceSupplier": ("V", "ns=1;i=6037", {}),
                "PartsOfAssetReplaced": ("V", "ns=1;i=6039", {}),
                "PartsOfAssetServiced": ("V", "ns=1;i=6040", {}),
                "PlannedDate": ("V", "ns=1;i=6035", {}),
                "QualificationOfPersonnel": ("V", "ns=1;i=6038", {}),
            },
        ),
        "IRootCauseIndicationType": (
            "OT",
            "ns=1;i=1002",
            {"PotentialRootCauses": ("V", "ns=1;i=6015", {})},
        ),
    },
    "objects": {
        "Assets": (
            "O",
            "ns=1;i=5002",
            {
                "AssetsByAssetId": (
                    "O",
                    "ns=1;i=5004",
                    {
                        "FindAlias": (
                            "M",
                            "ns=1;i=7003",
                            {
                                "InputArguments": ("V", "ns=1;i=6006", {}),
                                "OutputArguments": ("V", "ns=1;i=6007", {}),
                            },
                        ),
                        "NodeVersion": ("V", "ns=1;i=6008", {}),
                    },
                ),
                "AssetsByProductInstanceUri": (
                    "O",
                    "ns=1;i=5003",
                    {
                        "FindAlias": (
                            "M",
                            "ns=1;i=7002",
                            {
                                "InputArguments": ("V", "ns=1;i=6003", {}),
                                "OutputArguments": ("V", "ns=1;i=6004", {}),
                            },
                        ),
                        "NodeVersion": ("V", "ns=1;i=6005", {}),
                    },
                ),
                "FindAlias": (
                    "M",
                    "ns=1;i=7001",
                    {
                        "InputArguments": ("V", "ns=1;i=6001", {}),
                        "OutputArguments": ("V", "ns=1;i=6002", {}),
                    },
                ),
            },
        ),
        "Default Binary": ("O", "ns=1;i=5012", {}),
        "Default XML": ("O", "ns=1;i=5013", {}),
        "HierarchicalLocations": ("O", "ns=1;i=5021", {}),
        "OperationalLocations": ("O", "ns=1;i=5022", {}),
        "TypeDictionary": (
            "V",
            "ns=1;i=6011",
            {
                "NameNodeIdDataType": ("V", "ns=1;i=6028", {}),
                "NamespaceUri": ("V", "ns=1;i=6012", {}),
                "RootCauseDataType": ("V", "ns=1;i=6014", {}),
            },
        ),
        "http://opcfoundation.org/UA/AMB/": (
            "O",
            "ns=1;i=5018",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=6043", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=6044", {}),
                "NamespaceUri": ("V", "ns=1;i=6045", {}),
                "NamespaceVersion": ("V", "ns=1;i=6046", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=6047", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=6048", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=6049", {}),
            },
        ),
    },
    "objtypes": {
        "BadConfigurationConditionClassType": ("OT", "ns=1;i=1008", {}),
        "CalibrationDueConditionClassType": ("OT", "ns=1;i=1005", {}),
        "ConnectionFailureConditionClassType": ("OT", "ns=1;i=1003", {}),
        "DocumentationLinksType": (
            "OT",
            "ns=1;i=1011",
            {
                "<Link>": ("V", "ns=1;i=6017", {}),
                "AddLink": (
                    "M",
                    "ns=1;i=7004",
                    {
                        "InputArguments": ("V", "ns=1;i=6018", {}),
                        "OutputArguments": ("V", "ns=1;i=6019", {}),
                    },
                ),
                "DefaultInstanceBrowseName": ("V", "ns=1;i=6016", {}),
                "RemoveLink": (
                    "M",
                    "ns=1;i=7005",
                    {"InputArguments": ("V", "ns=1;i=6020", {})},
                ),
            },
        ),
        "ExternalCheckConditionClassType": ("OT", "ns=1;i=1015", {}),
        "FlashUpdateFailedConditionClassType": ("OT", "ns=1;i=1019", {}),
        "FlashUpdateInProgressConditionClassType": ("OT", "ns=1;i=1007", {}),
        "ImprovementConditionClassType": ("OT", "ns=1;i=1018", {}),
        "InspectionConditionClassType": ("OT", "ns=1;i=1014", {}),
        "MaintenanceEventStateMachineType": (
            "OT",
            "ns=1;i=1013",
            {
                "Executing": (
                    "O",
                    "ns=1;i=5007",
                    {"StateNumber": ("V", "ns=1;i=6022", {})},
                ),
                "Finished": (
                    "O",
                    "ns=1;i=5008",
                    {"StateNumber": ("V", "ns=1;i=6023", {})},
                ),
                "FromExecutingToFinished": (
                    "O",
                    "ns=1;i=5010",
                    {"TransitionNumber": ("V", "ns=1;i=6025", {})},
                ),
                "FromFinishedToPlanned": (
                    "O",
                    "ns=1;i=5011",
                    {"TransitionNumber": ("V", "ns=1;i=6026", {})},
                ),
                "FromPlannedToExecuting": (
                    "O",
                    "ns=1;i=5009",
                    {"TransitionNumber": ("V", "ns=1;i=6024", {})},
                ),
                "Planned": (
                    "O",
                    "ns=1;i=5006",
                    {"StateNumber": ("V", "ns=1;i=6021", {})},
                ),
            },
        ),
        "OutOfResourcesConditionClassType": (
            "OT",
            "ns=1;i=1009",
            {"OutOfMemoryConditionClassType": ("OT", "ns=1;i=1010", {})},
        ),
        "OverTemperatureConditionClassType": ("OT", "ns=1;i=1004", {}),
        "RepairConditionClassType": ("OT", "ns=1;i=1017", {}),
        "SelfTestFailureConditionClassType": ("OT", "ns=1;i=1006", {}),
        "ServicingConditionClassType": ("OT", "ns=1;i=1016", {}),
    },
    "reftypes": {
        "Contains": (
            "RT",
            "ns=1;i=4002",
            {
                "HierarchicalContains": ("RT", "ns=1;i=4003", {}),
                "OperationalContains": ("RT", "ns=1;i=4004", {}),
            },
        )
    },
}
