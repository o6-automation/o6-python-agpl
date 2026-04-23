# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 940eb7bda062aae46b26d1de5d39a058e3ea9a53885ab0021e039abfa7511ab6
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/ECM/"
_VERSION: str = "1.0.0"
_REQUIRED: list = [
    {"uri": "http://opcfoundation.org/UA/", "version": "1.05.03"},
    {"uri": "http://opcfoundation.org/UA/DI/", "version": "1.04.0"},
    {"uri": "http://opcfoundation.org/UA/IA/", "version": "1.01.2"},
]
_STRUCTURES: list = [
    (
        "ns=1;i=3005",
        "AcPeDataType",
        "ns=1;i=5010",
        {
            "structure_type": 0,
            "fields": [
                {"name": "L1", "data_type": "i=10", "value_rank": -1},
                {"name": "L2", "data_type": "i=10", "value_rank": -1},
                {"name": "L3", "data_type": "i=10", "value_rank": -1},
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
                {"name": "L1L2", "data_type": "i=10", "value_rank": -1},
                {"name": "L2L3", "data_type": "i=10", "value_rank": -1},
                {"name": "L3L1", "data_type": "i=10", "value_rank": -1},
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
        "ns=1;i=3007",
        "MeasurementPeriodDataType",
        "ns=1;i=5008",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Duration", "data_type": "i=290", "value_rank": -1},
                {"name": "Definition", "data_type": "ns=1;i=3010", "value_rank": -1},
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
        "ns=1;i=3010",
        "MeasurementPeriodEnum",
        {
            "fields": [
                {"name": "SlidingDemand", "value": 0, "display_name": "SlidingDemand"},
                {
                    "name": "FixedBlockCompleted",
                    "value": 1,
                    "display_name": "FixedBlockCompleted",
                },
                {
                    "name": "FixedBlockInstantaneous",
                    "value": 2,
                    "display_name": "FixedBlockInstantaneous",
                },
                {
                    "name": "FixedBlockPredicted",
                    "value": 3,
                    "display_name": "FixedBlockPredicted",
                },
            ]
        },
    )
]
_ORIGINAL_NODEIDS: tuple = (
    [
        ("ns=1;i=3005", "ns=1;i=5010", ["i=10", "i=10", "i=10"]),
        ("ns=1;i=3006", "ns=1;i=5013", ["i=10", "i=10", "i=10"]),
        ("ns=1;i=3003", "ns=1;i=5004", ["i=3", "i=3", "i=290", "i=10"]),
        ("ns=1;i=3007", "ns=1;i=5008", ["i=290", "ns=1;i=3010"]),
        ("ns=1;i=3002", "ns=1;i=5001", ["i=3", "i=290", "i=290", "i=10"]),
    ],
    ["ns=1;i=3010"],
)
_NODES: dict = {
    "datatypes": {
        "AcPeDataType": ("D", "ns=1;i=3005", {}),
        "AcPpDataType": ("D", "ns=1;i=3006", {}),
        "EnergyStateInformationDataType": ("D", "ns=1;i=3003", {}),
        "MeasurementPeriodDataType": ("D", "ns=1;i=3007", {}),
        "MeasurementPeriodEnum": (
            "D",
            "ns=1;i=3010",
            {"EnumValues": ("V", "ns=1;i=6361", {})},
        ),
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
                        "AccuracyClass": (
                            "V",
                            "ns=1;i=6235",
                            {
                                "EnumValues": ("V", "ns=1;i=6236", {}),
                                "ValueAsText": ("V", "ns=1;i=6237", {}),
                            },
                        ),
                        "AccuracyDomain": ("V", "ns=1;i=6104", {}),
                        "AccuracyRange": ("V", "ns=1;i=6198", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6105", {}),
                        "MeasurementID": ("V", "ns=1;i=6168", {}),
                        "Resource": (
                            "V",
                            "ns=1;i=6269",
                            {
                                "EnumValues": ("V", "ns=1;i=6270", {}),
                                "ValueAsText": ("V", "ns=1;i=6271", {}),
                            },
                        ),
                    },
                )
            },
        ),
        "IEnergyProfileD1Type": (
            "OT",
            "ns=1;i=1015",
            {
                "DcActivePower": (
                    "V",
                    "ns=1;i=6307",
                    {
                        "AccuracyClass": (
                            "V",
                            "ns=1;i=6308",
                            {
                                "EnumValues": ("V", "ns=1;i=6309", {}),
                                "ValueAsText": ("V", "ns=1;i=6310", {}),
                            },
                        ),
                        "AccuracyDomain": ("V", "ns=1;i=6311", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6351", {}),
                        "MeasurementID": ("V", "ns=1;i=6352", {}),
                        "Resource": (
                            "V",
                            "ns=1;i=6312",
                            {
                                "EnumValues": ("V", "ns=1;i=6313", {}),
                                "ValueAsText": ("V", "ns=1;i=6314", {}),
                            },
                        ),
                    },
                ),
                "DcCurrent": (
                    "V",
                    "ns=1;i=6291",
                    {
                        "AccuracyClass": (
                            "V",
                            "ns=1;i=6292",
                            {
                                "EnumValues": ("V", "ns=1;i=6293", {}),
                                "ValueAsText": ("V", "ns=1;i=6294", {}),
                            },
                        ),
                        "AccuracyDomain": ("V", "ns=1;i=6295", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6347", {}),
                        "MeasurementID": ("V", "ns=1;i=6348", {}),
                        "Resource": (
                            "V",
                            "ns=1;i=6296",
                            {
                                "EnumValues": ("V", "ns=1;i=6297", {}),
                                "ValueAsText": ("V", "ns=1;i=6298", {}),
                            },
                        ),
                    },
                ),
                "DcVoltage": (
                    "V",
                    "ns=1;i=6299",
                    {
                        "AccuracyClass": (
                            "V",
                            "ns=1;i=6300",
                            {
                                "EnumValues": ("V", "ns=1;i=6301", {}),
                                "ValueAsText": ("V", "ns=1;i=6302", {}),
                            },
                        ),
                        "AccuracyDomain": ("V", "ns=1;i=6303", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6349", {}),
                        "MeasurementID": ("V", "ns=1;i=6350", {}),
                        "Resource": (
                            "V",
                            "ns=1;i=6304",
                            {
                                "EnumValues": ("V", "ns=1;i=6305", {}),
                                "ValueAsText": ("V", "ns=1;i=6306", {}),
                            },
                        ),
                    },
                ),
            },
        ),
        "IEnergyProfileE0Type": (
            "OT",
            "ns=1;i=1007",
            {
                "AcCurrentPe": (
                    "V",
                    "ns=1;i=6060",
                    {
                        "AccuracyClass": (
                            "V",
                            "ns=1;i=6077",
                            {
                                "EnumValues": ("V", "ns=1;i=6083", {}),
                                "ValueAsText": ("V", "ns=1;i=6087", {}),
                            },
                        ),
                        "AccuracyDomain": ("V", "ns=1;i=6062", {}),
                        "AccuracyRange": ("V", "ns=1;i=6114", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6063", {}),
                        "MeasurementID": ("V", "ns=1;i=6153", {}),
                        "Resource": (
                            "V",
                            "ns=1;i=6173",
                            {
                                "EnumValues": ("V", "ns=1;i=6175", {}),
                                "ValueAsText": ("V", "ns=1;i=6177", {}),
                            },
                        ),
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
                        "AccuracyClass": (
                            "V",
                            "ns=1;i=6091",
                            {
                                "EnumValues": ("V", "ns=1;i=6095", {}),
                                "ValueAsText": ("V", "ns=1;i=6103", {}),
                            },
                        ),
                        "AccuracyDomain": ("V", "ns=1;i=6066", {}),
                        "AccuracyRange": ("V", "ns=1;i=6170", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6067", {}),
                        "MeasurementID": ("V", "ns=1;i=6154", {}),
                        "Resource": (
                            "V",
                            "ns=1;i=6179",
                            {
                                "EnumValues": ("V", "ns=1;i=6181", {}),
                                "ValueAsText": ("V", "ns=1;i=6183", {}),
                            },
                        ),
                    },
                )
            },
        ),
        "IEnergyProfileE2Type": (
            "OT",
            "ns=1;i=1009",
            {
                "AcActivePowerTotal": (
                    "V",
                    "ns=1;i=6068",
                    {
                        "AccuracyClass": (
                            "V",
                            "ns=1;i=6122",
                            {
                                "EnumValues": ("V", "ns=1;i=6125", {}),
                                "ValueAsText": ("V", "ns=1;i=6128", {}),
                            },
                        ),
                        "AccuracyDomain": ("V", "ns=1;i=6070", {}),
                        "AccuracyRange": ("V", "ns=1;i=6172", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6071", {}),
                        "MeasurementID": ("V", "ns=1;i=6155", {}),
                        "Resource": (
                            "V",
                            "ns=1;i=6185",
                            {
                                "EnumValues": ("V", "ns=1;i=6187", {}),
                                "ValueAsText": ("V", "ns=1;i=6189", {}),
                            },
                        ),
                    },
                )
            },
        ),
        "IEnergyProfileE3Type": (
            "OT",
            "ns=1;i=1010",
            {
                "AcActivePowerPe": (
                    "V",
                    "ns=1;i=6080",
                    {
                        "AccuracyClass": (
                            "V",
                            "ns=1;i=6205",
                            {
                                "EnumValues": ("V", "ns=1;i=6206", {}),
                                "ValueAsText": ("V", "ns=1;i=6207", {}),
                            },
                        ),
                        "AccuracyDomain": ("V", "ns=1;i=6123", {}),
                        "AccuracyRange": ("V", "ns=1;i=6178", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6124", {}),
                        "MeasurementID": ("V", "ns=1;i=6158", {}),
                        "Resource": (
                            "V",
                            "ns=1;i=6239",
                            {
                                "EnumValues": ("V", "ns=1;i=6240", {}),
                                "ValueAsText": ("V", "ns=1;i=6241", {}),
                            },
                        ),
                    },
                ),
                "AcCurrentPe": (
                    "V",
                    "ns=1;i=6100",
                    {
                        "AccuracyClass": (
                            "V",
                            "ns=1;i=6229",
                            {
                                "EnumValues": ("V", "ns=1;i=6230", {}),
                                "ValueAsText": ("V", "ns=1;i=6231", {}),
                            },
                        ),
                        "AccuracyDomain": ("V", "ns=1;i=6126", {}),
                        "AccuracyRange": ("V", "ns=1;i=6194", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6127", {}),
                        "MeasurementID": ("V", "ns=1;i=6166", {}),
                        "Resource": (
                            "V",
                            "ns=1;i=6263",
                            {
                                "EnumValues": ("V", "ns=1;i=6264", {}),
                                "ValueAsText": ("V", "ns=1;i=6265", {}),
                            },
                        ),
                    },
                ),
                "AcPowerFactorPe": (
                    "V",
                    "ns=1;i=6101",
                    {
                        "AccuracyClass": (
                            "V",
                            "ns=1;i=6232",
                            {
                                "EnumValues": ("V", "ns=1;i=6233", {}),
                                "ValueAsText": ("V", "ns=1;i=6234", {}),
                            },
                        ),
                        "AccuracyDomain": ("V", "ns=1;i=6129", {}),
                        "AccuracyRange": ("V", "ns=1;i=6196", {}),
                        "MeasurementID": ("V", "ns=1;i=6167", {}),
                        "Resource": (
                            "V",
                            "ns=1;i=6266",
                            {
                                "EnumValues": ("V", "ns=1;i=6267", {}),
                                "ValueAsText": ("V", "ns=1;i=6268", {}),
                            },
                        ),
                    },
                ),
                "AcReactivePowerPe": (
                    "V",
                    "ns=1;i=6081",
                    {
                        "AccuracyClass": (
                            "V",
                            "ns=1;i=6208",
                            {
                                "EnumValues": ("V", "ns=1;i=6209", {}),
                                "ValueAsText": ("V", "ns=1;i=6210", {}),
                            },
                        ),
                        "AccuracyDomain": ("V", "ns=1;i=6132", {}),
                        "AccuracyRange": ("V", "ns=1;i=6180", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6133", {}),
                        "MeasurementID": ("V", "ns=1;i=6159", {}),
                        "Resource": (
                            "V",
                            "ns=1;i=6242",
                            {
                                "EnumValues": ("V", "ns=1;i=6243", {}),
                                "ValueAsText": ("V", "ns=1;i=6244", {}),
                            },
                        ),
                    },
                ),
                "AcVoltagePe": (
                    "V",
                    "ns=1;i=6098",
                    {
                        "AccuracyClass": (
                            "V",
                            "ns=1;i=6223",
                            {
                                "EnumValues": ("V", "ns=1;i=6224", {}),
                                "ValueAsText": ("V", "ns=1;i=6225", {}),
                            },
                        ),
                        "AccuracyDomain": ("V", "ns=1;i=6135", {}),
                        "AccuracyRange": ("V", "ns=1;i=6190", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6136", {}),
                        "MeasurementID": ("V", "ns=1;i=6164", {}),
                        "Resource": (
                            "V",
                            "ns=1;i=6257",
                            {
                                "EnumValues": ("V", "ns=1;i=6258", {}),
                                "ValueAsText": ("V", "ns=1;i=6259", {}),
                            },
                        ),
                    },
                ),
                "AcVoltagePp": (
                    "V",
                    "ns=1;i=6099",
                    {
                        "AccuracyClass": (
                            "V",
                            "ns=1;i=6226",
                            {
                                "EnumValues": ("V", "ns=1;i=6227", {}),
                                "ValueAsText": ("V", "ns=1;i=6228", {}),
                            },
                        ),
                        "AccuracyDomain": ("V", "ns=1;i=6138", {}),
                        "AccuracyRange": ("V", "ns=1;i=6192", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6139", {}),
                        "MeasurementID": ("V", "ns=1;i=6165", {}),
                        "Resource": (
                            "V",
                            "ns=1;i=6260",
                            {
                                "EnumValues": ("V", "ns=1;i=6261", {}),
                                "ValueAsText": ("V", "ns=1;i=6262", {}),
                            },
                        ),
                    },
                ),
            },
        ),
    },
    "objects": {
        "AcActiveEnergyTotalExportHp": (
            "V",
            "ns=1;i=6086",
            {
                "AccuracyClass": (
                    "V",
                    "ns=1;i=6214",
                    {
                        "EnumValues": ("V", "ns=1;i=6215", {}),
                        "ValueAsText": ("V", "ns=1;i=6216", {}),
                    },
                ),
                "AccuracyDomain": ("V", "ns=1;i=6088", {}),
                "AccuracyRange": ("V", "ns=1;i=6184", {}),
                "EngineeringUnits": ("V", "ns=1;i=6089", {}),
                "MeasurementID": ("V", "ns=1;i=6161", {}),
                "Resource": (
                    "V",
                    "ns=1;i=6248",
                    {
                        "EnumValues": ("V", "ns=1;i=6249", {}),
                        "ValueAsText": ("V", "ns=1;i=6250", {}),
                    },
                ),
            },
        ),
        "AcActiveEnergyTotalExportLp": (
            "V",
            "ns=1;i=6076",
            {
                "AccuracyClass": (
                    "V",
                    "ns=1;i=6202",
                    {
                        "EnumValues": ("V", "ns=1;i=6203", {}),
                        "ValueAsText": ("V", "ns=1;i=6204", {}),
                    },
                ),
                "AccuracyDomain": ("V", "ns=1;i=6078", {}),
                "AccuracyRange": ("V", "ns=1;i=6176", {}),
                "EngineeringUnits": ("V", "ns=1;i=6079", {}),
                "MeasurementID": ("V", "ns=1;i=6157", {}),
                "Resource": (
                    "V",
                    "ns=1;i=6197",
                    {
                        "EnumValues": ("V", "ns=1;i=6199", {}),
                        "ValueAsText": ("V", "ns=1;i=6238", {}),
                    },
                ),
            },
        ),
        "AcActiveEnergyTotalImportHp": (
            "V",
            "ns=1;i=6082",
            {
                "AccuracyClass": (
                    "V",
                    "ns=1;i=6211",
                    {
                        "EnumValues": ("V", "ns=1;i=6212", {}),
                        "ValueAsText": ("V", "ns=1;i=6213", {}),
                    },
                ),
                "AccuracyDomain": ("V", "ns=1;i=6084", {}),
                "AccuracyRange": ("V", "ns=1;i=6182", {}),
                "EngineeringUnits": ("V", "ns=1;i=6085", {}),
                "MeasurementID": ("V", "ns=1;i=6160", {}),
                "Resource": (
                    "V",
                    "ns=1;i=6245",
                    {
                        "EnumValues": ("V", "ns=1;i=6246", {}),
                        "ValueAsText": ("V", "ns=1;i=6247", {}),
                    },
                ),
            },
        ),
        "AcActiveEnergyTotalImportLp": (
            "V",
            "ns=1;i=6072",
            {
                "AccuracyClass": (
                    "V",
                    "ns=1;i=6131",
                    {
                        "EnumValues": ("V", "ns=1;i=6134", {}),
                        "ValueAsText": ("V", "ns=1;i=6137", {}),
                    },
                ),
                "AccuracyDomain": ("V", "ns=1;i=6074", {}),
                "AccuracyRange": ("V", "ns=1;i=6174", {}),
                "EngineeringUnits": ("V", "ns=1;i=6075", {}),
                "MeasurementID": ("V", "ns=1;i=6156", {}),
                "Resource": (
                    "V",
                    "ns=1;i=6191",
                    {
                        "EnumValues": ("V", "ns=1;i=6193", {}),
                        "ValueAsText": ("V", "ns=1;i=6195", {}),
                    },
                ),
            },
        ),
        "AcReactiveEnergyTotalExportHp": (
            "V",
            "ns=1;i=6094",
            {
                "AccuracyClass": (
                    "V",
                    "ns=1;i=6220",
                    {
                        "EnumValues": ("V", "ns=1;i=6221", {}),
                        "ValueAsText": ("V", "ns=1;i=6222", {}),
                    },
                ),
                "AccuracyDomain": ("V", "ns=1;i=6096", {}),
                "AccuracyRange": ("V", "ns=1;i=6188", {}),
                "EngineeringUnits": ("V", "ns=1;i=6097", {}),
                "MeasurementID": ("V", "ns=1;i=6163", {}),
                "Resource": (
                    "V",
                    "ns=1;i=6254",
                    {
                        "EnumValues": ("V", "ns=1;i=6255", {}),
                        "ValueAsText": ("V", "ns=1;i=6256", {}),
                    },
                ),
            },
        ),
        "AcReactiveEnergyTotalImportHp": (
            "V",
            "ns=1;i=6090",
            {
                "AccuracyClass": (
                    "V",
                    "ns=1;i=6217",
                    {
                        "EnumValues": ("V", "ns=1;i=6218", {}),
                        "ValueAsText": ("V", "ns=1;i=6219", {}),
                    },
                ),
                "AccuracyDomain": ("V", "ns=1;i=6092", {}),
                "AccuracyRange": ("V", "ns=1;i=6186", {}),
                "EngineeringUnits": ("V", "ns=1;i=6093", {}),
                "MeasurementID": ("V", "ns=1;i=6162", {}),
                "Resource": (
                    "V",
                    "ns=1;i=6251",
                    {
                        "EnumValues": ("V", "ns=1;i=6252", {}),
                        "ValueAsText": ("V", "ns=1;i=6253", {}),
                    },
                ),
            },
        ),
        "AccuracyDomains": (
            "O",
            "ns=1;i=5009",
            {
                "ACCURACY_DOMAIN_EN": (
                    "O",
                    "ns=1;i=5030",
                    {"EnumValues": ("V", "ns=1;i=6275", {})},
                ),
                "ACCURACY_DOMAIN_IEC": (
                    "O",
                    "ns=1;i=5027",
                    {"EnumValues": ("V", "ns=1;i=6274", {})},
                ),
                "ACCURACY_DOMAIN_PERCENT_ACTUAL_READING": (
                    "O",
                    "ns=1;i=5024",
                    {"EnumValues": ("V", "ns=1;i=6273", {})},
                ),
                "ACCURACY_DOMAIN_PERCENT_FULL_SCALE": (
                    "O",
                    "ns=1;i=5019",
                    {"EnumValues": ("V", "ns=1;i=6272", {})},
                ),
            },
        ),
        "DcElectricalCharge": (
            "V",
            "ns=1;i=6331",
            {
                "AccuracyClass": (
                    "V",
                    "ns=1;i=6332",
                    {
                        "EnumValues": ("V", "ns=1;i=6333", {}),
                        "ValueAsText": ("V", "ns=1;i=6334", {}),
                    },
                ),
                "AccuracyDomain": ("V", "ns=1;i=6335", {}),
                "EngineeringUnits": ("V", "ns=1;i=6355", {}),
                "MeasurementID": ("V", "ns=1;i=6356", {}),
                "Resource": (
                    "V",
                    "ns=1;i=6336",
                    {
                        "EnumValues": ("V", "ns=1;i=6337", {}),
                        "ValueAsText": ("V", "ns=1;i=6338", {}),
                    },
                ),
            },
        ),
        "DcEnergyTotalExportLp": (
            "V",
            "ns=1;i=6323",
            {
                "AccuracyClass": (
                    "V",
                    "ns=1;i=6324",
                    {
                        "EnumValues": ("V", "ns=1;i=6325", {}),
                        "ValueAsText": ("V", "ns=1;i=6326", {}),
                    },
                ),
                "AccuracyDomain": ("V", "ns=1;i=6327", {}),
                "EngineeringUnits": ("V", "ns=1;i=6362", {}),
                "MeasurementID": ("V", "ns=1;i=6363", {}),
                "Resource": (
                    "V",
                    "ns=1;i=6328",
                    {
                        "EnumValues": ("V", "ns=1;i=6329", {}),
                        "ValueAsText": ("V", "ns=1;i=6330", {}),
                    },
                ),
            },
        ),
        "DcEnergyTotalImportLp": (
            "V",
            "ns=1;i=6315",
            {
                "AccuracyClass": (
                    "V",
                    "ns=1;i=6316",
                    {
                        "EnumValues": ("V", "ns=1;i=6317", {}),
                        "ValueAsText": ("V", "ns=1;i=6318", {}),
                    },
                ),
                "AccuracyDomain": ("V", "ns=1;i=6319", {}),
                "EngineeringUnits": ("V", "ns=1;i=6353", {}),
                "MeasurementID": ("V", "ns=1;i=6354", {}),
                "Resource": (
                    "V",
                    "ns=1;i=6320",
                    {
                        "EnumValues": ("V", "ns=1;i=6321", {}),
                        "ValueAsText": ("V", "ns=1;i=6322", {}),
                    },
                ),
            },
        ),
        "DcRelativeCharge": (
            "V",
            "ns=1;i=6339",
            {
                "AccuracyClass": (
                    "V",
                    "ns=1;i=6340",
                    {
                        "EnumValues": ("V", "ns=1;i=6341", {}),
                        "ValueAsText": ("V", "ns=1;i=6342", {}),
                    },
                ),
                "AccuracyDomain": ("V", "ns=1;i=6343", {}),
                "EngineeringUnits": ("V", "ns=1;i=6357", {}),
                "MeasurementID": ("V", "ns=1;i=6358", {}),
                "Resource": (
                    "V",
                    "ns=1;i=6344",
                    {
                        "EnumValues": ("V", "ns=1;i=6345", {}),
                        "ValueAsText": ("V", "ns=1;i=6346", {}),
                    },
                ),
            },
        ),
        "Default Binary": ("O", "ns=1;i=5013", {}),
        "Default JSON": ("O", "ns=1;i=5023", {}),
        "Default XML": ("O", "ns=1;i=5022", {}),
        "TypeDictionary": (
            "V",
            "ns=1;i=6003",
            {
                "AcPeDataType": ("V", "ns=1;i=6012", {}),
                "AcPpDataType": ("V", "ns=1;i=6014", {}),
                "Deprecated": ("V", "ns=1;i=6277", {}),
                "EnergyStateInformationDataType": ("V", "ns=1;i=6008", {}),
                "MeasurementPeriodDataType": ("V", "ns=1;i=6360", {}),
                "NamespaceUri": ("V", "ns=1;i=6004", {}),
                "StandbyModeTransitionDataType": ("V", "ns=1;i=6006", {}),
            },
        ),
        "http://opcfoundation.org/UA/ECM/": (
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
        "AccuracyDomainType": (
            "OT",
            "ns=1;i=1014",
            {"EnumValues": ("V", "ns=1;i=6201", {})},
        ),
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
                        "AccuracyClass": (
                            "V",
                            "ns=1;i=6065",
                            {
                                "EnumValues": ("V", "ns=1;i=6069", {}),
                                "ValueAsText": ("V", "ns=1;i=6073", {}),
                            },
                        ),
                        "AccuracyDomain": ("V", "ns=1;i=6058", {}),
                        "AccuracyRange": ("V", "ns=1;i=6112", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6059", {}),
                        "MeasurementID": ("V", "ns=1;i=6152", {}),
                        "Resource": (
                            "V",
                            "ns=1;i=6130",
                            {
                                "EnumValues": ("V", "ns=1;i=6169", {}),
                                "ValueAsText": ("V", "ns=1;i=6171", {}),
                            },
                        ),
                    },
                ),
                "ApplicationTag": ("V", "ns=1;i=6055", {}),
                "ResetStatistics": ("M", "ns=1;i=7008", {}),
                "StartTime": ("V", "ns=1;i=6009", {}),
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
                        "ID": ("V", "ns=1;i=6200", {}),
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
                "EnergySavingModes": (
                    "O",
                    "ns=1;i=5018",
                    {
                        "EnergySavingModes": (
                            "O",
                            "ns=1;i=5007",
                            {
                                "DynamicData": ("V", "ns=1;i=6278", {}),
                                "EnergyConsumptionToOperate": (
                                    "V",
                                    "ns=1;i=6279",
                                    {"EngineeringUnits": ("V", "ns=1;i=6280", {})},
                                ),
                                "EnergyConsumptionToPause": (
                                    "V",
                                    "ns=1;i=6281",
                                    {"EngineeringUnits": ("V", "ns=1;i=6282", {})},
                                ),
                                "ID": ("V", "ns=1;i=6283", {}),
                                "ModePowerConsumption": (
                                    "V",
                                    "ns=1;i=6284",
                                    {"EngineeringUnits": ("V", "ns=1;i=6285", {})},
                                ),
                                "RegularTimeToOperate": ("V", "ns=1;i=6286", {}),
                                "TimeMaxLengthOfStay": ("V", "ns=1;i=6287", {}),
                                "TimeMinLengthOfStay": ("V", "ns=1;i=6288", {}),
                                "TimeMinPause": ("V", "ns=1;i=6289", {}),
                                "TimeToPause": ("V", "ns=1;i=6290", {}),
                            },
                        )
                    },
                ),
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
    },
    "vartypes": {
        "EnergyMeasurementValueType": (
            "VT",
            "ns=1;i=2002",
            {
                "AccuracyClass": (
                    "V",
                    "ns=1;i=6020",
                    {
                        "EnumValues": ("V", "ns=1;i=6057", {}),
                        "ValueAsText": ("V", "ns=1;i=6061", {}),
                    },
                ),
                "AccuracyDomain": ("V", "ns=1;i=6019", {}),
                "AccuracyRange": ("V", "ns=1;i=6010", {}),
                "EngineeringUnits": ("V", "ns=1;i=6021", {}),
                "MeasurementID": ("V", "ns=1;i=6018", {}),
                "MeasurementPeriod": ("V", "ns=1;i=6015", {}),
                "Resource": (
                    "V",
                    "ns=1;i=6017",
                    {
                        "EnumValues": ("V", "ns=1;i=6111", {}),
                        "ValueAsText": ("V", "ns=1;i=6113", {}),
                    },
                ),
                "ValueBeforeReset": ("V", "ns=1;i=6022", {}),
            },
        )
    },
}
