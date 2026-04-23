# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 4153430e86babb1ae72f3e8272b953acfb790cd8e4ea5f0468cfc408c75350bc
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/MDIS"
_VERSION: str = "1.3"
_REQUIRED: list = [{"uri": "http://opcfoundation.org/UA/", "version": "1.05.04"}]
_STRUCTURES: list = [
    (
        "ns=1;i=1289",
        "MDISVersionDataType",
        "ns=1;i=1484",
        {
            "structure_type": 0,
            "fields": [
                {"name": "MajorVersion", "data_type": "i=3", "value_rank": -1},
                {"name": "MinorVersion", "data_type": "i=3", "value_rank": -1},
                {"name": "Build", "data_type": "i=3", "value_rank": -1},
            ],
        },
    )
]
_ENUMS: list = [
    (
        "ns=1;i=15009",
        "ArbitrationModeEnum",
        {
            "fields": [
                {"name": "Average", "value": 1, "display_name": "Average"},
                {"name": "DefaultA", "value": 2, "display_name": "DefaultA"},
                {"name": "DefaultB", "value": 4, "display_name": "DefaultB"},
                {"name": "ForceA", "value": 8, "display_name": "ForceA"},
                {"name": "ForceB", "value": 16, "display_name": "ForceB"},
                {"name": "High", "value": 32, "display_name": "High"},
                {"name": "Low", "value": 64, "display_name": "Low"},
            ]
        },
    ),
    (
        "ns=1;i=701",
        "ChokeCommandEnum",
        {
            "fields": [
                {"name": "Close", "value": 1, "display_name": "Close"},
                {"name": "Open", "value": 2, "display_name": "Open"},
            ]
        },
    ),
    (
        "ns=1;i=602",
        "ChokeMoveEnum",
        {
            "fields": [
                {"name": "Moving", "value": 1, "display_name": "Moving"},
                {"name": "Stopped", "value": 2, "display_name": "Stopped"},
            ]
        },
    ),
    (
        "ns=1;i=15007",
        "CIMVMoveEnum",
        {
            "fields": [
                {"name": "MoveClose", "value": 1, "display_name": "MoveClose"},
                {"name": "MoveOpen", "value": 2, "display_name": "MoveOpen"},
                {"name": "Stop", "value": 4, "display_name": "Stop"},
            ]
        },
    ),
    (
        "ns=1;i=15102",
        "CIMVOperationModeEnum",
        {
            "fields": [
                {"name": "Position", "value": 1, "display_name": "Position"},
                {"name": "Flow", "value": 2, "display_name": "Flow"},
                {"name": "Manual", "value": 4, "display_name": "Manual"},
            ]
        },
    ),
    (
        "ns=1;i=3",
        "CommandEnum",
        {
            "fields": [
                {"name": "Close", "value": 1, "display_name": "Close"},
                {"name": "Open", "value": 2, "display_name": "Open"},
                {"name": "None", "value": 4, "display_name": "None"},
            ]
        },
    ),
    (
        "ns=1;i=15013",
        "MotorOperationEnum",
        {
            "fields": [
                {"name": "Off", "value": 1, "display_name": "Off"},
                {"name": "Auto", "value": 2, "display_name": "Auto"},
                {"name": "Manual", "value": 4, "display_name": "Manual"},
            ]
        },
    ),
    (
        "ns=1;i=15011",
        "MotorStateEnum",
        {
            "fields": [
                {"name": "Active", "value": 1, "display_name": "Active"},
                {"name": "NonActive", "value": 2, "display_name": "NonActive"},
            ]
        },
    ),
    (
        "ns=1;i=5",
        "SEMEnum",
        {
            "fields": [
                {"name": "SEM_A", "value": 1, "display_name": "SEM_A"},
                {"name": "SEM_B", "value": 2, "display_name": "SEM_B"},
                {"name": "Auto", "value": 4, "display_name": "Auto"},
            ]
        },
    ),
    (
        "ns=1;i=1287",
        "SetCalculatedPositionEnum",
        {
            "fields": [
                {"name": "Initial", "value": 0, "display_name": "Initial"},
                {"name": "Inprogress", "value": 1, "display_name": "Inprogress"},
                {"name": "Complete", "value": 2, "display_name": "Complete"},
                {"name": "Fault", "value": 4, "display_name": "Fault"},
            ]
        },
    ),
    (
        "ns=1;i=699",
        "SignatureStatusEnum",
        {
            "fields": [
                {"name": "NotAvailable", "value": 1, "display_name": "NotAvailable"},
                {"name": "Completed", "value": 2, "display_name": "Completed"},
                {"name": "Failed", "value": 4, "display_name": "Failed"},
            ]
        },
    ),
    (
        "ns=1;i=703",
        "ValvePositionEnum",
        {
            "fields": [
                {"name": "Closed", "value": 1, "display_name": "Closed"},
                {"name": "Open", "value": 2, "display_name": "Open"},
                {"name": "Moving", "value": 4, "display_name": "Moving"},
                {"name": "Unknown", "value": 8, "display_name": "Unknown"},
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = (
    [("ns=1;i=1289", "ns=1;i=1484", ["i=3", "i=3", "i=3"])],
    [
        "ns=1;i=15009",
        "ns=1;i=701",
        "ns=1;i=602",
        "ns=1;i=15007",
        "ns=1;i=15102",
        "ns=1;i=3",
        "ns=1;i=15013",
        "ns=1;i=15011",
        "ns=1;i=5",
        "ns=1;i=1287",
        "ns=1;i=699",
        "ns=1;i=703",
    ],
)
_NODES: dict = {
    "datatypes": {
        "ArbitrationModeEnum": (
            "D",
            "ns=1;i=15009",
            {"EnumValues": ("V", "ns=1;i=15010", {})},
        ),
        "CIMVMoveEnum": (
            "D",
            "ns=1;i=15007",
            {"EnumValues": ("V", "ns=1;i=15008", {})},
        ),
        "CIMVOperationModeEnum": (
            "D",
            "ns=1;i=15102",
            {"EnumValues": ("V", "ns=1;i=15103", {})},
        ),
        "ChokeCommandEnum": (
            "D",
            "ns=1;i=701",
            {"EnumValues": ("V", "ns=1;i=702", {})},
        ),
        "ChokeMoveEnum": ("D", "ns=1;i=602", {"EnumValues": ("V", "ns=1;i=603", {})}),
        "CommandEnum": ("D", "ns=1;i=3", {"EnumValues": ("V", "ns=1;i=616", {})}),
        "MDISVersionDataType": ("D", "ns=1;i=1289", {}),
        "MotorOperationEnum": (
            "D",
            "ns=1;i=15013",
            {"EnumValues": ("V", "ns=1;i=15014", {})},
        ),
        "MotorStateEnum": (
            "D",
            "ns=1;i=15011",
            {"EnumValues": ("V", "ns=1;i=15012", {})},
        ),
        "SEMEnum": ("D", "ns=1;i=5", {"EnumValues": ("V", "ns=1;i=6", {})}),
        "SetCalculatedPositionEnum": (
            "D",
            "ns=1;i=1287",
            {"EnumValues": ("V", "ns=1;i=1288", {})},
        ),
        "SignatureStatusEnum": (
            "D",
            "ns=1;i=699",
            {"EnumValues": ("V", "ns=1;i=700", {})},
        ),
        "ValvePositionEnum": (
            "D",
            "ns=1;i=703",
            {"EnumValues": ("V", "ns=1;i=704", {})},
        ),
    },
    "objects": {
        "<InterlockPlaceholder>": ("V", "ns=1;i=1280", {}),
        "<ValveSignature>": (
            "O",
            "ns=1;i=1294",
            {
                "Close": (
                    "M",
                    "ns=1;i=1302",
                    {"InputArguments": ("V", "ns=1;i=1303", {})},
                ),
                "GetPosition": (
                    "M",
                    "ns=1;i=1309",
                    {
                        "InputArguments": ("V", "ns=1;i=1310", {}),
                        "OutputArguments": ("V", "ns=1;i=1311", {}),
                    },
                ),
                "Open": (
                    "M",
                    "ns=1;i=1299",
                    {
                        "InputArguments": ("V", "ns=1;i=1300", {}),
                        "OutputArguments": ("V", "ns=1;i=1301", {}),
                    },
                ),
                "OpenCount": ("V", "ns=1;i=1298", {}),
                "Read": (
                    "M",
                    "ns=1;i=1304",
                    {
                        "InputArguments": ("V", "ns=1;i=1305", {}),
                        "OutputArguments": ("V", "ns=1;i=1306", {}),
                    },
                ),
                "SetPosition": (
                    "M",
                    "ns=1;i=1312",
                    {"InputArguments": ("V", "ns=1;i=1313", {})},
                ),
                "Size": ("V", "ns=1;i=1295", {}),
                "UserWritable": ("V", "ns=1;i=1297", {}),
                "Writable": ("V", "ns=1;i=1296", {}),
                "Write": (
                    "M",
                    "ns=1;i=1307",
                    {"InputArguments": ("V", "ns=1;i=1308", {})},
                ),
            },
        ),
        "Default Binary": ("O", "ns=1;i=1484", {}),
        "Default JSON": ("O", "ns=1;i=15004", {}),
        "Default XML": ("O", "ns=1;i=1480", {}),
        "MDISInformation": (
            "O",
            "ns=1;i=15044",
            {
                "MDISVersion": (
                    "V",
                    "ns=1;i=15049",
                    {
                        "Build": ("V", "ns=1;i=15052", {}),
                        "MajorVersion": ("V", "ns=1;i=15050", {}),
                        "MinorVersion": ("V", "ns=1;i=15051", {}),
                    },
                ),
                "Signatures": ("O", "ns=1;i=15048", {}),
                "TimeSynchronization": (
                    "O",
                    "ns=1;i=15045",
                    {
                        "SetTime": (
                            "M",
                            "ns=1;i=15046",
                            {"InputArguments": ("V", "ns=1;i=15047", {})},
                        )
                    },
                ),
            },
        ),
        "Opc.MDIS": (
            "V",
            "ns=1;i=367",
            {
                "Deprecated": ("V", "ns=1;i=15003", {}),
                "MDISVersionDataType": ("V", "ns=1;i=1481", {}),
                "NamespaceUri": ("V", "ns=1;i=369", {}),
            },
        ),
        "http://opcfoundation.org/UA/MDIS": (
            "O",
            "ns=1;i=5001",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=6001", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=6002", {}),
                "NamespaceUri": ("V", "ns=1;i=6003", {}),
                "NamespaceVersion": ("V", "ns=1;i=6004", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=6005", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=6006", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=6007", {}),
            },
        ),
    },
    "objtypes": {
        "MDISBaseObjectType": (
            "OT",
            "ns=1;i=194",
            {
                "EnableDisable": (
                    "M",
                    "ns=1;i=195",
                    {"InputArguments": ("V", "ns=1;i=196", {})},
                ),
                "Enabled": ("V", "ns=1;i=476", {}),
                "Fault": ("V", "ns=1;i=489", {}),
                "FaultCode": ("V", "ns=1;i=1165", {}),
                "MDISAggregateObjectType": (
                    "OT",
                    "ns=1;i=1315",
                    {
                        "<CIMVPlaceholder>": (
                            "O",
                            "ns=1;i=15311",
                            {
                                "Abort": ("M", "ns=1;i=15381", {}),
                                "Fault": ("V", "ns=1;i=15312", {}),
                                "FlowRate": (
                                    "V",
                                    "ns=1;i=15329",
                                    {
                                        "EURange": ("V", "ns=1;i=15333", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=15334", {}),
                                    },
                                ),
                                "Moving": ("V", "ns=1;i=15342", {}),
                                "OperationMode": ("V", "ns=1;i=15328", {}),
                                "Position": ("V", "ns=1;i=15341", {}),
                                "SetFlowRate": (
                                    "M",
                                    "ns=1;i=15375",
                                    {"InputArguments": ("V", "ns=1;i=15376", {})},
                                ),
                                "SetOperationMode": (
                                    "M",
                                    "ns=1;i=15373",
                                    {"InputArguments": ("V", "ns=1;i=15374", {})},
                                ),
                                "SetPosition": (
                                    "M",
                                    "ns=1;i=15377",
                                    {"InputArguments": ("V", "ns=1;i=15378", {})},
                                ),
                                "TargetFlowRate": (
                                    "V",
                                    "ns=1;i=15403",
                                    {
                                        "EURange": ("V", "ns=1;i=15407", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=15408", {}),
                                    },
                                ),
                                "TargetPosition": ("V", "ns=1;i=15409", {}),
                            },
                        ),
                        "<ChokePlaceholder>": (
                            "O",
                            "ns=1;i=1437",
                            {
                                "Abort": ("M", "ns=1;i=1459", {}),
                                "CalculatedPosition": ("V", "ns=1;i=1446", {}),
                                "Fault": ("V", "ns=1;i=1438", {}),
                                "Move": (
                                    "M",
                                    "ns=1;i=1455",
                                    {"InputArguments": ("V", "ns=1;i=1456", {})},
                                ),
                                "Moving": ("V", "ns=1;i=1449", {}),
                                "SetCalculatedPosition": (
                                    "M",
                                    "ns=1;i=1460",
                                    {"InputArguments": ("V", "ns=1;i=1461", {})},
                                ),
                            },
                        ),
                        "<CounterPlaceholder>": (
                            "O",
                            "ns=1;i=15382",
                            {"Count": ("V", "ns=1;i=15383", {})},
                        ),
                        "<DigitalArbitrationPlaceholder>": (
                            "O",
                            "ns=1;i=15241",
                            {
                                "ArbitrationMode": ("V", "ns=1;i=15253", {}),
                                "Fault": ("V", "ns=1;i=15242", {}),
                                "SourceA": ("V", "ns=1;i=15251", {}),
                                "SourceB": ("V", "ns=1;i=15252", {}),
                                "State": ("V", "ns=1;i=15250", {}),
                            },
                        ),
                        "<DigitalOutPlaceholder>": (
                            "O",
                            "ns=1;i=1392",
                            {
                                "Fault": ("V", "ns=1;i=1393", {}),
                                "State": ("V", "ns=1;i=1401", {}),
                                "WriteState": (
                                    "M",
                                    "ns=1;i=1402",
                                    {"InputArguments": ("V", "ns=1;i=1403", {})},
                                ),
                            },
                        ),
                        "<DigitalPlaceholder>": (
                            "O",
                            "ns=1;i=1347",
                            {
                                "Fault": ("V", "ns=1;i=1348", {}),
                                "State": ("V", "ns=1;i=1356", {}),
                            },
                        ),
                        "<DiscreteArbitrationPlaceholder>": (
                            "O",
                            "ns=1;i=15256",
                            {
                                "ArbitrationMode": ("V", "ns=1;i=15268", {}),
                                "Fault": ("V", "ns=1;i=15257", {}),
                                "SourceA": ("V", "ns=1;i=15266", {}),
                                "SourceB": ("V", "ns=1;i=15267", {}),
                                "State": ("V", "ns=1;i=15265", {}),
                            },
                        ),
                        "<DiscreteOutPlaceholder>": (
                            "O",
                            "ns=1;i=1404",
                            {
                                "Fault": ("V", "ns=1;i=1405", {}),
                                "State": ("V", "ns=1;i=1413", {}),
                                "WriteValue": (
                                    "M",
                                    "ns=1;i=1414",
                                    {"InputArguments": ("V", "ns=1;i=1415", {})},
                                ),
                            },
                        ),
                        "<DiscretePlaceholder>": (
                            "O",
                            "ns=1;i=1357",
                            {
                                "Fault": ("V", "ns=1;i=1358", {}),
                                "State": ("V", "ns=1;i=1366", {}),
                            },
                        ),
                        "<ElectricChokePlaceholder>": (
                            "O",
                            "ns=1;i=15271",
                            {
                                "Abort": ("M", "ns=1;i=15289", {}),
                                "ActualPosition": ("V", "ns=1;i=15280", {}),
                                "Fault": ("V", "ns=1;i=15272", {}),
                                "Move": (
                                    "M",
                                    "ns=1;i=15287",
                                    {"InputArguments": ("V", "ns=1;i=15288", {})},
                                ),
                                "Moving": ("V", "ns=1;i=15281", {}),
                            },
                        ),
                        "<InstrumentArbitrationPlaceholder>": (
                            "O",
                            "ns=1;i=15212",
                            {
                                "ArbitrationMode": ("V", "ns=1;i=15237", {}),
                                "Fault": ("V", "ns=1;i=15213", {}),
                                "ProcessVariable": (
                                    "V",
                                    "ns=1;i=15221",
                                    {
                                        "EURange": ("V", "ns=1;i=15225", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=15226", {}),
                                    },
                                ),
                                "SourceA": ("V", "ns=1;i=15235", {}),
                                "SourceB": ("V", "ns=1;i=15236", {}),
                            },
                        ),
                        "<InstrumentOutPlaceholder>": (
                            "O",
                            "ns=1;i=1367",
                            {
                                "Fault": ("V", "ns=1;i=1368", {}),
                                "ProcessVariable": (
                                    "V",
                                    "ns=1;i=1376",
                                    {
                                        "EURange": ("V", "ns=1;i=1380", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1381", {}),
                                    },
                                ),
                                "WriteValue": (
                                    "M",
                                    "ns=1;i=1390",
                                    {"InputArguments": ("V", "ns=1;i=1391", {})},
                                ),
                            },
                        ),
                        "<InstrumentPlaceholder>": (
                            "O",
                            "ns=1;i=1324",
                            {
                                "Fault": ("V", "ns=1;i=1325", {}),
                                "ProcessVariable": (
                                    "V",
                                    "ns=1;i=1333",
                                    {
                                        "EURange": ("V", "ns=1;i=1337", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=1338", {}),
                                    },
                                ),
                            },
                        ),
                        "<MotorPlaceholder>": (
                            "O",
                            "ns=1;i=15290",
                            {
                                "Fault": ("V", "ns=1;i=15291", {}),
                                "Operation": ("V", "ns=1;i=15300", {}),
                                "Running": ("V", "ns=1;i=15299", {}),
                            },
                        ),
                        "<ValvePlaceholder>": (
                            "O",
                            "ns=1;i=1416",
                            {
                                "Fault": ("V", "ns=1;i=1417", {}),
                                "Move": (
                                    "M",
                                    "ns=1;i=1433",
                                    {"InputArguments": ("V", "ns=1;i=1434", {})},
                                ),
                                "Position": ("V", "ns=1;i=1425", {}),
                            },
                        ),
                    },
                ),
                "MDISCIMVObjectType": (
                    "OT",
                    "ns=1;i=15114",
                    {
                        "Abort": ("M", "ns=1;i=15176", {}),
                        "CommandRejected": ("V", "ns=1;i=15162", {}),
                        "DeviceCurrent": (
                            "V",
                            "ns=1;i=15138",
                            {
                                "EURange": ("V", "ns=1;i=15142", {}),
                                "EngineeringUnits": ("V", "ns=1;i=15143", {}),
                            },
                        ),
                        "FlowRate": (
                            "V",
                            "ns=1;i=15124",
                            {
                                "EURange": ("V", "ns=1;i=15128", {}),
                                "EngineeringUnits": ("V", "ns=1;i=15129", {}),
                            },
                        ),
                        "InletPressure": (
                            "V",
                            "ns=1;i=15144",
                            {
                                "EURange": ("V", "ns=1;i=15148", {}),
                                "EngineeringUnits": ("V", "ns=1;i=15149", {}),
                            },
                        ),
                        "InternalPressure": (
                            "V",
                            "ns=1;i=15150",
                            {
                                "EURange": ("V", "ns=1;i=15154", {}),
                                "EngineeringUnits": ("V", "ns=1;i=15155", {}),
                            },
                        ),
                        "MotorOperationsCount": (
                            "O",
                            "ns=1;i=15180",
                            {
                                "Count": ("V", "ns=1;i=15181", {}),
                                "SetCount": (
                                    "M",
                                    "ns=1;i=15182",
                                    {"InputArguments": ("V", "ns=1;i=15183", {})},
                                ),
                            },
                        ),
                        "Moving": ("V", "ns=1;i=15137", {}),
                        "NonDefeatableCloseInterlock": ("V", "ns=1;i=15165", {}),
                        "NonDefeatableCommandInProgressInterlock": (
                            "V",
                            "ns=1;i=15164",
                            {},
                        ),
                        "NonDefeatableOpenInterlock": ("V", "ns=1;i=15163", {}),
                        "OperationMode": ("V", "ns=1;i=15123", {}),
                        "OutletPressure": (
                            "V",
                            "ns=1;i=15156",
                            {
                                "EURange": ("V", "ns=1;i=15160", {}),
                                "EngineeringUnits": ("V", "ns=1;i=15161", {}),
                            },
                        ),
                        "Position": ("V", "ns=1;i=15136", {}),
                        "ResetTotalFlow": (
                            "M",
                            "ns=1;i=15166",
                            {"InputArguments": ("V", "ns=1;i=15167", {})},
                        ),
                        "SetFlowRate": (
                            "M",
                            "ns=1;i=15170",
                            {"InputArguments": ("V", "ns=1;i=15171", {})},
                        ),
                        "SetManual": (
                            "M",
                            "ns=1;i=15174",
                            {"InputArguments": ("V", "ns=1;i=15175", {})},
                        ),
                        "SetOperationMode": (
                            "M",
                            "ns=1;i=15168",
                            {"InputArguments": ("V", "ns=1;i=15169", {})},
                        ),
                        "SetPosition": (
                            "M",
                            "ns=1;i=15172",
                            {"InputArguments": ("V", "ns=1;i=15173", {})},
                        ),
                        "TargetFlowRate": (
                            "V",
                            "ns=1;i=15202",
                            {
                                "EURange": ("V", "ns=1;i=15302", {}),
                                "EngineeringUnits": ("V", "ns=1;i=15303", {}),
                            },
                        ),
                        "TargetPosition": ("V", "ns=1;i=15304", {}),
                        "TotalFlow": (
                            "V",
                            "ns=1;i=15130",
                            {
                                "EURange": ("V", "ns=1;i=15134", {}),
                                "EngineeringUnits": ("V", "ns=1;i=15135", {}),
                            },
                        ),
                        "TotalMotorRuntime": (
                            "O",
                            "ns=1;i=15005",
                            {
                                "Count": ("V", "ns=1;i=15006", {}),
                                "SetCount": (
                                    "M",
                                    "ns=1;i=15178",
                                    {"InputArguments": ("V", "ns=1;i=15179", {})},
                                ),
                            },
                        ),
                    },
                ),
                "MDISChokeObjectType": (
                    "OT",
                    "ns=1;i=1066",
                    {
                        "Abort": ("M", "ns=1;i=1159", {}),
                        "CalculatedPosition": ("V", "ns=1;i=1147", {}),
                        "CommandRejected": ("V", "ns=1;i=1150", {}),
                        "DefeatableCloseInterlock": ("V", "ns=1;i=1154", {}),
                        "DefeatableOpenInterlock": ("V", "ns=1;i=1152", {}),
                        "Move": (
                            "M",
                            "ns=1;i=1155",
                            {"InputArguments": ("V", "ns=1;i=1156", {})},
                        ),
                        "Moving": ("V", "ns=1;i=1149", {}),
                        "NonDefeatableCloseInterlock": ("V", "ns=1;i=1153", {}),
                        "NonDefeatableOpenInterlock": ("V", "ns=1;i=1151", {}),
                        "PositionInSteps": ("V", "ns=1;i=1148", {}),
                        "SetCalculatedPosition": (
                            "M",
                            "ns=1;i=1284",
                            {"InputArguments": ("V", "ns=1;i=1285", {})},
                        ),
                        "SetCalculatedPositionStatus": ("V", "ns=1;i=1314", {}),
                        "Step": (
                            "M",
                            "ns=1;i=1157",
                            {"InputArguments": ("V", "ns=1;i=1158", {})},
                        ),
                        "StepDurationClose": ("V", "ns=1;i=1163", {}),
                        "StepDurationOpen": ("V", "ns=1;i=1162", {}),
                        "TotalSteps": ("V", "ns=1;i=1164", {}),
                    },
                ),
                "MDISDigitalInstrumentObjectType": (
                    "OT",
                    "ns=1;i=889",
                    {
                        "MDISDigitalArbitrationObjectType": (
                            "OT",
                            "ns=1;i=15015",
                            {
                                "ArbitrationMode": ("V", "ns=1;i=15027", {}),
                                "SetArbitrationMode": (
                                    "M",
                                    "ns=1;i=15028",
                                    {"InputArguments": ("V", "ns=1;i=15029", {})},
                                ),
                                "SourceA": ("V", "ns=1;i=15025", {}),
                                "SourceB": ("V", "ns=1;i=15026", {}),
                            },
                        ),
                        "MDISDigitalOutObjectType": (
                            "OT",
                            "ns=1;i=1230",
                            {
                                "WriteState": (
                                    "M",
                                    "ns=1;i=1240",
                                    {"InputArguments": ("V", "ns=1;i=1241", {})},
                                )
                            },
                        ),
                        "State": ("V", "ns=1;i=970", {}),
                    },
                ),
                "MDISDiscreteInstrumentObjectType": (
                    "OT",
                    "ns=1;i=1214",
                    {
                        "MDISDiscreteArbitrationObjectType": (
                            "OT",
                            "ns=1;i=15032",
                            {
                                "ArbitrationMode": ("V", "ns=1;i=15544", {}),
                                "SetArbitrationMode": (
                                    "M",
                                    "ns=1;i=15545",
                                    {"InputArguments": ("V", "ns=1;i=15546", {})},
                                ),
                                "SourceA": ("V", "ns=1;i=15042", {}),
                                "SourceB": ("V", "ns=1;i=15043", {}),
                            },
                        ),
                        "MDISDiscreteOutObjectType": (
                            "OT",
                            "ns=1;i=1242",
                            {
                                "WriteValue": (
                                    "M",
                                    "ns=1;i=1252",
                                    {"InputArguments": ("V", "ns=1;i=1253", {})},
                                )
                            },
                        ),
                        "State": ("V", "ns=1;i=1223", {}),
                    },
                ),
                "MDISElectricChokeObjectType": (
                    "OT",
                    "ns=1;i=15076",
                    {
                        "Abort": ("M", "ns=1;i=15094", {}),
                        "ActualPosition": ("V", "ns=1;i=15085", {}),
                        "CommandRejected": ("V", "ns=1;i=15087", {}),
                        "DefeatableCloseInterlock": ("V", "ns=1;i=15091", {}),
                        "DefeatableOpenInterlock": ("V", "ns=1;i=15089", {}),
                        "Move": (
                            "M",
                            "ns=1;i=15092",
                            {"InputArguments": ("V", "ns=1;i=15093", {})},
                        ),
                        "Moving": ("V", "ns=1;i=15086", {}),
                        "NonDefeatableCloseInterlock": ("V", "ns=1;i=15090", {}),
                        "NonDefeatableOpenInterlock": ("V", "ns=1;i=15088", {}),
                    },
                ),
                "MDISInstrumentObjectType": (
                    "OT",
                    "ns=1;i=971",
                    {
                        "HHSetPoint": ("V", "ns=1;i=1062", {}),
                        "HHlimit": ("V", "ns=1;i=1058", {}),
                        "HSetPoint": ("V", "ns=1;i=1063", {}),
                        "Hlimit": ("V", "ns=1;i=1059", {}),
                        "LLSetPoint": ("V", "ns=1;i=1065", {}),
                        "LLlimit": ("V", "ns=1;i=1061", {}),
                        "LSetPoint": ("V", "ns=1;i=1064", {}),
                        "Llimit": ("V", "ns=1;i=1060", {}),
                        "MDISInstrumentArbitrationObjectType": (
                            "OT",
                            "ns=1;i=15547",
                            {
                                "ArbitrationMode": ("V", "ns=1;i=15072", {}),
                                "DiscrepancySetPoint": ("V", "ns=1;i=15073", {}),
                                "SetArbitrationMode": (
                                    "M",
                                    "ns=1;i=15074",
                                    {"InputArguments": ("V", "ns=1;i=15075", {})},
                                ),
                                "SourceA": ("V", "ns=1;i=15070", {}),
                                "SourceB": ("V", "ns=1;i=15071", {}),
                            },
                        ),
                        "MDISInstrumentOutObjectType": (
                            "OT",
                            "ns=1;i=1254",
                            {
                                "WriteValue": (
                                    "M",
                                    "ns=1;i=1277",
                                    {"InputArguments": ("V", "ns=1;i=1278", {})},
                                )
                            },
                        ),
                        "ProcessVariable": (
                            "V",
                            "ns=1;i=1052",
                            {
                                "EURange": ("V", "ns=1;i=1056", {}),
                                "EngineeringUnits": ("V", "ns=1;i=1057", {}),
                            },
                        ),
                    },
                ),
                "MDISMotorObjectType": (
                    "OT",
                    "ns=1;i=15190",
                    {
                        "DefeatableStartInterlock": ("V", "ns=1;i=15396", {}),
                        "DefeatableStopInterlock": ("V", "ns=1;i=15398", {}),
                        "NonDefeatableStartInterlock": ("V", "ns=1;i=15395", {}),
                        "NonDefeatableStopInterlock": ("V", "ns=1;i=15397", {}),
                        "Operation": ("V", "ns=1;i=15200", {}),
                        "Running": ("V", "ns=1;i=15199", {}),
                        "SetOperation": (
                            "M",
                            "ns=1;i=15209",
                            {"InputArguments": ("V", "ns=1;i=15210", {})},
                        ),
                        "Start": (
                            "M",
                            "ns=1;i=15205",
                            {"InputArguments": ("V", "ns=1;i=15206", {})},
                        ),
                        "Stop": (
                            "M",
                            "ns=1;i=15207",
                            {"InputArguments": ("V", "ns=1;i=15208", {})},
                        ),
                    },
                ),
                "MDISValveObjectType": (
                    "OT",
                    "ns=1;i=794",
                    {
                        "CloseTimeDuration": ("V", "ns=1;i=888", {}),
                        "CommandRejected": ("V", "ns=1;i=876", {}),
                        "DefeatableCloseInterlock": ("V", "ns=1;i=882", {}),
                        "DefeatableOpenInterlock": ("V", "ns=1;i=880", {}),
                        "LastCommand": ("V", "ns=1;i=878", {}),
                        "Move": (
                            "M",
                            "ns=1;i=883",
                            {"InputArguments": ("V", "ns=1;i=884", {})},
                        ),
                        "NonDefeatableCloseInterlock": ("V", "ns=1;i=881", {}),
                        "NonDefeatableOpenInterlock": ("V", "ns=1;i=879", {}),
                        "OpenTimeDuration": ("V", "ns=1;i=887", {}),
                        "Position": ("V", "ns=1;i=875", {}),
                        "SignatureRequestStatus": ("V", "ns=1;i=877", {}),
                    },
                ),
                "TagId": ("V", "ns=1;i=197", {}),
                "Warning": ("V", "ns=1;i=497", {}),
                "WarningCode": ("V", "ns=1;i=1166", {}),
            },
        ),
        "MDISCounterObjectType": (
            "OT",
            "ns=1;i=15098",
            {
                "Count": ("V", "ns=1;i=15099", {}),
                "SetCount": (
                    "M",
                    "ns=1;i=15100",
                    {"InputArguments": ("V", "ns=1;i=15101", {})},
                ),
            },
        ),
        "MDISInformationObjectType": (
            "OT",
            "ns=1;i=1471",
            {
                "MDISVersion": (
                    "V",
                    "ns=1;i=1476",
                    {
                        "Build": ("V", "ns=1;i=1479", {}),
                        "MajorVersion": ("V", "ns=1;i=1477", {}),
                        "MinorVersion": ("V", "ns=1;i=1478", {}),
                    },
                ),
                "Signatures": ("O", "ns=1;i=1475", {}),
                "TimeSynchronization": (
                    "O",
                    "ns=1;i=1472",
                    {
                        "SetTime": (
                            "M",
                            "ns=1;i=1473",
                            {"InputArguments": ("V", "ns=1;i=1474", {})},
                        )
                    },
                ),
            },
        ),
        "MDISTimeSyncObjectType": (
            "OT",
            "ns=1;i=1468",
            {
                "SetTime": (
                    "M",
                    "ns=1;i=1469",
                    {"InputArguments": ("V", "ns=1;i=1470", {})},
                )
            },
        ),
    },
    "reftypes": {
        "HasInterlock": ("RT", "ns=1;i=1183", {}),
        "HasSignature": ("RT", "ns=1;i=1286", {}),
        "InterlockFor": ("RT", "ns=1;i=1184", {}),
    },
    "vartypes": {
        "InterlockVariableType": ("VT", "ns=1;i=1279", {}),
        "MDISVersionVariableType": (
            "VT",
            "ns=1;i=1290",
            {
                "Build": ("V", "ns=1;i=1293", {}),
                "MajorVersion": ("V", "ns=1;i=1291", {}),
                "MinorVersion": ("V", "ns=1;i=1292", {}),
            },
        ),
    },
}
