# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 0c541ac40a8a5fffefd61e85dfa5853a4669e87cc08115b6906cee829d033c14
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/WoT-Con/"
_VERSION: str = "1.02.0"
_REQUIRED: list = [{"uri": "http://opcfoundation.org/UA/", "version": "1.05.04"}]
_STRUCTURES: list = []
_ENUMS: list = []
_ORIGINAL_NODEIDS: tuple = ([], [])
_NODES: dict = {
    "ifacetypes": {
        "IWoTAssetType": (
            "OT",
            "ns=1;i=42",
            {
                "AssetEndpoint": ("V", "ns=1;i=122", {}),
                "WoTFile": (
                    "O",
                    "ns=1;i=43",
                    {
                        "Close": (
                            "M",
                            "ns=1;i=54",
                            {"InputArguments": ("V", "ns=1;i=55", {})},
                        ),
                        "CloseAndUpdate": (
                            "M",
                            "ns=1;i=106",
                            {"InputArguments": ("V", "ns=1;i=107", {})},
                        ),
                        "GetPosition": (
                            "M",
                            "ns=1;i=61",
                            {
                                "InputArguments": ("V", "ns=1;i=62", {}),
                                "OutputArguments": ("V", "ns=1;i=63", {}),
                            },
                        ),
                        "Open": (
                            "M",
                            "ns=1;i=51",
                            {
                                "InputArguments": ("V", "ns=1;i=52", {}),
                                "OutputArguments": ("V", "ns=1;i=53", {}),
                            },
                        ),
                        "OpenCount": ("V", "ns=1;i=47", {}),
                        "Read": (
                            "M",
                            "ns=1;i=56",
                            {
                                "InputArguments": ("V", "ns=1;i=57", {}),
                                "OutputArguments": ("V", "ns=1;i=58", {}),
                            },
                        ),
                        "SetPosition": (
                            "M",
                            "ns=1;i=64",
                            {"InputArguments": ("V", "ns=1;i=65", {})},
                        ),
                        "Size": ("V", "ns=1;i=44", {}),
                        "UserWritable": ("V", "ns=1;i=46", {}),
                        "Writable": ("V", "ns=1;i=45", {}),
                        "Write": (
                            "M",
                            "ns=1;i=59",
                            {"InputArguments": ("V", "ns=1;i=60", {})},
                        ),
                    },
                ),
            },
        ),
        "WoTAssetConfigurationType": (
            "OT",
            "ns=1;i=105",
            {
                "<WoTConfigurationParameterName>": ("V", "ns=1;i=108", {}),
                "License": ("V", "ns=1;i=109", {}),
            },
        ),
    },
    "objects": {
        "<WoTPropertyName>": ("V", "ns=1;i=66", {}),
        "WoTAssetConnectionManagement": (
            "O",
            "ns=1;i=31",
            {
                "CreateAsset": (
                    "M",
                    "ns=1;i=32",
                    {
                        "InputArguments": ("V", "ns=1;i=33", {}),
                        "OutputArguments": ("V", "ns=1;i=34", {}),
                    },
                ),
                "DeleteAsset": (
                    "M",
                    "ns=1;i=35",
                    {"InputArguments": ("V", "ns=1;i=36", {})},
                ),
            },
        ),
        "http://opcfoundation.org/UA/WoT-Con/": (
            "O",
            "ns=1;i=67",
            {
                "DefaultAccessRestrictions": ("V", "ns=1;i=101", {}),
                "DefaultRolePermissions": ("V", "ns=1;i=99", {}),
                "DefaultUserRolePermissions": ("V", "ns=1;i=100", {}),
                "IsNamespaceSubset": ("V", "ns=1;i=71", {}),
                "ModelVersion": ("V", "ns=1;i=39", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=70", {}),
                "NamespaceUri": ("V", "ns=1;i=68", {}),
                "NamespaceVersion": ("V", "ns=1;i=69", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=72", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=73", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=74", {}),
            },
        ),
    },
    "objtypes": {
        "WoTAssetConnectionManagementType": (
            "OT",
            "ns=1;i=1",
            {
                "<WoTAssetName>": (
                    "O",
                    "ns=1;i=2",
                    {
                        "AssetEndpoint": ("V", "ns=1;i=169", {}),
                        "WoTFile": (
                            "O",
                            "ns=1;i=144",
                            {
                                "Close": (
                                    "M",
                                    "ns=1;i=155",
                                    {"InputArguments": ("V", "ns=1;i=156", {})},
                                ),
                                "CloseAndUpdate": (
                                    "M",
                                    "ns=1;i=167",
                                    {"InputArguments": ("V", "ns=1;i=168", {})},
                                ),
                                "GetPosition": (
                                    "M",
                                    "ns=1;i=162",
                                    {
                                        "InputArguments": ("V", "ns=1;i=163", {}),
                                        "OutputArguments": ("V", "ns=1;i=164", {}),
                                    },
                                ),
                                "Open": (
                                    "M",
                                    "ns=1;i=152",
                                    {
                                        "InputArguments": ("V", "ns=1;i=153", {}),
                                        "OutputArguments": ("V", "ns=1;i=154", {}),
                                    },
                                ),
                                "OpenCount": ("V", "ns=1;i=148", {}),
                                "Read": (
                                    "M",
                                    "ns=1;i=157",
                                    {
                                        "InputArguments": ("V", "ns=1;i=158", {}),
                                        "OutputArguments": ("V", "ns=1;i=159", {}),
                                    },
                                ),
                                "SetPosition": (
                                    "M",
                                    "ns=1;i=165",
                                    {"InputArguments": ("V", "ns=1;i=166", {})},
                                ),
                                "Size": ("V", "ns=1;i=145", {}),
                                "UserWritable": ("V", "ns=1;i=147", {}),
                                "Writable": ("V", "ns=1;i=146", {}),
                                "Write": (
                                    "M",
                                    "ns=1;i=160",
                                    {"InputArguments": ("V", "ns=1;i=161", {})},
                                ),
                            },
                        ),
                    },
                ),
                "Configuration": ("O", "ns=1;i=78", {}),
                "ConnectionTest": (
                    "M",
                    "ns=1;i=75",
                    {
                        "InputArguments": ("V", "ns=1;i=76", {}),
                        "OutputArguments": ("V", "ns=1;i=77", {}),
                    },
                ),
                "CreateAsset": (
                    "M",
                    "ns=1;i=26",
                    {
                        "InputArguments": ("V", "ns=1;i=27", {}),
                        "OutputArguments": ("V", "ns=1;i=28", {}),
                    },
                ),
                "CreateAssetForEndpoint": (
                    "M",
                    "ns=1;i=49",
                    {
                        "InputArguments": ("V", "ns=1;i=50", {}),
                        "OutputArguments": ("V", "ns=1;i=170", {}),
                    },
                ),
                "DeleteAsset": (
                    "M",
                    "ns=1;i=29",
                    {"InputArguments": ("V", "ns=1;i=30", {})},
                ),
                "DiscoverAssets": (
                    "M",
                    "ns=1;i=41",
                    {"OutputArguments": ("V", "ns=1;i=48", {})},
                ),
                "SupportedWoTBindings": ("V", "ns=1;i=40", {}),
            },
        ),
        "WoTAssetFileType": (
            "OT",
            "ns=1;i=110",
            {
                "CloseAndUpdate": (
                    "M",
                    "ns=1;i=111",
                    {"InputArguments": ("V", "ns=1;i=112", {})},
                )
            },
        ),
    },
    "reftypes": {"HasWoTComponent": ("RT", "ns=1;i=142", {})},
}
