# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 79a2b2c4425d9ead9377dbe3e14b0f2b8a99c82d4af4d549f5236025e42c794d
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/CranesHoists/"
_VERSION: str = "1.00"
_REQUIRED: list = [
    {"uri": "http://opcfoundation.org/UA/", "version": "1.05.01"},
    {"uri": "http://opcfoundation.org/UA/DI/", "version": "1.03.1"},
    {"uri": "http://opcfoundation.org/UA/Machinery/", "version": "1.02.0"},
    {"uri": "http://opcfoundation.org/UA/Robotics/", "version": "1.0.0"},
]
_STRUCTURES: list = []
_ENUMS: list = [
    (
        "ns=4;i=3000",
        "CraneOperationalModeEnum",
        {
            "fields": [
                {"name": "OTHER", "value": 0, "display_name": "OTHER"},
                {"name": "MANUAL", "value": 1, "display_name": "MANUAL"},
                {"name": "SEMIAUTOMATIC", "value": 2, "display_name": "SEMIAUTOMATIC"},
                {"name": "FULLAUTOMATIC", "value": 3, "display_name": "FULLAUTOMATIC"},
                {"name": "BYPASS_ON", "value": 4, "display_name": "BYPASS_ON"},
                {"name": "MAINTENANCE", "value": 5, "display_name": "MAINTENANCE"},
            ]
        },
    ),
    (
        "ns=4;i=3001",
        "ExternalControlRequestEnum",
        {
            "fields": [
                {"name": "NOT_REQUESTED", "value": 0, "display_name": "NOT_REQUESTED"},
                {
                    "name": "REQUESTED_AND_CONTROL_ACTIVE",
                    "value": 1,
                    "display_name": "REQUESTED_AND_CONTROL_ACTIVE",
                },
                {
                    "name": "REQUESTED_AND_CONTROL_INACTIVE",
                    "value": 2,
                    "display_name": "REQUESTED_AND_CONTROL_INACTIVE",
                },
                {
                    "name": "REQUESTED_AND_CONTROL_BYPASSED",
                    "value": 3,
                    "display_name": "REQUESTED_AND_CONTROL_BYPASSED",
                },
            ]
        },
    ),
    (
        "ns=4;i=3002",
        "ProtectiveFunctionEnum",
        {
            "fields": [
                {"name": "OTHER", "value": 0, "display_name": "OTHER"},
                {"name": "FORCE_LIMITER", "value": 1, "display_name": "FORCE_LIMITER"},
                {
                    "name": "OVERSPEED_CONTROL",
                    "value": 2,
                    "display_name": "OVERSPEED_CONTROL",
                },
                {
                    "name": "MOTION_LIMITER",
                    "value": 3,
                    "display_name": "MOTION_LIMITER",
                },
                {"name": "ANTICOLLISION", "value": 4, "display_name": "ANTICOLLISION"},
            ]
        },
    ),
    (
        "ns=4;i=3003",
        "CraneMotionDeviceCategoryEnum",
        {
            "fields": [
                {"name": "HOIST", "value": 0, "display_name": "HOIST"},
                {
                    "name": "TROLLEY_TRAVERSE",
                    "value": 1,
                    "display_name": "TROLLEY_TRAVERSE",
                },
                {
                    "name": "BRIDGE_OR_GANTRY_TRAVEL",
                    "value": 2,
                    "display_name": "BRIDGE_OR_GANTRY_TRAVEL",
                },
                {
                    "name": "LOAD_LIFTING_ATTACHMENT",
                    "value": 3,
                    "display_name": "LOAD_LIFTING_ATTACHMENT",
                },
                {
                    "name": "ROTATING_OR_SLEWING",
                    "value": 4,
                    "display_name": "ROTATING_OR_SLEWING",
                },
                {"name": "LUFFING", "value": 5, "display_name": "LUFFING"},
                {
                    "name": "POWER_SUPPLY_MACHINERY",
                    "value": 6,
                    "display_name": "POWER_SUPPLY_MACHINERY",
                },
                {"name": "OTHER", "value": 7, "display_name": "OTHER"},
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = (
    [],
    ["ns=4;i=3000", "ns=4;i=3001", "ns=4;i=3002", "ns=4;i=3003"],
)
_NODES: dict = {
    "datatypes": {
        "CraneMotionDeviceCategoryEnum": (
            "D",
            "ns=4;i=3003",
            {"EnumValues": ("V", "ns=4;i=6003", {})},
        ),
        "CraneOperationalModeEnum": (
            "D",
            "ns=4;i=3000",
            {"EnumValues": ("V", "ns=4;i=6001", {})},
        ),
        "ExternalControlRequestEnum": (
            "D",
            "ns=4;i=3001",
            {"EnumValues": ("V", "ns=4;i=6013", {})},
        ),
        "ProtectiveFunctionEnum": (
            "D",
            "ns=4;i=3002",
            {"EnumValues": ("V", "ns=4;i=6014", {})},
        ),
    },
    "objects": {
        "<CraneMotionDeviceIdentifier>": ("O", "ns=4;i=1263", {}),
        "Components": (
            "O",
            "ns=4;i=5016",
            {"<CraneMotorIdentifier>": ("O", "ns=4;i=5022", {})},
        ),
        "Identification": ("O", "ns=4;i=5024", {}),
        "http://opcfoundation.org/UA/CranesHoists/": (
            "O",
            "ns=4;i=1000",
            {
                "DefaultRolePermissions": ("V", "ns=4;i=1008", {}),
                "IsNamespaceSubset": ("V", "ns=4;i=1001", {}),
                "NamespacePublicationDate": ("V", "ns=4;i=1002", {}),
                "NamespaceUri": ("V", "ns=4;i=1003", {}),
                "NamespaceVersion": ("V", "ns=4;i=1004", {}),
                "StaticNodeIdTypes": ("V", "ns=4;i=1005", {}),
                "StaticNumericNodeIdRange": ("V", "ns=4;i=1006", {}),
                "StaticStringNodeIdPattern": ("V", "ns=4;i=1007", {}),
            },
        ),
    },
    "objtypes": {
        "BrakeType": (
            "OT",
            "ns=4;i=1556",
            {
                "Operational": ("O", "ns=4;i=5009", {}),
                "ParameterSet": (
                    "O",
                    "ns=4;i=5020",
                    {"BrakeReleased": ("V", "ns=4;i=6005", {})},
                ),
            },
        ),
        "CraneAxisType": (
            "OT",
            "ns=4;i=1369",
            {
                "<BackupBrakeIdentifier>": ("O", "ns=4;i=1373", {}),
                "ActualLoad": ("O", "ns=4;i=1378", {}),
                "Configuration": (
                    "O",
                    "ns=4;i=5007",
                    {
                        "SpeedLimitDirMinusSetpoint": ("V", "ns=4;i=1486", {}),
                        "SpeedLimitDirPlusSetpoint": ("V", "ns=4;i=1485", {}),
                        "SpeedLimitEnabledDirMinus": ("V", "ns=4;i=1845", {}),
                        "SpeedLimitEnabledDirPlus": ("V", "ns=4;i=1511", {}),
                    },
                ),
                "Operational": (
                    "O",
                    "ns=4;i=5003",
                    {
                        "CraneAxisFunction": (
                            "V",
                            "ns=4;i=2416",
                            {
                                "EnumValues": ("V", "ns=4;i=6016", {}),
                                "ValueAsText": ("V", "ns=4;i=6017", {}),
                            },
                        ),
                        "IsMoving": ("V", "ns=4;i=2037", {}),
                        "RatedSpeed": ("V", "ns=4;i=1852", {}),
                        "SpeedLimitDirMinus": ("V", "ns=4;i=2031", {}),
                        "SpeedLimitDirPlus": ("V", "ns=4;i=1950", {}),
                    },
                ),
                "ParameterSet": (
                    "O",
                    "ns=4;i=2093",
                    {"ActualPositionCapability": ("V", "ns=4;i=2096", {})},
                ),
            },
        ),
        "CraneMotionDeviceSystemType": (
            "OT",
            "ns=4;i=2112",
            {
                "Configuration": (
                    "O",
                    "ns=4;i=5011",
                    {"SpeedLimitGlobalEnabled": ("V", "ns=4;i=2381", {})},
                ),
                "Manufacturer": ("V", "ns=4;i=6007", {}),
                "Operational": (
                    "O",
                    "ns=4;i=5012",
                    {
                        "CraneOperationalMode": ("V", "ns=4;i=2348", {}),
                        "ExternalControlRequest": ("V", "ns=4;i=2369", {}),
                        "SystemOn": ("V", "ns=4;i=2347", {}),
                    },
                ),
                "ParameterSet": ("O", "ns=4;i=2114", {}),
                "ProductInstanceUri": ("V", "ns=4;i=6011", {}),
                "ProtectiveFunctions": (
                    "O",
                    "ns=4;i=2113",
                    {"<ProtectiveFunctionIdentifier>": ("O", "ns=4;i=5025", {})},
                ),
                "SerialNumber": ("V", "ns=4;i=6008", {}),
            },
        ),
        "CraneMotionDeviceType": (
            "OT",
            "ns=4;i=1392",
            {
                "Axes": (
                    "O",
                    "ns=4;i=5010",
                    {"<AxisIdentifier>": ("O", "ns=4;i=5001", {})},
                ),
                "CraneMotionDeviceCategory": ("V", "ns=4;i=6004", {}),
                "Manufacturer": ("V", "ns=4;i=6009", {}),
                "Operational": ("O", "ns=4;i=5014", {}),
                "ParameterSet": (
                    "O",
                    "ns=4;i=5017",
                    {"DesignedWorkingPeriod": ("V", "ns=4;i=6002", {})},
                ),
                "ProductInstanceUri": ("V", "ns=4;i=6012", {}),
                "SerialNumber": ("V", "ns=4;i=6010", {}),
            },
        ),
        "CraneMotorType": (
            "OT",
            "ns=4;i=1262",
            {
                "Operational": ("O", "ns=4;i=5019", {}),
                "ParameterSet": (
                    "O",
                    "ns=4;i=5018",
                    {"Overheated": ("V", "ns=4;i=6000", {})},
                ),
            },
        ),
        "ProtectiveFunctionType": (
            "OT",
            "ns=4;i=1462",
            {
                "Name": ("V", "ns=4;i=1479", {}),
                "Operational": ("O", "ns=4;i=5013", {}),
                "ParameterSet": (
                    "O",
                    "ns=4;i=5004",
                    {
                        "Active": ("V", "ns=4;i=1463", {}),
                        "DirMinusSlowdown": ("V", "ns=4;i=2375", {}),
                        "DirMinusStop": ("V", "ns=4;i=1861", {}),
                        "DirPlusSlowdown": ("V", "ns=4;i=2379", {}),
                        "DirPlusStop": ("V", "ns=4;i=1860", {}),
                        "Enabled": ("V", "ns=4;i=1478", {}),
                    },
                ),
                "ProtectiveFunctionMode": ("V", "ns=4;i=1864", {}),
                "RampDown": ("V", "ns=4;i=1472", {}),
            },
        ),
    },
    "reftypes": {"ProtectsAxis": ("RT", "ns=4;i=4001", {})},
}
