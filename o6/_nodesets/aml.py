# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 765418b87cdf508815ff6b8565c0f8c18fc56aaafe4b5f29a2bcb73022905f14
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/AML/"
_VERSION: str = "1.00"
_REQUIRED: list = [{"uri": "http://opcfoundation.org/UA/", "version": ""}]
_STRUCTURES: list = []
_ENUMS: list = []
_ORIGINAL_NODEIDS: tuple = ([], [])
_NODES: dict = {
    "objects": {
        "AutomationMLFiles": ("O", "ns=1;i=5006", {}),
        "AutomationMLInstanceHierarchies": ("O", "ns=1;i=5005", {}),
        "AutomationMLLibraries": (
            "O",
            "ns=1;i=5007",
            {
                "InterfaceClassLibs": ("O", "ns=1;i=5008", {}),
                "RoleClassLibs": ("O", "ns=1;i=5009", {}),
                "SystemUnitClassLibs": ("O", "ns=1;i=5010", {}),
            },
        ),
        "ID": ("V", "ns=1;i=1010", {}),
        "Version": ("V", "ns=1;i=1011", {}),
    },
    "objtypes": {
        "CAEXBasicObjectType": (
            "OT",
            "ns=1;i=1006",
            {
                "CAEXFileType": (
                    "OT",
                    "ns=1;i=1005",
                    {
                        "InstanceHierarchies": ("O", "ns=1;i=5001", {}),
                        "InterfaceClassLibs": ("O", "ns=1;i=5002", {}),
                        "RoleClassLibs": ("O", "ns=1;i=5003", {}),
                        "SystemUnitClassLibs": ("O", "ns=1;i=5004", {}),
                    },
                ),
                "CAEXObjectType": (
                    "OT",
                    "ns=1;i=1001",
                    {
                        "AutomationMLBaseInterface": ("OT", "ns=1;i=1002", {}),
                        "AutomationMLBaseRole": ("OT", "ns=1;i=1003", {}),
                        "AutomationMLBaseSystemUnit": ("OT", "ns=1;i=1004", {}),
                        "ID": ("V", "ns=1;i=6002", {}),
                    },
                ),
                "Version": ("V", "ns=1;i=6001", {}),
            },
        )
    },
    "reftypes": {
        "HasAMLInternalLink": ("RT", "ns=1;i=4002", {}),
        "HasAMLRoleReference": ("RT", "ns=1;i=4001", {}),
    },
    "vartypes": {
        "AMLBaseVariableType": (
            "VT",
            "ns=1;i=3001",
            {
                "AMLOpcUaConnectionType": (
                    "VT",
                    "ns=1;i=3002",
                    {
                        "ServerAddress": ("V", "ns=1;i=1014", {}),
                        "ServerAlias": ("V", "ns=1;i=1015", {}),
                        "VariableName": ("V", "ns=1;i=1013", {}),
                        "VariableNodeId": ("V", "ns=1;i=1012", {}),
                    },
                )
            },
        )
    },
}
