# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 15fa32b4952f12a2d696fddd2466a4c764afdac2125d198223547d787aab6adb
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/LADS/"
_VERSION: str = "1.0.0"
_REQUIRED: list = [
    {"uri": "http://opcfoundation.org/UA/", "version": "1.05.02"},
    {"uri": "http://opcfoundation.org/UA/DI/", "version": "1.04.0"},
    {"uri": "http://opcfoundation.org/UA/AMB/", "version": "1.01.0"},
    {"uri": "http://opcfoundation.org/UA/Machinery/", "version": "1.03.0"},
]
_STRUCTURES: list = [
    (
        "ns=4;i=3003",
        "KeyValueType",
        "ns=4;i=5045",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Key", "data_type": "i=12", "value_rank": -1},
                {"name": "Value", "data_type": "i=12", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=4;i=3002",
        "SampleInfoType",
        "ns=4;i=5042",
        {
            "structure_type": 0,
            "fields": [
                {"name": "ContainerId", "data_type": "i=12", "value_rank": -1},
                {"name": "SampleId", "data_type": "i=12", "value_rank": -1},
                {"name": "Position", "data_type": "i=12", "value_rank": -1},
                {"name": "CustomData", "data_type": "i=12", "value_rank": -1},
            ],
        },
    ),
]
_ENUMS: list = [
    (
        "ns=4;i=3000",
        "MaintenanceTaskResultEnum",
        {
            "fields": [
                {"name": "Success", "value": 0, "display_name": "Success"},
                {"name": "Failure", "value": 1, "display_name": "Failure"},
                {"name": "Undetermined", "value": 2, "display_name": "Undetermined"},
            ]
        },
    )
]
_ORIGINAL_NODEIDS: tuple = (
    [
        ("ns=4;i=3003", "ns=4;i=5045", ["i=12", "i=12"]),
        ("ns=4;i=3002", "ns=4;i=5042", ["i=12", "i=12", "i=12", "i=12"]),
    ],
    ["ns=4;i=3000"],
)
_NODES: dict = {
    "datatypes": {
        "KeyValueType": ("D", "ns=4;i=3003", {}),
        "MaintenanceTaskResultEnum": (
            "D",
            "ns=4;i=3000",
            {"EnumValues": ("V", "ns=4;i=6099", {})},
        ),
        "SampleInfoType": ("D", "ns=4;i=3002", {}),
    },
    "objects": {
        "Components": ("O", "ns=4;i=5073", {}),
        "Default Binary": ("O", "ns=4;i=5045", {}),
        "Default JSON": ("O", "ns=4;i=5057", {}),
        "Default XML": ("O", "ns=4;i=5056", {}),
        "Identification": ("O", "ns=4;i=5095", {}),
        "LifetimeCounters": ("O", "ns=4;i=5094", {}),
        "MachineryItemState": ("O", "ns=4;i=5089", {}),
        "MachineryOperationMode": ("O", "ns=4;i=5090", {}),
        "OperationCounters": ("O", "ns=4;i=5097", {}),
        "TypeDictionary": (
            "V",
            "ns=4;i=6141",
            {
                "KeyValueType": ("V", "ns=4;i=6310", {}),
                "NamespaceUri": ("V", "ns=4;i=6144", {}),
                "SampleInfoType": ("V", "ns=4;i=6311", {}),
            },
        ),
        "http://opcfoundation.org/UA/LADS/": (
            "O",
            "ns=4;i=5026",
            {
                "IsNamespaceSubset": ("V", "ns=4;i=6053", {}),
                "NamespacePublicationDate": ("V", "ns=4;i=6054", {}),
                "NamespaceUri": ("V", "ns=4;i=6055", {}),
                "NamespaceVersion": ("V", "ns=4;i=6056", {}),
                "StaticNodeIdTypes": ("V", "ns=4;i=6057", {}),
                "StaticNumericNodeIdRange": ("V", "ns=4;i=6058", {}),
                "StaticStringNodeIdPattern": ("V", "ns=4;i=6059", {}),
            },
        ),
    },
    "objtypes": {
        "ActiveProgramType": (
            "OT",
            "ns=4;i=1040",
            {
                "CurrentPauseTime": ("V", "ns=4;i=6180", {}),
                "CurrentProgramTemplate": ("V", "ns=4;i=6315", {}),
                "CurrentRuntime": ("V", "ns=4;i=6163", {}),
                "CurrentStepName": ("V", "ns=4;i=6184", {}),
                "CurrentStepNumber": ("V", "ns=4;i=6185", {}),
                "CurrentStepRuntime": ("V", "ns=4;i=6186", {}),
                "DeviceProgramRunId": ("V", "ns=4;i=6126", {}),
                "EstimatedRuntime": ("V", "ns=4;i=6159", {}),
                "EstimatedStepNumbers": ("V", "ns=4;i=6162", {}),
                "EstimatedStepRuntime": ("V", "ns=4;i=6183", {}),
            },
        ),
        "ControllerParameterType": (
            "OT",
            "ns=4;i=1048",
            {
                "AlarmMonitor": ("O", "ns=4;i=5146", {}),
                "CurrentValue": ("V", "ns=4;i=6109", {}),
                "TargetValue": ("V", "ns=4;i=6110", {}),
            },
        ),
        "ControllerTuningParameterType": (
            "OT",
            "ns=4;i=1008",
            {
                "PidControllerParameterType": (
                    "OT",
                    "ns=4;i=1030",
                    {
                        "CtrlP": ("V", "ns=4;i=6003", {}),
                        "CtrlTd": ("V", "ns=4;i=6004", {}),
                        "CtrlTi": ("V", "ns=4;i=6005", {}),
                    },
                )
            },
        ),
        "CoverStateMachineType": (
            "OT",
            "ns=4;i=1010",
            {
                "Close": ("M", "ns=4;i=7012", {}),
                "Closed": (
                    "O",
                    "ns=4;i=5028",
                    {"StateNumber": ("V", "ns=4;i=6044", {})},
                ),
                "ClosedToError": (
                    "O",
                    "ns=4;i=5079",
                    {"TransitionNumber": ("V", "ns=4;i=6467", {})},
                ),
                "ClosedToLocked": (
                    "O",
                    "ns=4;i=5075",
                    {"TransitionNumber": ("V", "ns=4;i=6464", {})},
                ),
                "ClosedToLocking": (
                    "O",
                    "ns=4;i=5139",
                    {"TransitionNumber": ("V", "ns=4;i=6294", {})},
                ),
                "ClosedToOpened": (
                    "O",
                    "ns=4;i=5074",
                    {"TransitionNumber": ("V", "ns=4;i=6463", {})},
                ),
                "ClosedToOpening": (
                    "O",
                    "ns=4;i=5115",
                    {"TransitionNumber": ("V", "ns=4;i=6295", {})},
                ),
                "Closing": (
                    "O",
                    "ns=4;i=5110",
                    {"StateNumber": ("V", "ns=4;i=6286", {})},
                ),
                "ClosingToClosed": (
                    "O",
                    "ns=4;i=5138",
                    {"TransitionNumber": ("V", "ns=4;i=6296", {})},
                ),
                "Error": (
                    "O",
                    "ns=4;i=5050",
                    {"StateNumber": ("V", "ns=4;i=6046", {})},
                ),
                "ErrorToOpened": (
                    "O",
                    "ns=4;i=5082",
                    {"TransitionNumber": ("V", "ns=4;i=6476", {})},
                ),
                "Lock": ("M", "ns=4;i=7013", {}),
                "Locked": (
                    "O",
                    "ns=4;i=5049",
                    {"StateNumber": ("V", "ns=4;i=6045", {})},
                ),
                "LockedToClosed": (
                    "O",
                    "ns=4;i=5077",
                    {"TransitionNumber": ("V", "ns=4;i=6465", {})},
                ),
                "LockedToError": (
                    "O",
                    "ns=4;i=5078",
                    {"TransitionNumber": ("V", "ns=4;i=6466", {})},
                ),
                "LockedToUnlocking": (
                    "O",
                    "ns=4;i=5098",
                    {"TransitionNumber": ("V", "ns=4;i=6300", {})},
                ),
                "Locking": (
                    "O",
                    "ns=4;i=5108",
                    {"StateNumber": ("V", "ns=4;i=6287", {})},
                ),
                "LockingToLocked": (
                    "O",
                    "ns=4;i=5140",
                    {"TransitionNumber": ("V", "ns=4;i=6301", {})},
                ),
                "Open": ("M", "ns=4;i=7011", {}),
                "Opened": (
                    "O",
                    "ns=4;i=5025",
                    {"StateNumber": ("V", "ns=4;i=6043", {})},
                ),
                "OpenedToClosed": (
                    "O",
                    "ns=4;i=5000",
                    {"TransitionNumber": ("V", "ns=4;i=6000", {})},
                ),
                "OpenedToClosing": (
                    "O",
                    "ns=4;i=5137",
                    {"TransitionNumber": ("V", "ns=4;i=6302", {})},
                ),
                "Opening": (
                    "O",
                    "ns=4;i=5109",
                    {"StateNumber": ("V", "ns=4;i=6288", {})},
                ),
                "OpeningToOpened": (
                    "O",
                    "ns=4;i=5136",
                    {"TransitionNumber": ("V", "ns=4;i=6303", {})},
                ),
                "Reset": ("M", "ns=4;i=7000", {}),
                "Unlock": ("M", "ns=4;i=7014", {}),
                "Unlocking": (
                    "O",
                    "ns=4;i=5107",
                    {"StateNumber": ("V", "ns=4;i=6293", {})},
                ),
                "UnlockingToClosed": (
                    "O",
                    "ns=4;i=5114",
                    {"TransitionNumber": ("V", "ns=4;i=6304", {})},
                ),
            },
        ),
        "FunctionType": (
            "OT",
            "ns=4;i=1004",
            {
                "BaseControlFunctionType": (
                    "OT",
                    "ns=4;i=1007",
                    {
                        "AlarmMonitor": (
                            "O",
                            "ns=4;i=5068",
                            {
                                "AckedState": (
                                    "V",
                                    "ns=4;i=6232",
                                    {"Id": ("V", "ns=4;i=6233", {})},
                                ),
                                "Acknowledge": (
                                    "M",
                                    "ns=4;i=7042",
                                    {"InputArguments": ("V", "ns=4;i=6234", {})},
                                ),
                                "ActiveState": (
                                    "V",
                                    "ns=4;i=6224",
                                    {"Id": ("V", "ns=4;i=6225", {})},
                                ),
                                "AddComment": (
                                    "M",
                                    "ns=4;i=7043",
                                    {"InputArguments": ("V", "ns=4;i=6235", {})},
                                ),
                                "BranchId": ("V", "ns=4;i=6236", {}),
                                "ClientUserId": ("V", "ns=4;i=6237", {}),
                                "Comment": (
                                    "V",
                                    "ns=4;i=6238",
                                    {"SourceTimestamp": ("V", "ns=4;i=6239", {})},
                                ),
                                "ConditionClassId": ("V", "ns=4;i=6240", {}),
                                "ConditionClassName": ("V", "ns=4;i=6241", {}),
                                "ConditionName": ("V", "ns=4;i=6242", {}),
                                "Disable": ("M", "ns=4;i=7044", {}),
                                "Enable": ("M", "ns=4;i=7045", {}),
                                "EnabledState": (
                                    "V",
                                    "ns=4;i=6228",
                                    {"Id": ("V", "ns=4;i=6229", {})},
                                ),
                                "EventId": ("V", "ns=4;i=6248", {}),
                                "EventType": ("V", "ns=4;i=6249", {}),
                                "HighHighLimit": ("V", "ns=4;i=6023", {}),
                                "HighLimit": ("V", "ns=4;i=6024", {}),
                                "InputNode": ("V", "ns=4;i=6230", {}),
                                "LastSeverity": (
                                    "V",
                                    "ns=4;i=6243",
                                    {"SourceTimestamp": ("V", "ns=4;i=6244", {})},
                                ),
                                "LimitState": (
                                    "O",
                                    "ns=4;i=5071",
                                    {
                                        "CurrentState": (
                                            "V",
                                            "ns=4;i=6226",
                                            {"Id": ("V", "ns=4;i=6227", {})},
                                        )
                                    },
                                ),
                                "LowLimit": ("V", "ns=4;i=6025", {}),
                                "LowLowLimit": ("V", "ns=4;i=6026", {}),
                                "Message": ("V", "ns=4;i=6250", {}),
                                "Quality": (
                                    "V",
                                    "ns=4;i=6245",
                                    {"SourceTimestamp": ("V", "ns=4;i=6246", {})},
                                ),
                                "ReceiveTime": ("V", "ns=4;i=6251", {}),
                                "Retain": ("V", "ns=4;i=6247", {}),
                                "SetpointNode": ("V", "ns=4;i=6223", {}),
                                "Severity": ("V", "ns=4;i=6252", {}),
                                "SourceName": ("V", "ns=4;i=6253", {}),
                                "SourceNode": ("V", "ns=4;i=6254", {}),
                                "SuppressedOrShelved": ("V", "ns=4;i=6231", {}),
                                "Time": ("V", "ns=4;i=6255", {}),
                            },
                        ),
                        "AnalogControlFunctionType": (
                            "OT",
                            "ns=4;i=1009",
                            {
                                "AnalogControlFunctionWithComposedTargetValueType": (
                                    "OT",
                                    "ns=4;i=1052",
                                    {"TargetValueSet": ("O", "ns=4;i=5087", {})},
                                ),
                                "AnalogControlFunctionWithRelativeTargetValueType": (
                                    "OT",
                                    "ns=4;i=1029",
                                    {
                                        "DecreaseRate": ("V", "ns=4;i=6125", {}),
                                        "IncreaseRate": ("V", "ns=4;i=6089", {}),
                                        "ModifyTargetValueBy": (
                                            "M",
                                            "ns=4;i=7022",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=4;i=6128",
                                                    {},
                                                )
                                            },
                                        ),
                                        "Operational": ("O", "ns=4;i=5084", {}),
                                    },
                                ),
                                "AnalogControlFunctionWithTotalizerType": (
                                    "OT",
                                    "ns=4;i=1014",
                                    {
                                        "Operational": ("O", "ns=4;i=5059", {}),
                                        "ResetTotalizer": (
                                            "M",
                                            "ns=4;i=7002",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=4;i=6132",
                                                    {},
                                                )
                                            },
                                        ),
                                        "TotalizedValue": ("V", "ns=4;i=6011", {}),
                                    },
                                ),
                                "ControlFunctionState": (
                                    "O",
                                    "ns=4;i=5141",
                                    {
                                        "StartWithTargetValue": (
                                            "M",
                                            "ns=4;i=7027",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=4;i=6305",
                                                    {},
                                                )
                                            },
                                        )
                                    },
                                ),
                                "CurrentValue": ("V", "ns=4;i=6001", {}),
                                "Operational": ("O", "ns=4;i=5009", {}),
                                "TargetValue": ("V", "ns=4;i=6006", {}),
                            },
                        ),
                        "ControlFunctionState": (
                            "O",
                            "ns=4;i=5038",
                            {
                                "CurrentState": (
                                    "V",
                                    "ns=4;i=6079",
                                    {"Id": ("V", "ns=4;i=6042", {})},
                                )
                            },
                        ),
                        "ControllerTuningParameter": ("O", "ns=4;i=5001", {}),
                        "DiscreteControlFunctionType": (
                            "OT",
                            "ns=4;i=1017",
                            {
                                "CurrentValue": ("V", "ns=4;i=6065", {}),
                                "MultiStateDiscreteControlFunctionType": (
                                    "OT",
                                    "ns=4;i=1045",
                                    {
                                        "ControlFunctionState": (
                                            "O",
                                            "ns=4;i=5142",
                                            {
                                                "StartWithTargetValue": (
                                                    "M",
                                                    "ns=4;i=7050",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=4;i=6306",
                                                            {},
                                                        )
                                                    },
                                                )
                                            },
                                        ),
                                        "CurrentValue": (
                                            "V",
                                            "ns=4;i=6067",
                                            {"EnumStrings": ("V", "ns=4;i=6157", {})},
                                        ),
                                        "TargetValue": (
                                            "V",
                                            "ns=4;i=6124",
                                            {"EnumStrings": ("V", "ns=4;i=6158", {})},
                                        ),
                                    },
                                ),
                                "TargetValue": ("V", "ns=4;i=6123", {}),
                                "TwoStateDiscreteControlFunctionType": (
                                    "OT",
                                    "ns=4;i=1042",
                                    {
                                        "ControlFunctionState": (
                                            "O",
                                            "ns=4;i=5144",
                                            {
                                                "StartWithTargetValue": (
                                                    "M",
                                                    "ns=4;i=7054",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=4;i=6309",
                                                            {},
                                                        )
                                                    },
                                                )
                                            },
                                        ),
                                        "CurrentValue": (
                                            "V",
                                            "ns=4;i=6066",
                                            {
                                                "FalseState": ("V", "ns=4;i=6138", {}),
                                                "TrueState": ("V", "ns=4;i=6140", {}),
                                            },
                                        ),
                                        "TargetValue": (
                                            "V",
                                            "ns=4;i=6135",
                                            {
                                                "FalseState": ("V", "ns=4;i=6155", {}),
                                                "TrueState": ("V", "ns=4;i=6156", {}),
                                            },
                                        ),
                                    },
                                ),
                            },
                        ),
                        "MultiModeAnalogControlFunctionType": (
                            "OT",
                            "ns=4;i=1047",
                            {
                                "ControllerModeSet": ("O", "ns=4;i=5076", {}),
                                "CurrentMode": (
                                    "V",
                                    "ns=4;i=6122",
                                    {"EnumStrings": ("V", "ns=4;i=6165", {})},
                                ),
                                "Operational": ("O", "ns=4;i=5058", {}),
                            },
                        ),
                        "Operational": (
                            "O",
                            "ns=4;i=5046",
                            {
                                "Reset": ("M", "ns=4;i=7029", {}),
                                "Stop": ("M", "ns=4;i=7028", {}),
                            },
                        ),
                        "TimerControlFunctionType": (
                            "OT",
                            "ns=4;i=1013",
                            {
                                "CurrentValue": (
                                    "V",
                                    "ns=4;i=6035",
                                    {"EngineeringUnits": ("V", "ns=4;i=6147", {})},
                                ),
                                "DifferenceValue": (
                                    "V",
                                    "ns=4;i=6012",
                                    {"EngineeringUnits": ("V", "ns=4;i=6148", {})},
                                ),
                                "Operational": ("O", "ns=4;i=5113", {}),
                                "TargetValue": (
                                    "V",
                                    "ns=4;i=6034",
                                    {"EngineeringUnits": ("V", "ns=4;i=6161", {})},
                                ),
                            },
                        ),
                    },
                ),
                "BaseSensorFunctionType": (
                    "OT",
                    "ns=4;i=1005",
                    {
                        "AnalogSensorFunctionType": (
                            "OT",
                            "ns=4;i=1046",
                            {
                                "AlarmMonitor": (
                                    "O",
                                    "ns=4;i=5069",
                                    {
                                        "AckedState": (
                                            "V",
                                            "ns=4;i=6199",
                                            {"Id": ("V", "ns=4;i=6200", {})},
                                        ),
                                        "Acknowledge": (
                                            "M",
                                            "ns=4;i=7038",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=4;i=6201",
                                                    {},
                                                )
                                            },
                                        ),
                                        "ActiveState": (
                                            "V",
                                            "ns=4;i=6191",
                                            {"Id": ("V", "ns=4;i=6192", {})},
                                        ),
                                        "AddComment": (
                                            "M",
                                            "ns=4;i=7039",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=4;i=6202",
                                                    {},
                                                )
                                            },
                                        ),
                                        "BranchId": ("V", "ns=4;i=6203", {}),
                                        "ClientUserId": ("V", "ns=4;i=6204", {}),
                                        "Comment": (
                                            "V",
                                            "ns=4;i=6205",
                                            {
                                                "SourceTimestamp": (
                                                    "V",
                                                    "ns=4;i=6206",
                                                    {},
                                                )
                                            },
                                        ),
                                        "ConditionClassId": ("V", "ns=4;i=6207", {}),
                                        "ConditionClassName": ("V", "ns=4;i=6208", {}),
                                        "ConditionName": ("V", "ns=4;i=6209", {}),
                                        "Disable": ("M", "ns=4;i=7040", {}),
                                        "Enable": ("M", "ns=4;i=7041", {}),
                                        "EnabledState": (
                                            "V",
                                            "ns=4;i=6195",
                                            {"Id": ("V", "ns=4;i=6196", {})},
                                        ),
                                        "EventId": ("V", "ns=4;i=6215", {}),
                                        "EventType": ("V", "ns=4;i=6216", {}),
                                        "InputNode": ("V", "ns=4;i=6197", {}),
                                        "LastSeverity": (
                                            "V",
                                            "ns=4;i=6210",
                                            {
                                                "SourceTimestamp": (
                                                    "V",
                                                    "ns=4;i=6211",
                                                    {},
                                                )
                                            },
                                        ),
                                        "LimitState": (
                                            "O",
                                            "ns=4;i=5070",
                                            {
                                                "CurrentState": (
                                                    "V",
                                                    "ns=4;i=6193",
                                                    {"Id": ("V", "ns=4;i=6194", {})},
                                                )
                                            },
                                        ),
                                        "Message": ("V", "ns=4;i=6217", {}),
                                        "Quality": (
                                            "V",
                                            "ns=4;i=6212",
                                            {
                                                "SourceTimestamp": (
                                                    "V",
                                                    "ns=4;i=6213",
                                                    {},
                                                )
                                            },
                                        ),
                                        "ReceiveTime": ("V", "ns=4;i=6218", {}),
                                        "Retain": ("V", "ns=4;i=6214", {}),
                                        "Severity": ("V", "ns=4;i=6219", {}),
                                        "SourceName": ("V", "ns=4;i=6220", {}),
                                        "SourceNode": ("V", "ns=4;i=6221", {}),
                                        "SuppressedOrShelved": ("V", "ns=4;i=6198", {}),
                                        "Time": ("V", "ns=4;i=6222", {}),
                                    },
                                ),
                                "AnalogArraySensorFunctionType": (
                                    "OT",
                                    "ns=4;i=1015",
                                    {
                                        "RawValue": ("V", "ns=4;i=6134", {}),
                                        "SensorValue": ("V", "ns=4;i=6130", {}),
                                    },
                                ),
                                "AnalogScalarSensorFunctionType": (
                                    "OT",
                                    "ns=4;i=1016",
                                    {
                                        "AnalogScalarSensorFunctionWithCompensationType": (
                                            "OT",
                                            "ns=4;i=1000",
                                            {
                                                "CompensationValue": (
                                                    "V",
                                                    "ns=4;i=6037",
                                                    {},
                                                )
                                            },
                                        ),
                                        "Operational": ("O", "ns=4;i=5024", {}),
                                        "RawValue": ("V", "ns=4;i=6039", {}),
                                        "SensorValue": ("V", "ns=4;i=6033", {}),
                                    },
                                ),
                                "Calibration": (
                                    "O",
                                    "ns=4;i=5135",
                                    {"CalibrationValues": ("V", "ns=4;i=6036", {})},
                                ),
                                "Operational": ("O", "ns=4;i=5011", {}),
                                "RawValue": ("V", "ns=4;i=6040", {}),
                                "SensorValue": ("V", "ns=4;i=6112", {}),
                                "Tuning": (
                                    "O",
                                    "ns=4;i=5010",
                                    {"Damping": ("V", "ns=4;i=6038", {})},
                                ),
                            },
                        ),
                        "Configuration": (
                            "O",
                            "ns=4;i=5030",
                            {"IsEnabled": ("V", "ns=4;i=6022", {})},
                        ),
                        "DiscreteSensorFunctionType": (
                            "OT",
                            "ns=4;i=1012",
                            {
                                "MultiStateDiscreteSensorFunctionType": (
                                    "OT",
                                    "ns=4;i=1037",
                                    {
                                        "SensorValue": (
                                            "V",
                                            "ns=4;i=6030",
                                            {"EnumStrings": ("V", "ns=4;i=6160", {})},
                                        )
                                    },
                                ),
                                "Operational": ("O", "ns=4;i=5061", {}),
                                "SensorValue": ("V", "ns=4;i=6031", {}),
                                "TwoStateDiscreteSensorFunctionType": (
                                    "OT",
                                    "ns=4;i=1031",
                                    {
                                        "SensorValue": (
                                            "V",
                                            "ns=4;i=6007",
                                            {
                                                "FalseState": ("V", "ns=4;i=6136", {}),
                                                "TrueState": ("V", "ns=4;i=6137", {}),
                                            },
                                        )
                                    },
                                ),
                            },
                        ),
                        "MultiSensorFunctionType": (
                            "OT",
                            "ns=4;i=1051",
                            {
                                "FunctionSet": (
                                    "O",
                                    "ns=4;i=5006",
                                    {"<SetElement>": ("O", "ns=4;i=5080", {})},
                                )
                            },
                        ),
                    },
                ),
                "Configuration": ("O", "ns=4;i=5012", {}),
                "CoverFunctionType": (
                    "OT",
                    "ns=4;i=1011",
                    {
                        "CoverState": (
                            "O",
                            "ns=4;i=5055",
                            {"CurrentState": ("V", "ns=4;i=6314", {})},
                        ),
                        "Operational": ("O", "ns=4;i=5064", {}),
                    },
                ),
                "FunctionSet": (
                    "O",
                    "ns=4;i=5013",
                    {"NodeVersion": ("V", "ns=4;i=6084", {})},
                ),
                "IsEnabled": ("V", "ns=4;i=6002", {}),
            },
        ),
        "FunctionalStateMachineType": (
            "OT",
            "ns=4;i=1038",
            {
                "Abort": ("M", "ns=4;i=7078", {}),
                "Aborted": (
                    "O",
                    "ns=4;i=5160",
                    {"StateNumber": ("V", "ns=4;i=6475", {})},
                ),
                "AbortedToClearing": (
                    "O",
                    "ns=4;i=5165",
                    {"TransitionNumber": ("V", "ns=4;i=6486", {})},
                ),
                "Aborting": (
                    "O",
                    "ns=4;i=5159",
                    {"StateNumber": ("V", "ns=4;i=6474", {})},
                ),
                "AbortingToAborted": (
                    "O",
                    "ns=4;i=5126",
                    {"TransitionNumber": ("V", "ns=4;i=6432", {})},
                ),
                "AvailableStates": ("V", "ns=4;i=6473", {}),
                "AvailableTransitions": ("V", "ns=4;i=6472", {}),
                "Clear": ("M", "ns=4;i=7079", {}),
                "Clearing": (
                    "O",
                    "ns=4;i=5143",
                    {"StateNumber": ("V", "ns=4;i=6449", {})},
                ),
                "ClearingToStopped": (
                    "O",
                    "ns=4;i=5104",
                    {"TransitionNumber": ("V", "ns=4;i=6529", {})},
                ),
                "ControlFunctionStateMachineType": (
                    "OT",
                    "ns=4;i=1044",
                    {
                        "Start": ("M", "ns=4;i=7035", {}),
                        "StartWithTargetValue": (
                            "M",
                            "ns=4;i=7009",
                            {"InputArguments": ("V", "ns=4;i=6129", {})},
                        ),
                    },
                ),
                "CurrentState": (
                    "V",
                    "ns=4;i=6100",
                    {"EffectiveDisplayName": ("V", "ns=4;i=6101", {})},
                ),
                "FunctionalUnitStateMachineType": (
                    "OT",
                    "ns=4;i=1043",
                    {
                        "CurrentState": (
                            "V",
                            "ns=4;i=6279",
                            {"EffectiveDisplayName": ("V", "ns=4;i=6280", {})},
                        ),
                        "Start": (
                            "M",
                            "ns=4;i=7004",
                            {"InputArguments": ("V", "ns=4;i=6127", {})},
                        ),
                        "StartProgram": (
                            "M",
                            "ns=4;i=7010",
                            {
                                "InputArguments": ("V", "ns=4;i=6098", {}),
                                "OutputArguments": ("V", "ns=4;i=6121", {}),
                            },
                        ),
                    },
                ),
                "Running": (
                    "O",
                    "ns=4;i=5099",
                    {"StateNumber": ("V", "ns=4;i=6509", {})},
                ),
                "RunningStateMachine": ("O", "ns=4;i=5130", {}),
                "RunningToAborting": (
                    "O",
                    "ns=4;i=5103",
                    {"TransitionNumber": ("V", "ns=4;i=6528", {})},
                ),
                "RunningToStopping": (
                    "O",
                    "ns=4;i=5105",
                    {"TransitionNumber": ("V", "ns=4;i=6534", {})},
                ),
                "Stop": ("M", "ns=4;i=7112", {}),
                "Stopped": (
                    "O",
                    "ns=4;i=5085",
                    {"StateNumber": ("V", "ns=4;i=6508", {})},
                ),
                "StoppedToRunning": (
                    "O",
                    "ns=4;i=5102",
                    {"TransitionNumber": ("V", "ns=4;i=6513", {})},
                ),
                "Stopping": (
                    "O",
                    "ns=4;i=5100",
                    {"StateNumber": ("V", "ns=4;i=6511", {})},
                ),
                "StoppingToStopped": (
                    "O",
                    "ns=4;i=5101",
                    {"TransitionNumber": ("V", "ns=4;i=6512", {})},
                ),
            },
        ),
        "FunctionalUnitType": (
            "OT",
            "ns=4;i=1003",
            {
                "AssetId": ("V", "ns=4;i=6284", {}),
                "ComponentName": ("V", "ns=4;i=6285", {}),
                "FunctionSet": ("O", "ns=4;i=5008", {}),
                "FunctionalUnitState": ("O", "ns=4;i=5005", {}),
                "Identification": ("O", "ns=4;i=5003", {}),
                "Lock": (
                    "O",
                    "ns=4;i=5004",
                    {
                        "BreakLock": (
                            "M",
                            "ns=4;i=7005",
                            {"OutputArguments": ("V", "ns=4;i=6013", {})},
                        ),
                        "ExitLock": (
                            "M",
                            "ns=4;i=7006",
                            {"OutputArguments": ("V", "ns=4;i=6014", {})},
                        ),
                        "InitLock": (
                            "M",
                            "ns=4;i=7007",
                            {
                                "InputArguments": ("V", "ns=4;i=6015", {}),
                                "OutputArguments": ("V", "ns=4;i=6016", {}),
                            },
                        ),
                        "Locked": ("V", "ns=4;i=6017", {}),
                        "LockingClient": ("V", "ns=4;i=6018", {}),
                        "LockingUser": ("V", "ns=4;i=6019", {}),
                        "RemainingLockTime": ("V", "ns=4;i=6020", {}),
                        "RenewLock": (
                            "M",
                            "ns=4;i=7008",
                            {"OutputArguments": ("V", "ns=4;i=6021", {})},
                        ),
                    },
                ),
                "Operational": (
                    "O",
                    "ns=4;i=5007",
                    {
                        "Abort": ("M", "ns=4;i=7025", {}),
                        "Clear": ("M", "ns=4;i=7019", {}),
                        "EffectiveDisplayName": ("V", "ns=4;i=6105", {}),
                        "StartProgram": (
                            "M",
                            "ns=4;i=7046",
                            {
                                "InputArguments": ("V", "ns=4;i=6142", {}),
                                "OutputArguments": ("V", "ns=4;i=6143", {}),
                            },
                        ),
                        "Stop": ("M", "ns=4;i=7024", {}),
                    },
                ),
                "ProgramManager": (
                    "O",
                    "ns=4;i=5015",
                    {
                        "ActiveProgram": ("O", "ns=4;i=5218", {}),
                        "ProgramTemplateSet": (
                            "O",
                            "ns=4;i=5021",
                            {"NodeVersion": ("V", "ns=4;i=6258", {})},
                        ),
                        "ResultSet": (
                            "O",
                            "ns=4;i=5022",
                            {"NodeVersion": ("V", "ns=4;i=6052", {})},
                        ),
                    },
                ),
                "SupportedPropertiesSet": ("O", "ns=4;i=5116", {}),
            },
        ),
        "LADSComponentType": (
            "OT",
            "ns=4;i=1024",
            {
                "AssetId": ("V", "ns=4;i=6149", {}),
                "ComponentName": ("V", "ns=4;i=6150", {}),
                "DeviceClass": ("V", "ns=4;i=6151", {}),
                "DeviceHealth": ("V", "ns=4;i=6480", {}),
                "DeviceHealthAlarms": ("O", "ns=4;i=5258", {}),
                "DeviceManual": ("V", "ns=4;i=6152", {}),
                "DeviceRevision": ("V", "ns=4;i=6153", {}),
                "HardwareRevision": ("V", "ns=4;i=6154", {}),
                "HierarchicalLocation": ("V", "ns=4;i=6080", {}),
                "MachineryBuildingBlocks": ("O", "ns=4;i=5088", {}),
                "Maintenance": (
                    "O",
                    "ns=4;i=5106",
                    {"NodeVersion": ("V", "ns=4;i=6189", {})},
                ),
                "Manufacturer": ("V", "ns=4;i=6169", {}),
                "ManufacturerUri": ("V", "ns=4;i=6170", {}),
                "Model": ("V", "ns=4;i=6171", {}),
                "OperationalLocation": ("V", "ns=4;i=6074", {}),
                "ProductCode": ("V", "ns=4;i=6172", {}),
                "ProductInstanceUri": ("V", "ns=4;i=6173", {}),
                "RevisionCounter": ("V", "ns=4;i=6174", {}),
                "SerialNumber": ("V", "ns=4;i=6175", {}),
                "SoftwareRevision": ("V", "ns=4;i=6176", {}),
            },
        ),
        "LADSComponentsType": (
            "OT",
            "ns=4;i=1025",
            {
                "<Component>": ("O", "ns=4;i=5065", {}),
                "NodeVersion": ("V", "ns=4;i=6085", {}),
            },
        ),
        "LADSDeviceStateMachineType": (
            "OT",
            "ns=4;i=1039",
            {
                "GotoOperate": ("M", "ns=4;i=7021", {}),
                "GotoShutdown": ("M", "ns=4;i=7031", {}),
                "GotoSleep": ("M", "ns=4;i=7032", {}),
                "Initialization": (
                    "O",
                    "ns=4;i=5177",
                    {"StateNumber": ("V", "ns=4;i=6329", {})},
                ),
                "InitializationToOperate": (
                    "O",
                    "ns=4;i=5181",
                    {"TransitionNumber": ("V", "ns=4;i=6352", {})},
                ),
                "Operate": (
                    "O",
                    "ns=4;i=5178",
                    {"StateNumber": ("V", "ns=4;i=6330", {})},
                ),
                "OperateToShutdown": (
                    "O",
                    "ns=4;i=5184",
                    {"TransitionNumber": ("V", "ns=4;i=6355", {})},
                ),
                "OperateToSleep": (
                    "O",
                    "ns=4;i=5260",
                    {"TransitionNumber": ("V", "ns=4;i=6556", {})},
                ),
                "Shutdown": (
                    "O",
                    "ns=4;i=5180",
                    {"StateNumber": ("V", "ns=4;i=6351", {})},
                ),
                "Sleep": (
                    "O",
                    "ns=4;i=5259",
                    {"StateNumber": ("V", "ns=4;i=6525", {})},
                ),
                "SleepToOperate": (
                    "O",
                    "ns=4;i=5083",
                    {"TransitionNumber": ("V", "ns=4;i=6482", {})},
                ),
            },
        ),
        "LADSDeviceType": (
            "OT",
            "ns=4;i=1002",
            {
                "AssetId": ("V", "ns=4;i=6068", {}),
                "ComponentName": ("V", "ns=4;i=6069", {}),
                "DeviceClass": ("V", "ns=4;i=6083", {}),
                "DeviceHealth": ("V", "ns=4;i=6086", {}),
                "DeviceManual": ("V", "ns=4;i=6051", {}),
                "DeviceRevision": ("V", "ns=4;i=6062", {}),
                "DeviceState": (
                    "O",
                    "ns=4;i=5191",
                    {
                        "CurrentState": (
                            "V",
                            "ns=4;i=6600",
                            {"Id": ("V", "ns=4;i=6601", {})},
                        ),
                        "GotoOperate": ("M", "ns=4;i=7124", {}),
                        "GotoShutdown": ("M", "ns=4;i=7125", {}),
                        "GotoSleep": ("M", "ns=4;i=7126", {}),
                    },
                ),
                "FunctionalUnitSet": (
                    "O",
                    "ns=4;i=5002",
                    {"NodeVersion": ("V", "ns=4;i=6103", {})},
                ),
                "HardwareRevision": ("V", "ns=4;i=6093", {}),
                "HierarchicalLocation": ("V", "ns=4;i=6029", {}),
                "MachineryBuildingBlocks": ("O", "ns=4;i=5063", {}),
                "Maintenance": (
                    "O",
                    "ns=4;i=5092",
                    {"NodeVersion": ("V", "ns=4;i=6113", {})},
                ),
                "Manufacturer": ("V", "ns=4;i=6009", {}),
                "ManufacturerUri": ("V", "ns=4;i=6094", {}),
                "Model": ("V", "ns=4;i=6010", {}),
                "OperationalLocation": ("V", "ns=4;i=6028", {}),
                "ProductCode": ("V", "ns=4;i=6095", {}),
                "ProductInstanceUri": ("V", "ns=4;i=6096", {}),
                "RevisionCounter": ("V", "ns=4;i=6008", {}),
                "SerialNumber": ("V", "ns=4;i=6064", {}),
                "SoftwareRevision": ("V", "ns=4;i=6063", {}),
            },
        ),
        "LADSOperationCountersType": (
            "OT",
            "ns=4;i=1034",
            {"LifeTime": ("V", "ns=4;i=6027", {})},
        ),
        "LADSOperationModeStateMachineType": (
            "OT",
            "ns=4;i=1050",
            {
                "GotoMaintenance": ("M", "ns=4;i=7055", {}),
                "GotoProcessing": ("M", "ns=4;i=7020", {}),
                "GotoSetup": ("M", "ns=4;i=7056", {}),
            },
        ),
        "MaintenanceTaskType": (
            "OT",
            "ns=4;i=1028",
            {
                "ConfigurationChanged": ("V", "ns=4;i=6097", {}),
                "EstimatedDowntime": ("V", "ns=4;i=6102", {}),
                "LastExecutionDate": ("V", "ns=4;i=6360", {}),
                "LastOperatingCycles": ("V", "ns=4;i=6088", {}),
                "LastOperatingTime": ("V", "ns=4;i=6081", {}),
                "MaintenanceMethod": ("V", "ns=4;i=6106", {}),
                "MaintenanceState": ("O", "ns=4;i=5066", {}),
                "MaintenanceSupplier": ("V", "ns=4;i=6107", {}),
                "NextOperatingCycles": ("V", "ns=4;i=6091", {}),
                "NextOperatingTime": ("V", "ns=4;i=6087", {}),
                "PartsOfAssetReplaced": ("V", "ns=4;i=6108", {}),
                "PartsOfAssetServiced": ("V", "ns=4;i=6111", {}),
                "PlannedDate": ("V", "ns=4;i=6119", {}),
                "QualificationOfPersonnel": ("V", "ns=4;i=6120", {}),
                "RecurrencePeriod": ("V", "ns=4;i=6362", {}),
                "ResetTask": ("M", "ns=4;i=7003", {}),
                "StartTask": ("M", "ns=4;i=7061", {}),
                "StopTask": (
                    "M",
                    "ns=4;i=7001",
                    {"InputArguments": ("V", "ns=4;i=6092", {})},
                ),
            },
        ),
        "ProgramManagerType": (
            "OT",
            "ns=4;i=1006",
            {
                "ActiveProgram": ("O", "ns=4;i=5190", {}),
                "Download": (
                    "M",
                    "ns=4;i=7051",
                    {
                        "InputArguments": ("V", "ns=4;i=6289", {}),
                        "OutputArguments": ("V", "ns=4;i=6290", {}),
                    },
                ),
                "ProgramTemplateSet": (
                    "O",
                    "ns=4;i=5020",
                    {"NodeVersion": ("V", "ns=4;i=6257", {})},
                ),
                "Remove": (
                    "M",
                    "ns=4;i=7052",
                    {"InputArguments": ("V", "ns=4;i=6291", {})},
                ),
                "ResultSet": (
                    "O",
                    "ns=4;i=5019",
                    {"NodeVersion": ("V", "ns=4;i=6041", {})},
                ),
                "Upload": (
                    "M",
                    "ns=4;i=7053",
                    {
                        "InputArguments": ("V", "ns=4;i=6292", {}),
                        "OutputArguments": ("V", "ns=4;i=6032", {}),
                    },
                ),
            },
        ),
        "ProgramTemplateType": (
            "OT",
            "ns=4;i=1018",
            {
                "Author": ("V", "ns=4;i=6348", {}),
                "Created": ("V", "ns=4;i=6341", {}),
                "Description": ("V", "ns=4;i=6340", {}),
                "DeviceTemplateId": ("V", "ns=4;i=6259", {}),
                "Modified": ("V", "ns=4;i=6344", {}),
                "SupervisoryTemplateId": ("V", "ns=4;i=6090", {}),
                "Version": ("V", "ns=4;i=6346", {}),
            },
        ),
        "ResultFileType": (
            "OT",
            "ns=4;i=1001",
            {
                "File": ("O", "ns=4;i=5072", {}),
                "MimeType": ("V", "ns=4;i=6297", {}),
                "Name": ("V", "ns=4;i=6298", {}),
                "URL": ("V", "ns=4;i=6299", {}),
            },
        ),
        "ResultType": (
            "OT",
            "ns=4;i=1021",
            {
                "ApplicationUri": ("V", "ns=4;i=6281", {}),
                "Description": ("V", "ns=4;i=6396", {}),
                "DeviceProgramRunId": ("V", "ns=4;i=6495", {}),
                "EstimatedRuntime": ("V", "ns=4;i=6504", {}),
                "FileSet": ("O", "ns=4;i=5081", {}),
                "ProgramTemplate": ("O", "ns=4;i=5112", {}),
                "Properties": ("V", "ns=4;i=6485", {}),
                "Samples": ("V", "ns=4;i=6308", {}),
                "Started": ("V", "ns=4;i=6307", {}),
                "Stopped": ("V", "ns=4;i=6394", {}),
                "SupervisoryJobId": ("V", "ns=4;i=6393", {}),
                "SupervisoryTaskId": ("V", "ns=4;i=6487", {}),
                "TotalPauseTime": ("V", "ns=4;i=6501", {}),
                "TotalRuntime": ("V", "ns=4;i=6500", {}),
                "User": ("V", "ns=4;i=6282", {}),
                "VariableSet": ("O", "ns=4;i=5067", {}),
            },
        ),
        "RunningStateMachineType": (
            "OT",
            "ns=4;i=1036",
            {
                "Complete": (
                    "O",
                    "ns=4;i=5128",
                    {"StateNumber": ("V", "ns=4;i=6434", {})},
                ),
                "CompleteToResetting": (
                    "O",
                    "ns=4;i=5035",
                    {"TransitionNumber": ("V", "ns=4;i=6060", {})},
                ),
                "Completing": (
                    "O",
                    "ns=4;i=5127",
                    {"StateNumber": ("V", "ns=4;i=6433", {})},
                ),
                "CompletingToComplete": (
                    "O",
                    "ns=4;i=5034",
                    {"TransitionNumber": ("V", "ns=4;i=6050", {})},
                ),
                "CurrentState": ("V", "ns=4;i=6146", {}),
                "Execute": (
                    "O",
                    "ns=4;i=5168",
                    {"StateNumber": ("V", "ns=4;i=6489", {})},
                ),
                "ExecuteToCompleting": (
                    "O",
                    "ns=4;i=5033",
                    {"TransitionNumber": ("V", "ns=4;i=6049", {})},
                ),
                "ExecuteToHolding": (
                    "O",
                    "ns=4;i=5051",
                    {"TransitionNumber": ("V", "ns=4;i=6076", {})},
                ),
                "ExecuteToSuspending": (
                    "O",
                    "ns=4;i=5037",
                    {"TransitionNumber": ("V", "ns=4;i=6070", {})},
                ),
                "Held": ("O", "ns=4;i=5124", {"StateNumber": ("V", "ns=4;i=6430", {})}),
                "HeldToUnholding": (
                    "O",
                    "ns=4;i=5053",
                    {"TransitionNumber": ("V", "ns=4;i=6078", {})},
                ),
                "Hold": ("M", "ns=4;i=7074", {}),
                "Holding": (
                    "O",
                    "ns=4;i=5123",
                    {"StateNumber": ("V", "ns=4;i=6429", {})},
                ),
                "HoldingToHeld": (
                    "O",
                    "ns=4;i=5052",
                    {"TransitionNumber": ("V", "ns=4;i=6077", {})},
                ),
                "Idle": ("O", "ns=4;i=5120", {"StateNumber": ("V", "ns=4;i=6426", {})}),
                "IdleToStarting": (
                    "O",
                    "ns=4;i=5031",
                    {"TransitionNumber": ("V", "ns=4;i=6047", {})},
                ),
                "Reset": ("M", "ns=4;i=7069", {}),
                "Resetting": (
                    "O",
                    "ns=4;i=5119",
                    {"StateNumber": ("V", "ns=4;i=6425", {})},
                ),
                "ResettingToIdle": (
                    "O",
                    "ns=4;i=5036",
                    {"TransitionNumber": ("V", "ns=4;i=6061", {})},
                ),
                "Starting": (
                    "O",
                    "ns=4;i=5117",
                    {"StateNumber": ("V", "ns=4;i=6423", {})},
                ),
                "StartingToExecute": (
                    "O",
                    "ns=4;i=5032",
                    {"TransitionNumber": ("V", "ns=4;i=6048", {})},
                ),
                "StartingToHolding": (
                    "O",
                    "ns=4;i=5131",
                    {"TransitionNumber": ("V", "ns=4;i=6116", {})},
                ),
                "Suspend": ("M", "ns=4;i=7073", {}),
                "Suspended": (
                    "O",
                    "ns=4;i=5121",
                    {"StateNumber": ("V", "ns=4;i=6427", {})},
                ),
                "SuspendedToHolding": (
                    "O",
                    "ns=4;i=5132",
                    {"TransitionNumber": ("V", "ns=4;i=6117", {})},
                ),
                "SuspendedToUnsuspending": (
                    "O",
                    "ns=4;i=5040",
                    {"TransitionNumber": ("V", "ns=4;i=6072", {})},
                ),
                "Suspending": (
                    "O",
                    "ns=4;i=5118",
                    {"StateNumber": ("V", "ns=4;i=6424", {})},
                ),
                "SuspendingToHolding": (
                    "O",
                    "ns=4;i=5129",
                    {"TransitionNumber": ("V", "ns=4;i=6115", {})},
                ),
                "SuspendingToSuspended": (
                    "O",
                    "ns=4;i=5039",
                    {"TransitionNumber": ("V", "ns=4;i=6071", {})},
                ),
                "ToComplete": ("M", "ns=4;i=7070", {}),
                "Unhold": ("M", "ns=4;i=7072", {}),
                "Unholding": (
                    "O",
                    "ns=4;i=5125",
                    {"StateNumber": ("V", "ns=4;i=6431", {})},
                ),
                "UnholdingToExecute": (
                    "O",
                    "ns=4;i=5054",
                    {"TransitionNumber": ("V", "ns=4;i=6114", {})},
                ),
                "UnholdingToHolding": (
                    "O",
                    "ns=4;i=5134",
                    {"TransitionNumber": ("V", "ns=4;i=6275", {})},
                ),
                "Unsuspend": ("M", "ns=4;i=7075", {}),
                "Unsuspending": (
                    "O",
                    "ns=4;i=5122",
                    {"StateNumber": ("V", "ns=4;i=6428", {})},
                ),
                "UnsuspendingToExecute": (
                    "O",
                    "ns=4;i=5041",
                    {"TransitionNumber": ("V", "ns=4;i=6073", {})},
                ),
                "UnsuspendingToHolding": (
                    "O",
                    "ns=4;i=5133",
                    {"TransitionNumber": ("V", "ns=4;i=6118", {})},
                ),
            },
        ),
        "SetType": (
            "OT",
            "ns=4;i=61",
            {
                "<SetElement>": ("O", "ns=4;i=5014", {}),
                "ControllerParameterSetType": (
                    "OT",
                    "ns=4;i=1049",
                    {"<SetElement>": ("O", "ns=4;i=5023", {})},
                ),
                "FunctionSetType": (
                    "OT",
                    "ns=4;i=1026",
                    {"<SetElement>": ("O", "ns=4;i=5027", {})},
                ),
                "FunctionalUnitSetType": (
                    "OT",
                    "ns=4;i=1023",
                    {"<SetElement>": ("O", "ns=4;i=5016", {})},
                ),
                "MaintenanceSetType": (
                    "OT",
                    "ns=4;i=1027",
                    {
                        "<SetElement>": (
                            "O",
                            "ns=4;i=5017",
                            {
                                "AckedState": (
                                    "V",
                                    "ns=4;i=6181",
                                    {"Id": ("V", "ns=4;i=6182", {})},
                                ),
                                "Acknowledge": (
                                    "M",
                                    "ns=4;i=7030",
                                    {"InputArguments": ("V", "ns=4;i=6187", {})},
                                ),
                                "ActiveState": (
                                    "V",
                                    "ns=4;i=6168",
                                    {"Id": ("V", "ns=4;i=6177", {})},
                                ),
                                "AddComment": (
                                    "M",
                                    "ns=4;i=7049",
                                    {"InputArguments": ("V", "ns=4;i=6267", {})},
                                ),
                                "BranchId": ("V", "ns=4;i=6256", {}),
                                "ClientUserId": ("V", "ns=4;i=6266", {}),
                                "Comment": (
                                    "V",
                                    "ns=4;i=6264",
                                    {"SourceTimestamp": ("V", "ns=4;i=6265", {})},
                                ),
                                "ConditionClassId": ("V", "ns=4;i=6268", {}),
                                "ConditionClassName": ("V", "ns=4;i=6269", {}),
                                "ConditionName": ("V", "ns=4;i=6190", {}),
                                "Disable": ("M", "ns=4;i=7048", {}),
                                "Enable": ("M", "ns=4;i=7047", {}),
                                "EnabledState": (
                                    "V",
                                    "ns=4;i=6166",
                                    {"Id": ("V", "ns=4;i=6167", {})},
                                ),
                                "EventId": ("V", "ns=4;i=6270", {}),
                                "EventType": ("V", "ns=4;i=6271", {}),
                                "InputNode": ("V", "ns=4;i=6179", {}),
                                "LastSeverity": (
                                    "V",
                                    "ns=4;i=6262",
                                    {"SourceTimestamp": ("V", "ns=4;i=6263", {})},
                                ),
                                "MaintenanceState": ("O", "ns=4;i=5018", {}),
                                "Message": ("V", "ns=4;i=6277", {}),
                                "NormalState": ("V", "ns=4;i=6164", {}),
                                "Quality": (
                                    "V",
                                    "ns=4;i=6260",
                                    {"SourceTimestamp": ("V", "ns=4;i=6261", {})},
                                ),
                                "ReceiveTime": ("V", "ns=4;i=6276", {}),
                                "Retain": ("V", "ns=4;i=6188", {}),
                                "Severity": ("V", "ns=4;i=6278", {}),
                                "SourceName": ("V", "ns=4;i=6273", {}),
                                "SourceNode": ("V", "ns=4;i=6272", {}),
                                "SuppressedOrShelved": ("V", "ns=4;i=6178", {}),
                                "Time": ("V", "ns=4;i=6274", {}),
                            },
                        )
                    },
                ),
                "NodeVersion": ("V", "ns=4;i=6075", {}),
                "ProgramTemplateSetType": (
                    "OT",
                    "ns=4;i=1019",
                    {
                        "<SetElement>": ("O", "ns=4;i=5029", {}),
                        "NodeVersion": ("V", "ns=4;i=6133", {}),
                    },
                ),
                "ResultFileSetType": (
                    "OT",
                    "ns=4;i=1022",
                    {"<SetElement>": ("O", "ns=4;i=5060", {})},
                ),
                "ResultSetType": (
                    "OT",
                    "ns=4;i=1020",
                    {
                        "<SetElement>": ("O", "ns=4;i=5062", {}),
                        "NodeVersion": ("V", "ns=4;i=6104", {}),
                    },
                ),
                "SupportedPropertiesSetType": (
                    "OT",
                    "ns=4;i=1033",
                    {"<SetElement>": ("O", "ns=4;i=5048", {})},
                ),
                "VariableSetType": (
                    "OT",
                    "ns=4;i=1041",
                    {
                        "<SetElement>": ("O", "ns=4;i=5086", {}),
                        "<VariableSetElement>": ("V", "ns=4;i=6082", {}),
                    },
                ),
            },
        ),
        "SupportedPropertyType": ("OT", "ns=4;i=1035", {}),
    },
}
