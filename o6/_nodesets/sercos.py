# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 804f0db4cdbc7a782f12f1ad7a29c3f2b9835bf76aa9176b1077d472671f3072
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://sercos.org/UA/"
_VERSION: str = "1.00"
_REQUIRED: list = [
    {"uri": "http://opcfoundation.org/UA/", "version": "1.04.3"},
    {"uri": "http://opcfoundation.org/UA/DI/", "version": "1.02"},
]
_STRUCTURES: list = []
_ENUMS: list = []
_ORIGINAL_NODEIDS: tuple = ([], [])
_NODES: dict = {
    "objects": {
        "http://sercos.org/UA/": (
            "O",
            "ns=1;i=6081",
            {
                "DefaultAccessRestrictions": ("V", "ns=1;i=6113", {}),
                "DefaultRolePermissions": ("V", "ns=1;i=6111", {}),
                "DefaultUserRolePermissions": ("V", "ns=1;i=6112", {}),
                "IsNamespaceSubset": ("V", "ns=1;i=6085", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=6084", {}),
                "NamespaceUri": ("V", "ns=1;i=6082", {}),
                "NamespaceVersion": ("V", "ns=1;i=6083", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=6086", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=6087", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=6088", {}),
            },
        )
    },
    "objtypes": {
        "FunctionalGroupType": (
            "OT",
            "ns=1;i=6012",
            {
                "ClassSet": (
                    "OT",
                    "ns=1;i=6077",
                    {"<SercosClassIdentifier>": ("O", "ns=1;i=6078", {})},
                ),
                "FunctionGroupSet": (
                    "OT",
                    "ns=1;i=6079",
                    {"<FunctionGroupIdentifier>": ("O", "ns=1;i=6080", {})},
                ),
                "ProfileSet": (
                    "OT",
                    "ns=1;i=6075",
                    {"<SercosProfileIdentifier>": ("O", "ns=1;i=6076", {})},
                ),
                "SercosClassType": ("OT", "ns=1;i=1003", {}),
                "SercosFunctionGroupType": ("OT", "ns=1;i=1004", {}),
                "SercosProfileType": ("OT", "ns=1;i=1002", {}),
            },
        ),
        "SercosDeviceType": (
            "OT",
            "ns=1;i=1001",
            {
                "ClassSet": ("O", "ns=1;i=5002", {}),
                "FunctionGroupSet": ("O", "ns=1;i=5003", {}),
                "ParameterSet": ("O", "ns=1;i=5007", {}),
                "ProfileSet": ("O", "ns=1;i=5001", {}),
            },
        ),
    },
    "vartypes": {
        "SercosParameterType": (
            "VT",
            "ns=1;i=2001",
            {
                "Attribute": ("V", "ns=1;i=6004", {}),
                "DisplayMaxValue": ("V", "ns=1;i=6008", {}),
                "DisplayMinValue": ("V", "ns=1;i=6007", {}),
                "DisplayValue": ("V", "ns=1;i=6009", {}),
                "Exponent": ("V", "ns=1;i=6006", {}),
                "MaxValue": ("V", "ns=1;i=6001", {}),
                "MinValue": ("V", "ns=1;i=6002", {}),
                "ProcedureCommand": ("V", "ns=1;i=6005", {}),
            },
        )
    },
}
