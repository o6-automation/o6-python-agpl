# AUTO-GENERATED — DO NOT EDIT
# source-sha256: d68852c397cb2604646a31a2a8448bfdaff46c7a7505101a03716a897ad975df
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/GPOS/"
_VERSION: str = "1.0.0"
_REQUIRED: list = [
    {"uri": "http://opcfoundation.org/UA/", "version": "1.05.05"},
    {"uri": "http://opcfoundation.org/UA/RSL/", "version": "1.00.1"},
]
_STRUCTURES: list = [
    (
        "ns=1;i=3003",
        "3DGeographicCoordinateDataType",
        "ns=1;i=5014",
        {
            "structure_type": 1,
            "fields": [
                {"name": "Longitude", "data_type": "i=11", "value_rank": -1},
                {"name": "Latitude", "data_type": "i=11", "value_rank": -1},
                {
                    "name": "Elevation",
                    "data_type": "i=11",
                    "value_rank": -1,
                    "is_optional": True,
                },
            ],
        },
    ),
    (
        "ns=1;i=3006",
        "GlobalPositionDataType",
        "ns=1;i=5001",
        {
            "structure_type": 1,
            "fields": [
                {
                    "name": "Accuracy",
                    "data_type": "i=11",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "Floor",
                    "data_type": "i=10",
                    "value_rank": -1,
                    "is_optional": True,
                },
            ],
        },
    ),
    (
        "ns=1;i=3004",
        "GlobalLocationDataType",
        "ns=1;i=5004",
        {
            "structure_type": 1,
            "fields": [
                {"name": "Position", "data_type": "ns=1;i=3006", "value_rank": -1},
                {
                    "name": "Orientation",
                    "data_type": "i=18812",
                    "value_rank": -1,
                    "is_optional": True,
                },
            ],
        },
    ),
    (
        "ns=1;i=3005",
        "GroundControlPointDataType",
        "ns=1;i=5008",
        {
            "structure_type": 0,
            "fields": [
                {
                    "name": "GlobalPosition",
                    "data_type": "ns=1;i=3003",
                    "value_rank": -1,
                },
                {"name": "LocalPosition", "data_type": "i=18810", "value_rank": -1},
            ],
        },
    ),
]
_ENUMS: list = []
_ORIGINAL_NODEIDS: tuple = (
    [
        ("ns=1;i=3003", "ns=1;i=5014", ["i=11", "i=11", "i=11"]),
        ("ns=1;i=3006", "ns=1;i=5001", ["i=11", "i=10"]),
        ("ns=1;i=3004", "ns=1;i=5004", ["ns=1;i=3006", "i=18812"]),
        ("ns=1;i=3005", "ns=1;i=5008", ["ns=1;i=3003", "i=18810"]),
    ],
    [],
)
_NODES: dict = {
    "datatypes": {
        "3DGeographicCoordinateDataType": (
            "D",
            "ns=1;i=3003",
            {"GlobalPositionDataType": ("D", "ns=1;i=3006", {})},
        ),
        "GlobalLocationDataType": ("D", "ns=1;i=3004", {}),
        "GroundControlPointDataType": ("D", "ns=1;i=3005", {}),
    },
    "objects": {
        "Default Binary": ("O", "ns=1;i=5014", {}),
        "Default XML": ("O", "ns=1;i=5015", {}),
        "GlobalLocations": ("O", "ns=1;i=5013", {}),
        "TypeDictionary": (
            "V",
            "ns=1;i=6004",
            {
                "3DGeographicCoordinateDataType": ("V", "ns=1;i=6017", {}),
                "Deprecated": ("V", "ns=1;i=6006", {}),
                "GlobalLocationDataType": ("V", "ns=1;i=6042", {}),
                "GlobalPositionDataType": ("V", "ns=1;i=6040", {}),
                "GroundControlPointDataType": ("V", "ns=1;i=6052", {}),
                "NamespaceUri": ("V", "ns=1;i=6005", {}),
            },
        ),
        "http://opcfoundation.org/UA/GPOS/": (
            "O",
            "ns=1;i=5007",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=6019", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=6020", {}),
                "NamespaceUri": ("V", "ns=1;i=6021", {}),
                "NamespaceVersion": ("V", "ns=1;i=6022", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=6023", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=6024", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=6025", {}),
            },
        ),
    },
    "objtypes": {
        "ZoneType": (
            "OT",
            "ns=1;i=1005",
            {
                "Building": ("V", "ns=1;i=6010", {}),
                "Floor": ("V", "ns=1;i=6011", {}),
                "GroundControlPoints": ("V", "ns=1;i=6047", {}),
                "IncompleteConfiguration": ("V", "ns=1;i=6013", {}),
                "Position": ("V", "ns=1;i=6045", {}),
                "Radius": ("V", "ns=1;i=6046", {}),
                "Site": ("V", "ns=1;i=6026", {}),
                "ZoneId": ("V", "ns=1;i=6043", {}),
            },
        )
    },
    "vartypes": {
        "GlobalLocationType": (
            "VT",
            "ns=1;i=2003",
            {
                "Orientation": (
                    "V",
                    "ns=1;i=6008",
                    {
                        "A": ("V", "ns=1;i=6014", {}),
                        "B": ("V", "ns=1;i=6015", {}),
                        "C": ("V", "ns=1;i=6016", {}),
                    },
                ),
                "Position": (
                    "V",
                    "ns=1;i=6009",
                    {
                        "CoordinateReferenceSystem": (
                            "V",
                            "ns=1;i=6036",
                            {
                                "EnumValues": ("V", "ns=1;i=6037", {}),
                                "ValueAsText": ("V", "ns=1;i=6048", {}),
                            },
                        ),
                        "Latitude": ("V", "ns=1;i=6032", {}),
                        "Longitude": ("V", "ns=1;i=6031", {}),
                        "SourceId": ("V", "ns=1;i=6039", {}),
                    },
                ),
            },
        ),
        "GlobalPositionType": (
            "VT",
            "ns=1;i=2006",
            {
                "Accuracy": ("V", "ns=1;i=6028", {}),
                "CoordinateReferenceSystem": (
                    "V",
                    "ns=1;i=6033",
                    {
                        "EnumValues": ("V", "ns=1;i=6034", {}),
                        "ValueAsText": ("V", "ns=1;i=6035", {}),
                    },
                ),
                "Elevation": ("V", "ns=1;i=6030", {}),
                "ElevationReference": (
                    "V",
                    "ns=1;i=6049",
                    {
                        "EnumValues": ("V", "ns=1;i=6050", {}),
                        "ValueAsText": ("V", "ns=1;i=6051", {}),
                    },
                ),
                "Floor": ("V", "ns=1;i=6012", {}),
                "Latitude": ("V", "ns=1;i=6029", {}),
                "Longitude": ("V", "ns=1;i=6027", {}),
                "SourceId": ("V", "ns=1;i=6038", {}),
            },
        ),
    },
}
