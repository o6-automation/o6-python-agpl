# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 83ab75fe035b71949d808a49c566ae4e6ec23d460e873814c97be671f87a2e12
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/PNEM/"
_VERSION: str = "1.0.0"
_REQUIRED: list = [
    {"uri": "http://opcfoundation.org/UA/", "version": "1.04.7"},
    {"uri": "http://opcfoundation.org/UA/DI/", "version": "1.02.2"},
]
_STRUCTURES: list = [
    (
        "ns=1;i=3005",
        "AcPeDataType",
        "ns=1;i=5010",
        {
            "structure_type": 0,
            "fields": [
                {"name": "A", "data_type": "i=10", "value_rank": -1},
                {"name": "B", "data_type": "i=10", "value_rank": -1},
                {"name": "C", "data_type": "i=10", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3006",
        "AcPpDataType",
        "ns=1;i=5013",
        {
            "structure_type": 0,
            "fields": [
                {"name": "A_b", "data_type": "i=10", "value_rank": -1},
                {"name": "B_c", "data_type": "i=10", "value_rank": -1},
                {"name": "C_a", "data_type": "i=10", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3003",
        "EnergyStateInformationDataType",
        "ns=1;i=5004",
        {
            "structure_type": 0,
            "fields": [
                {"name": "IDSource", "data_type": "i=3", "value_rank": -1},
                {"name": "IDDestination", "data_type": "i=3", "value_rank": -1},
                {
                    "name": "RegularTimeToOperate",
                    "data_type": "i=290",
                    "value_rank": -1,
                },
                {"name": "ModePowerConsumption", "data_type": "i=10", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3004",
        "PeVersionDataType",
        "ns=1;i=5007",
        {
            "structure_type": 0,
            "fields": [
                {"name": "MajorVersion", "data_type": "i=3", "value_rank": -1},
                {"name": "MinorVersion", "data_type": "i=3", "value_rank": -1},
                {"name": "Revision", "data_type": "i=3", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3002",
        "StandbyModeTransitionDataType",
        "ns=1;i=5001",
        {
            "structure_type": 0,
            "fields": [
                {"name": "IDDestination", "data_type": "i=3", "value_rank": -1},
                {
                    "name": "CurrentTimeToDestination",
                    "data_type": "i=290",
                    "value_rank": -1,
                },
                {
                    "name": "CurrentTimeToOperate",
                    "data_type": "i=290",
                    "value_rank": -1,
                },
                {
                    "name": "EnergyConsumptionToDestination",
                    "data_type": "i=10",
                    "value_rank": -1,
                },
            ],
        },
    ),
]
_ENUMS: list = [
    (
        "ns=1;i=3009",
        "AccuracyClassEnumeration",
        {
            "fields": [
                {
                    "name": "ACCURACY_CLASS_0",
                    "value": 0,
                    "display_name": "ACCURACY_CLASS_0",
                },
                {
                    "name": "ACCURACY_CLASS_1",
                    "value": 1,
                    "display_name": "ACCURACY_CLASS_1",
                },
                {
                    "name": "ACCURACY_CLASS_2",
                    "value": 2,
                    "display_name": "ACCURACY_CLASS_2",
                },
                {
                    "name": "ACCURACY_CLASS_3",
                    "value": 3,
                    "display_name": "ACCURACY_CLASS_3",
                },
                {
                    "name": "ACCURACY_CLASS_4",
                    "value": 4,
                    "display_name": "ACCURACY_CLASS_4",
                },
                {
                    "name": "ACCURACY_CLASS_5",
                    "value": 5,
                    "display_name": "ACCURACY_CLASS_5",
                },
                {
                    "name": "ACCURACY_CLASS_6",
                    "value": 6,
                    "display_name": "ACCURACY_CLASS_6",
                },
                {
                    "name": "ACCURACY_CLASS_7",
                    "value": 7,
                    "display_name": "ACCURACY_CLASS_7",
                },
                {
                    "name": "ACCURACY_CLASS_8",
                    "value": 8,
                    "display_name": "ACCURACY_CLASS_8",
                },
                {
                    "name": "ACCURACY_CLASS_9",
                    "value": 9,
                    "display_name": "ACCURACY_CLASS_9",
                },
                {
                    "name": "ACCURACY_CLASS_10",
                    "value": 10,
                    "display_name": "ACCURACY_CLASS_10",
                },
                {
                    "name": "ACCURACY_CLASS_11",
                    "value": 11,
                    "display_name": "ACCURACY_CLASS_11",
                },
                {
                    "name": "ACCURACY_CLASS_12",
                    "value": 12,
                    "display_name": "ACCURACY_CLASS_12",
                },
                {
                    "name": "ACCURACY_CLASS_13",
                    "value": 13,
                    "display_name": "ACCURACY_CLASS_13",
                },
                {
                    "name": "ACCURACY_CLASS_14",
                    "value": 14,
                    "display_name": "ACCURACY_CLASS_14",
                },
                {
                    "name": "ACCURACY_CLASS_15",
                    "value": 15,
                    "display_name": "ACCURACY_CLASS_15",
                },
            ]
        },
    ),
    (
        "ns=1;i=3010",
        "AccuracyDomainEnumeration",
        {
            "fields": [
                {
                    "name": "ACCURACY_DOMAIN_RESERVED",
                    "value": 0,
                    "display_name": "ACCURACY_DOMAIN_RESERVED",
                },
                {
                    "name": "ACCURACY_DOMAIN_PERCENT_FULL_SCALE",
                    "value": 1,
                    "display_name": "ACCURACY_DOMAIN_PERCENT_FULL_SCALE",
                },
                {
                    "name": "ACCURACY_DOMAIN_PERCENT_ACTUAL_READING",
                    "value": 2,
                    "display_name": "ACCURACY_DOMAIN_PERCENT_ACTUAL_READING",
                },
                {
                    "name": "ACCURACY_DOMAIN_IEC",
                    "value": 3,
                    "display_name": "ACCURACY_DOMAIN_IEC",
                },
                {
                    "name": "ACCURACY_DOMAIN_EN",
                    "value": 4,
                    "display_name": "ACCURACY_DOMAIN_EN",
                },
            ]
        },
    ),
    (
        "ns=1;i=3007",
        "PeClassEnumeration",
        {
            "fields": [
                {"name": "PE_CLASS1", "value": 0, "display_name": "PE_CLASS1"},
                {"name": "PE_CLASS2", "value": 1, "display_name": "PE_CLASS2"},
                {"name": "PE_CLASS3", "value": 2, "display_name": "PE_CLASS3"},
            ]
        },
    ),
    (
        "ns=1;i=3008",
        "PeSubclassEnumeration",
        {
            "fields": [
                {"name": "PE_SUBCLASS1", "value": 0, "display_name": "PE_SUBCLASS1"},
                {"name": "PE_SUBCLASS2", "value": 1, "display_name": "PE_SUBCLASS2"},
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = (
    [
        ("ns=1;i=3005", "ns=1;i=5010", ["i=10", "i=10", "i=10"]),
        ("ns=1;i=3006", "ns=1;i=5013", ["i=10", "i=10", "i=10"]),
        ("ns=1;i=3003", "ns=1;i=5004", ["i=3", "i=3", "i=290", "i=10"]),
        ("ns=1;i=3004", "ns=1;i=5007", ["i=3", "i=3", "i=3"]),
        ("ns=1;i=3002", "ns=1;i=5001", ["i=3", "i=290", "i=290", "i=10"]),
    ],
    ["ns=1;i=3009", "ns=1;i=3010", "ns=1;i=3007", "ns=1;i=3008"],
)
_NODES: dict = {
    "datatypes": {
        "AcPeDataType": ("D", "ns=1;i=3005", {}),
        "AcPpDataType": ("D", "ns=1;i=3006", {}),
        "AccuracyClassEnumeration": (
            "D",
            "ns=1;i=3009",
            {"EnumValues": ("V", "ns=1;i=6111", {})},
        ),
        "AccuracyDomainEnumeration": (
            "D",
            "ns=1;i=3010",
            {"EnumValues": ("V", "ns=1;i=6130", {})},
        ),
        "EnergyStateInformationDataType": ("D", "ns=1;i=3003", {}),
        "PeClassEnumeration": (
            "D",
            "ns=1;i=3007",
            {"EnumValues": ("V", "ns=1;i=6015", {})},
        ),
        "PeSubclassEnumeration": (
            "D",
            "ns=1;i=3008",
            {"EnumValues": ("V", "ns=1;i=6017", {})},
        ),
        "PeVersionDataType": ("D", "ns=1;i=3004", {}),
        "StandbyModeTransitionDataType": ("D", "ns=1;i=3002", {}),
    },
    "ifacetypes": {
        "IEnergyProfileD0Type": (
            "OT",
            "ns=1;i=1011",
            {
                "DcCurrent": (
                    "V",
                    "ns=1;i=6102",
                    {
                        "AccuracyClass": ("V", "ns=1;i=6103", {}),
                        "AccuracyDomain": ("V", "ns=1;i=6104", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6105", {}),
                        "PeMeasurementID": ("V", "ns=1;i=6168", {}),
                    },
                )
            },
        ),
        "IEnergyProfileE0Type": (
            "OT",
            "ns=1;i=1007",
            {
                "AcCurrent": (
                    "V",
                    "ns=1;i=6060",
                    {
                        "AccuracyClass": ("V", "ns=1;i=6061", {}),
                        "AccuracyDomain": ("V", "ns=1;i=6062", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6063", {}),
                        "PeMeasurementID": ("V", "ns=1;i=6153", {}),
                    },
                )
            },
        ),
        "IEnergyProfileE1Type": (
            "OT",
            "ns=1;i=1008",
            {
                "AcActivePowerTotal": (
                    "V",
                    "ns=1;i=6064",
                    {
                        "AccuracyClass": ("V", "ns=1;i=6065", {}),
                        "AccuracyDomain": ("V", "ns=1;i=6066", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6067", {}),
                        "PeMeasurementID": ("V", "ns=1;i=6154", {}),
                    },
                )
            },
        ),
        "IEnergyProfileE2Type": (
            "OT",
            "ns=1;i=1009",
            {
                "AcActiveEnergyTotalExportLp": (
                    "V",
                    "ns=1;i=6076",
                    {
                        "AccuracyClass": ("V", "ns=1;i=6077", {}),
                        "AccuracyDomain": ("V", "ns=1;i=6078", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6079", {}),
                        "PeMeasurementID": ("V", "ns=1;i=6157", {}),
                    },
                ),
                "AcActiveEnergyTotalImportLp": (
                    "V",
                    "ns=1;i=6072",
                    {
                        "AccuracyClass": ("V", "ns=1;i=6073", {}),
                        "AccuracyDomain": ("V", "ns=1;i=6074", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6075", {}),
                        "PeMeasurementID": ("V", "ns=1;i=6156", {}),
                    },
                ),
                "AcActivePowerTotal": (
                    "V",
                    "ns=1;i=6068",
                    {
                        "AccuracyClass": ("V", "ns=1;i=6069", {}),
                        "AccuracyDomain": ("V", "ns=1;i=6070", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6071", {}),
                        "PeMeasurementID": ("V", "ns=1;i=6155", {}),
                    },
                ),
            },
        ),
        "IEnergyProfileE3Type": (
            "OT",
            "ns=1;i=1010",
            {
                "AcActiveEnergyTotalExportHp": (
                    "V",
                    "ns=1;i=6086",
                    {
                        "AccuracyClass": ("V", "ns=1;i=6087", {}),
                        "AccuracyDomain": ("V", "ns=1;i=6088", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6089", {}),
                        "PeMeasurementID": ("V", "ns=1;i=6161", {}),
                    },
                ),
                "AcActiveEnergyTotalImportHp": (
                    "V",
                    "ns=1;i=6082",
                    {
                        "AccuracyClass": ("V", "ns=1;i=6083", {}),
                        "AccuracyDomain": ("V", "ns=1;i=6084", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6085", {}),
                        "PeMeasurementID": ("V", "ns=1;i=6160", {}),
                    },
                ),
                "AcActivePower": (
                    "V",
                    "ns=1;i=6080",
                    {
                        "AccuracyClass": ("V", "ns=1;i=6122", {}),
                        "AccuracyDomain": ("V", "ns=1;i=6123", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6124", {}),
                        "PeMeasurementID": ("V", "ns=1;i=6158", {}),
                    },
                ),
                "AcCurrent": (
                    "V",
                    "ns=1;i=6100",
                    {
                        "AccuracyClass": ("V", "ns=1;i=6125", {}),
                        "AccuracyDomain": ("V", "ns=1;i=6126", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6127", {}),
                        "PeMeasurementID": ("V", "ns=1;i=6166", {}),
                    },
                ),
                "AcPowerFactor": (
                    "V",
                    "ns=1;i=6101",
                    {
                        "AccuracyClass": ("V", "ns=1;i=6128", {}),
                        "AccuracyDomain": ("V", "ns=1;i=6129", {}),
                        "PeMeasurementID": ("V", "ns=1;i=6167", {}),
                    },
                ),
                "AcReactiveEnergyTotalExportHp": (
                    "V",
                    "ns=1;i=6094",
                    {
                        "AccuracyClass": ("V", "ns=1;i=6095", {}),
                        "AccuracyDomain": ("V", "ns=1;i=6096", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6097", {}),
                        "PeMeasurementID": ("V", "ns=1;i=6163", {}),
                    },
                ),
                "AcReactiveEnergyTotalImportHp": (
                    "V",
                    "ns=1;i=6090",
                    {
                        "AccuracyClass": ("V", "ns=1;i=6091", {}),
                        "AccuracyDomain": ("V", "ns=1;i=6092", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6093", {}),
                        "PeMeasurementID": ("V", "ns=1;i=6162", {}),
                    },
                ),
                "AcReactivePower": (
                    "V",
                    "ns=1;i=6081",
                    {
                        "AccuracyClass": ("V", "ns=1;i=6131", {}),
                        "AccuracyDomain": ("V", "ns=1;i=6132", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6133", {}),
                        "PeMeasurementID": ("V", "ns=1;i=6159", {}),
                    },
                ),
                "AcVoltagePe": (
                    "V",
                    "ns=1;i=6098",
                    {
                        "AccuracyClass": ("V", "ns=1;i=6134", {}),
                        "AccuracyDomain": ("V", "ns=1;i=6135", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6136", {}),
                        "PeMeasurementID": ("V", "ns=1;i=6164", {}),
                    },
                ),
                "AcVoltagePp": (
                    "V",
                    "ns=1;i=6099",
                    {
                        "AccuracyClass": ("V", "ns=1;i=6137", {}),
                        "AccuracyDomain": ("V", "ns=1;i=6138", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6139", {}),
                        "PeMeasurementID": ("V", "ns=1;i=6165", {}),
                    },
                ),
            },
        ),
    },
    "objects": {
        "Default Binary": ("O", "ns=1;i=5013", {}),
        "Default JSON": ("O", "ns=1;i=5015", {}),
        "Default XML": ("O", "ns=1;i=5014", {}),
        "TypeDictionary": (
            "V",
            "ns=1;i=6003",
            {
                "AcPeDataType": ("V", "ns=1;i=6012", {}),
                "AcPpDataType": ("V", "ns=1;i=6014", {}),
                "EnergyStateInformationDataType": ("V", "ns=1;i=6008", {}),
                "NamespaceUri": ("V", "ns=1;i=6004", {}),
                "PeVersionDataType": ("V", "ns=1;i=6010", {}),
                "StandbyModeTransitionDataType": ("V", "ns=1;i=6006", {}),
            },
        ),
        "http://opcfoundation.org/UA/PNEM/": (
            "O",
            "ns=1;i=5021",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=6115", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=6116", {}),
                "NamespaceUri": ("V", "ns=1;i=6117", {}),
                "NamespaceVersion": ("V", "ns=1;i=6118", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=6119", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=6120", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=6121", {}),
            },
        ),
    },
    "objtypes": {
        "EnergyDevicePowerOffType": (
            "OT",
            "ns=1;i=1012",
            {
                "ModePowerConsumption": ("V", "ns=1;i=6108", {}),
                "RegularTimeToOperate": ("V", "ns=1;i=6106", {}),
                "SwitchOffWOL": (
                    "M",
                    "ns=1;i=7009",
                    {"OutputArguments": ("V", "ns=1;i=6110", {})},
                ),
                "TimeMinPause": ("V", "ns=1;i=6107", {}),
                "WOLMagicPacket": ("V", "ns=1;i=6109", {}),
            },
        ),
        "EnergyMeasurementType": (
            "OT",
            "ns=1;i=1006",
            {
                "<MeasurementValue>": (
                    "V",
                    "ns=1;i=6056",
                    {
                        "AccuracyClass": ("V", "ns=1;i=6057", {}),
                        "AccuracyDomain": ("V", "ns=1;i=6058", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6059", {}),
                        "PeMeasurementID": ("V", "ns=1;i=6152", {}),
                    },
                ),
                "PeObjectNumber": ("V", "ns=1;i=6055", {}),
                "ResetEnergyCounter": ("M", "ns=1;i=7008", {}),
            },
        ),
        "EnergySavingModeStatusType": (
            "OT",
            "ns=1;i=1002",
            {
                "CurrentTransitionData": ("V", "ns=1;i=6023", {}),
                "StateInformation": ("V", "ns=1;i=6024", {}),
            },
        ),
        "EnergySavingModeType": (
            "OT",
            "ns=1;i=1003",
            {
                "DynamicData": ("V", "ns=1;i=6026", {}),
                "EnergyConsumptionToOperate": (
                    "V",
                    "ns=1;i=6036",
                    {"EngineeringUnits": ("V", "ns=1;i=6037", {})},
                ),
                "EnergyConsumptionToPause": (
                    "V",
                    "ns=1;i=6034",
                    {"EngineeringUnits": ("V", "ns=1;i=6035", {})},
                ),
                "ID": ("V", "ns=1;i=6025", {}),
                "ModePowerConsumption": (
                    "V",
                    "ns=1;i=6032",
                    {"EngineeringUnits": ("V", "ns=1;i=6033", {})},
                ),
                "RegularTimeToOperate": ("V", "ns=1;i=6031", {}),
                "TimeMaxLengthOfStay": ("V", "ns=1;i=6030", {}),
                "TimeMinLengthOfStay": ("V", "ns=1;i=6029", {}),
                "TimeMinPause": ("V", "ns=1;i=6027", {}),
                "TimeToPause": ("V", "ns=1;i=6028", {}),
            },
        ),
        "EnergySavingModesContainerType": (
            "OT",
            "ns=1;i=1004",
            {
                "<EnergySavingModes>": (
                    "O",
                    "ns=1;i=5016",
                    {
                        "DynamicData": ("V", "ns=1;i=6140", {}),
                        "EnergyConsumptionToOperate": (
                            "V",
                            "ns=1;i=6141",
                            {"EngineeringUnits": ("V", "ns=1;i=6142", {})},
                        ),
                        "EnergyConsumptionToPause": (
                            "V",
                            "ns=1;i=6143",
                            {"EngineeringUnits": ("V", "ns=1;i=6144", {})},
                        ),
                        "ModePowerConsumption": (
                            "V",
                            "ns=1;i=6145",
                            {"EngineeringUnits": ("V", "ns=1;i=6146", {})},
                        ),
                        "RegularTimeToOperate": ("V", "ns=1;i=6147", {}),
                        "TimeMaxLengthOfStay": ("V", "ns=1;i=6148", {}),
                        "TimeMinLengthOfStay": ("V", "ns=1;i=6149", {}),
                        "TimeMinPause": ("V", "ns=1;i=6150", {}),
                        "TimeToPause": ("V", "ns=1;i=6151", {}),
                    },
                )
            },
        ),
        "EnergyStandbyManagementType": (
            "OT",
            "ns=1;i=1005",
            {
                "EndPause": (
                    "M",
                    "ns=1;i=7006",
                    {"OutputArguments": ("V", "ns=1;i=6054", {})},
                ),
                "EnergySavingModeStatus": (
                    "O",
                    "ns=1;i=5017",
                    {"StateInformation": ("V", "ns=1;i=6039", {})},
                ),
                "EnergySavingModes": ("O", "ns=1;i=5018", {}),
                "Lock": (
                    "O",
                    "ns=1;i=5020",
                    {
                        "BreakLock": (
                            "M",
                            "ns=1;i=7001",
                            {"OutputArguments": ("V", "ns=1;i=6041", {})},
                        ),
                        "ExitLock": (
                            "M",
                            "ns=1;i=7002",
                            {"OutputArguments": ("V", "ns=1;i=6042", {})},
                        ),
                        "InitLock": (
                            "M",
                            "ns=1;i=7003",
                            {
                                "InputArguments": ("V", "ns=1;i=6043", {}),
                                "OutputArguments": ("V", "ns=1;i=6044", {}),
                            },
                        ),
                        "Locked": ("V", "ns=1;i=6045", {}),
                        "LockingClient": ("V", "ns=1;i=6046", {}),
                        "LockingUser": ("V", "ns=1;i=6047", {}),
                        "RemainingLockTime": ("V", "ns=1;i=6048", {}),
                        "RenewLock": (
                            "M",
                            "ns=1;i=7004",
                            {"OutputArguments": ("V", "ns=1;i=6049", {})},
                        ),
                    },
                ),
                "PauseTime": ("V", "ns=1;i=6040", {}),
                "StandbyManagementStatus": (
                    "V",
                    "ns=1;i=6016",
                    {"EnumStrings": ("V", "ns=1;i=6038", {})},
                ),
                "StartPause": (
                    "M",
                    "ns=1;i=7005",
                    {
                        "InputArguments": ("V", "ns=1;i=6050", {}),
                        "OutputArguments": ("V", "ns=1;i=6051", {}),
                    },
                ),
                "SwitchToEnergySavingMode": (
                    "M",
                    "ns=1;i=7007",
                    {
                        "InputArguments": ("V", "ns=1;i=6052", {}),
                        "OutputArguments": ("V", "ns=1;i=6053", {}),
                    },
                ),
            },
        ),
        "PeServiceAccessPointType": (
            "OT",
            "ns=1;i=1013",
            {
                "PeClass": ("V", "ns=1;i=6112", {}),
                "PeSubclass": ("V", "ns=1;i=6113", {}),
                "PeVersion": ("V", "ns=1;i=6114", {}),
            },
        ),
    },
    "reftypes": {
        "HasEnergyMeasurement": ("RT", "ns=1;i=4004", {}),
        "HasEnergyPowerOff": ("RT", "ns=1;i=4005", {}),
        "HasEnergyStandbyManagement": ("RT", "ns=1;i=4003", {}),
        "Represents": ("RT", "ns=1;i=4002", {}),
    },
    "vartypes": {
        "MeasurementValueType": (
            "VT",
            "ns=1;i=2002",
            {
                "AccuracyClass": ("V", "ns=1;i=6020", {}),
                "AccuracyDomain": ("V", "ns=1;i=6019", {}),
                "EngineeringUnits": ("V", "ns=1;i=6021", {}),
                "PeMeasurementID": ("V", "ns=1;i=6018", {}),
                "ValueBeforeReset": ("V", "ns=1;i=6022", {}),
            },
        )
    },
}
