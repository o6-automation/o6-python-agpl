# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 5103589141a60aa6be8523a9b9d55327b76b8c1b2081feae12b7c93da6c7849c
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/RSL/"
_VERSION: str = "1.00.1"
_REQUIRED: list = [{"uri": "http://opcfoundation.org/UA/", "version": "1.05.02"}]
_STRUCTURES: list = []
_ENUMS: list = []
_ORIGINAL_NODEIDS: tuple = ([], [])
_NODES: dict = {
    "objects": {
        "RelativeSpatialLocations": ("O", "ns=1;i=5001", {}),
        "http://opcfoundation.org/UA/RSL/": (
            "O",
            "ns=1;i=5005",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=6028", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=6029", {}),
                "NamespaceUri": ("V", "ns=1;i=6030", {}),
                "NamespaceVersion": ("V", "ns=1;i=6031", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=6032", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=6033", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=6034", {}),
            },
        ),
    },
    "objtypes": {
        "SpatialObjectType": (
            "OT",
            "ns=1;i=1002",
            {
                "AlternativeFrames": (
                    "O",
                    "ns=1;i=5004",
                    {
                        "<FrameIdentifier>": (
                            "V",
                            "ns=1;i=6020",
                            {"Base": ("V", "ns=1;i=6021", {})},
                        )
                    },
                ),
                "AttachPoints": (
                    "O",
                    "ns=1;i=5002",
                    {
                        "<FrameIdentifier>": (
                            "V",
                            "ns=1;i=6018",
                            {"Base": ("V", "ns=1;i=6019", {})},
                        )
                    },
                ),
                "DefaultInstanceBrowseName": ("V", "ns=1;i=6017", {}),
                "Identifier": ("V", "ns=1;i=6016", {}),
                "InternalFrames": (
                    "O",
                    "ns=1;i=5003",
                    {
                        "<FrameIdentifier>": (
                            "V",
                            "ns=1;i=6022",
                            {"Base": ("V", "ns=1;i=6023", {})},
                        )
                    },
                ),
                "PositionFrame": (
                    "V",
                    "ns=1;i=6014",
                    {"Base": ("V", "ns=1;i=6015", {})},
                ),
            },
        ),
        "SpatialObjectsListType": (
            "OT",
            "ns=1;i=1003",
            {
                "<SpatialObject>": (
                    "O",
                    "ns=1;i=5006",
                    {
                        "DefaultInstanceBrowseName": ("V", "ns=1;i=6035", {}),
                        "PositionFrame": (
                            "V",
                            "ns=1;i=6038",
                            {"Base": ("V", "ns=1;i=6039", {})},
                        ),
                    },
                ),
                "Identifier": ("V", "ns=1;i=6024", {}),
                "NodeVersion": ("V", "ns=1;i=6027", {}),
                "WorldFrame": ("V", "ns=1;i=6025", {"Base": ("V", "ns=1;i=6026", {})}),
            },
        ),
    },
    "vartypes": {
        "RelativeValueType": (
            "VT",
            "ns=1;i=2002",
            {
                "Base": ("V", "ns=1;i=6001", {}),
                "SpatialLocationType": (
                    "VT",
                    "ns=1;i=2003",
                    {
                        "Base": ("V", "ns=1;i=6002", {}),
                        "CartesianFrameAngleOrientationType": (
                            "VT",
                            "ns=1;i=2004",
                            {
                                "Base": ("V", "ns=1;i=6005", {}),
                                "Orientation": (
                                    "V",
                                    "ns=1;i=6006",
                                    {
                                        "A": ("V", "ns=1;i=6042", {}),
                                        "AngleUnit": ("V", "ns=1;i=6036", {}),
                                        "B": ("V", "ns=1;i=6043", {}),
                                        "C": ("V", "ns=1;i=6044", {}),
                                    },
                                ),
                                "Position": (
                                    "V",
                                    "ns=1;i=6007",
                                    {
                                        "LengthUnit": ("V", "ns=1;i=6045", {}),
                                        "X": ("V", "ns=1;i=6011", {}),
                                        "Y": ("V", "ns=1;i=6012", {}),
                                        "Z": ("V", "ns=1;i=6013", {}),
                                    },
                                ),
                            },
                        ),
                        "Orientation": ("V", "ns=1;i=6004", {}),
                        "Position": ("V", "ns=1;i=6003", {}),
                    },
                ),
            },
        ),
        "RpyOrientationType": (
            "VT",
            "ns=1;i=2005",
            {
                "A": ("V", "ns=1;i=6037", {}),
                "B": ("V", "ns=1;i=6040", {}),
                "C": ("V", "ns=1;i=6041", {}),
            },
        ),
    },
}
