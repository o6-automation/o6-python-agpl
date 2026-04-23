# AUTO-GENERATED — DO NOT EDIT
# source-sha256: c3d5e77aaeeed03862620e307cdf4974e5998267e8faa992c1f1a24f9be6a4ba
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/AutoID/"
_VERSION: str = "1.01"
_REQUIRED: list = [
    {"uri": "http://opcfoundation.org/UA/", "version": "1.03"},
    {"uri": "http://opcfoundation.org/UA/DI/", "version": "1.01"},
]
_STRUCTURES: list = [
    (
        "ns=1;i=3017",
        "AccessResult",
        "ns=1;i=5022",
        {
            "structure_type": 1,
            "fields": [
                {
                    "name": "CodeType",
                    "data_type": "i=12",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "Identifier",
                    "data_type": "ns=1;i=3020",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "Timestamp",
                    "data_type": "i=294",
                    "value_rank": -1,
                    "is_optional": True,
                },
            ],
        },
    ),
    (
        "ns=1;i=3018",
        "RfidAccessResult",
        "ns=1;i=5024",
        {
            "structure_type": 1,
            "fields": [
                {
                    "name": "CodeTypeRWData",
                    "data_type": "i=12",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "RWData",
                    "data_type": "ns=1;i=3020",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "Antenna",
                    "data_type": "i=6",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "CurrentPowerLevel",
                    "data_type": "i=6",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "PC",
                    "data_type": "i=5",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "Polarization",
                    "data_type": "i=12",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "Strength",
                    "data_type": "i=6",
                    "value_rank": -1,
                    "is_optional": True,
                },
            ],
        },
    ),
    (
        "ns=1;i=3011",
        "AntennaNameIdPair",
        "ns=1;i=5017",
        {
            "structure_type": 0,
            "fields": [
                {"name": "AntennaId", "data_type": "i=6", "value_rank": -1},
                {"name": "AntennaName", "data_type": "i=12", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3023",
        "DhcpGeoConfCoordinate",
        "ns=1;i=5034",
        {
            "structure_type": 0,
            "fields": [
                {"name": "LaRes", "data_type": "i=3", "value_rank": -1},
                {"name": "LatitudeInteger", "data_type": "i=4", "value_rank": -1},
                {"name": "LatitudeFraction", "data_type": "i=6", "value_rank": -1},
                {"name": "LoRes", "data_type": "i=3", "value_rank": -1},
                {"name": "LongitudeInteger", "data_type": "i=4", "value_rank": -1},
                {"name": "LongitudeFraction", "data_type": "i=6", "value_rank": -1},
                {"name": "AT", "data_type": "i=3", "value_rank": -1},
                {"name": "AltRes", "data_type": "i=3", "value_rank": -1},
                {"name": "AltitudeInteger", "data_type": "i=6", "value_rank": -1},
                {"name": "AltitudeFraction", "data_type": "i=4", "value_rank": -1},
                {"name": "Datum", "data_type": "i=3", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3019",
        "LocalCoordinate",
        "ns=1;i=5028",
        {
            "structure_type": 0,
            "fields": [
                {"name": "X", "data_type": "i=11", "value_rank": -1},
                {"name": "Y", "data_type": "i=11", "value_rank": -1},
                {"name": "Z", "data_type": "i=11", "value_rank": -1},
                {"name": "Timestamp", "data_type": "i=294", "value_rank": -1},
                {"name": "DilutionOfPrecision", "data_type": "i=11", "value_rank": -1},
                {"name": "UsefulPrecision", "data_type": "i=6", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3004",
        "Position",
        "ns=1;i=5007",
        {
            "structure_type": 0,
            "fields": [
                {"name": "PositionX", "data_type": "i=6", "value_rank": -1},
                {"name": "PositionY", "data_type": "i=6", "value_rank": -1},
                {"name": "SizeX", "data_type": "i=6", "value_rank": -1},
                {"name": "SizeY", "data_type": "i=6", "value_rank": -1},
                {"name": "Rotation", "data_type": "i=6", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3006",
        "RfidSighting",
        "ns=1;i=5009",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Antenna", "data_type": "i=6", "value_rank": -1},
                {"name": "Strength", "data_type": "i=6", "value_rank": -1},
                {"name": "Timestamp", "data_type": "i=294", "value_rank": -1},
                {"name": "CurrentPowerLevel", "data_type": "i=6", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3029",
        "Rotation",
        "ns=1;i=5050",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Yaw", "data_type": "i=11", "value_rank": -1},
                {"name": "Pitch", "data_type": "i=11", "value_rank": -1},
                {"name": "Roll", "data_type": "i=11", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3024",
        "ScanDataEpc",
        "ns=1;i=5036",
        {
            "structure_type": 0,
            "fields": [
                {"name": "PC", "data_type": "i=5", "value_rank": -1},
                {"name": "UId", "data_type": "i=15", "value_rank": -1},
                {"name": "XPC_W1", "data_type": "i=5", "value_rank": -1},
                {"name": "XPC_W2", "data_type": "i=5", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3001",
        "ScanResult",
        "ns=1;i=5002",
        {
            "structure_type": 1,
            "fields": [
                {"name": "CodeType", "data_type": "i=12", "value_rank": -1},
                {"name": "ScanData", "data_type": "ns=1;i=3020", "value_rank": -1},
                {"name": "Timestamp", "data_type": "i=294", "value_rank": -1},
                {
                    "name": "Location",
                    "data_type": "ns=1;i=3008",
                    "value_rank": -1,
                    "is_optional": True,
                },
            ],
        },
    ),
    (
        "ns=1;i=3002",
        "OcrScanResult",
        "ns=1;i=5004",
        {
            "structure_type": 1,
            "fields": [
                {"name": "ImageId", "data_type": "i=17", "value_rank": -1},
                {"name": "Quality", "data_type": "i=3", "value_rank": -1},
                {"name": "Position", "data_type": "ns=1;i=3004", "value_rank": -1},
                {
                    "name": "Font",
                    "data_type": "i=12",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "DecodingTime",
                    "data_type": "i=294",
                    "value_rank": -1,
                    "is_optional": True,
                },
            ],
        },
    ),
    (
        "ns=1;i=3026",
        "OpticalScanResult",
        "ns=1;i=5040",
        {
            "structure_type": 1,
            "fields": [
                {
                    "name": "Grade",
                    "data_type": "i=10",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "Position",
                    "data_type": "ns=1;i=3004",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "Symbology",
                    "data_type": "i=12",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "ImageId",
                    "data_type": "i=17",
                    "value_rank": -1,
                    "is_optional": True,
                },
            ],
        },
    ),
    (
        "ns=1;i=3030",
        "OpticalVerifierScanResult",
        "ns=1;i=5052",
        {
            "structure_type": 0,
            "fields": [
                {"name": "IsoGrade", "data_type": "i=12", "value_rank": -1},
                {"name": "RMin", "data_type": "i=4", "value_rank": -1},
                {"name": "SymbolContrast", "data_type": "i=4", "value_rank": -1},
                {"name": "ECMin", "data_type": "i=4", "value_rank": -1},
                {"name": "Modulation", "data_type": "i=4", "value_rank": -1},
                {"name": "Defects", "data_type": "i=4", "value_rank": -1},
                {"name": "Decodability", "data_type": "i=4", "value_rank": -1},
                {"name": "Decode", "data_type": "i=4", "value_rank": -1},
                {"name": "PrintGain", "data_type": "i=4", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3007",
        "RfidScanResult",
        "ns=1;i=5011",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Sighting", "data_type": "ns=1;i=3006", "value_rank": 1}
            ],
        },
    ),
    (
        "ns=1;i=3028",
        "RtlsLocationResult",
        "ns=1;i=5048",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Speed", "data_type": "i=11", "value_rank": -1},
                {"name": "Heading", "data_type": "i=11", "value_rank": -1},
                {"name": "Rotation", "data_type": "ns=1;i=3029", "value_rank": -1},
                {"name": "ReceiveTime", "data_type": "i=294", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3010",
        "ScanSettings",
        "ns=1;i=5015",
        {
            "structure_type": 1,
            "fields": [
                {"name": "Duration", "data_type": "i=290", "value_rank": -1},
                {"name": "Cycles", "data_type": "i=6", "value_rank": -1},
                {"name": "DataAvailable", "data_type": "i=1", "value_rank": -1},
                {
                    "name": "LocationType",
                    "data_type": "ns=1;i=3009",
                    "value_rank": -1,
                    "is_optional": True,
                },
            ],
        },
    ),
    (
        "ns=1;i=3008",
        "Location",
        "ns=1;i=5013",
        {
            "structure_type": 0,
            "fields": [
                {"name": "NMEA", "data_type": "i=12", "value_rank": -1},
                {"name": "Local", "data_type": "ns=1;i=3019", "value_rank": -1},
                {"name": "WGS84", "data_type": "ns=1;i=3027", "value_rank": -1},
                {"name": "Name", "data_type": "i=12", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3020",
        "ScanData",
        "ns=1;i=5030",
        {
            "structure_type": 0,
            "fields": [
                {"name": "ByteString", "data_type": "i=15", "value_rank": -1},
                {"name": "String", "data_type": "i=12", "value_rank": -1},
                {"name": "Epc", "data_type": "ns=1;i=3024", "value_rank": -1},
                {"name": "Custom", "data_type": "i=24", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3027",
        "WGS84Coordinate",
        "ns=1;i=5046",
        {
            "structure_type": 0,
            "fields": [
                {"name": "N/S Hemisphere", "data_type": "i=12", "value_rank": -1},
                {"name": "Latitude", "data_type": "i=11", "value_rank": -1},
                {"name": "E/W Hemisphere", "data_type": "i=12", "value_rank": -1},
                {"name": "Longitude", "data_type": "i=11", "value_rank": -1},
                {"name": "Altitude", "data_type": "i=11", "value_rank": -1},
                {"name": "Timestamp", "data_type": "i=294", "value_rank": -1},
                {"name": "DilutionOfPrecision", "data_type": "i=11", "value_rank": -1},
                {"name": "UsefulPrecisionLatLon", "data_type": "i=6", "value_rank": -1},
                {"name": "UsefulPrecisionAlt", "data_type": "i=6", "value_rank": -1},
            ],
        },
    ),
]
_ENUMS: list = [
    (
        "ns=1;i=3013",
        "AutoIdOperationStatusEnumeration",
        {
            "fields": [
                {"name": "SUCCESS", "value": 0, "display_name": "SUCCESS"},
                {
                    "name": "MISC_ERROR_TOTAL",
                    "value": 1,
                    "display_name": "MISC_ERROR_TOTAL",
                },
                {
                    "name": "MISC_ERROR_PARTIAL",
                    "value": 2,
                    "display_name": "MISC_ERROR_PARTIAL",
                },
                {
                    "name": "PERMISSON_ERROR",
                    "value": 3,
                    "display_name": "PERMISSON_ERROR",
                },
                {
                    "name": "PASSWORD_ERROR",
                    "value": 4,
                    "display_name": "PASSWORD_ERROR",
                },
                {
                    "name": "REGION_NOT_FOUND_ERROR",
                    "value": 5,
                    "display_name": "REGION_NOT_FOUND_ERROR",
                },
                {
                    "name": "OP_NOT_POSSIBLE_ERROR",
                    "value": 6,
                    "display_name": "OP_NOT_POSSIBLE_ERROR",
                },
                {
                    "name": "OUT_OF_RANGE_ERROR",
                    "value": 7,
                    "display_name": "OUT_OF_RANGE_ERROR",
                },
                {"name": "NO_IDENTIFIER", "value": 8, "display_name": "NO_IDENTIFIER"},
                {
                    "name": "MULTIPLE_IDENTIFIERS",
                    "value": 9,
                    "display_name": "MULTIPLE_IDENTIFIERS",
                },
                {"name": "READ_ERROR", "value": 10, "display_name": "READ_ERROR"},
                {
                    "name": "DECODING_ERROR",
                    "value": 11,
                    "display_name": "DECODING_ERROR",
                },
                {"name": "MATCH_ERROR", "value": 12, "display_name": "MATCH_ERROR"},
                {
                    "name": "CODE_NOT_SUPPORTED",
                    "value": 13,
                    "display_name": "CODE_NOT_SUPPORTED",
                },
                {"name": "WRITE_ERROR", "value": 14, "display_name": "WRITE_ERROR"},
                {
                    "name": "NOT_SUPPORTED_BY_DEVICE",
                    "value": 15,
                    "display_name": "NOT_SUPPORTED_BY_DEVICE",
                },
                {
                    "name": "NOT_SUPPORTED_BY_TAG",
                    "value": 16,
                    "display_name": "NOT_SUPPORTED_BY_TAG",
                },
                {
                    "name": "DEVICE_NOT_READY",
                    "value": 17,
                    "display_name": "DEVICE_NOT_READY",
                },
                {
                    "name": "INVALID_CONFIGURATION",
                    "value": 18,
                    "display_name": "INVALID_CONFIGURATION",
                },
                {
                    "name": "RF_COMMUNICATION_ERROR",
                    "value": 19,
                    "display_name": "RF_COMMUNICATION_ERROR",
                },
                {"name": "DEVICE_FAULT", "value": 20, "display_name": "DEVICE_FAULT"},
                {
                    "name": "TAG_HAS_LOW_BATTERY",
                    "value": 21,
                    "display_name": "TAG_HAS_LOW_BATTERY",
                },
            ]
        },
    ),
    (
        "ns=1;i=3003",
        "DeviceStatusEnumeration",
        {
            "fields": [
                {"name": "Idle", "value": 0, "display_name": "Idle"},
                {"name": "Error", "value": 1, "display_name": "Error"},
                {"name": "Scanning", "value": 2, "display_name": "Scanning"},
                {"name": "Busy", "value": 3, "display_name": "Busy"},
            ]
        },
    ),
    (
        "ns=1;i=3009",
        "LocationTypeEnumeration",
        {
            "fields": [
                {"name": "NMEA", "value": 0, "display_name": "NMEA"},
                {"name": "LOCAL", "value": 1, "display_name": "LOCAL"},
                {"name": "WGS84", "value": 2, "display_name": "WGS84"},
                {"name": "NAME", "value": 3, "display_name": "NAME"},
            ]
        },
    ),
    (
        "ns=1;i=3016",
        "RfidLockOperationEnumeration",
        {
            "fields": [
                {"name": "Lock", "value": 0, "display_name": "Lock"},
                {"name": "Unlock", "value": 1, "display_name": "Unlock"},
                {"name": "PermanentLock", "value": 2, "display_name": "PermanentLock"},
                {
                    "name": "PermanentUnlock",
                    "value": 3,
                    "display_name": "PermanentUnlock",
                },
            ]
        },
    ),
    (
        "ns=1;i=3015",
        "RfidLockRegionEnumeration",
        {
            "fields": [
                {"name": "Kill", "value": 0, "display_name": "Kill"},
                {"name": "Access", "value": 1, "display_name": "Access"},
                {"name": "EPC", "value": 2, "display_name": "EPC"},
                {"name": "TID", "value": 3, "display_name": "TID"},
                {"name": "User", "value": 4, "display_name": "User"},
            ]
        },
    ),
    (
        "ns=1;i=3014",
        "RfidPasswordTypeEnumeration",
        {
            "fields": [
                {"name": "Access", "value": 0, "display_name": "Access"},
                {"name": "Kill", "value": 1, "display_name": "Kill"},
                {"name": "Read", "value": 2, "display_name": "Read"},
                {"name": "Write", "value": 3, "display_name": "Write"},
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = (
    [
        ("ns=1;i=3017", "ns=1;i=5022", ["i=12", "ns=1;i=3020", "i=294"]),
        (
            "ns=1;i=3018",
            "ns=1;i=5024",
            ["i=12", "ns=1;i=3020", "i=6", "i=6", "i=5", "i=12", "i=6"],
        ),
        ("ns=1;i=3011", "ns=1;i=5017", ["i=6", "i=12"]),
        (
            "ns=1;i=3023",
            "ns=1;i=5034",
            [
                "i=3",
                "i=4",
                "i=6",
                "i=3",
                "i=4",
                "i=6",
                "i=3",
                "i=3",
                "i=6",
                "i=4",
                "i=3",
            ],
        ),
        (
            "ns=1;i=3019",
            "ns=1;i=5028",
            ["i=11", "i=11", "i=11", "i=294", "i=11", "i=6"],
        ),
        ("ns=1;i=3004", "ns=1;i=5007", ["i=6", "i=6", "i=6", "i=6", "i=6"]),
        ("ns=1;i=3006", "ns=1;i=5009", ["i=6", "i=6", "i=294", "i=6"]),
        ("ns=1;i=3029", "ns=1;i=5050", ["i=11", "i=11", "i=11"]),
        ("ns=1;i=3024", "ns=1;i=5036", ["i=5", "i=15", "i=5", "i=5"]),
        ("ns=1;i=3001", "ns=1;i=5002", ["i=12", "ns=1;i=3020", "i=294", "ns=1;i=3008"]),
        ("ns=1;i=3002", "ns=1;i=5004", ["i=17", "i=3", "ns=1;i=3004", "i=12", "i=294"]),
        ("ns=1;i=3026", "ns=1;i=5040", ["i=10", "ns=1;i=3004", "i=12", "i=17"]),
        (
            "ns=1;i=3030",
            "ns=1;i=5052",
            ["i=12", "i=4", "i=4", "i=4", "i=4", "i=4", "i=4", "i=4", "i=4"],
        ),
        ("ns=1;i=3007", "ns=1;i=5011", ["ns=1;i=3006"]),
        ("ns=1;i=3028", "ns=1;i=5048", ["i=11", "i=11", "ns=1;i=3029", "i=294"]),
        ("ns=1;i=3010", "ns=1;i=5015", ["i=290", "i=6", "i=1", "ns=1;i=3009"]),
        ("ns=1;i=3008", "ns=1;i=5013", ["i=12", "ns=1;i=3019", "ns=1;i=3027", "i=12"]),
        ("ns=1;i=3020", "ns=1;i=5030", ["i=15", "i=12", "ns=1;i=3024", "i=24"]),
        (
            "ns=1;i=3027",
            "ns=1;i=5046",
            ["i=12", "i=11", "i=12", "i=11", "i=11", "i=294", "i=11", "i=6", "i=6"],
        ),
    ],
    [
        "ns=1;i=3013",
        "ns=1;i=3003",
        "ns=1;i=3009",
        "ns=1;i=3016",
        "ns=1;i=3015",
        "ns=1;i=3014",
    ],
)
_NODES: dict = {
    "datatypes": {
        "AccessResult": (
            "D",
            "ns=1;i=3017",
            {"RfidAccessResult": ("D", "ns=1;i=3018", {})},
        ),
        "AntennaNameIdPair": ("D", "ns=1;i=3011", {}),
        "AutoIdOperationStatusEnumeration": (
            "D",
            "ns=1;i=3013",
            {"EnumValues": ("V", "ns=1;i=6201", {})},
        ),
        "CodeTypeDataType": ("D", "ns=1;i=3031", {}),
        "DeviceStatusEnumeration": (
            "D",
            "ns=1;i=3003",
            {"EnumStrings": ("V", "ns=1;i=6029", {})},
        ),
        "DhcpGeoConfCoordinate": ("D", "ns=1;i=3023", {}),
        "LocalCoordinate": ("D", "ns=1;i=3019", {}),
        "Location": ("D", "ns=1;i=3008", {}),
        "LocationName": ("D", "ns=1;i=3021", {}),
        "LocationTypeEnumeration": (
            "D",
            "ns=1;i=3009",
            {"EnumStrings": ("V", "ns=1;i=6040", {})},
        ),
        "NmeaCoordinateString": ("D", "ns=1;i=3012", {}),
        "Position": ("D", "ns=1;i=3004", {}),
        "RfidLockOperationEnumeration": (
            "D",
            "ns=1;i=3016",
            {"EnumStrings": ("V", "ns=1;i=6067", {})},
        ),
        "RfidLockRegionEnumeration": (
            "D",
            "ns=1;i=3015",
            {"EnumStrings": ("V", "ns=1;i=6066", {})},
        ),
        "RfidPasswordTypeEnumeration": (
            "D",
            "ns=1;i=3014",
            {"EnumStrings": ("V", "ns=1;i=6061", {})},
        ),
        "RfidSighting": ("D", "ns=1;i=3006", {}),
        "Rotation": ("D", "ns=1;i=3029", {}),
        "ScanData": ("D", "ns=1;i=3020", {}),
        "ScanDataEpc": ("D", "ns=1;i=3024", {}),
        "ScanResult": (
            "D",
            "ns=1;i=3001",
            {
                "OcrScanResult": ("D", "ns=1;i=3002", {}),
                "OpticalScanResult": (
                    "D",
                    "ns=1;i=3026",
                    {"OpticalVerifierScanResult": ("D", "ns=1;i=3030", {})},
                ),
                "RfidScanResult": ("D", "ns=1;i=3007", {}),
                "RtlsLocationResult": ("D", "ns=1;i=3028", {}),
            },
        ),
        "ScanSettings": ("D", "ns=1;i=3010", {}),
        "WGS84Coordinate": ("D", "ns=1;i=3027", {}),
    },
    "eventtypes": {
        "AutoIdDiagnosticsEventType": (
            "OT",
            "ns=1;i=1010",
            {
                "AutoIdAccessEventType": (
                    "OT",
                    "ns=1;i=1015",
                    {
                        "AccessResult": ("V", "ns=1;i=6091", {}),
                        "Client": ("V", "ns=1;i=6092", {}),
                        "Command": ("V", "ns=1;i=6093", {}),
                        "RfidAccessEventType": (
                            "OT",
                            "ns=1;i=1016",
                            {"AccessResult": ("V", "ns=1;i=6094", {})},
                        ),
                    },
                ),
                "AutoIdLogEntryEventType": ("OT", "ns=1;i=1017", {}),
                "AutoIdPresenceEventType": (
                    "OT",
                    "ns=1;i=1018",
                    {"Presence": ("V", "ns=1;i=6095", {})},
                ),
                "DeviceName": ("V", "ns=1;i=6090", {}),
            },
        ),
        "AutoIdScanEventType": (
            "OT",
            "ns=1;i=1004",
            {
                "DeviceName": ("V", "ns=1;i=6049", {}),
                "OcrScanEventType": (
                    "OT",
                    "ns=1;i=1005",
                    {"ScanResult": ("V", "ns=1;i=6041", {})},
                ),
                "OpticalScanEventType": (
                    "OT",
                    "ns=1;i=1009",
                    {
                        "OpticalVerifierScanEventType": (
                            "OT",
                            "ns=1;i=1013",
                            {"ScanResult": ("V", "ns=1;i=6227", {})},
                        ),
                        "ScanResult": ("V", "ns=1;i=6147", {}),
                    },
                ),
                "RfidScanEventType": (
                    "OT",
                    "ns=1;i=1006",
                    {"ScanResult": ("V", "ns=1;i=6042", {})},
                ),
                "RtlsLocationEventType": (
                    "OT",
                    "ns=1;i=1014",
                    {"ScanResult": ("V", "ns=1;i=6228", {})},
                ),
                "ScanResult": ("V", "ns=1;i=6024", {}),
            },
        ),
    },
    "objects": {
        "AutoID": (
            "V",
            "ns=1;i=6018",
            {
                "AccessResult": ("V", "ns=1;i=6087", {}),
                "AntennaNameIdPair": ("V", "ns=1;i=6047", {}),
                "DhcpGeoConfCoordinate": ("V", "ns=1;i=6190", {}),
                "LocalCoordinate": ("V", "ns=1;i=6123", {}),
                "Location": ("V", "ns=1;i=6036", {}),
                "NamespaceUri": ("V", "ns=1;i=6019", {}),
                "OcrScanResult": ("V", "ns=1;i=6023", {}),
                "OpticalScanResult": ("V", "ns=1;i=6143", {}),
                "OpticalVerifierScanResult": ("V", "ns=1;i=6230", {}),
                "Position": ("V", "ns=1;i=6033", {}),
                "RfidAccessResult": ("V", "ns=1;i=6089", {}),
                "RfidScanResult": ("V", "ns=1;i=6038", {}),
                "RfidSighting": ("V", "ns=1;i=6035", {}),
                "Rotation": ("V", "ns=1;i=6223", {}),
                "RtlsLocationResult": ("V", "ns=1;i=6221", {}),
                "ScanData": ("V", "ns=1;i=6132", {}),
                "ScanDataEpc": ("V", "ns=1;i=6139", {}),
                "ScanResult": ("V", "ns=1;i=6021", {}),
                "ScanSettings": ("V", "ns=1;i=6045", {}),
                "WGS84Coordinate": ("V", "ns=1;i=6213", {}),
            },
        ),
        "Default Binary": ("O", "ns=1;i=5052", {}),
        "Default XML": ("O", "ns=1;i=5053", {}),
        "http://opcfoundation.org/UA/AutoID/": (
            "O",
            "ns=1;i=5019",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=6028", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=6039", {}),
                "NamespaceUri": ("V", "ns=1;i=6053", {}),
                "NamespaceVersion": ("V", "ns=1;i=6068", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=6069", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=6070", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=6071", {}),
            },
        ),
    },
    "objtypes": {
        "AutoIdDeviceType": (
            "OT",
            "ns=1;i=1001",
            {
                "AutoIdModelVersion": ("V", "ns=1;i=6193", {}),
                "DeviceInfo": ("V", "ns=1;i=6026", {}),
                "DeviceLocation": ("V", "ns=1;i=6128", {}),
                "DeviceLocationName": ("V", "ns=1;i=6127", {}),
                "DeviceName": ("V", "ns=1;i=6124", {}),
                "DeviceStatus": ("V", "ns=1;i=6030", {}),
                "Diagnostics": (
                    "O",
                    "ns=1;i=5026",
                    {
                        "LastAccess": (
                            "O",
                            "ns=1;i=5027",
                            {
                                "Client": ("V", "ns=1;i=6103", {}),
                                "Command": ("V", "ns=1;i=6104", {}),
                                "Identifier": ("V", "ns=1;i=6105", {}),
                                "Timestamp": ("V", "ns=1;i=6106", {}),
                            },
                        ),
                        "Logbook": (
                            "O",
                            "ns=1;i=5032",
                            {
                                "LastLogEntry": ("V", "ns=1;i=6102", {}),
                                "LogColumns": ("V", "ns=1;i=6101", {}),
                            },
                        ),
                        "Presence": ("V", "ns=1;i=6100", {}),
                    },
                ),
                "GetDeviceLocation": (
                    "M",
                    "ns=1;i=7042",
                    {
                        "InputArguments": ("V", "ns=1;i=6130", {}),
                        "OutputArguments": ("V", "ns=1;i=6129", {}),
                    },
                ),
                "IOData": ("O", "ns=1;i=5054", {}),
                "LastScanData": ("V", "ns=1;i=6055", {}),
                "LastScanTimestamp": ("V", "ns=1;i=6096", {}),
                "OcrReaderDeviceType": (
                    "OT",
                    "ns=1;i=1002",
                    {
                        "Images": (
                            "O",
                            "ns=1;i=5006",
                            {
                                "<ImageName>": (
                                    "O",
                                    "ns=1;i=5021",
                                    {
                                        "Close": (
                                            "M",
                                            "ns=1;i=7011",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=6072",
                                                    {},
                                                )
                                            },
                                        ),
                                        "GetPosition": (
                                            "M",
                                            "ns=1;i=7012",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=6073",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=6074",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Open": (
                                            "M",
                                            "ns=1;i=7019",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=6075",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=6077",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "OpenCount": ("V", "ns=1;i=6078", {}),
                                        "Read": (
                                            "M",
                                            "ns=1;i=7020",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=6079",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=6080",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "SetPosition": (
                                            "M",
                                            "ns=1;i=7021",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=6081",
                                                    {},
                                                )
                                            },
                                        ),
                                        "Size": ("V", "ns=1;i=6082", {}),
                                        "UserWritable": ("V", "ns=1;i=6083", {}),
                                        "Writable": ("V", "ns=1;i=6084", {}),
                                        "Write": (
                                            "M",
                                            "ns=1;i=7022",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=6085",
                                                    {},
                                                )
                                            },
                                        ),
                                    },
                                )
                            },
                        ),
                        "RuntimeParameters": (
                            "O",
                            "ns=1;i=5043",
                            {
                                "MatchCode": ("V", "ns=1;i=6134", {}),
                                "TemplateName": ("V", "ns=1;i=6133", {}),
                            },
                        ),
                        "Scan": (
                            "M",
                            "ns=1;i=7001",
                            {
                                "InputArguments": ("V", "ns=1;i=6027", {}),
                                "OutputArguments": ("V", "ns=1;i=6015", {}),
                            },
                        ),
                    },
                ),
                "OpticalReaderDeviceType": (
                    "OT",
                    "ns=1;i=1008",
                    {
                        "Images": (
                            "O",
                            "ns=1;i=5001",
                            {
                                "<ImageName>": (
                                    "O",
                                    "ns=1;i=5020",
                                    {
                                        "Close": (
                                            "M",
                                            "ns=1;i=7002",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=6002",
                                                    {},
                                                )
                                            },
                                        ),
                                        "GetPosition": (
                                            "M",
                                            "ns=1;i=7003",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=6003",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=6004",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Open": (
                                            "M",
                                            "ns=1;i=7004",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=6005",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=6006",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "OpenCount": ("V", "ns=1;i=6007", {}),
                                        "Read": (
                                            "M",
                                            "ns=1;i=7005",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=6008",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=6009",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "SetPosition": (
                                            "M",
                                            "ns=1;i=7006",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=6010",
                                                    {},
                                                )
                                            },
                                        ),
                                        "Size": ("V", "ns=1;i=6011", {}),
                                        "UserWritable": ("V", "ns=1;i=6012", {}),
                                        "Writable": ("V", "ns=1;i=6013", {}),
                                        "Write": (
                                            "M",
                                            "ns=1;i=7007",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=6014",
                                                    {},
                                                )
                                            },
                                        ),
                                    },
                                )
                            },
                        ),
                        "OpticalVerifierDeviceType": (
                            "OT",
                            "ns=1;i=1011",
                            {
                                "Scan": (
                                    "M",
                                    "ns=1;i=7054",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6031", {}),
                                        "OutputArguments": ("V", "ns=1;i=6076", {}),
                                    },
                                )
                            },
                        ),
                        "RuntimeParameters": (
                            "O",
                            "ns=1;i=5045",
                            {
                                "MatchCode": ("V", "ns=1;i=6136", {}),
                                "TemplateName": ("V", "ns=1;i=6135", {}),
                            },
                        ),
                        "Scan": (
                            "M",
                            "ns=1;i=7043",
                            {
                                "InputArguments": ("V", "ns=1;i=6144", {}),
                                "OutputArguments": ("V", "ns=1;i=6145", {}),
                            },
                        ),
                    },
                ),
                "RfidReaderDeviceType": (
                    "OT",
                    "ns=1;i=1003",
                    {
                        "AntennaNames": ("V", "ns=1;i=6048", {}),
                        "Diagnostics": (
                            "O",
                            "ns=1;i=5038",
                            {
                                "LastAccess": (
                                    "O",
                                    "ns=1;i=5039",
                                    {
                                        "Antenna": ("V", "ns=1;i=6114", {}),
                                        "CurrentPowerLevel": ("V", "ns=1;i=6115", {}),
                                        "PC": ("V", "ns=1;i=6116", {}),
                                        "Polarization": ("V", "ns=1;i=6117", {}),
                                        "RWData": ("V", "ns=1;i=6113", {}),
                                        "Strength": ("V", "ns=1;i=6118", {}),
                                    },
                                )
                            },
                        ),
                        "KillTag": (
                            "M",
                            "ns=1;i=7017",
                            {
                                "InputArguments": ("V", "ns=1;i=6062", {}),
                                "OutputArguments": ("V", "ns=1;i=6063", {}),
                            },
                        ),
                        "LastScanAntenna": ("V", "ns=1;i=6097", {}),
                        "LastScanRSSI": ("V", "ns=1;i=6098", {}),
                        "LockTag": (
                            "M",
                            "ns=1;i=7018",
                            {
                                "InputArguments": ("V", "ns=1;i=6064", {}),
                                "OutputArguments": ("V", "ns=1;i=6065", {}),
                            },
                        ),
                        "ReadTag": (
                            "M",
                            "ns=1;i=7014",
                            {
                                "InputArguments": ("V", "ns=1;i=6054", {}),
                                "OutputArguments": ("V", "ns=1;i=6056", {}),
                            },
                        ),
                        "RuntimeParameters": (
                            "O",
                            "ns=1;i=5042",
                            {
                                "CodeTypesRWData": (
                                    "V",
                                    "ns=1;i=6119",
                                    {"EnumStrings": ("V", "ns=1;i=6120", {})},
                                ),
                                "EnableAntennas": ("V", "ns=1;i=6126", {}),
                                "MinRssi": ("V", "ns=1;i=6146", {}),
                                "RfPower": ("V", "ns=1;i=6141", {}),
                                "TagTypes": (
                                    "V",
                                    "ns=1;i=6121",
                                    {"EnumStrings": ("V", "ns=1;i=6125", {})},
                                ),
                            },
                        ),
                        "Scan": (
                            "M",
                            "ns=1;i=7013",
                            {
                                "InputArguments": ("V", "ns=1;i=6052", {}),
                                "OutputArguments": ("V", "ns=1;i=6043", {}),
                            },
                        ),
                        "SetTagPassword": (
                            "M",
                            "ns=1;i=7016",
                            {
                                "InputArguments": ("V", "ns=1;i=6059", {}),
                                "OutputArguments": ("V", "ns=1;i=6060", {}),
                            },
                        ),
                        "WriteTag": (
                            "M",
                            "ns=1;i=7015",
                            {
                                "InputArguments": ("V", "ns=1;i=6057", {}),
                                "OutputArguments": ("V", "ns=1;i=6058", {}),
                            },
                        ),
                        "WriteTagID": (
                            "M",
                            "ns=1;i=7023",
                            {
                                "InputArguments": ("V", "ns=1;i=6137", {}),
                                "OutputArguments": ("V", "ns=1;i=6140", {}),
                            },
                        ),
                    },
                ),
                "RtlsDeviceType": (
                    "OT",
                    "ns=1;i=1012",
                    {
                        "GeographicalUnit": ("V", "ns=1;i=6214", {}),
                        "GetLocation": (
                            "M",
                            "ns=1;i=7056",
                            {
                                "InputArguments": ("V", "ns=1;i=6224", {}),
                                "OutputArguments": ("V", "ns=1;i=6225", {}),
                            },
                        ),
                        "GetSupportedLocationTypes": (
                            "M",
                            "ns=1;i=7058",
                            {"OutputArguments": ("V", "ns=1;i=6226", {})},
                        ),
                        "GetUnits": ("M", "ns=1;i=7057", {}),
                        "LengthUnit": ("V", "ns=1;i=6217", {}),
                        "RotationalUnit": ("V", "ns=1;i=6216", {}),
                        "Scan": (
                            "M",
                            "ns=1;i=7055",
                            {
                                "InputArguments": ("V", "ns=1;i=6218", {}),
                                "OutputArguments": ("V", "ns=1;i=6219", {}),
                            },
                        ),
                        "SpeedUnit": ("V", "ns=1;i=6215", {}),
                    },
                ),
                "RuntimeParameters": (
                    "O",
                    "ns=1;i=5044",
                    {
                        "CodeTypes": (
                            "V",
                            "ns=1;i=6107",
                            {"EnumStrings": ("V", "ns=1;i=6108", {})},
                        ),
                        "ScanSettings": (
                            "O",
                            "ns=1;i=5033",
                            {
                                "CodeType": ("V", "ns=1;i=6109", {}),
                                "Cycles": ("V", "ns=1;i=6111", {}),
                                "DataAvailable": ("V", "ns=1;i=6110", {}),
                                "Duration": ("V", "ns=1;i=6112", {}),
                            },
                        ),
                    },
                ),
                "Scan": (
                    "M",
                    "ns=1;i=7008",
                    {
                        "InputArguments": ("V", "ns=1;i=6050", {}),
                        "OutputArguments": ("V", "ns=1;i=6001", {}),
                    },
                ),
                "ScanActive": ("V", "ns=1;i=6099", {}),
                "ScanStart": (
                    "M",
                    "ns=1;i=7009",
                    {
                        "InputArguments": ("V", "ns=1;i=6051", {}),
                        "OutputArguments": ("V", "ns=1;i=6208", {}),
                    },
                ),
                "ScanStop": ("M", "ns=1;i=7010", {}),
            },
        )
    },
    "vartypes": {
        "LocationVariableType": (
            "VT",
            "ns=1;i=2002",
            {
                "GeographicalUnit": ("V", "ns=1;i=6199", {}),
                "LengthUnit": ("V", "ns=1;i=6197", {}),
                "RotationalUnit": ("V", "ns=1;i=6198", {}),
                "SpeedUnit": ("V", "ns=1;i=6200", {}),
            },
        )
    },
}
