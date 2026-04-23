# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 9f0b8889707b5aa975d930e1cc7fb4613c7f2d6c68c1bd4fb79eb523bc56fd35
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/CommercialKitchenEquipment/"
_VERSION: str = "1.0"
_REQUIRED: list = [
    {"uri": "http://opcfoundation.org/UA/", "version": "1.04"},
    {"uri": "http://opcfoundation.org/UA/DI/", "version": "1.01"},
]
_STRUCTURES: list = []
_ENUMS: list = [
    (
        "ns=1;i=3014",
        "BeverageSMLEnumeration",
        {
            "fields": [
                {"name": "Inactive", "value": 0, "display_name": "Inactive"},
                {"name": "Small", "value": 1, "display_name": "Small"},
                {"name": "Large", "value": 2, "display_name": "Large"},
                {"name": "ExtraLarge", "value": 3, "display_name": "ExtraLarge"},
            ]
        },
    ),
    (
        "ns=1;i=3008",
        "ChamberModeEnumeration",
        {
            "fields": [
                {"name": "NoSpecialMode", "value": 0, "display_name": "NoSpecialMode"},
                {"name": "Off", "value": 1, "display_name": "Off"},
                {"name": "Autostart", "value": 2, "display_name": "Autostart"},
                {"name": "Standby", "value": 3, "display_name": "Standby"},
                {"name": "PreHeat", "value": 4, "display_name": "PreHeat"},
                {"name": "CoolDown", "value": 5, "display_name": "CoolDown"},
                {"name": "Working", "value": 6, "display_name": "Working"},
                {"name": "Cleaning", "value": 7, "display_name": "Cleaning"},
                {"name": "EnergySave", "value": 8, "display_name": "EnergySave"},
                {"name": "ServiceMode", "value": 9, "display_name": "ServiceMode"},
                {"name": "QuickCool", "value": 10, "display_name": "QuickCool"},
                {"name": "FlashFreeze", "value": 11, "display_name": "FlashFreeze"},
                {
                    "name": "ProofingInterruption",
                    "value": 12,
                    "display_name": "ProofingInterruption",
                },
                {"name": "ProofingDelay", "value": 13, "display_name": "ProofingDelay"},
                {"name": "Proofing", "value": 14, "display_name": "Proofing"},
                {"name": "Setting", "value": 15, "display_name": "Setting"},
                {"name": "Defrost", "value": 16, "display_name": "Defrost"},
                {"name": "Baking", "value": 17, "display_name": "Baking"},
                {"name": "Steaming", "value": 18, "display_name": "Steaming"},
            ]
        },
    ),
    (
        "ns=1;i=3015",
        "CoffeeMachineModeEnumeration",
        {
            "fields": [
                {"name": "Off", "value": 0, "display_name": "Off"},
                {"name": "Standby", "value": 1, "display_name": "Standby"},
                {"name": "Error", "value": 2, "display_name": "Error"},
                {"name": "Cleaning", "value": 3, "display_name": "Cleaning"},
            ]
        },
    ),
    (
        "ns=1;i=3006",
        "CombiSteamerModeEnumeration",
        {
            "fields": [
                {"name": "Off", "value": 0, "display_name": "Off"},
                {"name": "On", "value": 1, "display_name": "On"},
                {"name": "Preheat", "value": 2, "display_name": "Preheat"},
                {"name": "StandBy", "value": 3, "display_name": "StandBy"},
                {"name": "Steaming", "value": 4, "display_name": "Steaming"},
                {"name": "CombiSteaming", "value": 5, "display_name": "CombiSteaming"},
                {"name": "HotAir", "value": 6, "display_name": "HotAir"},
                {"name": "Perfection", "value": 7, "display_name": "Perfection"},
                {"name": "Cleaning", "value": 8, "display_name": "Cleaning"},
                {"name": "PresetStart", "value": 9, "display_name": "PresetStart"},
                {"name": "Error", "value": 10, "display_name": "Error"},
            ]
        },
    ),
    (
        "ns=1;i=3010",
        "CookingKettleModeEnumeration",
        {
            "fields": [
                {"name": "Off", "value": 0, "display_name": "Off"},
                {"name": "Preheat", "value": 1, "display_name": "Preheat"},
                {"name": "SoftCook", "value": 2, "display_name": "SoftCook"},
                {"name": "Cook", "value": 3, "display_name": "Cook"},
                {"name": "CookSlow", "value": 4, "display_name": "CookSlow"},
                {"name": "KeepWarming", "value": 5, "display_name": "KeepWarming"},
                {"name": "Stiring", "value": 6, "display_name": "Stiring"},
                {"name": "PresetStart", "value": 7, "display_name": "PresetStart"},
                {"name": "Error", "value": 8, "display_name": "Error"},
            ]
        },
    ),
    (
        "ns=1;i=3021",
        "CurrentStateEnumeration",
        {
            "fields": [
                {"name": "Off", "value": 0, "display_name": "Off"},
                {"name": "Standby", "value": 1, "display_name": "Standby"},
                {"name": "Power", "value": 2, "display_name": "Power"},
                {"name": "PotDetection", "value": 3, "display_name": "PotDetection"},
            ]
        },
    ),
    (
        "ns=1;i=3002",
        "EnergySourceEnumeration",
        {
            "fields": [
                {"name": "Electric", "value": 0, "display_name": "Electric"},
                {"name": "Gas", "value": 1, "display_name": "Gas"},
                {"name": "Steam", "value": 2, "display_name": "Steam"},
            ]
        },
    ),
    (
        "ns=1;i=3003",
        "FryerModeEnumeration",
        {
            "fields": [
                {"name": "Off", "value": 0, "display_name": "Off"},
                {"name": "Preheat", "value": 1, "display_name": "Preheat"},
                {"name": "Melting", "value": 2, "display_name": "Melting"},
                {"name": "Frying", "value": 3, "display_name": "Frying"},
                {"name": "StandBy", "value": 4, "display_name": "StandBy"},
                {"name": "Filtering", "value": 5, "display_name": "Filtering"},
                {"name": "Error", "value": 6, "display_name": "Error"},
            ]
        },
    ),
    (
        "ns=1;i=3005",
        "FryingPanModeEnumeration",
        {
            "fields": [
                {"name": "Off", "value": 0, "display_name": "Off"},
                {"name": "Preheat", "value": 1, "display_name": "Preheat"},
                {"name": "SoftCook", "value": 2, "display_name": "SoftCook"},
                {"name": "Cook", "value": 3, "display_name": "Cook"},
                {"name": "CookSlow", "value": 4, "display_name": "CookSlow"},
                {"name": "Frying", "value": 5, "display_name": "Frying"},
                {
                    "name": "PressureCooking",
                    "value": 6,
                    "display_name": "PressureCooking",
                },
                {"name": "KeepWarming", "value": 7, "display_name": "KeepWarming"},
                {"name": "PresetStart", "value": 8, "display_name": "PresetStart"},
                {"name": "Error", "value": 9, "display_name": "Error"},
            ]
        },
    ),
    (
        "ns=1;i=3025",
        "GrillingZoneStateEnumeration",
        {
            "fields": [
                {"name": "Off", "value": 0, "display_name": "Off"},
                {"name": "Standby", "value": 1, "display_name": "Standby"},
                {"name": "Idle", "value": 2, "display_name": "Idle"},
                {"name": "Grilling", "value": 3, "display_name": "Grilling"},
            ]
        },
    ),
    (
        "ns=1;i=3017",
        "HygieneModeEnumeration",
        {
            "fields": [
                {
                    "name": "HygieneOperationOFF",
                    "value": 0,
                    "display_name": "HygieneOperationOFF",
                },
                {"name": "HygieneA0", "value": 1, "display_name": "HygieneA0"},
                {"name": "HygieneHUE", "value": 2, "display_name": "HygieneHUE"},
                {"name": "HygieneMU", "value": 3, "display_name": "HygieneMU"},
                {
                    "name": "HygieneThermolable",
                    "value": 4,
                    "display_name": "HygieneThermolable",
                },
                {"name": "HygieneA0_TD", "value": 5, "display_name": "HygieneA0_TD"},
            ]
        },
    ),
    (
        "ns=1;i=3011",
        "MultiFunctionPanModeEnumeration",
        {
            "fields": [
                {"name": "Off", "value": 0, "display_name": "Off"},
                {"name": "On", "value": 1, "display_name": "On"},
                {"name": "Preheat", "value": 2, "display_name": "Preheat"},
                {"name": "StandBy", "value": 3, "display_name": "StandBy"},
                {
                    "name": "PressureCooking",
                    "value": 4,
                    "display_name": "PressureCooking",
                },
                {"name": "SoftCooking", "value": 5, "display_name": "SoftCooking"},
                {"name": "Cooking", "value": 6, "display_name": "Cooking"},
                {"name": "Grilling", "value": 7, "display_name": "Grilling"},
                {"name": "Frying", "value": 8, "display_name": "Frying"},
                {"name": "Regenerate", "value": 9, "display_name": "Regenerate"},
                {"name": "DeltaTcooking", "value": 10, "display_name": "DeltaTcooking"},
                {"name": "ZoneGrilling", "value": 11, "display_name": "ZoneGrilling"},
                {"name": "ZoneCooking", "value": 12, "display_name": "ZoneCooking"},
                {"name": "Cleaning", "value": 13, "display_name": "Cleaning"},
                {"name": "PresetStart", "value": 14, "display_name": "PresetStart"},
                {"name": "Error", "value": 15, "display_name": "Error"},
            ]
        },
    ),
    (
        "ns=1;i=3023",
        "OperatingModeEnumeration",
        {
            "fields": [
                {"name": "Preheat", "value": 0, "display_name": "Preheat"},
                {"name": "CoolDown", "value": 1, "display_name": "CoolDown"},
                {"name": "Process", "value": 2, "display_name": "Process"},
                {"name": "PowerSaving", "value": 3, "display_name": "PowerSaving"},
                {"name": "Standby", "value": 4, "display_name": "Standby"},
                {"name": "Service", "value": 5, "display_name": "Service"},
                {"name": "Cleaning", "value": 6, "display_name": "Cleaning"},
                {"name": "Off", "value": 7, "display_name": "Off"},
                {"name": "Error", "value": 8, "display_name": "Error"},
            ]
        },
    ),
    (
        "ns=1;i=3018",
        "OperationModeEnumeration",
        {
            "fields": [
                {"name": "Init", "value": 0, "display_name": "Init"},
                {"name": "MachineOff", "value": 1, "display_name": "MachineOff"},
                {"name": "Filling", "value": 2, "display_name": "Filling"},
                {
                    "name": "FillingHeating",
                    "value": 3,
                    "display_name": "FillingHeating",
                },
                {"name": "Heating", "value": 4, "display_name": "Heating"},
                {
                    "name": "EnableOperation",
                    "value": 5,
                    "display_name": "EnableOperation",
                },
                {
                    "name": "ReadyForOperation",
                    "value": 6,
                    "display_name": "ReadyForOperation",
                },
                {"name": "Operation", "value": 7, "display_name": "Operation"},
                {"name": "Cycle_pause", "value": 8, "display_name": "Cycle_pause"},
                {"name": "NotDefined1", "value": 9, "display_name": "NotDefined1"},
                {"name": "SelfCleaning", "value": 10, "display_name": "SelfCleaning"},
                {"name": "NotDefined2", "value": 11, "display_name": "NotDefined2"},
                {"name": "RemoteControl", "value": 12, "display_name": "RemoteControl"},
                {
                    "name": "ControllingOutputs",
                    "value": 13,
                    "display_name": "ControllingOutputs",
                },
                {"name": "NotDefined3", "value": 14, "display_name": "NotDefined3"},
                {"name": "Error", "value": 15, "display_name": "Error"},
            ]
        },
    ),
    (
        "ns=1;i=3013",
        "PastaCookerModeEnumeration",
        {
            "fields": [
                {"name": "Off", "value": 0, "display_name": "Off"},
                {"name": "Preheat", "value": 1, "display_name": "Preheat"},
                {"name": "SoftCook", "value": 2, "display_name": "SoftCook"},
                {"name": "Cook", "value": 3, "display_name": "Cook"},
                {"name": "CookSlow", "value": 4, "display_name": "CookSlow"},
                {"name": "KeepWarming", "value": 5, "display_name": "KeepWarming"},
                {"name": "PresetStart", "value": 6, "display_name": "PresetStart"},
                {"name": "Error", "value": 7, "display_name": "Error"},
            ]
        },
    ),
    (
        "ns=1;i=3022",
        "PlatenPositionStateEnumeration",
        {
            "fields": [
                {"name": "Home", "value": 0, "display_name": "Home"},
                {"name": "Cooking", "value": 1, "display_name": "Cooking"},
                {"name": "Idle", "value": 2, "display_name": "Idle"},
                {"name": "Open", "value": 3, "display_name": "Open"},
            ]
        },
    ),
    (
        "ns=1;i=3009",
        "PressureCookingKettleModeEnumeration",
        {
            "fields": [
                {"name": "Off", "value": 0, "display_name": "Off"},
                {"name": "Preheat", "value": 1, "display_name": "Preheat"},
                {"name": "SoftCook", "value": 2, "display_name": "SoftCook"},
                {"name": "Cook", "value": 3, "display_name": "Cook"},
                {"name": "CookSlow", "value": 4, "display_name": "CookSlow"},
                {"name": "Pressure", "value": 5, "display_name": "Pressure"},
                {"name": "KeepWarming", "value": 6, "display_name": "KeepWarming"},
                {"name": "PresetStart", "value": 7, "display_name": "PresetStart"},
                {"name": "Error", "value": 8, "display_name": "Error"},
            ]
        },
    ),
    (
        "ns=1;i=3016",
        "ProgramModeEnumeration",
        {
            "fields": [
                {"name": "OperationOFF", "value": 0, "display_name": "OperationOFF"},
                {"name": "PreWash", "value": 1, "display_name": "PreWash"},
                {"name": "Cleaning1", "value": 2, "display_name": "Cleaning1"},
                {
                    "name": "WashTimeIncreased",
                    "value": 3,
                    "display_name": "WashTimeIncreased",
                },
                {"name": "Cleaning2", "value": 4, "display_name": "Cleaning2"},
                {"name": "DrainingPause", "value": 5, "display_name": "DrainingPause"},
                {"name": "Draining", "value": 6, "display_name": "Draining"},
                {"name": "FinalRinse", "value": 7, "display_name": "FinalRinse"},
                {"name": "WaitingTime", "value": 8, "display_name": "WaitingTime"},
                {"name": "HeatRecovery", "value": 9, "display_name": "HeatRecovery"},
            ]
        },
    ),
    (
        "ns=1;i=3004",
        "SignalModeEnumeration",
        {
            "fields": [
                {"name": "SignalOff", "value": 0, "display_name": "SignalOff"},
                {"name": "SignalOn", "value": 1, "display_name": "SignalOn"},
                {"name": "SignalAck", "value": 2, "display_name": "SignalAck"},
            ]
        },
    ),
    (
        "ns=1;i=3007",
        "SpecialCookingModeEnumeration",
        {
            "fields": [
                {"name": "NoSpecialMode", "value": 0, "display_name": "NoSpecialMode"},
                {"name": "Baking", "value": 1, "display_name": "Baking"},
                {"name": "SousVide", "value": 2, "display_name": "SousVide"},
                {"name": "RestStage", "value": 3, "display_name": "RestStage"},
                {
                    "name": "Humidification",
                    "value": 4,
                    "display_name": "Humidification",
                },
                {"name": "PerfectHold", "value": 5, "display_name": "PerfectHold"},
                {"name": "InfoStep", "value": 6, "display_name": "InfoStep"},
                {"name": "Smoking", "value": 7, "display_name": "Smoking"},
                {
                    "name": "LowTemp-Cooking",
                    "value": 8,
                    "display_name": "LowTemp-Cooking",
                },
                {
                    "name": "DeltaTSteaming",
                    "value": 9,
                    "display_name": "DeltaTSteaming",
                },
            ]
        },
    ),
    (
        "ns=1;i=3012",
        "SpecialFunctionModeEnumeration",
        {
            "fields": [
                {"name": "LidUpDown", "value": 0, "display_name": "LidUpDown"},
                {"name": "PanTilt", "value": 1, "display_name": "PanTilt"},
                {"name": "WaterSupply", "value": 2, "display_name": "WaterSupply"},
                {"name": "DrainOnOff", "value": 3, "display_name": "DrainOnOff"},
            ]
        },
    ),
    (
        "ns=1;i=3024",
        "StatusEnumeration",
        {
            "fields": [
                {"name": "INIT", "value": 0, "display_name": "INIT"},
                {"name": "WATER_PURGE", "value": 1, "display_name": "WATER_PURGE"},
                {"name": "PRE_CHILL", "value": 2, "display_name": "PRE_CHILL"},
                {"name": "FREEZE", "value": 3, "display_name": "FREEZE"},
                {"name": "HARVEST", "value": 4, "display_name": "HARVEST"},
                {"name": "BIN_FULL", "value": 5, "display_name": "BIN_FULL"},
                {"name": "CLEAN", "value": 6, "display_name": "CLEAN"},
                {"name": "OFF", "value": 7, "display_name": "OFF"},
                {"name": "SLEEP_MODE", "value": 8, "display_name": "SLEEP_MODE"},
                {"name": "STANDBY", "value": 9, "display_name": "STANDBY"},
                {"name": "SAFE_MODE", "value": 10, "display_name": "SAFE_MODE"},
                {"name": "WATER_OUTAGE", "value": 11, "display_name": "WATER_OUTAGE"},
                {
                    "name": "HPCO_DELAY_ACTIVE",
                    "value": 12,
                    "display_name": "HPCO_DELAY_ACTIVE",
                },
                {"name": "CURTAIN_OPEN", "value": 13, "display_name": "CURTAIN_OPEN"},
                {
                    "name": "PRODUCTION_TEST",
                    "value": 14,
                    "display_name": "PRODUCTION_TEST",
                },
                {
                    "name": "SAFE_MODE_PRECHILL",
                    "value": 15,
                    "display_name": "SAFE_MODE_PRECHILL",
                },
                {
                    "name": "SAFE_MODE_FREEZE",
                    "value": 16,
                    "display_name": "SAFE_MODE_FREEZE",
                },
                {
                    "name": "SAFE_MODE_HARVEST",
                    "value": 17,
                    "display_name": "SAFE_MODE_HARVEST",
                },
                {
                    "name": "SAFE_MODE_FULL_BIN",
                    "value": 18,
                    "display_name": "SAFE_MODE_FULL_BIN",
                },
            ]
        },
    ),
    (
        "ns=1;i=3019",
        "TrayModeEnumeration",
        {
            "fields": [
                {"name": "Off", "value": 0, "display_name": "Off"},
                {"name": "PreHeat", "value": 1, "display_name": "PreHeat"},
                {"name": "PreCool", "value": 2, "display_name": "PreCool"},
                {"name": "HoldWarm", "value": 3, "display_name": "HoldWarm"},
                {"name": "HoldCool", "value": 4, "display_name": "HoldCool"},
                {"name": "Regenerating", "value": 5, "display_name": "Regenerating"},
            ]
        },
    ),
    (
        "ns=1;i=3020",
        "TrayTypeEnumeration",
        {
            "fields": [
                {"name": "Generic", "value": 0, "display_name": "Generic"},
                {"name": "HeaterPlate", "value": 1, "display_name": "HeaterPlate"},
                {"name": "CoolingPlate", "value": 2, "display_name": "CoolingPlate"},
                {"name": "CombiPlate", "value": 3, "display_name": "CombiPlate"},
                {"name": "BainMarie", "value": 4, "display_name": "BainMarie"},
                {"name": "HeaterCabinet", "value": 5, "display_name": "HeaterCabinet"},
                {
                    "name": "CoolingCabinet",
                    "value": 6,
                    "display_name": "CoolingCabinet",
                },
                {"name": "HeatBridge", "value": 7, "display_name": "HeatBridge"},
                {"name": "CombiCabinet", "value": 8, "display_name": "CombiCabinet"},
                {"name": "RegenCabinet", "value": 9, "display_name": "RegenCabinet"},
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = (
    [],
    [
        "ns=1;i=3014",
        "ns=1;i=3008",
        "ns=1;i=3015",
        "ns=1;i=3006",
        "ns=1;i=3010",
        "ns=1;i=3021",
        "ns=1;i=3002",
        "ns=1;i=3003",
        "ns=1;i=3005",
        "ns=1;i=3025",
        "ns=1;i=3017",
        "ns=1;i=3011",
        "ns=1;i=3023",
        "ns=1;i=3018",
        "ns=1;i=3013",
        "ns=1;i=3022",
        "ns=1;i=3009",
        "ns=1;i=3016",
        "ns=1;i=3004",
        "ns=1;i=3007",
        "ns=1;i=3012",
        "ns=1;i=3024",
        "ns=1;i=3019",
        "ns=1;i=3020",
    ],
)
_NODES: dict = {
    "datatypes": {
        "BeverageSMLEnumeration": (
            "D",
            "ns=1;i=3014",
            {"EnumStrings": ("V", "ns=1;i=6366", {})},
        ),
        "ChamberModeEnumeration": (
            "D",
            "ns=1;i=3008",
            {"EnumStrings": ("V", "ns=1;i=6020", {})},
        ),
        "CoffeeMachineModeEnumeration": (
            "D",
            "ns=1;i=3015",
            {"EnumStrings": ("V", "ns=1;i=6367", {})},
        ),
        "CombiSteamerModeEnumeration": (
            "D",
            "ns=1;i=3006",
            {"EnumStrings": ("V", "ns=1;i=6168", {})},
        ),
        "CookingKettleModeEnumeration": (
            "D",
            "ns=1;i=3010",
            {"EnumStrings": ("V", "ns=1;i=6102", {})},
        ),
        "CurrentStateEnumeration": (
            "D",
            "ns=1;i=3021",
            {"EnumStrings": ("V", "ns=1;i=6529", {})},
        ),
        "EnergySourceEnumeration": (
            "D",
            "ns=1;i=3002",
            {"EnumStrings": ("V", "ns=1;i=6254", {})},
        ),
        "FryerModeEnumeration": (
            "D",
            "ns=1;i=3003",
            {"EnumStrings": ("V", "ns=1;i=6022", {})},
        ),
        "FryingPanModeEnumeration": (
            "D",
            "ns=1;i=3005",
            {"EnumStrings": ("V", "ns=1;i=6253", {})},
        ),
        "GrillingZoneStateEnumeration": (
            "D",
            "ns=1;i=3025",
            {"EnumStrings": ("V", "ns=1;i=6717", {})},
        ),
        "HygieneModeEnumeration": (
            "D",
            "ns=1;i=3017",
            {"EnumStrings": ("V", "ns=1;i=6444", {})},
        ),
        "MultiFunctionPanModeEnumeration": (
            "D",
            "ns=1;i=3011",
            {"EnumStrings": ("V", "ns=1;i=6286", {})},
        ),
        "OperatingModeEnumeration": (
            "D",
            "ns=1;i=3023",
            {"EnumStrings": ("V", "ns=1;i=6581", {})},
        ),
        "OperationModeEnumeration": (
            "D",
            "ns=1;i=3018",
            {"EnumStrings": ("V", "ns=1;i=6445", {})},
        ),
        "PastaCookerModeEnumeration": (
            "D",
            "ns=1;i=3013",
            {"EnumStrings": ("V", "ns=1;i=6337", {})},
        ),
        "PlatenPositionStateEnumeration": (
            "D",
            "ns=1;i=3022",
            {"EnumStrings": ("V", "ns=1;i=6557", {})},
        ),
        "PressureCookingKettleModeEnumeration": (
            "D",
            "ns=1;i=3009",
            {"EnumStrings": ("V", "ns=1;i=6053", {})},
        ),
        "ProgramModeEnumeration": (
            "D",
            "ns=1;i=3016",
            {"EnumStrings": ("V", "ns=1;i=6443", {})},
        ),
        "SignalModeEnumeration": (
            "D",
            "ns=1;i=3004",
            {"EnumStrings": ("V", "ns=1;i=6206", {})},
        ),
        "SpecialCookingModeEnumeration": (
            "D",
            "ns=1;i=3007",
            {"EnumStrings": ("V", "ns=1;i=6021", {})},
        ),
        "SpecialFunctionModeEnumeration": (
            "D",
            "ns=1;i=3012",
            {"EnumStrings": ("V", "ns=1;i=6287", {})},
        ),
        "StatusEnumeration": (
            "D",
            "ns=1;i=3024",
            {"EnumStrings": ("V", "ns=1;i=6620", {})},
        ),
        "TrayModeEnumeration": (
            "D",
            "ns=1;i=3019",
            {"EnumStrings": ("V", "ns=1;i=6497", {})},
        ),
        "TrayTypeEnumeration": (
            "D",
            "ns=1;i=3020",
            {"EnumStrings": ("V", "ns=1;i=6498", {})},
        ),
    },
    "objects": {
        "TypeDictionary": (
            "V",
            "ns=1;i=6013",
            {"NamespaceUri": ("V", "ns=1;i=6014", {})},
        ),
        "http://opcfoundation.org/UA/CommercialKitchenEquipment/": (
            "O",
            "ns=1;i=5021",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=6707", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=6708", {}),
                "NamespaceUri": ("V", "ns=1;i=6709", {}),
                "NamespaceVersion": ("V", "ns=1;i=6710", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=6711", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=6712", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=6713", {}),
            },
        ),
    },
    "objtypes": {
        "BatchInformationType": (
            "OT",
            "ns=1;i=1002",
            {
                "BatchId": ("V", "ns=1;i=6002", {}),
                "LocalTime": ("V", "ns=1;i=6004", {}),
                "OrderId": ("V", "ns=1;i=6001", {}),
                "SystemTime": ("V", "ns=1;i=6003", {}),
            },
        ),
        "CommercialKitchenDeviceType": (
            "OT",
            "ns=1;i=1005",
            {
                "BatchInformation": (
                    "O",
                    "ns=1;i=5001",
                    {
                        "BatchId": ("V", "ns=1;i=6017", {}),
                        "LocalTime": ("V", "ns=1;i=6018", {}),
                        "OrderId": ("V", "ns=1;i=6019", {}),
                        "SystemTime": ("V", "ns=1;i=6671", {}),
                    },
                ),
                "CoffeeMachineDeviceType": (
                    "OT",
                    "ns=1;i=1024",
                    {
                        "<RecipeName>": (
                            "O",
                            "ns=1;i=5014",
                            {
                                "BeverageSML": ("V", "ns=1;i=6421", {}),
                                "BeverageSize": (
                                    "V",
                                    "ns=1;i=6418",
                                    {
                                        "EURange": ("V", "ns=1;i=6420", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6419", {}),
                                    },
                                ),
                                "CoffeeType": (
                                    "V",
                                    "ns=1;i=6422",
                                    {"EnumStrings": ("V", "ns=1;i=6423", {})},
                                ),
                                "Container": (
                                    "V",
                                    "ns=1;i=6424",
                                    {"EnumStrings": ("V", "ns=1;i=6425", {})},
                                ),
                                "FoamAmount": (
                                    "V",
                                    "ns=1;i=6426",
                                    {
                                        "EURange": ("V", "ns=1;i=6428", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6427", {}),
                                    },
                                ),
                                "GroundsAmount": (
                                    "V",
                                    "ns=1;i=6429",
                                    {
                                        "EURange": ("V", "ns=1;i=6431", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6430", {}),
                                    },
                                ),
                                "GroundsWater": (
                                    "V",
                                    "ns=1;i=6432",
                                    {
                                        "EURange": ("V", "ns=1;i=6434", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6433", {}),
                                    },
                                ),
                                "MilkAmount": (
                                    "V",
                                    "ns=1;i=6435",
                                    {
                                        "EURange": ("V", "ns=1;i=6437", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6436", {}),
                                    },
                                ),
                                "PowderAmount": (
                                    "V",
                                    "ns=1;i=6438",
                                    {
                                        "EURange": ("V", "ns=1;i=6440", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6439", {}),
                                    },
                                ),
                                "RcpType": (
                                    "V",
                                    "ns=1;i=6441",
                                    {"EnumStrings": ("V", "ns=1;i=6442", {})},
                                ),
                            },
                        ),
                        "Parameters": (
                            "O",
                            "ns=1;i=5013",
                            {
                                "BoilerPressureSteam": (
                                    "V",
                                    "ns=1;i=6665",
                                    {"EURange": ("V", "ns=1;i=6668", {})},
                                ),
                                "BoilerPressureWater": (
                                    "V",
                                    "ns=1;i=6409",
                                    {
                                        "EURange": ("V", "ns=1;i=6411", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6410", {}),
                                    },
                                ),
                                "BoilerTempWater": (
                                    "V",
                                    "ns=1;i=6412",
                                    {
                                        "EURange": ("V", "ns=1;i=6414", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6413", {}),
                                    },
                                ),
                                "CurrentState": ("V", "ns=1;i=6415", {}),
                                "SystemClean": ("V", "ns=1;i=6416", {}),
                                "TotalMix": ("V", "ns=1;i=6417", {}),
                            },
                        ),
                    },
                ),
                "CombiSteamerDeviceType": (
                    "OT",
                    "ns=1;i=1011",
                    {
                        "CombiSteamer": (
                            "O",
                            "ns=1;i=5007",
                            {
                                "ActualInternalCoreTemperature_<No.>": (
                                    "V",
                                    "ns=1;i=6151",
                                    {
                                        "EURange": ("V", "ns=1;i=6153", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6152", {}),
                                    },
                                ),
                                "ActualTemperatureChamber_<No.>": (
                                    "V",
                                    "ns=1;i=6154",
                                    {
                                        "EURange": ("V", "ns=1;i=6156", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6155", {}),
                                    },
                                ),
                                "CombiSteamerMode": ("V", "ns=1;i=6157", {}),
                                "IsDoorOpen": ("V", "ns=1;i=6158", {}),
                                "SetProcessTimeProgram": (
                                    "V",
                                    "ns=1;i=6159",
                                    {
                                        "EURange": ("V", "ns=1;i=6161", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6160", {}),
                                    },
                                ),
                                "SetTemperature": (
                                    "V",
                                    "ns=1;i=6162",
                                    {
                                        "EURange": ("V", "ns=1;i=6164", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6163", {}),
                                    },
                                ),
                                "TimeRemainingProgram": (
                                    "V",
                                    "ns=1;i=6165",
                                    {
                                        "EURange": ("V", "ns=1;i=6167", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6166", {}),
                                    },
                                ),
                            },
                        ),
                        "EnergySource": ("V", "ns=1;i=6146", {}),
                        "IsWithAutomaticCleaning": ("V", "ns=1;i=6147", {}),
                        "IsWithExternalCoreTempSensor": ("V", "ns=1;i=6149", {}),
                        "IsWithInternalCoreTempSensor": ("V", "ns=1;i=6148", {}),
                        "IsWithSousvideTempSensor": ("V", "ns=1;i=6150", {}),
                    },
                ),
                "CookingKettleDeviceType": (
                    "OT",
                    "ns=1;i=1017",
                    {
                        "CookingKettle": (
                            "O",
                            "ns=1;i=5010",
                            {
                                "ActualCoreTemperature": (
                                    "V",
                                    "ns=1;i=6271",
                                    {
                                        "EURange": ("V", "ns=1;i=6272", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6658", {}),
                                    },
                                ),
                                "ActualTemperature": (
                                    "V",
                                    "ns=1;i=6273",
                                    {
                                        "EURange": ("V", "ns=1;i=6274", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6661", {}),
                                    },
                                ),
                                "CookingLevel": ("V", "ns=1;i=6275", {}),
                                "ProgramMode": ("V", "ns=1;i=6276", {}),
                                "SetCoreTemperature": (
                                    "V",
                                    "ns=1;i=6277",
                                    {
                                        "EURange": ("V", "ns=1;i=6278", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6664", {}),
                                    },
                                ),
                                "SetProcessTime": (
                                    "V",
                                    "ns=1;i=6279",
                                    {
                                        "EURange": ("V", "ns=1;i=6280", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6667", {}),
                                    },
                                ),
                                "SetTemperature": (
                                    "V",
                                    "ns=1;i=6281",
                                    {
                                        "EURange": ("V", "ns=1;i=6282", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6670", {}),
                                    },
                                ),
                                "SignalMode": ("V", "ns=1;i=6283", {}),
                                "TimeRemaining": (
                                    "V",
                                    "ns=1;i=6284",
                                    {
                                        "EURange": ("V", "ns=1;i=6285", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6673", {}),
                                    },
                                ),
                            },
                        ),
                        "EnergySource": ("V", "ns=1;i=6270", {}),
                        "IsWithAgitator": ("V", "ns=1;i=6268", {}),
                        "IsWithCooling": ("V", "ns=1;i=6269", {}),
                    },
                ),
                "CookingZoneDeviceType": (
                    "OT",
                    "ns=1;i=1030",
                    {
                        "CookingZone_<No.>": (
                            "O",
                            "ns=1;i=5017",
                            {
                                "NominalPower": (
                                    "V",
                                    "ns=1;i=6674",
                                    {
                                        "EURange": ("V", "ns=1;i=6715", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6714", {}),
                                    },
                                )
                            },
                        ),
                        "EnergySource": ("V", "ns=1;i=6552", {}),
                        "IsWithPanDetection": ("V", "ns=1;i=6551", {}),
                        "NominalVoltage": (
                            "V",
                            "ns=1;i=6553",
                            {
                                "EURange": ("V", "ns=1;i=6554", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6556", {}),
                            },
                        ),
                        "NumberOfPhases": ("V", "ns=1;i=6555", {}),
                    },
                ),
                "DeviceClass": ("V", "ns=1;i=6015", {}),
                "DeviceLocationName": ("V", "ns=1;i=6016", {}),
                "DishWashingMachineDeviceType": (
                    "OT",
                    "ns=1;i=1026",
                    {
                        "Parameters": (
                            "O",
                            "ns=1;i=5015",
                            {
                                "ActualFinalRinseTemperatureNo": (
                                    "V",
                                    "ns=1;i=6488",
                                    {},
                                ),
                                "ActualFinalRinseTemperature_<No.>": (
                                    "V",
                                    "ns=1;i=6485",
                                    {
                                        "EURange": ("V", "ns=1;i=6487", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6486", {}),
                                    },
                                ),
                                "ActualMainTankTemperatureNo": ("V", "ns=1;i=6489", {}),
                                "ActualPreTankTemperatureNo": ("V", "ns=1;i=6490", {}),
                                "ActualPumpedFinalRinseTemperatureNo": (
                                    "V",
                                    "ns=1;i=6491",
                                    {},
                                ),
                                "FinalRinseTemperatureSetpointNo": (
                                    "V",
                                    "ns=1;i=6492",
                                    {},
                                ),
                                "MainTankTemperatureSetpointNo": (
                                    "V",
                                    "ns=1;i=6493",
                                    {},
                                ),
                                "OperationMode": ("V", "ns=1;i=6494", {}),
                                "PreTankTemperatureSetpointNo": (
                                    "V",
                                    "ns=1;i=6495",
                                    {},
                                ),
                                "PumpedFinalRinseTemperatureSetpointNo": (
                                    "V",
                                    "ns=1;i=6496",
                                    {},
                                ),
                            },
                        )
                    },
                ),
                "ErrorConditions": ("O", "ns=1;i=5002", {}),
                "FryerDeviceType": (
                    "OT",
                    "ns=1;i=1007",
                    {
                        "EnergySource": ("V", "ns=1;i=6038", {}),
                        "FryerCup_<No.>": (
                            "O",
                            "ns=1;i=5005",
                            {
                                "ActualTemperature": (
                                    "V",
                                    "ns=1;i=6039",
                                    {
                                        "EURange": ("V", "ns=1;i=6041", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6040", {}),
                                    },
                                ),
                                "ProgramMode": ("V", "ns=1;i=6042", {}),
                                "SetProcessTime": (
                                    "V",
                                    "ns=1;i=6043",
                                    {
                                        "EURange": ("V", "ns=1;i=6045", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6044", {}),
                                    },
                                ),
                                "SetTemperature": (
                                    "V",
                                    "ns=1;i=6046",
                                    {
                                        "EURange": ("V", "ns=1;i=6048", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6047", {}),
                                    },
                                ),
                                "SignalMode": ("V", "ns=1;i=6049", {}),
                                "TimeRemaining": (
                                    "V",
                                    "ns=1;i=6050",
                                    {
                                        "EURange": ("V", "ns=1;i=6052", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6051", {}),
                                    },
                                ),
                            },
                        ),
                        "IsWithLift": ("V", "ns=1;i=6037", {}),
                    },
                ),
                "FryingAndGrillingDeviceType": (
                    "OT",
                    "ns=1;i=1032",
                    {
                        "EnergySource": ("V", "ns=1;i=6580", {}),
                        "GrillingZone_<No.>": (
                            "O",
                            "ns=1;i=5018",
                            {"IsWithPlaten": ("V", "ns=1;i=6716", {})},
                        ),
                    },
                ),
                "FryingPanDeviceType": (
                    "OT",
                    "ns=1;i=1009",
                    {
                        "EnergySource": ("V", "ns=1;i=6080", {}),
                        "FryingPan": (
                            "O",
                            "ns=1;i=5006",
                            {
                                "ActualCoreTemperature": (
                                    "V",
                                    "ns=1;i=6081",
                                    {
                                        "EURange": ("V", "ns=1;i=6083", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6082", {}),
                                    },
                                ),
                                "ActualTemperature": (
                                    "V",
                                    "ns=1;i=6084",
                                    {
                                        "EURange": ("V", "ns=1;i=6086", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6085", {}),
                                    },
                                ),
                                "CookingLevel": ("V", "ns=1;i=6087", {}),
                                "ProgramMode": ("V", "ns=1;i=6088", {}),
                                "SetCoreTemperature": (
                                    "V",
                                    "ns=1;i=6089",
                                    {
                                        "EURange": ("V", "ns=1;i=6091", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6090", {}),
                                    },
                                ),
                                "SetProcessTime": (
                                    "V",
                                    "ns=1;i=6092",
                                    {
                                        "EURange": ("V", "ns=1;i=6094", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6093", {}),
                                    },
                                ),
                                "SetTemperature": (
                                    "V",
                                    "ns=1;i=6095",
                                    {
                                        "EURange": ("V", "ns=1;i=6097", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6096", {}),
                                    },
                                ),
                                "SignalMode": ("V", "ns=1;i=6098", {}),
                                "TimeRemaining": (
                                    "V",
                                    "ns=1;i=6099",
                                    {
                                        "EURange": ("V", "ns=1;i=6101", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6100", {}),
                                    },
                                ),
                            },
                        ),
                        "IsWithPressure": ("V", "ns=1;i=6079", {}),
                    },
                ),
                "HACCPValues": ("O", "ns=1;i=5004", {}),
                "IceMachineDeviceType": (
                    "OT",
                    "ns=1;i=1036",
                    {"IceMachine": ("O", "ns=1;i=5020", {})},
                ),
                "InformationConditions": ("O", "ns=1;i=5003", {}),
                "MicrowaveCombiOvenDeviceType": (
                    "OT",
                    "ns=1;i=1034",
                    {
                        "MicrowaveCombiOven": (
                            "O",
                            "ns=1;i=5019",
                            {
                                "ActualTemperatureChamber": (
                                    "V",
                                    "ns=1;i=6606",
                                    {
                                        "EURange": ("V", "ns=1;i=6608", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6607", {}),
                                    },
                                ),
                                "IsDoorOpen": ("V", "ns=1;i=6609", {}),
                                "OperatingMode": ("V", "ns=1;i=6610", {}),
                                "RemainingProcessTime": (
                                    "V",
                                    "ns=1;i=6611",
                                    {
                                        "EURange": ("V", "ns=1;i=6613", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6612", {}),
                                    },
                                ),
                                "SetProcessTime": (
                                    "V",
                                    "ns=1;i=6614",
                                    {
                                        "EURange": ("V", "ns=1;i=6616", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6615", {}),
                                    },
                                ),
                                "SetTemperature": (
                                    "V",
                                    "ns=1;i=6617",
                                    {
                                        "EURange": ("V", "ns=1;i=6619", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6618", {}),
                                    },
                                ),
                            },
                        )
                    },
                ),
                "MultiFunctionPanDeviceType": (
                    "OT",
                    "ns=1;i=1019",
                    {
                        "EnergySource": ("V", "ns=1;i=6321", {}),
                        "MultiFunctionPan_<No.>": (
                            "O",
                            "ns=1;i=5011",
                            {
                                "ActualCoreTemperature": (
                                    "V",
                                    "ns=1;i=6322",
                                    {
                                        "EURange": ("V", "ns=1;i=6323", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6639", {}),
                                    },
                                ),
                                "ActualTemperatureBottom": (
                                    "V",
                                    "ns=1;i=6324",
                                    {
                                        "EURange": ("V", "ns=1;i=6325", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6642", {}),
                                    },
                                ),
                                "ActualTemperatureCup": (
                                    "V",
                                    "ns=1;i=6326",
                                    {
                                        "EURange": ("V", "ns=1;i=6327", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6644", {}),
                                    },
                                ),
                                "MultiFunctionPanMode": ("V", "ns=1;i=6328", {}),
                                "SetCoreTemperature": (
                                    "V",
                                    "ns=1;i=6329",
                                    {
                                        "EURange": ("V", "ns=1;i=6330", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6647", {}),
                                    },
                                ),
                                "SetProcessTimeProgram": (
                                    "V",
                                    "ns=1;i=6331",
                                    {
                                        "EURange": ("V", "ns=1;i=6332", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6649", {}),
                                    },
                                ),
                                "SetTemperature": (
                                    "V",
                                    "ns=1;i=6333",
                                    {
                                        "EURange": ("V", "ns=1;i=6334", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6652", {}),
                                    },
                                ),
                                "TimeRemainingProgram": (
                                    "V",
                                    "ns=1;i=6335",
                                    {
                                        "EURange": ("V", "ns=1;i=6336", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6655", {}),
                                    },
                                ),
                            },
                        ),
                    },
                ),
                "OvenDeviceType": (
                    "OT",
                    "ns=1;i=1013",
                    {
                        "Chamber_<No.>": (
                            "O",
                            "ns=1;i=5008",
                            {"OperationMode": ("V", "ns=1;i=6205", {})},
                        )
                    },
                ),
                "PastaCookerDeviceType": (
                    "OT",
                    "ns=1;i=1021",
                    {
                        "EnergySource": ("V", "ns=1;i=6350", {}),
                        "IsWithLift": ("V", "ns=1;i=6349", {}),
                        "PastaCooker": (
                            "O",
                            "ns=1;i=5012",
                            {
                                "ActualTemperature": (
                                    "V",
                                    "ns=1;i=6351",
                                    {
                                        "EURange": ("V", "ns=1;i=6353", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6352", {}),
                                    },
                                ),
                                "CookingLevel": ("V", "ns=1;i=6354", {}),
                                "ProgramMode": ("V", "ns=1;i=6355", {}),
                                "SetProcessTime": (
                                    "V",
                                    "ns=1;i=6356",
                                    {
                                        "EURange": ("V", "ns=1;i=6358", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6357", {}),
                                    },
                                ),
                                "SetTemperature": (
                                    "V",
                                    "ns=1;i=6359",
                                    {
                                        "EURange": ("V", "ns=1;i=6361", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6360", {}),
                                    },
                                ),
                                "SignalMode": ("V", "ns=1;i=6362", {}),
                                "TimeRemaining": (
                                    "V",
                                    "ns=1;i=6363",
                                    {
                                        "EURange": ("V", "ns=1;i=6365", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6364", {}),
                                    },
                                ),
                            },
                        ),
                    },
                ),
                "PressureCookingKettleDeviceType": (
                    "OT",
                    "ns=1;i=1015",
                    {
                        "EnergySource": ("V", "ns=1;i=6229", {}),
                        "PressureCookingKettle": (
                            "O",
                            "ns=1;i=5009",
                            {
                                "ActualCoreTemperature": (
                                    "V",
                                    "ns=1;i=6230",
                                    {
                                        "EURange": ("V", "ns=1;i=6231", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6676", {}),
                                    },
                                ),
                                "ActualPressureAbsolute": (
                                    "V",
                                    "ns=1;i=6232",
                                    {
                                        "EURange": ("V", "ns=1;i=6233", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6678", {}),
                                    },
                                ),
                                "ActualPressureKettle": (
                                    "V",
                                    "ns=1;i=6234",
                                    {
                                        "EURange": ("V", "ns=1;i=6235", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6680", {}),
                                    },
                                ),
                                "ActualTemperature": (
                                    "V",
                                    "ns=1;i=6236",
                                    {
                                        "EURange": ("V", "ns=1;i=6237", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6682", {}),
                                    },
                                ),
                                "CookingLevel": ("V", "ns=1;i=6238", {}),
                                "IsLidLocked": ("V", "ns=1;i=6239", {}),
                                "IsOpenExpressActive": ("V", "ns=1;i=6240", {}),
                                "IsSteamActive": ("V", "ns=1;i=6241", {}),
                                "ProgramMode": ("V", "ns=1;i=6242", {}),
                                "SetCoreTemperature": (
                                    "V",
                                    "ns=1;i=6243",
                                    {
                                        "EURange": ("V", "ns=1;i=6244", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6684", {}),
                                    },
                                ),
                                "SetProcessTime": (
                                    "V",
                                    "ns=1;i=6245",
                                    {
                                        "EURange": ("V", "ns=1;i=6246", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6686", {}),
                                    },
                                ),
                                "SetTemperature": (
                                    "V",
                                    "ns=1;i=6247",
                                    {
                                        "EURange": ("V", "ns=1;i=6248", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6688", {}),
                                    },
                                ),
                                "SignalMode": ("V", "ns=1;i=6249", {}),
                                "TimeRemaining": (
                                    "V",
                                    "ns=1;i=6250",
                                    {
                                        "EURange": ("V", "ns=1;i=6251", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6690", {}),
                                    },
                                ),
                            },
                        ),
                    },
                ),
                "ServeryCounterDeviceType": (
                    "OT",
                    "ns=1;i=1028",
                    {
                        "Tray_<No.>": (
                            "O",
                            "ns=1;i=5016",
                            {
                                "ActiveSince": (
                                    "V",
                                    "ns=1;i=6514",
                                    {
                                        "EURange": ("V", "ns=1;i=6516", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6515", {}),
                                    },
                                ),
                                "ActualTemperature": (
                                    "V",
                                    "ns=1;i=6517",
                                    {
                                        "EURange": ("V", "ns=1;i=6519", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6518", {}),
                                    },
                                ),
                                "Name": ("V", "ns=1;i=6520", {}),
                                "OperatingCounter": (
                                    "V",
                                    "ns=1;i=6521",
                                    {
                                        "EURange": ("V", "ns=1;i=6523", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6522", {}),
                                    },
                                ),
                                "ProgramMode": ("V", "ns=1;i=6524", {}),
                                "SetTemperature": (
                                    "V",
                                    "ns=1;i=6525",
                                    {
                                        "EURange": ("V", "ns=1;i=6527", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=6526", {}),
                                    },
                                ),
                                "Type": ("V", "ns=1;i=6528", {}),
                            },
                        )
                    },
                ),
            },
        ),
        "KitchenDeviceHAConfigType": (
            "OT",
            "ns=1;i=1003",
            {
                "HistoryDuration": ("V", "ns=1;i=6005", {}),
                "SamplingInterval": ("V", "ns=1;i=6006", {}),
            },
        ),
        "KitchenDeviceParameterType": (
            "OT",
            "ns=1;i=1004",
            {
                "ChamberType": (
                    "OT",
                    "ns=1;i=1012",
                    {
                        "ActualBoilerTemperature_<No.>": (
                            "V",
                            "ns=1;i=6192",
                            {
                                "EURange": ("V", "ns=1;i=6193", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6691", {}),
                            },
                        ),
                        "ActualBottomTemperature_<No.>": (
                            "V",
                            "ns=1;i=6188",
                            {
                                "EURange": ("V", "ns=1;i=6189", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6692", {}),
                            },
                        ),
                        "ActualChamberTemperature_<No.>": (
                            "V",
                            "ns=1;i=6182",
                            {
                                "EURange": ("V", "ns=1;i=6183", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6693", {}),
                            },
                        ),
                        "ActualCoreTemperature_<No.>": (
                            "V",
                            "ns=1;i=6190",
                            {
                                "EURange": ("V", "ns=1;i=6191", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6694", {}),
                            },
                        ),
                        "ActualFanSpeed_<No.>": (
                            "V",
                            "ns=1;i=6201",
                            {
                                "EURange": ("V", "ns=1;i=6202", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6695", {}),
                            },
                        ),
                        "ActualHumidity_<No.>": (
                            "V",
                            "ns=1;i=6196",
                            {
                                "EURange": ("V", "ns=1;i=6197", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6696", {}),
                            },
                        ),
                        "ActualTopTemperature_<No.>": (
                            "V",
                            "ns=1;i=6186",
                            {
                                "EURange": ("V", "ns=1;i=6187", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6697", {}),
                            },
                        ),
                        "IsDoorOpen": ("V", "ns=1;i=6200", {}),
                        "IsProgramEnd": ("V", "ns=1;i=6199", {}),
                        "IsReadyToStart": ("V", "ns=1;i=6198", {}),
                        "OperationMode": ("V", "ns=1;i=6169", {}),
                        "SetBoilerTemperature": (
                            "V",
                            "ns=1;i=6180",
                            {
                                "EURange": ("V", "ns=1;i=6181", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6698", {}),
                            },
                        ),
                        "SetBottomTemperature": (
                            "V",
                            "ns=1;i=6176",
                            {
                                "EURange": ("V", "ns=1;i=6177", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6699", {}),
                            },
                        ),
                        "SetChamberTemperature": (
                            "V",
                            "ns=1;i=6172",
                            {
                                "EURange": ("V", "ns=1;i=6173", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6700", {}),
                            },
                        ),
                        "SetCoreTemperature": (
                            "V",
                            "ns=1;i=6178",
                            {
                                "EURange": ("V", "ns=1;i=6179", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6701", {}),
                            },
                        ),
                        "SetFanSpeed": (
                            "V",
                            "ns=1;i=6203",
                            {
                                "EURange": ("V", "ns=1;i=6204", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6702", {}),
                            },
                        ),
                        "SetHumidity": (
                            "V",
                            "ns=1;i=6194",
                            {
                                "EURange": ("V", "ns=1;i=6195", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6703", {}),
                            },
                        ),
                        "SetProcessTimeProgram": (
                            "V",
                            "ns=1;i=6184",
                            {
                                "EURange": ("V", "ns=1;i=6185", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6704", {}),
                            },
                        ),
                        "SetTopTemperature": (
                            "V",
                            "ns=1;i=6174",
                            {
                                "EURange": ("V", "ns=1;i=6175", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6705", {}),
                            },
                        ),
                        "TimeRemaining": (
                            "V",
                            "ns=1;i=6170",
                            {
                                "EURange": ("V", "ns=1;i=6171", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6706", {}),
                            },
                        ),
                    },
                ),
                "CoffeeMachineParameterType": (
                    "OT",
                    "ns=1;i=1022",
                    {
                        "BoilerPressureSteam": (
                            "V",
                            "ns=1;i=6659",
                            {"EURange": ("V", "ns=1;i=6662", {})},
                        ),
                        "BoilerPressureWater": (
                            "V",
                            "ns=1;i=6369",
                            {
                                "EURange": ("V", "ns=1;i=6370", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6380", {}),
                            },
                        ),
                        "BoilerTempSteam": (
                            "V",
                            "ns=1;i=6373",
                            {
                                "EURange": ("V", "ns=1;i=6374", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6381", {}),
                            },
                        ),
                        "BoilerTempWater": (
                            "V",
                            "ns=1;i=6371",
                            {
                                "EURange": ("V", "ns=1;i=6372", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6382", {}),
                            },
                        ),
                        "CurrentState": ("V", "ns=1;i=6368", {}),
                        "GrinderRuntime_<No.>": (
                            "V",
                            "ns=1;i=6378",
                            {
                                "EURange": ("V", "ns=1;i=6379", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6383", {}),
                            },
                        ),
                        "SystemClean": ("V", "ns=1;i=6375", {}),
                        "TotalBrew_<No.>": ("V", "ns=1;i=6376", {}),
                        "TotalMix": ("V", "ns=1;i=6377", {}),
                    },
                ),
                "CoffeeMachineRecipeParameterType": (
                    "OT",
                    "ns=1;i=1023",
                    {
                        "BeverageSML": ("V", "ns=1;i=6386", {}),
                        "BeverageSize": (
                            "V",
                            "ns=1;i=6384",
                            {
                                "EURange": ("V", "ns=1;i=6385", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6403", {}),
                            },
                        ),
                        "CoffeeType": (
                            "V",
                            "ns=1;i=6393",
                            {"EnumStrings": ("V", "ns=1;i=6394", {})},
                        ),
                        "Container": (
                            "V",
                            "ns=1;i=6391",
                            {"EnumStrings": ("V", "ns=1;i=6392", {})},
                        ),
                        "FoamAmount": (
                            "V",
                            "ns=1;i=6399",
                            {
                                "EURange": ("V", "ns=1;i=6400", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6404", {}),
                            },
                        ),
                        "GroundsAmount": (
                            "V",
                            "ns=1;i=6387",
                            {
                                "EURange": ("V", "ns=1;i=6388", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6405", {}),
                            },
                        ),
                        "GroundsWater": (
                            "V",
                            "ns=1;i=6389",
                            {
                                "EURange": ("V", "ns=1;i=6390", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6406", {}),
                            },
                        ),
                        "MilkAmount": (
                            "V",
                            "ns=1;i=6397",
                            {
                                "EURange": ("V", "ns=1;i=6398", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6407", {}),
                            },
                        ),
                        "PowderAmount": (
                            "V",
                            "ns=1;i=6401",
                            {
                                "EURange": ("V", "ns=1;i=6402", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6408", {}),
                            },
                        ),
                        "RcpType": (
                            "V",
                            "ns=1;i=6395",
                            {"EnumStrings": ("V", "ns=1;i=6396", {})},
                        ),
                    },
                ),
                "CombiSteamerParameterType": (
                    "OT",
                    "ns=1;i=1010",
                    {
                        "ActualExternalCoreTemperature_<No.>": (
                            "V",
                            "ns=1;i=6119",
                            {
                                "EURange": ("V", "ns=1;i=6120", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6134", {}),
                            },
                        ),
                        "ActualHumidity": (
                            "V",
                            "ns=1;i=6128",
                            {
                                "EURange": ("V", "ns=1;i=6129", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6135", {}),
                            },
                        ),
                        "ActualInternalCoreTemperature_<No.>": (
                            "V",
                            "ns=1;i=6115",
                            {
                                "EURange": ("V", "ns=1;i=6116", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6136", {}),
                            },
                        ),
                        "ActualTemperatureChamber_<No.>": (
                            "V",
                            "ns=1;i=6107",
                            {
                                "EURange": ("V", "ns=1;i=6108", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6137", {}),
                            },
                        ),
                        "CombiSteamerMode": ("V", "ns=1;i=6104", {}),
                        "IsDoorOpen": ("V", "ns=1;i=6130", {}),
                        "IsEnergySavingActive": ("V", "ns=1;i=6131", {}),
                        "IsLoaActive": ("V", "ns=1;i=6133", {}),
                        "IsSteamExhaustSystemActive": ("V", "ns=1;i=6132", {}),
                        "SetExternalCoreTemperature": (
                            "V",
                            "ns=1;i=6117",
                            {
                                "EURange": ("V", "ns=1;i=6118", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6138", {}),
                            },
                        ),
                        "SetHumidity": (
                            "V",
                            "ns=1;i=6126",
                            {
                                "EURange": ("V", "ns=1;i=6127", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6139", {}),
                            },
                        ),
                        "SetInternalCoreTemperature": (
                            "V",
                            "ns=1;i=6113",
                            {
                                "EURange": ("V", "ns=1;i=6114", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6140", {}),
                            },
                        ),
                        "SetProcessTimeProgram": (
                            "V",
                            "ns=1;i=6109",
                            {
                                "EURange": ("V", "ns=1;i=6110", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6141", {}),
                            },
                        ),
                        "SetProcessTimeStep": (
                            "V",
                            "ns=1;i=6122",
                            {
                                "EURange": ("V", "ns=1;i=6123", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6142", {}),
                            },
                        ),
                        "SetTemperature": (
                            "V",
                            "ns=1;i=6105",
                            {
                                "EURange": ("V", "ns=1;i=6106", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6143", {}),
                            },
                        ),
                        "SpecialCookingMode": ("V", "ns=1;i=6121", {}),
                        "TimeRemainingProgram": (
                            "V",
                            "ns=1;i=6111",
                            {
                                "EURange": ("V", "ns=1;i=6112", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6144", {}),
                            },
                        ),
                        "TimeRemainingStep": (
                            "V",
                            "ns=1;i=6124",
                            {
                                "EURange": ("V", "ns=1;i=6125", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6145", {}),
                            },
                        ),
                    },
                ),
                "CookingKettleParameterType": (
                    "OT",
                    "ns=1;i=1016",
                    {
                        "ActualCoreTemperature": (
                            "V",
                            "ns=1;i=6265",
                            {
                                "EURange": ("V", "ns=1;i=6266", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6657", {}),
                            },
                        ),
                        "ActualTemperature": (
                            "V",
                            "ns=1;i=6257",
                            {
                                "EURange": ("V", "ns=1;i=6258", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6660", {}),
                            },
                        ),
                        "CookingLevel": ("V", "ns=1;i=6252", {}),
                        "ProgramMode": ("V", "ns=1;i=6103", {}),
                        "SetCoreTemperature": (
                            "V",
                            "ns=1;i=6263",
                            {
                                "EURange": ("V", "ns=1;i=6264", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6663", {}),
                            },
                        ),
                        "SetProcessTime": (
                            "V",
                            "ns=1;i=6259",
                            {
                                "EURange": ("V", "ns=1;i=6260", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6666", {}),
                            },
                        ),
                        "SetTemperature": (
                            "V",
                            "ns=1;i=6255",
                            {
                                "EURange": ("V", "ns=1;i=6256", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6669", {}),
                            },
                        ),
                        "SignalMode": ("V", "ns=1;i=6267", {}),
                        "TimeRemaining": (
                            "V",
                            "ns=1;i=6261",
                            {
                                "EURange": ("V", "ns=1;i=6262", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6672", {}),
                            },
                        ),
                    },
                ),
                "CookingZoneParameterType": (
                    "OT",
                    "ns=1;i=1029",
                    {
                        "ActualPower": (
                            "V",
                            "ns=1;i=6540",
                            {
                                "EURange": ("V", "ns=1;i=6541", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6545", {}),
                            },
                        ),
                        "ActualProcessTime": (
                            "V",
                            "ns=1;i=6536",
                            {
                                "EURange": ("V", "ns=1;i=6537", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6546", {}),
                            },
                        ),
                        "ActualTemperature": (
                            "V",
                            "ns=1;i=6532",
                            {
                                "EURange": ("V", "ns=1;i=6533", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6547", {}),
                            },
                        ),
                        "CookingZoneName": ("V", "ns=1;i=6531", {}),
                        "CurrentState": ("V", "ns=1;i=6530", {}),
                        "IsPanDetected": ("V", "ns=1;i=6542", {}),
                        "NominalPower": (
                            "V",
                            "ns=1;i=6543",
                            {
                                "EURange": ("V", "ns=1;i=6544", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6548", {}),
                            },
                        ),
                        "SetPowerValue": (
                            "V",
                            "ns=1;i=6538",
                            {
                                "EURange": ("V", "ns=1;i=6539", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6549", {}),
                            },
                        ),
                        "SetTemperature": (
                            "V",
                            "ns=1;i=6534",
                            {
                                "EURange": ("V", "ns=1;i=6535", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6550", {}),
                            },
                        ),
                    },
                ),
                "DishWashingMachineProgramParameterType": (
                    "OT",
                    "ns=1;i=1025",
                    {
                        "ActualFinalRinseTemperatureNo": ("V", "ns=1;i=6469", {}),
                        "ActualFinalRinseTemperature_<No.>": (
                            "V",
                            "ns=1;i=6470",
                            {
                                "EURange": ("V", "ns=1;i=6471", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6477", {}),
                            },
                        ),
                        "ActualHygieneValue": ("V", "ns=1;i=6473", {}),
                        "ActualMainTankTemperatureNo": ("V", "ns=1;i=6463", {}),
                        "ActualMainTankTemperature_<No.>": (
                            "V",
                            "ns=1;i=6464",
                            {
                                "EURange": ("V", "ns=1;i=6465", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6478", {}),
                            },
                        ),
                        "ActualPreTankTemperatureNo": ("V", "ns=1;i=6460", {}),
                        "ActualPreTankTemperature_<No.>": (
                            "V",
                            "ns=1;i=6461",
                            {
                                "EURange": ("V", "ns=1;i=6462", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6479", {}),
                            },
                        ),
                        "ActualPumpedFinalRinseTemperatureNo": ("V", "ns=1;i=6466", {}),
                        "ActualPumpedFinalRinseTemperature_<No.>": (
                            "V",
                            "ns=1;i=6467",
                            {
                                "EURange": ("V", "ns=1;i=6468", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6480", {}),
                            },
                        ),
                        "FinalRinseTemperatureSetpointNo": ("V", "ns=1;i=6457", {}),
                        "FinalRinseTemperatureSetpoint_<No.>": (
                            "V",
                            "ns=1;i=6458",
                            {
                                "EURange": ("V", "ns=1;i=6459", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6481", {}),
                            },
                        ),
                        "HygieneMode": ("V", "ns=1;i=6475", {}),
                        "HygieneSetpoint": ("V", "ns=1;i=6472", {}),
                        "MainTankTemperatureSetpointNo": ("V", "ns=1;i=6451", {}),
                        "MainTankTemperatureSetpoint_<No.>": (
                            "V",
                            "ns=1;i=6452",
                            {
                                "EURange": ("V", "ns=1;i=6453", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6482", {}),
                            },
                        ),
                        "OperationMode": ("V", "ns=1;i=6476", {}),
                        "PreTankTemperatureSetpointNo": ("V", "ns=1;i=6448", {}),
                        "PreTankTemperatureSetpoint_<No.>": (
                            "V",
                            "ns=1;i=6449",
                            {
                                "EURange": ("V", "ns=1;i=6450", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6483", {}),
                            },
                        ),
                        "ProductGroup": ("V", "ns=1;i=6446", {}),
                        "ProductType": ("V", "ns=1;i=6447", {}),
                        "ProgramMode": ("V", "ns=1;i=6474", {}),
                        "PumpedFinalRinseTemperatureSetpointNo": (
                            "V",
                            "ns=1;i=6454",
                            {},
                        ),
                        "PumpedFinalRinseTemperatureSetpoint_<No.>": (
                            "V",
                            "ns=1;i=6455",
                            {
                                "EURange": ("V", "ns=1;i=6456", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6484", {}),
                            },
                        ),
                    },
                ),
                "FryerParameterType": (
                    "OT",
                    "ns=1;i=1006",
                    {
                        "ActualTemperature": (
                            "V",
                            "ns=1;i=6025",
                            {
                                "EURange": ("V", "ns=1;i=6026", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6033", {}),
                            },
                        ),
                        "IsLiftUp": ("V", "ns=1;i=6032", {}),
                        "ProgramMode": ("V", "ns=1;i=6010", {}),
                        "SetProcessTime": (
                            "V",
                            "ns=1;i=6027",
                            {
                                "EURange": ("V", "ns=1;i=6028", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6035", {}),
                            },
                        ),
                        "SetTemperature": (
                            "V",
                            "ns=1;i=6023",
                            {
                                "EURange": ("V", "ns=1;i=6024", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6034", {}),
                            },
                        ),
                        "SignalMode": ("V", "ns=1;i=6031", {}),
                        "TimeRemaining": (
                            "V",
                            "ns=1;i=6029",
                            {
                                "EURange": ("V", "ns=1;i=6030", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6036", {}),
                            },
                        ),
                    },
                ),
                "FryingAndGrillingParameterType": (
                    "OT",
                    "ns=1;i=1031",
                    {
                        "ActualGrillTemperature_<No.>": (
                            "V",
                            "ns=1;i=6560",
                            {
                                "EURange": ("V", "ns=1;i=6561", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6574", {}),
                            },
                        ),
                        "ActualPlatenTemperature_<No.>": (
                            "V",
                            "ns=1;i=6564",
                            {
                                "EURange": ("V", "ns=1;i=6565", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6575", {}),
                            },
                        ),
                        "CurrentState": ("V", "ns=1;i=6558", {}),
                        "GrillingZoneName": ("V", "ns=1;i=6559", {}),
                        "IsWithPlaten": ("V", "ns=1;i=6573", {}),
                        "PlatenPositionState": ("V", "ns=1;i=6572", {}),
                        "RemainingProcessTime": (
                            "V",
                            "ns=1;i=6570",
                            {
                                "EURange": ("V", "ns=1;i=6571", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6576", {}),
                            },
                        ),
                        "SetGrillTemperature_<No.>": (
                            "V",
                            "ns=1;i=6562",
                            {
                                "EURange": ("V", "ns=1;i=6563", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6577", {}),
                            },
                        ),
                        "SetPlatenTemperature_<No.>": (
                            "V",
                            "ns=1;i=6566",
                            {
                                "EURange": ("V", "ns=1;i=6567", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6578", {}),
                            },
                        ),
                        "SetProcessTime": (
                            "V",
                            "ns=1;i=6568",
                            {
                                "EURange": ("V", "ns=1;i=6569", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6579", {}),
                            },
                        ),
                    },
                ),
                "FryingPanParameterType": (
                    "OT",
                    "ns=1;i=1008",
                    {
                        "ActualCoreTemperature": (
                            "V",
                            "ns=1;i=6067",
                            {
                                "EURange": ("V", "ns=1;i=6068", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6073", {}),
                            },
                        ),
                        "ActualPressurePan": (
                            "V",
                            "ns=1;i=6070",
                            {
                                "EURange": ("V", "ns=1;i=6071", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6074", {}),
                            },
                        ),
                        "ActualTemperature": (
                            "V",
                            "ns=1;i=6058",
                            {
                                "EURange": ("V", "ns=1;i=6059", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6075", {}),
                            },
                        ),
                        "CookingLevel": ("V", "ns=1;i=6055", {}),
                        "IsLidLocked": ("V", "ns=1;i=6072", {}),
                        "ProgramMode": ("V", "ns=1;i=6054", {}),
                        "SetCoreTemperature": (
                            "V",
                            "ns=1;i=6064",
                            {
                                "EURange": ("V", "ns=1;i=6065", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6066", {}),
                            },
                        ),
                        "SetProcessTime": (
                            "V",
                            "ns=1;i=6060",
                            {
                                "EURange": ("V", "ns=1;i=6061", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6076", {}),
                            },
                        ),
                        "SetTemperature": (
                            "V",
                            "ns=1;i=6056",
                            {
                                "EURange": ("V", "ns=1;i=6057", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6077", {}),
                            },
                        ),
                        "SignalMode": ("V", "ns=1;i=6069", {}),
                        "TimeRemaining": (
                            "V",
                            "ns=1;i=6062",
                            {
                                "EURange": ("V", "ns=1;i=6063", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6078", {}),
                            },
                        ),
                    },
                ),
                "IceMachineParameterType": (
                    "OT",
                    "ns=1;i=1035",
                    {
                        "LastFreezeTime": (
                            "V",
                            "ns=1;i=6622",
                            {
                                "EURange": ("V", "ns=1;i=6623", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6630", {}),
                            },
                        ),
                        "LastHarvestTime": (
                            "V",
                            "ns=1;i=6624",
                            {
                                "EURange": ("V", "ns=1;i=6625", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6631", {}),
                            },
                        ),
                        "Status": ("V", "ns=1;i=6621", {}),
                        "Temperature_<No.>": (
                            "V",
                            "ns=1;i=6628",
                            {
                                "EURange": ("V", "ns=1;i=6629", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6632", {}),
                            },
                        ),
                        "WaterFillTime": (
                            "V",
                            "ns=1;i=6626",
                            {
                                "EURange": ("V", "ns=1;i=6627", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6633", {}),
                            },
                        ),
                    },
                ),
                "MicrowaveCombiOvenParameterType": (
                    "OT",
                    "ns=1;i=1033",
                    {
                        "ActualTemperatureChamber": (
                            "V",
                            "ns=1;i=6582",
                            {
                                "EURange": ("V", "ns=1;i=6583", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6599", {}),
                            },
                        ),
                        "CookingStep": ("V", "ns=1;i=6592", {}),
                        "FanSpeed": (
                            "V",
                            "ns=1;i=6593",
                            {
                                "EURange": ("V", "ns=1;i=6594", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6600", {}),
                            },
                        ),
                        "IsDoorOpen": ("V", "ns=1;i=6598", {}),
                        "MicrowaveEnergy": (
                            "V",
                            "ns=1;i=6595",
                            {
                                "EURange": ("V", "ns=1;i=6596", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6601", {}),
                            },
                        ),
                        "OperatingMode": ("V", "ns=1;i=6597", {}),
                        "RemainingProcessTime": (
                            "V",
                            "ns=1;i=6588",
                            {
                                "EURange": ("V", "ns=1;i=6589", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6602", {}),
                            },
                        ),
                        "RemainingProcessTimeStep": (
                            "V",
                            "ns=1;i=6590",
                            {
                                "EURange": ("V", "ns=1;i=6591", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6603", {}),
                            },
                        ),
                        "SetProcessTime": (
                            "V",
                            "ns=1;i=6586",
                            {
                                "EURange": ("V", "ns=1;i=6587", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6604", {}),
                            },
                        ),
                        "SetTemperature": (
                            "V",
                            "ns=1;i=6584",
                            {
                                "EURange": ("V", "ns=1;i=6585", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6605", {}),
                            },
                        ),
                    },
                ),
                "MultiFunctionPanParameterType": (
                    "OT",
                    "ns=1;i=1018",
                    {
                        "ActualCoreTemperature": (
                            "V",
                            "ns=1;i=6303",
                            {
                                "EURange": ("V", "ns=1;i=6304", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6638", {}),
                            },
                        ),
                        "ActualPressureAbsolute": (
                            "V",
                            "ns=1;i=6305",
                            {
                                "EURange": ("V", "ns=1;i=6306", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6640", {}),
                            },
                        ),
                        "ActualTemperatureBottom": (
                            "V",
                            "ns=1;i=6293",
                            {
                                "EURange": ("V", "ns=1;i=6294", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6641", {}),
                            },
                        ),
                        "ActualTemperatureCup": (
                            "V",
                            "ns=1;i=6295",
                            {
                                "EURange": ("V", "ns=1;i=6296", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6643", {}),
                            },
                        ),
                        "ActualZoneTemperature_<No.>": (
                            "V",
                            "ns=1;i=6313",
                            {
                                "EURange": ("V", "ns=1;i=6314", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6645", {}),
                            },
                        ),
                        "CookingLevel": ("V", "ns=1;i=6290", {}),
                        "IsLidLocked": ("V", "ns=1;i=6315", {}),
                        "IsLidOpen": ("V", "ns=1;i=6316", {}),
                        "IsWithCleaning": ("V", "ns=1;i=6319", {}),
                        "IsWithLift": ("V", "ns=1;i=6320", {}),
                        "IsWithPressure": ("V", "ns=1;i=6317", {}),
                        "IsWithTilting": ("V", "ns=1;i=6318", {}),
                        "MultiFunctionPanMode": ("V", "ns=1;i=6288", {}),
                        "SetCoreTemperature": (
                            "V",
                            "ns=1;i=6301",
                            {
                                "EURange": ("V", "ns=1;i=6302", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6646", {}),
                            },
                        ),
                        "SetProcessTimeProgram": (
                            "V",
                            "ns=1;i=6297",
                            {
                                "EURange": ("V", "ns=1;i=6298", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6648", {}),
                            },
                        ),
                        "SetProcessTimeStep": (
                            "V",
                            "ns=1;i=6307",
                            {
                                "EURange": ("V", "ns=1;i=6308", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6650", {}),
                            },
                        ),
                        "SetTemperature": (
                            "V",
                            "ns=1;i=6291",
                            {
                                "EURange": ("V", "ns=1;i=6292", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6651", {}),
                            },
                        ),
                        "SetZoneTemperature_<No.>": (
                            "V",
                            "ns=1;i=6311",
                            {
                                "EURange": ("V", "ns=1;i=6312", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6653", {}),
                            },
                        ),
                        "SpecialFunctionMode": ("V", "ns=1;i=6289", {}),
                        "TimeRemainingProgram": (
                            "V",
                            "ns=1;i=6299",
                            {
                                "EURange": ("V", "ns=1;i=6300", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6654", {}),
                            },
                        ),
                        "TimeRemainingStep": (
                            "V",
                            "ns=1;i=6309",
                            {
                                "EURange": ("V", "ns=1;i=6310", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6656", {}),
                            },
                        ),
                    },
                ),
                "PastaCookerParameterType": (
                    "OT",
                    "ns=1;i=1020",
                    {
                        "ActualTemperature": (
                            "V",
                            "ns=1;i=6342",
                            {
                                "EURange": ("V", "ns=1;i=6343", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6634", {}),
                            },
                        ),
                        "CookingLevel": ("V", "ns=1;i=6339", {}),
                        "ProgramMode": ("V", "ns=1;i=6338", {}),
                        "SetProcessTime": (
                            "V",
                            "ns=1;i=6344",
                            {
                                "EURange": ("V", "ns=1;i=6345", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6635", {}),
                            },
                        ),
                        "SetTemperature": (
                            "V",
                            "ns=1;i=6340",
                            {
                                "EURange": ("V", "ns=1;i=6341", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6636", {}),
                            },
                        ),
                        "SignalMode": ("V", "ns=1;i=6348", {}),
                        "TimeRemaining": (
                            "V",
                            "ns=1;i=6346",
                            {
                                "EURange": ("V", "ns=1;i=6347", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6637", {}),
                            },
                        ),
                    },
                ),
                "PressureCookingKettleParameterType": (
                    "OT",
                    "ns=1;i=1014",
                    {
                        "ActualCoreTemperature": (
                            "V",
                            "ns=1;i=6219",
                            {
                                "EURange": ("V", "ns=1;i=6220", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6675", {}),
                            },
                        ),
                        "ActualPressureAbsolute": (
                            "V",
                            "ns=1;i=6221",
                            {
                                "EURange": ("V", "ns=1;i=6222", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6677", {}),
                            },
                        ),
                        "ActualPressureKettle": (
                            "V",
                            "ns=1;i=6223",
                            {
                                "EURange": ("V", "ns=1;i=6224", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6679", {}),
                            },
                        ),
                        "ActualTemperature": (
                            "V",
                            "ns=1;i=6211",
                            {
                                "EURange": ("V", "ns=1;i=6212", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6681", {}),
                            },
                        ),
                        "CookingLevel": ("V", "ns=1;i=6208", {}),
                        "IsLidLocked": ("V", "ns=1;i=6226", {}),
                        "IsOpenExpressActive": ("V", "ns=1;i=6228", {}),
                        "IsSteamActive": ("V", "ns=1;i=6227", {}),
                        "ProgramMode": ("V", "ns=1;i=6207", {}),
                        "SetCoreTemperature": (
                            "V",
                            "ns=1;i=6217",
                            {
                                "EURange": ("V", "ns=1;i=6218", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6683", {}),
                            },
                        ),
                        "SetProcessTime": (
                            "V",
                            "ns=1;i=6213",
                            {
                                "EURange": ("V", "ns=1;i=6214", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6685", {}),
                            },
                        ),
                        "SetTemperature": (
                            "V",
                            "ns=1;i=6209",
                            {
                                "EURange": ("V", "ns=1;i=6210", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6687", {}),
                            },
                        ),
                        "SignalMode": ("V", "ns=1;i=6225", {}),
                        "TimeRemaining": (
                            "V",
                            "ns=1;i=6215",
                            {
                                "EURange": ("V", "ns=1;i=6216", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6689", {}),
                            },
                        ),
                    },
                ),
                "ProgramId": ("V", "ns=1;i=6007", {}),
                "ProgramName": ("V", "ns=1;i=6008", {}),
                "ProgramUId": ("V", "ns=1;i=6009", {}),
                "TrayType": (
                    "OT",
                    "ns=1;i=1027",
                    {
                        "ActiveSince": (
                            "V",
                            "ns=1;i=6506",
                            {
                                "EURange": ("V", "ns=1;i=6507", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6510", {}),
                            },
                        ),
                        "ActualTemperature": (
                            "V",
                            "ns=1;i=6500",
                            {
                                "EURange": ("V", "ns=1;i=6501", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6511", {}),
                            },
                        ),
                        "Name": ("V", "ns=1;i=6504", {}),
                        "OperatingCounter": (
                            "V",
                            "ns=1;i=6508",
                            {
                                "EURange": ("V", "ns=1;i=6509", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6512", {}),
                            },
                        ),
                        "ProgramMode": ("V", "ns=1;i=6499", {}),
                        "SetTemperature": (
                            "V",
                            "ns=1;i=6502",
                            {
                                "EURange": ("V", "ns=1;i=6503", {}),
                                "EngineeringUnits": ("V", "ns=1;i=6513", {}),
                            },
                        ),
                        "Type": ("V", "ns=1;i=6505", {}),
                    },
                ),
            },
        ),
    },
}
