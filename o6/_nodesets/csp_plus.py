# AUTO-GENERATED — DO NOT EDIT
# source-sha256: d0fe53d0a4ea0e4882fc743fc45a25ba93a065648e7dec215b4eadd574714cdd
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/CSPPlusForMachine/"
_VERSION: str = "1.00"
_REQUIRED: list = [
    {"uri": "http://opcfoundation.org/UA/", "version": "1.03"},
    {"uri": "http://opcfoundation.org/UA/DI/", "version": "1.01"},
]
_STRUCTURES: list = []
_ENUMS: list = []
_ORIGINAL_NODEIDS: tuple = ([], [])
_NODES: dict = {
    "objects": {
        "http://opcfoundation.org/UA/CSPPlusForMachine/": (
            "O",
            "ns=1;i=5005",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=6007", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=6008", {}),
                "NamespaceUri": ("V", "ns=1;i=6009", {}),
                "NamespaceVersion": ("V", "ns=1;i=6010", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=6011", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=6012", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=6013", {}),
            },
        )
    },
    "objtypes": {
        "CsppMachineType": (
            "OT",
            "ns=1;i=1001",
            {
                "<CommIfSection>": (
                    "O",
                    "ns=1;i=5002",
                    {
                        "<CommIfConfigurationPart>": (
                            "O",
                            "ns=1;i=5004",
                            {"<ConfigurationName>": ("V", "ns=1;i=6005", {})},
                        ),
                        "<CommIfVariablePart>": (
                            "O",
                            "ns=1;i=5003",
                            {"<VariableName>": ("V", "ns=1;i=6004", {})},
                        ),
                        "<VariableOrConfigurationName>": ("V", "ns=1;i=6003", {}),
                    },
                ),
                "ParameterSet": (
                    "O",
                    "ns=1;i=5001",
                    {
                        "<ConfigurationName>": ("V", "ns=1;i=6002", {}),
                        "<VariableName>": ("V", "ns=1;i=6001", {}),
                    },
                ),
            },
        )
    },
    "vartypes": {
        "CsppAnalogItemType": (
            "VT",
            "ns=1;i=2001",
            {"Duration": ("V", "ns=1;i=6006", {})},
        )
    },
}
