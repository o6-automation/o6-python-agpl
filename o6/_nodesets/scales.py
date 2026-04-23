# AUTO-GENERATED — DO NOT EDIT
# source-sha256: cffc839eaae775e5c9fc31557048b4a07d3a5b69bcea1260b15d1a459db19f70
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/Scales/V2/"
_VERSION: str = "2.00"
_REQUIRED: list = [
    {"uri": "http://opcfoundation.org/UA/", "version": "1.05.03"},
    {"uri": "http://opcfoundation.org/UA/DI/", "version": "1.04.0"},
    {"uri": "http://opcfoundation.org/UA/IA/", "version": "1.01.2"},
    {"uri": "http://opcfoundation.org/UA/Machinery/", "version": "1.03.0"},
    {"uri": "http://opcfoundation.org/UA/PackML/", "version": "1.01"},
]
_STRUCTURES: list = [
    (
        "ns=1;i=63",
        "AbstractWeightType",
        "ns=1;i=109",
        {"structure_type": 0, "fields": []},
    ),
    (
        "ns=1;i=56",
        "PrintableWeightType",
        "ns=1;i=97",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Gross", "data_type": "i=12", "value_rank": -1},
                {"name": "Net", "data_type": "i=12", "value_rank": -1},
                {"name": "Tare", "data_type": "i=12", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=55",
        "WeightType",
        "ns=1;i=88",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Gross", "data_type": "i=11", "value_rank": -1},
                {"name": "Net", "data_type": "i=11", "value_rank": -1},
                {"name": "Tare", "data_type": "i=11", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=59",
        "RecipeReportElementType",
        "ns=1;i=106",
        {
            "structure_type": 0,
            "fields": [
                {"name": "ReportMessage", "data_type": "i=21", "value_rank": -1},
                {"name": "Timestamp", "data_type": "i=294", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=58",
        "RecipeTargetValueType",
        "ns=1;i=103",
        {
            "structure_type": 1,
            "fields": [
                {"name": "TargetValueId", "data_type": "i=7", "value_rank": -1},
                {
                    "name": "TargetValueNodeId",
                    "data_type": "i=17",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {"name": "TargetValueName", "data_type": "i=21", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=57",
        "RecipeThresholdType",
        "ns=1;i=100",
        {
            "structure_type": 1,
            "fields": [
                {"name": "ThresholdId", "data_type": "i=7", "value_rank": -1},
                {
                    "name": "ThresholdNodeId",
                    "data_type": "i=17",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {"name": "ThresholdName", "data_type": "i=21", "value_rank": -1},
            ],
        },
    ),
]
_ENUMS: list = [
    (
        "ns=1;i=65",
        "DraftShieldType",
        {
            "fields": [
                {"name": "Right_0", "value": 0, "display_name": "Right_0"},
                {"name": "Left_1", "value": 1, "display_name": "Left_1"},
                {"name": "Top_2", "value": 2, "display_name": "Top_2"},
                {"name": "All_3", "value": 3, "display_name": "All_3"},
            ]
        },
    ),
    (
        "ns=1;i=62",
        "EdgeOperator",
        {
            "fields": [
                {"name": "Rising_0", "value": 0, "display_name": "Rising_0"},
                {"name": "Falling_1", "value": 1, "display_name": "Falling_1"},
            ]
        },
    ),
    (
        "ns=1;i=61",
        "EqualityAndRelationalOperator",
        {
            "fields": [
                {"name": "Equal_0", "value": 0, "display_name": "Equal_0"},
                {"name": "NotEqual_1", "value": 1, "display_name": "NotEqual_1"},
                {
                    "name": "LessOrEqualThan_2",
                    "value": 2,
                    "display_name": "LessOrEqualThan_2",
                },
                {
                    "name": "GreaterOrEqualThan_3",
                    "value": 3,
                    "display_name": "GreaterOrEqualThan_3",
                },
                {"name": "LessThan_4", "value": 4, "display_name": "LessThan_4"},
                {"name": "GreaterThan_5", "value": 5, "display_name": "GreaterThan_5"},
            ]
        },
    ),
    (
        "ns=1;i=30003",
        "RateControlMode",
        {
            "fields": [
                {"name": "Gravimetric_0", "value": 0, "display_name": "Gravimetric_0"},
                {"name": "Volumetric_1", "value": 1, "display_name": "Volumetric_1"},
            ]
        },
    ),
    (
        "ns=1;i=54",
        "TareMode",
        {
            "fields": [
                {"name": "None_0", "value": 0, "display_name": "None_0"},
                {
                    "name": "MeasuredTare_1",
                    "value": 1,
                    "display_name": "MeasuredTare_1",
                },
                {"name": "PresetTare_2", "value": 2, "display_name": "PresetTare_2"},
                {
                    "name": "ProportionalTare_3",
                    "value": 3,
                    "display_name": "ProportionalTare_3",
                },
            ]
        },
    ),
    (
        "ns=1;i=60",
        "ToleranceState",
        {
            "fields": [
                {"name": "In_0", "value": 0, "display_name": "In_0"},
                {"name": "Under_1", "value": 1, "display_name": "Under_1"},
                {"name": "Over_2", "value": 2, "display_name": "Over_2"},
                {"name": "UnderOrOver_3", "value": 3, "display_name": "UnderOrOver_3"},
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = (
    [
        ("ns=1;i=63", "ns=1;i=109", []),
        ("ns=1;i=56", "ns=1;i=97", ["i=12", "i=12", "i=12"]),
        ("ns=1;i=55", "ns=1;i=88", ["i=11", "i=11", "i=11"]),
        ("ns=1;i=59", "ns=1;i=106", ["i=21", "i=294"]),
        ("ns=1;i=58", "ns=1;i=103", ["i=7", "i=17", "i=21"]),
        ("ns=1;i=57", "ns=1;i=100", ["i=7", "i=17", "i=21"]),
    ],
    ["ns=1;i=65", "ns=1;i=62", "ns=1;i=61", "ns=1;i=30003", "ns=1;i=54", "ns=1;i=60"],
)
_NODES: dict = {
    "datatypes": {
        "AbstractWeightType": (
            "D",
            "ns=1;i=63",
            {
                "PrintableWeightType": ("D", "ns=1;i=56", {}),
                "WeightType": ("D", "ns=1;i=55", {}),
            },
        ),
        "DraftShieldType": ("D", "ns=1;i=65", {"EnumStrings": ("V", "ns=1;i=760", {})}),
        "EdgeOperator": ("D", "ns=1;i=62", {"EnumStrings": ("V", "ns=1;i=323", {})}),
        "EqualityAndRelationalOperator": (
            "D",
            "ns=1;i=61",
            {"EnumStrings": ("V", "ns=1;i=322", {})},
        ),
        "RateControlMode": (
            "D",
            "ns=1;i=30003",
            {"EnumStrings": ("V", "ns=1;i=60156", {})},
        ),
        "RecipeReportElementType": ("D", "ns=1;i=59", {}),
        "RecipeTargetValueType": ("D", "ns=1;i=58", {}),
        "RecipeThresholdType": ("D", "ns=1;i=57", {}),
        "TareMode": ("D", "ns=1;i=54", {"EnumStrings": ("V", "ns=1;i=195", {})}),
        "ToleranceState": ("D", "ns=1;i=60", {"EnumStrings": ("V", "ns=1;i=321", {})}),
    },
    "eventtypes": {
        "ScaleEventType": (
            "OT",
            "ns=1;i=13",
            {
                "AuxParameters": ("V", "ns=1;i=312", {}),
                "HelpSource": ("V", "ns=1;i=319", {}),
                "NotificationCategory": (
                    "V",
                    "ns=1;i=325",
                    {
                        "EnumValues": ("V", "ns=1;i=326", {}),
                        "ValueAsText": ("V", "ns=1;i=327", {}),
                    },
                ),
                "NotificationId": (
                    "V",
                    "ns=1;i=134",
                    {
                        "EnumValues": ("V", "ns=1;i=233", {}),
                        "ValueAsText": ("V", "ns=1;i=244", {}),
                    },
                ),
                "VendorNotificationId": ("V", "ns=1;i=948", {}),
            },
        )
    },
    "objects": {
        "<PackagesAcceptedWithProperty>": (
            "O",
            "ns=1;i=1169",
            {"Weighed": ("V", "ns=1;i=1206", {})},
        ),
        "<PackagesRejectedBySystem>": (
            "O",
            "ns=1;i=50032",
            {"Weighed": ("V", "ns=1;i=60235", {})},
        ),
        "Default Binary": ("O", "ns=1;i=109", {}),
        "Default JSON": ("O", "ns=1;i=111", {}),
        "Default XML": ("O", "ns=1;i=110", {}),
        "GiveAway": (
            "V",
            "ns=1;i=60185",
            {"EngineeringUnits": ("V", "ns=1;i=60186", {})},
        ),
        "Identification": (
            "O",
            "ns=1;i=50014",
            {
                "Manufacturer": ("V", "ns=1;i=60072", {}),
                "ProductInstanceUri": ("V", "ns=1;i=60073", {}),
                "SerialNumber": ("V", "ns=1;i=60241", {}),
            },
        ),
        "ItemCount": ("V", "ns=1;i=320", {}),
        "MachineryItemState": (
            "O",
            "ns=1;i=50029",
            {"CurrentState": ("V", "ns=1;i=60134", {"Id": ("V", "ns=1;i=60135", {})})},
        ),
        "MachineryOperationMode": (
            "O",
            "ns=1;i=50030",
            {"CurrentState": ("V", "ns=1;i=60136", {"Id": ("V", "ns=1;i=60137", {})})},
        ),
        "MaxValue": (
            "V",
            "ns=1;i=60191",
            {"EngineeringUnits": ("V", "ns=1;i=60192", {})},
        ),
        "MeanValue": (
            "V",
            "ns=1;i=60193",
            {"EngineeringUnits": ("V", "ns=1;i=60194", {})},
        ),
        "MinValue": (
            "V",
            "ns=1;i=60195",
            {"EngineeringUnits": ("V", "ns=1;i=60196", {})},
        ),
        "Opc.Ua.Scale": (
            "V",
            "ns=1;i=188",
            {
                "NamespaceUri": ("V", "ns=1;i=189", {}),
                "PrintableWeightType": ("V", "ns=1;i=60096", {}),
                "RecipeReportElementType": ("V", "ns=1;i=60100", {}),
                "RecipeTargetValueType": ("V", "ns=1;i=60102", {}),
                "RecipeThresholdType": ("V", "ns=1;i=60104", {}),
                "WeightType": ("V", "ns=1;i=60098", {}),
            },
        ),
        "PackagesAcceptedWithLowerToleranceLimit1": (
            "O",
            "ns=1;i=1042",
            {"Weighed": ("V", "ns=1;i=1087", {})},
        ),
        "PackagesRejectedByDistanceFault": (
            "O",
            "ns=1;i=1043",
            {"Weighed": ("V", "ns=1;i=1089", {})},
        ),
        "PackagesRejectedByLength": (
            "O",
            "ns=1;i=1044",
            {"Weighed": ("V", "ns=1;i=1091", {})},
        ),
        "PackagesRejectedByLowerToleranceLimit1": (
            "O",
            "ns=1;i=1045",
            {"Weighed": ("V", "ns=1;i=1093", {})},
        ),
        "PackagesRejectedByLowerToleranceLimit2": (
            "O",
            "ns=1;i=1046",
            {"Weighed": ("V", "ns=1;i=1095", {})},
        ),
        "PackagesRejectedByMeanValueRequirement": (
            "O",
            "ns=1;i=1047",
            {"Weighed": ("V", "ns=1;i=1097", {})},
        ),
        "PackagesRejectedByMetal": (
            "O",
            "ns=1;i=1048",
            {"Weighed": ("V", "ns=1;i=1099", {})},
        ),
        "PackagesRejectedByVision": (
            "O",
            "ns=1;i=1049",
            {"Weighed": ("V", "ns=1;i=1101", {})},
        ),
        "PackagesRejectedByXRay": (
            "O",
            "ns=1;i=1050",
            {"Weighed": ("V", "ns=1;i=1103", {})},
        ),
        "PercentageLowerToleranceLimit": (
            "V",
            "ns=1;i=1104",
            {"EURange": ("V", "ns=1;i=60094", {})},
        ),
        "PercentageOfTotal": (
            "V",
            "ns=1;i=60197",
            {"EngineeringUnits": ("V", "ns=1;i=60198", {})},
        ),
        "StandardDeviation": (
            "V",
            "ns=1;i=60199",
            {"EngineeringUnits": ("V", "ns=1;i=60200", {})},
        ),
        "SumWeight": (
            "V",
            "ns=1;i=60187",
            {"EngineeringUnits": ("V", "ns=1;i=60188", {})},
        ),
        "Tare": ("V", "ns=1;i=60165", {"EngineeringUnits": ("V", "ns=1;i=60166", {})}),
        "Throughput": (
            "V",
            "ns=1;i=60167",
            {"EngineeringUnits": ("V", "ns=1;i=60168", {})},
        ),
        "TotalPackages": ("O", "ns=1;i=1051", {"Weighed": ("V", "ns=1;i=1110", {})}),
        "TotalPackagesAccepted": (
            "O",
            "ns=1;i=50033",
            {"Weighed": ("V", "ns=1;i=60237", {})},
        ),
        "TotalPackagesRejected": (
            "O",
            "ns=1;i=50034",
            {"Weighed": ("V", "ns=1;i=60239", {})},
        ),
        "TotalPackagesWeighed": (
            "O",
            "ns=1;i=1054",
            {"Weighed": ("V", "ns=1;i=1116", {})},
        ),
        "http://opcfoundation.org/UA/Scales/V2/": (
            "O",
            "ns=1;i=839",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=918", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=919", {}),
                "NamespaceUri": ("V", "ns=1;i=920", {}),
                "NamespaceVersion": ("V", "ns=1;i=921", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=922", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=923", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=924", {}),
            },
        ),
    },
    "objtypes": {
        "FeederModuleType": (
            "OT",
            "ns=1;i=28",
            {
                "FeederLoad": (
                    "V",
                    "ns=1;i=338",
                    {
                        "EURange": ("V", "ns=1;i=341", {}),
                        "EngineeringUnits": ("V", "ns=1;i=340", {}),
                        "ValuePrecision": ("V", "ns=1;i=342", {}),
                    },
                ),
                "FeederRunning": ("V", "ns=1;i=925", {}),
                "FeederSpeed": (
                    "V",
                    "ns=1;i=334",
                    {
                        "EURange": ("V", "ns=1;i=336", {}),
                        "EngineeringUnits": ("V", "ns=1;i=335", {}),
                    },
                ),
                "MachineryBuildingBlocks": ("O", "ns=1;i=50019", {}),
                "MaximumFeederSpeed": (
                    "V",
                    "ns=1;i=60143",
                    {"EngineeringUnits": ("V", "ns=1;i=60159", {})},
                ),
                "MinimalFeederSpeed": (
                    "V",
                    "ns=1;i=60160",
                    {"EngineeringUnits": ("V", "ns=1;i=60161", {})},
                ),
                "SetFeederSpeed": (
                    "M",
                    "ns=1;i=453",
                    {"InputArguments": ("V", "ns=1;i=337", {})},
                ),
            },
        ),
        "MaterialType": (
            "OT",
            "ns=1;i=35",
            {
                "MaterialAutomaticType": (
                    "OT",
                    "ns=1;i=41",
                    {
                        "FillingProductInformation": (
                            "O",
                            "ns=1;i=113",
                            {
                                "FeedRateMeasuringInterval": ("V", "ns=1;i=564", {}),
                                "FillingTime": ("V", "ns=1;i=563", {}),
                                "InFlightWeight": (
                                    "V",
                                    "ns=1;i=556",
                                    {
                                        "Definition": ("V", "ns=1;i=718", {}),
                                        "EURange": ("V", "ns=1;i=559", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=719", {}),
                                        "InstrumentRange": ("V", "ns=1;i=720", {}),
                                        "ValuePrecision": ("V", "ns=1;i=721", {}),
                                    },
                                ),
                                "JogFeed": ("V", "ns=1;i=560", {}),
                                "MinimumDeltaPerFeedRateMeasuringInterval": (
                                    "V",
                                    "ns=1;i=565",
                                    {
                                        "Definition": ("V", "ns=1;i=710", {}),
                                        "EURange": ("V", "ns=1;i=566", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=711", {}),
                                        "InstrumentRange": ("V", "ns=1;i=712", {}),
                                        "ValuePrecision": ("V", "ns=1;i=713", {}),
                                    },
                                ),
                                "ProductId": ("V", "ns=1;i=1385", {}),
                                "ProductName": ("V", "ns=1;i=448", {}),
                                "SettlingTime": ("V", "ns=1;i=561", {}),
                                "Statistic": (
                                    "O",
                                    "ns=1;i=114",
                                    {"StartTime": ("V", "ns=1;i=475", {})},
                                ),
                                "TareId": ("V", "ns=1;i=567", {}),
                                "TargetWeight": (
                                    "V",
                                    "ns=1;i=562",
                                    {
                                        "EURange": ("V", "ns=1;i=569", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=568", {}),
                                        "InstrumentRange": ("V", "ns=1;i=696", {}),
                                    },
                                ),
                            },
                        )
                    },
                ),
                "MaterialId": ("V", "ns=1;i=309", {}),
                "MaterialName": ("V", "ns=1;i=308", {}),
            },
        ),
        "PrinterModuleType": (
            "OT",
            "ns=1;i=29",
            {
                "LabelLength": (
                    "V",
                    "ns=1;i=60056",
                    {"EngineeringUnits": ("V", "ns=1;i=60162", {})},
                ),
                "LabelStock": ("V", "ns=1;i=343", {"EURange": ("V", "ns=1;i=344", {})}),
                "LabelTypeId": ("V", "ns=1;i=351", {}),
                "LabelWidth": (
                    "V",
                    "ns=1;i=60163",
                    {"EngineeringUnits": ("V", "ns=1;i=60164", {})},
                ),
                "MachineryBuildingBlocks": ("O", "ns=1;i=50020", {}),
                "PrintMediaStock": (
                    "V",
                    "ns=1;i=349",
                    {"EURange": ("V", "ns=1;i=350", {})},
                ),
            },
        ),
        "ProductType": (
            "OT",
            "ns=1;i=11",
            {
                "AutomaticFillingProductType": (
                    "OT",
                    "ns=1;i=16",
                    {
                        "FeedRateMeasuringInterval": ("V", "ns=1;i=552", {}),
                        "FillingTime": ("V", "ns=1;i=551", {}),
                        "FineFeedWeight": (
                            "V",
                            "ns=1;i=546",
                            {
                                "Definition": ("V", "ns=1;i=726", {}),
                                "EURange": ("V", "ns=1;i=558", {}),
                                "EngineeringUnits": ("V", "ns=1;i=727", {}),
                                "InstrumentRange": ("V", "ns=1;i=728", {}),
                                "ValuePrecision": ("V", "ns=1;i=729", {}),
                            },
                        ),
                        "InFlightWeight": (
                            "V",
                            "ns=1;i=545",
                            {
                                "Definition": ("V", "ns=1;i=714", {}),
                                "EURange": ("V", "ns=1;i=557", {}),
                                "EngineeringUnits": ("V", "ns=1;i=715", {}),
                                "InstrumentRange": ("V", "ns=1;i=716", {}),
                                "ValuePrecision": ("V", "ns=1;i=717", {}),
                            },
                        ),
                        "JogFeed": ("V", "ns=1;i=549", {}),
                        "MinimumDeltaPerFeedRateMeasuringInterval": (
                            "V",
                            "ns=1;i=553",
                            {
                                "Definition": ("V", "ns=1;i=706", {}),
                                "EURange": ("V", "ns=1;i=554", {}),
                                "EngineeringUnits": ("V", "ns=1;i=707", {}),
                                "InstrumentRange": ("V", "ns=1;i=708", {}),
                                "ValuePrecision": ("V", "ns=1;i=709", {}),
                            },
                        ),
                        "SettlingTime": ("V", "ns=1;i=547", {}),
                        "TareId": ("V", "ns=1;i=555", {}),
                        "TargetWeight": (
                            "V",
                            "ns=1;i=544",
                            {
                                "EURange": ("V", "ns=1;i=550", {}),
                                "EngineeringUnits": ("V", "ns=1;i=548", {}),
                                "InstrumentRange": ("V", "ns=1;i=691", {}),
                            },
                        ),
                    },
                ),
                "BatchId": ("V", "ns=1;i=648", {}),
                "BatchName": ("V", "ns=1;i=649", {}),
                "CatchweigherProductType": (
                    "OT",
                    "ns=1;i=17",
                    {
                        "<Zones>": (
                            "O",
                            "ns=1;i=68",
                            {
                                "LowerLimit": (
                                    "V",
                                    "ns=1;i=60205",
                                    {"EngineeringUnits": ("V", "ns=1;i=60206", {})},
                                ),
                                "Name": ("V", "ns=1;i=137", {}),
                                "UpperLimit": (
                                    "V",
                                    "ns=1;i=60207",
                                    {"EngineeringUnits": ("V", "ns=1;i=60208", {})},
                                ),
                                "ZoneStatistic": (
                                    "O",
                                    "ns=1;i=96",
                                    {"Weighed": ("V", "ns=1;i=768", {})},
                                ),
                            },
                        ),
                        "AddZone": (
                            "M",
                            "ns=1;i=525",
                            {
                                "InputArguments": ("V", "ns=1;i=145", {}),
                                "OutputArguments": ("V", "ns=1;i=146", {}),
                            },
                        ),
                        "AutomaticWeightPriceLabelerProductType": (
                            "OT",
                            "ns=1;i=47",
                            {
                                "LastItem": (
                                    "O",
                                    "ns=1;i=836",
                                    {
                                        "MeasuredWeight": (
                                            "V",
                                            "ns=1;i=902",
                                            {
                                                "CenterOfZero": ("V", "ns=1;i=901", {}),
                                                "EURange": ("V", "ns=1;i=904", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=903",
                                                    {},
                                                ),
                                                "GrossNegative": (
                                                    "V",
                                                    "ns=1;i=911",
                                                    {},
                                                ),
                                                "HighResolutionValue": (
                                                    "V",
                                                    "ns=1;i=912",
                                                    {},
                                                ),
                                                "InsideZero": ("V", "ns=1;i=905", {}),
                                                "Overload": ("V", "ns=1;i=907", {}),
                                                "PrintableValue": (
                                                    "V",
                                                    "ns=1;i=913",
                                                    {},
                                                ),
                                                "TareMode": ("V", "ns=1;i=908", {}),
                                                "Underload": ("V", "ns=1;i=909", {}),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=914",
                                                    {},
                                                ),
                                                "WeightId": ("V", "ns=1;i=915", {}),
                                                "WeightStable": ("V", "ns=1;i=910", {}),
                                            },
                                        )
                                    },
                                ),
                                "UnitPrice": (
                                    "V",
                                    "ns=1;i=1357",
                                    {"CurrencyUnit": ("V", "ns=1;i=1211", {})},
                                ),
                            },
                        ),
                        "CheckweigherProductType": (
                            "OT",
                            "ns=1;i=46",
                            {
                                "LowerToleranceLimit1": (
                                    "V",
                                    "ns=1;i=60138",
                                    {"EngineeringUnits": ("V", "ns=1;i=60139", {})},
                                ),
                                "LowerToleranceLimit2": (
                                    "V",
                                    "ns=1;i=60140",
                                    {"EngineeringUnits": ("V", "ns=1;i=60141", {})},
                                ),
                                "NominalWeight": (
                                    "V",
                                    "ns=1;i=378",
                                    {
                                        "EURange": ("V", "ns=1;i=380", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=379", {}),
                                    },
                                ),
                                "Statistic": (
                                    "O",
                                    "ns=1;i=71",
                                    {
                                        "ResetCondition": ("V", "ns=1;i=1075", {}),
                                        "StartTime": ("V", "ns=1;i=1076", {}),
                                    },
                                ),
                            },
                        ),
                        "LastItem": (
                            "O",
                            "ns=1;i=87",
                            {
                                "MeasuredWeight": (
                                    "V",
                                    "ns=1;i=495",
                                    {
                                        "CenterOfZero": ("V", "ns=1;i=496", {}),
                                        "EURange": ("V", "ns=1;i=498", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=497", {}),
                                        "GrossNegative": ("V", "ns=1;i=499", {}),
                                        "HighResolutionValue": ("V", "ns=1;i=500", {}),
                                        "InsideZero": ("V", "ns=1;i=501", {}),
                                        "Overload": ("V", "ns=1;i=503", {}),
                                        "PrintableValue": ("V", "ns=1;i=504", {}),
                                        "TareMode": ("V", "ns=1;i=505", {}),
                                        "Underload": ("V", "ns=1;i=506", {}),
                                        "ValuePrecision": ("V", "ns=1;i=508", {}),
                                        "WeightId": ("V", "ns=1;i=509", {}),
                                        "WeightStable": ("V", "ns=1;i=510", {}),
                                    },
                                )
                            },
                        ),
                        "PresetHeight": (
                            "V",
                            "ns=1;i=60171",
                            {"EngineeringUnits": ("V", "ns=1;i=60172", {})},
                        ),
                        "PresetLength": (
                            "V",
                            "ns=1;i=60173",
                            {"EngineeringUnits": ("V", "ns=1;i=60174", {})},
                        ),
                        "PresetWidth": (
                            "V",
                            "ns=1;i=60175",
                            {"EngineeringUnits": ("V", "ns=1;i=60176", {})},
                        ),
                        "RemoveZone": (
                            "M",
                            "ns=1;i=526",
                            {"InputArguments": ("V", "ns=1;i=147", {})},
                        ),
                        "TargetThroughput": (
                            "V",
                            "ns=1;i=472",
                            {
                                "EURange": ("V", "ns=1;i=474", {}),
                                "EngineeringUnits": ("V", "ns=1;i=473", {}),
                            },
                        ),
                    },
                ),
                "ContinuousProductType": (
                    "OT",
                    "ns=1;i=18",
                    {
                        "MaterialDensity": (
                            "V",
                            "ns=1;i=60217",
                            {"EngineeringUnits": ("V", "ns=1;i=60218", {})},
                        ),
                        "TargetFlowRate": (
                            "V",
                            "ns=1;i=235",
                            {
                                "EURange": ("V", "ns=1;i=237", {}),
                                "EngineeringUnits": ("V", "ns=1;i=236", {}),
                                "ValuePrecision": ("V", "ns=1;i=673", {}),
                            },
                        ),
                        "TargetWeight": (
                            "V",
                            "ns=1;i=531",
                            {
                                "EURange": ("V", "ns=1;i=533", {}),
                                "EngineeringUnits": ("V", "ns=1;i=532", {}),
                                "ValuePrecision": ("V", "ns=1;i=663", {}),
                            },
                        ),
                    },
                ),
                "JobId": ("V", "ns=1;i=185", {}),
                "JobName": ("V", "ns=1;i=310", {}),
                "Lock": (
                    "O",
                    "ns=1;i=1181",
                    {
                        "BreakLock": (
                            "M",
                            "ns=1;i=1410",
                            {"OutputArguments": ("V", "ns=1;i=1375", {})},
                        ),
                        "ExitLock": (
                            "M",
                            "ns=1;i=1411",
                            {"OutputArguments": ("V", "ns=1;i=1376", {})},
                        ),
                        "InitLock": (
                            "M",
                            "ns=1;i=1412",
                            {
                                "InputArguments": ("V", "ns=1;i=1377", {}),
                                "OutputArguments": ("V", "ns=1;i=1378", {}),
                            },
                        ),
                        "Locked": ("V", "ns=1;i=1379", {}),
                        "LockingClient": ("V", "ns=1;i=1380", {}),
                        "LockingUser": ("V", "ns=1;i=1381", {}),
                        "RemainingLockTime": ("V", "ns=1;i=1382", {}),
                        "RenewLock": (
                            "M",
                            "ns=1;i=1413",
                            {"OutputArguments": ("V", "ns=1;i=1383", {})},
                        ),
                    },
                ),
                "PieceCountingProductType": (
                    "OT",
                    "ns=1;i=12",
                    {
                        "CurrentItemCount": ("V", "ns=1;i=261", {}),
                        "FeedRateMeasuringInterval": ("V", "ns=1;i=597", {}),
                        "FillingTime": ("V", "ns=1;i=274", {}),
                        "FineFeedCount": ("V", "ns=1;i=376", {}),
                        "InFlightCount": ("V", "ns=1;i=578", {}),
                        "JogFeed": ("V", "ns=1;i=589", {}),
                        "MinimumDeltaPerFeedRateMeasuringInterval": (
                            "V",
                            "ns=1;i=590",
                            {
                                "EURange": ("V", "ns=1;i=591", {}),
                                "EngineeringUnits": ("V", "ns=1;i=656", {}),
                                "InstrumentRange": ("V", "ns=1;i=657", {}),
                                "ValuePrecision": ("V", "ns=1;i=658", {}),
                            },
                        ),
                        "NumberOfReferencePieces": ("V", "ns=1;i=167", {}),
                        "ReferencePieceWeight": (
                            "V",
                            "ns=1;i=173",
                            {
                                "EURange": ("V", "ns=1;i=174", {}),
                                "EngineeringUnits": ("V", "ns=1;i=650", {}),
                                "InstrumentRange": ("V", "ns=1;i=651", {}),
                                "ValuePrecision": ("V", "ns=1;i=652", {}),
                            },
                        ),
                        "RegisteredPieceCount": ("V", "ns=1;i=579", {}),
                        "SetTargetItemCount": (
                            "M",
                            "ns=1;i=460",
                            {"InputArguments": ("V", "ns=1;i=398", {})},
                        ),
                        "SetTargetPieceCount": (
                            "M",
                            "ns=1;i=577",
                            {"InputArguments": ("V", "ns=1;i=184", {})},
                        ),
                        "SettlingTime": ("V", "ns=1;i=580", {}),
                        "TareId": ("V", "ns=1;i=592", {}),
                        "TargetItemCount": ("V", "ns=1;i=587", {}),
                        "TargetPieceCount": (
                            "V",
                            "ns=1;i=178",
                            {
                                "EURange": ("V", "ns=1;i=183", {}),
                                "EngineeringUnits": ("V", "ns=1;i=179", {}),
                                "InstrumentRange": ("V", "ns=1;i=641", {}),
                            },
                        ),
                        "TotalizedItemCount": ("V", "ns=1;i=581", {}),
                        "TotalizedWeight": (
                            "V",
                            "ns=1;i=582",
                            {
                                "CenterOfZero": ("V", "ns=1;i=583", {}),
                                "EURange": ("V", "ns=1;i=593", {}),
                                "EngineeringUnits": ("V", "ns=1;i=588", {}),
                                "GrossNegative": ("V", "ns=1;i=584", {}),
                                "HighResolutionValue": ("V", "ns=1;i=780", {}),
                                "InsideZero": ("V", "ns=1;i=225", {}),
                                "Overload": ("V", "ns=1;i=223", {}),
                                "PrintableValue": ("V", "ns=1;i=779", {}),
                                "TareMode": ("V", "ns=1;i=585", {}),
                                "Underload": ("V", "ns=1;i=224", {}),
                                "ValuePrecision": ("V", "ns=1;i=594", {}),
                                "WeightId": ("V", "ns=1;i=640", {}),
                                "WeightStable": ("V", "ns=1;i=586", {}),
                            },
                        ),
                    },
                ),
                "PresetTare": (
                    "V",
                    "ns=1;i=60169",
                    {"EngineeringUnits": ("V", "ns=1;i=60170", {})},
                ),
                "ProductId": ("V", "ns=1;i=963", {}),
                "ProductMode": (
                    "V",
                    "ns=1;i=360",
                    {
                        "FalseState": ("V", "ns=1;i=361", {}),
                        "TrueState": ("V", "ns=1;i=362", {}),
                    },
                ),
                "ProductName": ("V", "ns=1;i=166", {}),
                "RecipeProductType": (
                    "OT",
                    "ns=1;i=19",
                    {
                        "RecipeNodeId": ("V", "ns=1;i=633", {}),
                        "Report": ("V", "ns=1;i=632", {}),
                        "ReportFile": (
                            "O",
                            "ns=1;i=131",
                            {
                                "Close": (
                                    "M",
                                    "ns=1;i=613",
                                    {"InputArguments": ("V", "ns=1;i=614", {})},
                                ),
                                "GetPosition": (
                                    "M",
                                    "ns=1;i=615",
                                    {
                                        "InputArguments": ("V", "ns=1;i=616", {}),
                                        "OutputArguments": ("V", "ns=1;i=617", {}),
                                    },
                                ),
                                "Open": (
                                    "M",
                                    "ns=1;i=618",
                                    {
                                        "InputArguments": ("V", "ns=1;i=619", {}),
                                        "OutputArguments": ("V", "ns=1;i=620", {}),
                                    },
                                ),
                                "OpenCount": ("V", "ns=1;i=621", {}),
                                "Read": (
                                    "M",
                                    "ns=1;i=622",
                                    {
                                        "InputArguments": ("V", "ns=1;i=623", {}),
                                        "OutputArguments": ("V", "ns=1;i=624", {}),
                                    },
                                ),
                                "SetPosition": (
                                    "M",
                                    "ns=1;i=625",
                                    {"InputArguments": ("V", "ns=1;i=626", {})},
                                ),
                                "Size": ("V", "ns=1;i=627", {}),
                                "UserWritable": ("V", "ns=1;i=628", {}),
                                "Writable": ("V", "ns=1;i=629", {}),
                                "Write": (
                                    "M",
                                    "ns=1;i=630",
                                    {"InputArguments": ("V", "ns=1;i=631", {})},
                                ),
                            },
                        ),
                    },
                ),
                "SimpleProductType": (
                    "OT",
                    "ns=1;i=20",
                    {
                        "ContainerId": ("V", "ns=1;i=1012", {}),
                        "UnitPrice": (
                            "V",
                            "ns=1;i=1318",
                            {"CurrencyUnit": ("V", "ns=1;i=1356", {})},
                        ),
                    },
                ),
                "Statistic": ("O", "ns=1;i=95", {"StartTime": ("V", "ns=1;i=444", {})}),
                "TotalizingHopperProductType": (
                    "OT",
                    "ns=1;i=22",
                    {
                        "TipCounter": ("V", "ns=1;i=637", {}),
                        "VolumeTargetValue": (
                            "V",
                            "ns=1;i=634",
                            {
                                "EURange": ("V", "ns=1;i=636", {}),
                                "EngineeringUnits": ("V", "ns=1;i=635", {}),
                            },
                        ),
                    },
                ),
                "VehicleProductType": (
                    "OT",
                    "ns=1;i=832",
                    {
                        "CarrierDisplayName": ("V", "ns=1;i=858", {}),
                        "CarrierId": ("V", "ns=1;i=859", {}),
                        "Customer": ("V", "ns=1;i=860", {}),
                        "DeltaWeight": (
                            "V",
                            "ns=1;i=861",
                            {
                                "EURange": ("V", "ns=1;i=869", {}),
                                "EngineeringUnits": ("V", "ns=1;i=868", {}),
                                "InsideZero": ("V", "ns=1;i=862", {}),
                                "IsFilling": ("V", "ns=1;i=899", {}),
                                "Overload": ("V", "ns=1;i=864", {}),
                                "TareMode": ("V", "ns=1;i=865", {}),
                                "Underload": ("V", "ns=1;i=866", {}),
                                "WeightStable": ("V", "ns=1;i=867", {}),
                            },
                        ),
                        "Destination": ("V", "ns=1;i=870", {}),
                        "DriverDisplayName": ("V", "ns=1;i=871", {}),
                        "DriverId": ("V", "ns=1;i=872", {}),
                        "GetVehicleInformation": (
                            "M",
                            "ns=1;i=1396",
                            {"InputArguments": ("V", "ns=1;i=1208", {})},
                        ),
                        "InboundScale": ("V", "ns=1;i=874", {}),
                        "InboundWeight": (
                            "V",
                            "ns=1;i=887",
                            {
                                "EURange": ("V", "ns=1;i=895", {}),
                                "EngineeringUnits": ("V", "ns=1;i=894", {}),
                                "InsideZero": ("V", "ns=1;i=888", {}),
                                "Overload": ("V", "ns=1;i=890", {}),
                                "TareMode": ("V", "ns=1;i=891", {}),
                                "Underload": ("V", "ns=1;i=892", {}),
                                "WeightStable": ("V", "ns=1;i=893", {}),
                            },
                        ),
                        "Material": (
                            "O",
                            "ns=1;i=835",
                            {
                                "MaterialId": ("V", "ns=1;i=875", {}),
                                "MaterialName": ("V", "ns=1;i=876", {}),
                            },
                        ),
                        "OutboundScale": ("V", "ns=1;i=877", {}),
                        "OutboundWeight": (
                            "V",
                            "ns=1;i=878",
                            {
                                "EURange": ("V", "ns=1;i=886", {}),
                                "EngineeringUnits": ("V", "ns=1;i=885", {}),
                                "InsideZero": ("V", "ns=1;i=879", {}),
                                "Overload": ("V", "ns=1;i=881", {}),
                                "TareMode": ("V", "ns=1;i=882", {}),
                                "Underload": ("V", "ns=1;i=883", {}),
                                "WeightStable": ("V", "ns=1;i=884", {}),
                            },
                        ),
                        "ScaleOperatorId": ("V", "ns=1;i=896", {}),
                        "Supplier": ("V", "ns=1;i=897", {}),
                        "Tare": ("V", "ns=1;i=1117", {}),
                        "TareExpirationDate": ("V", "ns=1;i=898", {}),
                        "TotalWeight": ("V", "ns=1;i=1210", {}),
                        "TotalWeightResetDate": ("V", "ns=1;i=873", {}),
                        "VehicleId": ("V", "ns=1;i=900", {}),
                    },
                ),
            },
        ),
        "ProductionPresetType": (
            "OT",
            "ns=1;i=14",
            {
                "AddProduct": (
                    "M",
                    "ns=1;i=638",
                    {
                        "InputArguments": ("V", "ns=1;i=246", {}),
                        "OutputArguments": ("V", "ns=1;i=177", {}),
                    },
                ),
                "CurrentProducts": ("V", "ns=1;i=436", {}),
                "DeselectProduct": (
                    "M",
                    "ns=1;i=576",
                    {"InputArguments": ("V", "ns=1;i=176", {})},
                ),
                "Products": (
                    "O",
                    "ns=1;i=75",
                    {
                        "<Product>": (
                            "O",
                            "ns=1;i=92",
                            {
                                "ProductId": ("V", "ns=1;i=1384", {}),
                                "ProductName": ("V", "ns=1;i=414", {}),
                                "Statistic": (
                                    "O",
                                    "ns=1;i=93",
                                    {"StartTime": ("V", "ns=1;i=60074", {})},
                                ),
                            },
                        )
                    },
                ),
                "RemoveProduct": (
                    "M",
                    "ns=1;i=646",
                    {"InputArguments": ("V", "ns=1;i=647", {})},
                ),
                "SelectProduct": (
                    "M",
                    "ns=1;i=464",
                    {"InputArguments": ("V", "ns=1;i=175", {})},
                ),
                "SwitchProduct": (
                    "M",
                    "ns=1;i=1021",
                    {"InputArguments": ("V", "ns=1;i=988", {})},
                ),
            },
        ),
        "RecipeElementType": (
            "OT",
            "ns=1;i=32",
            {
                "ActivationType": (
                    "OT",
                    "ns=1;i=40",
                    {
                        "TargetValue": (
                            "V",
                            "ns=1;i=60219",
                            {"EngineeringUnits": ("V", "ns=1;i=60220", {})},
                        ),
                        "TargetValueId": ("V", "ns=1;i=306", {}),
                        "TargetValueNodeId": ("V", "ns=1;i=307", {}),
                    },
                ),
                "ConditionSleepType": (
                    "OT",
                    "ns=1;i=37",
                    {
                        "AnalogConditionSleepType": (
                            "OT",
                            "ns=1;i=38",
                            {
                                "ConditionMode": ("V", "ns=1;i=302", {}),
                                "TargetThresholdValue": (
                                    "V",
                                    "ns=1;i=300",
                                    {
                                        "AllowedEngineeringUnits": (
                                            "V",
                                            "ns=1;i=800",
                                            {},
                                        ),
                                        "EURange": ("V", "ns=1;i=435", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=434", {}),
                                    },
                                ),
                            },
                        ),
                        "EdgeTriggeredSleepType": (
                            "OT",
                            "ns=1;i=39",
                            {
                                "ConditionMode": ("V", "ns=1;i=303", {}),
                                "TargetThresholdValue": ("V", "ns=1;i=301", {}),
                            },
                        ),
                        "TargetThresholdValue": ("V", "ns=1;i=299", {}),
                        "ThresholdValueId": ("V", "ns=1;i=943", {}),
                        "ThresholdValueNodeId": ("V", "ns=1;i=60240", {}),
                        "Timeout": ("V", "ns=1;i=945", {}),
                    },
                ),
                "TimerType": ("OT", "ns=1;i=36", {"Duration": ("V", "ns=1;i=298", {})}),
                "UserInstructionType": (
                    "OT",
                    "ns=1;i=33",
                    {
                        "DisplayText": ("V", "ns=1;i=292", {}),
                        "InstructionId": ("V", "ns=1;i=293", {}),
                    },
                ),
                "WeighingType": (
                    "OT",
                    "ns=1;i=34",
                    {
                        "Material": (
                            "O",
                            "ns=1;i=86",
                            {
                                "MaterialId": ("V", "ns=1;i=259", {}),
                                "MaterialName": ("V", "ns=1;i=260", {}),
                            },
                        ),
                        "TargetWeight": (
                            "V",
                            "ns=1;i=294",
                            {
                                "EURange": ("V", "ns=1;i=296", {}),
                                "EngineeringUnits": ("V", "ns=1;i=295", {}),
                                "ValuePrecision": ("V", "ns=1;i=411", {}),
                            },
                        ),
                        "WeighingModuleNodeId": ("V", "ns=1;i=297", {}),
                    },
                ),
            },
        ),
        "RecipeManagementType": (
            "OT",
            "ns=1;i=30",
            {
                "<Recipe_No>": (
                    "O",
                    "ns=1;i=112",
                    {
                        "AddRecipeElement": (
                            "M",
                            "ns=1;i=469",
                            {
                                "InputArguments": ("V", "ns=1;i=443", {}),
                                "OutputArguments": ("V", "ns=1;i=445", {}),
                            },
                        ),
                        "RecipeElements": ("O", "ns=1;i=84", {}),
                        "RecipeId": ("V", "ns=1;i=290", {}),
                        "RecipeName": ("V", "ns=1;i=289", {}),
                        "RemoveRecipeElement": (
                            "M",
                            "ns=1;i=470",
                            {"InputArguments": ("V", "ns=1;i=446", {})},
                        ),
                    },
                ),
                "AddRecipe": (
                    "M",
                    "ns=1;i=456",
                    {
                        "InputArguments": ("V", "ns=1;i=181", {}),
                        "OutputArguments": ("V", "ns=1;i=182", {}),
                    },
                ),
                "RemoveRecipe": (
                    "M",
                    "ns=1;i=459",
                    {"InputArguments": ("V", "ns=1;i=180", {})},
                ),
            },
        ),
        "RecipeType": (
            "OT",
            "ns=1;i=31",
            {
                "AddRecipeElement": (
                    "M",
                    "ns=1;i=465",
                    {
                        "InputArguments": ("V", "ns=1;i=437", {}),
                        "OutputArguments": ("V", "ns=1;i=438", {}),
                    },
                ),
                "RecipeElements": ("O", "ns=1;i=82", {}),
                "RecipeFile": (
                    "O",
                    "ns=1;i=50006",
                    {
                        "Close": (
                            "M",
                            "ns=1;i=70004",
                            {"InputArguments": ("V", "ns=1;i=60035", {})},
                        ),
                        "GetPosition": (
                            "M",
                            "ns=1;i=70005",
                            {
                                "InputArguments": ("V", "ns=1;i=60036", {}),
                                "OutputArguments": ("V", "ns=1;i=60037", {}),
                            },
                        ),
                        "Open": (
                            "M",
                            "ns=1;i=70006",
                            {
                                "InputArguments": ("V", "ns=1;i=60038", {}),
                                "OutputArguments": ("V", "ns=1;i=60039", {}),
                            },
                        ),
                        "OpenCount": ("V", "ns=1;i=60040", {}),
                        "Read": (
                            "M",
                            "ns=1;i=70007",
                            {
                                "InputArguments": ("V", "ns=1;i=60041", {}),
                                "OutputArguments": ("V", "ns=1;i=60042", {}),
                            },
                        ),
                        "SetPosition": (
                            "M",
                            "ns=1;i=70008",
                            {"InputArguments": ("V", "ns=1;i=60043", {})},
                        ),
                        "Size": ("V", "ns=1;i=60044", {}),
                        "UserWritable": ("V", "ns=1;i=60045", {}),
                        "Writable": ("V", "ns=1;i=60046", {}),
                        "Write": (
                            "M",
                            "ns=1;i=70009",
                            {"InputArguments": ("V", "ns=1;i=60047", {})},
                        ),
                    },
                ),
                "RecipeId": ("V", "ns=1;i=288", {}),
                "RecipeName": ("V", "ns=1;i=287", {}),
                "RemoveRecipeElement": (
                    "M",
                    "ns=1;i=466",
                    {"InputArguments": ("V", "ns=1;i=439", {})},
                ),
            },
        ),
        "ScaleAlarmType": (
            "OT",
            "ns=1;i=21",
            {
                "AuxParameters": ("V", "ns=1;i=763", {}),
                "HelpSource": ("V", "ns=1;i=764", {}),
                "NotificationCategory": (
                    "V",
                    "ns=1;i=328",
                    {
                        "EnumValues": ("V", "ns=1;i=330", {}),
                        "ValueAsText": ("V", "ns=1;i=339", {}),
                    },
                ),
                "NotificationId": (
                    "V",
                    "ns=1;i=353",
                    {
                        "EnumValues": ("V", "ns=1;i=358", {}),
                        "ValueAsText": ("V", "ns=1;i=359", {}),
                    },
                ),
                "VendorNotificationId": ("V", "ns=1;i=1020", {}),
            },
        ),
        "ScaleDeviceType": (
            "OT",
            "ns=1;i=2",
            {
                "<ListOfWeighingRanges>": (
                    "O",
                    "ns=1;i=94",
                    {
                        "ActualScaleInterval": (
                            "V",
                            "ns=1;i=1229",
                            {"EngineeringUnits": ("V", "ns=1;i=1230", {})},
                        ),
                        "Range": (
                            "V",
                            "ns=1;i=926",
                            {"EngineeringUnits": ("V", "ns=1;i=1369", {})},
                        ),
                        "VerificationScaleInterval": (
                            "V",
                            "ns=1;i=1231",
                            {"EngineeringUnits": ("V", "ns=1;i=1232", {})},
                        ),
                    },
                ),
                "AllowedEngineeringUnits": ("V", "ns=1;i=989", {}),
                "AutomaticFillingScaleType": (
                    "OT",
                    "ns=1;i=5",
                    {
                        "Deviation": (
                            "V",
                            "ns=1;i=60189",
                            {"EngineeringUnits": ("V", "ns=1;i=60190", {})},
                        ),
                        "ProductionPreset": (
                            "O",
                            "ns=1;i=848",
                            {
                                "Products": (
                                    "O",
                                    "ns=1;i=121",
                                    {
                                        "<Product>": (
                                            "O",
                                            "ns=1;i=122",
                                            {
                                                "FeedRateMeasuringInterval": (
                                                    "V",
                                                    "ns=1;i=1212",
                                                    {},
                                                ),
                                                "FillingTime": ("V", "ns=1;i=1213", {}),
                                                "FineFeedWeight": (
                                                    "V",
                                                    "ns=1;i=1214",
                                                    {
                                                        "Definition": (
                                                            "V",
                                                            "ns=1;i=1215",
                                                            {},
                                                        ),
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=1217",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=1216",
                                                            {},
                                                        ),
                                                        "InstrumentRange": (
                                                            "V",
                                                            "ns=1;i=1218",
                                                            {},
                                                        ),
                                                        "ValuePrecision": (
                                                            "V",
                                                            "ns=1;i=1219",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "InFlightWeight": (
                                                    "V",
                                                    "ns=1;i=570",
                                                    {
                                                        "Definition": (
                                                            "V",
                                                            "ns=1;i=722",
                                                            {},
                                                        ),
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=571",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=723",
                                                            {},
                                                        ),
                                                        "InstrumentRange": (
                                                            "V",
                                                            "ns=1;i=724",
                                                            {},
                                                        ),
                                                        "ValuePrecision": (
                                                            "V",
                                                            "ns=1;i=725",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "JogFeed": ("V", "ns=1;i=1220", {}),
                                                "MinimumDeltaPerFeedRateMeasuringInterval": (
                                                    "V",
                                                    "ns=1;i=1221",
                                                    {
                                                        "Definition": (
                                                            "V",
                                                            "ns=1;i=1222",
                                                            {},
                                                        ),
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=1224",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=1223",
                                                            {},
                                                        ),
                                                        "InstrumentRange": (
                                                            "V",
                                                            "ns=1;i=1225",
                                                            {},
                                                        ),
                                                        "ValuePrecision": (
                                                            "V",
                                                            "ns=1;i=1226",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "ProductId": ("V", "ns=1;i=1386", {}),
                                                "ProductName": ("V", "ns=1;i=507", {}),
                                                "SettlingTime": (
                                                    "V",
                                                    "ns=1;i=1227",
                                                    {},
                                                ),
                                                "Statistic": (
                                                    "O",
                                                    "ns=1;i=123",
                                                    {
                                                        "StartTime": (
                                                            "V",
                                                            "ns=1;i=60077",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "TareId": ("V", "ns=1;i=1228", {}),
                                                "TargetWeight": (
                                                    "V",
                                                    "ns=1;i=572",
                                                    {
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=574",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=573",
                                                            {},
                                                        ),
                                                        "InstrumentRange": (
                                                            "V",
                                                            "ns=1;i=701",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                            },
                                        )
                                    },
                                )
                            },
                        ),
                        "ToleranceState": ("V", "ns=1;i=543", {}),
                    },
                ),
                "CatchweigherType": (
                    "OT",
                    "ns=1;i=4",
                    {
                        "AutomaticWeightPriceLabelerType": (
                            "OT",
                            "ns=1;i=49",
                            {
                                "ProductionPreset": (
                                    "O",
                                    "ns=1;i=851",
                                    {
                                        "Products": (
                                            "O",
                                            "ns=1;i=116",
                                            {
                                                "<Product>": (
                                                    "O",
                                                    "ns=1;i=117",
                                                    {
                                                        "LastItem": (
                                                            "O",
                                                            "ns=1;i=1417",
                                                            {
                                                                "MeasuredWeight": (
                                                                    "V",
                                                                    "ns=1;i=1449",
                                                                    {
                                                                        "CenterOfZero": (
                                                                            "V",
                                                                            "ns=1;i=1450",
                                                                            {},
                                                                        ),
                                                                        "EURange": (
                                                                            "V",
                                                                            "ns=1;i=1452",
                                                                            {},
                                                                        ),
                                                                        "EngineeringUnits": (
                                                                            "V",
                                                                            "ns=1;i=1451",
                                                                            {},
                                                                        ),
                                                                        "GrossNegative": (
                                                                            "V",
                                                                            "ns=1;i=1453",
                                                                            {},
                                                                        ),
                                                                        "HighResolutionValue": (
                                                                            "V",
                                                                            "ns=1;i=1454",
                                                                            {},
                                                                        ),
                                                                        "InsideZero": (
                                                                            "V",
                                                                            "ns=1;i=1455",
                                                                            {},
                                                                        ),
                                                                        "Overload": (
                                                                            "V",
                                                                            "ns=1;i=1457",
                                                                            {},
                                                                        ),
                                                                        "PrintableValue": (
                                                                            "V",
                                                                            "ns=1;i=1458",
                                                                            {},
                                                                        ),
                                                                        "TareMode": (
                                                                            "V",
                                                                            "ns=1;i=1459",
                                                                            {},
                                                                        ),
                                                                        "Underload": (
                                                                            "V",
                                                                            "ns=1;i=1460",
                                                                            {},
                                                                        ),
                                                                        "ValuePrecision": (
                                                                            "V",
                                                                            "ns=1;i=1461",
                                                                            {},
                                                                        ),
                                                                        "WeightId": (
                                                                            "V",
                                                                            "ns=1;i=1462",
                                                                            {},
                                                                        ),
                                                                        "WeightStable": (
                                                                            "V",
                                                                            "ns=1;i=1463",
                                                                            {},
                                                                        ),
                                                                    },
                                                                )
                                                            },
                                                        ),
                                                        "ProductId": (
                                                            "V",
                                                            "ns=1;i=1446",
                                                            {},
                                                        ),
                                                        "ProductName": (
                                                            "V",
                                                            "ns=1;i=1447",
                                                            {},
                                                        ),
                                                        "Statistic": (
                                                            "O",
                                                            "ns=1;i=1416",
                                                            {
                                                                "StartTime": (
                                                                    "V",
                                                                    "ns=1;i=60075",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "UnitPrice": (
                                                            "V",
                                                            "ns=1;i=1464",
                                                            {
                                                                "CurrencyUnit": (
                                                                    "V",
                                                                    "ns=1;i=1465",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                    },
                                                )
                                            },
                                        )
                                    },
                                )
                            },
                        ),
                        "CheckweigherType": (
                            "OT",
                            "ns=1;i=45",
                            {
                                "ProductionPreset": (
                                    "O",
                                    "ns=1;i=850",
                                    {
                                        "Products": (
                                            "O",
                                            "ns=1;i=91",
                                            {
                                                "<Product>": (
                                                    "O",
                                                    "ns=1;i=846",
                                                    {
                                                        "<Zones>": (
                                                            "O",
                                                            "ns=1;i=847",
                                                            {
                                                                "LowerLimit": (
                                                                    "V",
                                                                    "ns=1;i=60209",
                                                                    {
                                                                        "EngineeringUnits": (
                                                                            "V",
                                                                            "ns=1;i=60210",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                                "Name": (
                                                                    "V",
                                                                    "ns=1;i=937",
                                                                    {},
                                                                ),
                                                                "UpperLimit": (
                                                                    "V",
                                                                    "ns=1;i=60211",
                                                                    {
                                                                        "EngineeringUnits": (
                                                                            "V",
                                                                            "ns=1;i=60212",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                            },
                                                        ),
                                                        "AddZone": (
                                                            "M",
                                                            "ns=1;i=831",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "ns=1;i=805",
                                                                    {},
                                                                ),
                                                                "OutputArguments": (
                                                                    "V",
                                                                    "ns=1;i=806",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                        "LastItem": (
                                                            "O",
                                                            "ns=1;i=801",
                                                            {
                                                                "MeasuredWeight": (
                                                                    "V",
                                                                    "ns=1;i=807",
                                                                    {
                                                                        "CenterOfZero": (
                                                                            "V",
                                                                            "ns=1;i=825",
                                                                            {},
                                                                        ),
                                                                        "EURange": (
                                                                            "V",
                                                                            "ns=1;i=809",
                                                                            {},
                                                                        ),
                                                                        "EngineeringUnits": (
                                                                            "V",
                                                                            "ns=1;i=808",
                                                                            {},
                                                                        ),
                                                                        "GrossNegative": (
                                                                            "V",
                                                                            "ns=1;i=826",
                                                                            {},
                                                                        ),
                                                                        "HighResolutionValue": (
                                                                            "V",
                                                                            "ns=1;i=827",
                                                                            {},
                                                                        ),
                                                                        "InsideZero": (
                                                                            "V",
                                                                            "ns=1;i=810",
                                                                            {},
                                                                        ),
                                                                        "Overload": (
                                                                            "V",
                                                                            "ns=1;i=812",
                                                                            {},
                                                                        ),
                                                                        "PrintableValue": (
                                                                            "V",
                                                                            "ns=1;i=828",
                                                                            {},
                                                                        ),
                                                                        "TareMode": (
                                                                            "V",
                                                                            "ns=1;i=813",
                                                                            {},
                                                                        ),
                                                                        "Underload": (
                                                                            "V",
                                                                            "ns=1;i=814",
                                                                            {},
                                                                        ),
                                                                        "ValuePrecision": (
                                                                            "V",
                                                                            "ns=1;i=829",
                                                                            {},
                                                                        ),
                                                                        "WeightId": (
                                                                            "V",
                                                                            "ns=1;i=830",
                                                                            {},
                                                                        ),
                                                                        "WeightStable": (
                                                                            "V",
                                                                            "ns=1;i=815",
                                                                            {},
                                                                        ),
                                                                    },
                                                                )
                                                            },
                                                        ),
                                                        "NominalWeight": (
                                                            "V",
                                                            "ns=1;i=940",
                                                            {
                                                                "EURange": (
                                                                    "V",
                                                                    "ns=1;i=942",
                                                                    {},
                                                                ),
                                                                "EngineeringUnits": (
                                                                    "V",
                                                                    "ns=1;i=941",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                        "ProductId": (
                                                            "V",
                                                            "ns=1;i=1007",
                                                            {},
                                                        ),
                                                        "ProductName": (
                                                            "V",
                                                            "ns=1;i=1008",
                                                            {},
                                                        ),
                                                        "Statistic": (
                                                            "O",
                                                            "ns=1;i=802",
                                                            {
                                                                "<PackagesAcceptedWithProperty>": (
                                                                    "O",
                                                                    "ns=1;i=1170",
                                                                    {
                                                                        "Weighed": (
                                                                            "V",
                                                                            "ns=1;i=1243",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                                "ResetCondition": (
                                                                    "V",
                                                                    "ns=1;i=1105",
                                                                    {},
                                                                ),
                                                                "StartTime": (
                                                                    "V",
                                                                    "ns=1;i=6021",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                        "TargetThroughput": (
                                                            "V",
                                                            "ns=1;i=822",
                                                            {
                                                                "EURange": (
                                                                    "V",
                                                                    "ns=1;i=824",
                                                                    {},
                                                                ),
                                                                "EngineeringUnits": (
                                                                    "V",
                                                                    "ns=1;i=823",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                    },
                                                )
                                            },
                                        )
                                    },
                                ),
                                "TU1Percent": ("V", "ns=1;i=447", {}),
                            },
                        ),
                        "ProductionPreset": (
                            "O",
                            "ns=1;i=849",
                            {
                                "Products": (
                                    "O",
                                    "ns=1;i=76",
                                    {
                                        "<Product>": (
                                            "O",
                                            "ns=1;i=77",
                                            {
                                                "ProductId": ("V", "ns=1;i=1468", {}),
                                                "ProductName": ("V", "ns=1;i=1469", {}),
                                            },
                                        )
                                    },
                                )
                            },
                        ),
                    },
                ),
                "ClearTare": ("M", "ns=1;i=1406", {}),
                "ContinuousScaleType": (
                    "OT",
                    "ns=1;i=10",
                    {
                        "<Totalizer>": (
                            "O",
                            "ns=1;i=72",
                            {
                                "TotalizedValue": (
                                    "V",
                                    "ns=1;i=390",
                                    {
                                        "EURange": ("V", "ns=1;i=392", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=391", {}),
                                        "ValuePrecision": ("V", "ns=1;i=393", {}),
                                    },
                                )
                            },
                        ),
                        "ControlMagnitude": (
                            "V",
                            "ns=1;i=60153",
                            {"EngineeringUnits": ("V", "ns=1;i=60142", {})},
                        ),
                        "FlowRate": (
                            "V",
                            "ns=1;i=517",
                            {
                                "EURange": ("V", "ns=1;i=519", {}),
                                "EngineeringUnits": ("V", "ns=1;i=518", {}),
                                "ValuePrecision": ("V", "ns=1;i=520", {}),
                            },
                        ),
                        "Load": (
                            "V",
                            "ns=1;i=60232",
                            {"EngineeringUnits": ("V", "ns=1;i=60233", {})},
                        ),
                        "LossInWeightScaleType": (
                            "OT",
                            "ns=1;i=50",
                            {
                                "BinWeight": (
                                    "V",
                                    "ns=1;i=60150",
                                    {
                                        "EURange": ("V", "ns=1;i=60229", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=60151", {}),
                                    },
                                ),
                                "DischargeStart": ("M", "ns=1;i=539", {}),
                                "DischargeStop": ("M", "ns=1;i=540", {}),
                                "Discharging": ("V", "ns=1;i=916", {}),
                                "HopperFillLevel": (
                                    "V",
                                    "ns=1;i=60157",
                                    {"EngineeringUnits": ("V", "ns=1;i=60158", {})},
                                ),
                                "HopperWeight": (
                                    "V",
                                    "ns=1;i=60144",
                                    {
                                        "EURange": ("V", "ns=1;i=60146", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=60145", {}),
                                        "ValuePrecision": ("V", "ns=1;i=60147", {}),
                                    },
                                ),
                                "RefillStart": ("M", "ns=1;i=537", {}),
                                "RefillStop": ("M", "ns=1;i=538", {}),
                                "Refilling": ("V", "ns=1;i=917", {}),
                            },
                        ),
                        "MasterTotalizer": (
                            "O",
                            "ns=1;i=73",
                            {
                                "TotalizedValue": (
                                    "V",
                                    "ns=1;i=394",
                                    {
                                        "EURange": ("V", "ns=1;i=396", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=395", {}),
                                        "ValuePrecision": ("V", "ns=1;i=397", {}),
                                    },
                                )
                            },
                        ),
                        "MaxFlowRate": (
                            "V",
                            "ns=1;i=60213",
                            {"EngineeringUnits": ("V", "ns=1;i=60214", {})},
                        ),
                        "MinFlowRate": (
                            "V",
                            "ns=1;i=60215",
                            {"EngineeringUnits": ("V", "ns=1;i=60216", {})},
                        ),
                        "ProductionPreset": (
                            "O",
                            "ns=1;i=852",
                            {
                                "Products": (
                                    "O",
                                    "ns=1;i=118",
                                    {
                                        "<Product>": (
                                            "O",
                                            "ns=1;i=119",
                                            {
                                                "ProductId": ("V", "ns=1;i=1009", {}),
                                                "ProductName": ("V", "ns=1;i=489", {}),
                                                "Statistic": (
                                                    "O",
                                                    "ns=1;i=120",
                                                    {
                                                        "StartTime": (
                                                            "V",
                                                            "ns=1;i=60076",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "TargetFlowRate": (
                                                    "V",
                                                    "ns=1;i=1258",
                                                    {
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=1260",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=1259",
                                                            {},
                                                        ),
                                                        "ValuePrecision": (
                                                            "V",
                                                            "ns=1;i=1265",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "TargetWeight": (
                                                    "V",
                                                    "ns=1;i=534",
                                                    {
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=536",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=535",
                                                            {},
                                                        ),
                                                        "ValuePrecision": (
                                                            "V",
                                                            "ns=1;i=668",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                            },
                                        )
                                    },
                                )
                            },
                        ),
                        "RateControlMode": ("V", "ns=1;i=60152", {}),
                        "Speed": (
                            "V",
                            "ns=1;i=60154",
                            {"EngineeringUnits": ("V", "ns=1;i=60155", {})},
                        ),
                        "TargetFlowRate": (
                            "V",
                            "ns=1;i=60148",
                            {"EngineeringUnits": ("V", "ns=1;i=60149", {})},
                        ),
                    },
                ),
                "CurrentWeight": (
                    "V",
                    "ns=1;i=203",
                    {
                        "CenterOfZero": ("V", "ns=1;i=206", {}),
                        "CurrentRangeId": ("V", "ns=1;i=399", {}),
                        "EURange": ("V", "ns=1;i=200", {}),
                        "EngineeringUnits": ("V", "ns=1;i=159", {}),
                        "Gross": ("V", "ns=1;i=60113", {}),
                        "GrossNegative": ("V", "ns=1;i=205", {}),
                        "HighResolutionValue": ("V", "ns=1;i=773", {}),
                        "InsideZero": ("V", "ns=1;i=165", {}),
                        "LegalForTrade": ("V", "ns=1;i=60114", {}),
                        "Net": ("V", "ns=1;i=60115", {}),
                        "Overload": ("V", "ns=1;i=163", {}),
                        "PrintableValue": ("V", "ns=1;i=772", {}),
                        "Tare": ("V", "ns=1;i=60116", {}),
                        "TareMode": ("V", "ns=1;i=209", {}),
                        "Underload": ("V", "ns=1;i=164", {}),
                        "ValuePrecision": ("V", "ns=1;i=160", {}),
                        "WeightId": ("V", "ns=1;i=204", {}),
                        "WeightStable": ("V", "ns=1;i=210", {}),
                    },
                ),
                "MachineryBuildingBlocks": ("O", "ns=1;i=50021", {}),
                "MaterialClass": ("V", "ns=1;i=234", {}),
                "MinimalWeight": (
                    "V",
                    "ns=1;i=60053",
                    {"EngineeringUnits": ("V", "ns=1;i=60054", {})},
                ),
                "PieceCountingScaleType": (
                    "OT",
                    "ns=1;i=6",
                    {
                        "CurrentPieceCount": (
                            "V",
                            "ns=1;i=607",
                            {
                                "EURange": ("V", "ns=1;i=609", {}),
                                "EngineeringUnits": ("V", "ns=1;i=608", {}),
                                "InstrumentRange": ("V", "ns=1;i=449", {}),
                                "ValuePrecision": ("V", "ns=1;i=610", {}),
                            },
                        ),
                        "ProductionPreset": (
                            "O",
                            "ns=1;i=853",
                            {
                                "Products": (
                                    "O",
                                    "ns=1;i=124",
                                    {
                                        "<Product>": (
                                            "O",
                                            "ns=1;i=125",
                                            {
                                                "CurrentItemCount": (
                                                    "V",
                                                    "ns=1;i=595",
                                                    {},
                                                ),
                                                "FeedRateMeasuringInterval": (
                                                    "V",
                                                    "ns=1;i=1266",
                                                    {},
                                                ),
                                                "FillingTime": ("V", "ns=1;i=1267", {}),
                                                "FineFeedCount": (
                                                    "V",
                                                    "ns=1;i=1268",
                                                    {},
                                                ),
                                                "InFlightCount": (
                                                    "V",
                                                    "ns=1;i=596",
                                                    {},
                                                ),
                                                "JogFeed": ("V", "ns=1;i=1269", {}),
                                                "MinimumDeltaPerFeedRateMeasuringInterval": (
                                                    "V",
                                                    "ns=1;i=1270",
                                                    {
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=1272",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=1271",
                                                            {},
                                                        ),
                                                        "InstrumentRange": (
                                                            "V",
                                                            "ns=1;i=1273",
                                                            {},
                                                        ),
                                                        "ValuePrecision": (
                                                            "V",
                                                            "ns=1;i=1274",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "NumberOfReferencePieces": (
                                                    "V",
                                                    "ns=1;i=598",
                                                    {},
                                                ),
                                                "ProductId": ("V", "ns=1;i=965", {}),
                                                "ProductName": ("V", "ns=1;i=516", {}),
                                                "ReferencePieceWeight": (
                                                    "V",
                                                    "ns=1;i=599",
                                                    {
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=600",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=653",
                                                            {},
                                                        ),
                                                        "InstrumentRange": (
                                                            "V",
                                                            "ns=1;i=654",
                                                            {},
                                                        ),
                                                        "ValuePrecision": (
                                                            "V",
                                                            "ns=1;i=655",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "RegisteredPieceCount": (
                                                    "V",
                                                    "ns=1;i=601",
                                                    {},
                                                ),
                                                "SetTargetItemCount": (
                                                    "M",
                                                    "ns=1;i=1398",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=1;i=1275",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "SetTargetPieceCount": (
                                                    "M",
                                                    "ns=1;i=1399",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=1;i=1276",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "SettlingTime": (
                                                    "V",
                                                    "ns=1;i=1277",
                                                    {},
                                                ),
                                                "Statistic": (
                                                    "O",
                                                    "ns=1;i=126",
                                                    {
                                                        "StartTime": (
                                                            "V",
                                                            "ns=1;i=60078",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "TareId": ("V", "ns=1;i=1278", {}),
                                                "TargetItemCount": (
                                                    "V",
                                                    "ns=1;i=1279",
                                                    {},
                                                ),
                                                "TargetPieceCount": (
                                                    "V",
                                                    "ns=1;i=1280",
                                                    {
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=1282",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=1281",
                                                            {},
                                                        ),
                                                        "InstrumentRange": (
                                                            "V",
                                                            "ns=1;i=1283",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "TotalizedItemCount": (
                                                    "V",
                                                    "ns=1;i=1288",
                                                    {},
                                                ),
                                                "TotalizedWeight": (
                                                    "V",
                                                    "ns=1;i=1289",
                                                    {
                                                        "CenterOfZero": (
                                                            "V",
                                                            "ns=1;i=1290",
                                                            {},
                                                        ),
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=1292",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=1291",
                                                            {},
                                                        ),
                                                        "GrossNegative": (
                                                            "V",
                                                            "ns=1;i=1293",
                                                            {},
                                                        ),
                                                        "HighResolutionValue": (
                                                            "V",
                                                            "ns=1;i=1294",
                                                            {},
                                                        ),
                                                        "InsideZero": (
                                                            "V",
                                                            "ns=1;i=1295",
                                                            {},
                                                        ),
                                                        "Overload": (
                                                            "V",
                                                            "ns=1;i=1297",
                                                            {},
                                                        ),
                                                        "PrintableValue": (
                                                            "V",
                                                            "ns=1;i=1298",
                                                            {},
                                                        ),
                                                        "TareMode": (
                                                            "V",
                                                            "ns=1;i=1299",
                                                            {},
                                                        ),
                                                        "Underload": (
                                                            "V",
                                                            "ns=1;i=1300",
                                                            {},
                                                        ),
                                                        "ValuePrecision": (
                                                            "V",
                                                            "ns=1;i=1301",
                                                            {},
                                                        ),
                                                        "WeightId": (
                                                            "V",
                                                            "ns=1;i=1302",
                                                            {},
                                                        ),
                                                        "WeightStable": (
                                                            "V",
                                                            "ns=1;i=1303",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                            },
                                        )
                                    },
                                )
                            },
                        ),
                        "ReferenceOptimisationRange": (
                            "V",
                            "ns=1;i=605",
                            {"EURange": ("V", "ns=1;i=606", {})},
                        ),
                        "SetNumberOfReferencePieces": (
                            "M",
                            "ns=1;i=1026",
                            {"InputArguments": ("V", "ns=1;i=990", {})},
                        ),
                        "SetReferencePieceWeight": (
                            "M",
                            "ns=1;i=603",
                            {"InputArguments": ("V", "ns=1;i=604", {})},
                        ),
                        "StartReference": (
                            "M",
                            "ns=1;i=602",
                            {"InputArguments": ("V", "ns=1;i=1013", {})},
                        ),
                    },
                ),
                "Policy": ("V", "ns=1;i=60048", {}),
                "ProcessStateId": ("V", "ns=1;i=229", {}),
                "ProcessStateMessage": ("V", "ns=1;i=161", {}),
                "ProductionOutput": ("O", "ns=1;i=50031", {}),
                "ProductionPreset": ("O", "ns=1;i=85", {}),
                "RecipeScaleType": (
                    "OT",
                    "ns=1;i=7",
                    {
                        "AbortRecipe": (
                            "M",
                            "ns=1;i=786",
                            {"InputArguments": ("V", "ns=1;i=1017", {})},
                        ),
                        "ContinueRecipe": (
                            "M",
                            "ns=1;i=784",
                            {"InputArguments": ("V", "ns=1;i=1015", {})},
                        ),
                        "ProductionPreset": (
                            "O",
                            "ns=1;i=854",
                            {
                                "Products": (
                                    "O",
                                    "ns=1;i=128",
                                    {
                                        "<Product>": (
                                            "O",
                                            "ns=1;i=129",
                                            {
                                                "ProductId": ("V", "ns=1;i=1011", {}),
                                                "ProductName": ("V", "ns=1;i=575", {}),
                                                "RecipeNodeId": (
                                                    "V",
                                                    "ns=1;i=1010",
                                                    {},
                                                ),
                                                "Report": ("V", "ns=1;i=253", {}),
                                                "ReportFile": (
                                                    "O",
                                                    "ns=1;i=1172",
                                                    {
                                                        "Close": (
                                                            "M",
                                                            "ns=1;i=1400",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "ns=1;i=1304",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "GetPosition": (
                                                            "M",
                                                            "ns=1;i=1401",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "ns=1;i=1305",
                                                                    {},
                                                                ),
                                                                "OutputArguments": (
                                                                    "V",
                                                                    "ns=1;i=1306",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                        "Open": (
                                                            "M",
                                                            "ns=1;i=1402",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "ns=1;i=1307",
                                                                    {},
                                                                ),
                                                                "OutputArguments": (
                                                                    "V",
                                                                    "ns=1;i=1308",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                        "OpenCount": (
                                                            "V",
                                                            "ns=1;i=1309",
                                                            {},
                                                        ),
                                                        "Read": (
                                                            "M",
                                                            "ns=1;i=1403",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "ns=1;i=1310",
                                                                    {},
                                                                ),
                                                                "OutputArguments": (
                                                                    "V",
                                                                    "ns=1;i=1311",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                        "SetPosition": (
                                                            "M",
                                                            "ns=1;i=1404",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "ns=1;i=1312",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "Size": (
                                                            "V",
                                                            "ns=1;i=1313",
                                                            {},
                                                        ),
                                                        "UserWritable": (
                                                            "V",
                                                            "ns=1;i=1314",
                                                            {},
                                                        ),
                                                        "Writable": (
                                                            "V",
                                                            "ns=1;i=1315",
                                                            {},
                                                        ),
                                                        "Write": (
                                                            "M",
                                                            "ns=1;i=1405",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "ns=1;i=1316",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                    },
                                                ),
                                                "Statistic": (
                                                    "O",
                                                    "ns=1;i=130",
                                                    {
                                                        "StartTime": (
                                                            "V",
                                                            "ns=1;i=60079",
                                                            {},
                                                        )
                                                    },
                                                ),
                                            },
                                        )
                                    },
                                )
                            },
                        ),
                        "Recipes": (
                            "O",
                            "ns=1;i=127",
                            {
                                "<Recipe_No>": (
                                    "O",
                                    "ns=1;i=74",
                                    {
                                        "AddRecipeElement": (
                                            "M",
                                            "ns=1;i=467",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=440",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=441",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "RecipeElements": ("O", "ns=1;i=83", {}),
                                        "RecipeId": ("V", "ns=1;i=257", {}),
                                        "RecipeName": ("V", "ns=1;i=258", {}),
                                        "RemoveRecipeElement": (
                                            "M",
                                            "ns=1;i=468",
                                            {"InputArguments": ("V", "ns=1;i=442", {})},
                                        ),
                                    },
                                ),
                                "AddRecipe": (
                                    "M",
                                    "ns=1;i=450",
                                    {
                                        "InputArguments": ("V", "ns=1;i=254", {}),
                                        "OutputArguments": ("V", "ns=1;i=255", {}),
                                    },
                                ),
                                "RecipeUpload": (
                                    "O",
                                    "ns=1;i=50004",
                                    {
                                        "ClientProcessingTimeout": (
                                            "V",
                                            "ns=1;i=60004",
                                            {},
                                        ),
                                        "CloseAndCommit": (
                                            "M",
                                            "ns=1;i=70001",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=60023",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=60024",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "GenerateFileForRead": (
                                            "M",
                                            "ns=1;i=70002",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=60025",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=60026",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "GenerateFileForWrite": (
                                            "M",
                                            "ns=1;i=70003",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=60027",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=60028",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "RemoveRecipe": (
                                    "M",
                                    "ns=1;i=452",
                                    {"InputArguments": ("V", "ns=1;i=256", {})},
                                ),
                            },
                        ),
                        "SkipCurrentRecipeElement": (
                            "M",
                            "ns=1;i=785",
                            {"InputArguments": ("V", "ns=1;i=1016", {})},
                        ),
                        "StartRecipe": (
                            "M",
                            "ns=1;i=458",
                            {"InputArguments": ("V", "ns=1;i=373", {})},
                        ),
                        "StopRecipe": (
                            "M",
                            "ns=1;i=783",
                            {"InputArguments": ("V", "ns=1;i=1014", {})},
                        ),
                        "SupportedMaterial": (
                            "O",
                            "ns=1;i=69",
                            {
                                "MaterialId": ("V", "ns=1;i=374", {}),
                                "MaterialName": ("V", "ns=1;i=787", {}),
                            },
                        ),
                        "SupportedTargetValues": ("V", "ns=1;i=612", {}),
                        "SupportedThresholdValues": ("V", "ns=1;i=611", {}),
                    },
                ),
                "RegisterWeight": ("M", "ns=1;i=471", {}),
                "RegisteredWeight": (
                    "V",
                    "ns=1;i=211",
                    {
                        "CenterOfZero": ("V", "ns=1;i=214", {}),
                        "CurrentRangeId": ("V", "ns=1;i=60117", {}),
                        "EURange": ("V", "ns=1;i=207", {}),
                        "EngineeringUnits": ("V", "ns=1;i=201", {}),
                        "Gross": ("V", "ns=1;i=60118", {}),
                        "GrossNegative": ("V", "ns=1;i=213", {}),
                        "HighResolutionValue": ("V", "ns=1;i=775", {}),
                        "InsideZero": ("V", "ns=1;i=221", {}),
                        "LegalForTrade": ("V", "ns=1;i=60119", {}),
                        "Net": ("V", "ns=1;i=60120", {}),
                        "Overload": ("V", "ns=1;i=215", {}),
                        "PrintableValue": ("V", "ns=1;i=774", {}),
                        "Tare": ("V", "ns=1;i=60121", {}),
                        "TareMode": ("V", "ns=1;i=217", {}),
                        "Underload": ("V", "ns=1;i=216", {}),
                        "ValuePrecision": ("V", "ns=1;i=202", {}),
                        "WeightId": ("V", "ns=1;i=212", {}),
                        "WeightStable": ("V", "ns=1;i=218", {}),
                    },
                ),
                "SetPresetTare": (
                    "M",
                    "ns=1;i=1407",
                    {"InputArguments": ("V", "ns=1;i=1353", {})},
                ),
                "SetTare": ("M", "ns=1;i=1409", {}),
                "SetZero": ("M", "ns=1;i=1408", {}),
                "SimpleScaleType": (
                    "OT",
                    "ns=1;i=3",
                    {
                        "HopperScaleType": (
                            "OT",
                            "ns=1;i=9",
                            {
                                "<Limits>": ("V", "ns=1;i=381", {}),
                                "LevelMax": (
                                    "V",
                                    "ns=1;i=60221",
                                    {
                                        "EngineeringUnits": ("V", "ns=1;i=60222", {}),
                                        "LevelMode": ("V", "ns=1;i=60230", {}),
                                    },
                                ),
                                "LevelMin": (
                                    "V",
                                    "ns=1;i=60223",
                                    {
                                        "EngineeringUnits": ("V", "ns=1;i=60224", {}),
                                        "LevelMode": ("V", "ns=1;i=60231", {}),
                                    },
                                ),
                                "LimitMax": ("V", "ns=1;i=388", {}),
                                "LimitMin": ("V", "ns=1;i=389", {}),
                            },
                        ),
                        "LaboratoryScaleType": (
                            "OT",
                            "ns=1;i=15",
                            {
                                "CalibrationNeeded": ("V", "ns=1;i=265", {}),
                                "CalibrationRunning": ("V", "ns=1;i=264", {}),
                                "CloseDraftShields": (
                                    "M",
                                    "ns=1;i=761",
                                    {"InputArguments": ("V", "ns=1;i=762", {})},
                                ),
                                "DraftShieldLeftClosed": ("V", "ns=1;i=238", {}),
                                "DraftShieldRightClosed": ("V", "ns=1;i=239", {}),
                                "DraftShieldTopClosed": ("V", "ns=1;i=240", {}),
                                "IonisatorRunning": ("V", "ns=1;i=1207", {}),
                                "LevelingRunning": ("V", "ns=1;i=263", {}),
                                "OpenDraftShields": (
                                    "M",
                                    "ns=1;i=758",
                                    {"InputArguments": ("V", "ns=1;i=759", {})},
                                ),
                                "StartCalibration": ("M", "ns=1;i=455", {}),
                                "StartIonisator": ("M", "ns=1;i=457", {}),
                                "StartLeveling": ("M", "ns=1;i=454", {}),
                                "StopIonisator": ("M", "ns=1;i=463", {}),
                            },
                        ),
                        "ProductionPreset": (
                            "O",
                            "ns=1;i=855",
                            {
                                "Products": (
                                    "O",
                                    "ns=1;i=842",
                                    {
                                        "<Product>": (
                                            "O",
                                            "ns=1;i=843",
                                            {
                                                "ContainerId": ("V", "ns=1;i=1317", {}),
                                                "ProductId": ("V", "ns=1;i=991", {}),
                                                "ProductName": ("V", "ns=1;i=966", {}),
                                                "Statistic": (
                                                    "O",
                                                    "ns=1;i=1173",
                                                    {
                                                        "StartTime": (
                                                            "V",
                                                            "ns=1;i=60081",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "UnitPrice": (
                                                    "V",
                                                    "ns=1;i=1466",
                                                    {
                                                        "CurrencyUnit": (
                                                            "V",
                                                            "ns=1;i=1467",
                                                            {},
                                                        )
                                                    },
                                                ),
                                            },
                                        )
                                    },
                                )
                            },
                        ),
                        "WeighingModuleType": ("OT", "ns=1;i=1", {}),
                    },
                ),
                "State": (
                    "O",
                    "ns=1;i=50005",
                    {
                        "AvailableStates": ("V", "ns=1;i=60029", {}),
                        "AvailableTransitions": ("V", "ns=1;i=60030", {}),
                        "CurrentState": (
                            "V",
                            "ns=1;i=60086",
                            {"Id": ("V", "ns=1;i=60087", {})},
                        ),
                        "MachineState": (
                            "O",
                            "ns=1;i=50015",
                            {
                                "AvailableStates": ("V", "ns=1;i=60031", {}),
                                "AvailableTransitions": ("V", "ns=1;i=60032", {}),
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=60084",
                                    {"Id": ("V", "ns=1;i=60085", {})},
                                ),
                                "ExecuteState": (
                                    "O",
                                    "ns=1;i=50017",
                                    {
                                        "AvailableStates": ("V", "ns=1;i=60105", {}),
                                        "AvailableTransitions": (
                                            "V",
                                            "ns=1;i=60106",
                                            {},
                                        ),
                                        "CurrentState": (
                                            "V",
                                            "ns=1;i=60107",
                                            {"Id": ("V", "ns=1;i=60108", {})},
                                        ),
                                    },
                                ),
                            },
                        ),
                    },
                ),
                "SubDevices": (
                    "O",
                    "ns=1;i=67",
                    {
                        "<FeederModule>": ("O", "ns=1;i=1177", {}),
                        "<PrinterModule>": ("O", "ns=1;i=1178", {}),
                        "<WeighingModule>": (
                            "O",
                            "ns=1;i=1414",
                            {
                                "<ListOfWeighingRanges>": (
                                    "O",
                                    "ns=1;i=1415",
                                    {
                                        "ActualScaleInterval": (
                                            "V",
                                            "ns=1;i=1427",
                                            {
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1428",
                                                    {},
                                                )
                                            },
                                        ),
                                        "Range": (
                                            "V",
                                            "ns=1;i=1429",
                                            {
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1430",
                                                    {},
                                                )
                                            },
                                        ),
                                        "VerificationScaleInterval": (
                                            "V",
                                            "ns=1;i=1431",
                                            {
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=1432",
                                                    {},
                                                )
                                            },
                                        ),
                                    },
                                ),
                                "CurrentWeight": (
                                    "V",
                                    "ns=1;i=1418",
                                    {
                                        "CenterOfZero": ("V", "ns=1;i=1437", {}),
                                        "CurrentRangeId": ("V", "ns=1;i=1438", {}),
                                        "EURange": ("V", "ns=1;i=1420", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1419", {}),
                                        "GrossNegative": ("V", "ns=1;i=1439", {}),
                                        "HighResolutionValue": ("V", "ns=1;i=1440", {}),
                                        "InsideZero": ("V", "ns=1;i=1441", {}),
                                        "Overload": ("V", "ns=1;i=1422", {}),
                                        "PrintableValue": ("V", "ns=1;i=1442", {}),
                                        "TareMode": ("V", "ns=1;i=1423", {}),
                                        "Underload": ("V", "ns=1;i=1424", {}),
                                        "ValuePrecision": ("V", "ns=1;i=1443", {}),
                                        "WeightId": ("V", "ns=1;i=1444", {}),
                                        "WeightStable": ("V", "ns=1;i=1445", {}),
                                    },
                                ),
                                "DeviceClass": ("V", "ns=1;i=1425", {}),
                                "HardwareRevision": ("V", "ns=1;i=1426", {}),
                                "Manufacturer": ("V", "ns=1;i=1433", {}),
                                "Model": ("V", "ns=1;i=1434", {}),
                                "SerialNumber": ("V", "ns=1;i=1435", {}),
                                "SoftwareRevision": ("V", "ns=1;i=1436", {}),
                            },
                        ),
                        "SupportedTypes": ("O", "ns=1;i=80", {}),
                    },
                ),
                "TotalizingHopperScaleType": (
                    "OT",
                    "ns=1;i=8",
                    {
                        "ProductionPreset": (
                            "O",
                            "ns=1;i=856",
                            {
                                "Products": (
                                    "O",
                                    "ns=1;i=840",
                                    {
                                        "<Product>": (
                                            "O",
                                            "ns=1;i=841",
                                            {
                                                "ProductId": ("V", "ns=1;i=1387", {}),
                                                "ProductName": ("V", "ns=1;i=964", {}),
                                                "Statistic": (
                                                    "O",
                                                    "ns=1;i=1174",
                                                    {
                                                        "StartTime": (
                                                            "V",
                                                            "ns=1;i=60080",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "TipCounter": ("V", "ns=1;i=962", {}),
                                                "VolumeTargetValue": (
                                                    "V",
                                                    "ns=1;i=1319",
                                                    {
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=1321",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=1320",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                            },
                                        )
                                    },
                                )
                            },
                        )
                    },
                ),
                "VehicleScaleType": (
                    "OT",
                    "ns=1;i=834",
                    {
                        "InboundWeighing": (
                            "M",
                            "ns=1;i=1022",
                            {"InputArguments": ("V", "ns=1;i=946", {})},
                        ),
                        "OnePassWeighing": (
                            "M",
                            "ns=1;i=1024",
                            {"InputArguments": ("V", "ns=1;i=949", {})},
                        ),
                        "OutboundWeighing": (
                            "M",
                            "ns=1;i=1023",
                            {"InputArguments": ("V", "ns=1;i=947", {})},
                        ),
                        "ProductionPreset": (
                            "O",
                            "ns=1;i=857",
                            {
                                "Products": (
                                    "O",
                                    "ns=1;i=844",
                                    {
                                        "<Product>": (
                                            "O",
                                            "ns=1;i=845",
                                            {
                                                "CarrierDisplayName": (
                                                    "V",
                                                    "ns=1;i=1326",
                                                    {},
                                                ),
                                                "CarrierId": ("V", "ns=1;i=1327", {}),
                                                "Customer": ("V", "ns=1;i=1328", {}),
                                                "DeltaWeight": (
                                                    "V",
                                                    "ns=1;i=967",
                                                    {
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=969",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=968",
                                                            {},
                                                        ),
                                                        "InsideZero": (
                                                            "V",
                                                            "ns=1;i=970",
                                                            {},
                                                        ),
                                                        "IsFilling": (
                                                            "V",
                                                            "ns=1;i=60082",
                                                            {},
                                                        ),
                                                        "Overload": (
                                                            "V",
                                                            "ns=1;i=972",
                                                            {},
                                                        ),
                                                        "TareMode": (
                                                            "V",
                                                            "ns=1;i=973",
                                                            {},
                                                        ),
                                                        "Underload": (
                                                            "V",
                                                            "ns=1;i=974",
                                                            {},
                                                        ),
                                                        "WeightStable": (
                                                            "V",
                                                            "ns=1;i=975",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "Destination": ("V", "ns=1;i=1329", {}),
                                                "DriverDisplayName": (
                                                    "V",
                                                    "ns=1;i=1330",
                                                    {},
                                                ),
                                                "DriverId": ("V", "ns=1;i=1331", {}),
                                                "GetVehicleInformation": (
                                                    "M",
                                                    "ns=1;i=1397",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=1;i=1209",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "InboundScale": (
                                                    "V",
                                                    "ns=1;i=1332",
                                                    {},
                                                ),
                                                "InboundWeight": (
                                                    "V",
                                                    "ns=1;i=1333",
                                                    {
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=1335",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=1334",
                                                            {},
                                                        ),
                                                        "InsideZero": (
                                                            "V",
                                                            "ns=1;i=1336",
                                                            {},
                                                        ),
                                                        "Overload": (
                                                            "V",
                                                            "ns=1;i=1338",
                                                            {},
                                                        ),
                                                        "TareMode": (
                                                            "V",
                                                            "ns=1;i=1339",
                                                            {},
                                                        ),
                                                        "Underload": (
                                                            "V",
                                                            "ns=1;i=1340",
                                                            {},
                                                        ),
                                                        "WeightStable": (
                                                            "V",
                                                            "ns=1;i=1341",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "Material": (
                                                    "O",
                                                    "ns=1;i=1176",
                                                    {
                                                        "MaterialId": (
                                                            "V",
                                                            "ns=1;i=1342",
                                                            {},
                                                        ),
                                                        "MaterialName": (
                                                            "V",
                                                            "ns=1;i=1343",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "OutboundScale": (
                                                    "V",
                                                    "ns=1;i=1344",
                                                    {},
                                                ),
                                                "OutboundWeight": (
                                                    "V",
                                                    "ns=1;i=976",
                                                    {
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=978",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=977",
                                                            {},
                                                        ),
                                                        "InsideZero": (
                                                            "V",
                                                            "ns=1;i=979",
                                                            {},
                                                        ),
                                                        "Overload": (
                                                            "V",
                                                            "ns=1;i=981",
                                                            {},
                                                        ),
                                                        "TareMode": (
                                                            "V",
                                                            "ns=1;i=982",
                                                            {},
                                                        ),
                                                        "Underload": (
                                                            "V",
                                                            "ns=1;i=983",
                                                            {},
                                                        ),
                                                        "WeightStable": (
                                                            "V",
                                                            "ns=1;i=984",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "ProductId": ("V", "ns=1;i=1019", {}),
                                                "ProductName": ("V", "ns=1;i=987", {}),
                                                "ScaleOperatorId": (
                                                    "V",
                                                    "ns=1;i=1345",
                                                    {},
                                                ),
                                                "Statistic": (
                                                    "O",
                                                    "ns=1;i=1175",
                                                    {
                                                        "StartTime": (
                                                            "V",
                                                            "ns=1;i=60083",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "Supplier": ("V", "ns=1;i=1346", {}),
                                                "Tare": ("V", "ns=1;i=1347", {}),
                                                "TareExpirationDate": (
                                                    "V",
                                                    "ns=1;i=1348",
                                                    {},
                                                ),
                                                "TotalWeight": ("V", "ns=1;i=1349", {}),
                                                "TotalWeightResetDate": (
                                                    "V",
                                                    "ns=1;i=1350",
                                                    {},
                                                ),
                                                "VehicleId": ("V", "ns=1;i=985", {}),
                                            },
                                        )
                                    },
                                )
                            },
                        ),
                    },
                ),
            },
        ),
        "ScaleSystemType": (
            "OT",
            "ns=1;i=44",
            {
                "MachineryBuildingBlocks": ("O", "ns=1;i=50022", {}),
                "Policy": ("V", "ns=1;i=140", {}),
                "ProcessStateId": ("V", "ns=1;i=356", {}),
                "ProcessStateMessage": ("V", "ns=1;i=357", {}),
                "ProductionOutput": ("O", "ns=1;i=79", {}),
                "ProductionPreset": ("O", "ns=1;i=70", {}),
                "ResetGlobalStatistics": ("M", "ns=1;i=1025", {}),
                "SubDevices": (
                    "O",
                    "ns=1;i=837",
                    {
                        "<ScaleDevice>": (
                            "O",
                            "ns=1;i=50001",
                            {
                                "<ListOfWeighingRanges>": (
                                    "O",
                                    "ns=1;i=50002",
                                    {
                                        "ActualScaleInterval": (
                                            "V",
                                            "ns=1;i=60010",
                                            {
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=60011",
                                                    {},
                                                )
                                            },
                                        ),
                                        "Range": (
                                            "V",
                                            "ns=1;i=60012",
                                            {
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=60013",
                                                    {},
                                                )
                                            },
                                        ),
                                        "VerificationScaleInterval": (
                                            "V",
                                            "ns=1;i=60014",
                                            {
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=60015",
                                                    {},
                                                )
                                            },
                                        ),
                                    },
                                ),
                                "CurrentWeight": (
                                    "V",
                                    "ns=1;i=60001",
                                    {
                                        "CenterOfZero": ("V", "ns=1;i=6010", {}),
                                        "CurrentRangeId": ("V", "ns=1;i=6011", {}),
                                        "EURange": ("V", "ns=1;i=60003", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=60002", {}),
                                        "GrossNegative": ("V", "ns=1;i=6012", {}),
                                        "HighResolutionValue": ("V", "ns=1;i=6013", {}),
                                        "InsideZero": ("V", "ns=1;i=6014", {}),
                                        "Overload": ("V", "ns=1;i=60005", {}),
                                        "PrintableValue": ("V", "ns=1;i=6015", {}),
                                        "TareMode": ("V", "ns=1;i=60006", {}),
                                        "Underload": ("V", "ns=1;i=60007", {}),
                                        "ValuePrecision": ("V", "ns=1;i=6016", {}),
                                        "WeightId": ("V", "ns=1;i=6017", {}),
                                        "WeightStable": ("V", "ns=1;i=6018", {}),
                                    },
                                ),
                                "DeviceClass": ("V", "ns=1;i=60008", {}),
                                "HardwareRevision": ("V", "ns=1;i=60009", {}),
                                "Manufacturer": ("V", "ns=1;i=60016", {}),
                                "Model": ("V", "ns=1;i=60017", {}),
                                "SerialNumber": ("V", "ns=1;i=60018", {}),
                                "SoftwareRevision": ("V", "ns=1;i=60019", {}),
                            },
                        ),
                        "SupportedTypes": ("O", "ns=1;i=838", {}),
                    },
                ),
                "SystemState": (
                    "O",
                    "ns=1;i=50008",
                    {
                        "AvailableStates": ("V", "ns=1;i=60049", {}),
                        "AvailableTransitions": ("V", "ns=1;i=60050", {}),
                        "CurrentState": (
                            "V",
                            "ns=1;i=60090",
                            {"Id": ("V", "ns=1;i=60091", {})},
                        ),
                        "MachineState": (
                            "O",
                            "ns=1;i=50016",
                            {
                                "AvailableStates": ("V", "ns=1;i=60051", {}),
                                "AvailableTransitions": ("V", "ns=1;i=60052", {}),
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=60088",
                                    {"Id": ("V", "ns=1;i=60089", {})},
                                ),
                                "ExecuteState": (
                                    "O",
                                    "ns=1;i=50018",
                                    {
                                        "AvailableStates": ("V", "ns=1;i=60109", {}),
                                        "AvailableTransitions": (
                                            "V",
                                            "ns=1;i=60110",
                                            {},
                                        ),
                                        "CurrentState": (
                                            "V",
                                            "ns=1;i=60111",
                                            {"Id": ("V", "ns=1;i=60112", {})},
                                        ),
                                    },
                                ),
                            },
                        ),
                    },
                ),
            },
        ),
        "StatisticCounterType": (
            "OT",
            "ns=1;i=43",
            {
                "AcceptedStatisticCounterType": ("OT", "ns=1;i=1027", {}),
                "RejectedStatisticCounterType": ("OT", "ns=1;i=1028", {}),
                "Weighed": ("V", "ns=1;i=162", {}),
            },
        ),
        "StatisticType": (
            "OT",
            "ns=1;i=25",
            {
                "CheckweigherStatisticType": ("OT", "ns=1;i=48", {}),
                "FloatingStatisticType": (
                    "OT",
                    "ns=1;i=26",
                    {"WindowNumberOfValues": ("V", "ns=1;i=60063", {})},
                ),
                "LastItem": (
                    "O",
                    "ns=1;i=1182",
                    {
                        "MeasuredWeight": (
                            "V",
                            "ns=1;i=1389",
                            {
                                "EURange": ("V", "ns=1;i=1391", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1390", {}),
                                "Overload": ("V", "ns=1;i=1393", {}),
                                "TareMode": ("V", "ns=1;i=1394", {}),
                                "Underload": ("V", "ns=1;i=1395", {}),
                            },
                        )
                    },
                ),
                "ResetCondition": ("V", "ns=1;i=986", {}),
                "StartTime": ("V", "ns=1;i=283", {}),
            },
        ),
        "TotalizerType": (
            "OT",
            "ns=1;i=27",
            {
                "ResetTotalizer": ("M", "ns=1;i=451", {}),
                "TotalizedValue": (
                    "V",
                    "ns=1;i=329",
                    {
                        "EURange": ("V", "ns=1;i=332", {}),
                        "EngineeringUnits": ("V", "ns=1;i=331", {}),
                        "ValuePrecision": ("V", "ns=1;i=333", {}),
                    },
                ),
            },
        ),
        "WeighingItemType": (
            "OT",
            "ns=1;i=24",
            {
                "ItemId": ("V", "ns=1;i=248", {}),
                "MeasuredHeight": (
                    "V",
                    "ns=1;i=60177",
                    {"EngineeringUnits": ("V", "ns=1;i=60178", {})},
                ),
                "MeasuredLength": (
                    "V",
                    "ns=1;i=60179",
                    {"EngineeringUnits": ("V", "ns=1;i=60180", {})},
                ),
                "MeasuredVolume": (
                    "V",
                    "ns=1;i=60181",
                    {"EngineeringUnits": ("V", "ns=1;i=60182", {})},
                ),
                "MeasuredWeight": (
                    "V",
                    "ns=1;i=247",
                    {
                        "CenterOfZero": ("V", "ns=1;i=363", {}),
                        "EURange": ("V", "ns=1;i=401", {}),
                        "EngineeringUnits": ("V", "ns=1;i=400", {}),
                        "GrossNegative": ("V", "ns=1;i=370", {}),
                        "HighResolutionValue": ("V", "ns=1;i=777", {}),
                        "InsideZero": ("V", "ns=1;i=230", {}),
                        "Overload": ("V", "ns=1;i=227", {}),
                        "PrintableValue": ("V", "ns=1;i=776", {}),
                        "TareMode": ("V", "ns=1;i=371", {}),
                        "Underload": ("V", "ns=1;i=228", {}),
                        "ValuePrecision": ("V", "ns=1;i=402", {}),
                        "WeightId": ("V", "ns=1;i=688", {}),
                        "WeightStable": ("V", "ns=1;i=372", {}),
                    },
                ),
                "MeasuredWidth": (
                    "V",
                    "ns=1;i=60183",
                    {"EngineeringUnits": ("V", "ns=1;i=60184", {})},
                ),
                "PriceItemType": (
                    "OT",
                    "ns=1;i=833",
                    {
                        "ItemPrice": (
                            "V",
                            "ns=1;i=1354",
                            {"CurrencyUnit": ("V", "ns=1;i=1355", {})},
                        )
                    },
                ),
                "ZoneName": ("V", "ns=1;i=1029", {}),
            },
        ),
        "WeighingRangeElementType": (
            "OT",
            "ns=1;i=23",
            {
                "ActualScaleInterval": (
                    "V",
                    "ns=1;i=262",
                    {"EngineeringUnits": ("V", "ns=1;i=1351", {})},
                ),
                "Range": (
                    "V",
                    "ns=1;i=291",
                    {"EngineeringUnits": ("V", "ns=1;i=1358", {})},
                ),
                "VerificationScaleInterval": (
                    "V",
                    "ns=1;i=417",
                    {"EngineeringUnits": ("V", "ns=1;i=1352", {})},
                ),
            },
        ),
        "ZoneType": (
            "OT",
            "ns=1;i=42",
            {
                "LowerLimit": (
                    "V",
                    "ns=1;i=60201",
                    {"EngineeringUnits": ("V", "ns=1;i=60202", {})},
                ),
                "Name": ("V", "ns=1;i=311", {}),
                "UpperLimit": (
                    "V",
                    "ns=1;i=60203",
                    {"EngineeringUnits": ("V", "ns=1;i=60204", {})},
                ),
                "ZoneStatistic": (
                    "O",
                    "ns=1;i=115",
                    {"Weighed": ("V", "ns=1;i=232", {})},
                ),
            },
        ),
    },
    "reftypes": {"NextRecipeElement": ("RT", "ns=1;i=66", {})},
    "vartypes": {
        "MeasuredItemType": (
            "VT",
            "ns=1;i=52",
            {
                "EURange": ("V", "ns=1;i=324", {}),
                "EngineeringUnits": ("V", "ns=1;i=190", {}),
                "InstrumentRange": ("V", "ns=1;i=133", {}),
                "ValuePrecision": ("V", "ns=1;i=191", {}),
                "WeightItemType": (
                    "VT",
                    "ns=1;i=53",
                    {
                        "CenterOfZero": ("V", "ns=1;i=192", {}),
                        "CurrentRangeId": ("V", "ns=1;i=141", {}),
                        "Gross": ("V", "ns=1;i=60033", {}),
                        "GrossNegative": ("V", "ns=1;i=193", {}),
                        "HighResolutionValue": ("V", "ns=1;i=771", {}),
                        "InsideZero": ("V", "ns=1;i=144", {}),
                        "LegalForTrade": ("V", "ns=1;i=769", {}),
                        "Net": ("V", "ns=1;i=60034", {}),
                        "Overload": ("V", "ns=1;i=142", {}),
                        "PrintableValue": ("V", "ns=1;i=770", {}),
                        "Tare": ("V", "ns=1;i=60055", {}),
                        "TareMode": ("V", "ns=1;i=194", {}),
                        "Underload": ("V", "ns=1;i=143", {}),
                        "WeightId": ("V", "ns=1;i=196", {}),
                        "WeightStable": ("V", "ns=1;i=199", {}),
                    },
                ),
            },
        ),
        "TargetItemType": (
            "VT",
            "ns=1;i=51",
            {
                "AllowedEngineeringUnits": ("V", "ns=1;i=433", {}),
                "EngineeringUnits": ("V", "ns=1;i=168", {}),
                "MinusTolerance": (
                    "V",
                    "ns=1;i=60225",
                    {"EngineeringUnits": ("V", "ns=1;i=60226", {})},
                ),
                "PlusTolerance": (
                    "V",
                    "ns=1;i=60227",
                    {"EngineeringUnits": ("V", "ns=1;i=60228", {})},
                ),
            },
        ),
    },
}
