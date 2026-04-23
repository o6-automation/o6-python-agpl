# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 79d538a65639d4ac0ae6da73b7a916eeb1b12a5c7a16767bdcbd7b513d107973
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/CAS/"
_VERSION: str = "1.00.1"
_REQUIRED: list = [
    {"uri": "http://opcfoundation.org/UA/", "version": "1.04.7"},
    {"uri": "http://opcfoundation.org/UA/DI/", "version": "1.03.0"},
    {"uri": "http://opcfoundation.org/UA/IA/", "version": "1.00.0"},
    {"uri": "http://opcfoundation.org/UA/Machinery/", "version": "1.01.0"},
]
_STRUCTURES: list = [
    (
        "ns=1;i=3007",
        "FilterClassDataType",
        "ns=1;i=5042",
        {
            "structure_type": 0,
            "fields": [
                {"name": "A", "data_type": "ns=1;i=3008", "value_rank": -1},
                {"name": "B", "data_type": "ns=1;i=3008", "value_rank": -1},
                {"name": "C", "data_type": "ns=1;i=3008", "value_rank": -1},
            ],
        },
    )
]
_ENUMS: list = [
    (
        "ns=1;i=3022",
        "AirnetHealthStateEnum",
        {
            "fields": [
                {"name": "OK", "value": 0, "display_name": "OK"},
                {"name": "Warning", "value": 1, "display_name": "Warning"},
                {"name": "Error", "value": 2, "display_name": "Error"},
                {"name": "Critical", "value": 3, "display_name": "Critical"},
            ]
        },
    ),
    (
        "ns=1;i=3023",
        "AirnetIntegratedStateEnum",
        {
            "fields": [
                {
                    "name": "FullyIntegrated",
                    "value": 0,
                    "display_name": "FullyIntegrated",
                },
                {
                    "name": "PartiallyIntegrated",
                    "value": 1,
                    "display_name": "PartiallyIntegrated",
                },
                {"name": "FullyIsolated", "value": 2, "display_name": "FullyIsolated"},
            ]
        },
    ),
    (
        "ns=1;i=3024",
        "AirnetOperatingStateEnum",
        {
            "fields": [
                {"name": "Other", "value": 0, "display_name": "Other"},
                {"name": "Stopped", "value": 1, "display_name": "Stopped"},
                {"name": "Starting", "value": 2, "display_name": "Starting"},
                {"name": "Stopping", "value": 3, "display_name": "Stopping"},
                {"name": "Operational", "value": 4, "display_name": "Operational"},
            ]
        },
    ),
    (
        "ns=1;i=3025",
        "CompressorOperatingStateEnum",
        {
            "fields": [
                {"name": "Other", "value": 0, "display_name": "Other"},
                {"name": "Stopped", "value": 1, "display_name": "Stopped"},
                {"name": "Starting", "value": 2, "display_name": "Starting"},
                {"name": "Stopping", "value": 3, "display_name": "Stopping"},
                {"name": "Unloaded", "value": 4, "display_name": "Unloaded"},
                {"name": "Loading", "value": 5, "display_name": "Loading"},
                {"name": "Unloading", "value": 6, "display_name": "Unloading"},
                {"name": "Loaded", "value": 7, "display_name": "Loaded"},
            ]
        },
    ),
    (
        "ns=1;i=3018",
        "CompressorTypeEnum",
        {
            "fields": [
                {"name": "Other", "value": 0, "display_name": "Other"},
                {
                    "name": "AxialTurboCompressor",
                    "value": 1,
                    "display_name": "AxialTurboCompressor",
                },
                {
                    "name": "BellowsCompressor",
                    "value": 2,
                    "display_name": "BellowsCompressor",
                },
                {
                    "name": "DiaphragmCompressor",
                    "value": 3,
                    "display_name": "DiaphragmCompressor",
                },
                {
                    "name": "LiquidRingCompressor",
                    "value": 4,
                    "display_name": "LiquidRingCompressor",
                },
                {
                    "name": "PistonCompressor",
                    "value": 5,
                    "display_name": "PistonCompressor",
                },
                {
                    "name": "RadialTurboCompressor",
                    "value": 6,
                    "display_name": "RadialTurboCompressor",
                },
                {
                    "name": "RootsCompressor",
                    "value": 7,
                    "display_name": "RootsCompressor",
                },
                {
                    "name": "ScrewCompressor",
                    "value": 8,
                    "display_name": "ScrewCompressor",
                },
                {
                    "name": "ScrollCompressor",
                    "value": 9,
                    "display_name": "ScrollCompressor",
                },
                {
                    "name": "SideChannelCompressor",
                    "value": 10,
                    "display_name": "SideChannelCompressor",
                },
                {
                    "name": "StraightLobeCompressor",
                    "value": 11,
                    "display_name": "StraightLobeCompressor",
                },
                {
                    "name": "VaneCompressor",
                    "value": 12,
                    "display_name": "VaneCompressor",
                },
            ]
        },
    ),
    (
        "ns=1;i=3015",
        "ConverterTypeEnum",
        {
            "fields": [
                {"name": "Other", "value": 0, "display_name": "Other"},
                {
                    "name": "CatalyticHCConverter",
                    "value": 1,
                    "display_name": "CatalyticHCConverter",
                },
            ]
        },
    ),
    (
        "ns=1;i=3020",
        "DisplacementTypeEnum",
        {
            "fields": [
                {
                    "name": "PositiveDisplacement",
                    "value": 0,
                    "display_name": "PositiveDisplacement",
                },
                {
                    "name": "DynamicDisplacement",
                    "value": 1,
                    "display_name": "DynamicDisplacement",
                },
            ]
        },
    ),
    (
        "ns=1;i=3012",
        "DrainTypeEnum",
        {
            "fields": [
                {"name": "Other", "value": 0, "display_name": "Other"},
                {
                    "name": "CapacitiveDrain",
                    "value": 1,
                    "display_name": "CapacitiveDrain",
                },
                {
                    "name": "LevelControlledDrain",
                    "value": 2,
                    "display_name": "LevelControlledDrain",
                },
                {"name": "TimedDrain", "value": 3, "display_name": "TimedDrain"},
            ]
        },
    ),
    (
        "ns=1;i=3026",
        "DryerOperatingStateEnum",
        {
            "fields": [
                {"name": "Other", "value": 0, "display_name": "Other"},
                {"name": "Stopped", "value": 1, "display_name": "Stopped"},
                {"name": "Running", "value": 2, "display_name": "Running"},
                {
                    "name": "RefrigerantCompressorStopped",
                    "value": 3,
                    "display_name": "RefrigerantCompressorStopped",
                },
                {
                    "name": "RefrigerantCompressorRunning",
                    "value": 4,
                    "display_name": "RefrigerantCompressorRunning",
                },
                {
                    "name": "PurgeValveClosed",
                    "value": 5,
                    "display_name": "PurgeValveClosed",
                },
                {
                    "name": "PurgeValveOpen",
                    "value": 6,
                    "display_name": "PurgeValveOpen",
                },
                {
                    "name": "ParallelModeOfBothVessels",
                    "value": 7,
                    "display_name": "ParallelModeOfBothVessels",
                },
                {
                    "name": "Depressurizing",
                    "value": 8,
                    "display_name": "Depressurizing",
                },
                {"name": "Desorbing", "value": 9, "display_name": "Desorbing"},
                {"name": "Cooling", "value": 10, "display_name": "Cooling"},
                {"name": "Pressurizing", "value": 11, "display_name": "Pressurizing"},
                {
                    "name": "RegeneratedVesselInStand-by",
                    "value": 12,
                    "display_name": "RegeneratedVesselInStand-by",
                },
            ]
        },
    ),
    (
        "ns=1;i=3017",
        "DryerTypeEnum",
        {
            "fields": [
                {"name": "Other", "value": 0, "display_name": "Other"},
                {
                    "name": "AbsorptionDryer",
                    "value": 1,
                    "display_name": "AbsorptionDryer",
                },
                {
                    "name": "AdsorptionDryer",
                    "value": 2,
                    "display_name": "AdsorptionDryer",
                },
                {"name": "MembraneDryer", "value": 3, "display_name": "MembraneDryer"},
                {
                    "name": "RefrigerationDryer",
                    "value": 4,
                    "display_name": "RefrigerationDryer",
                },
            ]
        },
    ),
    (
        "ns=1;i=3008",
        "FilterClassEnum",
        {
            "fields": [
                {"name": "0", "value": 0, "display_name": "0"},
                {"name": "1", "value": 1, "display_name": "1"},
                {"name": "2", "value": 2, "display_name": "2"},
                {"name": "3", "value": 3, "display_name": "3"},
                {"name": "4", "value": 4, "display_name": "4"},
                {"name": "5", "value": 5, "display_name": "5"},
                {"name": "6", "value": 6, "display_name": "6"},
                {"name": "7", "value": 7, "display_name": "7"},
                {"name": "8", "value": 8, "display_name": "8"},
                {"name": "9", "value": 9, "display_name": "9"},
                {"name": "X", "value": 10, "display_name": "X"},
            ]
        },
    ),
    (
        "ns=1;i=3005",
        "FilterTypeEnum",
        {
            "fields": [
                {"name": "Other", "value": 0, "display_name": "Other"},
                {
                    "name": "ActivatedCarbonFilter",
                    "value": 1,
                    "display_name": "ActivatedCarbonFilter",
                },
                {
                    "name": "AdsorptionFilter",
                    "value": 2,
                    "display_name": "AdsorptionFilter",
                },
                {
                    "name": "CoalescingFilter",
                    "value": 3,
                    "display_name": "CoalescingFilter",
                },
                {
                    "name": "ParticulateFilter",
                    "value": 4,
                    "display_name": "ParticulateFilter",
                },
                {"name": "FabricFilter", "value": 5, "display_name": "FabricFilter"},
                {"name": "SterileFilter", "value": 6, "display_name": "SterileFilter"},
            ]
        },
    ),
    (
        "ns=1;i=3006",
        "FluidTypeEnum",
        {
            "fields": [
                {"name": "Air", "value": 0, "display_name": "Air"},
                {"name": "Condensate", "value": 1, "display_name": "Condensate"},
                {"name": "Oil", "value": 2, "display_name": "Oil"},
                {"name": "Water", "value": 3, "display_name": "Water"},
            ]
        },
    ),
    (
        "ns=1;i=3003",
        "HealthStateEnum",
        {
            "fields": [
                {"name": "OK", "value": 0, "display_name": "OK"},
                {"name": "Warning", "value": 1, "display_name": "Warning"},
                {"name": "Error", "value": 2, "display_name": "Error"},
                {"name": "Critical", "value": 3, "display_name": "Critical"},
            ]
        },
    ),
    (
        "ns=1;i=3009",
        "IntegratedStateEnum",
        {
            "fields": [
                {
                    "name": "FullyIntegrated",
                    "value": 0,
                    "display_name": "FullyIntegrated",
                },
                {
                    "name": "PartiallyIntegrated",
                    "value": 1,
                    "display_name": "PartiallyIntegrated",
                },
                {"name": "FullyIsolated", "value": 2, "display_name": "FullyIsolated"},
            ]
        },
    ),
    (
        "ns=1;i=3016",
        "IpVersionEnum",
        {
            "fields": [
                {"name": "IPv4", "value": 0, "display_name": "IPv4"},
                {"name": "IPv6", "value": 1, "display_name": "IPv6"},
            ]
        },
    ),
    (
        "ns=1;i=3019",
        "LubricationTypeEnum",
        {
            "fields": [
                {"name": "NoLubrication", "value": 0, "display_name": "NoLubrication"},
                {"name": "OilLubricated", "value": 1, "display_name": "OilLubricated"},
                {
                    "name": "WaterLubricated",
                    "value": 2,
                    "display_name": "WaterLubricated",
                },
            ]
        },
    ),
    (
        "ns=1;i=3014",
        "OperatingStateEnum",
        {
            "fields": [
                {"name": "Other", "value": 0, "display_name": "Other"},
                {"name": "Stopped", "value": 1, "display_name": "Stopped"},
                {"name": "Starting", "value": 2, "display_name": "Starting"},
                {"name": "Stopping", "value": 3, "display_name": "Stopping"},
                {"name": "Operational", "value": 4, "display_name": "Operational"},
            ]
        },
    ),
    (
        "ns=1;i=3004",
        "ReceiverTypeEnum",
        {
            "fields": [
                {"name": "Other", "value": 0, "display_name": "Other"},
                {"name": "DryReceiver", "value": 1, "display_name": "DryReceiver"},
                {"name": "WetReceiver", "value": 2, "display_name": "WetReceiver"},
            ]
        },
    ),
    (
        "ns=1;i=3021",
        "SensorTypeEnum",
        {
            "fields": [
                {"name": "Other", "value": 0, "display_name": "Other"},
                {"name": "Ammeter", "value": 1, "display_name": "Ammeter"},
                {
                    "name": "DewPointSensor",
                    "value": 2,
                    "display_name": "DewPointSensor",
                },
                {
                    "name": "FlowRateSensor",
                    "value": 3,
                    "display_name": "FlowRateSensor",
                },
                {
                    "name": "FlowSpeedSensor",
                    "value": 4,
                    "display_name": "FlowSpeedSensor",
                },
                {
                    "name": "HumiditySensor",
                    "value": 5,
                    "display_name": "HumiditySensor",
                },
                {
                    "name": "OilConcentrationSensor",
                    "value": 6,
                    "display_name": "OilConcentrationSensor",
                },
                {
                    "name": "ParticleCounter",
                    "value": 7,
                    "display_name": "ParticleCounter",
                },
                {
                    "name": "PressureSensor",
                    "value": 8,
                    "display_name": "PressureSensor",
                },
                {
                    "name": "TemperatureSensor",
                    "value": 9,
                    "display_name": "TemperatureSensor",
                },
                {"name": "Voltmeter", "value": 10, "display_name": "Voltmeter"},
                {"name": "VolumeSensor", "value": 11, "display_name": "VolumeSensor"},
                {"name": "Wattmeter", "value": 12, "display_name": "Wattmeter"},
            ]
        },
    ),
    (
        "ns=1;i=3013",
        "SeparatorTypeEnum",
        {
            "fields": [
                {"name": "Other", "value": 0, "display_name": "Other"},
                {
                    "name": "CentrifugalOilyWaterSeparator",
                    "value": 1,
                    "display_name": "CentrifugalOilyWaterSeparator",
                },
                {
                    "name": "EmulsionSplittingSeparator",
                    "value": 2,
                    "display_name": "EmulsionSplittingSeparator",
                },
                {
                    "name": "FlotationSeparator",
                    "value": 3,
                    "display_name": "FlotationSeparator",
                },
                {
                    "name": "GravityPlateSeparator",
                    "value": 4,
                    "display_name": "GravityPlateSeparator",
                },
                {
                    "name": "HydrocycloneOilyWaterSeparator",
                    "value": 5,
                    "display_name": "HydrocycloneOilyWaterSeparator",
                },
            ]
        },
    ),
    (
        "ns=1;i=3011",
        "ValveTypeEnum",
        {
            "fields": [
                {"name": "Other", "value": 0, "display_name": "Other"},
                {"name": "CheckValve", "value": 1, "display_name": "CheckValve"},
                {
                    "name": "ContinuousValve",
                    "value": 2,
                    "display_name": "ContinuousValve",
                },
                {
                    "name": "FlowControlValve",
                    "value": 3,
                    "display_name": "FlowControlValve",
                },
                {"name": "PressureValve", "value": 4, "display_name": "PressureValve"},
                {
                    "name": "SwitchingValve",
                    "value": 5,
                    "display_name": "SwitchingValve",
                },
            ]
        },
    ),
    (
        "ns=1;i=3010",
        "SensorTechnologyOptionSet",
        {
            "fields": [
                {
                    "name": "CapacitiveSensor",
                    "value": 0,
                    "display_name": "CapacitiveSensor",
                },
                {"name": "ElectronTube", "value": 1, "display_name": "ElectronTube"},
                {
                    "name": "InductiveSensor",
                    "value": 2,
                    "display_name": "InductiveSensor",
                },
                {
                    "name": "IonizationSensor",
                    "value": 3,
                    "display_name": "IonizationSensor",
                },
                {"name": "Magnetometer", "value": 4, "display_name": "Magnetometer"},
                {"name": "OpticalSensor", "value": 5, "display_name": "OpticalSensor"},
                {
                    "name": "PiezoelectricSensor",
                    "value": 6,
                    "display_name": "PiezoelectricSensor",
                },
                {
                    "name": "ResistiveSensor",
                    "value": 7,
                    "display_name": "ResistiveSensor",
                },
                {
                    "name": "ResonantSensor",
                    "value": 8,
                    "display_name": "ResonantSensor",
                },
                {
                    "name": "TemperatureSensor",
                    "value": 9,
                    "display_name": "TemperatureSensor",
                },
                {"name": "ThermalSensor", "value": 10, "display_name": "ThermalSensor"},
                {
                    "name": "UltrasoundSensor",
                    "value": 11,
                    "display_name": "UltrasoundSensor",
                },
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = (
    [("ns=1;i=3007", "ns=1;i=5042", ["ns=1;i=3008", "ns=1;i=3008", "ns=1;i=3008"])],
    [
        "ns=1;i=3022",
        "ns=1;i=3023",
        "ns=1;i=3024",
        "ns=1;i=3025",
        "ns=1;i=3018",
        "ns=1;i=3015",
        "ns=1;i=3020",
        "ns=1;i=3012",
        "ns=1;i=3026",
        "ns=1;i=3017",
        "ns=1;i=3008",
        "ns=1;i=3005",
        "ns=1;i=3006",
        "ns=1;i=3003",
        "ns=1;i=3009",
        "ns=1;i=3016",
        "ns=1;i=3019",
        "ns=1;i=3014",
        "ns=1;i=3004",
        "ns=1;i=3021",
        "ns=1;i=3013",
        "ns=1;i=3011",
        "ns=1;i=3010",
    ],
)
_NODES: dict = {
    "datatypes": {
        "AirnetHealthStateEnum": (
            "D",
            "ns=1;i=3022",
            {"EnumValues": ("V", "ns=1;i=10608", {})},
        ),
        "AirnetIntegratedStateEnum": (
            "D",
            "ns=1;i=3023",
            {"EnumValues": ("V", "ns=1;i=10609", {})},
        ),
        "AirnetOperatingStateEnum": (
            "D",
            "ns=1;i=3024",
            {"EnumValues": ("V", "ns=1;i=10610", {})},
        ),
        "CompressorOperatingStateEnum": (
            "D",
            "ns=1;i=3025",
            {"EnumValues": ("V", "ns=1;i=10648", {})},
        ),
        "CompressorTypeEnum": (
            "D",
            "ns=1;i=3018",
            {"EnumValues": ("V", "ns=1;i=9788", {})},
        ),
        "ConverterTypeEnum": (
            "D",
            "ns=1;i=3015",
            {"EnumValues": ("V", "ns=1;i=8301", {})},
        ),
        "DisplacementTypeEnum": (
            "D",
            "ns=1;i=3020",
            {"EnumValues": ("V", "ns=1;i=7960", {})},
        ),
        "DrainTypeEnum": ("D", "ns=1;i=3012", {"EnumValues": ("V", "ns=1;i=8303", {})}),
        "DryerOperatingStateEnum": (
            "D",
            "ns=1;i=3026",
            {"EnumValues": ("V", "ns=1;i=10649", {})},
        ),
        "DryerTypeEnum": ("D", "ns=1;i=3017", {"EnumValues": ("V", "ns=1;i=7666", {})}),
        "FilterClassDataType": ("D", "ns=1;i=3007", {}),
        "FilterClassEnum": (
            "D",
            "ns=1;i=3008",
            {"EnumValues": ("V", "ns=1;i=8001", {})},
        ),
        "FilterTypeEnum": (
            "D",
            "ns=1;i=3005",
            {"EnumValues": ("V", "ns=1;i=6447", {})},
        ),
        "FluidTypeEnum": ("D", "ns=1;i=3006", {"EnumValues": ("V", "ns=1;i=8302", {})}),
        "HealthStateEnum": (
            "D",
            "ns=1;i=3003",
            {"EnumValues": ("V", "ns=1;i=10645", {})},
        ),
        "IntegratedStateEnum": (
            "D",
            "ns=1;i=3009",
            {"EnumValues": ("V", "ns=1;i=10646", {})},
        ),
        "IpVersionEnum": (
            "D",
            "ns=1;i=3016",
            {"EnumValues": ("V", "ns=1;i=10529", {})},
        ),
        "LubricationTypeEnum": (
            "D",
            "ns=1;i=3019",
            {"EnumValues": ("V", "ns=1;i=9789", {})},
        ),
        "OperatingStateEnum": (
            "D",
            "ns=1;i=3014",
            {"EnumValues": ("V", "ns=1;i=10647", {})},
        ),
        "ReceiverTypeEnum": (
            "D",
            "ns=1;i=3004",
            {"EnumValues": ("V", "ns=1;i=6441", {})},
        ),
        "SensorTechnologyOptionSet": (
            "D",
            "ns=1;i=3010",
            {"OptionSetValues": ("V", "ns=1;i=6328", {})},
        ),
        "SensorTypeEnum": (
            "D",
            "ns=1;i=3021",
            {"EnumValues": ("V", "ns=1;i=6439", {})},
        ),
        "SeparatorTypeEnum": (
            "D",
            "ns=1;i=3013",
            {"EnumValues": ("V", "ns=1;i=8798", {})},
        ),
        "ValveTypeEnum": ("D", "ns=1;i=3011", {"EnumValues": ("V", "ns=1;i=7667", {})}),
    },
    "objects": {
        "CompressorZ": (
            "O",
            "ns=1;i=5414",
            {
                "ActiveAirnet": ("V", "ns=1;i=12503", {}),
                "Configuration": ("O", "ns=1;i=5415", {}),
                "Design": (
                    "O",
                    "ns=1;i=5073",
                    {"ComponentClass": ("V", "ns=1;i=6172", {})},
                ),
                "Identification": (
                    "O",
                    "ns=1;i=5170",
                    {
                        "DeviceClass": ("V", "ns=1;i=7886", {}),
                        "Manufacturer": ("V", "ns=1;i=6134", {}),
                        "ProductInstanceUri": ("V", "ns=1;i=6380", {}),
                        "SerialNumber": ("V", "ns=1;i=6307", {}),
                    },
                ),
            },
        ),
        "Compressors": ("O", "ns=1;i=5117", {}),
        "Default Binary": ("O", "ns=1;i=5175", {}),
        "Default JSON": ("O", "ns=1;i=5177", {}),
        "Default XML": ("O", "ns=1;i=5176", {}),
        "TypeDictionary": (
            "V",
            "ns=1;i=6025",
            {
                "FilterClassDataType": ("V", "ns=1;i=6446", {}),
                "NamespaceUri": ("V", "ns=1;i=6026", {}),
                "SensorTechnologyOptionSet": ("V", "ns=1;i=7381", {}),
            },
        ),
        "http://opcfoundation.org/UA/CAS/": (
            "O",
            "ns=1;i=5150",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=6979", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=6980", {}),
                "NamespaceUri": ("V", "ns=1;i=6981", {}),
                "NamespaceVersion": ("V", "ns=1;i=6982", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=6983", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=6984", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=6985", {}),
            },
        ),
    },
    "objtypes": {
        "AirnetComponentsType": (
            "OT",
            "ns=1;i=1050",
            {
                "<ComponentsGroup>": ("O", "ns=1;i=5193", {}),
                "ChargingSystems": ("O", "ns=1;i=5194", {}),
                "Compressors": ("O", "ns=1;i=5195", {}),
                "CondensateDrains": ("O", "ns=1;i=5196", {}),
                "CondensateSeparators": ("O", "ns=1;i=5212", {}),
                "Converters": ("O", "ns=1;i=5213", {}),
                "CoolingSystems": ("O", "ns=1;i=5214", {}),
                "Dryers": ("O", "ns=1;i=5215", {}),
                "Filters": ("O", "ns=1;i=5218", {}),
                "HeatRecoverySystems": ("O", "ns=1;i=5219", {}),
                "Receivers": ("O", "ns=1;i=5220", {}),
                "Sensors": ("O", "ns=1;i=5221", {}),
                "Valves": ("O", "ns=1;i=5222", {}),
            },
        ),
        "AirnetType": (
            "OT",
            "ns=1;i=1007",
            {
                "Ambient": (
                    "O",
                    "ns=1;i=5051",
                    {
                        "AbsolutePressure": (
                            "V",
                            "ns=1;i=7967",
                            {
                                "Definition": ("V", "ns=1;i=7971", {}),
                                "EURange": ("V", "ns=1;i=7972", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7973", {}),
                                "InstrumentRange": ("V", "ns=1;i=7974", {}),
                                "KindOfQuantity": ("V", "ns=1;i=7975", {}),
                                "ValuePrecision": ("V", "ns=1;i=7976", {}),
                            },
                        ),
                        "DewPoint": (
                            "V",
                            "ns=1;i=7968",
                            {
                                "Definition": ("V", "ns=1;i=7977", {}),
                                "EURange": ("V", "ns=1;i=7979", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7985", {}),
                                "InstrumentRange": ("V", "ns=1;i=7986", {}),
                                "KindOfQuantity": ("V", "ns=1;i=7987", {}),
                                "ValuePrecision": ("V", "ns=1;i=7988", {}),
                            },
                        ),
                        "RelativeHumidity": (
                            "V",
                            "ns=1;i=7969",
                            {
                                "Definition": ("V", "ns=1;i=7989", {}),
                                "EURange": ("V", "ns=1;i=7995", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8157", {}),
                                "InstrumentRange": ("V", "ns=1;i=8158", {}),
                                "KindOfQuantity": ("V", "ns=1;i=8159", {}),
                                "ValuePrecision": ("V", "ns=1;i=8160", {}),
                            },
                        ),
                        "Temperature": (
                            "V",
                            "ns=1;i=7970",
                            {
                                "Definition": ("V", "ns=1;i=8196", {}),
                                "EURange": ("V", "ns=1;i=8291", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8304", {}),
                                "InstrumentRange": ("V", "ns=1;i=8305", {}),
                                "KindOfQuantity": ("V", "ns=1;i=8307", {}),
                                "ValuePrecision": ("V", "ns=1;i=8308", {}),
                            },
                        ),
                    },
                ),
                "Components": (
                    "O",
                    "ns=1;i=5001",
                    {
                        "ChargingSystems": ("O", "ns=1;i=5223", {}),
                        "Compressors": ("O", "ns=1;i=5224", {}),
                        "CondensateDrains": ("O", "ns=1;i=5225", {}),
                        "CondensateSeparators": ("O", "ns=1;i=5226", {}),
                        "Converters": ("O", "ns=1;i=5227", {}),
                        "CoolingSystems": ("O", "ns=1;i=5228", {}),
                        "Dryers": ("O", "ns=1;i=5229", {}),
                        "Filters": ("O", "ns=1;i=5230", {}),
                        "HeatRecoverySystems": ("O", "ns=1;i=5231", {}),
                        "Receivers": ("O", "ns=1;i=5232", {}),
                        "Sensors": ("O", "ns=1;i=5233", {}),
                        "Valves": ("O", "ns=1;i=5234", {}),
                    },
                ),
                "Configuration": (
                    "O",
                    "ns=1;i=5015",
                    {
                        "OperatingModes": (
                            "V",
                            "ns=1;i=6265",
                            {"EnumStrings": ("V", "ns=1;i=6266", {})},
                        ),
                        "OperatingProfiles": (
                            "V",
                            "ns=1;i=6267",
                            {"EnumStrings": ("V", "ns=1;i=6268", {})},
                        ),
                        "UIElement": ("V", "ns=1;i=6232", {}),
                    },
                ),
                "ElectricalCircuit": (
                    "O",
                    "ns=1;i=5050",
                    {
                        "Delta": (
                            "O",
                            "ns=1;i=5109",
                            {
                                "ApparentPower": (
                                    "V",
                                    "ns=1;i=6681",
                                    {
                                        "Definition": ("V", "ns=1;i=8000", {}),
                                        "EURange": ("V", "ns=1;i=8031", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8030", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8032", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=8033", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8034", {}),
                                    },
                                ),
                                "Current": (
                                    "V",
                                    "ns=1;i=6682",
                                    {
                                        "Definition": ("V", "ns=1;i=8035", {}),
                                        "EURange": ("V", "ns=1;i=8037", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8036", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8038", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=8039", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8040", {}),
                                    },
                                ),
                                "Energy": (
                                    "V",
                                    "ns=1;i=7817",
                                    {
                                        "Definition": ("V", "ns=1;i=8041", {}),
                                        "EURange": ("V", "ns=1;i=8043", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8042", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8044", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8045", {}),
                                    },
                                ),
                                "Power": (
                                    "V",
                                    "ns=1;i=7818",
                                    {
                                        "Definition": ("V", "ns=1;i=8046", {}),
                                        "EURange": ("V", "ns=1;i=8048", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8047", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8049", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=8050", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8051", {}),
                                    },
                                ),
                                "ResetStatistics": ("M", "ns=1;i=7819", {}),
                                "StartTime": ("V", "ns=1;i=7820", {}),
                                "Voltage": (
                                    "V",
                                    "ns=1;i=7821",
                                    {
                                        "Definition": ("V", "ns=1;i=8052", {}),
                                        "EURange": ("V", "ns=1;i=8054", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8053", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8055", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=8056", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8218", {}),
                                    },
                                ),
                            },
                        ),
                        "Input": (
                            "O",
                            "ns=1;i=5052",
                            {
                                "ApparentPower": (
                                    "V",
                                    "ns=1;i=9602",
                                    {
                                        "Definition": ("V", "ns=1;i=9659", {}),
                                        "EURange": ("V", "ns=1;i=9661", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9660", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9662", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9663", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9664", {}),
                                    },
                                ),
                                "Current": (
                                    "V",
                                    "ns=1;i=9603",
                                    {
                                        "Definition": ("V", "ns=1;i=9665", {}),
                                        "EURange": ("V", "ns=1;i=9667", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9666", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9668", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9669", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9670", {}),
                                    },
                                ),
                                "Energy": (
                                    "V",
                                    "ns=1;i=9604",
                                    {
                                        "Definition": ("V", "ns=1;i=9671", {}),
                                        "EURange": ("V", "ns=1;i=9673", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9672", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9674", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9675", {}),
                                    },
                                ),
                                "Power": (
                                    "V",
                                    "ns=1;i=9605",
                                    {
                                        "Definition": ("V", "ns=1;i=9676", {}),
                                        "EURange": ("V", "ns=1;i=9678", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9677", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9679", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9680", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9681", {}),
                                    },
                                ),
                                "ResetStatistics": ("M", "ns=1;i=9606", {}),
                                "StartTime": ("V", "ns=1;i=9607", {}),
                                "Voltage": (
                                    "V",
                                    "ns=1;i=9608",
                                    {
                                        "Definition": ("V", "ns=1;i=9682", {}),
                                        "EURange": ("V", "ns=1;i=9684", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9683", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9685", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9686", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9689", {}),
                                    },
                                ),
                            },
                        ),
                        "Output": (
                            "O",
                            "ns=1;i=5110",
                            {
                                "ApparentPower": (
                                    "V",
                                    "ns=1;i=9976",
                                    {
                                        "Definition": ("V", "ns=1;i=10033", {}),
                                        "EURange": ("V", "ns=1;i=10035", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10034", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10036", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=10037", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10038", {}),
                                    },
                                ),
                                "Current": (
                                    "V",
                                    "ns=1;i=9977",
                                    {
                                        "Definition": ("V", "ns=1;i=10039", {}),
                                        "EURange": ("V", "ns=1;i=10041", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10040", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10042", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=10043", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10044", {}),
                                    },
                                ),
                                "Energy": (
                                    "V",
                                    "ns=1;i=9978",
                                    {
                                        "Definition": ("V", "ns=1;i=10045", {}),
                                        "EURange": ("V", "ns=1;i=10047", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10046", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10048", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10049", {}),
                                    },
                                ),
                                "Power": (
                                    "V",
                                    "ns=1;i=9979",
                                    {
                                        "Definition": ("V", "ns=1;i=10050", {}),
                                        "EURange": ("V", "ns=1;i=10052", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10051", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10053", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=10054", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10055", {}),
                                    },
                                ),
                                "ResetStatistics": ("M", "ns=1;i=9980", {}),
                                "StartTime": ("V", "ns=1;i=9981", {}),
                                "Voltage": (
                                    "V",
                                    "ns=1;i=9982",
                                    {
                                        "Definition": ("V", "ns=1;i=10056", {}),
                                        "EURange": ("V", "ns=1;i=10058", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10057", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10059", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=10060", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10061", {}),
                                    },
                                ),
                            },
                        ),
                    },
                ),
                "Identification": (
                    "O",
                    "ns=1;i=5009",
                    {
                        "AssetId": ("V", "ns=1;i=6180", {}),
                        "ComponentName": ("V", "ns=1;i=6181", {}),
                        "UIElement": ("V", "ns=1;i=6182", {}),
                    },
                ),
                "Operational": (
                    "O",
                    "ns=1;i=5008",
                    {
                        "AirDeliveryRate": (
                            "V",
                            "ns=1;i=10553",
                            {
                                "Definition": ("V", "ns=1;i=10559", {}),
                                "EURange": ("V", "ns=1;i=10560", {}),
                                "EngineeringUnits": ("V", "ns=1;i=10561", {}),
                                "InstrumentRange": ("V", "ns=1;i=10562", {}),
                                "ValuePrecision": ("V", "ns=1;i=10563", {}),
                            },
                        ),
                        "CompressorsIntegrated": (
                            "V",
                            "ns=1;i=6073",
                            {
                                "Definition": ("V", "ns=1;i=6035", {}),
                                "EURange": ("V", "ns=1;i=6036", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6040", {}),
                                "InstrumentRange": ("V", "ns=1;i=6041", {}),
                                "ValuePrecision": ("V", "ns=1;i=6074", {}),
                            },
                        ),
                        "CompressorsIsolated": (
                            "V",
                            "ns=1;i=6075",
                            {
                                "Definition": ("V", "ns=1;i=6684", {}),
                                "EURange": ("V", "ns=1;i=10076", {}),
                                "EngineeringUnits": ("V", "ns=1;i=10075", {}),
                                "InstrumentRange": ("V", "ns=1;i=10092", {}),
                                "ValuePrecision": ("V", "ns=1;i=10093", {}),
                            },
                        ),
                        "CompressorsNotAvailable": (
                            "V",
                            "ns=1;i=6078",
                            {
                                "Definition": ("V", "ns=1;i=6100", {}),
                                "EURange": ("V", "ns=1;i=6102", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6101", {}),
                                "InstrumentRange": ("V", "ns=1;i=6103", {}),
                                "ValuePrecision": ("V", "ns=1;i=6104", {}),
                            },
                        ),
                        "ControlPressure": (
                            "V",
                            "ns=1;i=8290",
                            {
                                "Definition": ("V", "ns=1;i=8292", {}),
                                "EURange": ("V", "ns=1;i=8293", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8294", {}),
                                "InstrumentRange": ("V", "ns=1;i=8295", {}),
                                "ValuePrecision": ("V", "ns=1;i=8296", {}),
                            },
                        ),
                        "HealthState": (
                            "V",
                            "ns=1;i=6223",
                            {
                                "Definition": ("V", "ns=1;i=6658", {}),
                                "ValuePrecision": ("V", "ns=1;i=6676", {}),
                            },
                        ),
                        "IntegratedState": (
                            "V",
                            "ns=1;i=6656",
                            {
                                "Definition": ("V", "ns=1;i=8216", {}),
                                "ValuePrecision": ("V", "ns=1;i=8230", {}),
                            },
                        ),
                        "OperatingState": (
                            "V",
                            "ns=1;i=6657",
                            {
                                "Definition": ("V", "ns=1;i=8231", {}),
                                "ValuePrecision": ("V", "ns=1;i=10650", {}),
                            },
                        ),
                        "SpecificEnergy": (
                            "V",
                            "ns=1;i=10555",
                            {
                                "Definition": ("V", "ns=1;i=10564", {}),
                                "EURange": ("V", "ns=1;i=10565", {}),
                                "EngineeringUnits": ("V", "ns=1;i=10566", {}),
                                "InstrumentRange": ("V", "ns=1;i=10567", {}),
                                "ValuePrecision": ("V", "ns=1;i=10568", {}),
                            },
                        ),
                        "SpecificEnergyCost": (
                            "V",
                            "ns=1;i=10557",
                            {
                                "Definition": ("V", "ns=1;i=10569", {}),
                                "EURange": ("V", "ns=1;i=10570", {}),
                                "EngineeringUnits": ("V", "ns=1;i=10571", {}),
                                "InstrumentRange": ("V", "ns=1;i=10572", {}),
                                "ValuePrecision": ("V", "ns=1;i=10573", {}),
                            },
                        ),
                        "UIElement": ("V", "ns=1;i=8479", {}),
                        "VolumeFlowRateAvailable": (
                            "V",
                            "ns=1;i=6080",
                            {
                                "Definition": ("V", "ns=1;i=6106", {}),
                                "EURange": ("V", "ns=1;i=6107", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6108", {}),
                                "InstrumentRange": ("V", "ns=1;i=10625", {}),
                                "ValuePrecision": ("V", "ns=1;i=10626", {}),
                            },
                        ),
                        "VolumeFlowRateUnavailable": (
                            "V",
                            "ns=1;i=6082",
                            {
                                "Definition": ("V", "ns=1;i=6109", {}),
                                "EURange": ("V", "ns=1;i=6110", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6111", {}),
                                "InstrumentRange": ("V", "ns=1;i=10629", {}),
                                "ValuePrecision": ("V", "ns=1;i=10630", {}),
                            },
                        ),
                    },
                ),
                "ProcessFluidCircuit": (
                    "O",
                    "ns=1;i=5031",
                    {
                        "Delta": (
                            "O",
                            "ns=1;i=5034",
                            {
                                "AbsolutePressure": (
                                    "V",
                                    "ns=1;i=7812",
                                    {
                                        "Definition": ("V", "ns=1;i=7945", {}),
                                        "EURange": ("V", "ns=1;i=7947", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7946", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7948", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7949", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7950", {}),
                                    },
                                ),
                                "AccumulatedVolume": (
                                    "V",
                                    "ns=1;i=6907",
                                    {
                                        "Definition": ("V", "ns=1;i=6014", {}),
                                        "EURange": ("V", "ns=1;i=7217", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7216", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7218", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7219", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7220", {}),
                                    },
                                ),
                                "DewPoint": (
                                    "V",
                                    "ns=1;i=6908",
                                    {
                                        "Definition": ("V", "ns=1;i=7221", {}),
                                        "EURange": ("V", "ns=1;i=7252", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7251", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7253", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7254", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7255", {}),
                                    },
                                ),
                                "GaugePressure": (
                                    "V",
                                    "ns=1;i=6909",
                                    {
                                        "Definition": ("V", "ns=1;i=7256", {}),
                                        "EURange": ("V", "ns=1;i=7264", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7257", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7265", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7266", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7267", {}),
                                    },
                                ),
                                "MassFlowRate": (
                                    "V",
                                    "ns=1;i=6910",
                                    {
                                        "Definition": ("V", "ns=1;i=7268", {}),
                                        "EURange": ("V", "ns=1;i=7270", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7269", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7271", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7273", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7274", {}),
                                    },
                                ),
                                "OilConcentration": (
                                    "V",
                                    "ns=1;i=6911",
                                    {
                                        "Definition": ("V", "ns=1;i=7275", {}),
                                        "EURange": ("V", "ns=1;i=7289", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7276", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7290", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7291", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7292", {}),
                                    },
                                ),
                                "ParticlesPerSizeRange": (
                                    "O",
                                    "ns=1;i=5041",
                                    {
                                        "Fine": (
                                            "V",
                                            "ns=1;i=6430",
                                            {
                                                "Definition": ("V", "ns=1;i=7313", {}),
                                                "EURange": ("V", "ns=1;i=7315", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=7314",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=7316",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8707",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=7317",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Large": (
                                            "V",
                                            "ns=1;i=6431",
                                            {
                                                "Definition": ("V", "ns=1;i=8830", {}),
                                                "EURange": ("V", "ns=1;i=8832", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=8831",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=8842",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8843",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=8852",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Medium": (
                                            "V",
                                            "ns=1;i=6432",
                                            {
                                                "Definition": ("V", "ns=1;i=9268", {}),
                                                "EURange": ("V", "ns=1;i=9275", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9269",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9276",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9277",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9278",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "RelativeHumidity": (
                                    "V",
                                    "ns=1;i=7009",
                                    {
                                        "Definition": ("V", "ns=1;i=7293", {}),
                                        "EURange": ("V", "ns=1;i=7295", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7294", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7296", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7321", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7322", {}),
                                    },
                                ),
                                "ResetStatistics": ("M", "ns=1;i=7010", {}),
                                "StartTime": ("V", "ns=1;i=7011", {}),
                                "Temperature": (
                                    "V",
                                    "ns=1;i=7012",
                                    {
                                        "Definition": ("V", "ns=1;i=7323", {}),
                                        "EURange": ("V", "ns=1;i=7325", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7324", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7326", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7327", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7328", {}),
                                    },
                                ),
                                "Volume": (
                                    "V",
                                    "ns=1;i=7052",
                                    {
                                        "Definition": ("V", "ns=1;i=7329", {}),
                                        "EURange": ("V", "ns=1;i=7331", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7330", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7332", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7333", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7334", {}),
                                    },
                                ),
                                "VolumeFlowRate": (
                                    "V",
                                    "ns=1;i=7053",
                                    {
                                        "Definition": ("V", "ns=1;i=7335", {}),
                                        "EURange": ("V", "ns=1;i=7344", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7336", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7345", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7346", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7347", {}),
                                    },
                                ),
                            },
                        ),
                        "FluidType": (
                            "V",
                            "ns=1;i=6009",
                            {"Definition": ("V", "ns=1;i=6013", {})},
                        ),
                        "Inlet": (
                            "O",
                            "ns=1;i=5037",
                            {
                                "AbsolutePressure": (
                                    "V",
                                    "ns=1;i=7285",
                                    {
                                        "Definition": ("V", "ns=1;i=9031", {}),
                                        "EURange": ("V", "ns=1;i=9033", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9032", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9034", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9035", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9036", {}),
                                    },
                                ),
                                "AccumulatedVolume": (
                                    "V",
                                    "ns=1;i=7286",
                                    {
                                        "Definition": ("V", "ns=1;i=9037", {}),
                                        "EURange": ("V", "ns=1;i=9039", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9038", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9040", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9041", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9042", {}),
                                    },
                                ),
                                "DewPoint": (
                                    "V",
                                    "ns=1;i=7287",
                                    {
                                        "Definition": ("V", "ns=1;i=9043", {}),
                                        "EURange": ("V", "ns=1;i=9045", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9044", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9046", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9047", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9048", {}),
                                    },
                                ),
                                "GaugePressure": (
                                    "V",
                                    "ns=1;i=7288",
                                    {
                                        "Definition": ("V", "ns=1;i=9049", {}),
                                        "EURange": ("V", "ns=1;i=9051", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9050", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9052", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9068", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9069", {}),
                                    },
                                ),
                                "MassFlowRate": (
                                    "V",
                                    "ns=1;i=7337",
                                    {
                                        "Definition": ("V", "ns=1;i=9070", {}),
                                        "EURange": ("V", "ns=1;i=9072", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9071", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9073", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9074", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9076", {}),
                                    },
                                ),
                                "OilConcentration": (
                                    "V",
                                    "ns=1;i=7338",
                                    {
                                        "Definition": ("V", "ns=1;i=9077", {}),
                                        "EURange": ("V", "ns=1;i=9080", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9079", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9081", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9082", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9085", {}),
                                    },
                                ),
                                "ParticlesPerSizeRange": (
                                    "O",
                                    "ns=1;i=5153",
                                    {
                                        "Fine": (
                                            "V",
                                            "ns=1;i=6542",
                                            {
                                                "Definition": ("V", "ns=1;i=7709", {}),
                                                "EURange": ("V", "ns=1;i=7711", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=7710",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=7712",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8712",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=7728",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Large": (
                                            "V",
                                            "ns=1;i=6543",
                                            {
                                                "Definition": ("V", "ns=1;i=8962", {}),
                                                "EURange": ("V", "ns=1;i=9016", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=8963",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9017",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9018",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9019",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Medium": (
                                            "V",
                                            "ns=1;i=6546",
                                            {
                                                "Definition": ("V", "ns=1;i=10254", {}),
                                                "EURange": ("V", "ns=1;i=10256", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10255",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10257",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10258",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10323",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "RelativeHumidity": (
                                    "V",
                                    "ns=1;i=8802",
                                    {
                                        "Definition": ("V", "ns=1;i=9101", {}),
                                        "EURange": ("V", "ns=1;i=9103", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9102", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9104", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9109", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9110", {}),
                                    },
                                ),
                                "ResetStatistics": ("M", "ns=1;i=8803", {}),
                                "StartTime": ("V", "ns=1;i=8804", {}),
                                "Temperature": (
                                    "V",
                                    "ns=1;i=8805",
                                    {
                                        "Definition": ("V", "ns=1;i=9111", {}),
                                        "EURange": ("V", "ns=1;i=9113", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9112", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9114", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9115", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9116", {}),
                                    },
                                ),
                                "Volume": (
                                    "V",
                                    "ns=1;i=8806",
                                    {
                                        "Definition": ("V", "ns=1;i=9117", {}),
                                        "EURange": ("V", "ns=1;i=9119", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9118", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9120", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9121", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9122", {}),
                                    },
                                ),
                                "VolumeFlowRate": (
                                    "V",
                                    "ns=1;i=8807",
                                    {
                                        "Definition": ("V", "ns=1;i=9123", {}),
                                        "EURange": ("V", "ns=1;i=9125", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9124", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9126", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9127", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9128", {}),
                                    },
                                ),
                            },
                        ),
                        "Outlet": (
                            "O",
                            "ns=1;i=5040",
                            {
                                "AbsolutePressure": (
                                    "V",
                                    "ns=1;i=9320",
                                    {
                                        "Definition": ("V", "ns=1;i=9426", {}),
                                        "EURange": ("V", "ns=1;i=9428", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9427", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9429", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9430", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9431", {}),
                                    },
                                ),
                                "AccumulatedVolume": (
                                    "V",
                                    "ns=1;i=9321",
                                    {
                                        "Definition": ("V", "ns=1;i=9432", {}),
                                        "EURange": ("V", "ns=1;i=9434", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9433", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9435", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9436", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9437", {}),
                                    },
                                ),
                                "DewPoint": (
                                    "V",
                                    "ns=1;i=9322",
                                    {
                                        "Definition": ("V", "ns=1;i=9438", {}),
                                        "EURange": ("V", "ns=1;i=9440", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9439", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9443", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9444", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9445", {}),
                                    },
                                ),
                                "GaugePressure": (
                                    "V",
                                    "ns=1;i=9323",
                                    {
                                        "Definition": ("V", "ns=1;i=9446", {}),
                                        "EURange": ("V", "ns=1;i=9448", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9447", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9449", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9450", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9451", {}),
                                    },
                                ),
                                "MassFlowRate": (
                                    "V",
                                    "ns=1;i=9324",
                                    {
                                        "Definition": ("V", "ns=1;i=9452", {}),
                                        "EURange": ("V", "ns=1;i=9454", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9453", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9455", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9456", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9457", {}),
                                    },
                                ),
                                "OilConcentration": (
                                    "V",
                                    "ns=1;i=9325",
                                    {
                                        "Definition": ("V", "ns=1;i=9458", {}),
                                        "EURange": ("V", "ns=1;i=9460", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9459", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9461", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9462", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9463", {}),
                                    },
                                ),
                                "ParticlesPerSizeRange": (
                                    "O",
                                    "ns=1;i=5046",
                                    {
                                        "Fine": (
                                            "V",
                                            "ns=1;i=6442",
                                            {
                                                "Definition": ("V", "ns=1;i=7656", {}),
                                                "EURange": ("V", "ns=1;i=7658", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=7657",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=7660",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8709",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=7698",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Large": (
                                            "V",
                                            "ns=1;i=6444",
                                            {
                                                "Definition": ("V", "ns=1;i=8926", {}),
                                                "EURange": ("V", "ns=1;i=8928", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=8927",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=8929",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8930",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=8931",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Medium": (
                                            "V",
                                            "ns=1;i=6453",
                                            {
                                                "Definition": ("V", "ns=1;i=9538", {}),
                                                "EURange": ("V", "ns=1;i=9540", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9539",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9720",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9721",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9722",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "RelativeHumidity": (
                                    "V",
                                    "ns=1;i=9326",
                                    {
                                        "Definition": ("V", "ns=1;i=9464", {}),
                                        "EURange": ("V", "ns=1;i=9466", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9465", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9467", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9468", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9469", {}),
                                    },
                                ),
                                "ResetStatistics": ("M", "ns=1;i=9327", {}),
                                "StartTime": ("V", "ns=1;i=9328", {}),
                                "Temperature": (
                                    "V",
                                    "ns=1;i=9329",
                                    {
                                        "Definition": ("V", "ns=1;i=9470", {}),
                                        "EURange": ("V", "ns=1;i=9472", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9471", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9473", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9474", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9475", {}),
                                    },
                                ),
                                "Volume": (
                                    "V",
                                    "ns=1;i=9330",
                                    {
                                        "Definition": ("V", "ns=1;i=9476", {}),
                                        "EURange": ("V", "ns=1;i=9478", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9477", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9479", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9480", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9481", {}),
                                    },
                                ),
                                "VolumeFlowRate": (
                                    "V",
                                    "ns=1;i=9331",
                                    {
                                        "Definition": ("V", "ns=1;i=9482", {}),
                                        "EURange": ("V", "ns=1;i=9484", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9483", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9485", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9486", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9487", {}),
                                    },
                                ),
                            },
                        ),
                    },
                ),
            },
        ),
        "AirnetsType": (
            "OT",
            "ns=1;i=1038",
            {
                "<Component>": (
                    "O",
                    "ns=1;i=5029",
                    {
                        "Ambient": (
                            "O",
                            "ns=1;i=5032",
                            {
                                "AbsolutePressure": (
                                    "V",
                                    "ns=1;i=6203",
                                    {
                                        "Definition": ("V", "ns=1;i=8070", {}),
                                        "EURange": ("V", "ns=1;i=8071", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8072", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8073", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=8074", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8075", {}),
                                    },
                                ),
                                "DewPoint": (
                                    "V",
                                    "ns=1;i=6204",
                                    {
                                        "Definition": ("V", "ns=1;i=8076", {}),
                                        "EURange": ("V", "ns=1;i=8077", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8078", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8079", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=8080", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8081", {}),
                                    },
                                ),
                                "RelativeHumidity": (
                                    "V",
                                    "ns=1;i=6213",
                                    {
                                        "Definition": ("V", "ns=1;i=8082", {}),
                                        "EURange": ("V", "ns=1;i=8083", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8084", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8085", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=8086", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8087", {}),
                                    },
                                ),
                                "Temperature": (
                                    "V",
                                    "ns=1;i=6214",
                                    {
                                        "Definition": ("V", "ns=1;i=8088", {}),
                                        "EURange": ("V", "ns=1;i=8089", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8090", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8091", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=8092", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8093", {}),
                                    },
                                ),
                            },
                        ),
                        "Components": (
                            "O",
                            "ns=1;i=5047",
                            {
                                "ChargingSystems": ("O", "ns=1;i=5069", {}),
                                "Compressors": ("O", "ns=1;i=5095", {}),
                                "CondensateDrains": ("O", "ns=1;i=5105", {}),
                                "CondensateSeparators": ("O", "ns=1;i=5106", {}),
                                "Converters": ("O", "ns=1;i=5107", {}),
                                "CoolingSystems": ("O", "ns=1;i=5111", {}),
                                "Dryers": ("O", "ns=1;i=5113", {}),
                                "Filters": ("O", "ns=1;i=5114", {}),
                                "HeatRecoverySystems": ("O", "ns=1;i=5118", {}),
                                "Receivers": ("O", "ns=1;i=5119", {}),
                                "Sensors": ("O", "ns=1;i=5122", {}),
                                "Valves": ("O", "ns=1;i=5128", {}),
                            },
                        ),
                        "Configuration": (
                            "O",
                            "ns=1;i=5049",
                            {
                                "OperatingModes": (
                                    "V",
                                    "ns=1;i=6448",
                                    {"EnumStrings": ("V", "ns=1;i=6449", {})},
                                ),
                                "OperatingProfiles": (
                                    "V",
                                    "ns=1;i=6193",
                                    {"EnumStrings": ("V", "ns=1;i=6202", {})},
                                ),
                                "UIElement": ("V", "ns=1;i=6233", {}),
                            },
                        ),
                        "ElectricalCircuit": (
                            "O",
                            "ns=1;i=5053",
                            {
                                "Delta": (
                                    "O",
                                    "ns=1;i=5134",
                                    {
                                        "ApparentPower": (
                                            "V",
                                            "ns=1;i=8094",
                                            {
                                                "Definition": ("V", "ns=1;i=8654", {}),
                                                "EURange": ("V", "ns=1;i=8655", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=8656",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=8657",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8658",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=8659",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Current": (
                                            "V",
                                            "ns=1;i=8095",
                                            {
                                                "Definition": ("V", "ns=1;i=8660", {}),
                                                "EURange": ("V", "ns=1;i=8661", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=8662",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=8663",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8664",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=8665",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Energy": (
                                            "V",
                                            "ns=1;i=8096",
                                            {
                                                "Definition": ("V", "ns=1;i=8666", {}),
                                                "EURange": ("V", "ns=1;i=8667", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=8668",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=8669",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=8670",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Power": (
                                            "V",
                                            "ns=1;i=8097",
                                            {
                                                "Definition": ("V", "ns=1;i=8671", {}),
                                                "EURange": ("V", "ns=1;i=8672", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=8673",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=8674",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8675",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=8676",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "ResetStatistics": ("M", "ns=1;i=8098", {}),
                                        "StartTime": ("V", "ns=1;i=8134", {}),
                                        "Voltage": (
                                            "V",
                                            "ns=1;i=8135",
                                            {
                                                "Definition": ("V", "ns=1;i=8677", {}),
                                                "EURange": ("V", "ns=1;i=8678", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=8679",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=8680",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8681",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=8682",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "Input": (
                                    "O",
                                    "ns=1;i=5139",
                                    {
                                        "ApparentPower": (
                                            "V",
                                            "ns=1;i=8136",
                                            {
                                                "Definition": ("V", "ns=1;i=8683", {}),
                                                "EURange": ("V", "ns=1;i=8684", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=8685",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=8686",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8687",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=8688",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Current": (
                                            "V",
                                            "ns=1;i=8137",
                                            {
                                                "Definition": ("V", "ns=1;i=8689", {}),
                                                "EURange": ("V", "ns=1;i=8690", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=8691",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=8692",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8693",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=8694",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Energy": (
                                            "V",
                                            "ns=1;i=8138",
                                            {
                                                "Definition": ("V", "ns=1;i=8695", {}),
                                                "EURange": ("V", "ns=1;i=8696", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=8697",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=8698",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=8699",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Power": (
                                            "V",
                                            "ns=1;i=8139",
                                            {
                                                "Definition": ("V", "ns=1;i=8700", {}),
                                                "EURange": ("V", "ns=1;i=8701", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=8702",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=8703",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8704",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=8705",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "ResetStatistics": ("M", "ns=1;i=8140", {}),
                                        "StartTime": ("V", "ns=1;i=8141", {}),
                                        "Voltage": (
                                            "V",
                                            "ns=1;i=8142",
                                            {
                                                "Definition": ("V", "ns=1;i=8706", {}),
                                                "EURange": ("V", "ns=1;i=8710", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=8713",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=8714",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8715",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=8716",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "Output": (
                                    "O",
                                    "ns=1;i=5147",
                                    {
                                        "ApparentPower": (
                                            "V",
                                            "ns=1;i=8143",
                                            {
                                                "Definition": ("V", "ns=1;i=8784", {}),
                                                "EURange": ("V", "ns=1;i=8785", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=8786",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=8787",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8788",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=8789",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Current": (
                                            "V",
                                            "ns=1;i=8144",
                                            {
                                                "Definition": ("V", "ns=1;i=8790", {}),
                                                "EURange": ("V", "ns=1;i=8792", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=8794",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=8795",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8796",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=8797",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Energy": (
                                            "V",
                                            "ns=1;i=8145",
                                            {
                                                "Definition": ("V", "ns=1;i=8801", {}),
                                                "EURange": ("V", "ns=1;i=8932", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=8933",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=8938",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=8939",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Power": (
                                            "V",
                                            "ns=1;i=8146",
                                            {
                                                "Definition": ("V", "ns=1;i=8940", {}),
                                                "EURange": ("V", "ns=1;i=8941", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9026",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9027",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9028",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9029",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "ResetStatistics": ("M", "ns=1;i=8147", {}),
                                        "StartTime": ("V", "ns=1;i=8148", {}),
                                        "Voltage": (
                                            "V",
                                            "ns=1;i=8150",
                                            {
                                                "Definition": ("V", "ns=1;i=9030", {}),
                                                "EURange": ("V", "ns=1;i=9053", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9090",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9091",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9092",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9093",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                            },
                        ),
                        "Identification": (
                            "O",
                            "ns=1;i=5030",
                            {
                                "AssetId": ("V", "ns=1;i=6190", {}),
                                "ComponentName": ("V", "ns=1;i=6191", {}),
                                "UIElement": ("V", "ns=1;i=6192", {}),
                            },
                        ),
                        "Operational": (
                            "O",
                            "ns=1;i=5056",
                            {
                                "AirDeliveryRate": (
                                    "V",
                                    "ns=1;i=6455",
                                    {
                                        "Definition": ("V", "ns=1;i=8151", {}),
                                        "EURange": ("V", "ns=1;i=8152", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8153", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8154", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8155", {}),
                                    },
                                ),
                                "CompressorsIntegrated": (
                                    "V",
                                    "ns=1;i=6456",
                                    {
                                        "Definition": ("V", "ns=1;i=8156", {}),
                                        "EURange": ("V", "ns=1;i=8163", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8164", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8165", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8166", {}),
                                    },
                                ),
                                "CompressorsIsolated": (
                                    "V",
                                    "ns=1;i=7720",
                                    {
                                        "Definition": ("V", "ns=1;i=8167", {}),
                                        "EURange": ("V", "ns=1;i=8168", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8169", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8170", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8171", {}),
                                    },
                                ),
                                "CompressorsNotAvailable": (
                                    "V",
                                    "ns=1;i=7721",
                                    {
                                        "Definition": ("V", "ns=1;i=8172", {}),
                                        "EURange": ("V", "ns=1;i=8173", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8370", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8371", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8372", {}),
                                    },
                                ),
                                "ControlPressure": (
                                    "V",
                                    "ns=1;i=7722",
                                    {
                                        "Definition": ("V", "ns=1;i=8373", {}),
                                        "EURange": ("V", "ns=1;i=8374", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8375", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8376", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8377", {}),
                                    },
                                ),
                                "HealthState": (
                                    "V",
                                    "ns=1;i=7723",
                                    {
                                        "Definition": ("V", "ns=1;i=8378", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8379", {}),
                                    },
                                ),
                                "IntegratedState": (
                                    "V",
                                    "ns=1;i=7724",
                                    {
                                        "Definition": ("V", "ns=1;i=8380", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8381", {}),
                                    },
                                ),
                                "OperatingState": (
                                    "V",
                                    "ns=1;i=7725",
                                    {
                                        "Definition": ("V", "ns=1;i=8382", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8383", {}),
                                    },
                                ),
                                "SpecificEnergy": (
                                    "V",
                                    "ns=1;i=7726",
                                    {
                                        "Definition": ("V", "ns=1;i=8384", {}),
                                        "EURange": ("V", "ns=1;i=8385", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8386", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8387", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8388", {}),
                                    },
                                ),
                                "SpecificEnergyCost": (
                                    "V",
                                    "ns=1;i=7727",
                                    {
                                        "Definition": ("V", "ns=1;i=8389", {}),
                                        "EURange": ("V", "ns=1;i=8396", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8397", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8398", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8399", {}),
                                    },
                                ),
                                "UIElement": ("V", "ns=1;i=7743", {}),
                                "VolumeFlowRateAvailable": (
                                    "V",
                                    "ns=1;i=7744",
                                    {
                                        "Definition": ("V", "ns=1;i=8400", {}),
                                        "EURange": ("V", "ns=1;i=8401", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8402", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8403", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8404", {}),
                                    },
                                ),
                                "VolumeFlowRateUnavailable": (
                                    "V",
                                    "ns=1;i=7769",
                                    {
                                        "Definition": ("V", "ns=1;i=8405", {}),
                                        "EURange": ("V", "ns=1;i=8406", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8407", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8408", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8409", {}),
                                    },
                                ),
                            },
                        ),
                        "ProcessFluidCircuit": (
                            "O",
                            "ns=1;i=5063",
                            {
                                "Delta": (
                                    "O",
                                    "ns=1;i=5151",
                                    {
                                        "AbsolutePressure": (
                                            "V",
                                            "ns=1;i=8410",
                                            {
                                                "Definition": ("V", "ns=1;i=9094", {}),
                                                "EURange": ("V", "ns=1;i=9095", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9174",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9723",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9754",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9755",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "AccumulatedVolume": (
                                            "V",
                                            "ns=1;i=8411",
                                            {
                                                "Definition": ("V", "ns=1;i=9786", {}),
                                                "EURange": ("V", "ns=1;i=9787", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9792",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9793",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9794",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9795",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DewPoint": (
                                            "V",
                                            "ns=1;i=8412",
                                            {
                                                "Definition": ("V", "ns=1;i=9797", {}),
                                                "EURange": ("V", "ns=1;i=9798", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9799",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9800",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9825",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9826",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "GaugePressure": (
                                            "V",
                                            "ns=1;i=8413",
                                            {
                                                "Definition": ("V", "ns=1;i=9827", {}),
                                                "EURange": ("V", "ns=1;i=9828", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9831",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9832",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9835",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9836",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "MassFlowRate": (
                                            "V",
                                            "ns=1;i=8414",
                                            {
                                                "Definition": ("V", "ns=1;i=9837", {}),
                                                "EURange": ("V", "ns=1;i=9838", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9839",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9840",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9841",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9842",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "OilConcentration": (
                                            "V",
                                            "ns=1;i=8415",
                                            {
                                                "Definition": ("V", "ns=1;i=9843", {}),
                                                "EURange": ("V", "ns=1;i=9844", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9845",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9846",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9847",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9848",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "ParticlesPerSizeRange": (
                                            "O",
                                            "ns=1;i=5162",
                                            {
                                                "Fine": (
                                                    "V",
                                                    "ns=1;i=8416",
                                                    {
                                                        "Definition": (
                                                            "V",
                                                            "ns=1;i=10416",
                                                            {},
                                                        ),
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=10417",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=10418",
                                                            {},
                                                        ),
                                                        "InstrumentRange": (
                                                            "V",
                                                            "ns=1;i=10419",
                                                            {},
                                                        ),
                                                        "KindOfQuantity": (
                                                            "V",
                                                            "ns=1;i=10420",
                                                            {},
                                                        ),
                                                        "ValuePrecision": (
                                                            "V",
                                                            "ns=1;i=10421",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "Large": (
                                                    "V",
                                                    "ns=1;i=8417",
                                                    {
                                                        "Definition": (
                                                            "V",
                                                            "ns=1;i=10422",
                                                            {},
                                                        ),
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=10423",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=10424",
                                                            {},
                                                        ),
                                                        "InstrumentRange": (
                                                            "V",
                                                            "ns=1;i=10425",
                                                            {},
                                                        ),
                                                        "KindOfQuantity": (
                                                            "V",
                                                            "ns=1;i=10426",
                                                            {},
                                                        ),
                                                        "ValuePrecision": (
                                                            "V",
                                                            "ns=1;i=10427",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "Medium": (
                                                    "V",
                                                    "ns=1;i=8418",
                                                    {
                                                        "Definition": (
                                                            "V",
                                                            "ns=1;i=10428",
                                                            {},
                                                        ),
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=10429",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=10430",
                                                            {},
                                                        ),
                                                        "InstrumentRange": (
                                                            "V",
                                                            "ns=1;i=10431",
                                                            {},
                                                        ),
                                                        "KindOfQuantity": (
                                                            "V",
                                                            "ns=1;i=10432",
                                                            {},
                                                        ),
                                                        "ValuePrecision": (
                                                            "V",
                                                            "ns=1;i=10433",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                            },
                                        ),
                                        "RelativeHumidity": (
                                            "V",
                                            "ns=1;i=8472",
                                            {
                                                "Definition": ("V", "ns=1;i=9849", {}),
                                                "EURange": ("V", "ns=1;i=9850", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9851",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9852",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9853",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9854",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "ResetStatistics": ("M", "ns=1;i=8473", {}),
                                        "StartTime": ("V", "ns=1;i=8474", {}),
                                        "Temperature": (
                                            "V",
                                            "ns=1;i=8475",
                                            {
                                                "Definition": ("V", "ns=1;i=9855", {}),
                                                "EURange": ("V", "ns=1;i=9856", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9857",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9858",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9859",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9860",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Volume": (
                                            "V",
                                            "ns=1;i=8476",
                                            {
                                                "Definition": ("V", "ns=1;i=9861", {}),
                                                "EURange": ("V", "ns=1;i=9862", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9863",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9864",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9865",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9866",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "VolumeFlowRate": (
                                            "V",
                                            "ns=1;i=8478",
                                            {
                                                "Definition": ("V", "ns=1;i=9867", {}),
                                                "EURange": ("V", "ns=1;i=9868", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9869",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9870",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10067",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10068",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "FluidType": (
                                    "V",
                                    "ns=1;i=7771",
                                    {"Definition": ("V", "ns=1;i=8481", {})},
                                ),
                                "Inlet": (
                                    "O",
                                    "ns=1;i=5156",
                                    {
                                        "AbsolutePressure": (
                                            "V",
                                            "ns=1;i=8482",
                                            {
                                                "Definition": ("V", "ns=1;i=10069", {}),
                                                "EURange": ("V", "ns=1;i=10073", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10074",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10077",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10078",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10079",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "AccumulatedVolume": (
                                            "V",
                                            "ns=1;i=8483",
                                            {
                                                "Definition": ("V", "ns=1;i=10080", {}),
                                                "EURange": ("V", "ns=1;i=10081", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10082",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10083",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10084",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10086",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DewPoint": (
                                            "V",
                                            "ns=1;i=8484",
                                            {
                                                "Definition": ("V", "ns=1;i=10087", {}),
                                                "EURange": ("V", "ns=1;i=10088", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10089",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10090",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10091",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10094",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "GaugePressure": (
                                            "V",
                                            "ns=1;i=8485",
                                            {
                                                "Definition": ("V", "ns=1;i=10095", {}),
                                                "EURange": ("V", "ns=1;i=10097", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10098",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10099",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10100",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10101",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "MassFlowRate": (
                                            "V",
                                            "ns=1;i=8486",
                                            {
                                                "Definition": ("V", "ns=1;i=10102", {}),
                                                "EURange": ("V", "ns=1;i=10103", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10104",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10105",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10106",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10107",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "OilConcentration": (
                                            "V",
                                            "ns=1;i=8487",
                                            {
                                                "Definition": ("V", "ns=1;i=10108", {}),
                                                "EURange": ("V", "ns=1;i=10109", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10110",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10111",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10112",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10114",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "ParticlesPerSizeRange": (
                                            "O",
                                            "ns=1;i=5171",
                                            {
                                                "Fine": (
                                                    "V",
                                                    "ns=1;i=8488",
                                                    {
                                                        "Definition": (
                                                            "V",
                                                            "ns=1;i=10434",
                                                            {},
                                                        ),
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=10435",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=10436",
                                                            {},
                                                        ),
                                                        "InstrumentRange": (
                                                            "V",
                                                            "ns=1;i=10437",
                                                            {},
                                                        ),
                                                        "KindOfQuantity": (
                                                            "V",
                                                            "ns=1;i=10438",
                                                            {},
                                                        ),
                                                        "ValuePrecision": (
                                                            "V",
                                                            "ns=1;i=10439",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "Large": (
                                                    "V",
                                                    "ns=1;i=8489",
                                                    {
                                                        "Definition": (
                                                            "V",
                                                            "ns=1;i=10440",
                                                            {},
                                                        ),
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=10441",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=10442",
                                                            {},
                                                        ),
                                                        "InstrumentRange": (
                                                            "V",
                                                            "ns=1;i=10443",
                                                            {},
                                                        ),
                                                        "KindOfQuantity": (
                                                            "V",
                                                            "ns=1;i=10444",
                                                            {},
                                                        ),
                                                        "ValuePrecision": (
                                                            "V",
                                                            "ns=1;i=10445",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "Medium": (
                                                    "V",
                                                    "ns=1;i=8490",
                                                    {
                                                        "Definition": (
                                                            "V",
                                                            "ns=1;i=10446",
                                                            {},
                                                        ),
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=10447",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=10448",
                                                            {},
                                                        ),
                                                        "InstrumentRange": (
                                                            "V",
                                                            "ns=1;i=10449",
                                                            {},
                                                        ),
                                                        "KindOfQuantity": (
                                                            "V",
                                                            "ns=1;i=10450",
                                                            {},
                                                        ),
                                                        "ValuePrecision": (
                                                            "V",
                                                            "ns=1;i=10451",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                            },
                                        ),
                                        "RelativeHumidity": (
                                            "V",
                                            "ns=1;i=8491",
                                            {
                                                "Definition": ("V", "ns=1;i=10119", {}),
                                                "EURange": ("V", "ns=1;i=10120", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10121",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10122",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10214",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10215",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "ResetStatistics": ("M", "ns=1;i=8619", {}),
                                        "StartTime": ("V", "ns=1;i=8620", {}),
                                        "Temperature": (
                                            "V",
                                            "ns=1;i=8621",
                                            {
                                                "Definition": ("V", "ns=1;i=10216", {}),
                                                "EURange": ("V", "ns=1;i=10217", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10218",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10219",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10220",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10221",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Volume": (
                                            "V",
                                            "ns=1;i=8622",
                                            {
                                                "Definition": ("V", "ns=1;i=10222", {}),
                                                "EURange": ("V", "ns=1;i=10223", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10225",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10227",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10261",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10262",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "VolumeFlowRate": (
                                            "V",
                                            "ns=1;i=8623",
                                            {
                                                "Definition": ("V", "ns=1;i=10275", {}),
                                                "EURange": ("V", "ns=1;i=10276", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10277",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10278",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10279",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10281",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "Outlet": (
                                    "O",
                                    "ns=1;i=5157",
                                    {
                                        "AbsolutePressure": (
                                            "V",
                                            "ns=1;i=8635",
                                            {
                                                "Definition": ("V", "ns=1;i=10287", {}),
                                                "EURange": ("V", "ns=1;i=10289", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10290",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10291",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10292",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10293",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "AccumulatedVolume": (
                                            "V",
                                            "ns=1;i=8638",
                                            {
                                                "Definition": ("V", "ns=1;i=10294", {}),
                                                "EURange": ("V", "ns=1;i=10296", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10315",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10316",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10317",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10318",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "DewPoint": (
                                            "V",
                                            "ns=1;i=8640",
                                            {
                                                "Definition": ("V", "ns=1;i=10319", {}),
                                                "EURange": ("V", "ns=1;i=10320", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10321",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10322",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10330",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10331",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "GaugePressure": (
                                            "V",
                                            "ns=1;i=8642",
                                            {
                                                "Definition": ("V", "ns=1;i=10332", {}),
                                                "EURange": ("V", "ns=1;i=10333", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10334",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10335",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10354",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10355",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "MassFlowRate": (
                                            "V",
                                            "ns=1;i=8643",
                                            {
                                                "Definition": ("V", "ns=1;i=10356", {}),
                                                "EURange": ("V", "ns=1;i=10357", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10358",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10359",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10384",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10385",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "OilConcentration": (
                                            "V",
                                            "ns=1;i=8644",
                                            {
                                                "Definition": ("V", "ns=1;i=10386", {}),
                                                "EURange": ("V", "ns=1;i=10387", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10388",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10389",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10390",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10391",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "ParticlesPerSizeRange": (
                                            "O",
                                            "ns=1;i=5183",
                                            {
                                                "Fine": (
                                                    "V",
                                                    "ns=1;i=8645",
                                                    {
                                                        "Definition": (
                                                            "V",
                                                            "ns=1;i=10452",
                                                            {},
                                                        ),
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=10453",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=10454",
                                                            {},
                                                        ),
                                                        "InstrumentRange": (
                                                            "V",
                                                            "ns=1;i=10455",
                                                            {},
                                                        ),
                                                        "KindOfQuantity": (
                                                            "V",
                                                            "ns=1;i=10456",
                                                            {},
                                                        ),
                                                        "ValuePrecision": (
                                                            "V",
                                                            "ns=1;i=10457",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "Large": (
                                                    "V",
                                                    "ns=1;i=8646",
                                                    {
                                                        "Definition": (
                                                            "V",
                                                            "ns=1;i=10458",
                                                            {},
                                                        ),
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=10459",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=10460",
                                                            {},
                                                        ),
                                                        "InstrumentRange": (
                                                            "V",
                                                            "ns=1;i=10461",
                                                            {},
                                                        ),
                                                        "KindOfQuantity": (
                                                            "V",
                                                            "ns=1;i=10462",
                                                            {},
                                                        ),
                                                        "ValuePrecision": (
                                                            "V",
                                                            "ns=1;i=10463",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "Medium": (
                                                    "V",
                                                    "ns=1;i=8647",
                                                    {
                                                        "Definition": (
                                                            "V",
                                                            "ns=1;i=10464",
                                                            {},
                                                        ),
                                                        "EURange": (
                                                            "V",
                                                            "ns=1;i=10465",
                                                            {},
                                                        ),
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "ns=1;i=10466",
                                                            {},
                                                        ),
                                                        "InstrumentRange": (
                                                            "V",
                                                            "ns=1;i=10467",
                                                            {},
                                                        ),
                                                        "KindOfQuantity": (
                                                            "V",
                                                            "ns=1;i=10468",
                                                            {},
                                                        ),
                                                        "ValuePrecision": (
                                                            "V",
                                                            "ns=1;i=10469",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                            },
                                        ),
                                        "RelativeHumidity": (
                                            "V",
                                            "ns=1;i=8648",
                                            {
                                                "Definition": ("V", "ns=1;i=10392", {}),
                                                "EURange": ("V", "ns=1;i=10393", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10394",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10395",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10396",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10397",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "ResetStatistics": ("M", "ns=1;i=8649", {}),
                                        "StartTime": ("V", "ns=1;i=8650", {}),
                                        "Temperature": (
                                            "V",
                                            "ns=1;i=8651",
                                            {
                                                "Definition": ("V", "ns=1;i=10398", {}),
                                                "EURange": ("V", "ns=1;i=10399", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10400",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10401",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10402",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10403",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Volume": (
                                            "V",
                                            "ns=1;i=8652",
                                            {
                                                "Definition": ("V", "ns=1;i=10404", {}),
                                                "EURange": ("V", "ns=1;i=10405", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10406",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10407",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10408",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10409",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "VolumeFlowRate": (
                                            "V",
                                            "ns=1;i=8653",
                                            {
                                                "Definition": ("V", "ns=1;i=10410", {}),
                                                "EURange": ("V", "ns=1;i=10411", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10412",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10413",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10414",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10415",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                            },
                        ),
                    },
                ),
                "DefaultInstanceBrowseName": ("V", "ns=1;i=10213", {}),
            },
        ),
        "AnalysesType": (
            "OT",
            "ns=1;i=1049",
            {
                "<Analysis>": (
                    "O",
                    "ns=1;i=5093",
                    {
                        "OutputFile": (
                            "O",
                            "ns=1;i=5094",
                            {
                                "Close": (
                                    "M",
                                    "ns=1;i=7920",
                                    {"InputArguments": ("V", "ns=1;i=6250", {})},
                                ),
                                "GetPosition": (
                                    "M",
                                    "ns=1;i=7922",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6251", {}),
                                        "OutputArguments": ("V", "ns=1;i=6360", {}),
                                    },
                                ),
                                "MimeType": ("V", "ns=1;i=11368", {}),
                                "Open": (
                                    "M",
                                    "ns=1;i=7923",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6361", {}),
                                        "OutputArguments": ("V", "ns=1;i=7924", {}),
                                    },
                                ),
                                "OpenCount": ("V", "ns=1;i=7925", {}),
                                "Read": (
                                    "M",
                                    "ns=1;i=7926",
                                    {
                                        "InputArguments": ("V", "ns=1;i=7927", {}),
                                        "OutputArguments": ("V", "ns=1;i=7928", {}),
                                    },
                                ),
                                "SetPosition": (
                                    "M",
                                    "ns=1;i=7929",
                                    {"InputArguments": ("V", "ns=1;i=7930", {})},
                                ),
                                "Size": ("V", "ns=1;i=7931", {}),
                                "UserWritable": ("V", "ns=1;i=7932", {}),
                                "Writable": ("V", "ns=1;i=7933", {}),
                                "Write": (
                                    "M",
                                    "ns=1;i=7934",
                                    {"InputArguments": ("V", "ns=1;i=7935", {})},
                                ),
                            },
                        ),
                        "Trigger": ("M", "ns=1;i=7936", {}),
                    },
                ),
                "<PrefabAnalysis>": (
                    "O",
                    "ns=1;i=5027",
                    {
                        "Close": (
                            "M",
                            "ns=1;i=11346",
                            {"InputArguments": ("V", "ns=1;i=11347", {})},
                        ),
                        "GetPosition": (
                            "M",
                            "ns=1;i=11348",
                            {
                                "InputArguments": ("V", "ns=1;i=11349", {}),
                                "OutputArguments": ("V", "ns=1;i=11350", {}),
                            },
                        ),
                        "MimeType": ("V", "ns=1;i=11365", {}),
                        "Open": (
                            "M",
                            "ns=1;i=11351",
                            {
                                "InputArguments": ("V", "ns=1;i=11352", {}),
                                "OutputArguments": ("V", "ns=1;i=11353", {}),
                            },
                        ),
                        "OpenCount": ("V", "ns=1;i=11354", {}),
                        "Read": (
                            "M",
                            "ns=1;i=11355",
                            {
                                "InputArguments": ("V", "ns=1;i=11356", {}),
                                "OutputArguments": ("V", "ns=1;i=11357", {}),
                            },
                        ),
                        "SetPosition": (
                            "M",
                            "ns=1;i=11358",
                            {"InputArguments": ("V", "ns=1;i=11359", {})},
                        ),
                        "Size": ("V", "ns=1;i=11360", {}),
                        "UserWritable": ("V", "ns=1;i=11361", {}),
                        "Writable": ("V", "ns=1;i=11362", {}),
                        "Write": (
                            "M",
                            "ns=1;i=11363",
                            {"InputArguments": ("V", "ns=1;i=11364", {})},
                        ),
                    },
                ),
                "EnergyReportISO50001": (
                    "O",
                    "ns=1;i=5092",
                    {
                        "OutputFile": (
                            "O",
                            "ns=1;i=5096",
                            {
                                "Close": (
                                    "M",
                                    "ns=1;i=7940",
                                    {"InputArguments": ("V", "ns=1;i=7941", {})},
                                ),
                                "GetPosition": (
                                    "M",
                                    "ns=1;i=7942",
                                    {
                                        "InputArguments": ("V", "ns=1;i=8233", {}),
                                        "OutputArguments": ("V", "ns=1;i=8234", {}),
                                    },
                                ),
                                "MimeType": ("V", "ns=1;i=11367", {}),
                                "Open": (
                                    "M",
                                    "ns=1;i=8235",
                                    {
                                        "InputArguments": ("V", "ns=1;i=8237", {}),
                                        "OutputArguments": ("V", "ns=1;i=9756", {}),
                                    },
                                ),
                                "OpenCount": ("V", "ns=1;i=9757", {}),
                                "Read": (
                                    "M",
                                    "ns=1;i=9758",
                                    {
                                        "InputArguments": ("V", "ns=1;i=9759", {}),
                                        "OutputArguments": ("V", "ns=1;i=9760", {}),
                                    },
                                ),
                                "SetPosition": (
                                    "M",
                                    "ns=1;i=9761",
                                    {"InputArguments": ("V", "ns=1;i=9762", {})},
                                ),
                                "Size": ("V", "ns=1;i=9763", {}),
                                "UserWritable": ("V", "ns=1;i=9764", {}),
                                "Writable": ("V", "ns=1;i=9765", {}),
                                "Write": (
                                    "M",
                                    "ns=1;i=9766",
                                    {"InputArguments": ("V", "ns=1;i=9767", {})},
                                ),
                            },
                        ),
                        "Trigger": ("M", "ns=1;i=7938", {}),
                    },
                ),
            },
        ),
        "AnalysisType": (
            "OT",
            "ns=1;i=1004",
            {
                "OutputFile": (
                    "O",
                    "ns=1;i=5059",
                    {
                        "Close": (
                            "M",
                            "ns=1;i=7900",
                            {"InputArguments": ("V", "ns=1;i=7901", {})},
                        ),
                        "GetPosition": (
                            "M",
                            "ns=1;i=7902",
                            {
                                "InputArguments": ("V", "ns=1;i=7903", {}),
                                "OutputArguments": ("V", "ns=1;i=7904", {}),
                            },
                        ),
                        "MimeType": ("V", "ns=1;i=11366", {}),
                        "Open": (
                            "M",
                            "ns=1;i=7905",
                            {
                                "InputArguments": ("V", "ns=1;i=7906", {}),
                                "OutputArguments": ("V", "ns=1;i=7907", {}),
                            },
                        ),
                        "OpenCount": ("V", "ns=1;i=7908", {}),
                        "Read": (
                            "M",
                            "ns=1;i=7909",
                            {
                                "InputArguments": ("V", "ns=1;i=7910", {}),
                                "OutputArguments": ("V", "ns=1;i=7911", {}),
                            },
                        ),
                        "SetPosition": (
                            "M",
                            "ns=1;i=7912",
                            {"InputArguments": ("V", "ns=1;i=7913", {})},
                        ),
                        "Size": ("V", "ns=1;i=7914", {}),
                        "UserWritable": ("V", "ns=1;i=7915", {}),
                        "Writable": ("V", "ns=1;i=7916", {}),
                        "Write": (
                            "M",
                            "ns=1;i=7917",
                            {"InputArguments": ("V", "ns=1;i=7918", {})},
                        ),
                    },
                ),
                "Trigger": ("M", "ns=1;i=7919", {}),
            },
        ),
        "CASComponentType": (
            "OT",
            "ns=1;i=1021",
            {
                "ActiveAirnet": ("V", "ns=1;i=12533", {}),
                "Ambient": (
                    "O",
                    "ns=1;i=5140",
                    {
                        "AbsolutePressure": (
                            "V",
                            "ns=1;i=8240",
                            {
                                "Definition": ("V", "ns=1;i=9170", {}),
                                "EURange": ("V", "ns=1;i=9172", {}),
                                "EngineeringUnits": ("V", "ns=1;i=9171", {}),
                                "InstrumentRange": ("V", "ns=1;i=9173", {}),
                                "KindOfQuantity": ("V", "ns=1;i=7674", {}),
                                "ValuePrecision": ("V", "ns=1;i=9307", {}),
                            },
                        ),
                        "DewPoint": (
                            "V",
                            "ns=1;i=7680",
                            {
                                "Definition": ("V", "ns=1;i=7735", {}),
                                "EURange": ("V", "ns=1;i=7736", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7737", {}),
                                "InstrumentRange": ("V", "ns=1;i=7738", {}),
                                "KindOfQuantity": ("V", "ns=1;i=7772", {}),
                                "ValuePrecision": ("V", "ns=1;i=7773", {}),
                            },
                        ),
                        "RelativeHumidity": (
                            "V",
                            "ns=1;i=7682",
                            {
                                "Definition": ("V", "ns=1;i=7774", {}),
                                "EURange": ("V", "ns=1;i=7775", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7787", {}),
                                "InstrumentRange": ("V", "ns=1;i=7788", {}),
                                "KindOfQuantity": ("V", "ns=1;i=7792", {}),
                                "ValuePrecision": ("V", "ns=1;i=7794", {}),
                            },
                        ),
                        "Temperature": (
                            "V",
                            "ns=1;i=7734",
                            {
                                "Definition": ("V", "ns=1;i=7887", {}),
                                "EURange": ("V", "ns=1;i=7888", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7889", {}),
                                "InstrumentRange": ("V", "ns=1;i=7964", {}),
                                "KindOfQuantity": ("V", "ns=1;i=7965", {}),
                                "ValuePrecision": ("V", "ns=1;i=7966", {}),
                            },
                        ),
                    },
                ),
                "ChargingSystemType": ("OT", "ns=1;i=1005", {}),
                "CompressorType": (
                    "OT",
                    "ns=1;i=1039",
                    {
                        "Design": (
                            "O",
                            "ns=1;i=5058",
                            {
                                "ComponentClass": (
                                    "V",
                                    "ns=1;i=6052",
                                    {"Definition": ("V", "ns=1;i=6335", {})},
                                ),
                                "DisplacementType": (
                                    "V",
                                    "ns=1;i=6340",
                                    {"Definition": ("V", "ns=1;i=6372", {})},
                                ),
                                "LubricationType": (
                                    "V",
                                    "ns=1;i=6341",
                                    {"Definition": ("V", "ns=1;i=6373", {})},
                                ),
                                "NumberOfStages": (
                                    "V",
                                    "ns=1;i=6362",
                                    {"Definition": ("V", "ns=1;i=6374", {})},
                                ),
                                "VariableFlow": (
                                    "V",
                                    "ns=1;i=6363",
                                    {
                                        "Definition": ("V", "ns=1;i=6375", {}),
                                        "FalseState": ("V", "ns=1;i=6364", {}),
                                        "TrueState": ("V", "ns=1;i=6371", {}),
                                    },
                                ),
                            },
                        ),
                        "Identification": (
                            "O",
                            "ns=1;i=5189",
                            {
                                "DeviceClass": ("V", "ns=1;i=9824", {}),
                                "Manufacturer": ("V", "ns=1;i=7937", {}),
                                "ProductInstanceUri": ("V", "ns=1;i=7921", {}),
                                "SerialNumber": ("V", "ns=1;i=7939", {}),
                            },
                        ),
                        "Operational": (
                            "O",
                            "ns=1;i=5070",
                            {
                                "ActivePressureBand": (
                                    "V",
                                    "ns=1;i=6061",
                                    {"Definition": ("V", "ns=1;i=6218", {})},
                                ),
                                "FlowRateRatio": (
                                    "V",
                                    "ns=1;i=6062",
                                    {
                                        "Definition": ("V", "ns=1;i=6219", {}),
                                        "EURange": ("V", "ns=1;i=6220", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6221", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10273", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10274", {}),
                                    },
                                ),
                                "IsentropicEfficiency": (
                                    "V",
                                    "ns=1;i=10113",
                                    {
                                        "Definition": ("V", "ns=1;i=10115", {}),
                                        "EURange": ("V", "ns=1;i=10116", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10117", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10265", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10266", {}),
                                    },
                                ),
                                "OperatingState": (
                                    "V",
                                    "ns=1;i=6067",
                                    {
                                        "Definition": ("V", "ns=1;i=6068", {}),
                                        "ValuePrecision": ("V", "ns=1;i=6217", {}),
                                    },
                                ),
                                "SpecificEnergyRequirement": (
                                    "V",
                                    "ns=1;i=6098",
                                    {
                                        "Definition": ("V", "ns=1;i=6137", {}),
                                        "EURange": ("V", "ns=1;i=6224", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6225", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10269", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10270", {}),
                                    },
                                ),
                            },
                        ),
                        "Statistics": (
                            "O",
                            "ns=1;i=5072",
                            {
                                "LoadedTime": (
                                    "V",
                                    "ns=1;i=6565",
                                    {
                                        "Definition": ("V", "ns=1;i=6651", {}),
                                        "EURange": ("V", "ns=1;i=6697", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6698", {}),
                                        "InstrumentRange": ("V", "ns=1;i=6699", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7183", {}),
                                    },
                                ),
                                "UnloadedTime": (
                                    "V",
                                    "ns=1;i=6567",
                                    {
                                        "Definition": ("V", "ns=1;i=7184", {}),
                                        "EURange": ("V", "ns=1;i=7185", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7662", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7663", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7664", {}),
                                    },
                                ),
                            },
                        ),
                    },
                ),
                "Configuration": (
                    "O",
                    "ns=1;i=5038",
                    {"UIElement": ("V", "ns=1;i=6564", {})},
                ),
                "ConverterType": (
                    "OT",
                    "ns=1;i=1029",
                    {
                        "Design": (
                            "O",
                            "ns=1;i=5054",
                            {
                                "ComponentClass": (
                                    "V",
                                    "ns=1;i=6085",
                                    {"Definition": ("V", "ns=1;i=8063", {})},
                                )
                            },
                        ),
                        "Operational": (
                            "O",
                            "ns=1;i=5159",
                            {
                                "CatalyticMaterialTemperature": (
                                    "V",
                                    "ns=1;i=6454",
                                    {
                                        "Definition": ("V", "ns=1;i=6458", {}),
                                        "EURange": ("V", "ns=1;i=6459", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8015", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10309", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10310", {}),
                                    },
                                )
                            },
                        ),
                    },
                ),
                "CoolantCircuit": (
                    "O",
                    "ns=1;i=5138",
                    {
                        "Delta": (
                            "O",
                            "ns=1;i=5116",
                            {
                                "AbsolutePressure": (
                                    "V",
                                    "ns=1;i=7864",
                                    {
                                        "Definition": ("V", "ns=1;i=7957", {}),
                                        "EURange": ("V", "ns=1;i=7959", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7958", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7961", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7962", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7963", {}),
                                    },
                                ),
                                "AccumulatedVolume": (
                                    "V",
                                    "ns=1;i=7172",
                                    {
                                        "Definition": ("V", "ns=1;i=7692", {}),
                                        "EURange": ("V", "ns=1;i=7694", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7693", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7695", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7696", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7697", {}),
                                    },
                                ),
                                "DewPoint": (
                                    "V",
                                    "ns=1;i=7173",
                                    {
                                        "Definition": ("V", "ns=1;i=7745", {}),
                                        "EURange": ("V", "ns=1;i=7747", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7746", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7748", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7749", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7750", {}),
                                    },
                                ),
                                "GaugePressure": (
                                    "V",
                                    "ns=1;i=7174",
                                    {
                                        "Definition": ("V", "ns=1;i=7751", {}),
                                        "EURange": ("V", "ns=1;i=7753", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7752", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7754", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7761", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7762", {}),
                                    },
                                ),
                                "MassFlowRate": (
                                    "V",
                                    "ns=1;i=7175",
                                    {
                                        "Definition": ("V", "ns=1;i=7763", {}),
                                        "EURange": ("V", "ns=1;i=7765", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7764", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7766", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7767", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7768", {}),
                                    },
                                ),
                                "OilConcentration": (
                                    "V",
                                    "ns=1;i=7176",
                                    {
                                        "Definition": ("V", "ns=1;i=7770", {}),
                                        "EURange": ("V", "ns=1;i=7777", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7776", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7778", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7779", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7780", {}),
                                    },
                                ),
                                "ParticlesPerSizeRange": (
                                    "O",
                                    "ns=1;i=5129",
                                    {
                                        "Fine": (
                                            "V",
                                            "ns=1;i=6463",
                                            {
                                                "Definition": ("V", "ns=1;i=7704", {}),
                                                "EURange": ("V", "ns=1;i=7706", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=7705",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=7707",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8711",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=7708",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Large": (
                                            "V",
                                            "ns=1;i=6464",
                                            {
                                                "Definition": ("V", "ns=1;i=8942", {}),
                                                "EURange": ("V", "ns=1;i=8958", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=8943",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=8959",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8960",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=8961",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Medium": (
                                            "V",
                                            "ns=1;i=6506",
                                            {
                                                "Definition": ("V", "ns=1;i=10070", {}),
                                                "EURange": ("V", "ns=1;i=10072", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10071",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10236",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10237",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10238",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "RelativeHumidity": (
                                    "V",
                                    "ns=1;i=7177",
                                    {
                                        "Definition": ("V", "ns=1;i=7781", {}),
                                        "EURange": ("V", "ns=1;i=7783", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7782", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7784", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7785", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7786", {}),
                                    },
                                ),
                                "ResetStatistics": ("M", "ns=1;i=7178", {}),
                                "StartTime": ("V", "ns=1;i=7179", {}),
                                "Temperature": (
                                    "V",
                                    "ns=1;i=7187",
                                    {
                                        "Definition": ("V", "ns=1;i=7789", {}),
                                        "EURange": ("V", "ns=1;i=7795", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7790", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7796", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7797", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7798", {}),
                                    },
                                ),
                                "Volume": (
                                    "V",
                                    "ns=1;i=7188",
                                    {
                                        "Definition": ("V", "ns=1;i=7799", {}),
                                        "EURange": ("V", "ns=1;i=7801", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7800", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7802", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7803", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7804", {}),
                                    },
                                ),
                                "VolumeFlowRate": (
                                    "V",
                                    "ns=1;i=7189",
                                    {
                                        "Definition": ("V", "ns=1;i=7805", {}),
                                        "EURange": ("V", "ns=1;i=7807", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7806", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7808", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7809", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7810", {}),
                                    },
                                ),
                            },
                        ),
                        "FluidType": (
                            "V",
                            "ns=1;i=8297",
                            {"Definition": ("V", "ns=1;i=8477", {})},
                        ),
                        "Inlet": (
                            "O",
                            "ns=1;i=5123",
                            {
                                "AbsolutePressure": (
                                    "V",
                                    "ns=1;i=8850",
                                    {
                                        "Definition": ("V", "ns=1;i=9220", {}),
                                        "EURange": ("V", "ns=1;i=9222", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9221", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9223", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9224", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9225", {}),
                                    },
                                ),
                                "AccumulatedVolume": (
                                    "V",
                                    "ns=1;i=8851",
                                    {
                                        "Definition": ("V", "ns=1;i=9226", {}),
                                        "EURange": ("V", "ns=1;i=9228", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9227", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9229", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9230", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9231", {}),
                                    },
                                ),
                                "DewPoint": (
                                    "V",
                                    "ns=1;i=8934",
                                    {
                                        "Definition": ("V", "ns=1;i=9232", {}),
                                        "EURange": ("V", "ns=1;i=9234", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9233", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9235", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9236", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9237", {}),
                                    },
                                ),
                                "GaugePressure": (
                                    "V",
                                    "ns=1;i=8935",
                                    {
                                        "Definition": ("V", "ns=1;i=9238", {}),
                                        "EURange": ("V", "ns=1;i=9240", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9239", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9247", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9248", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9249", {}),
                                    },
                                ),
                                "MassFlowRate": (
                                    "V",
                                    "ns=1;i=8936",
                                    {
                                        "Definition": ("V", "ns=1;i=9250", {}),
                                        "EURange": ("V", "ns=1;i=9252", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9251", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9253", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9254", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9255", {}),
                                    },
                                ),
                                "OilConcentration": (
                                    "V",
                                    "ns=1;i=8937",
                                    {
                                        "Definition": ("V", "ns=1;i=9256", {}),
                                        "EURange": ("V", "ns=1;i=9258", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9257", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9259", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9260", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9261", {}),
                                    },
                                ),
                                "ParticlesPerSizeRange": (
                                    "O",
                                    "ns=1;i=5186",
                                    {
                                        "Fine": (
                                            "V",
                                            "ns=1;i=7260",
                                            {
                                                "Definition": ("V", "ns=1;i=7990", {}),
                                                "EURange": ("V", "ns=1;i=7992", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=7991",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=7993",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8813",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=7994",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Large": (
                                            "V",
                                            "ns=1;i=7261",
                                            {
                                                "Definition": ("V", "ns=1;i=9096", {}),
                                                "EURange": ("V", "ns=1;i=9098", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9097",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9099",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9100",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9105",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Medium": (
                                            "V",
                                            "ns=1;i=7262",
                                            {
                                                "Definition": ("V", "ns=1;i=10360", {}),
                                                "EURange": ("V", "ns=1;i=10362", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10361",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10363",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10364",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10365",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "RelativeHumidity": (
                                    "V",
                                    "ns=1;i=8944",
                                    {
                                        "Definition": ("V", "ns=1;i=9282", {}),
                                        "EURange": ("V", "ns=1;i=9284", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9283", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9285", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9286", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9287", {}),
                                    },
                                ),
                                "ResetStatistics": ("M", "ns=1;i=8945", {}),
                                "StartTime": ("V", "ns=1;i=8946", {}),
                                "Temperature": (
                                    "V",
                                    "ns=1;i=8947",
                                    {
                                        "Definition": ("V", "ns=1;i=9288", {}),
                                        "EURange": ("V", "ns=1;i=9290", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9289", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9291", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9292", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9293", {}),
                                    },
                                ),
                                "Volume": (
                                    "V",
                                    "ns=1;i=8948",
                                    {
                                        "Definition": ("V", "ns=1;i=9294", {}),
                                        "EURange": ("V", "ns=1;i=9296", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9295", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9297", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9298", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9299", {}),
                                    },
                                ),
                                "VolumeFlowRate": (
                                    "V",
                                    "ns=1;i=8949",
                                    {
                                        "Definition": ("V", "ns=1;i=9300", {}),
                                        "EURange": ("V", "ns=1;i=9302", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9301", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9303", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9304", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9306", {}),
                                    },
                                ),
                            },
                        ),
                        "Outlet": (
                            "O",
                            "ns=1;i=5124",
                            {
                                "AbsolutePressure": (
                                    "V",
                                    "ns=1;i=9349",
                                    {
                                        "Definition": ("V", "ns=1;i=9559", {}),
                                        "EURange": ("V", "ns=1;i=9561", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9560", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9562", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9563", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9564", {}),
                                    },
                                ),
                                "AccumulatedVolume": (
                                    "V",
                                    "ns=1;i=9350",
                                    {
                                        "Definition": ("V", "ns=1;i=9565", {}),
                                        "EURange": ("V", "ns=1;i=9567", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9566", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9568", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9569", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9570", {}),
                                    },
                                ),
                                "DewPoint": (
                                    "V",
                                    "ns=1;i=9351",
                                    {
                                        "Definition": ("V", "ns=1;i=9571", {}),
                                        "EURange": ("V", "ns=1;i=9573", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9572", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9574", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9575", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9576", {}),
                                    },
                                ),
                                "GaugePressure": (
                                    "V",
                                    "ns=1;i=9352",
                                    {
                                        "Definition": ("V", "ns=1;i=9577", {}),
                                        "EURange": ("V", "ns=1;i=9579", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9578", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9580", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9581", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9582", {}),
                                    },
                                ),
                                "MassFlowRate": (
                                    "V",
                                    "ns=1;i=9353",
                                    {
                                        "Definition": ("V", "ns=1;i=9583", {}),
                                        "EURange": ("V", "ns=1;i=9688", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9687", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9719", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9729", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9730", {}),
                                    },
                                ),
                                "OilConcentration": (
                                    "V",
                                    "ns=1;i=9354",
                                    {
                                        "Definition": ("V", "ns=1;i=9731", {}),
                                        "EURange": ("V", "ns=1;i=9733", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9732", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9739", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9740", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9741", {}),
                                    },
                                ),
                                "ParticlesPerSizeRange": (
                                    "O",
                                    "ns=1;i=5154",
                                    {
                                        "Fine": (
                                            "V",
                                            "ns=1;i=6549",
                                            {
                                                "Definition": ("V", "ns=1;i=7729", {}),
                                                "EURange": ("V", "ns=1;i=7731", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=7730",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=7732",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8791",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=7733",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Large": (
                                            "V",
                                            "ns=1;i=6560",
                                            {
                                                "Definition": ("V", "ns=1;i=9020", {}),
                                                "EURange": ("V", "ns=1;i=9022", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9021",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9023",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9024",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9025",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Medium": (
                                            "V",
                                            "ns=1;i=6563",
                                            {
                                                "Definition": ("V", "ns=1;i=10324", {}),
                                                "EURange": ("V", "ns=1;i=10326", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10325",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10327",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10328",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10329",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "RelativeHumidity": (
                                    "V",
                                    "ns=1;i=9355",
                                    {
                                        "Definition": ("V", "ns=1;i=9742", {}),
                                        "EURange": ("V", "ns=1;i=9749", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9743", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9750", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9751", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9752", {}),
                                    },
                                ),
                                "ResetStatistics": ("M", "ns=1;i=9356", {}),
                                "StartTime": ("V", "ns=1;i=9357", {}),
                                "Temperature": (
                                    "V",
                                    "ns=1;i=9358",
                                    {
                                        "Definition": ("V", "ns=1;i=9753", {}),
                                        "EURange": ("V", "ns=1;i=10130", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10129", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10239", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=10240", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10241", {}),
                                    },
                                ),
                                "Volume": (
                                    "V",
                                    "ns=1;i=9359",
                                    {
                                        "Definition": ("V", "ns=1;i=10242", {}),
                                        "EURange": ("V", "ns=1;i=10244", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10243", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10245", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=10246", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10247", {}),
                                    },
                                ),
                                "VolumeFlowRate": (
                                    "V",
                                    "ns=1;i=9360",
                                    {
                                        "Definition": ("V", "ns=1;i=10248", {}),
                                        "EURange": ("V", "ns=1;i=10250", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10249", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10251", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=10252", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10253", {}),
                                    },
                                ),
                            },
                        ),
                    },
                ),
                "CoolingSystemType": ("OT", "ns=1;i=1001", {}),
                "Design": (
                    "O",
                    "ns=1;i=5010",
                    {
                        "ComponentClass": (
                            "V",
                            "ns=1;i=6022",
                            {"Definition": ("V", "ns=1;i=6269", {})},
                        ),
                        "UIElement": ("V", "ns=1;i=6587", {}),
                    },
                ),
                "DrainType": (
                    "OT",
                    "ns=1;i=1025",
                    {
                        "Design": (
                            "O",
                            "ns=1;i=5039",
                            {
                                "ComponentClass": (
                                    "V",
                                    "ns=1;i=6072",
                                    {"Definition": ("V", "ns=1;i=8062", {})},
                                )
                            },
                        ),
                        "Operational": (
                            "O",
                            "ns=1;i=5158",
                            {"DrainTest": ("M", "ns=1;i=8161", {})},
                        ),
                        "ProcessFluidCircuit": (
                            "O",
                            "ns=1;i=5185",
                            {
                                "FluidType": (
                                    "V",
                                    "ns=1;i=10517",
                                    {"Definition": ("V", "ns=1;i=10518", {})},
                                )
                            },
                        ),
                    },
                ),
                "DryerType": (
                    "OT",
                    "ns=1;i=1030",
                    {
                        "Design": (
                            "O",
                            "ns=1;i=5057",
                            {
                                "ComponentClass": (
                                    "V",
                                    "ns=1;i=6086",
                                    {"Definition": ("V", "ns=1;i=6116", {})},
                                ),
                                "LowestAmbientTemperature": (
                                    "V",
                                    "ns=1;i=6121",
                                    {
                                        "Definition": ("V", "ns=1;i=6135", {}),
                                        "EURange": ("V", "ns=1;i=6138", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6139", {}),
                                    },
                                ),
                            },
                        ),
                        "Operational": (
                            "O",
                            "ns=1;i=5160",
                            {
                                "OnOff": (
                                    "V",
                                    "ns=1;i=10695",
                                    {
                                        "Definition": ("V", "ns=1;i=10709", {}),
                                        "FalseState": ("V", "ns=1;i=10696", {}),
                                        "TrueState": ("V", "ns=1;i=10697", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10710", {}),
                                    },
                                ),
                                "OperatingState": (
                                    "V",
                                    "ns=1;i=10698",
                                    {
                                        "Definition": ("V", "ns=1;i=10711", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10712", {}),
                                    },
                                ),
                                "PressureDewPoint": (
                                    "V",
                                    "ns=1;i=6452",
                                    {
                                        "Definition": ("V", "ns=1;i=6457", {}),
                                        "EURange": ("V", "ns=1;i=6544", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6545", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10313", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10314", {}),
                                    },
                                ),
                            },
                        ),
                    },
                ),
                "ElectricalCircuit": (
                    "O",
                    "ns=1;i=5145",
                    {
                        "Delta": (
                            "O",
                            "ns=1;i=5155",
                            {
                                "ApparentPower": (
                                    "V",
                                    "ns=1;i=7836",
                                    {
                                        "Definition": ("V", "ns=1;i=9274", {}),
                                        "EURange": ("V", "ns=1;i=9336", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9335", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9337", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9338", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9339", {}),
                                    },
                                ),
                                "Current": (
                                    "V",
                                    "ns=1;i=7837",
                                    {
                                        "Definition": ("V", "ns=1;i=9400", {}),
                                        "EURange": ("V", "ns=1;i=9402", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9401", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9403", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9404", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9441", {}),
                                    },
                                ),
                                "Energy": (
                                    "V",
                                    "ns=1;i=7838",
                                    {
                                        "Definition": ("V", "ns=1;i=9442", {}),
                                        "EURange": ("V", "ns=1;i=9492", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9491", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9493", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9494", {}),
                                    },
                                ),
                                "Power": (
                                    "V",
                                    "ns=1;i=7839",
                                    {
                                        "Definition": ("V", "ns=1;i=9495", {}),
                                        "EURange": ("V", "ns=1;i=9585", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9584", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9586", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9587", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9588", {}),
                                    },
                                ),
                                "ResetStatistics": ("M", "ns=1;i=7840", {}),
                                "StartTime": ("V", "ns=1;i=7841", {}),
                                "Voltage": (
                                    "V",
                                    "ns=1;i=7842",
                                    {
                                        "Definition": ("V", "ns=1;i=9589", {}),
                                        "EURange": ("V", "ns=1;i=9591", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9590", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9592", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9593", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9594", {}),
                                    },
                                ),
                            },
                        ),
                        "Input": (
                            "O",
                            "ns=1;i=5178",
                            {
                                "ApparentPower": (
                                    "V",
                                    "ns=1;i=9623",
                                    {
                                        "Definition": ("V", "ns=1;i=9812", {}),
                                        "EURange": ("V", "ns=1;i=9814", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9813", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9815", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9816", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9817", {}),
                                    },
                                ),
                                "Current": (
                                    "V",
                                    "ns=1;i=9624",
                                    {
                                        "Definition": ("V", "ns=1;i=9818", {}),
                                        "EURange": ("V", "ns=1;i=9820", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9819", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9821", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9822", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9951", {}),
                                    },
                                ),
                                "Energy": (
                                    "V",
                                    "ns=1;i=9625",
                                    {
                                        "Definition": ("V", "ns=1;i=9952", {}),
                                        "EURange": ("V", "ns=1;i=9954", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9953", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9955", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9956", {}),
                                    },
                                ),
                                "Power": (
                                    "V",
                                    "ns=1;i=9626",
                                    {
                                        "Definition": ("V", "ns=1;i=9957", {}),
                                        "EURange": ("V", "ns=1;i=9959", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9958", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9960", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9961", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9962", {}),
                                    },
                                ),
                                "ResetStatistics": ("M", "ns=1;i=9627", {}),
                                "StartTime": ("V", "ns=1;i=9628", {}),
                                "Voltage": (
                                    "V",
                                    "ns=1;i=9629",
                                    {
                                        "Definition": ("V", "ns=1;i=9963", {}),
                                        "EURange": ("V", "ns=1;i=9965", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9964", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9966", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9967", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9968", {}),
                                    },
                                ),
                            },
                        ),
                        "Output": (
                            "O",
                            "ns=1;i=5180",
                            {
                                "ApparentPower": (
                                    "V",
                                    "ns=1;i=9997",
                                    {
                                        "Definition": ("V", "ns=1;i=10184", {}),
                                        "EURange": ("V", "ns=1;i=10186", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10185", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10187", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=10188", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10189", {}),
                                    },
                                ),
                                "Current": (
                                    "V",
                                    "ns=1;i=9998",
                                    {
                                        "Definition": ("V", "ns=1;i=10190", {}),
                                        "EURange": ("V", "ns=1;i=10192", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10191", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10193", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=10194", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10195", {}),
                                    },
                                ),
                                "Energy": (
                                    "V",
                                    "ns=1;i=9999",
                                    {
                                        "Definition": ("V", "ns=1;i=10196", {}),
                                        "EURange": ("V", "ns=1;i=10198", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10197", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10199", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10200", {}),
                                    },
                                ),
                                "Power": (
                                    "V",
                                    "ns=1;i=10000",
                                    {
                                        "Definition": ("V", "ns=1;i=10201", {}),
                                        "EURange": ("V", "ns=1;i=10203", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10202", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10204", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=10205", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10206", {}),
                                    },
                                ),
                                "ResetStatistics": ("M", "ns=1;i=10001", {}),
                                "StartTime": ("V", "ns=1;i=10002", {}),
                                "Voltage": (
                                    "V",
                                    "ns=1;i=10003",
                                    {
                                        "Definition": ("V", "ns=1;i=10207", {}),
                                        "EURange": ("V", "ns=1;i=10209", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10208", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10210", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=10211", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10212", {}),
                                    },
                                ),
                            },
                        ),
                    },
                ),
                "Events": (
                    "O",
                    "ns=1;i=5035",
                    {
                        "<Event>": (
                            "O",
                            "ns=1;i=5206",
                            {
                                "AddComment": (
                                    "M",
                                    "ns=1;i=9833",
                                    {"InputArguments": ("V", "ns=1;i=9834", {})},
                                ),
                                "BranchId": ("V", "ns=1;i=10849", {}),
                                "ClientUserId": ("V", "ns=1;i=10850", {}),
                                "Comment": (
                                    "V",
                                    "ns=1;i=10851",
                                    {"SourceTimestamp": ("V", "ns=1;i=10852", {})},
                                ),
                                "ConditionClassId": ("V", "ns=1;i=10853", {}),
                                "ConditionClassName": ("V", "ns=1;i=10854", {}),
                                "ConditionName": ("V", "ns=1;i=10855", {}),
                                "Disable": ("M", "ns=1;i=10856", {}),
                                "Enable": ("M", "ns=1;i=10857", {}),
                                "EnabledState": (
                                    "V",
                                    "ns=1;i=10858",
                                    {"Id": ("V", "ns=1;i=10859", {})},
                                ),
                                "EventId": ("V", "ns=1;i=10860", {}),
                                "EventType": ("V", "ns=1;i=10861", {}),
                                "LastSeverity": (
                                    "V",
                                    "ns=1;i=10862",
                                    {"SourceTimestamp": ("V", "ns=1;i=10863", {})},
                                ),
                                "Message": ("V", "ns=1;i=10864", {}),
                                "Quality": (
                                    "V",
                                    "ns=1;i=10865",
                                    {"SourceTimestamp": ("V", "ns=1;i=10866", {})},
                                ),
                                "ReceiveTime": ("V", "ns=1;i=10867", {}),
                                "Retain": ("V", "ns=1;i=10868", {}),
                                "Severity": ("V", "ns=1;i=10869", {}),
                                "SourceName": ("V", "ns=1;i=10870", {}),
                                "SourceNode": ("V", "ns=1;i=10871", {}),
                                "Time": ("V", "ns=1;i=10872", {}),
                            },
                        ),
                        "EmergencyStop": (
                            "O",
                            "ns=1;i=5068",
                            {
                                "AckedState": (
                                    "V",
                                    "ns=1;i=6057",
                                    {
                                        "FalseState": ("V", "ns=1;i=7566", {}),
                                        "Id": ("V", "ns=1;i=6058", {}),
                                        "TransitionTime": ("V", "ns=1;i=7567", {}),
                                        "TrueState": ("V", "ns=1;i=7568", {}),
                                    },
                                ),
                                "Acknowledge": (
                                    "M",
                                    "ns=1;i=7060",
                                    {"InputArguments": ("V", "ns=1;i=6059", {})},
                                ),
                                "ActiveState": (
                                    "V",
                                    "ns=1;i=6069",
                                    {
                                        "EffectiveDisplayName": (
                                            "V",
                                            "ns=1;i=7569",
                                            {},
                                        ),
                                        "EffectiveTransitionTime": (
                                            "V",
                                            "ns=1;i=7570",
                                            {},
                                        ),
                                        "FalseState": ("V", "ns=1;i=7571", {}),
                                        "Id": ("V", "ns=1;i=6070", {}),
                                        "TransitionTime": ("V", "ns=1;i=7572", {}),
                                        "TrueState": ("V", "ns=1;i=7573", {}),
                                    },
                                ),
                                "AddComment": (
                                    "M",
                                    "ns=1;i=7065",
                                    {"InputArguments": ("V", "ns=1;i=6216", {})},
                                ),
                                "AudibleEnabled": ("V", "ns=1;i=7352", {}),
                                "AudibleSound": ("V", "ns=1;i=7353", {}),
                                "BranchId": ("V", "ns=1;i=6314", {}),
                                "ClientUserId": ("V", "ns=1;i=6315", {}),
                                "Comment": (
                                    "V",
                                    "ns=1;i=6925",
                                    {"SourceTimestamp": ("V", "ns=1;i=6926", {})},
                                ),
                                "ConditionClassId": ("V", "ns=1;i=6927", {}),
                                "ConditionClassName": ("V", "ns=1;i=6928", {}),
                                "ConditionName": ("V", "ns=1;i=6929", {}),
                                "ConditionSubClassId": ("V", "ns=1;i=7354", {}),
                                "ConditionSubClassName": ("V", "ns=1;i=7355", {}),
                                "Confirm": (
                                    "M",
                                    "ns=1;i=7356",
                                    {"InputArguments": ("V", "ns=1;i=7357", {})},
                                ),
                                "ConfirmedState": (
                                    "V",
                                    "ns=1;i=7358",
                                    {
                                        "FalseState": ("V", "ns=1;i=7359", {}),
                                        "Id": ("V", "ns=1;i=7360", {}),
                                        "TransitionTime": ("V", "ns=1;i=7361", {}),
                                        "TrueState": ("V", "ns=1;i=7362", {}),
                                    },
                                ),
                                "Disable": ("M", "ns=1;i=7066", {}),
                                "Enable": ("M", "ns=1;i=7067", {}),
                                "EnabledState": (
                                    "V",
                                    "ns=1;i=6930",
                                    {
                                        "EffectiveDisplayName": (
                                            "V",
                                            "ns=1;i=7574",
                                            {},
                                        ),
                                        "EffectiveTransitionTime": (
                                            "V",
                                            "ns=1;i=7575",
                                            {},
                                        ),
                                        "FalseState": ("V", "ns=1;i=7576", {}),
                                        "Id": ("V", "ns=1;i=6931", {}),
                                        "TransitionTime": ("V", "ns=1;i=7577", {}),
                                        "TrueState": ("V", "ns=1;i=7578", {}),
                                    },
                                ),
                                "EventId": ("V", "ns=1;i=6932", {}),
                                "EventType": ("V", "ns=1;i=6933", {}),
                                "FirstInGroup": ("O", "ns=1;i=5097", {}),
                                "FirstInGroupFlag": ("V", "ns=1;i=7363", {}),
                                "InputNode": ("V", "ns=1;i=6934", {}),
                                "LastSeverity": (
                                    "V",
                                    "ns=1;i=6935",
                                    {"SourceTimestamp": ("V", "ns=1;i=6936", {})},
                                ),
                                "LatchedState": (
                                    "V",
                                    "ns=1;i=7364",
                                    {
                                        "FalseState": ("V", "ns=1;i=7365", {}),
                                        "Id": ("V", "ns=1;i=7366", {}),
                                        "TransitionTime": ("V", "ns=1;i=7367", {}),
                                        "TrueState": ("V", "ns=1;i=7368", {}),
                                    },
                                ),
                                "LocalTime": ("V", "ns=1;i=7369", {}),
                                "MaxTimeShelved": ("V", "ns=1;i=7370", {}),
                                "Message": ("V", "ns=1;i=6937", {}),
                                "NormalState": ("V", "ns=1;i=6938", {}),
                                "OffDelay": ("V", "ns=1;i=7371", {}),
                                "OnDelay": ("V", "ns=1;i=7372", {}),
                                "OutOfServiceState": (
                                    "V",
                                    "ns=1;i=7373",
                                    {
                                        "FalseState": ("V", "ns=1;i=7374", {}),
                                        "Id": ("V", "ns=1;i=7375", {}),
                                        "TransitionTime": ("V", "ns=1;i=7376", {}),
                                        "TrueState": ("V", "ns=1;i=7377", {}),
                                    },
                                ),
                                "PlaceInService": ("M", "ns=1;i=7378", {}),
                                "Quality": (
                                    "V",
                                    "ns=1;i=6939",
                                    {"SourceTimestamp": ("V", "ns=1;i=6940", {})},
                                ),
                                "ReAlarmRepeatCount": ("V", "ns=1;i=7379", {}),
                                "ReAlarmTime": ("V", "ns=1;i=7382", {}),
                                "ReceiveTime": ("V", "ns=1;i=6941", {}),
                                "RemoveFromService": ("M", "ns=1;i=7383", {}),
                                "Reset": ("M", "ns=1;i=7384", {}),
                                "Retain": ("V", "ns=1;i=6942", {}),
                                "Severity": ("V", "ns=1;i=6943", {}),
                                "ShelvingState": (
                                    "O",
                                    "ns=1;i=5098",
                                    {
                                        "CurrentState": (
                                            "V",
                                            "ns=1;i=7385",
                                            {"Id": ("V", "ns=1;i=7386", {})},
                                        ),
                                        "LastTransition": (
                                            "V",
                                            "ns=1;i=7387",
                                            {
                                                "Id": ("V", "ns=1;i=7388", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=7622",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "OneShotShelve": ("M", "ns=1;i=7389", {}),
                                        "TimedShelve": (
                                            "M",
                                            "ns=1;i=7390",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=7391",
                                                    {},
                                                )
                                            },
                                        ),
                                        "Unshelve": ("M", "ns=1;i=7392", {}),
                                        "UnshelveTime": ("V", "ns=1;i=7393", {}),
                                    },
                                ),
                                "Silence": ("M", "ns=1;i=7394", {}),
                                "SilenceState": (
                                    "V",
                                    "ns=1;i=7395",
                                    {
                                        "FalseState": ("V", "ns=1;i=7396", {}),
                                        "Id": ("V", "ns=1;i=7397", {}),
                                        "TransitionTime": ("V", "ns=1;i=7398", {}),
                                        "TrueState": ("V", "ns=1;i=7399", {}),
                                    },
                                ),
                                "SourceName": ("V", "ns=1;i=6944", {}),
                                "SourceNode": ("V", "ns=1;i=6945", {}),
                                "Suppress": ("M", "ns=1;i=7400", {}),
                                "SuppressedOrShelved": ("V", "ns=1;i=6946", {}),
                                "SuppressedState": (
                                    "V",
                                    "ns=1;i=7401",
                                    {
                                        "FalseState": ("V", "ns=1;i=7402", {}),
                                        "Id": ("V", "ns=1;i=7403", {}),
                                        "TransitionTime": ("V", "ns=1;i=7404", {}),
                                        "TrueState": ("V", "ns=1;i=7405", {}),
                                    },
                                ),
                                "Time": ("V", "ns=1;i=6947", {}),
                                "Unsuppress": ("M", "ns=1;i=7406", {}),
                            },
                        ),
                        "Service": (
                            "O",
                            "ns=1;i=5086",
                            {
                                "AckedState": (
                                    "V",
                                    "ns=1;i=6948",
                                    {
                                        "FalseState": ("V", "ns=1;i=7583", {}),
                                        "Id": ("V", "ns=1;i=6949", {}),
                                        "TransitionTime": ("V", "ns=1;i=7584", {}),
                                        "TrueState": ("V", "ns=1;i=7585", {}),
                                    },
                                ),
                                "Acknowledge": (
                                    "M",
                                    "ns=1;i=7068",
                                    {"InputArguments": ("V", "ns=1;i=6950", {})},
                                ),
                                "ActiveState": (
                                    "V",
                                    "ns=1;i=6951",
                                    {
                                        "EffectiveDisplayName": (
                                            "V",
                                            "ns=1;i=7586",
                                            {},
                                        ),
                                        "EffectiveTransitionTime": (
                                            "V",
                                            "ns=1;i=7587",
                                            {},
                                        ),
                                        "FalseState": ("V", "ns=1;i=7588", {}),
                                        "Id": ("V", "ns=1;i=6952", {}),
                                        "TransitionTime": ("V", "ns=1;i=7589", {}),
                                        "TrueState": ("V", "ns=1;i=7590", {}),
                                    },
                                ),
                                "AddComment": (
                                    "M",
                                    "ns=1;i=7069",
                                    {"InputArguments": ("V", "ns=1;i=6953", {})},
                                ),
                                "AudibleEnabled": ("V", "ns=1;i=7407", {}),
                                "AudibleSound": ("V", "ns=1;i=8420", {}),
                                "BranchId": ("V", "ns=1;i=6954", {}),
                                "ClientUserId": ("V", "ns=1;i=6955", {}),
                                "Comment": (
                                    "V",
                                    "ns=1;i=6956",
                                    {"SourceTimestamp": ("V", "ns=1;i=6957", {})},
                                ),
                                "ConditionClassId": ("V", "ns=1;i=6958", {}),
                                "ConditionClassName": ("V", "ns=1;i=6959", {}),
                                "ConditionName": ("V", "ns=1;i=6960", {}),
                                "ConditionSubClassId": ("V", "ns=1;i=7409", {}),
                                "ConditionSubClassName": ("V", "ns=1;i=7410", {}),
                                "Confirm": (
                                    "M",
                                    "ns=1;i=7411",
                                    {"InputArguments": ("V", "ns=1;i=7412", {})},
                                ),
                                "ConfirmedState": (
                                    "V",
                                    "ns=1;i=7413",
                                    {
                                        "FalseState": ("V", "ns=1;i=7414", {}),
                                        "Id": ("V", "ns=1;i=7415", {}),
                                        "TransitionTime": ("V", "ns=1;i=7416", {}),
                                        "TrueState": ("V", "ns=1;i=7417", {}),
                                    },
                                ),
                                "Disable": ("M", "ns=1;i=7070", {}),
                                "Enable": ("M", "ns=1;i=7071", {}),
                                "EnabledState": (
                                    "V",
                                    "ns=1;i=6961",
                                    {
                                        "EffectiveDisplayName": (
                                            "V",
                                            "ns=1;i=7591",
                                            {},
                                        ),
                                        "EffectiveTransitionTime": (
                                            "V",
                                            "ns=1;i=7592",
                                            {},
                                        ),
                                        "FalseState": ("V", "ns=1;i=7593", {}),
                                        "Id": ("V", "ns=1;i=6962", {}),
                                        "TransitionTime": ("V", "ns=1;i=7594", {}),
                                        "TrueState": ("V", "ns=1;i=7595", {}),
                                    },
                                ),
                                "EventId": ("V", "ns=1;i=6963", {}),
                                "EventType": ("V", "ns=1;i=6964", {}),
                                "FirstInGroup": ("O", "ns=1;i=5099", {}),
                                "FirstInGroupFlag": ("V", "ns=1;i=7418", {}),
                                "InputNode": ("V", "ns=1;i=6965", {}),
                                "LastSeverity": (
                                    "V",
                                    "ns=1;i=6966",
                                    {"SourceTimestamp": ("V", "ns=1;i=6967", {})},
                                ),
                                "LatchedState": (
                                    "V",
                                    "ns=1;i=7419",
                                    {
                                        "FalseState": ("V", "ns=1;i=7420", {}),
                                        "Id": ("V", "ns=1;i=7421", {}),
                                        "TransitionTime": ("V", "ns=1;i=7422", {}),
                                        "TrueState": ("V", "ns=1;i=7423", {}),
                                    },
                                ),
                                "LocalTime": ("V", "ns=1;i=7424", {}),
                                "MaxTimeShelved": ("V", "ns=1;i=7425", {}),
                                "Message": ("V", "ns=1;i=6968", {}),
                                "NormalState": ("V", "ns=1;i=6969", {}),
                                "OffDelay": ("V", "ns=1;i=7426", {}),
                                "OnDelay": ("V", "ns=1;i=7427", {}),
                                "OutOfServiceState": (
                                    "V",
                                    "ns=1;i=7428",
                                    {
                                        "FalseState": ("V", "ns=1;i=7429", {}),
                                        "Id": ("V", "ns=1;i=7430", {}),
                                        "TransitionTime": ("V", "ns=1;i=7431", {}),
                                        "TrueState": ("V", "ns=1;i=7432", {}),
                                    },
                                ),
                                "PlaceInService": ("M", "ns=1;i=7433", {}),
                                "Quality": (
                                    "V",
                                    "ns=1;i=6970",
                                    {"SourceTimestamp": ("V", "ns=1;i=6971", {})},
                                ),
                                "ReAlarmRepeatCount": ("V", "ns=1;i=7434", {}),
                                "ReAlarmTime": ("V", "ns=1;i=7435", {}),
                                "ReceiveTime": ("V", "ns=1;i=6972", {}),
                                "RemoveFromService": ("M", "ns=1;i=7436", {}),
                                "Reset": ("M", "ns=1;i=7437", {}),
                                "Retain": ("V", "ns=1;i=6973", {}),
                                "Severity": ("V", "ns=1;i=6974", {}),
                                "ShelvingState": (
                                    "O",
                                    "ns=1;i=5100",
                                    {
                                        "CurrentState": (
                                            "V",
                                            "ns=1;i=7438",
                                            {"Id": ("V", "ns=1;i=7439", {})},
                                        ),
                                        "LastTransition": (
                                            "V",
                                            "ns=1;i=7440",
                                            {
                                                "Id": ("V", "ns=1;i=7441", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=7623",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "OneShotShelve": ("M", "ns=1;i=7442", {}),
                                        "TimedShelve": (
                                            "M",
                                            "ns=1;i=7443",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=7444",
                                                    {},
                                                )
                                            },
                                        ),
                                        "Unshelve": ("M", "ns=1;i=7445", {}),
                                        "UnshelveTime": ("V", "ns=1;i=7446", {}),
                                    },
                                ),
                                "Silence": ("M", "ns=1;i=7447", {}),
                                "SilenceState": (
                                    "V",
                                    "ns=1;i=7448",
                                    {
                                        "FalseState": ("V", "ns=1;i=7449", {}),
                                        "Id": ("V", "ns=1;i=7450", {}),
                                        "TransitionTime": ("V", "ns=1;i=7451", {}),
                                        "TrueState": ("V", "ns=1;i=7452", {}),
                                    },
                                ),
                                "SourceName": ("V", "ns=1;i=6975", {}),
                                "SourceNode": ("V", "ns=1;i=6976", {}),
                                "Suppress": ("M", "ns=1;i=7453", {}),
                                "SuppressedOrShelved": ("V", "ns=1;i=6977", {}),
                                "SuppressedState": (
                                    "V",
                                    "ns=1;i=7454",
                                    {
                                        "FalseState": ("V", "ns=1;i=7455", {}),
                                        "Id": ("V", "ns=1;i=7456", {}),
                                        "TransitionTime": ("V", "ns=1;i=7457", {}),
                                        "TrueState": ("V", "ns=1;i=7458", {}),
                                    },
                                ),
                                "Time": ("V", "ns=1;i=6978", {}),
                                "Unsuppress": ("M", "ns=1;i=7459", {}),
                            },
                        ),
                        "Shutdown": (
                            "O",
                            "ns=1;i=5087",
                            {
                                "AckedState": (
                                    "V",
                                    "ns=1;i=7095",
                                    {
                                        "FalseState": ("V", "ns=1;i=7596", {}),
                                        "Id": ("V", "ns=1;i=7096", {}),
                                        "TransitionTime": ("V", "ns=1;i=7597", {}),
                                        "TrueState": ("V", "ns=1;i=7598", {}),
                                    },
                                ),
                                "Acknowledge": (
                                    "M",
                                    "ns=1;i=7097",
                                    {"InputArguments": ("V", "ns=1;i=7098", {})},
                                ),
                                "ActiveState": (
                                    "V",
                                    "ns=1;i=7099",
                                    {
                                        "EffectiveDisplayName": (
                                            "V",
                                            "ns=1;i=7599",
                                            {},
                                        ),
                                        "EffectiveTransitionTime": (
                                            "V",
                                            "ns=1;i=7600",
                                            {},
                                        ),
                                        "FalseState": ("V", "ns=1;i=7601", {}),
                                        "Id": ("V", "ns=1;i=7100", {}),
                                        "TransitionTime": ("V", "ns=1;i=7602", {}),
                                        "TrueState": ("V", "ns=1;i=7603", {}),
                                    },
                                ),
                                "AddComment": (
                                    "M",
                                    "ns=1;i=7101",
                                    {"InputArguments": ("V", "ns=1;i=7102", {})},
                                ),
                                "AudibleEnabled": ("V", "ns=1;i=7460", {}),
                                "AudibleSound": ("V", "ns=1;i=7461", {}),
                                "BranchId": ("V", "ns=1;i=7103", {}),
                                "ClientUserId": ("V", "ns=1;i=7104", {}),
                                "Comment": (
                                    "V",
                                    "ns=1;i=7105",
                                    {"SourceTimestamp": ("V", "ns=1;i=7106", {})},
                                ),
                                "ConditionClassId": ("V", "ns=1;i=7107", {}),
                                "ConditionClassName": ("V", "ns=1;i=7108", {}),
                                "ConditionName": ("V", "ns=1;i=7109", {}),
                                "ConditionSubClassId": ("V", "ns=1;i=7462", {}),
                                "ConditionSubClassName": ("V", "ns=1;i=7463", {}),
                                "Confirm": (
                                    "M",
                                    "ns=1;i=7464",
                                    {"InputArguments": ("V", "ns=1;i=7465", {})},
                                ),
                                "ConfirmedState": (
                                    "V",
                                    "ns=1;i=7466",
                                    {
                                        "FalseState": ("V", "ns=1;i=7467", {}),
                                        "Id": ("V", "ns=1;i=7468", {}),
                                        "TransitionTime": ("V", "ns=1;i=7469", {}),
                                        "TrueState": ("V", "ns=1;i=7470", {}),
                                    },
                                ),
                                "Disable": ("M", "ns=1;i=7110", {}),
                                "Enable": ("M", "ns=1;i=7111", {}),
                                "EnabledState": (
                                    "V",
                                    "ns=1;i=7112",
                                    {
                                        "EffectiveDisplayName": (
                                            "V",
                                            "ns=1;i=7604",
                                            {},
                                        ),
                                        "EffectiveTransitionTime": (
                                            "V",
                                            "ns=1;i=7605",
                                            {},
                                        ),
                                        "FalseState": ("V", "ns=1;i=7606", {}),
                                        "Id": ("V", "ns=1;i=7113", {}),
                                        "TransitionTime": ("V", "ns=1;i=7607", {}),
                                        "TrueState": ("V", "ns=1;i=7608", {}),
                                    },
                                ),
                                "EventId": ("V", "ns=1;i=7114", {}),
                                "EventType": ("V", "ns=1;i=7115", {}),
                                "FirstInGroup": ("O", "ns=1;i=5101", {}),
                                "FirstInGroupFlag": ("V", "ns=1;i=7471", {}),
                                "InputNode": ("V", "ns=1;i=7116", {}),
                                "LastSeverity": (
                                    "V",
                                    "ns=1;i=7117",
                                    {"SourceTimestamp": ("V", "ns=1;i=7118", {})},
                                ),
                                "LatchedState": (
                                    "V",
                                    "ns=1;i=7472",
                                    {
                                        "FalseState": ("V", "ns=1;i=7473", {}),
                                        "Id": ("V", "ns=1;i=7474", {}),
                                        "TransitionTime": ("V", "ns=1;i=7475", {}),
                                        "TrueState": ("V", "ns=1;i=7476", {}),
                                    },
                                ),
                                "LocalTime": ("V", "ns=1;i=7477", {}),
                                "MaxTimeShelved": ("V", "ns=1;i=7478", {}),
                                "Message": ("V", "ns=1;i=7119", {}),
                                "NormalState": ("V", "ns=1;i=7120", {}),
                                "OffDelay": ("V", "ns=1;i=7479", {}),
                                "OnDelay": ("V", "ns=1;i=7480", {}),
                                "OutOfServiceState": (
                                    "V",
                                    "ns=1;i=7481",
                                    {
                                        "FalseState": ("V", "ns=1;i=7482", {}),
                                        "Id": ("V", "ns=1;i=7483", {}),
                                        "TransitionTime": ("V", "ns=1;i=7484", {}),
                                        "TrueState": ("V", "ns=1;i=7485", {}),
                                    },
                                ),
                                "PlaceInService": ("M", "ns=1;i=7486", {}),
                                "Quality": (
                                    "V",
                                    "ns=1;i=7121",
                                    {"SourceTimestamp": ("V", "ns=1;i=7122", {})},
                                ),
                                "ReAlarmRepeatCount": ("V", "ns=1;i=7487", {}),
                                "ReAlarmTime": ("V", "ns=1;i=7488", {}),
                                "ReceiveTime": ("V", "ns=1;i=7123", {}),
                                "RemoveFromService": ("M", "ns=1;i=7489", {}),
                                "Reset": ("M", "ns=1;i=7490", {}),
                                "Retain": ("V", "ns=1;i=7124", {}),
                                "Severity": ("V", "ns=1;i=7125", {}),
                                "ShelvingState": (
                                    "O",
                                    "ns=1;i=5102",
                                    {
                                        "CurrentState": (
                                            "V",
                                            "ns=1;i=7491",
                                            {"Id": ("V", "ns=1;i=7492", {})},
                                        ),
                                        "LastTransition": (
                                            "V",
                                            "ns=1;i=7493",
                                            {
                                                "Id": ("V", "ns=1;i=7494", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=7624",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "OneShotShelve": ("M", "ns=1;i=7495", {}),
                                        "TimedShelve": (
                                            "M",
                                            "ns=1;i=7496",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=7497",
                                                    {},
                                                )
                                            },
                                        ),
                                        "Unshelve": ("M", "ns=1;i=7498", {}),
                                        "UnshelveTime": ("V", "ns=1;i=7499", {}),
                                    },
                                ),
                                "Silence": ("M", "ns=1;i=7500", {}),
                                "SilenceState": (
                                    "V",
                                    "ns=1;i=7501",
                                    {
                                        "FalseState": ("V", "ns=1;i=7502", {}),
                                        "Id": ("V", "ns=1;i=7503", {}),
                                        "TransitionTime": ("V", "ns=1;i=7504", {}),
                                        "TrueState": ("V", "ns=1;i=7505", {}),
                                    },
                                ),
                                "SourceName": ("V", "ns=1;i=7126", {}),
                                "SourceNode": ("V", "ns=1;i=7127", {}),
                                "Suppress": ("M", "ns=1;i=7506", {}),
                                "SuppressedOrShelved": ("V", "ns=1;i=7128", {}),
                                "SuppressedState": (
                                    "V",
                                    "ns=1;i=7507",
                                    {
                                        "FalseState": ("V", "ns=1;i=7508", {}),
                                        "Id": ("V", "ns=1;i=7509", {}),
                                        "TransitionTime": ("V", "ns=1;i=7510", {}),
                                        "TrueState": ("V", "ns=1;i=7511", {}),
                                    },
                                ),
                                "Time": ("V", "ns=1;i=7129", {}),
                                "Unsuppress": ("M", "ns=1;i=7512", {}),
                            },
                        ),
                        "UIElement": ("V", "ns=1;i=6548", {}),
                        "Warning": (
                            "O",
                            "ns=1;i=5090",
                            {
                                "AckedState": (
                                    "V",
                                    "ns=1;i=7130",
                                    {
                                        "FalseState": ("V", "ns=1;i=7609", {}),
                                        "Id": ("V", "ns=1;i=7131", {}),
                                        "TransitionTime": ("V", "ns=1;i=7610", {}),
                                        "TrueState": ("V", "ns=1;i=7611", {}),
                                    },
                                ),
                                "Acknowledge": (
                                    "M",
                                    "ns=1;i=7132",
                                    {"InputArguments": ("V", "ns=1;i=7133", {})},
                                ),
                                "ActiveState": (
                                    "V",
                                    "ns=1;i=7134",
                                    {
                                        "EffectiveDisplayName": (
                                            "V",
                                            "ns=1;i=7612",
                                            {},
                                        ),
                                        "EffectiveTransitionTime": (
                                            "V",
                                            "ns=1;i=7613",
                                            {},
                                        ),
                                        "FalseState": ("V", "ns=1;i=7614", {}),
                                        "Id": ("V", "ns=1;i=7135", {}),
                                        "TransitionTime": ("V", "ns=1;i=7615", {}),
                                        "TrueState": ("V", "ns=1;i=7616", {}),
                                    },
                                ),
                                "AddComment": (
                                    "M",
                                    "ns=1;i=7136",
                                    {"InputArguments": ("V", "ns=1;i=7137", {})},
                                ),
                                "AudibleEnabled": ("V", "ns=1;i=7513", {}),
                                "AudibleSound": ("V", "ns=1;i=8526", {}),
                                "BranchId": ("V", "ns=1;i=7138", {}),
                                "ClientUserId": ("V", "ns=1;i=7139", {}),
                                "Comment": (
                                    "V",
                                    "ns=1;i=7140",
                                    {"SourceTimestamp": ("V", "ns=1;i=7141", {})},
                                ),
                                "ConditionClassId": ("V", "ns=1;i=7142", {}),
                                "ConditionClassName": ("V", "ns=1;i=7143", {}),
                                "ConditionName": ("V", "ns=1;i=7144", {}),
                                "ConditionSubClassId": ("V", "ns=1;i=7515", {}),
                                "ConditionSubClassName": ("V", "ns=1;i=7516", {}),
                                "Confirm": (
                                    "M",
                                    "ns=1;i=7517",
                                    {"InputArguments": ("V", "ns=1;i=7518", {})},
                                ),
                                "ConfirmedState": (
                                    "V",
                                    "ns=1;i=7519",
                                    {
                                        "FalseState": ("V", "ns=1;i=7520", {}),
                                        "Id": ("V", "ns=1;i=7521", {}),
                                        "TransitionTime": ("V", "ns=1;i=7522", {}),
                                        "TrueState": ("V", "ns=1;i=7523", {}),
                                    },
                                ),
                                "Disable": ("M", "ns=1;i=7145", {}),
                                "Enable": ("M", "ns=1;i=7146", {}),
                                "EnabledState": (
                                    "V",
                                    "ns=1;i=7147",
                                    {
                                        "EffectiveDisplayName": (
                                            "V",
                                            "ns=1;i=7617",
                                            {},
                                        ),
                                        "EffectiveTransitionTime": (
                                            "V",
                                            "ns=1;i=7618",
                                            {},
                                        ),
                                        "FalseState": ("V", "ns=1;i=7619", {}),
                                        "Id": ("V", "ns=1;i=7148", {}),
                                        "TransitionTime": ("V", "ns=1;i=7620", {}),
                                        "TrueState": ("V", "ns=1;i=7621", {}),
                                    },
                                ),
                                "EventId": ("V", "ns=1;i=7149", {}),
                                "EventType": ("V", "ns=1;i=7150", {}),
                                "FirstInGroup": ("O", "ns=1;i=5103", {}),
                                "FirstInGroupFlag": ("V", "ns=1;i=7524", {}),
                                "InputNode": ("V", "ns=1;i=7151", {}),
                                "LastSeverity": (
                                    "V",
                                    "ns=1;i=7152",
                                    {"SourceTimestamp": ("V", "ns=1;i=7153", {})},
                                ),
                                "LatchedState": (
                                    "V",
                                    "ns=1;i=7525",
                                    {
                                        "FalseState": ("V", "ns=1;i=7526", {}),
                                        "Id": ("V", "ns=1;i=7527", {}),
                                        "TransitionTime": ("V", "ns=1;i=7528", {}),
                                        "TrueState": ("V", "ns=1;i=7529", {}),
                                    },
                                ),
                                "LocalTime": ("V", "ns=1;i=7530", {}),
                                "MaxTimeShelved": ("V", "ns=1;i=7531", {}),
                                "Message": ("V", "ns=1;i=7154", {}),
                                "NormalState": ("V", "ns=1;i=7155", {}),
                                "OffDelay": ("V", "ns=1;i=7532", {}),
                                "OnDelay": ("V", "ns=1;i=7533", {}),
                                "OutOfServiceState": (
                                    "V",
                                    "ns=1;i=7534",
                                    {
                                        "FalseState": ("V", "ns=1;i=7535", {}),
                                        "Id": ("V", "ns=1;i=7536", {}),
                                        "TransitionTime": ("V", "ns=1;i=7537", {}),
                                        "TrueState": ("V", "ns=1;i=7538", {}),
                                    },
                                ),
                                "PlaceInService": ("M", "ns=1;i=7539", {}),
                                "Quality": (
                                    "V",
                                    "ns=1;i=7156",
                                    {"SourceTimestamp": ("V", "ns=1;i=7157", {})},
                                ),
                                "ReAlarmRepeatCount": ("V", "ns=1;i=7540", {}),
                                "ReAlarmTime": ("V", "ns=1;i=7541", {}),
                                "ReceiveTime": ("V", "ns=1;i=7158", {}),
                                "RemoveFromService": ("M", "ns=1;i=7542", {}),
                                "Reset": ("M", "ns=1;i=7543", {}),
                                "Retain": ("V", "ns=1;i=7159", {}),
                                "Severity": ("V", "ns=1;i=7160", {}),
                                "ShelvingState": (
                                    "O",
                                    "ns=1;i=5104",
                                    {
                                        "CurrentState": (
                                            "V",
                                            "ns=1;i=7544",
                                            {"Id": ("V", "ns=1;i=7545", {})},
                                        ),
                                        "LastTransition": (
                                            "V",
                                            "ns=1;i=7546",
                                            {
                                                "Id": ("V", "ns=1;i=7547", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=7625",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "OneShotShelve": ("M", "ns=1;i=7548", {}),
                                        "TimedShelve": (
                                            "M",
                                            "ns=1;i=7549",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=7550",
                                                    {},
                                                )
                                            },
                                        ),
                                        "Unshelve": ("M", "ns=1;i=7551", {}),
                                        "UnshelveTime": ("V", "ns=1;i=7552", {}),
                                    },
                                ),
                                "Silence": ("M", "ns=1;i=7553", {}),
                                "SilenceState": (
                                    "V",
                                    "ns=1;i=7554",
                                    {
                                        "FalseState": ("V", "ns=1;i=7555", {}),
                                        "Id": ("V", "ns=1;i=7556", {}),
                                        "TransitionTime": ("V", "ns=1;i=7557", {}),
                                        "TrueState": ("V", "ns=1;i=7558", {}),
                                    },
                                ),
                                "SourceName": ("V", "ns=1;i=7161", {}),
                                "SourceNode": ("V", "ns=1;i=7162", {}),
                                "Suppress": ("M", "ns=1;i=7559", {}),
                                "SuppressedOrShelved": ("V", "ns=1;i=7163", {}),
                                "SuppressedState": (
                                    "V",
                                    "ns=1;i=7560",
                                    {
                                        "FalseState": ("V", "ns=1;i=7561", {}),
                                        "Id": ("V", "ns=1;i=7562", {}),
                                        "TransitionTime": ("V", "ns=1;i=7563", {}),
                                        "TrueState": ("V", "ns=1;i=7564", {}),
                                    },
                                ),
                                "Time": ("V", "ns=1;i=7164", {}),
                                "Unsuppress": ("M", "ns=1;i=7565", {}),
                            },
                        ),
                    },
                ),
                "FilterType": (
                    "OT",
                    "ns=1;i=1034",
                    {
                        "Design": (
                            "O",
                            "ns=1;i=5061",
                            {
                                "ComponentClass": (
                                    "V",
                                    "ns=1;i=6087",
                                    {"Definition": ("V", "ns=1;i=8059", {})},
                                ),
                                "FilterClass": (
                                    "V",
                                    "ns=1;i=8060",
                                    {"Definition": ("V", "ns=1;i=8061", {})},
                                ),
                            },
                        )
                    },
                ),
                "HeatRecoverySystemType": ("OT", "ns=1;i=1042", {}),
                "Identification": (
                    "O",
                    "ns=1;i=5005",
                    {
                        "AssetId": ("V", "ns=1;i=6381", {}),
                        "ComponentName": ("V", "ns=1;i=6382", {}),
                        "DeviceClass": ("V", "ns=1;i=6383", {}),
                        "HardwareRevision": ("V", "ns=1;i=6384", {}),
                        "InitialOperationDate": ("V", "ns=1;i=6385", {}),
                        "Manufacturer": ("V", "ns=1;i=6047", {}),
                        "ManufacturerUri": ("V", "ns=1;i=6386", {}),
                        "Model": ("V", "ns=1;i=6387", {}),
                        "MonthOfConstruction": ("V", "ns=1;i=6388", {}),
                        "ProductCode": ("V", "ns=1;i=6389", {}),
                        "ProductInstanceUri": ("V", "ns=1;i=6390", {}),
                        "SerialNumber": ("V", "ns=1;i=6133", {}),
                        "SoftwareRevision": ("V", "ns=1;i=6391", {}),
                        "UIElement": ("V", "ns=1;i=7884", {}),
                        "YearOfConstruction": ("V", "ns=1;i=7885", {}),
                    },
                ),
                "Operational": (
                    "O",
                    "ns=1;i=5036",
                    {
                        "HealthState": (
                            "V",
                            "ns=1;i=10715",
                            {
                                "Definition": ("V", "ns=1;i=10721", {}),
                                "ValuePrecision": ("V", "ns=1;i=10722", {}),
                            },
                        ),
                        "IntegratedState": (
                            "V",
                            "ns=1;i=10716",
                            {
                                "Definition": ("V", "ns=1;i=10723", {}),
                                "ValuePrecision": ("V", "ns=1;i=10724", {}),
                            },
                        ),
                        "OnOff": (
                            "V",
                            "ns=1;i=10717",
                            {
                                "Definition": ("V", "ns=1;i=10725", {}),
                                "FalseState": ("V", "ns=1;i=10718", {}),
                                "TrueState": ("V", "ns=1;i=10719", {}),
                                "ValuePrecision": ("V", "ns=1;i=10726", {}),
                            },
                        ),
                        "OperatingState": (
                            "V",
                            "ns=1;i=10720",
                            {
                                "Definition": ("V", "ns=1;i=10727", {}),
                                "ValuePrecision": ("V", "ns=1;i=10728", {}),
                            },
                        ),
                        "UIElement": ("V", "ns=1;i=6547", {}),
                    },
                ),
                "ProcessFluidCircuit": (
                    "O",
                    "ns=1;i=5135",
                    {
                        "Delta": (
                            "O",
                            "ns=1;i=5165",
                            {
                                "AbsolutePressure": (
                                    "V",
                                    "ns=1;i=7813",
                                    {
                                        "Definition": ("V", "ns=1;i=7951", {}),
                                        "EURange": ("V", "ns=1;i=7953", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7952", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7954", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7955", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7956", {}),
                                    },
                                ),
                                "AccumulatedVolume": (
                                    "V",
                                    "ns=1;i=7055",
                                    {
                                        "Definition": ("V", "ns=1;i=7348", {}),
                                        "EURange": ("V", "ns=1;i=7350", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7349", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7351", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7626", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7627", {}),
                                    },
                                ),
                                "DewPoint": (
                                    "V",
                                    "ns=1;i=7057",
                                    {
                                        "Definition": ("V", "ns=1;i=7628", {}),
                                        "EURange": ("V", "ns=1;i=7630", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7629", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7631", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7632", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7633", {}),
                                    },
                                ),
                                "GaugePressure": (
                                    "V",
                                    "ns=1;i=7058",
                                    {
                                        "Definition": ("V", "ns=1;i=7634", {}),
                                        "EURange": ("V", "ns=1;i=7636", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7635", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7637", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7638", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7639", {}),
                                    },
                                ),
                                "MassFlowRate": (
                                    "V",
                                    "ns=1;i=7059",
                                    {
                                        "Definition": ("V", "ns=1;i=7640", {}),
                                        "EURange": ("V", "ns=1;i=7642", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7641", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7643", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7644", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7645", {}),
                                    },
                                ),
                                "OilConcentration": (
                                    "V",
                                    "ns=1;i=7061",
                                    {
                                        "Definition": ("V", "ns=1;i=7646", {}),
                                        "EURange": ("V", "ns=1;i=7648", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7647", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7649", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7650", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7651", {}),
                                    },
                                ),
                                "ParticlesPerSizeRange": (
                                    "O",
                                    "ns=1;i=5172",
                                    {
                                        "Fine": (
                                            "V",
                                            "ns=1;i=6568",
                                            {
                                                "Definition": ("V", "ns=1;i=7739", {}),
                                                "EURange": ("V", "ns=1;i=7741", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=7740",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=7742",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8793",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=7755",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Large": (
                                            "V",
                                            "ns=1;i=6569",
                                            {
                                                "Definition": ("V", "ns=1;i=9054", {}),
                                                "EURange": ("V", "ns=1;i=9056", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9055",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9057",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9058",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9063",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Medium": (
                                            "V",
                                            "ns=1;i=6570",
                                            {
                                                "Definition": ("V", "ns=1;i=10336", {}),
                                                "EURange": ("V", "ns=1;i=10338", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10337",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10339",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10340",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10341",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "RelativeHumidity": (
                                    "V",
                                    "ns=1;i=7166",
                                    {
                                        "Definition": ("V", "ns=1;i=7652", {}),
                                        "EURange": ("V", "ns=1;i=7665", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7653", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7668", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7669", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7670", {}),
                                    },
                                ),
                                "ResetStatistics": ("M", "ns=1;i=7167", {}),
                                "StartTime": ("V", "ns=1;i=7168", {}),
                                "Temperature": (
                                    "V",
                                    "ns=1;i=7169",
                                    {
                                        "Definition": ("V", "ns=1;i=7671", {}),
                                        "EURange": ("V", "ns=1;i=7673", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7672", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7675", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7676", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7677", {}),
                                    },
                                ),
                                "Volume": (
                                    "V",
                                    "ns=1;i=7170",
                                    {
                                        "Definition": ("V", "ns=1;i=7678", {}),
                                        "EURange": ("V", "ns=1;i=7681", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7679", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7683", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7684", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7685", {}),
                                    },
                                ),
                                "VolumeFlowRate": (
                                    "V",
                                    "ns=1;i=7171",
                                    {
                                        "Definition": ("V", "ns=1;i=7686", {}),
                                        "EURange": ("V", "ns=1;i=7688", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7687", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7689", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=7690", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7691", {}),
                                    },
                                ),
                            },
                        ),
                        "FluidType": (
                            "V",
                            "ns=1;i=9147",
                            {"Definition": ("V", "ns=1;i=9305", {})},
                        ),
                        "Inlet": (
                            "O",
                            "ns=1;i=5166",
                            {
                                "AbsolutePressure": (
                                    "V",
                                    "ns=1;i=8808",
                                    {
                                        "Definition": ("V", "ns=1;i=9129", {}),
                                        "EURange": ("V", "ns=1;i=9131", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9130", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9132", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9133", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9134", {}),
                                    },
                                ),
                                "AccumulatedVolume": (
                                    "V",
                                    "ns=1;i=8809",
                                    {
                                        "Definition": ("V", "ns=1;i=9135", {}),
                                        "EURange": ("V", "ns=1;i=9137", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9136", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9138", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9139", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9145", {}),
                                    },
                                ),
                                "DewPoint": (
                                    "V",
                                    "ns=1;i=8810",
                                    {
                                        "Definition": ("V", "ns=1;i=9146", {}),
                                        "EURange": ("V", "ns=1;i=9149", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9148", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9150", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9151", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9152", {}),
                                    },
                                ),
                                "GaugePressure": (
                                    "V",
                                    "ns=1;i=8811",
                                    {
                                        "Definition": ("V", "ns=1;i=9153", {}),
                                        "EURange": ("V", "ns=1;i=9155", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9154", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9156", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9157", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9158", {}),
                                    },
                                ),
                                "MassFlowRate": (
                                    "V",
                                    "ns=1;i=8812",
                                    {
                                        "Definition": ("V", "ns=1;i=9159", {}),
                                        "EURange": ("V", "ns=1;i=9161", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9160", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9162", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9163", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9164", {}),
                                    },
                                ),
                                "OilConcentration": (
                                    "V",
                                    "ns=1;i=8828",
                                    {
                                        "Definition": ("V", "ns=1;i=9165", {}),
                                        "EURange": ("V", "ns=1;i=9167", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9166", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9168", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9169", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9175", {}),
                                    },
                                ),
                                "ParticlesPerSizeRange": (
                                    "O",
                                    "ns=1;i=5181",
                                    {
                                        "Fine": (
                                            "V",
                                            "ns=1;i=6571",
                                            {
                                                "Definition": ("V", "ns=1;i=7756", {}),
                                                "EURange": ("V", "ns=1;i=7758", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=7757",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=7759",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8799",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=7760",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Large": (
                                            "V",
                                            "ns=1;i=6572",
                                            {
                                                "Definition": ("V", "ns=1;i=9064", {}),
                                                "EURange": ("V", "ns=1;i=9066", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9065",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9067",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9075",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9078",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Medium": (
                                            "V",
                                            "ns=1;i=6573",
                                            {
                                                "Definition": ("V", "ns=1;i=10342", {}),
                                                "EURange": ("V", "ns=1;i=10344", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10343",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10345",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10346",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10347",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "RelativeHumidity": (
                                    "V",
                                    "ns=1;i=8844",
                                    {
                                        "Definition": ("V", "ns=1;i=9191", {}),
                                        "EURange": ("V", "ns=1;i=9193", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9192", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9194", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9195", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9196", {}),
                                    },
                                ),
                                "ResetStatistics": ("M", "ns=1;i=8845", {}),
                                "StartTime": ("V", "ns=1;i=8846", {}),
                                "Temperature": (
                                    "V",
                                    "ns=1;i=8847",
                                    {
                                        "Definition": ("V", "ns=1;i=9197", {}),
                                        "EURange": ("V", "ns=1;i=9199", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9198", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9200", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9201", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9202", {}),
                                    },
                                ),
                                "Volume": (
                                    "V",
                                    "ns=1;i=8848",
                                    {
                                        "Definition": ("V", "ns=1;i=9203", {}),
                                        "EURange": ("V", "ns=1;i=9210", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9204", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9211", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9212", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9213", {}),
                                    },
                                ),
                                "VolumeFlowRate": (
                                    "V",
                                    "ns=1;i=8849",
                                    {
                                        "Definition": ("V", "ns=1;i=9214", {}),
                                        "EURange": ("V", "ns=1;i=9216", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9215", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9217", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9218", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9219", {}),
                                    },
                                ),
                            },
                        ),
                        "Outlet": (
                            "O",
                            "ns=1;i=5169",
                            {
                                "AbsolutePressure": (
                                    "V",
                                    "ns=1;i=9332",
                                    {
                                        "Definition": ("V", "ns=1;i=9488", {}),
                                        "EURange": ("V", "ns=1;i=9490", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9489", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9496", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9497", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9498", {}),
                                    },
                                ),
                                "AccumulatedVolume": (
                                    "V",
                                    "ns=1;i=9333",
                                    {
                                        "Definition": ("V", "ns=1;i=9499", {}),
                                        "EURange": ("V", "ns=1;i=9501", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9500", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9502", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9503", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9504", {}),
                                    },
                                ),
                                "DewPoint": (
                                    "V",
                                    "ns=1;i=9334",
                                    {
                                        "Definition": ("V", "ns=1;i=9505", {}),
                                        "EURange": ("V", "ns=1;i=9507", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9506", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9508", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9509", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9510", {}),
                                    },
                                ),
                                "GaugePressure": (
                                    "V",
                                    "ns=1;i=9340",
                                    {
                                        "Definition": ("V", "ns=1;i=9511", {}),
                                        "EURange": ("V", "ns=1;i=9513", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9512", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9514", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9515", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9516", {}),
                                    },
                                ),
                                "MassFlowRate": (
                                    "V",
                                    "ns=1;i=9341",
                                    {
                                        "Definition": ("V", "ns=1;i=9517", {}),
                                        "EURange": ("V", "ns=1;i=9519", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9518", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9520", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9521", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9522", {}),
                                    },
                                ),
                                "OilConcentration": (
                                    "V",
                                    "ns=1;i=9342",
                                    {
                                        "Definition": ("V", "ns=1;i=9523", {}),
                                        "EURange": ("V", "ns=1;i=9525", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9524", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9526", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9527", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9528", {}),
                                    },
                                ),
                                "ParticlesPerSizeRange": (
                                    "O",
                                    "ns=1;i=5182",
                                    {
                                        "Fine": (
                                            "V",
                                            "ns=1;i=7180",
                                            {
                                                "Definition": ("V", "ns=1;i=7980", {}),
                                                "EURange": ("V", "ns=1;i=7982", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=7981",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=7983",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8800",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=7984",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Large": (
                                            "V",
                                            "ns=1;i=7181",
                                            {
                                                "Definition": ("V", "ns=1;i=9083", {}),
                                                "EURange": ("V", "ns=1;i=9086", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9084",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9087",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9088",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9089",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Medium": (
                                            "V",
                                            "ns=1;i=7182",
                                            {
                                                "Definition": ("V", "ns=1;i=10348", {}),
                                                "EURange": ("V", "ns=1;i=10350", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10349",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10351",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10352",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10353",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "RelativeHumidity": (
                                    "V",
                                    "ns=1;i=9343",
                                    {
                                        "Definition": ("V", "ns=1;i=9529", {}),
                                        "EURange": ("V", "ns=1;i=9531", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9530", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9532", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9533", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9534", {}),
                                    },
                                ),
                                "ResetStatistics": ("M", "ns=1;i=9344", {}),
                                "StartTime": ("V", "ns=1;i=9345", {}),
                                "Temperature": (
                                    "V",
                                    "ns=1;i=9346",
                                    {
                                        "Definition": ("V", "ns=1;i=9541", {}),
                                        "EURange": ("V", "ns=1;i=9543", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9542", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9544", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9545", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9546", {}),
                                    },
                                ),
                                "Volume": (
                                    "V",
                                    "ns=1;i=9347",
                                    {
                                        "Definition": ("V", "ns=1;i=9547", {}),
                                        "EURange": ("V", "ns=1;i=9549", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9548", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9550", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9551", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9552", {}),
                                    },
                                ),
                                "VolumeFlowRate": (
                                    "V",
                                    "ns=1;i=9348",
                                    {
                                        "Definition": ("V", "ns=1;i=9553", {}),
                                        "EURange": ("V", "ns=1;i=9555", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9554", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9556", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9557", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9558", {}),
                                    },
                                ),
                            },
                        ),
                    },
                ),
                "ReceiverType": (
                    "OT",
                    "ns=1;i=1022",
                    {
                        "Design": (
                            "O",
                            "ns=1;i=5062",
                            {
                                "ComponentClass": (
                                    "V",
                                    "ns=1;i=6088",
                                    {"Definition": ("V", "ns=1;i=6469", {})},
                                ),
                                "Volume": (
                                    "V",
                                    "ns=1;i=10637",
                                    {
                                        "Definition": ("V", "ns=1;i=10639", {}),
                                        "EURange": ("V", "ns=1;i=10640", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10638", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10641", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10642", {}),
                                    },
                                ),
                            },
                        )
                    },
                ),
                "SensorType": (
                    "OT",
                    "ns=1;i=1015",
                    {
                        "Calibration": (
                            "O",
                            "ns=1;i=5002",
                            {
                                "LastCalibrationDate": (
                                    "V",
                                    "ns=1;i=6293",
                                    {"Definition": ("V", "ns=1;i=6296", {})},
                                ),
                                "NextCalibrationDate": (
                                    "V",
                                    "ns=1;i=6294",
                                    {"Definition": ("V", "ns=1;i=6688", {})},
                                ),
                            },
                        ),
                        "Design": (
                            "O",
                            "ns=1;i=5064",
                            {
                                "ComponentClass": (
                                    "V",
                                    "ns=1;i=6089",
                                    {"Definition": ("V", "ns=1;i=6689", {})},
                                ),
                                "SensorTechnology": (
                                    "V",
                                    "ns=1;i=6690",
                                    {"Definition": ("V", "ns=1;i=6692", {})},
                                ),
                                "SoftSensor": (
                                    "V",
                                    "ns=1;i=6799",
                                    {
                                        "Definition": ("V", "ns=1;i=10531", {}),
                                        "FalseState": ("V", "ns=1;i=6800", {}),
                                        "TrueState": ("V", "ns=1;i=8162", {}),
                                    },
                                ),
                            },
                        ),
                        "Maintenance": (
                            "O",
                            "ns=1;i=5149",
                            {
                                "RealTimeSinceLastService": (
                                    "V",
                                    "ns=1;i=10224",
                                    {
                                        "Definition": ("V", "ns=1;i=10233", {}),
                                        "EURange": ("V", "ns=1;i=10235", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10234", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10299", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10300", {}),
                                    },
                                ),
                                "RealTimeToNextService": (
                                    "V",
                                    "ns=1;i=10226",
                                    {
                                        "Definition": ("V", "ns=1;i=10306", {}),
                                        "EURange": ("V", "ns=1;i=11331", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=11330", {}),
                                        "InstrumentRange": ("V", "ns=1;i=11332", {}),
                                        "ValuePrecision": ("V", "ns=1;i=11333", {}),
                                    },
                                ),
                            },
                        ),
                        "Operational": (
                            "O",
                            "ns=1;i=5137",
                            {
                                "<Quantity>": (
                                    "V",
                                    "ns=1;i=10085",
                                    {
                                        "Definition": ("V", "ns=1;i=6461", {}),
                                        "EURange": ("V", "ns=1;i=6462", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7699", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7700", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7701", {}),
                                    },
                                )
                            },
                        ),
                    },
                ),
                "SeparatorType": (
                    "OT",
                    "ns=1;i=1026",
                    {
                        "Design": (
                            "O",
                            "ns=1;i=5048",
                            {
                                "ComponentClass": (
                                    "V",
                                    "ns=1;i=6084",
                                    {"Definition": ("V", "ns=1;i=7272", {})},
                                )
                            },
                        ),
                        "ProcessFluidCircuit": (
                            "O",
                            "ns=1;i=5184",
                            {
                                "FluidType": (
                                    "V",
                                    "ns=1;i=10516",
                                    {"Definition": ("V", "ns=1;i=10519", {})},
                                )
                            },
                        ),
                    },
                ),
                "Statistics": (
                    "O",
                    "ns=1;i=5130",
                    {
                        "RealTime": (
                            "V",
                            "ns=1;i=6053",
                            {
                                "Definition": ("V", "ns=1;i=6321", {}),
                                "EURange": ("V", "ns=1;i=6322", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6330", {}),
                                "InstrumentRange": ("V", "ns=1;i=6331", {}),
                                "ValuePrecision": ("V", "ns=1;i=6333", {}),
                            },
                        ),
                        "RealTimeToNextService": (
                            "V",
                            "ns=1;i=6396",
                            {
                                "Definition": ("V", "ns=1;i=10283", {}),
                                "EURange": ("V", "ns=1;i=10285", {}),
                                "EngineeringUnits": ("V", "ns=1;i=10284", {}),
                                "InstrumentRange": ("V", "ns=1;i=10286", {}),
                                "ValuePrecision": ("V", "ns=1;i=10288", {}),
                            },
                        ),
                        "ResetCondition": ("V", "ns=1;i=6054", {}),
                        "ResetStatistics": ("M", "ns=1;i=7661", {}),
                        "RunningTime": (
                            "V",
                            "ns=1;i=6056",
                            {
                                "Definition": ("V", "ns=1;i=6334", {}),
                                "EURange": ("V", "ns=1;i=6476", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6477", {}),
                                "InstrumentRange": ("V", "ns=1;i=6478", {}),
                                "ValuePrecision": ("V", "ns=1;i=6479", {}),
                            },
                        ),
                        "RunningTimeToNextService": (
                            "V",
                            "ns=1;i=7579",
                            {
                                "Definition": ("V", "ns=1;i=10298", {}),
                                "EURange": ("V", "ns=1;i=10613", {}),
                                "EngineeringUnits": ("V", "ns=1;i=10612", {}),
                                "InstrumentRange": ("V", "ns=1;i=10614", {}),
                                "ValuePrecision": ("V", "ns=1;i=10616", {}),
                            },
                        ),
                        "StartTime": ("V", "ns=1;i=6060", {}),
                        "UIElement": ("V", "ns=1;i=6509", {}),
                    },
                ),
                "ValveType": (
                    "OT",
                    "ns=1;i=1024",
                    {
                        "Design": (
                            "O",
                            "ns=1;i=5065",
                            {
                                "ComponentClass": (
                                    "V",
                                    "ns=1;i=6090",
                                    {"Definition": ("V", "ns=1;i=8057", {})},
                                ),
                                "NumberOfPorts": (
                                    "V",
                                    "ns=1;i=6091",
                                    {"Definition": ("V", "ns=1;i=8058", {})},
                                ),
                            },
                        ),
                        "Operational": (
                            "O",
                            "ns=1;i=5161",
                            {
                                "ContinuousPosition": (
                                    "V",
                                    "ns=1;i=10691",
                                    {
                                        "Definition": ("V", "ns=1;i=10700", {}),
                                        "EURange": ("V", "ns=1;i=10701", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10702", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10703", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10704", {}),
                                    },
                                ),
                                "PortUsed": (
                                    "V",
                                    "ns=1;i=10699",
                                    {
                                        "Definition": ("V", "ns=1;i=10713", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10714", {}),
                                    },
                                ),
                            },
                        ),
                    },
                ),
            },
        ),
        "CASIdentificationType": (
            "OT",
            "ns=1;i=1051",
            {
                "AssetId": ("V", "ns=1;i=7702", {}),
                "ComponentName": ("V", "ns=1;i=7703", {}),
            },
        ),
        "CASType": (
            "OT",
            "ns=1;i=1035",
            {
                "Airnets": ("O", "ns=1;i=5006", {}),
                "Components": (
                    "O",
                    "ns=1;i=5013",
                    {
                        "ChargingSystems": ("O", "ns=1;i=5197", {}),
                        "Compressors": ("O", "ns=1;i=5198", {}),
                        "CondensateDrains": ("O", "ns=1;i=5199", {}),
                        "CondensateSeparators": ("O", "ns=1;i=5200", {}),
                        "Converters": ("O", "ns=1;i=5203", {}),
                        "CoolingSystems": ("O", "ns=1;i=5204", {}),
                        "Dryers": ("O", "ns=1;i=5205", {}),
                        "Filters": ("O", "ns=1;i=5207", {}),
                        "HeatRecoverySystems": ("O", "ns=1;i=5208", {}),
                        "Receivers": ("O", "ns=1;i=5209", {}),
                        "Sensors": ("O", "ns=1;i=5210", {}),
                        "Valves": ("O", "ns=1;i=5211", {}),
                    },
                ),
                "Identification": (
                    "O",
                    "ns=1;i=5003",
                    {
                        "AssetId": ("V", "ns=1;i=6234", {}),
                        "ComponentName": ("V", "ns=1;i=6235", {}),
                        "UIElement": ("V", "ns=1;i=6295", {}),
                    },
                ),
                "MCS": (
                    "O",
                    "ns=1;i=5387",
                    {
                        "Analyses": (
                            "O",
                            "ns=1;i=5701",
                            {
                                "EnergyReportISO50001": (
                                    "O",
                                    "ns=1;i=5115",
                                    {
                                        "OutputFile": (
                                            "O",
                                            "ns=1;i=5121",
                                            {
                                                "Close": (
                                                    "M",
                                                    "ns=1;i=9890",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=1;i=9891",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "GetPosition": (
                                                    "M",
                                                    "ns=1;i=9892",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=1;i=9893",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "ns=1;i=9894",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "MimeType": ("V", "ns=1;i=11372", {}),
                                                "Open": (
                                                    "M",
                                                    "ns=1;i=9895",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=1;i=9896",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "ns=1;i=9897",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "OpenCount": ("V", "ns=1;i=9898", {}),
                                                "Read": (
                                                    "M",
                                                    "ns=1;i=9899",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=1;i=9900",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "ns=1;i=9901",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "SetPosition": (
                                                    "M",
                                                    "ns=1;i=9902",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=1;i=9903",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "Size": ("V", "ns=1;i=9904", {}),
                                                "UserWritable": (
                                                    "V",
                                                    "ns=1;i=9905",
                                                    {},
                                                ),
                                                "Writable": ("V", "ns=1;i=9906", {}),
                                                "Write": (
                                                    "M",
                                                    "ns=1;i=9907",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=1;i=9908",
                                                            {},
                                                        )
                                                    },
                                                ),
                                            },
                                        ),
                                        "Trigger": ("M", "ns=1;i=9829", {}),
                                    },
                                ),
                                "UIElement": ("V", "ns=1;i=8069", {}),
                            },
                        ),
                        "Configuration": (
                            "O",
                            "ns=1;i=5702",
                            {
                                "CommunicationSettings": (
                                    "O",
                                    "ns=1;i=5705",
                                    {
                                        "DefaultGateway": ("V", "ns=1;i=11319", {}),
                                        "Dhcp": (
                                            "V",
                                            "ns=1;i=11320",
                                            {
                                                "Definition": ("V", "ns=1;i=11329", {}),
                                                "FalseState": ("V", "ns=1;i=11321", {}),
                                                "TrueState": ("V", "ns=1;i=11322", {}),
                                            },
                                        ),
                                        "DnsServer": ("V", "ns=1;i=11323", {}),
                                        "DomainName": ("V", "ns=1;i=18629", {}),
                                        "Hostname": ("V", "ns=1;i=18630", {}),
                                        "IpAddress": ("V", "ns=1;i=18631", {}),
                                        "IpVersion": ("V", "ns=1;i=11324", {}),
                                        "SubnetMask": ("V", "ns=1;i=11326", {}),
                                    },
                                ),
                                "ConfigurationFile": (
                                    "O",
                                    "ns=1;i=5126",
                                    {
                                        "Close": (
                                            "M",
                                            "ns=1;i=9930",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=9931",
                                                    {},
                                                )
                                            },
                                        ),
                                        "GetPosition": (
                                            "M",
                                            "ns=1;i=9932",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=9933",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=9934",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "MimeType": ("V", "ns=1;i=6401", {}),
                                        "Open": (
                                            "M",
                                            "ns=1;i=9935",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=9936",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=9937",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "OpenCount": ("V", "ns=1;i=9938", {}),
                                        "Read": (
                                            "M",
                                            "ns=1;i=9939",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=9940",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=9941",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "SetPosition": (
                                            "M",
                                            "ns=1;i=9942",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=9943",
                                                    {},
                                                )
                                            },
                                        ),
                                        "Size": ("V", "ns=1;i=9944", {}),
                                        "UserWritable": ("V", "ns=1;i=9945", {}),
                                        "Writable": ("V", "ns=1;i=9946", {}),
                                        "Write": (
                                            "M",
                                            "ns=1;i=9947",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=9948",
                                                    {},
                                                )
                                            },
                                        ),
                                    },
                                ),
                                "LoadConfigurationFile": ("M", "ns=1;i=9949", {}),
                                "SaveConfigurationFile": ("M", "ns=1;i=10127", {}),
                                "UIElement": ("V", "ns=1;i=8067", {}),
                            },
                        ),
                        "ElectricalCircuit": (
                            "O",
                            "ns=1;i=5141",
                            {
                                "Delta": (
                                    "O",
                                    "ns=1;i=5142",
                                    {
                                        "ApparentPower": (
                                            "V",
                                            "ns=1;i=7829",
                                            {
                                                "Definition": ("V", "ns=1;i=8513", {}),
                                                "EURange": ("V", "ns=1;i=8833", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=8514",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=8834",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8835",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=8836",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Current": (
                                            "V",
                                            "ns=1;i=7830",
                                            {
                                                "Definition": ("V", "ns=1;i=8837", {}),
                                                "EURange": ("V", "ns=1;i=8839", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=8838",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=8840",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=8841",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9059",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Energy": (
                                            "V",
                                            "ns=1;i=7831",
                                            {
                                                "Definition": ("V", "ns=1;i=9060", {}),
                                                "EURange": ("V", "ns=1;i=9062", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9061",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9140",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9141",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Power": (
                                            "V",
                                            "ns=1;i=7832",
                                            {
                                                "Definition": ("V", "ns=1;i=9142", {}),
                                                "EURange": ("V", "ns=1;i=9144", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9143",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9205",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9206",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9207",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "ResetStatistics": ("M", "ns=1;i=7833", {}),
                                        "StartTime": ("V", "ns=1;i=7834", {}),
                                        "Voltage": (
                                            "V",
                                            "ns=1;i=7835",
                                            {
                                                "Definition": ("V", "ns=1;i=9208", {}),
                                                "EURange": ("V", "ns=1;i=9270", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9209",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9271",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9272",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9273",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "Input": (
                                    "O",
                                    "ns=1;i=5143",
                                    {
                                        "ApparentPower": (
                                            "V",
                                            "ns=1;i=9616",
                                            {
                                                "Definition": ("V", "ns=1;i=9724", {}),
                                                "EURange": ("V", "ns=1;i=9726", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9725",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9727",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9728",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9734",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Current": (
                                            "V",
                                            "ns=1;i=9617",
                                            {
                                                "Definition": ("V", "ns=1;i=9735", {}),
                                                "EURange": ("V", "ns=1;i=9737", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9736",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9738",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9744",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9745",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Energy": (
                                            "V",
                                            "ns=1;i=9618",
                                            {
                                                "Definition": ("V", "ns=1;i=9746", {}),
                                                "EURange": ("V", "ns=1;i=9748", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9747",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9790",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9791",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Power": (
                                            "V",
                                            "ns=1;i=9619",
                                            {
                                                "Definition": ("V", "ns=1;i=9796", {}),
                                                "EURange": ("V", "ns=1;i=9802", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9801",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9803",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9804",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9805",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "ResetStatistics": ("M", "ns=1;i=9620", {}),
                                        "StartTime": ("V", "ns=1;i=9621", {}),
                                        "Voltage": (
                                            "V",
                                            "ns=1;i=9622",
                                            {
                                                "Definition": ("V", "ns=1;i=9806", {}),
                                                "EURange": ("V", "ns=1;i=9808", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=9807",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=9809",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=9810",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=9811",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "Output": (
                                    "O",
                                    "ns=1;i=5146",
                                    {
                                        "ApparentPower": (
                                            "V",
                                            "ns=1;i=9990",
                                            {
                                                "Definition": ("V", "ns=1;i=10155", {}),
                                                "EURange": ("V", "ns=1;i=10157", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10156",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10158",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10159",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10160",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Current": (
                                            "V",
                                            "ns=1;i=9991",
                                            {
                                                "Definition": ("V", "ns=1;i=10161", {}),
                                                "EURange": ("V", "ns=1;i=10163", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10162",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10164",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10165",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10166",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Energy": (
                                            "V",
                                            "ns=1;i=9992",
                                            {
                                                "Definition": ("V", "ns=1;i=10167", {}),
                                                "EURange": ("V", "ns=1;i=10169", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10168",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10170",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10171",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Power": (
                                            "V",
                                            "ns=1;i=9993",
                                            {
                                                "Definition": ("V", "ns=1;i=10172", {}),
                                                "EURange": ("V", "ns=1;i=10174", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10173",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10175",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10176",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10177",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "ResetStatistics": ("M", "ns=1;i=9994", {}),
                                        "StartTime": ("V", "ns=1;i=9995", {}),
                                        "Voltage": (
                                            "V",
                                            "ns=1;i=9996",
                                            {
                                                "Definition": ("V", "ns=1;i=10178", {}),
                                                "EURange": ("V", "ns=1;i=10180", {}),
                                                "EngineeringUnits": (
                                                    "V",
                                                    "ns=1;i=10179",
                                                    {},
                                                ),
                                                "InstrumentRange": (
                                                    "V",
                                                    "ns=1;i=10181",
                                                    {},
                                                ),
                                                "KindOfQuantity": (
                                                    "V",
                                                    "ns=1;i=10182",
                                                    {},
                                                ),
                                                "ValuePrecision": (
                                                    "V",
                                                    "ns=1;i=10183",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                            },
                        ),
                        "Events": (
                            "O",
                            "ns=1;i=5700",
                            {
                                "Service": (
                                    "O",
                                    "ns=1;i=5136",
                                    {
                                        "AckedState": (
                                            "V",
                                            "ns=1;i=8247",
                                            {
                                                "FalseState": ("V", "ns=1;i=8717", {}),
                                                "Id": ("V", "ns=1;i=8248", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=8718",
                                                    {},
                                                ),
                                                "TrueState": ("V", "ns=1;i=8719", {}),
                                            },
                                        ),
                                        "Acknowledge": (
                                            "M",
                                            "ns=1;i=8249",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=8250",
                                                    {},
                                                )
                                            },
                                        ),
                                        "ActiveState": (
                                            "V",
                                            "ns=1;i=8251",
                                            {
                                                "EffectiveDisplayName": (
                                                    "V",
                                                    "ns=1;i=8720",
                                                    {},
                                                ),
                                                "EffectiveTransitionTime": (
                                                    "V",
                                                    "ns=1;i=8721",
                                                    {},
                                                ),
                                                "FalseState": ("V", "ns=1;i=8722", {}),
                                                "Id": ("V", "ns=1;i=8252", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=8723",
                                                    {},
                                                ),
                                                "TrueState": ("V", "ns=1;i=8724", {}),
                                            },
                                        ),
                                        "AddComment": (
                                            "M",
                                            "ns=1;i=8253",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=8254",
                                                    {},
                                                )
                                            },
                                        ),
                                        "AudibleEnabled": ("V", "ns=1;i=8725", {}),
                                        "AudibleSound": ("V", "ns=1;i=8726", {}),
                                        "BranchId": ("V", "ns=1;i=8255", {}),
                                        "ClientUserId": ("V", "ns=1;i=8256", {}),
                                        "Comment": (
                                            "V",
                                            "ns=1;i=8257",
                                            {
                                                "SourceTimestamp": (
                                                    "V",
                                                    "ns=1;i=8258",
                                                    {},
                                                )
                                            },
                                        ),
                                        "ConditionClassId": ("V", "ns=1;i=8259", {}),
                                        "ConditionClassName": ("V", "ns=1;i=8260", {}),
                                        "ConditionName": ("V", "ns=1;i=8261", {}),
                                        "ConditionSubClassId": ("V", "ns=1;i=8727", {}),
                                        "ConditionSubClassName": (
                                            "V",
                                            "ns=1;i=8728",
                                            {},
                                        ),
                                        "Confirm": (
                                            "M",
                                            "ns=1;i=8729",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=8730",
                                                    {},
                                                )
                                            },
                                        ),
                                        "ConfirmedState": (
                                            "V",
                                            "ns=1;i=8731",
                                            {
                                                "FalseState": ("V", "ns=1;i=8732", {}),
                                                "Id": ("V", "ns=1;i=8733", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=8734",
                                                    {},
                                                ),
                                                "TrueState": ("V", "ns=1;i=8735", {}),
                                            },
                                        ),
                                        "Disable": ("M", "ns=1;i=8262", {}),
                                        "Enable": ("M", "ns=1;i=8263", {}),
                                        "EnabledState": (
                                            "V",
                                            "ns=1;i=8264",
                                            {
                                                "EffectiveDisplayName": (
                                                    "V",
                                                    "ns=1;i=8736",
                                                    {},
                                                ),
                                                "EffectiveTransitionTime": (
                                                    "V",
                                                    "ns=1;i=8737",
                                                    {},
                                                ),
                                                "FalseState": ("V", "ns=1;i=8738", {}),
                                                "Id": ("V", "ns=1;i=8265", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=8739",
                                                    {},
                                                ),
                                                "TrueState": ("V", "ns=1;i=8740", {}),
                                            },
                                        ),
                                        "EventId": ("V", "ns=1;i=8266", {}),
                                        "EventType": ("V", "ns=1;i=8267", {}),
                                        "FirstInGroup": ("O", "ns=1;i=5167", {}),
                                        "FirstInGroupFlag": ("V", "ns=1;i=8741", {}),
                                        "InputNode": ("V", "ns=1;i=8268", {}),
                                        "LastSeverity": (
                                            "V",
                                            "ns=1;i=8269",
                                            {
                                                "SourceTimestamp": (
                                                    "V",
                                                    "ns=1;i=8270",
                                                    {},
                                                )
                                            },
                                        ),
                                        "LatchedState": (
                                            "V",
                                            "ns=1;i=8742",
                                            {
                                                "FalseState": ("V", "ns=1;i=8743", {}),
                                                "Id": ("V", "ns=1;i=8744", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=8745",
                                                    {},
                                                ),
                                                "TrueState": ("V", "ns=1;i=8746", {}),
                                            },
                                        ),
                                        "LocalTime": ("V", "ns=1;i=8747", {}),
                                        "MaxTimeShelved": ("V", "ns=1;i=8748", {}),
                                        "Message": ("V", "ns=1;i=8271", {}),
                                        "NormalState": ("V", "ns=1;i=8272", {}),
                                        "OffDelay": ("V", "ns=1;i=8749", {}),
                                        "OnDelay": ("V", "ns=1;i=8750", {}),
                                        "OutOfServiceState": (
                                            "V",
                                            "ns=1;i=8751",
                                            {
                                                "FalseState": ("V", "ns=1;i=8752", {}),
                                                "Id": ("V", "ns=1;i=8753", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=8754",
                                                    {},
                                                ),
                                                "TrueState": ("V", "ns=1;i=8755", {}),
                                            },
                                        ),
                                        "PlaceInService": ("M", "ns=1;i=8756", {}),
                                        "Quality": (
                                            "V",
                                            "ns=1;i=8273",
                                            {
                                                "SourceTimestamp": (
                                                    "V",
                                                    "ns=1;i=8274",
                                                    {},
                                                )
                                            },
                                        ),
                                        "ReAlarmRepeatCount": ("V", "ns=1;i=8757", {}),
                                        "ReAlarmTime": ("V", "ns=1;i=8758", {}),
                                        "ReceiveTime": ("V", "ns=1;i=8275", {}),
                                        "RemoveFromService": ("M", "ns=1;i=8759", {}),
                                        "Reset": ("M", "ns=1;i=8760", {}),
                                        "Retain": ("V", "ns=1;i=8276", {}),
                                        "Severity": ("V", "ns=1;i=8277", {}),
                                        "ShelvingState": (
                                            "O",
                                            "ns=1;i=5168",
                                            {
                                                "CurrentState": (
                                                    "V",
                                                    "ns=1;i=8761",
                                                    {"Id": ("V", "ns=1;i=8762", {})},
                                                ),
                                                "LastTransition": (
                                                    "V",
                                                    "ns=1;i=8763",
                                                    {
                                                        "Id": ("V", "ns=1;i=8764", {}),
                                                        "TransitionTime": (
                                                            "V",
                                                            "ns=1;i=8765",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "OneShotShelve": (
                                                    "M",
                                                    "ns=1;i=8766",
                                                    {},
                                                ),
                                                "TimedShelve": (
                                                    "M",
                                                    "ns=1;i=8767",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=1;i=8768",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "Unshelve": ("M", "ns=1;i=8769", {}),
                                                "UnshelveTime": (
                                                    "V",
                                                    "ns=1;i=8770",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Silence": ("M", "ns=1;i=8771", {}),
                                        "SilenceState": (
                                            "V",
                                            "ns=1;i=8772",
                                            {
                                                "FalseState": ("V", "ns=1;i=8773", {}),
                                                "Id": ("V", "ns=1;i=8774", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=8775",
                                                    {},
                                                ),
                                                "TrueState": ("V", "ns=1;i=8776", {}),
                                            },
                                        ),
                                        "SourceName": ("V", "ns=1;i=8278", {}),
                                        "SourceNode": ("V", "ns=1;i=8279", {}),
                                        "Suppress": ("M", "ns=1;i=8777", {}),
                                        "SuppressedOrShelved": ("V", "ns=1;i=8280", {}),
                                        "SuppressedState": (
                                            "V",
                                            "ns=1;i=8778",
                                            {
                                                "FalseState": ("V", "ns=1;i=8779", {}),
                                                "Id": ("V", "ns=1;i=8780", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=8781",
                                                    {},
                                                ),
                                                "TrueState": ("V", "ns=1;i=8782", {}),
                                            },
                                        ),
                                        "Time": ("V", "ns=1;i=8281", {}),
                                        "Unsuppress": ("M", "ns=1;i=8783", {}),
                                    },
                                ),
                                "UIElement": ("V", "ns=1;i=8065", {}),
                                "Warning": (
                                    "O",
                                    "ns=1;i=5144",
                                    {
                                        "AckedState": (
                                            "V",
                                            "ns=1;i=8321",
                                            {
                                                "FalseState": ("V", "ns=1;i=8856", {}),
                                                "Id": ("V", "ns=1;i=8322", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=8857",
                                                    {},
                                                ),
                                                "TrueState": ("V", "ns=1;i=8858", {}),
                                            },
                                        ),
                                        "Acknowledge": (
                                            "M",
                                            "ns=1;i=8323",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=8324",
                                                    {},
                                                )
                                            },
                                        ),
                                        "ActiveState": (
                                            "V",
                                            "ns=1;i=8325",
                                            {
                                                "EffectiveDisplayName": (
                                                    "V",
                                                    "ns=1;i=8859",
                                                    {},
                                                ),
                                                "EffectiveTransitionTime": (
                                                    "V",
                                                    "ns=1;i=8860",
                                                    {},
                                                ),
                                                "FalseState": ("V", "ns=1;i=8861", {}),
                                                "Id": ("V", "ns=1;i=8326", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=8862",
                                                    {},
                                                ),
                                                "TrueState": ("V", "ns=1;i=8863", {}),
                                            },
                                        ),
                                        "AddComment": (
                                            "M",
                                            "ns=1;i=8327",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=8328",
                                                    {},
                                                )
                                            },
                                        ),
                                        "AudibleEnabled": ("V", "ns=1;i=8864", {}),
                                        "AudibleSound": ("V", "ns=1;i=8865", {}),
                                        "BranchId": ("V", "ns=1;i=8329", {}),
                                        "ClientUserId": ("V", "ns=1;i=8330", {}),
                                        "Comment": (
                                            "V",
                                            "ns=1;i=8331",
                                            {
                                                "SourceTimestamp": (
                                                    "V",
                                                    "ns=1;i=8332",
                                                    {},
                                                )
                                            },
                                        ),
                                        "ConditionClassId": ("V", "ns=1;i=8333", {}),
                                        "ConditionClassName": ("V", "ns=1;i=8334", {}),
                                        "ConditionName": ("V", "ns=1;i=8336", {}),
                                        "ConditionSubClassId": ("V", "ns=1;i=8866", {}),
                                        "ConditionSubClassName": (
                                            "V",
                                            "ns=1;i=8867",
                                            {},
                                        ),
                                        "Confirm": (
                                            "M",
                                            "ns=1;i=8868",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=8869",
                                                    {},
                                                )
                                            },
                                        ),
                                        "ConfirmedState": (
                                            "V",
                                            "ns=1;i=8870",
                                            {
                                                "FalseState": ("V", "ns=1;i=8871", {}),
                                                "Id": ("V", "ns=1;i=8872", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=8873",
                                                    {},
                                                ),
                                                "TrueState": ("V", "ns=1;i=8874", {}),
                                            },
                                        ),
                                        "Disable": ("M", "ns=1;i=8337", {}),
                                        "Enable": ("M", "ns=1;i=8339", {}),
                                        "EnabledState": (
                                            "V",
                                            "ns=1;i=8340",
                                            {
                                                "EffectiveDisplayName": (
                                                    "V",
                                                    "ns=1;i=8875",
                                                    {},
                                                ),
                                                "EffectiveTransitionTime": (
                                                    "V",
                                                    "ns=1;i=8876",
                                                    {},
                                                ),
                                                "FalseState": ("V", "ns=1;i=8877", {}),
                                                "Id": ("V", "ns=1;i=8341", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=8878",
                                                    {},
                                                ),
                                                "TrueState": ("V", "ns=1;i=8879", {}),
                                            },
                                        ),
                                        "EventId": ("V", "ns=1;i=8342", {}),
                                        "EventType": ("V", "ns=1;i=8343", {}),
                                        "FirstInGroup": ("O", "ns=1;i=5173", {}),
                                        "FirstInGroupFlag": ("V", "ns=1;i=8880", {}),
                                        "InputNode": ("V", "ns=1;i=8344", {}),
                                        "LastSeverity": (
                                            "V",
                                            "ns=1;i=8345",
                                            {
                                                "SourceTimestamp": (
                                                    "V",
                                                    "ns=1;i=8346",
                                                    {},
                                                )
                                            },
                                        ),
                                        "LatchedState": (
                                            "V",
                                            "ns=1;i=8881",
                                            {
                                                "FalseState": ("V", "ns=1;i=8882", {}),
                                                "Id": ("V", "ns=1;i=8883", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=8884",
                                                    {},
                                                ),
                                                "TrueState": ("V", "ns=1;i=8885", {}),
                                            },
                                        ),
                                        "LocalTime": ("V", "ns=1;i=8886", {}),
                                        "MaxTimeShelved": ("V", "ns=1;i=8887", {}),
                                        "Message": ("V", "ns=1;i=8347", {}),
                                        "NormalState": ("V", "ns=1;i=8348", {}),
                                        "OffDelay": ("V", "ns=1;i=8888", {}),
                                        "OnDelay": ("V", "ns=1;i=8889", {}),
                                        "OutOfServiceState": (
                                            "V",
                                            "ns=1;i=8890",
                                            {
                                                "FalseState": ("V", "ns=1;i=8891", {}),
                                                "Id": ("V", "ns=1;i=8892", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=8893",
                                                    {},
                                                ),
                                                "TrueState": ("V", "ns=1;i=8894", {}),
                                            },
                                        ),
                                        "PlaceInService": ("M", "ns=1;i=8895", {}),
                                        "Quality": (
                                            "V",
                                            "ns=1;i=8349",
                                            {
                                                "SourceTimestamp": (
                                                    "V",
                                                    "ns=1;i=8350",
                                                    {},
                                                )
                                            },
                                        ),
                                        "ReAlarmRepeatCount": ("V", "ns=1;i=8896", {}),
                                        "ReAlarmTime": ("V", "ns=1;i=8897", {}),
                                        "ReceiveTime": ("V", "ns=1;i=8351", {}),
                                        "RemoveFromService": ("M", "ns=1;i=8898", {}),
                                        "Reset": ("M", "ns=1;i=8899", {}),
                                        "Retain": ("V", "ns=1;i=8352", {}),
                                        "Severity": ("V", "ns=1;i=8353", {}),
                                        "ShelvingState": (
                                            "O",
                                            "ns=1;i=5174",
                                            {
                                                "CurrentState": (
                                                    "V",
                                                    "ns=1;i=8900",
                                                    {"Id": ("V", "ns=1;i=8901", {})},
                                                ),
                                                "LastTransition": (
                                                    "V",
                                                    "ns=1;i=8902",
                                                    {
                                                        "Id": ("V", "ns=1;i=8903", {}),
                                                        "TransitionTime": (
                                                            "V",
                                                            "ns=1;i=8904",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "OneShotShelve": (
                                                    "M",
                                                    "ns=1;i=8905",
                                                    {},
                                                ),
                                                "TimedShelve": (
                                                    "M",
                                                    "ns=1;i=8906",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=1;i=8907",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "Unshelve": ("M", "ns=1;i=8908", {}),
                                                "UnshelveTime": (
                                                    "V",
                                                    "ns=1;i=8909",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Silence": ("M", "ns=1;i=8910", {}),
                                        "SilenceState": (
                                            "V",
                                            "ns=1;i=8911",
                                            {
                                                "FalseState": ("V", "ns=1;i=8912", {}),
                                                "Id": ("V", "ns=1;i=8913", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=8914",
                                                    {},
                                                ),
                                                "TrueState": ("V", "ns=1;i=8915", {}),
                                            },
                                        ),
                                        "SourceName": ("V", "ns=1;i=8354", {}),
                                        "SourceNode": ("V", "ns=1;i=8355", {}),
                                        "Suppress": ("M", "ns=1;i=8916", {}),
                                        "SuppressedOrShelved": ("V", "ns=1;i=8356", {}),
                                        "SuppressedState": (
                                            "V",
                                            "ns=1;i=8917",
                                            {
                                                "FalseState": ("V", "ns=1;i=8918", {}),
                                                "Id": ("V", "ns=1;i=8919", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=8920",
                                                    {},
                                                ),
                                                "TrueState": ("V", "ns=1;i=8921", {}),
                                            },
                                        ),
                                        "Time": ("V", "ns=1;i=8365", {}),
                                        "Unsuppress": ("M", "ns=1;i=8922", {}),
                                    },
                                ),
                            },
                        ),
                        "Identification": (
                            "O",
                            "ns=1;i=5081",
                            {
                                "AssetId": ("V", "ns=1;i=7659", {}),
                                "ComponentName": ("V", "ns=1;i=7871", {}),
                                "DeviceClass": ("V", "ns=1;i=7872", {}),
                                "DeviceRevision": ("V", "ns=1;i=7873", {}),
                                "HardwareRevision": ("V", "ns=1;i=7874", {}),
                                "InitialOperationDate": ("V", "ns=1;i=7875", {}),
                                "Manufacturer": ("V", "ns=1;i=6287", {}),
                                "ManufacturerUri": ("V", "ns=1;i=7876", {}),
                                "Model": ("V", "ns=1;i=7877", {}),
                                "MonthOfConstruction": ("V", "ns=1;i=7878", {}),
                                "ProductCode": ("V", "ns=1;i=7879", {}),
                                "ProductInstanceUri": ("V", "ns=1;i=7880", {}),
                                "SerialNumber": ("V", "ns=1;i=6297", {}),
                                "SoftwareRevision": ("V", "ns=1;i=7881", {}),
                                "UIElement": ("V", "ns=1;i=7882", {}),
                                "YearOfConstruction": ("V", "ns=1;i=7883", {}),
                            },
                        ),
                        "Operational": (
                            "O",
                            "ns=1;i=5704",
                            {
                                "OperatingState": (
                                    "V",
                                    "ns=1;i=8493",
                                    {
                                        "Definition": ("V", "ns=1;i=8515", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8516", {}),
                                    },
                                ),
                                "UIElement": ("V", "ns=1;i=8494", {}),
                            },
                        ),
                        "Statistics": (
                            "O",
                            "ns=1;i=5703",
                            {
                                "RealTime": (
                                    "V",
                                    "ns=1;i=8523",
                                    {
                                        "Definition": ("V", "ns=1;i=8596", {}),
                                        "EURange": ("V", "ns=1;i=8611", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8597", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8612", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8613", {}),
                                    },
                                ),
                                "RealTimeToNextService": (
                                    "V",
                                    "ns=1;i=10665",
                                    {
                                        "Definition": ("V", "ns=1;i=10666", {}),
                                        "EURange": ("V", "ns=1;i=10668", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10667", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10669", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10675", {}),
                                    },
                                ),
                                "ResetCondition": ("V", "ns=1;i=8524", {}),
                                "ResetStatistics": ("M", "ns=1;i=8538", {}),
                                "RunningTime": (
                                    "V",
                                    "ns=1;i=8539",
                                    {
                                        "Definition": ("V", "ns=1;i=8614", {}),
                                        "EURange": ("V", "ns=1;i=8616", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8615", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8617", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8618", {}),
                                    },
                                ),
                                "RunningTimeToNextService": (
                                    "V",
                                    "ns=1;i=10688",
                                    {
                                        "Definition": ("V", "ns=1;i=10689", {}),
                                        "EURange": ("V", "ns=1;i=10693", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10690", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10694", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10706", {}),
                                    },
                                ),
                                "StartTime": ("V", "ns=1;i=8540", {}),
                                "UIElement": ("V", "ns=1;i=8585", {}),
                            },
                        ),
                    },
                ),
            },
        ),
        "CalibrationType": (
            "OT",
            "ns=1;i=1054",
            {
                "LastCalibrationDate": (
                    "V",
                    "ns=1;i=6715",
                    {"Definition": ("V", "ns=1;i=6718", {})},
                ),
                "NextCalibrationDate": (
                    "V",
                    "ns=1;i=6716",
                    {"Definition": ("V", "ns=1;i=6719", {})},
                ),
            },
        ),
        "CommunicationSettingsType": (
            "OT",
            "ns=1;i=1048",
            {
                "DefaultGateway": ("V", "ns=1;i=10520", {}),
                "Dhcp": (
                    "V",
                    "ns=1;i=11298",
                    {
                        "Definition": ("V", "ns=1;i=11302", {}),
                        "FalseState": ("V", "ns=1;i=11299", {}),
                        "TrueState": ("V", "ns=1;i=11300", {}),
                    },
                ),
                "DnsServer": ("V", "ns=1;i=10521", {}),
                "DomainName": ("V", "ns=1;i=6324", {}),
                "Hostname": ("V", "ns=1;i=6325", {}),
                "IpAddress": ("V", "ns=1;i=6326", {}),
                "IpVersion": ("V", "ns=1;i=10527", {}),
                "MacAddress": ("V", "ns=1;i=6460", {}),
                "SubnetMask": ("V", "ns=1;i=10528", {}),
            },
        ),
        "ComponentsGroupType": (
            "OT",
            "ns=1;i=1047",
            {
                "<ComponentsGroup>": ("O", "ns=1;i=5187", {}),
                "ChargingSystems": ("O", "ns=1;i=5012", {}),
                "Compressors": ("O", "ns=1;i=5011", {}),
                "CondensateDrains": ("O", "ns=1;i=5014", {}),
                "CondensateSeparators": ("O", "ns=1;i=5016", {}),
                "Converters": ("O", "ns=1;i=5023", {}),
                "CoolingSystems": ("O", "ns=1;i=5024", {}),
                "Dryers": ("O", "ns=1;i=5028", {}),
                "Filters": ("O", "ns=1;i=5091", {}),
                "HeatRecoverySystems": ("O", "ns=1;i=5188", {}),
                "Receivers": ("O", "ns=1;i=5190", {}),
                "Sensors": ("O", "ns=1;i=5191", {}),
                "Valves": ("O", "ns=1;i=5192", {}),
            },
        ),
        "ConfigurationType": (
            "OT",
            "ns=1;i=1037",
            {
                "AirnetConfigurationType": (
                    "OT",
                    "ns=1;i=1016",
                    {
                        "OperatingModes": (
                            "V",
                            "ns=1;i=6255",
                            {"EnumStrings": ("V", "ns=1;i=6257", {})},
                        ),
                        "OperatingProfiles": (
                            "V",
                            "ns=1;i=6260",
                            {"EnumStrings": ("V", "ns=1;i=6261", {})},
                        ),
                    },
                ),
                "MCSConfigurationType": (
                    "OT",
                    "ns=1;i=1019",
                    {
                        "CommunicationSettings": (
                            "O",
                            "ns=1;i=5026",
                            {
                                "DefaultGateway": ("V", "ns=1;i=11303", {}),
                                "Dhcp": (
                                    "V",
                                    "ns=1;i=11304",
                                    {
                                        "Definition": ("V", "ns=1;i=11327", {}),
                                        "FalseState": ("V", "ns=1;i=11305", {}),
                                        "TrueState": ("V", "ns=1;i=11306", {}),
                                    },
                                ),
                                "DnsServer": ("V", "ns=1;i=11307", {}),
                                "DomainName": ("V", "ns=1;i=6246", {}),
                                "Hostname": ("V", "ns=1;i=6247", {}),
                                "IpAddress": ("V", "ns=1;i=6117", {}),
                                "IpVersion": ("V", "ns=1;i=11308", {}),
                                "SubnetMask": ("V", "ns=1;i=11310", {}),
                            },
                        ),
                        "ConfigurationFile": (
                            "O",
                            "ns=1;i=5025",
                            {
                                "Close": (
                                    "M",
                                    "ns=1;i=9768",
                                    {"InputArguments": ("V", "ns=1;i=6323", {})},
                                ),
                                "GetPosition": (
                                    "M",
                                    "ns=1;i=9769",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6332", {}),
                                        "OutputArguments": ("V", "ns=1;i=9770", {}),
                                    },
                                ),
                                "MimeType": ("V", "ns=1;i=6327", {}),
                                "Open": (
                                    "M",
                                    "ns=1;i=9771",
                                    {
                                        "InputArguments": ("V", "ns=1;i=9772", {}),
                                        "OutputArguments": ("V", "ns=1;i=9773", {}),
                                    },
                                ),
                                "OpenCount": ("V", "ns=1;i=9774", {}),
                                "Read": (
                                    "M",
                                    "ns=1;i=9775",
                                    {
                                        "InputArguments": ("V", "ns=1;i=9776", {}),
                                        "OutputArguments": ("V", "ns=1;i=9777", {}),
                                    },
                                ),
                                "SetPosition": (
                                    "M",
                                    "ns=1;i=9778",
                                    {"InputArguments": ("V", "ns=1;i=9779", {})},
                                ),
                                "Size": ("V", "ns=1;i=9780", {}),
                                "UserWritable": ("V", "ns=1;i=9781", {}),
                                "Writable": ("V", "ns=1;i=9782", {}),
                                "Write": (
                                    "M",
                                    "ns=1;i=9783",
                                    {"InputArguments": ("V", "ns=1;i=9784", {})},
                                ),
                            },
                        ),
                        "LoadConfigurationFile": ("M", "ns=1;i=9785", {}),
                        "SaveConfigurationFile": ("M", "ns=1;i=10123", {}),
                    },
                ),
            },
        ),
        "DesignType": (
            "OT",
            "ns=1;i=1044",
            {
                "ComponentClass": (
                    "V",
                    "ns=1;i=6273",
                    {"Definition": ("V", "ns=1;i=6282", {})},
                ),
                "CompressorDesignType": (
                    "OT",
                    "ns=1;i=1008",
                    {
                        "ComponentClass": (
                            "V",
                            "ns=1;i=6071",
                            {"Definition": ("V", "ns=1;i=6092", {})},
                        ),
                        "DisplacementType": (
                            "V",
                            "ns=1;i=6316",
                            {"Definition": ("V", "ns=1;i=6336", {})},
                        ),
                        "LubricationType": (
                            "V",
                            "ns=1;i=6317",
                            {"Definition": ("V", "ns=1;i=6337", {})},
                        ),
                        "NumberOfStages": (
                            "V",
                            "ns=1;i=6318",
                            {"Definition": ("V", "ns=1;i=6338", {})},
                        ),
                        "VariableFlow": (
                            "V",
                            "ns=1;i=6319",
                            {
                                "Definition": ("V", "ns=1;i=6339", {}),
                                "FalseState": ("V", "ns=1;i=6320", {}),
                                "TrueState": ("V", "ns=1;i=6329", {}),
                            },
                        ),
                    },
                ),
                "ConverterDesignType": (
                    "OT",
                    "ns=1;i=1041",
                    {
                        "ComponentClass": (
                            "V",
                            "ns=1;i=6642",
                            {"Definition": ("V", "ns=1;i=6643", {})},
                        )
                    },
                ),
                "DrainDesignType": (
                    "OT",
                    "ns=1;i=1036",
                    {
                        "ComponentClass": (
                            "V",
                            "ns=1;i=6632",
                            {"Definition": ("V", "ns=1;i=6636", {})},
                        )
                    },
                ),
                "DryerDesignType": (
                    "OT",
                    "ns=1;i=1033",
                    {
                        "ComponentClass": (
                            "V",
                            "ns=1;i=6624",
                            {"Definition": ("V", "ns=1;i=6626", {})},
                        ),
                        "LowestAmbientTemperature": (
                            "V",
                            "ns=1;i=6625",
                            {
                                "Definition": ("V", "ns=1;i=6627", {}),
                                "EURange": ("V", "ns=1;i=6628", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6631", {}),
                            },
                        ),
                    },
                ),
                "FilterDesignType": (
                    "OT",
                    "ns=1;i=1009",
                    {
                        "ComponentClass": (
                            "V",
                            "ns=1;i=6599",
                            {"Definition": ("V", "ns=1;i=6600", {})},
                        ),
                        "FilterClass": (
                            "V",
                            "ns=1;i=6589",
                            {"Definition": ("V", "ns=1;i=6601", {})},
                        ),
                    },
                ),
                "ReceiverDesignType": (
                    "OT",
                    "ns=1;i=1023",
                    {
                        "ComponentClass": (
                            "V",
                            "ns=1;i=6603",
                            {"Definition": ("V", "ns=1;i=6604", {})},
                        ),
                        "Volume": (
                            "V",
                            "ns=1;i=7890",
                            {
                                "Definition": ("V", "ns=1;i=10633", {}),
                                "EURange": ("V", "ns=1;i=10634", {}),
                                "EngineeringUnits": ("V", "ns=1;i=10632", {}),
                                "InstrumentRange": ("V", "ns=1;i=10635", {}),
                                "ValuePrecision": ("V", "ns=1;i=10636", {}),
                            },
                        ),
                    },
                ),
                "SensorDesignType": (
                    "OT",
                    "ns=1;i=1031",
                    {
                        "ComponentClass": (
                            "V",
                            "ns=1;i=6614",
                            {"Definition": ("V", "ns=1;i=6617", {})},
                        ),
                        "SensorTechnology": (
                            "V",
                            "ns=1;i=6615",
                            {"Definition": ("V", "ns=1;i=6618", {})},
                        ),
                        "SoftSensor": (
                            "V",
                            "ns=1;i=6616",
                            {
                                "Definition": ("V", "ns=1;i=7165", {}),
                                "FalseState": ("V", "ns=1;i=6619", {}),
                                "TrueState": ("V", "ns=1;i=6691", {}),
                            },
                        ),
                    },
                ),
                "SeparatorDesignType": (
                    "OT",
                    "ns=1;i=1040",
                    {
                        "ComponentClass": (
                            "V",
                            "ns=1;i=6638",
                            {"Definition": ("V", "ns=1;i=6640", {})},
                        )
                    },
                ),
                "ValveDesignType": (
                    "OT",
                    "ns=1;i=1032",
                    {
                        "ComponentClass": (
                            "V",
                            "ns=1;i=6620",
                            {"Definition": ("V", "ns=1;i=6622", {})},
                        ),
                        "NumberOfPorts": (
                            "V",
                            "ns=1;i=6621",
                            {"Definition": ("V", "ns=1;i=6623", {})},
                        ),
                    },
                ),
            },
        ),
        "ElectricalCircuitType": (
            "OT",
            "ns=1;i=1014",
            {
                "<Other>": (
                    "O",
                    "ns=1;i=5060",
                    {
                        "ApparentPower": (
                            "V",
                            "ns=1;i=6174",
                            {
                                "Definition": ("V", "ns=1;i=6184", {}),
                                "EURange": ("V", "ns=1;i=6185", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6186", {}),
                                "InstrumentRange": ("V", "ns=1;i=6215", {}),
                                "KindOfQuantity": ("V", "ns=1;i=6236", {}),
                                "ValuePrecision": ("V", "ns=1;i=6237", {}),
                            },
                        ),
                        "Current": (
                            "V",
                            "ns=1;i=6175",
                            {
                                "Definition": ("V", "ns=1;i=6238", {}),
                                "EURange": ("V", "ns=1;i=6239", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6240", {}),
                                "InstrumentRange": ("V", "ns=1;i=6241", {}),
                                "KindOfQuantity": ("V", "ns=1;i=6242", {}),
                                "ValuePrecision": ("V", "ns=1;i=6243", {}),
                            },
                        ),
                        "Energy": (
                            "V",
                            "ns=1;i=6176",
                            {
                                "Definition": ("V", "ns=1;i=6244", {}),
                                "EURange": ("V", "ns=1;i=6245", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6248", {}),
                                "InstrumentRange": ("V", "ns=1;i=6249", {}),
                                "ValuePrecision": ("V", "ns=1;i=6252", {}),
                            },
                        ),
                        "Power": (
                            "V",
                            "ns=1;i=6177",
                            {
                                "Definition": ("V", "ns=1;i=6253", {}),
                                "EURange": ("V", "ns=1;i=6275", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6276", {}),
                                "InstrumentRange": ("V", "ns=1;i=6277", {}),
                                "KindOfQuantity": ("V", "ns=1;i=6278", {}),
                                "ValuePrecision": ("V", "ns=1;i=6279", {}),
                            },
                        ),
                        "ResetStatistics": ("M", "ns=1;i=7815", {}),
                        "StartTime": ("V", "ns=1;i=6179", {}),
                        "Voltage": (
                            "V",
                            "ns=1;i=6183",
                            {
                                "Definition": ("V", "ns=1;i=6280", {}),
                                "EURange": ("V", "ns=1;i=6304", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6305", {}),
                                "InstrumentRange": ("V", "ns=1;i=6306", {}),
                                "KindOfQuantity": ("V", "ns=1;i=6650", {}),
                                "ValuePrecision": ("V", "ns=1;i=6652", {}),
                            },
                        ),
                    },
                ),
                "Delta": (
                    "O",
                    "ns=1;i=5108",
                    {
                        "ApparentPower": (
                            "V",
                            "ns=1;i=6661",
                            {
                                "Definition": ("V", "ns=1;i=7843", {}),
                                "EURange": ("V", "ns=1;i=7844", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7845", {}),
                                "InstrumentRange": ("V", "ns=1;i=7846", {}),
                                "KindOfQuantity": ("V", "ns=1;i=7847", {}),
                                "ValuePrecision": ("V", "ns=1;i=7848", {}),
                            },
                        ),
                        "Current": (
                            "V",
                            "ns=1;i=6662",
                            {
                                "Definition": ("V", "ns=1;i=7849", {}),
                                "EURange": ("V", "ns=1;i=7850", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7851", {}),
                                "InstrumentRange": ("V", "ns=1;i=7852", {}),
                                "KindOfQuantity": ("V", "ns=1;i=7853", {}),
                                "ValuePrecision": ("V", "ns=1;i=7854", {}),
                            },
                        ),
                        "Energy": (
                            "V",
                            "ns=1;i=6672",
                            {
                                "Definition": ("V", "ns=1;i=7855", {}),
                                "EURange": ("V", "ns=1;i=7856", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7857", {}),
                                "InstrumentRange": ("V", "ns=1;i=7858", {}),
                                "ValuePrecision": ("V", "ns=1;i=7859", {}),
                            },
                        ),
                        "Power": (
                            "V",
                            "ns=1;i=6673",
                            {
                                "Definition": ("V", "ns=1;i=7860", {}),
                                "EURange": ("V", "ns=1;i=7861", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7862", {}),
                                "InstrumentRange": ("V", "ns=1;i=7863", {}),
                                "KindOfQuantity": ("V", "ns=1;i=7892", {}),
                                "ValuePrecision": ("V", "ns=1;i=7893", {}),
                            },
                        ),
                        "ResetStatistics": ("M", "ns=1;i=7816", {}),
                        "StartTime": ("V", "ns=1;i=6674", {}),
                        "Voltage": (
                            "V",
                            "ns=1;i=6680",
                            {
                                "Definition": ("V", "ns=1;i=7894", {}),
                                "EURange": ("V", "ns=1;i=7895", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7896", {}),
                                "InstrumentRange": ("V", "ns=1;i=7897", {}),
                                "KindOfQuantity": ("V", "ns=1;i=7898", {}),
                                "ValuePrecision": ("V", "ns=1;i=7899", {}),
                            },
                        ),
                    },
                ),
                "Input": (
                    "O",
                    "ns=1;i=5066",
                    {
                        "ApparentPower": (
                            "V",
                            "ns=1;i=9595",
                            {
                                "Definition": ("V", "ns=1;i=9630", {}),
                                "EURange": ("V", "ns=1;i=9631", {}),
                                "EngineeringUnits": ("V", "ns=1;i=9632", {}),
                                "InstrumentRange": ("V", "ns=1;i=9633", {}),
                                "KindOfQuantity": ("V", "ns=1;i=9634", {}),
                                "ValuePrecision": ("V", "ns=1;i=9635", {}),
                            },
                        ),
                        "Current": (
                            "V",
                            "ns=1;i=9596",
                            {
                                "Definition": ("V", "ns=1;i=9636", {}),
                                "EURange": ("V", "ns=1;i=9637", {}),
                                "EngineeringUnits": ("V", "ns=1;i=9638", {}),
                                "InstrumentRange": ("V", "ns=1;i=9639", {}),
                                "KindOfQuantity": ("V", "ns=1;i=9640", {}),
                                "ValuePrecision": ("V", "ns=1;i=9641", {}),
                            },
                        ),
                        "Energy": (
                            "V",
                            "ns=1;i=9597",
                            {
                                "Definition": ("V", "ns=1;i=9642", {}),
                                "EURange": ("V", "ns=1;i=9643", {}),
                                "EngineeringUnits": ("V", "ns=1;i=9644", {}),
                                "InstrumentRange": ("V", "ns=1;i=9645", {}),
                                "ValuePrecision": ("V", "ns=1;i=9646", {}),
                            },
                        ),
                        "Power": (
                            "V",
                            "ns=1;i=9598",
                            {
                                "Definition": ("V", "ns=1;i=9647", {}),
                                "EURange": ("V", "ns=1;i=9648", {}),
                                "EngineeringUnits": ("V", "ns=1;i=9649", {}),
                                "InstrumentRange": ("V", "ns=1;i=9650", {}),
                                "KindOfQuantity": ("V", "ns=1;i=9651", {}),
                                "ValuePrecision": ("V", "ns=1;i=9652", {}),
                            },
                        ),
                        "ResetStatistics": ("M", "ns=1;i=9599", {}),
                        "StartTime": ("V", "ns=1;i=9600", {}),
                        "Voltage": (
                            "V",
                            "ns=1;i=9601",
                            {
                                "Definition": ("V", "ns=1;i=9653", {}),
                                "EURange": ("V", "ns=1;i=9654", {}),
                                "EngineeringUnits": ("V", "ns=1;i=9655", {}),
                                "InstrumentRange": ("V", "ns=1;i=9656", {}),
                                "KindOfQuantity": ("V", "ns=1;i=9657", {}),
                                "ValuePrecision": ("V", "ns=1;i=9658", {}),
                            },
                        ),
                    },
                ),
                "Output": (
                    "O",
                    "ns=1;i=5067",
                    {
                        "ApparentPower": (
                            "V",
                            "ns=1;i=9969",
                            {
                                "Definition": ("V", "ns=1;i=10004", {}),
                                "EURange": ("V", "ns=1;i=10005", {}),
                                "EngineeringUnits": ("V", "ns=1;i=10006", {}),
                                "InstrumentRange": ("V", "ns=1;i=10007", {}),
                                "KindOfQuantity": ("V", "ns=1;i=10008", {}),
                                "ValuePrecision": ("V", "ns=1;i=10009", {}),
                            },
                        ),
                        "Current": (
                            "V",
                            "ns=1;i=9970",
                            {
                                "Definition": ("V", "ns=1;i=10010", {}),
                                "EURange": ("V", "ns=1;i=10011", {}),
                                "EngineeringUnits": ("V", "ns=1;i=10012", {}),
                                "InstrumentRange": ("V", "ns=1;i=10013", {}),
                                "KindOfQuantity": ("V", "ns=1;i=10014", {}),
                                "ValuePrecision": ("V", "ns=1;i=10015", {}),
                            },
                        ),
                        "Energy": (
                            "V",
                            "ns=1;i=9971",
                            {
                                "Definition": ("V", "ns=1;i=10016", {}),
                                "EURange": ("V", "ns=1;i=10017", {}),
                                "EngineeringUnits": ("V", "ns=1;i=10018", {}),
                                "InstrumentRange": ("V", "ns=1;i=10019", {}),
                                "ValuePrecision": ("V", "ns=1;i=10020", {}),
                            },
                        ),
                        "Power": (
                            "V",
                            "ns=1;i=9972",
                            {
                                "Definition": ("V", "ns=1;i=10021", {}),
                                "EURange": ("V", "ns=1;i=10022", {}),
                                "EngineeringUnits": ("V", "ns=1;i=10023", {}),
                                "InstrumentRange": ("V", "ns=1;i=10024", {}),
                                "KindOfQuantity": ("V", "ns=1;i=10025", {}),
                                "ValuePrecision": ("V", "ns=1;i=10026", {}),
                            },
                        ),
                        "ResetStatistics": ("M", "ns=1;i=9973", {}),
                        "StartTime": ("V", "ns=1;i=9974", {}),
                        "Voltage": (
                            "V",
                            "ns=1;i=9975",
                            {
                                "Definition": ("V", "ns=1;i=10027", {}),
                                "EURange": ("V", "ns=1;i=10028", {}),
                                "EngineeringUnits": ("V", "ns=1;i=10029", {}),
                                "InstrumentRange": ("V", "ns=1;i=10030", {}),
                                "KindOfQuantity": ("V", "ns=1;i=10031", {}),
                                "ValuePrecision": ("V", "ns=1;i=10032", {}),
                            },
                        ),
                    },
                ),
            },
        ),
        "ElectricalQuantitiesType": (
            "OT",
            "ns=1;i=1011",
            {
                "ApparentPower": (
                    "V",
                    "ns=1;i=6440",
                    {
                        "Definition": ("V", "ns=1;i=6114", {}),
                        "EURange": ("V", "ns=1;i=6115", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6140", {}),
                        "InstrumentRange": ("V", "ns=1;i=6141", {}),
                        "KindOfQuantity": ("V", "ns=1;i=6149", {}),
                        "ValuePrecision": ("V", "ns=1;i=6142", {}),
                    },
                ),
                "Current": (
                    "V",
                    "ns=1;i=6093",
                    {
                        "Definition": ("V", "ns=1;i=6143", {}),
                        "EURange": ("V", "ns=1;i=6144", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6145", {}),
                        "InstrumentRange": ("V", "ns=1;i=6146", {}),
                        "KindOfQuantity": ("V", "ns=1;i=6148", {}),
                        "ValuePrecision": ("V", "ns=1;i=6147", {}),
                    },
                ),
                "Energy": (
                    "V",
                    "ns=1;i=6094",
                    {
                        "Definition": ("V", "ns=1;i=6150", {}),
                        "EURange": ("V", "ns=1;i=6151", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6152", {}),
                        "InstrumentRange": ("V", "ns=1;i=6153", {}),
                        "ValuePrecision": ("V", "ns=1;i=6154", {}),
                    },
                ),
                "Power": (
                    "V",
                    "ns=1;i=6099",
                    {
                        "Definition": ("V", "ns=1;i=6155", {}),
                        "EURange": ("V", "ns=1;i=6156", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6157", {}),
                        "InstrumentRange": ("V", "ns=1;i=6158", {}),
                        "KindOfQuantity": ("V", "ns=1;i=6163", {}),
                        "ValuePrecision": ("V", "ns=1;i=6162", {}),
                    },
                ),
                "ResetStatistics": ("M", "ns=1;i=7814", {}),
                "StartTime": ("V", "ns=1;i=6113", {}),
                "Voltage": (
                    "V",
                    "ns=1;i=6112",
                    {
                        "Definition": ("V", "ns=1;i=6164", {}),
                        "EURange": ("V", "ns=1;i=6165", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6166", {}),
                        "InstrumentRange": ("V", "ns=1;i=6167", {}),
                        "KindOfQuantity": ("V", "ns=1;i=6173", {}),
                        "ValuePrecision": ("V", "ns=1;i=6168", {}),
                    },
                ),
            },
        ),
        "EventsType": (
            "OT",
            "ns=1;i=1020",
            {
                "<Event>": (
                    "O",
                    "ns=1;i=5080",
                    {
                        "AddComment": (
                            "M",
                            "ns=1;i=7036",
                            {"InputArguments": ("V", "ns=1;i=6288", {})},
                        ),
                        "BranchId": ("V", "ns=1;i=6289", {}),
                        "ClientUserId": ("V", "ns=1;i=6290", {}),
                        "Comment": (
                            "V",
                            "ns=1;i=6291",
                            {"SourceTimestamp": ("V", "ns=1;i=6342", {})},
                        ),
                        "ConditionClassId": ("V", "ns=1;i=6343", {}),
                        "ConditionClassName": ("V", "ns=1;i=6344", {}),
                        "ConditionName": ("V", "ns=1;i=6357", {}),
                        "ConditionSubClassId": ("V", "ns=1;i=6395", {}),
                        "ConditionSubClassName": ("V", "ns=1;i=6400", {}),
                        "Disable": ("M", "ns=1;i=7037", {}),
                        "Enable": ("M", "ns=1;i=7038", {}),
                        "EnabledState": (
                            "V",
                            "ns=1;i=6358",
                            {
                                "EffectiveDisplayName": ("V", "ns=1;i=6377", {}),
                                "EffectiveTransitionTime": ("V", "ns=1;i=6378", {}),
                                "FalseState": ("V", "ns=1;i=6379", {}),
                                "Id": ("V", "ns=1;i=6359", {}),
                                "TransitionTime": ("V", "ns=1;i=6393", {}),
                                "TrueState": ("V", "ns=1;i=6394", {}),
                            },
                        ),
                        "EventId": ("V", "ns=1;i=6806", {}),
                        "EventType": ("V", "ns=1;i=6807", {}),
                        "LastSeverity": (
                            "V",
                            "ns=1;i=6801",
                            {"SourceTimestamp": ("V", "ns=1;i=6802", {})},
                        ),
                        "LocalTime": ("V", "ns=1;i=6402", {}),
                        "Message": ("V", "ns=1;i=6808", {}),
                        "Quality": (
                            "V",
                            "ns=1;i=6803",
                            {"SourceTimestamp": ("V", "ns=1;i=6804", {})},
                        ),
                        "ReceiveTime": ("V", "ns=1;i=6809", {}),
                        "Retain": ("V", "ns=1;i=6805", {}),
                        "Severity": ("V", "ns=1;i=6810", {}),
                        "SourceName": ("V", "ns=1;i=6811", {}),
                        "SourceNode": ("V", "ns=1;i=6812", {}),
                        "Time": ("V", "ns=1;i=6813", {}),
                    },
                ),
                "EmergencyStop": (
                    "O",
                    "ns=1;i=5082",
                    {
                        "AckedState": (
                            "V",
                            "ns=1;i=6818",
                            {
                                "FalseState": ("V", "ns=1;i=6403", {}),
                                "Id": ("V", "ns=1;i=6819", {}),
                                "TransitionTime": ("V", "ns=1;i=6404", {}),
                                "TrueState": ("V", "ns=1;i=6405", {}),
                            },
                        ),
                        "Acknowledge": (
                            "M",
                            "ns=1;i=7039",
                            {"InputArguments": ("V", "ns=1;i=6820", {})},
                        ),
                        "ActiveState": (
                            "V",
                            "ns=1;i=6369",
                            {
                                "EffectiveDisplayName": ("V", "ns=1;i=6406", {}),
                                "EffectiveTransitionTime": ("V", "ns=1;i=6407", {}),
                                "FalseState": ("V", "ns=1;i=6408", {}),
                                "Id": ("V", "ns=1;i=6370", {}),
                                "TransitionTime": ("V", "ns=1;i=6409", {}),
                                "TrueState": ("V", "ns=1;i=6410", {}),
                            },
                        ),
                        "AddComment": (
                            "M",
                            "ns=1;i=7040",
                            {"InputArguments": ("V", "ns=1;i=6821", {})},
                        ),
                        "AudibleEnabled": ("V", "ns=1;i=6416", {}),
                        "AudibleSound": ("V", "ns=1;i=6417", {}),
                        "BranchId": ("V", "ns=1;i=6822", {}),
                        "ClientUserId": ("V", "ns=1;i=6823", {}),
                        "Comment": (
                            "V",
                            "ns=1;i=6824",
                            {"SourceTimestamp": ("V", "ns=1;i=6825", {})},
                        ),
                        "ConditionClassId": ("V", "ns=1;i=6826", {}),
                        "ConditionClassName": ("V", "ns=1;i=6827", {}),
                        "ConditionName": ("V", "ns=1;i=6828", {}),
                        "ConditionSubClassId": ("V", "ns=1;i=6418", {}),
                        "ConditionSubClassName": ("V", "ns=1;i=6419", {}),
                        "Confirm": (
                            "M",
                            "ns=1;i=7001",
                            {"InputArguments": ("V", "ns=1;i=6421", {})},
                        ),
                        "ConfirmedState": (
                            "V",
                            "ns=1;i=6433",
                            {
                                "FalseState": ("V", "ns=1;i=6485", {}),
                                "Id": ("V", "ns=1;i=6434", {}),
                                "TransitionTime": ("V", "ns=1;i=6486", {}),
                                "TrueState": ("V", "ns=1;i=6487", {}),
                            },
                        ),
                        "Disable": ("M", "ns=1;i=7041", {}),
                        "Enable": ("M", "ns=1;i=7042", {}),
                        "EnabledState": (
                            "V",
                            "ns=1;i=6814",
                            {
                                "EffectiveDisplayName": ("V", "ns=1;i=6411", {}),
                                "EffectiveTransitionTime": ("V", "ns=1;i=6412", {}),
                                "FalseState": ("V", "ns=1;i=6413", {}),
                                "Id": ("V", "ns=1;i=6815", {}),
                                "TransitionTime": ("V", "ns=1;i=6414", {}),
                                "TrueState": ("V", "ns=1;i=6415", {}),
                            },
                        ),
                        "EventId": ("V", "ns=1;i=6834", {}),
                        "EventType": ("V", "ns=1;i=6835", {}),
                        "FirstInGroup": ("O", "ns=1;i=5074", {}),
                        "FirstInGroupFlag": ("V", "ns=1;i=6437", {}),
                        "InputNode": ("V", "ns=1;i=6816", {}),
                        "LastSeverity": (
                            "V",
                            "ns=1;i=6829",
                            {"SourceTimestamp": ("V", "ns=1;i=6830", {})},
                        ),
                        "LatchedState": (
                            "V",
                            "ns=1;i=6443",
                            {
                                "FalseState": ("V", "ns=1;i=6488", {}),
                                "Id": ("V", "ns=1;i=6450", {}),
                                "TransitionTime": ("V", "ns=1;i=6489", {}),
                                "TrueState": ("V", "ns=1;i=6490", {}),
                            },
                        ),
                        "LocalTime": ("V", "ns=1;i=6451", {}),
                        "MaxTimeShelved": ("V", "ns=1;i=6465", {}),
                        "Message": ("V", "ns=1;i=6836", {}),
                        "NormalState": ("V", "ns=1;i=6368", {}),
                        "OffDelay": ("V", "ns=1;i=6466", {}),
                        "OnDelay": ("V", "ns=1;i=6467", {}),
                        "OutOfServiceState": (
                            "V",
                            "ns=1;i=6468",
                            {
                                "FalseState": ("V", "ns=1;i=6491", {}),
                                "Id": ("V", "ns=1;i=6470", {}),
                                "TransitionTime": ("V", "ns=1;i=6492", {}),
                                "TrueState": ("V", "ns=1;i=6493", {}),
                            },
                        ),
                        "PlaceInService": ("M", "ns=1;i=7002", {}),
                        "Quality": (
                            "V",
                            "ns=1;i=6831",
                            {"SourceTimestamp": ("V", "ns=1;i=6832", {})},
                        ),
                        "ReAlarmRepeatCount": ("V", "ns=1;i=6471", {}),
                        "ReAlarmTime": ("V", "ns=1;i=6472", {}),
                        "ReceiveTime": ("V", "ns=1;i=6837", {}),
                        "RemoveFromService": ("M", "ns=1;i=7003", {}),
                        "Reset": ("M", "ns=1;i=7004", {}),
                        "Retain": ("V", "ns=1;i=6833", {}),
                        "Severity": ("V", "ns=1;i=6838", {}),
                        "ShelvingState": (
                            "O",
                            "ns=1;i=5075",
                            {
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=6473",
                                    {"Id": ("V", "ns=1;i=6474", {})},
                                ),
                                "LastTransition": (
                                    "V",
                                    "ns=1;i=6494",
                                    {
                                        "Id": ("V", "ns=1;i=6495", {}),
                                        "TransitionTime": ("V", "ns=1;i=6496", {}),
                                    },
                                ),
                                "OneShotShelve": ("M", "ns=1;i=7005", {}),
                                "TimedShelve": (
                                    "M",
                                    "ns=1;i=7006",
                                    {"InputArguments": ("V", "ns=1;i=6475", {})},
                                ),
                                "Unshelve": ("M", "ns=1;i=7014", {}),
                                "UnshelveTime": ("V", "ns=1;i=6480", {}),
                            },
                        ),
                        "Silence": ("M", "ns=1;i=7015", {}),
                        "SilenceState": (
                            "V",
                            "ns=1;i=6481",
                            {
                                "FalseState": ("V", "ns=1;i=6497", {}),
                                "Id": ("V", "ns=1;i=6482", {}),
                                "TransitionTime": ("V", "ns=1;i=6498", {}),
                                "TrueState": ("V", "ns=1;i=6499", {}),
                            },
                        ),
                        "SourceName": ("V", "ns=1;i=6839", {}),
                        "SourceNode": ("V", "ns=1;i=6840", {}),
                        "Suppress": ("M", "ns=1;i=7016", {}),
                        "SuppressedOrShelved": ("V", "ns=1;i=6817", {}),
                        "SuppressedState": (
                            "V",
                            "ns=1;i=6483",
                            {
                                "FalseState": ("V", "ns=1;i=6500", {}),
                                "Id": ("V", "ns=1;i=6484", {}),
                                "TransitionTime": ("V", "ns=1;i=6501", {}),
                                "TrueState": ("V", "ns=1;i=6502", {}),
                            },
                        ),
                        "Time": ("V", "ns=1;i=6841", {}),
                        "Unsuppress": ("M", "ns=1;i=7017", {}),
                    },
                ),
                "Service": (
                    "O",
                    "ns=1;i=5083",
                    {
                        "AckedState": (
                            "V",
                            "ns=1;i=6843",
                            {
                                "FalseState": ("V", "ns=1;i=6503", {}),
                                "Id": ("V", "ns=1;i=6844", {}),
                                "TransitionTime": ("V", "ns=1;i=6504", {}),
                                "TrueState": ("V", "ns=1;i=6505", {}),
                            },
                        ),
                        "Acknowledge": (
                            "M",
                            "ns=1;i=7043",
                            {"InputArguments": ("V", "ns=1;i=6845", {})},
                        ),
                        "ActiveState": (
                            "V",
                            "ns=1;i=6346",
                            {
                                "EffectiveDisplayName": ("V", "ns=1;i=6510", {}),
                                "EffectiveTransitionTime": ("V", "ns=1;i=6511", {}),
                                "FalseState": ("V", "ns=1;i=6512", {}),
                                "Id": ("V", "ns=1;i=6347", {}),
                                "TransitionTime": ("V", "ns=1;i=6523", {}),
                                "TrueState": ("V", "ns=1;i=6524", {}),
                            },
                        ),
                        "AddComment": (
                            "M",
                            "ns=1;i=7044",
                            {"InputArguments": ("V", "ns=1;i=6846", {})},
                        ),
                        "AudibleEnabled": ("V", "ns=1;i=6536", {}),
                        "AudibleSound": ("V", "ns=1;i=6538", {}),
                        "BranchId": ("V", "ns=1;i=6847", {}),
                        "ClientUserId": ("V", "ns=1;i=6848", {}),
                        "Comment": (
                            "V",
                            "ns=1;i=6849",
                            {"SourceTimestamp": ("V", "ns=1;i=6850", {})},
                        ),
                        "ConditionClassId": ("V", "ns=1;i=6851", {}),
                        "ConditionClassName": ("V", "ns=1;i=6852", {}),
                        "ConditionName": ("V", "ns=1;i=6853", {}),
                        "ConditionSubClassId": ("V", "ns=1;i=6550", {}),
                        "ConditionSubClassName": ("V", "ns=1;i=6551", {}),
                        "Confirm": (
                            "M",
                            "ns=1;i=7018",
                            {"InputArguments": ("V", "ns=1;i=6552", {})},
                        ),
                        "ConfirmedState": (
                            "V",
                            "ns=1;i=6553",
                            {
                                "FalseState": ("V", "ns=1;i=6592", {}),
                                "Id": ("V", "ns=1;i=6554", {}),
                                "TransitionTime": ("V", "ns=1;i=6593", {}),
                                "TrueState": ("V", "ns=1;i=6594", {}),
                            },
                        ),
                        "Disable": ("M", "ns=1;i=7045", {}),
                        "Enable": ("M", "ns=1;i=7046", {}),
                        "EnabledState": (
                            "V",
                            "ns=1;i=6351",
                            {
                                "EffectiveDisplayName": ("V", "ns=1;i=6525", {}),
                                "EffectiveTransitionTime": ("V", "ns=1;i=6526", {}),
                                "FalseState": ("V", "ns=1;i=6527", {}),
                                "Id": ("V", "ns=1;i=6352", {}),
                                "TransitionTime": ("V", "ns=1;i=6528", {}),
                                "TrueState": ("V", "ns=1;i=6534", {}),
                            },
                        ),
                        "EventId": ("V", "ns=1;i=6859", {}),
                        "EventType": ("V", "ns=1;i=6860", {}),
                        "FirstInGroup": ("O", "ns=1;i=5076", {}),
                        "FirstInGroupFlag": ("V", "ns=1;i=6555", {}),
                        "InputNode": ("V", "ns=1;i=6353", {}),
                        "LastSeverity": (
                            "V",
                            "ns=1;i=6854",
                            {"SourceTimestamp": ("V", "ns=1;i=6855", {})},
                        ),
                        "LatchedState": (
                            "V",
                            "ns=1;i=6556",
                            {
                                "FalseState": ("V", "ns=1;i=6595", {}),
                                "Id": ("V", "ns=1;i=6557", {}),
                                "TransitionTime": ("V", "ns=1;i=6596", {}),
                                "TrueState": ("V", "ns=1;i=6597", {}),
                            },
                        ),
                        "LocalTime": ("V", "ns=1;i=6558", {}),
                        "MaxTimeShelved": ("V", "ns=1;i=6559", {}),
                        "Message": ("V", "ns=1;i=6861", {}),
                        "NormalState": ("V", "ns=1;i=6345", {}),
                        "OffDelay": ("V", "ns=1;i=6561", {}),
                        "OnDelay": ("V", "ns=1;i=6562", {}),
                        "OutOfServiceState": (
                            "V",
                            "ns=1;i=6566",
                            {
                                "FalseState": ("V", "ns=1;i=6598", {}),
                                "Id": ("V", "ns=1;i=6576", {}),
                                "TransitionTime": ("V", "ns=1;i=6602", {}),
                                "TrueState": ("V", "ns=1;i=6605", {}),
                            },
                        ),
                        "PlaceInService": ("M", "ns=1;i=7019", {}),
                        "Quality": (
                            "V",
                            "ns=1;i=6856",
                            {"SourceTimestamp": ("V", "ns=1;i=6857", {})},
                        ),
                        "ReAlarmRepeatCount": ("V", "ns=1;i=6580", {}),
                        "ReAlarmTime": ("V", "ns=1;i=6581", {}),
                        "ReceiveTime": ("V", "ns=1;i=6862", {}),
                        "RemoveFromService": ("M", "ns=1;i=7020", {}),
                        "Reset": ("M", "ns=1;i=7021", {}),
                        "Retain": ("V", "ns=1;i=6858", {}),
                        "Severity": ("V", "ns=1;i=6863", {}),
                        "ShelvingState": (
                            "O",
                            "ns=1;i=5077",
                            {
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=6582",
                                    {"Id": ("V", "ns=1;i=6583", {})},
                                ),
                                "LastTransition": (
                                    "V",
                                    "ns=1;i=6606",
                                    {
                                        "Id": ("V", "ns=1;i=6607", {}),
                                        "TransitionTime": ("V", "ns=1;i=6608", {}),
                                    },
                                ),
                                "OneShotShelve": ("M", "ns=1;i=7022", {}),
                                "TimedShelve": (
                                    "M",
                                    "ns=1;i=7023",
                                    {"InputArguments": ("V", "ns=1;i=6584", {})},
                                ),
                                "Unshelve": ("M", "ns=1;i=7024", {}),
                                "UnshelveTime": ("V", "ns=1;i=6585", {}),
                            },
                        ),
                        "Silence": ("M", "ns=1;i=7025", {}),
                        "SilenceState": (
                            "V",
                            "ns=1;i=6586",
                            {
                                "FalseState": ("V", "ns=1;i=6609", {}),
                                "Id": ("V", "ns=1;i=6588", {}),
                                "TransitionTime": ("V", "ns=1;i=6610", {}),
                                "TrueState": ("V", "ns=1;i=6611", {}),
                            },
                        ),
                        "SourceName": ("V", "ns=1;i=6864", {}),
                        "SourceNode": ("V", "ns=1;i=6865", {}),
                        "Suppress": ("M", "ns=1;i=7026", {}),
                        "SuppressedOrShelved": ("V", "ns=1;i=6842", {}),
                        "SuppressedState": (
                            "V",
                            "ns=1;i=6590",
                            {
                                "FalseState": ("V", "ns=1;i=6612", {}),
                                "Id": ("V", "ns=1;i=6591", {}),
                                "TransitionTime": ("V", "ns=1;i=6613", {}),
                                "TrueState": ("V", "ns=1;i=6633", {}),
                            },
                        ),
                        "Time": ("V", "ns=1;i=6866", {}),
                        "Unsuppress": ("M", "ns=1;i=7027", {}),
                    },
                ),
                "Shutdown": (
                    "O",
                    "ns=1;i=5084",
                    {
                        "AckedState": (
                            "V",
                            "ns=1;i=6871",
                            {
                                "FalseState": ("V", "ns=1;i=6637", {}),
                                "Id": ("V", "ns=1;i=6872", {}),
                                "TransitionTime": ("V", "ns=1;i=6639", {}),
                                "TrueState": ("V", "ns=1;i=6641", {}),
                            },
                        ),
                        "Acknowledge": (
                            "M",
                            "ns=1;i=7013",
                            {"InputArguments": ("V", "ns=1;i=6873", {})},
                        ),
                        "ActiveState": (
                            "V",
                            "ns=1;i=6366",
                            {
                                "EffectiveDisplayName": ("V", "ns=1;i=6664", {}),
                                "EffectiveTransitionTime": ("V", "ns=1;i=6665", {}),
                                "FalseState": ("V", "ns=1;i=6685", {}),
                                "Id": ("V", "ns=1;i=6367", {}),
                                "TransitionTime": ("V", "ns=1;i=6686", {}),
                                "TrueState": ("V", "ns=1;i=6687", {}),
                            },
                        ),
                        "AddComment": (
                            "M",
                            "ns=1;i=7047",
                            {"InputArguments": ("V", "ns=1;i=6874", {})},
                        ),
                        "AudibleEnabled": ("V", "ns=1;i=6711", {}),
                        "AudibleSound": ("V", "ns=1;i=6721", {}),
                        "BranchId": ("V", "ns=1;i=6875", {}),
                        "ClientUserId": ("V", "ns=1;i=6876", {}),
                        "Comment": (
                            "V",
                            "ns=1;i=6877",
                            {"SourceTimestamp": ("V", "ns=1;i=6878", {})},
                        ),
                        "ConditionClassId": ("V", "ns=1;i=6879", {}),
                        "ConditionClassName": ("V", "ns=1;i=6880", {}),
                        "ConditionName": ("V", "ns=1;i=6881", {}),
                        "ConditionSubClassId": ("V", "ns=1;i=6723", {}),
                        "ConditionSubClassName": ("V", "ns=1;i=6724", {}),
                        "Confirm": (
                            "M",
                            "ns=1;i=7028",
                            {"InputArguments": ("V", "ns=1;i=6725", {})},
                        ),
                        "ConfirmedState": (
                            "V",
                            "ns=1;i=6726",
                            {
                                "FalseState": ("V", "ns=1;i=6747", {}),
                                "Id": ("V", "ns=1;i=6727", {}),
                                "TransitionTime": ("V", "ns=1;i=6748", {}),
                                "TrueState": ("V", "ns=1;i=6749", {}),
                            },
                        ),
                        "Disable": ("M", "ns=1;i=7048", {}),
                        "Enable": ("M", "ns=1;i=7049", {}),
                        "EnabledState": (
                            "V",
                            "ns=1;i=6867",
                            {
                                "EffectiveDisplayName": ("V", "ns=1;i=6703", {}),
                                "EffectiveTransitionTime": ("V", "ns=1;i=6704", {}),
                                "FalseState": ("V", "ns=1;i=6705", {}),
                                "Id": ("V", "ns=1;i=6868", {}),
                                "TransitionTime": ("V", "ns=1;i=6709", {}),
                                "TrueState": ("V", "ns=1;i=6710", {}),
                            },
                        ),
                        "EventId": ("V", "ns=1;i=6887", {}),
                        "EventType": ("V", "ns=1;i=6888", {}),
                        "FirstInGroup": ("O", "ns=1;i=5078", {}),
                        "FirstInGroupFlag": ("V", "ns=1;i=6728", {}),
                        "InputNode": ("V", "ns=1;i=6869", {}),
                        "LastSeverity": (
                            "V",
                            "ns=1;i=6882",
                            {"SourceTimestamp": ("V", "ns=1;i=6883", {})},
                        ),
                        "LatchedState": (
                            "V",
                            "ns=1;i=6729",
                            {
                                "FalseState": ("V", "ns=1;i=6750", {}),
                                "Id": ("V", "ns=1;i=6730", {}),
                                "TransitionTime": ("V", "ns=1;i=6751", {}),
                                "TrueState": ("V", "ns=1;i=6752", {}),
                            },
                        ),
                        "LocalTime": ("V", "ns=1;i=6731", {}),
                        "MaxTimeShelved": ("V", "ns=1;i=6732", {}),
                        "Message": ("V", "ns=1;i=6889", {}),
                        "NormalState": ("V", "ns=1;i=6365", {}),
                        "OffDelay": ("V", "ns=1;i=6733", {}),
                        "OnDelay": ("V", "ns=1;i=6734", {}),
                        "OutOfServiceState": (
                            "V",
                            "ns=1;i=6735",
                            {
                                "FalseState": ("V", "ns=1;i=6753", {}),
                                "Id": ("V", "ns=1;i=6736", {}),
                                "TransitionTime": ("V", "ns=1;i=6754", {}),
                                "TrueState": ("V", "ns=1;i=6755", {}),
                            },
                        ),
                        "PlaceInService": ("M", "ns=1;i=7029", {}),
                        "Quality": (
                            "V",
                            "ns=1;i=6884",
                            {"SourceTimestamp": ("V", "ns=1;i=6885", {})},
                        ),
                        "ReAlarmRepeatCount": ("V", "ns=1;i=6737", {}),
                        "ReAlarmTime": ("V", "ns=1;i=6738", {}),
                        "ReceiveTime": ("V", "ns=1;i=6890", {}),
                        "RemoveFromService": ("M", "ns=1;i=7030", {}),
                        "Reset": ("M", "ns=1;i=7031", {}),
                        "Retain": ("V", "ns=1;i=6886", {}),
                        "Severity": ("V", "ns=1;i=6891", {}),
                        "ShelvingState": (
                            "O",
                            "ns=1;i=5079",
                            {
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=6739",
                                    {"Id": ("V", "ns=1;i=6740", {})},
                                ),
                                "LastTransition": (
                                    "V",
                                    "ns=1;i=6756",
                                    {
                                        "Id": ("V", "ns=1;i=6757", {}),
                                        "TransitionTime": ("V", "ns=1;i=6758", {}),
                                    },
                                ),
                                "OneShotShelve": ("M", "ns=1;i=7032", {}),
                                "TimedShelve": (
                                    "M",
                                    "ns=1;i=7033",
                                    {"InputArguments": ("V", "ns=1;i=6741", {})},
                                ),
                                "Unshelve": ("M", "ns=1;i=7034", {}),
                                "UnshelveTime": ("V", "ns=1;i=6742", {}),
                            },
                        ),
                        "Silence": ("M", "ns=1;i=7035", {}),
                        "SilenceState": (
                            "V",
                            "ns=1;i=6743",
                            {
                                "FalseState": ("V", "ns=1;i=6759", {}),
                                "Id": ("V", "ns=1;i=6744", {}),
                                "TransitionTime": ("V", "ns=1;i=6760", {}),
                                "TrueState": ("V", "ns=1;i=6761", {}),
                            },
                        ),
                        "SourceName": ("V", "ns=1;i=6892", {}),
                        "SourceNode": ("V", "ns=1;i=6893", {}),
                        "Suppress": ("M", "ns=1;i=7072", {}),
                        "SuppressedOrShelved": ("V", "ns=1;i=6870", {}),
                        "SuppressedState": (
                            "V",
                            "ns=1;i=6745",
                            {
                                "FalseState": ("V", "ns=1;i=6762", {}),
                                "Id": ("V", "ns=1;i=6746", {}),
                                "TransitionTime": ("V", "ns=1;i=6763", {}),
                                "TrueState": ("V", "ns=1;i=6764", {}),
                            },
                        ),
                        "Time": ("V", "ns=1;i=6894", {}),
                        "Unsuppress": ("M", "ns=1;i=7073", {}),
                    },
                ),
                "Warning": (
                    "O",
                    "ns=1;i=5085",
                    {
                        "AckedState": (
                            "V",
                            "ns=1;i=6896",
                            {
                                "FalseState": ("V", "ns=1;i=6765", {}),
                                "Id": ("V", "ns=1;i=6897", {}),
                                "TransitionTime": ("V", "ns=1;i=6766", {}),
                                "TrueState": ("V", "ns=1;i=6767", {}),
                            },
                        ),
                        "Acknowledge": (
                            "M",
                            "ns=1;i=7050",
                            {"InputArguments": ("V", "ns=1;i=6898", {})},
                        ),
                        "ActiveState": (
                            "V",
                            "ns=1;i=6349",
                            {
                                "EffectiveDisplayName": ("V", "ns=1;i=6768", {}),
                                "EffectiveTransitionTime": ("V", "ns=1;i=6772", {}),
                                "FalseState": ("V", "ns=1;i=6773", {}),
                                "Id": ("V", "ns=1;i=6350", {}),
                                "TransitionTime": ("V", "ns=1;i=6774", {}),
                                "TrueState": ("V", "ns=1;i=6775", {}),
                            },
                        ),
                        "AddComment": (
                            "M",
                            "ns=1;i=7051",
                            {"InputArguments": ("V", "ns=1;i=6899", {})},
                        ),
                        "AudibleEnabled": ("V", "ns=1;i=6781", {}),
                        "AudibleSound": ("V", "ns=1;i=6782", {}),
                        "BranchId": ("V", "ns=1;i=6900", {}),
                        "ClientUserId": ("V", "ns=1;i=6901", {}),
                        "Comment": (
                            "V",
                            "ns=1;i=6902",
                            {"SourceTimestamp": ("V", "ns=1;i=6903", {})},
                        ),
                        "ConditionClassId": ("V", "ns=1;i=6904", {}),
                        "ConditionClassName": ("V", "ns=1;i=6905", {}),
                        "ConditionName": ("V", "ns=1;i=6906", {}),
                        "ConditionSubClassId": ("V", "ns=1;i=6783", {}),
                        "ConditionSubClassName": ("V", "ns=1;i=6784", {}),
                        "Confirm": (
                            "M",
                            "ns=1;i=7074",
                            {"InputArguments": ("V", "ns=1;i=6785", {})},
                        ),
                        "ConfirmedState": (
                            "V",
                            "ns=1;i=6786",
                            {
                                "FalseState": ("V", "ns=1;i=6994", {}),
                                "Id": ("V", "ns=1;i=6787", {}),
                                "TransitionTime": ("V", "ns=1;i=6995", {}),
                                "TrueState": ("V", "ns=1;i=6996", {}),
                            },
                        ),
                        "Disable": ("M", "ns=1;i=7054", {}),
                        "Enable": ("M", "ns=1;i=7056", {}),
                        "EnabledState": (
                            "V",
                            "ns=1;i=6354",
                            {
                                "EffectiveDisplayName": ("V", "ns=1;i=6776", {}),
                                "EffectiveTransitionTime": ("V", "ns=1;i=6777", {}),
                                "FalseState": ("V", "ns=1;i=6778", {}),
                                "Id": ("V", "ns=1;i=6355", {}),
                                "TransitionTime": ("V", "ns=1;i=6779", {}),
                                "TrueState": ("V", "ns=1;i=6780", {}),
                            },
                        ),
                        "EventId": ("V", "ns=1;i=6917", {}),
                        "EventType": ("V", "ns=1;i=6918", {}),
                        "FirstInGroup": ("O", "ns=1;i=5088", {}),
                        "FirstInGroupFlag": ("V", "ns=1;i=6788", {}),
                        "InputNode": ("V", "ns=1;i=6356", {}),
                        "LastSeverity": (
                            "V",
                            "ns=1;i=6912",
                            {"SourceTimestamp": ("V", "ns=1;i=6913", {})},
                        ),
                        "LatchedState": (
                            "V",
                            "ns=1;i=6789",
                            {
                                "FalseState": ("V", "ns=1;i=6997", {}),
                                "Id": ("V", "ns=1;i=6790", {}),
                                "TransitionTime": ("V", "ns=1;i=6998", {}),
                                "TrueState": ("V", "ns=1;i=6999", {}),
                            },
                        ),
                        "LocalTime": ("V", "ns=1;i=6791", {}),
                        "MaxTimeShelved": ("V", "ns=1;i=6792", {}),
                        "Message": ("V", "ns=1;i=6919", {}),
                        "NormalState": ("V", "ns=1;i=6348", {}),
                        "OffDelay": ("V", "ns=1;i=6793", {}),
                        "OnDelay": ("V", "ns=1;i=6794", {}),
                        "OutOfServiceState": (
                            "V",
                            "ns=1;i=6795",
                            {
                                "FalseState": ("V", "ns=1;i=7000", {}),
                                "Id": ("V", "ns=1;i=6796", {}),
                                "TransitionTime": ("V", "ns=1;i=7084", {}),
                                "TrueState": ("V", "ns=1;i=7085", {}),
                            },
                        ),
                        "PlaceInService": ("M", "ns=1;i=7075", {}),
                        "Quality": (
                            "V",
                            "ns=1;i=6914",
                            {"SourceTimestamp": ("V", "ns=1;i=6915", {})},
                        ),
                        "ReAlarmRepeatCount": ("V", "ns=1;i=6797", {}),
                        "ReAlarmTime": ("V", "ns=1;i=6798", {}),
                        "ReceiveTime": ("V", "ns=1;i=6920", {}),
                        "RemoveFromService": ("M", "ns=1;i=7076", {}),
                        "Reset": ("M", "ns=1;i=7077", {}),
                        "Retain": ("V", "ns=1;i=6916", {}),
                        "Severity": ("V", "ns=1;i=6921", {}),
                        "ShelvingState": (
                            "O",
                            "ns=1;i=5089",
                            {
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=6986",
                                    {"Id": ("V", "ns=1;i=6987", {})},
                                ),
                                "LastTransition": (
                                    "V",
                                    "ns=1;i=7086",
                                    {
                                        "Id": ("V", "ns=1;i=7087", {}),
                                        "TransitionTime": ("V", "ns=1;i=7088", {}),
                                    },
                                ),
                                "OneShotShelve": ("M", "ns=1;i=7078", {}),
                                "TimedShelve": (
                                    "M",
                                    "ns=1;i=7079",
                                    {"InputArguments": ("V", "ns=1;i=6988", {})},
                                ),
                                "Unshelve": ("M", "ns=1;i=7080", {}),
                                "UnshelveTime": ("V", "ns=1;i=6989", {}),
                            },
                        ),
                        "Silence": ("M", "ns=1;i=7081", {}),
                        "SilenceState": (
                            "V",
                            "ns=1;i=6990",
                            {
                                "FalseState": ("V", "ns=1;i=7089", {}),
                                "Id": ("V", "ns=1;i=6991", {}),
                                "TransitionTime": ("V", "ns=1;i=7090", {}),
                                "TrueState": ("V", "ns=1;i=7091", {}),
                            },
                        ),
                        "SourceName": ("V", "ns=1;i=6922", {}),
                        "SourceNode": ("V", "ns=1;i=6923", {}),
                        "Suppress": ("M", "ns=1;i=7082", {}),
                        "SuppressedOrShelved": ("V", "ns=1;i=6895", {}),
                        "SuppressedState": (
                            "V",
                            "ns=1;i=6992",
                            {
                                "FalseState": ("V", "ns=1;i=7092", {}),
                                "Id": ("V", "ns=1;i=6993", {}),
                                "TransitionTime": ("V", "ns=1;i=7093", {}),
                                "TrueState": ("V", "ns=1;i=7094", {}),
                            },
                        ),
                        "Time": ("V", "ns=1;i=6924", {}),
                        "Unsuppress": ("M", "ns=1;i=7083", {}),
                    },
                ),
            },
        ),
        "FluidCircuitType": (
            "OT",
            "ns=1;i=1013",
            {
                "<Other>": (
                    "O",
                    "ns=1;i=5179",
                    {
                        "AbsolutePressure": (
                            "V",
                            "ns=1;i=7339",
                            {
                                "Definition": ("V", "ns=1;i=7996", {}),
                                "EURange": ("V", "ns=1;i=7997", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7998", {}),
                                "InstrumentRange": ("V", "ns=1;i=7999", {}),
                                "KindOfQuantity": ("V", "ns=1;i=8002", {}),
                                "ValuePrecision": ("V", "ns=1;i=8003", {}),
                            },
                        ),
                        "AccumulatedVolume": (
                            "V",
                            "ns=1;i=7340",
                            {
                                "Definition": ("V", "ns=1;i=8004", {}),
                                "EURange": ("V", "ns=1;i=8005", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8006", {}),
                                "InstrumentRange": ("V", "ns=1;i=8007", {}),
                                "KindOfQuantity": ("V", "ns=1;i=8008", {}),
                                "ValuePrecision": ("V", "ns=1;i=8009", {}),
                            },
                        ),
                        "DewPoint": (
                            "V",
                            "ns=1;i=7341",
                            {
                                "Definition": ("V", "ns=1;i=8010", {}),
                                "EURange": ("V", "ns=1;i=8011", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8012", {}),
                                "InstrumentRange": ("V", "ns=1;i=8013", {}),
                                "KindOfQuantity": ("V", "ns=1;i=8014", {}),
                                "ValuePrecision": ("V", "ns=1;i=8016", {}),
                            },
                        ),
                        "GaugePressure": (
                            "V",
                            "ns=1;i=7342",
                            {
                                "Definition": ("V", "ns=1;i=8017", {}),
                                "EURange": ("V", "ns=1;i=8018", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8019", {}),
                                "InstrumentRange": ("V", "ns=1;i=8020", {}),
                                "KindOfQuantity": ("V", "ns=1;i=8022", {}),
                                "ValuePrecision": ("V", "ns=1;i=8023", {}),
                            },
                        ),
                        "MassFlowRate": (
                            "V",
                            "ns=1;i=7343",
                            {
                                "Definition": ("V", "ns=1;i=8024", {}),
                                "EURange": ("V", "ns=1;i=8025", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8026", {}),
                                "InstrumentRange": ("V", "ns=1;i=8027", {}),
                                "KindOfQuantity": ("V", "ns=1;i=8028", {}),
                                "ValuePrecision": ("V", "ns=1;i=8029", {}),
                            },
                        ),
                        "OilConcentration": (
                            "V",
                            "ns=1;i=7713",
                            {
                                "Definition": ("V", "ns=1;i=8241", {}),
                                "EURange": ("V", "ns=1;i=8242", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8243", {}),
                                "InstrumentRange": ("V", "ns=1;i=8244", {}),
                                "KindOfQuantity": ("V", "ns=1;i=8245", {}),
                                "ValuePrecision": ("V", "ns=1;i=8246", {}),
                            },
                        ),
                        "ParticlesPerSizeRange": (
                            "O",
                            "ns=1;i=5201",
                            {
                                "Fine": (
                                    "V",
                                    "ns=1;i=7263",
                                    {
                                        "Definition": ("V", "ns=1;i=8358", {}),
                                        "EURange": ("V", "ns=1;i=8360", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8359", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8361", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=8814", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8362", {}),
                                    },
                                ),
                                "Large": (
                                    "V",
                                    "ns=1;i=7277",
                                    {
                                        "Definition": ("V", "ns=1;i=9106", {}),
                                        "EURange": ("V", "ns=1;i=9108", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9107", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9176", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9177", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9178", {}),
                                    },
                                ),
                                "Medium": (
                                    "V",
                                    "ns=1;i=7278",
                                    {
                                        "Definition": ("V", "ns=1;i=10366", {}),
                                        "EURange": ("V", "ns=1;i=10368", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10367", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10369", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=10370", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10371", {}),
                                    },
                                ),
                            },
                        ),
                        "RelativeHumidity": (
                            "V",
                            "ns=1;i=7714",
                            {
                                "Definition": ("V", "ns=1;i=8282", {}),
                                "EURange": ("V", "ns=1;i=8298", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8299", {}),
                                "InstrumentRange": ("V", "ns=1;i=8300", {}),
                                "KindOfQuantity": ("V", "ns=1;i=8306", {}),
                                "ValuePrecision": ("V", "ns=1;i=8309", {}),
                            },
                        ),
                        "ResetStatistics": ("M", "ns=1;i=7715", {}),
                        "StartTime": ("V", "ns=1;i=7716", {}),
                        "Temperature": (
                            "V",
                            "ns=1;i=7717",
                            {
                                "Definition": ("V", "ns=1;i=8310", {}),
                                "EURange": ("V", "ns=1;i=8311", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8312", {}),
                                "InstrumentRange": ("V", "ns=1;i=8313", {}),
                                "KindOfQuantity": ("V", "ns=1;i=8314", {}),
                                "ValuePrecision": ("V", "ns=1;i=8315", {}),
                            },
                        ),
                        "Volume": (
                            "V",
                            "ns=1;i=7718",
                            {
                                "Definition": ("V", "ns=1;i=8316", {}),
                                "EURange": ("V", "ns=1;i=8317", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8318", {}),
                                "InstrumentRange": ("V", "ns=1;i=8319", {}),
                                "KindOfQuantity": ("V", "ns=1;i=8320", {}),
                                "ValuePrecision": ("V", "ns=1;i=8335", {}),
                            },
                        ),
                        "VolumeFlowRate": (
                            "V",
                            "ns=1;i=7719",
                            {
                                "Definition": ("V", "ns=1;i=8338", {}),
                                "EURange": ("V", "ns=1;i=8357", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8366", {}),
                                "InstrumentRange": ("V", "ns=1;i=8367", {}),
                                "KindOfQuantity": ("V", "ns=1;i=8368", {}),
                                "ValuePrecision": ("V", "ns=1;i=8369", {}),
                            },
                        ),
                    },
                ),
                "Delta": (
                    "O",
                    "ns=1;i=5202",
                    {
                        "AbsolutePressure": (
                            "V",
                            "ns=1;i=7811",
                            {
                                "Definition": ("V", "ns=1;i=7865", {}),
                                "EURange": ("V", "ns=1;i=7866", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7867", {}),
                                "InstrumentRange": ("V", "ns=1;i=7891", {}),
                                "KindOfQuantity": ("V", "ns=1;i=7943", {}),
                                "ValuePrecision": ("V", "ns=1;i=7944", {}),
                            },
                        ),
                        "AccumulatedVolume": (
                            "V",
                            "ns=1;i=6574",
                            {
                                "Definition": ("V", "ns=1;i=7190", {}),
                                "EURange": ("V", "ns=1;i=7191", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7192", {}),
                                "InstrumentRange": ("V", "ns=1;i=7193", {}),
                                "KindOfQuantity": ("V", "ns=1;i=7194", {}),
                                "ValuePrecision": ("V", "ns=1;i=7195", {}),
                            },
                        ),
                        "DewPoint": (
                            "V",
                            "ns=1;i=6575",
                            {
                                "Definition": ("V", "ns=1;i=7196", {}),
                                "EURange": ("V", "ns=1;i=7197", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7198", {}),
                                "InstrumentRange": ("V", "ns=1;i=7199", {}),
                                "KindOfQuantity": ("V", "ns=1;i=7200", {}),
                                "ValuePrecision": ("V", "ns=1;i=7201", {}),
                            },
                        ),
                        "GaugePressure": (
                            "V",
                            "ns=1;i=6577",
                            {
                                "Definition": ("V", "ns=1;i=7202", {}),
                                "EURange": ("V", "ns=1;i=7203", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7204", {}),
                                "InstrumentRange": ("V", "ns=1;i=7205", {}),
                                "KindOfQuantity": ("V", "ns=1;i=7206", {}),
                                "ValuePrecision": ("V", "ns=1;i=7207", {}),
                            },
                        ),
                        "MassFlowRate": (
                            "V",
                            "ns=1;i=6578",
                            {
                                "Definition": ("V", "ns=1;i=7208", {}),
                                "EURange": ("V", "ns=1;i=7209", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7210", {}),
                                "InstrumentRange": ("V", "ns=1;i=7211", {}),
                                "KindOfQuantity": ("V", "ns=1;i=7212", {}),
                                "ValuePrecision": ("V", "ns=1;i=7213", {}),
                            },
                        ),
                        "OilConcentration": (
                            "V",
                            "ns=1;i=6579",
                            {
                                "Definition": ("V", "ns=1;i=7214", {}),
                                "EURange": ("V", "ns=1;i=7222", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7223", {}),
                                "InstrumentRange": ("V", "ns=1;i=7224", {}),
                                "KindOfQuantity": ("V", "ns=1;i=7225", {}),
                                "ValuePrecision": ("V", "ns=1;i=7226", {}),
                            },
                        ),
                        "ParticlesPerSizeRange": (
                            "O",
                            "ns=1;i=5216",
                            {
                                "Fine": (
                                    "V",
                                    "ns=1;i=7297",
                                    {
                                        "Definition": ("V", "ns=1;i=8363", {}),
                                        "EURange": ("V", "ns=1;i=8390", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8364", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8391", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=8815", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8392", {}),
                                    },
                                ),
                                "Large": (
                                    "V",
                                    "ns=1;i=7298",
                                    {
                                        "Definition": ("V", "ns=1;i=9179", {}),
                                        "EURange": ("V", "ns=1;i=9181", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9180", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9182", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9183", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9184", {}),
                                    },
                                ),
                                "Medium": (
                                    "V",
                                    "ns=1;i=7299",
                                    {
                                        "Definition": ("V", "ns=1;i=10372", {}),
                                        "EURange": ("V", "ns=1;i=10374", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10373", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10375", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=10376", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10377", {}),
                                    },
                                ),
                            },
                        ),
                        "RelativeHumidity": (
                            "V",
                            "ns=1;i=6629",
                            {
                                "Definition": ("V", "ns=1;i=7227", {}),
                                "EURange": ("V", "ns=1;i=7228", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7229", {}),
                                "InstrumentRange": ("V", "ns=1;i=7230", {}),
                                "KindOfQuantity": ("V", "ns=1;i=7231", {}),
                                "ValuePrecision": ("V", "ns=1;i=7232", {}),
                            },
                        ),
                        "ResetStatistics": ("M", "ns=1;i=7008", {}),
                        "StartTime": ("V", "ns=1;i=6630", {}),
                        "Temperature": (
                            "V",
                            "ns=1;i=6635",
                            {
                                "Definition": ("V", "ns=1;i=7233", {}),
                                "EURange": ("V", "ns=1;i=7234", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7235", {}),
                                "InstrumentRange": ("V", "ns=1;i=7236", {}),
                                "KindOfQuantity": ("V", "ns=1;i=7237", {}),
                                "ValuePrecision": ("V", "ns=1;i=7238", {}),
                            },
                        ),
                        "Volume": (
                            "V",
                            "ns=1;i=6720",
                            {
                                "Definition": ("V", "ns=1;i=7239", {}),
                                "EURange": ("V", "ns=1;i=7240", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7241", {}),
                                "InstrumentRange": ("V", "ns=1;i=7242", {}),
                                "KindOfQuantity": ("V", "ns=1;i=7243", {}),
                                "ValuePrecision": ("V", "ns=1;i=7244", {}),
                            },
                        ),
                        "VolumeFlowRate": (
                            "V",
                            "ns=1;i=6722",
                            {
                                "Definition": ("V", "ns=1;i=7245", {}),
                                "EURange": ("V", "ns=1;i=7246", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7247", {}),
                                "InstrumentRange": ("V", "ns=1;i=7248", {}),
                                "KindOfQuantity": ("V", "ns=1;i=7249", {}),
                                "ValuePrecision": ("V", "ns=1;i=7250", {}),
                            },
                        ),
                    },
                ),
                "FluidType": (
                    "V",
                    "ns=1;i=6274",
                    {"Definition": ("V", "ns=1;i=6284", {})},
                ),
                "Inlet": (
                    "O",
                    "ns=1;i=5217",
                    {
                        "AbsolutePressure": (
                            "V",
                            "ns=1;i=7062",
                            {
                                "Definition": ("V", "ns=1;i=8950", {}),
                                "EURange": ("V", "ns=1;i=8951", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8952", {}),
                                "InstrumentRange": ("V", "ns=1;i=8953", {}),
                                "KindOfQuantity": ("V", "ns=1;i=8954", {}),
                                "ValuePrecision": ("V", "ns=1;i=8955", {}),
                            },
                        ),
                        "AccumulatedVolume": (
                            "V",
                            "ns=1;i=7063",
                            {
                                "Definition": ("V", "ns=1;i=8956", {}),
                                "EURange": ("V", "ns=1;i=8957", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8964", {}),
                                "InstrumentRange": ("V", "ns=1;i=8965", {}),
                                "KindOfQuantity": ("V", "ns=1;i=8966", {}),
                                "ValuePrecision": ("V", "ns=1;i=8967", {}),
                            },
                        ),
                        "DewPoint": (
                            "V",
                            "ns=1;i=7064",
                            {
                                "Definition": ("V", "ns=1;i=8968", {}),
                                "EURange": ("V", "ns=1;i=8969", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8970", {}),
                                "InstrumentRange": ("V", "ns=1;i=8971", {}),
                                "KindOfQuantity": ("V", "ns=1;i=8972", {}),
                                "ValuePrecision": ("V", "ns=1;i=8973", {}),
                            },
                        ),
                        "GaugePressure": (
                            "V",
                            "ns=1;i=7215",
                            {
                                "Definition": ("V", "ns=1;i=8974", {}),
                                "EURange": ("V", "ns=1;i=8975", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8976", {}),
                                "InstrumentRange": ("V", "ns=1;i=8977", {}),
                                "KindOfQuantity": ("V", "ns=1;i=8978", {}),
                                "ValuePrecision": ("V", "ns=1;i=8979", {}),
                            },
                        ),
                        "MassFlowRate": (
                            "V",
                            "ns=1;i=7258",
                            {
                                "Definition": ("V", "ns=1;i=8980", {}),
                                "EURange": ("V", "ns=1;i=8981", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8982", {}),
                                "InstrumentRange": ("V", "ns=1;i=8983", {}),
                                "KindOfQuantity": ("V", "ns=1;i=8984", {}),
                                "ValuePrecision": ("V", "ns=1;i=8985", {}),
                            },
                        ),
                        "OilConcentration": (
                            "V",
                            "ns=1;i=7259",
                            {
                                "Definition": ("V", "ns=1;i=8986", {}),
                                "EURange": ("V", "ns=1;i=8987", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8988", {}),
                                "InstrumentRange": ("V", "ns=1;i=8989", {}),
                                "KindOfQuantity": ("V", "ns=1;i=8990", {}),
                                "ValuePrecision": ("V", "ns=1;i=8991", {}),
                            },
                        ),
                        "ParticlesPerSizeRange": (
                            "O",
                            "ns=1;i=5045",
                            {
                                "Fine": (
                                    "V",
                                    "ns=1;i=6435",
                                    {
                                        "Definition": ("V", "ns=1;i=7318", {}),
                                        "EURange": ("V", "ns=1;i=7320", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=7319", {}),
                                        "InstrumentRange": ("V", "ns=1;i=7654", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=8708", {}),
                                        "ValuePrecision": ("V", "ns=1;i=7655", {}),
                                    },
                                ),
                                "Large": (
                                    "V",
                                    "ns=1;i=6436",
                                    {
                                        "Definition": ("V", "ns=1;i=8853", {}),
                                        "EURange": ("V", "ns=1;i=8855", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8854", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8923", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=8924", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8925", {}),
                                    },
                                ),
                                "Medium": (
                                    "V",
                                    "ns=1;i=6438",
                                    {
                                        "Definition": ("V", "ns=1;i=9279", {}),
                                        "EURange": ("V", "ns=1;i=9281", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9280", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9535", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9536", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9537", {}),
                                    },
                                ),
                            },
                        ),
                        "RelativeHumidity": (
                            "V",
                            "ns=1;i=7279",
                            {
                                "Definition": ("V", "ns=1;i=8992", {}),
                                "EURange": ("V", "ns=1;i=8993", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8994", {}),
                                "InstrumentRange": ("V", "ns=1;i=8995", {}),
                                "KindOfQuantity": ("V", "ns=1;i=8996", {}),
                                "ValuePrecision": ("V", "ns=1;i=8997", {}),
                            },
                        ),
                        "ResetStatistics": ("M", "ns=1;i=7280", {}),
                        "StartTime": ("V", "ns=1;i=7281", {}),
                        "Temperature": (
                            "V",
                            "ns=1;i=7282",
                            {
                                "Definition": ("V", "ns=1;i=8998", {}),
                                "EURange": ("V", "ns=1;i=8999", {}),
                                "EngineeringUnits": ("V", "ns=1;i=9000", {}),
                                "InstrumentRange": ("V", "ns=1;i=9001", {}),
                                "KindOfQuantity": ("V", "ns=1;i=9002", {}),
                                "ValuePrecision": ("V", "ns=1;i=9003", {}),
                            },
                        ),
                        "Volume": (
                            "V",
                            "ns=1;i=7283",
                            {
                                "Definition": ("V", "ns=1;i=9004", {}),
                                "EURange": ("V", "ns=1;i=9005", {}),
                                "EngineeringUnits": ("V", "ns=1;i=9006", {}),
                                "InstrumentRange": ("V", "ns=1;i=9007", {}),
                                "KindOfQuantity": ("V", "ns=1;i=9008", {}),
                                "ValuePrecision": ("V", "ns=1;i=9009", {}),
                            },
                        ),
                        "VolumeFlowRate": (
                            "V",
                            "ns=1;i=7284",
                            {
                                "Definition": ("V", "ns=1;i=9010", {}),
                                "EURange": ("V", "ns=1;i=9011", {}),
                                "EngineeringUnits": ("V", "ns=1;i=9012", {}),
                                "InstrumentRange": ("V", "ns=1;i=9013", {}),
                                "KindOfQuantity": ("V", "ns=1;i=9014", {}),
                                "ValuePrecision": ("V", "ns=1;i=9015", {}),
                            },
                        ),
                    },
                ),
                "Outlet": (
                    "O",
                    "ns=1;i=5251",
                    {
                        "AbsolutePressure": (
                            "V",
                            "ns=1;i=9308",
                            {
                                "Definition": ("V", "ns=1;i=9361", {}),
                                "EURange": ("V", "ns=1;i=9362", {}),
                                "EngineeringUnits": ("V", "ns=1;i=9363", {}),
                                "InstrumentRange": ("V", "ns=1;i=9364", {}),
                                "KindOfQuantity": ("V", "ns=1;i=9365", {}),
                                "ValuePrecision": ("V", "ns=1;i=9366", {}),
                            },
                        ),
                        "AccumulatedVolume": (
                            "V",
                            "ns=1;i=9309",
                            {
                                "Definition": ("V", "ns=1;i=9367", {}),
                                "EURange": ("V", "ns=1;i=9368", {}),
                                "EngineeringUnits": ("V", "ns=1;i=9369", {}),
                                "InstrumentRange": ("V", "ns=1;i=9370", {}),
                                "KindOfQuantity": ("V", "ns=1;i=9371", {}),
                                "ValuePrecision": ("V", "ns=1;i=9372", {}),
                            },
                        ),
                        "DewPoint": (
                            "V",
                            "ns=1;i=9310",
                            {
                                "Definition": ("V", "ns=1;i=9373", {}),
                                "EURange": ("V", "ns=1;i=9374", {}),
                                "EngineeringUnits": ("V", "ns=1;i=9375", {}),
                                "InstrumentRange": ("V", "ns=1;i=9376", {}),
                                "KindOfQuantity": ("V", "ns=1;i=9377", {}),
                                "ValuePrecision": ("V", "ns=1;i=9378", {}),
                            },
                        ),
                        "GaugePressure": (
                            "V",
                            "ns=1;i=9311",
                            {
                                "Definition": ("V", "ns=1;i=9379", {}),
                                "EURange": ("V", "ns=1;i=9380", {}),
                                "EngineeringUnits": ("V", "ns=1;i=9381", {}),
                                "InstrumentRange": ("V", "ns=1;i=9382", {}),
                                "KindOfQuantity": ("V", "ns=1;i=9383", {}),
                                "ValuePrecision": ("V", "ns=1;i=9384", {}),
                            },
                        ),
                        "MassFlowRate": (
                            "V",
                            "ns=1;i=9312",
                            {
                                "Definition": ("V", "ns=1;i=9385", {}),
                                "EURange": ("V", "ns=1;i=9386", {}),
                                "EngineeringUnits": ("V", "ns=1;i=9387", {}),
                                "InstrumentRange": ("V", "ns=1;i=9388", {}),
                                "KindOfQuantity": ("V", "ns=1;i=9389", {}),
                                "ValuePrecision": ("V", "ns=1;i=9390", {}),
                            },
                        ),
                        "OilConcentration": (
                            "V",
                            "ns=1;i=9313",
                            {
                                "Definition": ("V", "ns=1;i=9391", {}),
                                "EURange": ("V", "ns=1;i=9392", {}),
                                "EngineeringUnits": ("V", "ns=1;i=9393", {}),
                                "InstrumentRange": ("V", "ns=1;i=9394", {}),
                                "KindOfQuantity": ("V", "ns=1;i=9395", {}),
                                "ValuePrecision": ("V", "ns=1;i=9396", {}),
                            },
                        ),
                        "ParticlesPerSizeRange": (
                            "O",
                            "ns=1;i=5265",
                            {
                                "Fine": (
                                    "V",
                                    "ns=1;i=7300",
                                    {
                                        "Definition": ("V", "ns=1;i=8393", {}),
                                        "EURange": ("V", "ns=1;i=8395", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8394", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8561", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=8816", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8562", {}),
                                    },
                                ),
                                "Large": (
                                    "V",
                                    "ns=1;i=7301",
                                    {
                                        "Definition": ("V", "ns=1;i=9185", {}),
                                        "EURange": ("V", "ns=1;i=9187", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9186", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9188", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9189", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9190", {}),
                                    },
                                ),
                                "Medium": (
                                    "V",
                                    "ns=1;i=7302",
                                    {
                                        "Definition": ("V", "ns=1;i=10378", {}),
                                        "EURange": ("V", "ns=1;i=10380", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10379", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10381", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=10382", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10383", {}),
                                    },
                                ),
                            },
                        ),
                        "RelativeHumidity": (
                            "V",
                            "ns=1;i=9314",
                            {
                                "Definition": ("V", "ns=1;i=9397", {}),
                                "EURange": ("V", "ns=1;i=9398", {}),
                                "EngineeringUnits": ("V", "ns=1;i=9399", {}),
                                "InstrumentRange": ("V", "ns=1;i=9405", {}),
                                "KindOfQuantity": ("V", "ns=1;i=9406", {}),
                                "ValuePrecision": ("V", "ns=1;i=9407", {}),
                            },
                        ),
                        "ResetStatistics": ("M", "ns=1;i=9315", {}),
                        "StartTime": ("V", "ns=1;i=9316", {}),
                        "Temperature": (
                            "V",
                            "ns=1;i=9317",
                            {
                                "Definition": ("V", "ns=1;i=9408", {}),
                                "EURange": ("V", "ns=1;i=9409", {}),
                                "EngineeringUnits": ("V", "ns=1;i=9410", {}),
                                "InstrumentRange": ("V", "ns=1;i=9411", {}),
                                "KindOfQuantity": ("V", "ns=1;i=9412", {}),
                                "ValuePrecision": ("V", "ns=1;i=9413", {}),
                            },
                        ),
                        "Volume": (
                            "V",
                            "ns=1;i=9318",
                            {
                                "Definition": ("V", "ns=1;i=9414", {}),
                                "EURange": ("V", "ns=1;i=9415", {}),
                                "EngineeringUnits": ("V", "ns=1;i=9416", {}),
                                "InstrumentRange": ("V", "ns=1;i=9417", {}),
                                "KindOfQuantity": ("V", "ns=1;i=9418", {}),
                                "ValuePrecision": ("V", "ns=1;i=9419", {}),
                            },
                        ),
                        "VolumeFlowRate": (
                            "V",
                            "ns=1;i=9319",
                            {
                                "Definition": ("V", "ns=1;i=9420", {}),
                                "EURange": ("V", "ns=1;i=9421", {}),
                                "EngineeringUnits": ("V", "ns=1;i=9422", {}),
                                "InstrumentRange": ("V", "ns=1;i=9423", {}),
                                "KindOfQuantity": ("V", "ns=1;i=9424", {}),
                                "ValuePrecision": ("V", "ns=1;i=9425", {}),
                            },
                        ),
                    },
                ),
            },
        ),
        "FluidQuantitiesType": (
            "OT",
            "ns=1;i=1012",
            {
                "<Quantity>": (
                    "V",
                    "ns=1;i=6159",
                    {
                        "Definition": ("V", "ns=1;i=6160", {}),
                        "EURange": ("V", "ns=1;i=6533", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6535", {}),
                        "InstrumentRange": ("V", "ns=1;i=6537", {}),
                        "KindOfQuantity": ("V", "ns=1;i=6540", {}),
                        "ValuePrecision": ("V", "ns=1;i=6539", {}),
                    },
                ),
                "AbsolutePressure": (
                    "V",
                    "ns=1;i=7791",
                    {
                        "Definition": ("V", "ns=1;i=6015", {}),
                        "EURange": ("V", "ns=1;i=6016", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6118", {}),
                        "InstrumentRange": ("V", "ns=1;i=6119", {}),
                        "KindOfQuantity": ("V", "ns=1;i=6169", {}),
                        "ValuePrecision": ("V", "ns=1;i=6120", {}),
                    },
                ),
                "AccumulatedVolume": (
                    "V",
                    "ns=1;i=6161",
                    {
                        "Definition": ("V", "ns=1;i=6196", {}),
                        "EURange": ("V", "ns=1;i=6197", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6198", {}),
                        "InstrumentRange": ("V", "ns=1;i=6199", {}),
                        "KindOfQuantity": ("V", "ns=1;i=6201", {}),
                        "ValuePrecision": ("V", "ns=1;i=6200", {}),
                    },
                ),
                "DewPoint": (
                    "V",
                    "ns=1;i=6170",
                    {
                        "Definition": ("V", "ns=1;i=6205", {}),
                        "EURange": ("V", "ns=1;i=6206", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6207", {}),
                        "InstrumentRange": ("V", "ns=1;i=6208", {}),
                        "KindOfQuantity": ("V", "ns=1;i=6210", {}),
                        "ValuePrecision": ("V", "ns=1;i=6209", {}),
                    },
                ),
                "GaugePressure": (
                    "V",
                    "ns=1;i=6171",
                    {
                        "Definition": ("V", "ns=1;i=6211", {}),
                        "EURange": ("V", "ns=1;i=6212", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6254", {}),
                        "InstrumentRange": ("V", "ns=1;i=6256", {}),
                        "KindOfQuantity": ("V", "ns=1;i=6270", {}),
                        "ValuePrecision": ("V", "ns=1;i=6258", {}),
                    },
                ),
                "MassFlowRate": (
                    "V",
                    "ns=1;i=6178",
                    {
                        "Definition": ("V", "ns=1;i=6271", {}),
                        "EURange": ("V", "ns=1;i=6272", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6281", {}),
                        "InstrumentRange": ("V", "ns=1;i=6283", {}),
                        "KindOfQuantity": ("V", "ns=1;i=6309", {}),
                        "ValuePrecision": ("V", "ns=1;i=6308", {}),
                    },
                ),
                "OilConcentration": (
                    "V",
                    "ns=1;i=6187",
                    {
                        "Definition": ("V", "ns=1;i=6310", {}),
                        "EURange": ("V", "ns=1;i=6311", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6312", {}),
                        "InstrumentRange": ("V", "ns=1;i=6313", {}),
                        "KindOfQuantity": ("V", "ns=1;i=6420", {}),
                        "ValuePrecision": ("V", "ns=1;i=6392", {}),
                    },
                ),
                "ParticlesPerSizeRange": (
                    "O",
                    "ns=1;i=5007",
                    {
                        "Fine": (
                            "V",
                            "ns=1;i=6044",
                            {
                                "Definition": ("V", "ns=1;i=7308", {}),
                                "EURange": ("V", "ns=1;i=7310", {}),
                                "EngineeringUnits": ("V", "ns=1;i=7309", {}),
                                "InstrumentRange": ("V", "ns=1;i=7311", {}),
                                "KindOfQuantity": ("V", "ns=1;i=8564", {}),
                                "ValuePrecision": ("V", "ns=1;i=7312", {}),
                            },
                        ),
                        "Large": (
                            "V",
                            "ns=1;i=6045",
                            {
                                "Definition": ("V", "ns=1;i=8823", {}),
                                "EURange": ("V", "ns=1;i=8825", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8824", {}),
                                "InstrumentRange": ("V", "ns=1;i=8826", {}),
                                "KindOfQuantity": ("V", "ns=1;i=8827", {}),
                                "ValuePrecision": ("V", "ns=1;i=8829", {}),
                            },
                        ),
                        "Medium": (
                            "V",
                            "ns=1;i=6046",
                            {
                                "Definition": ("V", "ns=1;i=9262", {}),
                                "EURange": ("V", "ns=1;i=9264", {}),
                                "EngineeringUnits": ("V", "ns=1;i=9263", {}),
                                "InstrumentRange": ("V", "ns=1;i=9265", {}),
                                "KindOfQuantity": ("V", "ns=1;i=9266", {}),
                                "ValuePrecision": ("V", "ns=1;i=9267", {}),
                            },
                        ),
                    },
                ),
                "RelativeHumidity": (
                    "V",
                    "ns=1;i=6188",
                    {
                        "Definition": ("V", "ns=1;i=6422", {}),
                        "EURange": ("V", "ns=1;i=6423", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6424", {}),
                        "InstrumentRange": ("V", "ns=1;i=6425", {}),
                        "KindOfQuantity": ("V", "ns=1;i=6427", {}),
                        "ValuePrecision": ("V", "ns=1;i=6426", {}),
                    },
                ),
                "ResetStatistics": ("M", "ns=1;i=7007", {}),
                "StartTime": ("V", "ns=1;i=6541", {}),
                "Temperature": (
                    "V",
                    "ns=1;i=6189",
                    {
                        "Definition": ("V", "ns=1;i=6428", {}),
                        "EURange": ("V", "ns=1;i=6429", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6507", {}),
                        "InstrumentRange": ("V", "ns=1;i=6508", {}),
                        "KindOfQuantity": ("V", "ns=1;i=6514", {}),
                        "ValuePrecision": ("V", "ns=1;i=6513", {}),
                    },
                ),
                "Volume": (
                    "V",
                    "ns=1;i=6194",
                    {
                        "Definition": ("V", "ns=1;i=6515", {}),
                        "EURange": ("V", "ns=1;i=6516", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6517", {}),
                        "InstrumentRange": ("V", "ns=1;i=6518", {}),
                        "KindOfQuantity": ("V", "ns=1;i=6520", {}),
                        "ValuePrecision": ("V", "ns=1;i=6519", {}),
                    },
                ),
                "VolumeFlowRate": (
                    "V",
                    "ns=1;i=6195",
                    {
                        "Definition": ("V", "ns=1;i=6521", {}),
                        "EURange": ("V", "ns=1;i=6522", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6529", {}),
                        "InstrumentRange": ("V", "ns=1;i=6530", {}),
                        "KindOfQuantity": ("V", "ns=1;i=6532", {}),
                        "ValuePrecision": ("V", "ns=1;i=6531", {}),
                    },
                ),
            },
        ),
        "MCSType": (
            "OT",
            "ns=1;i=1017",
            {
                "Analyses": (
                    "O",
                    "ns=1;i=5022",
                    {
                        "EnergyReportISO50001": (
                            "O",
                            "ns=1;i=5112",
                            {
                                "OutputFile": (
                                    "O",
                                    "ns=1;i=5120",
                                    {
                                        "Close": (
                                            "M",
                                            "ns=1;i=9871",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=9872",
                                                    {},
                                                )
                                            },
                                        ),
                                        "GetPosition": (
                                            "M",
                                            "ns=1;i=9873",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=9874",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=9875",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "MimeType": ("V", "ns=1;i=11369", {}),
                                        "Open": (
                                            "M",
                                            "ns=1;i=9876",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=9877",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=9878",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "OpenCount": ("V", "ns=1;i=9879", {}),
                                        "Read": (
                                            "M",
                                            "ns=1;i=9880",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=9881",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=9882",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "SetPosition": (
                                            "M",
                                            "ns=1;i=9883",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=9884",
                                                    {},
                                                )
                                            },
                                        ),
                                        "Size": ("V", "ns=1;i=9885", {}),
                                        "UserWritable": ("V", "ns=1;i=9886", {}),
                                        "Writable": ("V", "ns=1;i=9887", {}),
                                        "Write": (
                                            "M",
                                            "ns=1;i=9888",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=9889",
                                                    {},
                                                )
                                            },
                                        ),
                                    },
                                ),
                                "Trigger": ("M", "ns=1;i=9823", {}),
                            },
                        ),
                        "UIElement": ("V", "ns=1;i=8068", {}),
                    },
                ),
                "Configuration": (
                    "O",
                    "ns=1;i=5019",
                    {
                        "CommunicationSettings": (
                            "O",
                            "ns=1;i=5071",
                            {
                                "DefaultGateway": ("V", "ns=1;i=11311", {}),
                                "Dhcp": (
                                    "V",
                                    "ns=1;i=11312",
                                    {
                                        "Definition": ("V", "ns=1;i=11328", {}),
                                        "FalseState": ("V", "ns=1;i=11313", {}),
                                        "TrueState": ("V", "ns=1;i=11314", {}),
                                    },
                                ),
                                "DnsServer": ("V", "ns=1;i=11315", {}),
                                "DomainName": ("V", "ns=1;i=7869", {}),
                                "Hostname": ("V", "ns=1;i=7870", {}),
                                "IpAddress": ("V", "ns=1;i=7868", {}),
                                "IpVersion": ("V", "ns=1;i=11316", {}),
                                "SubnetMask": ("V", "ns=1;i=11318", {}),
                            },
                        ),
                        "ConfigurationFile": (
                            "O",
                            "ns=1;i=5125",
                            {
                                "Close": (
                                    "M",
                                    "ns=1;i=9909",
                                    {"InputArguments": ("V", "ns=1;i=9910", {})},
                                ),
                                "GetPosition": (
                                    "M",
                                    "ns=1;i=9911",
                                    {
                                        "InputArguments": ("V", "ns=1;i=9912", {}),
                                        "OutputArguments": ("V", "ns=1;i=9913", {}),
                                    },
                                ),
                                "MimeType": ("V", "ns=1;i=6376", {}),
                                "Open": (
                                    "M",
                                    "ns=1;i=9914",
                                    {
                                        "InputArguments": ("V", "ns=1;i=9915", {}),
                                        "OutputArguments": ("V", "ns=1;i=9916", {}),
                                    },
                                ),
                                "OpenCount": ("V", "ns=1;i=9917", {}),
                                "Read": (
                                    "M",
                                    "ns=1;i=9918",
                                    {
                                        "InputArguments": ("V", "ns=1;i=9919", {}),
                                        "OutputArguments": ("V", "ns=1;i=9920", {}),
                                    },
                                ),
                                "SetPosition": (
                                    "M",
                                    "ns=1;i=9921",
                                    {"InputArguments": ("V", "ns=1;i=9922", {})},
                                ),
                                "Size": ("V", "ns=1;i=9923", {}),
                                "UserWritable": ("V", "ns=1;i=9924", {}),
                                "Writable": ("V", "ns=1;i=9925", {}),
                                "Write": (
                                    "M",
                                    "ns=1;i=9926",
                                    {"InputArguments": ("V", "ns=1;i=9927", {})},
                                ),
                            },
                        ),
                        "LoadConfigurationFile": ("M", "ns=1;i=9928", {}),
                        "SaveConfigurationFile": ("M", "ns=1;i=10125", {}),
                        "UIElement": ("V", "ns=1;i=8066", {}),
                    },
                ),
                "ElectricalCircuit": (
                    "O",
                    "ns=1;i=5055",
                    {
                        "Delta": (
                            "O",
                            "ns=1;i=5127",
                            {
                                "ApparentPower": (
                                    "V",
                                    "ns=1;i=7822",
                                    {
                                        "Definition": ("V", "ns=1;i=8219", {}),
                                        "EURange": ("V", "ns=1;i=8221", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8220", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8222", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=8223", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8224", {}),
                                    },
                                ),
                                "Current": (
                                    "V",
                                    "ns=1;i=7823",
                                    {
                                        "Definition": ("V", "ns=1;i=8225", {}),
                                        "EURange": ("V", "ns=1;i=8227", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8226", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8228", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=8229", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8238", {}),
                                    },
                                ),
                                "Energy": (
                                    "V",
                                    "ns=1;i=7824",
                                    {
                                        "Definition": ("V", "ns=1;i=8239", {}),
                                        "EURange": ("V", "ns=1;i=8498", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8497", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8499", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8500", {}),
                                    },
                                ),
                                "Power": (
                                    "V",
                                    "ns=1;i=7825",
                                    {
                                        "Definition": ("V", "ns=1;i=8501", {}),
                                        "EURange": ("V", "ns=1;i=8503", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8502", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8504", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=8505", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8506", {}),
                                    },
                                ),
                                "ResetStatistics": ("M", "ns=1;i=7826", {}),
                                "StartTime": ("V", "ns=1;i=7827", {}),
                                "Voltage": (
                                    "V",
                                    "ns=1;i=7828",
                                    {
                                        "Definition": ("V", "ns=1;i=8507", {}),
                                        "EURange": ("V", "ns=1;i=8509", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=8508", {}),
                                        "InstrumentRange": ("V", "ns=1;i=8510", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=8511", {}),
                                        "ValuePrecision": ("V", "ns=1;i=8512", {}),
                                    },
                                ),
                            },
                        ),
                        "Input": (
                            "O",
                            "ns=1;i=5132",
                            {
                                "ApparentPower": (
                                    "V",
                                    "ns=1;i=9609",
                                    {
                                        "Definition": ("V", "ns=1;i=9690", {}),
                                        "EURange": ("V", "ns=1;i=9692", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9691", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9693", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9694", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9695", {}),
                                    },
                                ),
                                "Current": (
                                    "V",
                                    "ns=1;i=9610",
                                    {
                                        "Definition": ("V", "ns=1;i=9696", {}),
                                        "EURange": ("V", "ns=1;i=9698", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9697", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9699", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9700", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9701", {}),
                                    },
                                ),
                                "Energy": (
                                    "V",
                                    "ns=1;i=9611",
                                    {
                                        "Definition": ("V", "ns=1;i=9702", {}),
                                        "EURange": ("V", "ns=1;i=9704", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9703", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9705", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9706", {}),
                                    },
                                ),
                                "Power": (
                                    "V",
                                    "ns=1;i=9612",
                                    {
                                        "Definition": ("V", "ns=1;i=9707", {}),
                                        "EURange": ("V", "ns=1;i=9709", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9708", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9710", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9711", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9712", {}),
                                    },
                                ),
                                "ResetStatistics": ("M", "ns=1;i=9613", {}),
                                "StartTime": ("V", "ns=1;i=9614", {}),
                                "Voltage": (
                                    "V",
                                    "ns=1;i=9615",
                                    {
                                        "Definition": ("V", "ns=1;i=9713", {}),
                                        "EURange": ("V", "ns=1;i=9715", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=9714", {}),
                                        "InstrumentRange": ("V", "ns=1;i=9716", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=9717", {}),
                                        "ValuePrecision": ("V", "ns=1;i=9718", {}),
                                    },
                                ),
                            },
                        ),
                        "Output": (
                            "O",
                            "ns=1;i=5133",
                            {
                                "ApparentPower": (
                                    "V",
                                    "ns=1;i=9983",
                                    {
                                        "Definition": ("V", "ns=1;i=10062", {}),
                                        "EURange": ("V", "ns=1;i=10064", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10063", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10065", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=10066", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10131", {}),
                                    },
                                ),
                                "Current": (
                                    "V",
                                    "ns=1;i=9984",
                                    {
                                        "Definition": ("V", "ns=1;i=10132", {}),
                                        "EURange": ("V", "ns=1;i=10134", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10133", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10135", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=10136", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10137", {}),
                                    },
                                ),
                                "Energy": (
                                    "V",
                                    "ns=1;i=9985",
                                    {
                                        "Definition": ("V", "ns=1;i=10138", {}),
                                        "EURange": ("V", "ns=1;i=10140", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10139", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10141", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10142", {}),
                                    },
                                ),
                                "Power": (
                                    "V",
                                    "ns=1;i=9986",
                                    {
                                        "Definition": ("V", "ns=1;i=10143", {}),
                                        "EURange": ("V", "ns=1;i=10145", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10144", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10146", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=10147", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10148", {}),
                                    },
                                ),
                                "ResetStatistics": ("M", "ns=1;i=9987", {}),
                                "StartTime": ("V", "ns=1;i=9988", {}),
                                "Voltage": (
                                    "V",
                                    "ns=1;i=9989",
                                    {
                                        "Definition": ("V", "ns=1;i=10149", {}),
                                        "EURange": ("V", "ns=1;i=10151", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10150", {}),
                                        "InstrumentRange": ("V", "ns=1;i=10152", {}),
                                        "KindOfQuantity": ("V", "ns=1;i=10153", {}),
                                        "ValuePrecision": ("V", "ns=1;i=10154", {}),
                                    },
                                ),
                            },
                        ),
                    },
                ),
                "Events": (
                    "O",
                    "ns=1;i=5020",
                    {
                        "Service": (
                            "O",
                            "ns=1;i=5004",
                            {
                                "AckedState": (
                                    "V",
                                    "ns=1;i=8099",
                                    {
                                        "FalseState": ("V", "ns=1;i=8598", {}),
                                        "Id": ("V", "ns=1;i=8100", {}),
                                        "TransitionTime": ("V", "ns=1;i=8599", {}),
                                        "TrueState": ("V", "ns=1;i=8600", {}),
                                    },
                                ),
                                "Acknowledge": (
                                    "M",
                                    "ns=1;i=8101",
                                    {"InputArguments": ("V", "ns=1;i=8102", {})},
                                ),
                                "ActiveState": (
                                    "V",
                                    "ns=1;i=8103",
                                    {
                                        "EffectiveDisplayName": (
                                            "V",
                                            "ns=1;i=8601",
                                            {},
                                        ),
                                        "EffectiveTransitionTime": (
                                            "V",
                                            "ns=1;i=8602",
                                            {},
                                        ),
                                        "FalseState": ("V", "ns=1;i=8603", {}),
                                        "Id": ("V", "ns=1;i=8104", {}),
                                        "TransitionTime": ("V", "ns=1;i=8604", {}),
                                        "TrueState": ("V", "ns=1;i=8605", {}),
                                    },
                                ),
                                "AddComment": (
                                    "M",
                                    "ns=1;i=8105",
                                    {"InputArguments": ("V", "ns=1;i=8106", {})},
                                ),
                                "AudibleEnabled": ("V", "ns=1;i=8419", {}),
                                "AudibleSound": ("V", "ns=1;i=7408", {}),
                                "BranchId": ("V", "ns=1;i=8107", {}),
                                "ClientUserId": ("V", "ns=1;i=8108", {}),
                                "Comment": (
                                    "V",
                                    "ns=1;i=8109",
                                    {"SourceTimestamp": ("V", "ns=1;i=8110", {})},
                                ),
                                "ConditionClassId": ("V", "ns=1;i=8111", {}),
                                "ConditionClassName": ("V", "ns=1;i=8112", {}),
                                "ConditionName": ("V", "ns=1;i=8113", {}),
                                "ConditionSubClassId": ("V", "ns=1;i=8421", {}),
                                "ConditionSubClassName": ("V", "ns=1;i=8422", {}),
                                "Confirm": (
                                    "M",
                                    "ns=1;i=8423",
                                    {"InputArguments": ("V", "ns=1;i=8424", {})},
                                ),
                                "ConfirmedState": (
                                    "V",
                                    "ns=1;i=8425",
                                    {
                                        "FalseState": ("V", "ns=1;i=8426", {}),
                                        "Id": ("V", "ns=1;i=8427", {}),
                                        "TransitionTime": ("V", "ns=1;i=8428", {}),
                                        "TrueState": ("V", "ns=1;i=8429", {}),
                                    },
                                ),
                                "Disable": ("M", "ns=1;i=8114", {}),
                                "Enable": ("M", "ns=1;i=8115", {}),
                                "EnabledState": (
                                    "V",
                                    "ns=1;i=8116",
                                    {
                                        "EffectiveDisplayName": (
                                            "V",
                                            "ns=1;i=8606",
                                            {},
                                        ),
                                        "EffectiveTransitionTime": (
                                            "V",
                                            "ns=1;i=8607",
                                            {},
                                        ),
                                        "FalseState": ("V", "ns=1;i=8608", {}),
                                        "Id": ("V", "ns=1;i=8117", {}),
                                        "TransitionTime": ("V", "ns=1;i=8609", {}),
                                        "TrueState": ("V", "ns=1;i=8610", {}),
                                    },
                                ),
                                "EventId": ("V", "ns=1;i=8118", {}),
                                "EventType": ("V", "ns=1;i=8119", {}),
                                "FirstInGroup": ("O", "ns=1;i=5148", {}),
                                "FirstInGroupFlag": ("V", "ns=1;i=8430", {}),
                                "InputNode": ("V", "ns=1;i=8120", {}),
                                "LastSeverity": (
                                    "V",
                                    "ns=1;i=8121",
                                    {"SourceTimestamp": ("V", "ns=1;i=8122", {})},
                                ),
                                "LatchedState": (
                                    "V",
                                    "ns=1;i=8431",
                                    {
                                        "FalseState": ("V", "ns=1;i=8432", {}),
                                        "Id": ("V", "ns=1;i=8433", {}),
                                        "TransitionTime": ("V", "ns=1;i=8434", {}),
                                        "TrueState": ("V", "ns=1;i=8435", {}),
                                    },
                                ),
                                "LocalTime": ("V", "ns=1;i=8436", {}),
                                "MaxTimeShelved": ("V", "ns=1;i=8437", {}),
                                "Message": ("V", "ns=1;i=8123", {}),
                                "NormalState": ("V", "ns=1;i=8124", {}),
                                "OffDelay": ("V", "ns=1;i=8438", {}),
                                "OnDelay": ("V", "ns=1;i=8439", {}),
                                "OutOfServiceState": (
                                    "V",
                                    "ns=1;i=8440",
                                    {
                                        "FalseState": ("V", "ns=1;i=8441", {}),
                                        "Id": ("V", "ns=1;i=8442", {}),
                                        "TransitionTime": ("V", "ns=1;i=8443", {}),
                                        "TrueState": ("V", "ns=1;i=8444", {}),
                                    },
                                ),
                                "PlaceInService": ("M", "ns=1;i=8445", {}),
                                "Quality": (
                                    "V",
                                    "ns=1;i=8125",
                                    {"SourceTimestamp": ("V", "ns=1;i=8126", {})},
                                ),
                                "ReAlarmRepeatCount": ("V", "ns=1;i=8446", {}),
                                "ReAlarmTime": ("V", "ns=1;i=8447", {}),
                                "ReceiveTime": ("V", "ns=1;i=8127", {}),
                                "RemoveFromService": ("M", "ns=1;i=8448", {}),
                                "Reset": ("M", "ns=1;i=8449", {}),
                                "Retain": ("V", "ns=1;i=8128", {}),
                                "Severity": ("V", "ns=1;i=8129", {}),
                                "ShelvingState": (
                                    "O",
                                    "ns=1;i=5152",
                                    {
                                        "CurrentState": (
                                            "V",
                                            "ns=1;i=8450",
                                            {"Id": ("V", "ns=1;i=8451", {})},
                                        ),
                                        "LastTransition": (
                                            "V",
                                            "ns=1;i=8452",
                                            {
                                                "Id": ("V", "ns=1;i=8453", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=8639",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "OneShotShelve": ("M", "ns=1;i=8454", {}),
                                        "TimedShelve": (
                                            "M",
                                            "ns=1;i=8455",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=8456",
                                                    {},
                                                )
                                            },
                                        ),
                                        "Unshelve": ("M", "ns=1;i=8457", {}),
                                        "UnshelveTime": ("V", "ns=1;i=8458", {}),
                                    },
                                ),
                                "Silence": ("M", "ns=1;i=8459", {}),
                                "SilenceState": (
                                    "V",
                                    "ns=1;i=8460",
                                    {
                                        "FalseState": ("V", "ns=1;i=8461", {}),
                                        "Id": ("V", "ns=1;i=8462", {}),
                                        "TransitionTime": ("V", "ns=1;i=8463", {}),
                                        "TrueState": ("V", "ns=1;i=8464", {}),
                                    },
                                ),
                                "SourceName": ("V", "ns=1;i=8130", {}),
                                "SourceNode": ("V", "ns=1;i=8131", {}),
                                "Suppress": ("M", "ns=1;i=8465", {}),
                                "SuppressedOrShelved": ("V", "ns=1;i=8132", {}),
                                "SuppressedState": (
                                    "V",
                                    "ns=1;i=8466",
                                    {
                                        "FalseState": ("V", "ns=1;i=8467", {}),
                                        "Id": ("V", "ns=1;i=8468", {}),
                                        "TransitionTime": ("V", "ns=1;i=8469", {}),
                                        "TrueState": ("V", "ns=1;i=8470", {}),
                                    },
                                ),
                                "Time": ("V", "ns=1;i=8133", {}),
                                "Unsuppress": ("M", "ns=1;i=8471", {}),
                            },
                        ),
                        "UIElement": ("V", "ns=1;i=8064", {}),
                        "Warning": (
                            "O",
                            "ns=1;i=5131",
                            {
                                "AckedState": (
                                    "V",
                                    "ns=1;i=8176",
                                    {
                                        "FalseState": ("V", "ns=1;i=8624", {}),
                                        "Id": ("V", "ns=1;i=8177", {}),
                                        "TransitionTime": ("V", "ns=1;i=8625", {}),
                                        "TrueState": ("V", "ns=1;i=8626", {}),
                                    },
                                ),
                                "Acknowledge": (
                                    "M",
                                    "ns=1;i=8178",
                                    {"InputArguments": ("V", "ns=1;i=8179", {})},
                                ),
                                "ActiveState": (
                                    "V",
                                    "ns=1;i=8180",
                                    {
                                        "EffectiveDisplayName": (
                                            "V",
                                            "ns=1;i=8627",
                                            {},
                                        ),
                                        "EffectiveTransitionTime": (
                                            "V",
                                            "ns=1;i=8628",
                                            {},
                                        ),
                                        "FalseState": ("V", "ns=1;i=8629", {}),
                                        "Id": ("V", "ns=1;i=8181", {}),
                                        "TransitionTime": ("V", "ns=1;i=8630", {}),
                                        "TrueState": ("V", "ns=1;i=8631", {}),
                                    },
                                ),
                                "AddComment": (
                                    "M",
                                    "ns=1;i=8182",
                                    {"InputArguments": ("V", "ns=1;i=8183", {})},
                                ),
                                "AudibleEnabled": ("V", "ns=1;i=8525", {}),
                                "AudibleSound": ("V", "ns=1;i=7514", {}),
                                "BranchId": ("V", "ns=1;i=8184", {}),
                                "ClientUserId": ("V", "ns=1;i=8185", {}),
                                "Comment": (
                                    "V",
                                    "ns=1;i=8186",
                                    {"SourceTimestamp": ("V", "ns=1;i=8187", {})},
                                ),
                                "ConditionClassId": ("V", "ns=1;i=8188", {}),
                                "ConditionClassName": ("V", "ns=1;i=8189", {}),
                                "ConditionName": ("V", "ns=1;i=8190", {}),
                                "ConditionSubClassId": ("V", "ns=1;i=8527", {}),
                                "ConditionSubClassName": ("V", "ns=1;i=8528", {}),
                                "Confirm": (
                                    "M",
                                    "ns=1;i=8529",
                                    {"InputArguments": ("V", "ns=1;i=8530", {})},
                                ),
                                "ConfirmedState": (
                                    "V",
                                    "ns=1;i=8531",
                                    {
                                        "FalseState": ("V", "ns=1;i=8532", {}),
                                        "Id": ("V", "ns=1;i=8533", {}),
                                        "TransitionTime": ("V", "ns=1;i=8534", {}),
                                        "TrueState": ("V", "ns=1;i=8535", {}),
                                    },
                                ),
                                "Disable": ("M", "ns=1;i=8191", {}),
                                "Enable": ("M", "ns=1;i=8192", {}),
                                "EnabledState": (
                                    "V",
                                    "ns=1;i=8193",
                                    {
                                        "EffectiveDisplayName": (
                                            "V",
                                            "ns=1;i=8632",
                                            {},
                                        ),
                                        "EffectiveTransitionTime": (
                                            "V",
                                            "ns=1;i=8633",
                                            {},
                                        ),
                                        "FalseState": ("V", "ns=1;i=8634", {}),
                                        "Id": ("V", "ns=1;i=8194", {}),
                                        "TransitionTime": ("V", "ns=1;i=8636", {}),
                                        "TrueState": ("V", "ns=1;i=8637", {}),
                                    },
                                ),
                                "EventId": ("V", "ns=1;i=8195", {}),
                                "EventType": ("V", "ns=1;i=8197", {}),
                                "FirstInGroup": ("O", "ns=1;i=5163", {}),
                                "FirstInGroupFlag": ("V", "ns=1;i=8536", {}),
                                "InputNode": ("V", "ns=1;i=8198", {}),
                                "LastSeverity": (
                                    "V",
                                    "ns=1;i=8199",
                                    {"SourceTimestamp": ("V", "ns=1;i=8200", {})},
                                ),
                                "LatchedState": (
                                    "V",
                                    "ns=1;i=8537",
                                    {
                                        "FalseState": ("V", "ns=1;i=8541", {}),
                                        "Id": ("V", "ns=1;i=8542", {}),
                                        "TransitionTime": ("V", "ns=1;i=8543", {}),
                                        "TrueState": ("V", "ns=1;i=8544", {}),
                                    },
                                ),
                                "LocalTime": ("V", "ns=1;i=8545", {}),
                                "MaxTimeShelved": ("V", "ns=1;i=8546", {}),
                                "Message": ("V", "ns=1;i=8201", {}),
                                "NormalState": ("V", "ns=1;i=8202", {}),
                                "OffDelay": ("V", "ns=1;i=8547", {}),
                                "OnDelay": ("V", "ns=1;i=8548", {}),
                                "OutOfServiceState": (
                                    "V",
                                    "ns=1;i=8549",
                                    {
                                        "FalseState": ("V", "ns=1;i=8550", {}),
                                        "Id": ("V", "ns=1;i=8551", {}),
                                        "TransitionTime": ("V", "ns=1;i=8552", {}),
                                        "TrueState": ("V", "ns=1;i=8553", {}),
                                    },
                                ),
                                "PlaceInService": ("M", "ns=1;i=8554", {}),
                                "Quality": (
                                    "V",
                                    "ns=1;i=8203",
                                    {"SourceTimestamp": ("V", "ns=1;i=8204", {})},
                                ),
                                "ReAlarmRepeatCount": ("V", "ns=1;i=8555", {}),
                                "ReAlarmTime": ("V", "ns=1;i=8556", {}),
                                "ReceiveTime": ("V", "ns=1;i=8205", {}),
                                "RemoveFromService": ("M", "ns=1;i=8557", {}),
                                "Reset": ("M", "ns=1;i=8558", {}),
                                "Retain": ("V", "ns=1;i=8206", {}),
                                "Severity": ("V", "ns=1;i=8207", {}),
                                "ShelvingState": (
                                    "O",
                                    "ns=1;i=5164",
                                    {
                                        "CurrentState": (
                                            "V",
                                            "ns=1;i=8559",
                                            {"Id": ("V", "ns=1;i=8560", {})},
                                        ),
                                        "LastTransition": (
                                            "V",
                                            "ns=1;i=8565",
                                            {
                                                "Id": ("V", "ns=1;i=8566", {}),
                                                "TransitionTime": (
                                                    "V",
                                                    "ns=1;i=8641",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "OneShotShelve": ("M", "ns=1;i=8567", {}),
                                        "TimedShelve": (
                                            "M",
                                            "ns=1;i=8568",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=8569",
                                                    {},
                                                )
                                            },
                                        ),
                                        "Unshelve": ("M", "ns=1;i=8570", {}),
                                        "UnshelveTime": ("V", "ns=1;i=8571", {}),
                                    },
                                ),
                                "Silence": ("M", "ns=1;i=8572", {}),
                                "SilenceState": (
                                    "V",
                                    "ns=1;i=8573",
                                    {
                                        "FalseState": ("V", "ns=1;i=8574", {}),
                                        "Id": ("V", "ns=1;i=8575", {}),
                                        "TransitionTime": ("V", "ns=1;i=8576", {}),
                                        "TrueState": ("V", "ns=1;i=8577", {}),
                                    },
                                ),
                                "SourceName": ("V", "ns=1;i=8208", {}),
                                "SourceNode": ("V", "ns=1;i=8209", {}),
                                "Suppress": ("M", "ns=1;i=8578", {}),
                                "SuppressedOrShelved": ("V", "ns=1;i=8210", {}),
                                "SuppressedState": (
                                    "V",
                                    "ns=1;i=8579",
                                    {
                                        "FalseState": ("V", "ns=1;i=8580", {}),
                                        "Id": ("V", "ns=1;i=8581", {}),
                                        "TransitionTime": ("V", "ns=1;i=8582", {}),
                                        "TrueState": ("V", "ns=1;i=8583", {}),
                                    },
                                ),
                                "Time": ("V", "ns=1;i=8211", {}),
                                "Unsuppress": ("M", "ns=1;i=8584", {}),
                            },
                        ),
                    },
                ),
                "Identification": (
                    "O",
                    "ns=1;i=5017",
                    {
                        "AssetId": ("V", "ns=1;i=6298", {}),
                        "ComponentName": ("V", "ns=1;i=6299", {}),
                        "DeviceClass": ("V", "ns=1;i=6300", {}),
                        "DeviceRevision": ("V", "ns=1;i=6301", {}),
                        "HardwareRevision": ("V", "ns=1;i=6302", {}),
                        "InitialOperationDate": ("V", "ns=1;i=6303", {}),
                        "Manufacturer": ("V", "ns=1;i=6285", {}),
                        "ManufacturerUri": ("V", "ns=1;i=6634", {}),
                        "Model": ("V", "ns=1;i=6647", {}),
                        "MonthOfConstruction": ("V", "ns=1;i=6649", {}),
                        "ProductCode": ("V", "ns=1;i=6660", {}),
                        "ProductInstanceUri": ("V", "ns=1;i=6694", {}),
                        "SerialNumber": ("V", "ns=1;i=6286", {}),
                        "SoftwareRevision": ("V", "ns=1;i=6702", {}),
                        "UIElement": ("V", "ns=1;i=6713", {}),
                        "YearOfConstruction": ("V", "ns=1;i=6717", {}),
                    },
                ),
                "Operational": (
                    "O",
                    "ns=1;i=5021",
                    {
                        "OperatingState": (
                            "V",
                            "ns=1;i=8480",
                            {
                                "Definition": ("V", "ns=1;i=8495", {}),
                                "ValuePrecision": ("V", "ns=1;i=8496", {}),
                            },
                        ),
                        "UIElement": ("V", "ns=1;i=8492", {}),
                    },
                ),
                "Statistics": (
                    "O",
                    "ns=1;i=5018",
                    {
                        "RealTime": (
                            "V",
                            "ns=1;i=8517",
                            {
                                "Definition": ("V", "ns=1;i=8586", {}),
                                "EURange": ("V", "ns=1;i=8587", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8588", {}),
                                "InstrumentRange": ("V", "ns=1;i=8589", {}),
                                "ValuePrecision": ("V", "ns=1;i=8590", {}),
                            },
                        ),
                        "RealTimeToNextService": (
                            "V",
                            "ns=1;i=6259",
                            {
                                "Definition": ("V", "ns=1;i=6397", {}),
                                "EURange": ("V", "ns=1;i=6399", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6398", {}),
                                "InstrumentRange": ("V", "ns=1;i=10280", {}),
                                "ValuePrecision": ("V", "ns=1;i=10282", {}),
                            },
                        ),
                        "ResetCondition": ("V", "ns=1;i=8518", {}),
                        "ResetStatistics": ("M", "ns=1;i=8519", {}),
                        "RunningTime": (
                            "V",
                            "ns=1;i=8520",
                            {
                                "Definition": ("V", "ns=1;i=8591", {}),
                                "EURange": ("V", "ns=1;i=8592", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8593", {}),
                                "InstrumentRange": ("V", "ns=1;i=8594", {}),
                                "ValuePrecision": ("V", "ns=1;i=8595", {}),
                            },
                        ),
                        "RunningTimeToNextService": (
                            "V",
                            "ns=1;i=10096",
                            {
                                "Definition": ("V", "ns=1;i=10118", {}),
                                "EURange": ("V", "ns=1;i=10260", {}),
                                "EngineeringUnits": ("V", "ns=1;i=10259", {}),
                                "InstrumentRange": ("V", "ns=1;i=10295", {}),
                                "ValuePrecision": ("V", "ns=1;i=10297", {}),
                            },
                        ),
                        "StartTime": ("V", "ns=1;i=8521", {}),
                        "UIElement": ("V", "ns=1;i=8522", {}),
                    },
                ),
            },
        ),
        "MaintenanceType": (
            "OT",
            "ns=1;i=1028",
            {
                "RealTimeSinceLastService": (
                    "V",
                    "ns=1;i=6292",
                    {
                        "Definition": ("V", "ns=1;i=10228", {}),
                        "EURange": ("V", "ns=1;i=10229", {}),
                        "EngineeringUnits": ("V", "ns=1;i=10230", {}),
                        "InstrumentRange": ("V", "ns=1;i=10231", {}),
                        "ValuePrecision": ("V", "ns=1;i=10232", {}),
                    },
                ),
                "RealTimeToNextService": (
                    "V",
                    "ns=1;i=6714",
                    {
                        "Definition": ("V", "ns=1;i=10301", {}),
                        "EURange": ("V", "ns=1;i=10302", {}),
                        "EngineeringUnits": ("V", "ns=1;i=10303", {}),
                        "InstrumentRange": ("V", "ns=1;i=10304", {}),
                        "ValuePrecision": ("V", "ns=1;i=10305", {}),
                    },
                ),
            },
        ),
        "OperationalType": (
            "OT",
            "ns=1;i=1006",
            {
                "AirnetOperationalType": (
                    "OT",
                    "ns=1;i=1002",
                    {
                        "AirDeliveryRate": (
                            "V",
                            "ns=1;i=10532",
                            {
                                "Definition": ("V", "ns=1;i=10538", {}),
                                "EURange": ("V", "ns=1;i=10539", {}),
                                "EngineeringUnits": ("V", "ns=1;i=10540", {}),
                                "InstrumentRange": ("V", "ns=1;i=10541", {}),
                                "ValuePrecision": ("V", "ns=1;i=10542", {}),
                            },
                        ),
                        "CompressorsIntegrated": (
                            "V",
                            "ns=1;i=6017",
                            {
                                "Definition": ("V", "ns=1;i=6033", {}),
                                "EURange": ("V", "ns=1;i=6034", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6037", {}),
                                "InstrumentRange": ("V", "ns=1;i=6038", {}),
                                "ValuePrecision": ("V", "ns=1;i=6039", {}),
                            },
                        ),
                        "CompressorsIsolated": (
                            "V",
                            "ns=1;i=6019",
                            {
                                "Definition": ("V", "ns=1;i=6105", {}),
                                "EURange": ("V", "ns=1;i=6128", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6129", {}),
                                "InstrumentRange": ("V", "ns=1;i=6663", {}),
                                "ValuePrecision": ("V", "ns=1;i=6683", {}),
                            },
                        ),
                        "CompressorsNotAvailable": (
                            "V",
                            "ns=1;i=6027",
                            {
                                "Definition": ("V", "ns=1;i=6076", {}),
                                "EURange": ("V", "ns=1;i=6079", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6095", {}),
                                "InstrumentRange": ("V", "ns=1;i=6096", {}),
                                "ValuePrecision": ("V", "ns=1;i=6097", {}),
                            },
                        ),
                        "ControlPressure": (
                            "V",
                            "ns=1;i=8283",
                            {
                                "Definition": ("V", "ns=1;i=8285", {}),
                                "EURange": ("V", "ns=1;i=8286", {}),
                                "EngineeringUnits": ("V", "ns=1;i=8287", {}),
                                "InstrumentRange": ("V", "ns=1;i=8288", {}),
                                "ValuePrecision": ("V", "ns=1;i=8289", {}),
                            },
                        ),
                        "HealthState": (
                            "V",
                            "ns=1;i=6771",
                            {
                                "Definition": ("V", "ns=1;i=8174", {}),
                                "ValuePrecision": ("V", "ns=1;i=8175", {}),
                            },
                        ),
                        "IntegratedState": (
                            "V",
                            "ns=1;i=7186",
                            {
                                "Definition": ("V", "ns=1;i=8212", {}),
                                "ValuePrecision": ("V", "ns=1;i=8213", {}),
                            },
                        ),
                        "OperatingState": (
                            "V",
                            "ns=1;i=8021",
                            {
                                "Definition": ("V", "ns=1;i=8214", {}),
                                "ValuePrecision": ("V", "ns=1;i=8215", {}),
                            },
                        ),
                        "SpecificEnergy": (
                            "V",
                            "ns=1;i=10534",
                            {
                                "Definition": ("V", "ns=1;i=10548", {}),
                                "EURange": ("V", "ns=1;i=10549", {}),
                                "EngineeringUnits": ("V", "ns=1;i=10550", {}),
                                "InstrumentRange": ("V", "ns=1;i=10551", {}),
                                "ValuePrecision": ("V", "ns=1;i=10552", {}),
                            },
                        ),
                        "SpecificEnergyCost": (
                            "V",
                            "ns=1;i=10536",
                            {
                                "Definition": ("V", "ns=1;i=10543", {}),
                                "EURange": ("V", "ns=1;i=10544", {}),
                                "EngineeringUnits": ("V", "ns=1;i=10545", {}),
                                "InstrumentRange": ("V", "ns=1;i=10546", {}),
                                "ValuePrecision": ("V", "ns=1;i=10547", {}),
                            },
                        ),
                        "VolumeFlowRateAvailable": (
                            "V",
                            "ns=1;i=6029",
                            {
                                "Definition": ("V", "ns=1;i=6042", {}),
                                "EURange": ("V", "ns=1;i=6043", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6048", {}),
                                "InstrumentRange": ("V", "ns=1;i=10623", {}),
                                "ValuePrecision": ("V", "ns=1;i=10624", {}),
                            },
                        ),
                        "VolumeFlowRateUnavailable": (
                            "V",
                            "ns=1;i=6031",
                            {
                                "Definition": ("V", "ns=1;i=6049", {}),
                                "EURange": ("V", "ns=1;i=6051", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6055", {}),
                                "InstrumentRange": ("V", "ns=1;i=10627", {}),
                                "ValuePrecision": ("V", "ns=1;i=10628", {}),
                            },
                        ),
                    },
                ),
                "CompressorOperationalType": (
                    "OT",
                    "ns=1;i=1045",
                    {
                        "ActivePressureBand": (
                            "V",
                            "ns=1;i=6644",
                            {"Definition": ("V", "ns=1;i=6645", {})},
                        ),
                        "FlowRateRatio": (
                            "V",
                            "ns=1;i=6646",
                            {
                                "Definition": ("V", "ns=1;i=6666", {}),
                                "EURange": ("V", "ns=1;i=6667", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6668", {}),
                                "InstrumentRange": ("V", "ns=1;i=10271", {}),
                                "ValuePrecision": ("V", "ns=1;i=10272", {}),
                            },
                        ),
                        "IsentropicEfficiency": (
                            "V",
                            "ns=1;i=6648",
                            {
                                "Definition": ("V", "ns=1;i=6669", {}),
                                "EURange": ("V", "ns=1;i=6670", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6671", {}),
                                "InstrumentRange": ("V", "ns=1;i=10263", {}),
                                "ValuePrecision": ("V", "ns=1;i=10264", {}),
                            },
                        ),
                        "OperatingState": (
                            "V",
                            "ns=1;i=8217",
                            {
                                "Definition": ("V", "ns=1;i=8232", {}),
                                "ValuePrecision": ("V", "ns=1;i=8236", {}),
                            },
                        ),
                        "SpecificEnergyRequirement": (
                            "V",
                            "ns=1;i=6659",
                            {
                                "Definition": ("V", "ns=1;i=6677", {}),
                                "EURange": ("V", "ns=1;i=6678", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6679", {}),
                                "InstrumentRange": ("V", "ns=1;i=10267", {}),
                                "ValuePrecision": ("V", "ns=1;i=10268", {}),
                            },
                        ),
                    },
                ),
                "ConverterOperationalType": (
                    "OT",
                    "ns=1;i=1046",
                    {
                        "CatalyticMaterialTemperature": (
                            "V",
                            "ns=1;i=6693",
                            {
                                "Definition": ("V", "ns=1;i=6695", {}),
                                "EURange": ("V", "ns=1;i=6696", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6700", {}),
                                "InstrumentRange": ("V", "ns=1;i=10307", {}),
                                "ValuePrecision": ("V", "ns=1;i=10308", {}),
                            },
                        )
                    },
                ),
                "DrainOperationalType": (
                    "OT",
                    "ns=1;i=1003",
                    {"DrainTest": ("M", "ns=1;i=10530", {})},
                ),
                "DryerOperationalType": (
                    "OT",
                    "ns=1;i=1052",
                    {
                        "OnOff": (
                            "V",
                            "ns=1;i=10670",
                            {
                                "Definition": ("V", "ns=1;i=10678", {}),
                                "FalseState": ("V", "ns=1;i=10671", {}),
                                "TrueState": ("V", "ns=1;i=10672", {}),
                                "ValuePrecision": ("V", "ns=1;i=10679", {}),
                            },
                        ),
                        "OperatingState": (
                            "V",
                            "ns=1;i=10673",
                            {
                                "Definition": ("V", "ns=1;i=10680", {}),
                                "ValuePrecision": ("V", "ns=1;i=10681", {}),
                            },
                        ),
                        "PressureDewPoint": (
                            "V",
                            "ns=1;i=6701",
                            {
                                "Definition": ("V", "ns=1;i=6706", {}),
                                "EURange": ("V", "ns=1;i=6707", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6708", {}),
                                "InstrumentRange": ("V", "ns=1;i=10311", {}),
                                "ValuePrecision": ("V", "ns=1;i=10312", {}),
                            },
                        ),
                    },
                ),
                "HealthState": (
                    "V",
                    "ns=1;i=6064",
                    {
                        "Definition": ("V", "ns=1;i=6130", {}),
                        "ValuePrecision": ("V", "ns=1;i=6131", {}),
                    },
                ),
                "IntegratedState": (
                    "V",
                    "ns=1;i=6065",
                    {
                        "Definition": ("V", "ns=1;i=6132", {}),
                        "ValuePrecision": ("V", "ns=1;i=6222", {}),
                    },
                ),
                "OnOff": (
                    "V",
                    "ns=1;i=6655",
                    {
                        "Definition": ("V", "ns=1;i=6769", {}),
                        "FalseState": ("V", "ns=1;i=6675", {}),
                        "TrueState": ("V", "ns=1;i=10607", {}),
                        "ValuePrecision": ("V", "ns=1;i=6770", {}),
                    },
                ),
                "OperatingState": (
                    "V",
                    "ns=1;i=6066",
                    {
                        "Definition": ("V", "ns=1;i=6653", {}),
                        "ValuePrecision": ("V", "ns=1;i=6654", {}),
                    },
                ),
                "ValveOperationalType": (
                    "OT",
                    "ns=1;i=1053",
                    {
                        "ContinuousPosition": (
                            "V",
                            "ns=1;i=6712",
                            {
                                "Definition": ("V", "ns=1;i=7978", {}),
                                "EURange": ("V", "ns=1;i=8149", {}),
                                "EngineeringUnits": ("V", "ns=1;i=11340", {}),
                                "InstrumentRange": ("V", "ns=1;i=11341", {}),
                                "ValuePrecision": ("V", "ns=1;i=11342", {}),
                            },
                        ),
                        "PortUsed": (
                            "V",
                            "ns=1;i=11343",
                            {
                                "Definition": ("V", "ns=1;i=11344", {}),
                                "ValuePrecision": ("V", "ns=1;i=11345", {}),
                            },
                        ),
                    },
                ),
            },
        ),
        "ParticleType": (
            "OT",
            "ns=1;i=1043",
            {
                "Fine": (
                    "V",
                    "ns=1;i=6010",
                    {
                        "Definition": ("V", "ns=1;i=7303", {}),
                        "EURange": ("V", "ns=1;i=7304", {}),
                        "EngineeringUnits": ("V", "ns=1;i=7305", {}),
                        "InstrumentRange": ("V", "ns=1;i=7306", {}),
                        "KindOfQuantity": ("V", "ns=1;i=8563", {}),
                        "ValuePrecision": ("V", "ns=1;i=7307", {}),
                    },
                ),
                "Large": (
                    "V",
                    "ns=1;i=6011",
                    {
                        "Definition": ("V", "ns=1;i=8817", {}),
                        "EURange": ("V", "ns=1;i=8818", {}),
                        "EngineeringUnits": ("V", "ns=1;i=8819", {}),
                        "InstrumentRange": ("V", "ns=1;i=8820", {}),
                        "KindOfQuantity": ("V", "ns=1;i=8822", {}),
                        "ValuePrecision": ("V", "ns=1;i=8821", {}),
                    },
                ),
                "Medium": (
                    "V",
                    "ns=1;i=6012",
                    {
                        "Definition": ("V", "ns=1;i=9241", {}),
                        "EURange": ("V", "ns=1;i=9242", {}),
                        "EngineeringUnits": ("V", "ns=1;i=9243", {}),
                        "InstrumentRange": ("V", "ns=1;i=9244", {}),
                        "KindOfQuantity": ("V", "ns=1;i=9246", {}),
                        "ValuePrecision": ("V", "ns=1;i=9245", {}),
                    },
                ),
            },
        ),
        "StatisticsType": (
            "OT",
            "ns=1;i=1018",
            {
                "CompressorStatisticsType": (
                    "OT",
                    "ns=1;i=1027",
                    {
                        "LoadedTime": (
                            "V",
                            "ns=1;i=6083",
                            {
                                "Definition": ("V", "ns=1;i=6123", {}),
                                "EURange": ("V", "ns=1;i=6124", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6125", {}),
                                "InstrumentRange": ("V", "ns=1;i=6126", {}),
                                "ValuePrecision": ("V", "ns=1;i=6127", {}),
                            },
                        ),
                        "UnloadedTime": (
                            "V",
                            "ns=1;i=6122",
                            {
                                "Definition": ("V", "ns=1;i=6136", {}),
                                "EURange": ("V", "ns=1;i=6226", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6227", {}),
                                "InstrumentRange": ("V", "ns=1;i=6228", {}),
                                "ValuePrecision": ("V", "ns=1;i=6229", {}),
                            },
                        ),
                    },
                ),
                "RealTime": (
                    "V",
                    "ns=1;i=6002",
                    {
                        "Definition": ("V", "ns=1;i=6018", {}),
                        "EURange": ("V", "ns=1;i=6020", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6021", {}),
                        "InstrumentRange": ("V", "ns=1;i=6028", {}),
                        "ValuePrecision": ("V", "ns=1;i=6030", {}),
                    },
                ),
                "RealTimeToNextService": (
                    "V",
                    "ns=1;i=6005",
                    {
                        "Definition": ("V", "ns=1;i=6007", {}),
                        "EURange": ("V", "ns=1;i=6008", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6262", {}),
                        "InstrumentRange": ("V", "ns=1;i=6263", {}),
                        "ValuePrecision": ("V", "ns=1;i=6264", {}),
                    },
                ),
                "ResetCondition": ("V", "ns=1;i=6231", {}),
                "ResetStatistics": ("M", "ns=1;i=7793", {}),
                "RunningTime": (
                    "V",
                    "ns=1;i=6006",
                    {
                        "Definition": ("V", "ns=1;i=6032", {}),
                        "EURange": ("V", "ns=1;i=6050", {}),
                        "EngineeringUnits": ("V", "ns=1;i=6063", {}),
                        "InstrumentRange": ("V", "ns=1;i=6077", {}),
                        "ValuePrecision": ("V", "ns=1;i=6081", {}),
                    },
                ),
                "RunningTimeToNextService": (
                    "V",
                    "ns=1;i=6001",
                    {
                        "Definition": ("V", "ns=1;i=6003", {}),
                        "EURange": ("V", "ns=1;i=6004", {}),
                        "EngineeringUnits": ("V", "ns=1;i=7580", {}),
                        "InstrumentRange": ("V", "ns=1;i=7581", {}),
                        "ValuePrecision": ("V", "ns=1;i=7582", {}),
                    },
                ),
                "StartTime": ("V", "ns=1;i=6230", {}),
            },
        ),
    },
}
