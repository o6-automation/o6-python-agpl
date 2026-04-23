# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 3f84f3ba23b2ded393919f079fd566d8ba5834b6b1dacd342a65a3201e0dd600
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/Weihenstephan/"
_VERSION: str = "1.00.0"
_REQUIRED: list = [
    {"uri": "http://opcfoundation.org/UA/", "version": "1.04.7"},
    {"uri": "http://opcfoundation.org/UA/DI/", "version": "1.02.2"},
    {"uri": "http://opcfoundation.org/UA/Machinery/", "version": "1.0.0"},
    {"uri": "http://opcfoundation.org/UA/PackML/", "version": "1.01"},
]
_STRUCTURES: list = []
_ENUMS: list = [
    (
        "ns=4;i=3000",
        "WSOperatingModeEnumerationType",
        {
            "fields": [
                {"name": "Off", "value": 1, "display_name": "Off"},
                {"name": "Manual", "value": 2, "display_name": "Manual"},
                {
                    "name": "Semi-automatic",
                    "value": 4,
                    "display_name": "Semi-automatic",
                },
                {"name": "Automatic", "value": 8, "display_name": "Automatic"},
            ]
        },
    ),
    (
        "ns=4;i=3001",
        "WSProgramEnumerationType",
        {
            "fields": [
                {
                    "name": "Undefined (No Program)",
                    "value": 0,
                    "display_name": "Undefined (No Program)",
                },
                {"name": "Production", "value": 1, "display_name": "Production"},
                {"name": "Start Up", "value": 2, "display_name": "Start Up"},
                {"name": "Run Down", "value": 4, "display_name": "Run Down"},
                {"name": "Clean", "value": 8, "display_name": "Clean"},
                {"name": "Changeover", "value": 16, "display_name": "Changeover"},
                {"name": "Maintenance", "value": 32, "display_name": "Maintenance"},
                {"name": "Break", "value": 64, "display_name": "Break"},
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = ([], ["ns=4;i=3000", "ns=4;i=3001"])
_NODES: dict = {
    "datatypes": {
        "WSOperatingModeEnumerationType": (
            "D",
            "ns=4;i=3000",
            {"EnumValues": ("V", "ns=4;i=6021", {})},
        ),
        "WSProgramEnumerationType": (
            "D",
            "ns=4;i=3001",
            {"EnumValues": ("V", "ns=4;i=6026", {})},
        ),
    },
    "objects": {
        "Identification": (
            "O",
            "ns=4;i=5001",
            {
                "Manufacturer": ("V", "ns=4;i=6014", {}),
                "ProductInstanceUri": ("V", "ns=4;i=6013", {}),
                "SerialNumber": ("V", "ns=4;i=6012", {}),
            },
        ),
        "http://opcfoundation.org/UA/Weihenstephan/": (
            "O",
            "ns=4;i=5000",
            {
                "IsNamespaceSubset": ("V", "ns=4;i=6000", {}),
                "NamespacePublicationDate": ("V", "ns=4;i=6001", {}),
                "NamespaceUri": ("V", "ns=4;i=6002", {}),
                "NamespaceVersion": ("V", "ns=4;i=6003", {}),
                "StaticNodeIdTypes": ("V", "ns=4;i=6004", {}),
                "StaticNumericNodeIdRange": ("V", "ns=4;i=6005", {}),
                "StaticStringNodeIdPattern": ("V", "ns=4;i=6006", {}),
            },
        ),
    },
    "objtypes": {
        "WSBaseObjectType": (
            "OT",
            "ns=4;i=1001",
            {
                "WSAlarmType": (
                    "OT",
                    "ns=4;i=1002",
                    {
                        "WSAlarmCode": ("V", "ns=4;i=6016", {}),
                        "WSAlarmMessage": ("V", "ns=4;i=6017", {}),
                    },
                ),
                "WSTagNumber": ("V", "ns=4;i=6015", {}),
                "WSWarningType": (
                    "OT",
                    "ns=4;i=1003",
                    {
                        "WSWarningCode": ("V", "ns=4;i=6018", {}),
                        "WSWarningMessage": ("V", "ns=4;i=6019", {}),
                    },
                ),
            },
        ),
        "WSBaseStateMachineType": (
            "OT",
            "ns=4;i=1004",
            {"WSTagNumber": ("V", "ns=4;i=6020", {})},
        ),
        "WSExecuteStateMachineType": (
            "OT",
            "ns=4;i=1005",
            {
                "Held": ("O", "ns=4;i=5028", {}),
                "HeldState": ("O", "ns=4;i=5026", {}),
                "Suspended": ("O", "ns=4;i=5029", {}),
                "SuspendedState": ("O", "ns=4;i=5027", {}),
            },
        ),
        "WSHeldStateMachineType": (
            "OT",
            "ns=4;i=1006",
            {
                "EquipmentFailure": ("O", "ns=4;i=5012", {}),
                "ExternalFailure": ("O", "ns=4;i=5014", {}),
            },
        ),
        "WSMachineType": (
            "OT",
            "ns=4;i=1000",
            {
                "Alarms": ("O", "ns=4;i=5008", {}),
                "BatchAndArticleTracing": ("O", "ns=4;i=5004", {}),
                "ComputedValues": ("O", "ns=4;i=5002", {}),
                "Counters": ("O", "ns=4;i=5003", {}),
                "MeasuredValues": ("O", "ns=4;i=5009", {}),
                "OperatingModes": ("O", "ns=4;i=5005", {}),
                "OperatingStates": ("O", "ns=4;i=5006", {}),
                "Parameters": ("O", "ns=4;i=5010", {}),
                "Programs": ("O", "ns=4;i=5007", {}),
                "WSMachineProfile": ("V", "ns=4;i=6008", {}),
                "WSVersion": ("V", "ns=4;i=6009", {}),
                "WSVersionProject": ("V", "ns=4;i=6011", {}),
                "WSVersionVendor": ("V", "ns=4;i=6010", {}),
                "Warnings": ("O", "ns=4;i=5011", {}),
            },
        ),
        "WSSuspendedStateMachineType": (
            "OT",
            "ns=4;i=1007",
            {
                "Lack": ("O", "ns=4;i=5016", {}),
                "LackBranchLine": ("O", "ns=4;i=5018", {}),
                "Prepared": ("O", "ns=4;i=5020", {}),
                "Tailback": ("O", "ns=4;i=5022", {}),
                "TailbackBranchLine": ("O", "ns=4;i=5024", {}),
            },
        ),
    },
    "vartypes": {
        "WSAnalogUnitType": (
            "VT",
            "ns=4;i=2000",
            {"WSTagNumber": ("V", "ns=4;i=6027", {})},
        ),
        "WSBaseDataVariableType": (
            "VT",
            "ns=4;i=2001",
            {"WSTagNumber": ("V", "ns=4;i=6022", {})},
        ),
    },
}
