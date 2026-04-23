# AUTO-GENERATED — DO NOT EDIT
# source-sha256: c22bb62dc971eaec64dce9c3445d7c87a6a56a29d179d5ff5ea485547e06046c
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://fdi-cooperation.com/OPCUA/FDI5/"
_VERSION: str = "1.1"
_REQUIRED: list = [
    {"uri": "http://opcfoundation.org/UA/", "version": "1.04.3"},
    {"uri": "http://opcfoundation.org/UA/DI/", "version": "1.02"},
]
_STRUCTURES: list = [
    (
        "ns=1;i=37",
        "RegistrationParameters",
        "ns=1;i=118",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Path", "data_type": "i=540", "value_rank": -1},
                {"name": "SelectionFlags", "data_type": "i=7", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=38",
        "RegisteredNode",
        "ns=1;i=119",
        {
            "structure_type": 0,
            "fields": [
                {"name": "NodeStatus", "data_type": "i=6", "value_rank": -1},
                {"name": "OnlineContextNodeId", "data_type": "i=17", "value_rank": -1},
                {"name": "OnlineDeviceNodeId", "data_type": "i=17", "value_rank": -1},
                {"name": "OfflineContextNodeId", "data_type": "i=17", "value_rank": -1},
                {"name": "OfflineDeviceNodeId", "data_type": "i=17", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=39",
        "RegisterNodesResult",
        "ns=1;i=120",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Status", "data_type": "i=6", "value_rank": -1},
                {"name": "RegisteredNodes", "data_type": "ns=1;i=38", "value_rank": 1},
            ],
        },
    ),
    (
        "ns=1;i=43",
        "TransferIncident",
        "ns=1;i=121",
        {
            "structure_type": 0,
            "fields": [
                {"name": "ContextNodeId", "data_type": "i=17", "value_rank": -1},
                {"name": "StatusCode", "data_type": "i=19", "value_rank": -1},
                {"name": "Diagnostics", "data_type": "i=25", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=44",
        "ApplyResult",
        "ns=1;i=122",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Status", "data_type": "i=6", "value_rank": -1},
                {
                    "name": "TransferIncidents",
                    "data_type": "ns=1;i=43",
                    "value_rank": 1,
                },
            ],
        },
    ),
]
_ENUMS: list = [
    (
        "ns=1;i=194",
        "WindowModeType",
        {
            "fields": [
                {"name": "ModalWindow", "value": 1, "display_name": "ModalWindow"},
                {
                    "name": "NonModalWindow",
                    "value": 2,
                    "display_name": "NonModalWindow",
                },
                {"name": "UIP", "value": 3, "display_name": "UIP"},
            ]
        },
    ),
    (
        "ns=1;i=196",
        "StyleType",
        {
            "fields": [
                {"name": "Window", "value": 1, "display_name": "Window"},
                {"name": "Dialog", "value": 2, "display_name": "Dialog"},
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = (
    [
        ("ns=1;i=37", "ns=1;i=118", ["i=540", "i=7"]),
        ("ns=1;i=38", "ns=1;i=119", ["i=6", "i=17", "i=17", "i=17", "i=17"]),
        ("ns=1;i=39", "ns=1;i=120", ["i=6", "ns=1;i=38"]),
        ("ns=1;i=43", "ns=1;i=121", ["i=17", "i=19", "i=25"]),
        ("ns=1;i=44", "ns=1;i=122", ["i=6", "ns=1;i=43"]),
    ],
    ["ns=1;i=194", "ns=1;i=196"],
)
_NODES: dict = {
    "datatypes": {
        "ApplyResult": ("D", "ns=1;i=44", {}),
        "RegisterNodesResult": ("D", "ns=1;i=39", {}),
        "RegisteredNode": ("D", "ns=1;i=38", {}),
        "RegistrationParameters": ("D", "ns=1;i=37", {}),
        "StyleType": ("D", "ns=1;i=196", {"EnumValues": ("V", "ns=1;i=197", {})}),
        "TransferIncident": ("D", "ns=1;i=43", {}),
        "WindowModeType": ("D", "ns=1;i=194", {"EnumValues": ("V", "ns=1;i=195", {})}),
    },
    "objects": {
        "ActionIdentifier": ("O", "ns=1;i=182", {}),
        "ActionSet": (
            "O",
            "ns=1;i=183",
            {
                "AbortAction": (
                    "M",
                    "ns=1;i=190",
                    {
                        "InputArguments": ("V", "ns=1;i=191", {}),
                        "OutputArguments": ("V", "ns=1;i=192", {}),
                    },
                ),
                "InvokeAction": (
                    "M",
                    "ns=1;i=184",
                    {
                        "InputArguments": ("V", "ns=1;i=185", {}),
                        "OutputArguments": ("V", "ns=1;i=186", {}),
                    },
                ),
                "RespondAction": (
                    "M",
                    "ns=1;i=187",
                    {
                        "InputArguments": ("V", "ns=1;i=188", {}),
                        "OutputArguments": ("V", "ns=1;i=189", {}),
                    },
                ),
            },
        ),
        "Default Binary": ("O", "ns=1;i=122", {}),
        "Default JSON": ("O", "ns=1;i=8005", {}),
        "Default XML": ("O", "ns=1;i=99", {}),
        "DeviceHealthDiagnostics": ("V", "ns=1;i=198", {}),
        "FDIServerVersion": ("V", "ns=1;i=94", {}),
        "LogAuditTrailMessage": (
            "M",
            "ns=1;i=92",
            {"InputArguments": ("V", "ns=1;i=93", {})},
        ),
        "Opc.Ua.Fdi5": (
            "V",
            "ns=1;i=100",
            {
                "ApplyResult": ("V", "ns=1;i=115", {}),
                "Deprecated": ("V", "ns=1;i=8008", {}),
                "NamespaceUri": ("V", "ns=1;i=102", {}),
                "RegisterNodesResult": ("V", "ns=1;i=109", {}),
                "RegisteredNode": ("V", "ns=1;i=106", {}),
                "RegistrationParameters": ("V", "ns=1;i=103", {}),
                "TransferIncident": ("V", "ns=1;i=112", {}),
            },
        ),
        "http://fdi-cooperation.com/OPCUA/FDI5/": (
            "O",
            "ns=1;i=15001",
            {
                "DefaultAccessRestrictions": ("V", "ns=1;i=15033", {}),
                "DefaultRolePermissions": ("V", "ns=1;i=15031", {}),
                "DefaultUserRolePermissions": ("V", "ns=1;i=15032", {}),
                "IsNamespaceSubset": ("V", "ns=1;i=15005", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=15004", {}),
                "NamespaceUri": ("V", "ns=1;i=15002", {}),
                "NamespaceVersion": ("V", "ns=1;i=15003", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=15006", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=15007", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=15008", {}),
            },
        ),
    },
    "objtypes": {
        "ActionServiceType": (
            "OT",
            "ns=1;i=21",
            {
                "<ActionIdentifier>": ("O", "ns=1;i=181", {}),
                "AbortAction": (
                    "M",
                    "ns=1;i=28",
                    {
                        "InputArguments": ("V", "ns=1;i=29", {}),
                        "OutputArguments": ("V", "ns=1;i=30", {}),
                    },
                ),
                "InvokeAction": (
                    "M",
                    "ns=1;i=22",
                    {
                        "InputArguments": ("V", "ns=1;i=23", {}),
                        "OutputArguments": ("V", "ns=1;i=24", {}),
                    },
                ),
                "RespondAction": (
                    "M",
                    "ns=1;i=25",
                    {
                        "InputArguments": ("V", "ns=1;i=26", {}),
                        "OutputArguments": ("V", "ns=1;i=27", {}),
                    },
                ),
            },
        ),
        "ActionType": ("OT", "ns=1;i=11", {}),
        "DirectDeviceAccessType": (
            "OT",
            "ns=1;i=82",
            {
                "EndDirectAccess": (
                    "M",
                    "ns=1;i=89",
                    {
                        "InputArguments": ("V", "ns=1;i=90", {}),
                        "OutputArguments": ("V", "ns=1;i=91", {}),
                    },
                ),
                "InitDirectAccess": (
                    "M",
                    "ns=1;i=83",
                    {
                        "InputArguments": ("V", "ns=1;i=84", {}),
                        "OutputArguments": ("V", "ns=1;i=85", {}),
                    },
                ),
                "Transfer": (
                    "M",
                    "ns=1;i=86",
                    {
                        "InputArguments": ("V", "ns=1;i=87", {}),
                        "OutputArguments": ("V", "ns=1;i=88", {}),
                    },
                ),
            },
        ),
        "EditContextType": (
            "OT",
            "ns=1;i=54",
            {
                "Apply": (
                    "M",
                    "ns=1;i=64",
                    {
                        "InputArguments": ("V", "ns=1;i=65", {}),
                        "OutputArguments": ("V", "ns=1;i=66", {}),
                    },
                ),
                "Discard": (
                    "M",
                    "ns=1;i=70",
                    {
                        "InputArguments": ("V", "ns=1;i=71", {}),
                        "OutputArguments": ("V", "ns=1;i=72", {}),
                    },
                ),
                "GetEditContext": (
                    "M",
                    "ns=1;i=55",
                    {
                        "InputArguments": ("V", "ns=1;i=56", {}),
                        "OutputArguments": ("V", "ns=1;i=57", {}),
                    },
                ),
                "RegisterNodesById": (
                    "M",
                    "ns=1;i=58",
                    {
                        "InputArguments": ("V", "ns=1;i=59", {}),
                        "OutputArguments": ("V", "ns=1;i=60", {}),
                    },
                ),
                "RegisterNodesByRelativePath": (
                    "M",
                    "ns=1;i=61",
                    {
                        "InputArguments": ("V", "ns=1;i=62", {}),
                        "OutputArguments": ("V", "ns=1;i=63", {}),
                    },
                ),
                "Reset": (
                    "M",
                    "ns=1;i=67",
                    {
                        "InputArguments": ("V", "ns=1;i=68", {}),
                        "OutputArguments": ("V", "ns=1;i=69", {}),
                    },
                ),
            },
        ),
    },
    "vartypes": {
        "UIDescriptionType": ("VT", "ns=1;i=1", {}),
        "UIPlugInType": (
            "VT",
            "ns=1;i=2",
            {
                "CpuInformation": ("V", "ns=1;i=6", {}),
                "Documentation": ("O", "ns=1;i=10", {}),
                "FDITechnologyVersion": ("V", "ns=1;i=4", {}),
                "PlatformId": ("V", "ns=1;i=7", {}),
                "RuntimeId": ("V", "ns=1;i=5", {}),
                "StartElementName": ("V", "ns=1;i=9", {}),
                "Style": ("V", "ns=1;i=8", {}),
                "UIPVariantVersion": ("V", "ns=1;i=3", {}),
            },
        ),
    },
}
