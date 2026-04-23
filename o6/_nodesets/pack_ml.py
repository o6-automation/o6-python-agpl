# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 79016b1468d3288da36fca3604ad5439ebae7fdfca87e4f8def2aa1999e49adf
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/PackML/"
_VERSION: str = "1.01"
_REQUIRED: list = [{"uri": "http://opcfoundation.org/UA/", "version": "1.04.6"}]
_STRUCTURES: list = [
    (
        "ns=1;i=15",
        "PackMLAlarmDataType",
        "ns=1;i=74",
        {
            "structure_type": 0,
            "fields": [
                {"name": "ID", "data_type": "i=6", "value_rank": -1},
                {"name": "Value", "data_type": "i=6", "value_rank": -1},
                {"name": "Message", "data_type": "i=12", "value_rank": -1},
                {"name": "Category", "data_type": "i=6", "value_rank": -1},
                {"name": "DateTime", "data_type": "i=294", "value_rank": -1},
                {"name": "AckDateTime", "data_type": "i=294", "value_rank": -1},
                {"name": "Trigger", "data_type": "i=1", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=14",
        "PackMLCountDataType",
        "ns=1;i=69",
        {
            "structure_type": 0,
            "fields": [
                {"name": "ID", "data_type": "i=6", "value_rank": -1},
                {"name": "Name", "data_type": "i=12", "value_rank": -1},
                {"name": "Unit", "data_type": "i=887", "value_rank": -1},
                {"name": "Count", "data_type": "i=6", "value_rank": -1},
                {"name": "AccCount", "data_type": "i=6", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=16",
        "PackMLDescriptorDataType",
        "ns=1;i=77",
        {
            "structure_type": 0,
            "fields": [
                {"name": "ID", "data_type": "i=6", "value_rank": -1},
                {"name": "Name", "data_type": "i=12", "value_rank": -1},
                {"name": "Unit", "data_type": "i=887", "value_rank": -1},
                {"name": "Value", "data_type": "i=10", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=17",
        "PackMLIngredientsDataType",
        "ns=1;i=79",
        {
            "structure_type": 0,
            "fields": [
                {"name": "IngredientID", "data_type": "i=6", "value_rank": -1},
                {"name": "Parameter", "data_type": "ns=1;i=16", "value_rank": 1},
            ],
        },
    ),
    (
        "ns=1;i=18",
        "PackMLProductDataType",
        "ns=1;i=81",
        {
            "structure_type": 0,
            "fields": [
                {"name": "ProductID", "data_type": "i=6", "value_rank": -1},
                {"name": "ProcessVariables", "data_type": "ns=1;i=16", "value_rank": 1},
                {"name": "Ingredients", "data_type": "ns=1;i=17", "value_rank": 1},
            ],
        },
    ),
    (
        "ns=1;i=19",
        "PackMLRemoteInterfaceDataType",
        "ns=1;i=83",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Number", "data_type": "i=6", "value_rank": -1},
                {"name": "ControlCmdNumber", "data_type": "i=6", "value_rank": -1},
                {"name": "CmdValue", "data_type": "i=6", "value_rank": -1},
                {"name": "Parameter", "data_type": "ns=1;i=16", "value_rank": 1},
            ],
        },
    ),
]
_ENUMS: list = [
    (
        "ns=1;i=11",
        "ProductionMaintenanceModeEnum",
        {
            "fields": [
                {"name": "Invalid", "value": 0, "display_name": "Invalid"},
                {"name": "Produce", "value": 1, "display_name": "Produce"},
                {"name": "Maintenance", "value": 2, "display_name": "Maintenance"},
                {"name": "Manual", "value": 3, "display_name": "Manual"},
            ]
        },
    )
]
_ORIGINAL_NODEIDS: tuple = (
    [
        (
            "ns=1;i=15",
            "ns=1;i=74",
            ["i=6", "i=6", "i=12", "i=6", "i=294", "i=294", "i=1"],
        ),
        ("ns=1;i=14", "ns=1;i=69", ["i=6", "i=12", "i=887", "i=6", "i=6"]),
        ("ns=1;i=16", "ns=1;i=77", ["i=6", "i=12", "i=887", "i=10"]),
        ("ns=1;i=17", "ns=1;i=79", ["i=6", "ns=1;i=16"]),
        ("ns=1;i=18", "ns=1;i=81", ["i=6", "ns=1;i=16", "ns=1;i=17"]),
        ("ns=1;i=19", "ns=1;i=83", ["i=6", "i=6", "i=6", "ns=1;i=16"]),
    ],
    ["ns=1;i=11"],
)
_NODES: dict = {
    "datatypes": {
        "PackMLAlarmDataType": ("D", "ns=1;i=15", {}),
        "PackMLCountDataType": ("D", "ns=1;i=14", {}),
        "PackMLDescriptorDataType": ("D", "ns=1;i=16", {}),
        "PackMLIngredientsDataType": ("D", "ns=1;i=17", {}),
        "PackMLProductDataType": ("D", "ns=1;i=18", {}),
        "PackMLRemoteInterfaceDataType": ("D", "ns=1;i=19", {}),
        "ProductionMaintenanceModeEnum": (
            "D",
            "ns=1;i=11",
            {"EnumValues": ("V", "ns=1;i=194", {})},
        ),
    },
    "objects": {
        "Alarm": ("V", "ns=1;i=238", {}),
        "AlarmHistory": ("V", "ns=1;i=240", {}),
        "Default Binary": ("O", "ns=1;i=83", {}),
        "Default XML": ("O", "ns=1;i=84", {}),
        "MaterialInterlock": ("V", "ns=1;i=237", {}),
        "PackMLObjects": ("O", "ns=1;i=72", {}),
        "StopReason": ("V", "ns=1;i=244", {}),
        "TypeDictionary": (
            "V",
            "ns=1;i=197",
            {
                "NamespaceUri": ("V", "ns=1;i=198", {}),
                "PackMLAlarmDataType": ("V", "ns=1;i=183", {}),
                "PackMLCountDataType": ("V", "ns=1;i=181", {}),
                "PackMLDescriptorDataType": ("V", "ns=1;i=185", {}),
                "PackMLIngredientsDataType": ("V", "ns=1;i=189", {}),
                "PackMLProductDataType": ("V", "ns=1;i=191", {}),
                "PackMLRemoteInterfaceDataType": ("V", "ns=1;i=188", {}),
            },
        ),
        "Warning": ("V", "ns=1;i=242", {}),
        "http://opcfoundation.org/UA/PackML/": (
            "O",
            "ns=1;i=117",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=354", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=355", {}),
                "NamespaceUri": ("V", "ns=1;i=356", {}),
                "NamespaceVersion": ("V", "ns=1;i=357", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=358", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=359", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=360", {}),
            },
        ),
    },
    "objtypes": {
        "PackMLAdminObjectType": (
            "OT",
            "ns=1;i=5",
            {
                "AccTimeSinceReset": ("V", "ns=1;i=252", {}),
                "AlarmExtent": ("V", "ns=1;i=239", {}),
                "AlarmHistoryExtent": ("V", "ns=1;i=241", {}),
                "MachDesignSpeed": ("V", "ns=1;i=253", {}),
                "ModeCumulativeTime": ("V", "ns=1;i=247", {}),
                "ModeCurrentTime": ("V", "ns=1;i=246", {}),
                "Parameter": ("V", "ns=1;i=276", {}),
                "ProdConsumedCount": ("V", "ns=1;i=124", {}),
                "ProdDefectiveCount": ("V", "ns=1;i=119", {}),
                "ProdProcessedCount": ("V", "ns=1;i=120", {}),
                "StateCumulativeTime": ("V", "ns=1;i=249", {}),
                "StateCurrentTime": ("V", "ns=1;i=248", {}),
                "StopReasonExtent": ("V", "ns=1;i=245", {}),
                "WarningExtent": ("V", "ns=1;i=243", {}),
            },
        ),
        "PackMLBaseObjectType": (
            "OT",
            "ns=1;i=6",
            {
                "Admin": ("O", "ns=1;i=73", {}),
                "BaseStateMachine": (
                    "O",
                    "ns=1;i=88",
                    {
                        "AvailableStates": ("V", "ns=1;i=259", {}),
                        "AvailableTransitions": ("V", "ns=1;i=202", {}),
                        "CurrentState": (
                            "V",
                            "ns=1;i=272",
                            {"Id": ("V", "ns=1;i=273", {})},
                        ),
                        "MachineState": (
                            "O",
                            "ns=1;i=89",
                            {
                                "AvailableStates": ("V", "ns=1;i=214", {}),
                                "AvailableTransitions": ("V", "ns=1;i=213", {}),
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=262",
                                    {"Id": ("V", "ns=1;i=263", {})},
                                ),
                                "ExecuteState": (
                                    "O",
                                    "ns=1;i=90",
                                    {
                                        "AvailableStates": ("V", "ns=1;i=223", {}),
                                        "AvailableTransitions": ("V", "ns=1;i=222", {}),
                                        "CurrentState": (
                                            "V",
                                            "ns=1;i=266",
                                            {"Id": ("V", "ns=1;i=227", {})},
                                        ),
                                    },
                                ),
                            },
                        ),
                    },
                ),
                "PackMLVersion": ("V", "ns=1;i=221", {}),
                "RemoteCommand": (
                    "M",
                    "ns=1;i=403",
                    {"InputArguments": ("V", "ns=1;i=350", {})},
                ),
                "SetInterlock": (
                    "M",
                    "ns=1;i=404",
                    {"InputArguments": ("V", "ns=1;i=351", {})},
                ),
                "SetMachSpeed": (
                    "M",
                    "ns=1;i=400",
                    {"InputArguments": ("V", "ns=1;i=348", {})},
                ),
                "SetParameter": (
                    "M",
                    "ns=1;i=402",
                    {"InputArguments": ("V", "ns=1;i=352", {})},
                ),
                "SetProduct": (
                    "M",
                    "ns=1;i=401",
                    {"InputArguments": ("V", "ns=1;i=349", {})},
                ),
                "SetUnitMode": (
                    "M",
                    "ns=1;i=362",
                    {"InputArguments": ("V", "ns=1;i=118", {})},
                ),
                "Status": (
                    "O",
                    "ns=1;i=87",
                    {
                        "CurMachSpeed": (
                            "V",
                            "ns=1;i=255",
                            {"EURange": ("V", "ns=1;i=256", {})},
                        ),
                        "EquipmentBlocked": ("V", "ns=1;i=274", {}),
                        "EquipmentStarved": ("V", "ns=1;i=275", {}),
                        "MachSpeed": (
                            "V",
                            "ns=1;i=257",
                            {"EURange": ("V", "ns=1;i=258", {})},
                        ),
                        "UnitModeCurrent": ("V", "ns=1;i=225", {}),
                        "UnitSupportedModes": ("V", "ns=1;i=290", {}),
                    },
                ),
                "TagID": ("V", "ns=1;i=218", {}),
            },
        ),
        "PackMLBaseStateMachineType": (
            "OT",
            "ns=1;i=3",
            {
                "Abort": ("M", "ns=1;i=364", {}),
                "Aborted": ("O", "ns=1;i=62", {"StateNumber": ("V", "ns=1;i=169", {})}),
                "AbortedToCleared": (
                    "O",
                    "ns=1;i=65",
                    {"TransitionNumber": ("V", "ns=1;i=174", {})},
                ),
                "Aborting": (
                    "O",
                    "ns=1;i=61",
                    {"StateNumber": ("V", "ns=1;i=168", {})},
                ),
                "AbortingToAborted": (
                    "O",
                    "ns=1;i=66",
                    {"TransitionNumber": ("V", "ns=1;i=175", {})},
                ),
                "AvailableStates": ("V", "ns=1;i=167", {}),
                "AvailableTransitions": ("V", "ns=1;i=158", {}),
                "Clear": ("M", "ns=1;i=363", {}),
                "Cleared": ("O", "ns=1;i=71", {"StateNumber": ("V", "ns=1;i=178", {})}),
                "ClearedToAborting": (
                    "O",
                    "ns=1;i=67",
                    {"TransitionNumber": ("V", "ns=1;i=176", {})},
                ),
                "MachineState": (
                    "O",
                    "ns=1;i=64",
                    {
                        "AvailableStates": ("V", "ns=1;i=212", {}),
                        "AvailableTransitions": ("V", "ns=1;i=204", {}),
                        "CurrentState": (
                            "V",
                            "ns=1;i=172",
                            {"Id": ("V", "ns=1;i=173", {})},
                        ),
                    },
                ),
            },
        ),
        "PackMLExecuteStateMachineType": (
            "OT",
            "ns=1;i=1",
            {
                "AvailableStates": ("V", "ns=1;i=125", {}),
                "AvailableTransitions": ("V", "ns=1;i=126", {}),
                "Complete": (
                    "O",
                    "ns=1;i=38",
                    {"StateNumber": ("V", "ns=1;i=138", {})},
                ),
                "CompleteToResetting": (
                    "O",
                    "ns=1;i=51",
                    {"TransitionNumber": ("V", "ns=1;i=151", {})},
                ),
                "Completing": (
                    "O",
                    "ns=1;i=37",
                    {"StateNumber": ("V", "ns=1;i=137", {})},
                ),
                "CompletingToComplete": (
                    "O",
                    "ns=1;i=50",
                    {"TransitionNumber": ("V", "ns=1;i=150", {})},
                ),
                "Execute": ("O", "ns=1;i=36", {"StateNumber": ("V", "ns=1;i=136", {})}),
                "ExecuteToCompleting": (
                    "O",
                    "ns=1;i=49",
                    {"TransitionNumber": ("V", "ns=1;i=149", {})},
                ),
                "ExecuteToHolding": (
                    "O",
                    "ns=1;i=45",
                    {"TransitionNumber": ("V", "ns=1;i=145", {})},
                ),
                "ExecuteToSuspending": (
                    "O",
                    "ns=1;i=42",
                    {"TransitionNumber": ("V", "ns=1;i=142", {})},
                ),
                "Held": ("O", "ns=1;i=34", {"StateNumber": ("V", "ns=1;i=134", {})}),
                "HeldToUnholding": (
                    "O",
                    "ns=1;i=47",
                    {"TransitionNumber": ("V", "ns=1;i=147", {})},
                ),
                "Hold": ("M", "ns=1;i=366", {}),
                "Holding": ("O", "ns=1;i=33", {"StateNumber": ("V", "ns=1;i=133", {})}),
                "HoldingToHeld": (
                    "O",
                    "ns=1;i=46",
                    {"TransitionNumber": ("V", "ns=1;i=146", {})},
                ),
                "Idle": ("O", "ns=1;i=28", {"StateNumber": ("V", "ns=1;i=128", {})}),
                "IdleToStarting": (
                    "O",
                    "ns=1;i=40",
                    {"TransitionNumber": ("V", "ns=1;i=140", {})},
                ),
                "Reset": ("M", "ns=1;i=361", {}),
                "Resetting": (
                    "O",
                    "ns=1;i=27",
                    {"StateNumber": ("V", "ns=1;i=127", {})},
                ),
                "ResettingToIdle": (
                    "O",
                    "ns=1;i=39",
                    {"TransitionNumber": ("V", "ns=1;i=139", {})},
                ),
                "Start": (
                    "M",
                    "ns=1;i=369",
                    {"InputArguments": ("V", "ns=1;i=342", {})},
                ),
                "Starting": (
                    "O",
                    "ns=1;i=29",
                    {"StateNumber": ("V", "ns=1;i=129", {})},
                ),
                "StartingToExecute": (
                    "O",
                    "ns=1;i=41",
                    {"TransitionNumber": ("V", "ns=1;i=141", {})},
                ),
                "StartingToHolding": (
                    "O",
                    "ns=1;i=99",
                    {"TransitionNumber": ("V", "ns=1;i=179", {})},
                ),
                "Suspend": ("M", "ns=1;i=367", {}),
                "Suspended": (
                    "O",
                    "ns=1;i=31",
                    {"StateNumber": ("V", "ns=1;i=131", {})},
                ),
                "SuspendedToHolding": (
                    "O",
                    "ns=1;i=101",
                    {"TransitionNumber": ("V", "ns=1;i=215", {})},
                ),
                "SuspendedToUnsuspending": (
                    "O",
                    "ns=1;i=52",
                    {"TransitionNumber": ("V", "ns=1;i=152", {})},
                ),
                "Suspending": (
                    "O",
                    "ns=1;i=30",
                    {"StateNumber": ("V", "ns=1;i=130", {})},
                ),
                "SuspendingToHolding": (
                    "O",
                    "ns=1;i=102",
                    {"TransitionNumber": ("V", "ns=1;i=216", {})},
                ),
                "SuspendingToSuspended": (
                    "O",
                    "ns=1;i=43",
                    {"TransitionNumber": ("V", "ns=1;i=143", {})},
                ),
                "ToComplete": ("M", "ns=1;i=365", {}),
                "Unhold": ("M", "ns=1;i=368", {}),
                "Unholding": (
                    "O",
                    "ns=1;i=35",
                    {"StateNumber": ("V", "ns=1;i=135", {})},
                ),
                "UnholdingToExecute": (
                    "O",
                    "ns=1;i=48",
                    {"TransitionNumber": ("V", "ns=1;i=148", {})},
                ),
                "UnholdingToHolding": (
                    "O",
                    "ns=1;i=103",
                    {"TransitionNumber": ("V", "ns=1;i=217", {})},
                ),
                "Unsuspend": ("M", "ns=1;i=372", {}),
                "Unsuspending": (
                    "O",
                    "ns=1;i=32",
                    {"StateNumber": ("V", "ns=1;i=132", {})},
                ),
                "UnsuspendingToExecute": (
                    "O",
                    "ns=1;i=44",
                    {"TransitionNumber": ("V", "ns=1;i=144", {})},
                ),
                "UnsuspendingToHolding": (
                    "O",
                    "ns=1;i=100",
                    {"TransitionNumber": ("V", "ns=1;i=208", {})},
                ),
            },
        ),
        "PackMLMachineStateMachineType": (
            "OT",
            "ns=1;i=2",
            {
                "AvailableStates": ("V", "ns=1;i=153", {}),
                "AvailableTransitions": ("V", "ns=1;i=154", {}),
                "Clearing": (
                    "O",
                    "ns=1;i=55",
                    {"StateNumber": ("V", "ns=1;i=157", {})},
                ),
                "ClearingToStopped": (
                    "O",
                    "ns=1;i=58",
                    {"TransitionNumber": ("V", "ns=1;i=164", {})},
                ),
                "ExecuteState": (
                    "O",
                    "ns=1;i=56",
                    {
                        "AvailableStates": ("V", "ns=1;i=177", {}),
                        "AvailableTransitions": ("V", "ns=1;i=160", {}),
                        "CurrentState": (
                            "V",
                            "ns=1;i=161",
                            {"Id": ("V", "ns=1;i=162", {})},
                        ),
                    },
                ),
                "Reset": ("M", "ns=1;i=376", {}),
                "Running": ("O", "ns=1;i=75", {"StateNumber": ("V", "ns=1;i=171", {})}),
                "RunningToStopping": (
                    "O",
                    "ns=1;i=60",
                    {"TransitionNumber": ("V", "ns=1;i=166", {})},
                ),
                "Stop": ("M", "ns=1;i=375", {}),
                "Stopped": ("O", "ns=1;i=53", {"StateNumber": ("V", "ns=1;i=155", {})}),
                "StoppedToRunning": (
                    "O",
                    "ns=1;i=59",
                    {"TransitionNumber": ("V", "ns=1;i=165", {})},
                ),
                "Stopping": (
                    "O",
                    "ns=1;i=54",
                    {"StateNumber": ("V", "ns=1;i=156", {})},
                ),
                "StoppingToStopped": (
                    "O",
                    "ns=1;i=57",
                    {"TransitionNumber": ("V", "ns=1;i=163", {})},
                ),
            },
        ),
        "PackMLStatusObjectType": (
            "OT",
            "ns=1;i=4",
            {
                "CurMachSpeed": (
                    "V",
                    "ns=1;i=232",
                    {"EURange": ("V", "ns=1;i=233", {})},
                ),
                "EquipmentBlocked": ("V", "ns=1;i=211", {}),
                "EquipmentStarved": ("V", "ns=1;i=224", {}),
                "MachSpeed": ("V", "ns=1;i=219", {"EURange": ("V", "ns=1;i=220", {})}),
                "MaterialInterlocked": ("V", "ns=1;i=236", {}),
                "Parameter": ("V", "ns=1;i=121", {}),
                "Product": ("V", "ns=1;i=122", {}),
                "RemoteParameter": ("V", "ns=1;i=123", {}),
                "StateChangeInProcess": ("V", "ns=1;i=210", {}),
                "StateRequested": ("V", "ns=1;i=209", {}),
                "UnitModeChangeInProcess": ("V", "ns=1;i=201", {}),
                "UnitModeCurrent": ("V", "ns=1;i=200", {}),
                "UnitModeRequested": ("V", "ns=1;i=192", {}),
                "UnitSupportedModes": ("V", "ns=1;i=193", {}),
            },
        ),
    },
    "reftypes": {
        "HasAlarm": ("RT", "ns=1;i=22", {}),
        "HasAlarmHistory": ("RT", "ns=1;i=23", {}),
        "HasInterlock": ("RT", "ns=1;i=21", {}),
        "HasStopReason": ("RT", "ns=1;i=25", {}),
        "HasWarning": ("RT", "ns=1;i=24", {}),
    },
}
