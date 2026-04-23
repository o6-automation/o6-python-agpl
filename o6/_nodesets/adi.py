# AUTO-GENERATED — DO NOT EDIT
# source-sha256: f5f9a759c1f23ec0b79927894bc7ba4b463a1c127faa074c2867ec6e4773a1c9
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/ADI/"
_VERSION: str = "1.01"
_REQUIRED: list = [
    {"uri": "http://opcfoundation.org/UA/", "version": "1.03"},
    {"uri": "http://opcfoundation.org/UA/DI/", "version": "1.01"},
]
_STRUCTURES: list = []
_ENUMS: list = [
    (
        "ns=1;i=9378",
        "ExecutionCycleEnumeration",
        {
            "fields": [
                {"name": "IDLE", "value": 0, "display_name": "IDLE"},
                {"name": "DIAGNOSTIC", "value": 1, "display_name": "DIAGNOSTIC"},
                {"name": "CLEANING", "value": 2, "display_name": "CLEANING"},
                {"name": "CALIBRATION", "value": 4, "display_name": "CALIBRATION"},
                {"name": "VALIDATION", "value": 8, "display_name": "VALIDATION"},
                {"name": "SAMPLING", "value": 16, "display_name": "SAMPLING"},
                {
                    "name": "DIAGNOSTIC_WITH_GRAB_SAMPLE",
                    "value": 32769,
                    "display_name": "DIAGNOSTIC_WITH_GRAB_SAMPLE",
                },
                {
                    "name": "CLEANING_WITH_GRAB_SAMPLE",
                    "value": 32770,
                    "display_name": "CLEANING_WITH_GRAB_SAMPLE",
                },
                {
                    "name": "CALIBRATION_WITH_GRAB_SAMPLE",
                    "value": 32772,
                    "display_name": "CALIBRATION_WITH_GRAB_SAMPLE",
                },
                {
                    "name": "VALIDATION_WITH_GRAB_SAMPLE",
                    "value": 32776,
                    "display_name": "VALIDATION_WITH_GRAB_SAMPLE",
                },
                {
                    "name": "SAMPLING_WITH_GRAB_SAMPLE",
                    "value": 32784,
                    "display_name": "SAMPLING_WITH_GRAB_SAMPLE",
                },
            ]
        },
    ),
    (
        "ns=1;i=3003",
        "AcquisitionResultStatusEnumeration",
        {
            "fields": [
                {"name": "NOT_USED", "value": 0, "display_name": "NOT_USED"},
                {"name": "GOOD", "value": 1, "display_name": "GOOD"},
                {"name": "BAD", "value": 2, "display_name": "BAD"},
                {"name": "UNKNOWN", "value": 3, "display_name": "UNKNOWN"},
                {"name": "PARTIAL", "value": 4, "display_name": "PARTIAL"},
            ]
        },
    ),
    (
        "ns=1;i=3009",
        "AlarmStateEnumeration",
        {
            "fields": [
                {"name": "NORMAL_0", "value": 0, "display_name": "NORMAL_0"},
                {"name": "WARNING_LOW_1", "value": 1, "display_name": "WARNING_LOW_1"},
                {
                    "name": "WARNING_HIGH_2",
                    "value": 2,
                    "display_name": "WARNING_HIGH_2",
                },
                {"name": "WARNING_4", "value": 4, "display_name": "WARNING_4"},
                {"name": "ALARM_LOW_8", "value": 8, "display_name": "ALARM_LOW_8"},
                {"name": "ALARM_HIGH_16", "value": 16, "display_name": "ALARM_HIGH_16"},
                {"name": "ALARM_32", "value": 32, "display_name": "ALARM_32"},
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = ([], ["ns=1;i=9378", "ns=1;i=3003", "ns=1;i=3009"])
_NODES: dict = {
    "datatypes": {
        "AcquisitionResultStatusEnumeration": (
            "D",
            "ns=1;i=3003",
            {"EnumStrings": ("V", "ns=1;i=13027", {})},
        ),
        "AlarmStateEnumeration": (
            "D",
            "ns=1;i=3009",
            {"EnumValues": ("V", "ns=1;i=13063", {})},
        ),
        "ExecutionCycleEnumeration": (
            "D",
            "ns=1;i=9378",
            {"EnumValues": ("V", "ns=1;i=13026", {})},
        ),
    },
    "objects": {
        "<Source>": ("V", "ns=1;i=13040", {}),
        "<User defined Input#>": ("V", "ns=1;i=13036", {}),
        "<User defined Output#>": (
            "V",
            "ns=1;i=13045",
            {"AlarmState": ("V", "ns=1;i=13049", {})},
        ),
        "Opc.Ua.Adi": (
            "V",
            "ns=1;i=13064",
            {
                "Deprecated": ("V", "ns=1;i=8003", {}),
                "NamespaceUri": ("V", "ns=1;i=13066", {}),
            },
        ),
        "http://opcfoundation.org/UA/ADI/": (
            "O",
            "ns=1;i=15001",
            {
                "DefaultAccessRestrictions": ("V", "ns=1;i=15033", {}),
                "DefaultRolePermissions": ("V", "ns=1;i=15031", {}),
                "DefaultUserRolePermissions": ("V", "ns=1;i=15032", {}),
                "IsNamespaceSubset": ("V", "ns=1;i=15005", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=15004", {}),
                "NamespaceUri": ("V", "ns=1;i=15002", {}),
                "NamespaceVersion": ("V", "ns=1;i=15003", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=15006", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=15007", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=15008", {}),
            },
        ),
    },
    "objtypes": {
        "AccessorySlotStateMachineType": (
            "OT",
            "ns=1;i=1018",
            {
                "Empty": (
                    "O",
                    "ns=1;i=12842",
                    {"StateNumber": ("V", "ns=1;i=12843", {})},
                ),
                "EmptyToInsertingTransition": (
                    "O",
                    "ns=1;i=12854",
                    {"TransitionNumber": ("V", "ns=1;i=12855", {})},
                ),
                "EmptyToShutdownTransition": (
                    "O",
                    "ns=1;i=12868",
                    {"TransitionNumber": ("V", "ns=1;i=12869", {})},
                ),
                "Inserting": (
                    "O",
                    "ns=1;i=12844",
                    {"StateNumber": ("V", "ns=1;i=12845", {})},
                ),
                "InsertingToInstalledTransition": (
                    "O",
                    "ns=1;i=12860",
                    {"TransitionNumber": ("V", "ns=1;i=12861", {})},
                ),
                "InsertingToRemovingTransition": (
                    "O",
                    "ns=1;i=12858",
                    {"TransitionNumber": ("V", "ns=1;i=12859", {})},
                ),
                "InsertingToShutdownTransition": (
                    "O",
                    "ns=1;i=12870",
                    {"TransitionNumber": ("V", "ns=1;i=12871", {})},
                ),
                "InsertingTransition": (
                    "O",
                    "ns=1;i=12856",
                    {"TransitionNumber": ("V", "ns=1;i=12857", {})},
                ),
                "Installed": (
                    "O",
                    "ns=1;i=12846",
                    {"StateNumber": ("V", "ns=1;i=12847", {})},
                ),
                "InstalledToRemovingTransition": (
                    "O",
                    "ns=1;i=12862",
                    {"TransitionNumber": ("V", "ns=1;i=12863", {})},
                ),
                "InstalledToShutdownTransition": (
                    "O",
                    "ns=1;i=12872",
                    {"TransitionNumber": ("V", "ns=1;i=12873", {})},
                ),
                "Powerup": (
                    "O",
                    "ns=1;i=12840",
                    {"StateNumber": ("V", "ns=1;i=12841", {})},
                ),
                "PowerupToEmptyTransition": (
                    "O",
                    "ns=1;i=12852",
                    {"TransitionNumber": ("V", "ns=1;i=12853", {})},
                ),
                "Removing": (
                    "O",
                    "ns=1;i=12848",
                    {"StateNumber": ("V", "ns=1;i=12849", {})},
                ),
                "RemovingToEmptyTransition": (
                    "O",
                    "ns=1;i=12866",
                    {"TransitionNumber": ("V", "ns=1;i=12867", {})},
                ),
                "RemovingToShutdownTransition": (
                    "O",
                    "ns=1;i=12874",
                    {"TransitionNumber": ("V", "ns=1;i=12875", {})},
                ),
                "RemovingTransition": (
                    "O",
                    "ns=1;i=12864",
                    {"TransitionNumber": ("V", "ns=1;i=12865", {})},
                ),
                "Shutdown": (
                    "O",
                    "ns=1;i=12850",
                    {"StateNumber": ("V", "ns=1;i=12851", {})},
                ),
            },
        ),
        "AccessorySlotType": (
            "OT",
            "ns=1;i=1017",
            {
                "<AccessoryIdentifier>": (
                    "O",
                    "ns=1;i=12800",
                    {
                        "Configuration": ("O", "ns=1;i=12821", {}),
                        "FactorySettings": ("O", "ns=1;i=12825", {}),
                        "IsHotSwappable": ("V", "ns=1;i=12827", {}),
                        "IsReady": ("V", "ns=1;i=12828", {}),
                        "Status": ("O", "ns=1;i=12823", {}),
                    },
                ),
                "AccessorySlotStateMachine": (
                    "O",
                    "ns=1;i=12788",
                    {
                        "CurrentState": (
                            "V",
                            "ns=1;i=12789",
                            {"Id": ("V", "ns=1;i=12790", {})},
                        )
                    },
                ),
                "IsEnabled": ("V", "ns=1;i=12787", {}),
                "IsHotSwappable": ("V", "ns=1;i=12786", {}),
            },
        ),
        "AccessoryType": (
            "OT",
            "ns=1;i=1019",
            {
                "Configuration": ("O", "ns=1;i=12898", {}),
                "DetectorType": ("OT", "ns=1;i=9350", {}),
                "FactorySettings": ("O", "ns=1;i=12902", {}),
                "GcOvenType": ("OT", "ns=1;i=1020", {}),
                "IsHotSwappable": ("V", "ns=1;i=12904", {}),
                "IsReady": ("V", "ns=1;i=12905", {}),
                "SmartSamplingSystemType": ("OT", "ns=1;i=9359", {}),
                "SourceType": ("OT", "ns=1;i=9368", {}),
                "Status": ("O", "ns=1;i=12900", {}),
            },
        ),
        "AnalyserChannelLocalStateType": ("OT", "ns=1;i=1005", {}),
        "AnalyserChannelMaintenanceStateType": ("OT", "ns=1;i=1006", {}),
        "AnalyserChannelOperatingExecuteStateType": ("OT", "ns=1;i=8964", {}),
        "AnalyserChannelOperatingStateType": ("OT", "ns=1;i=1004", {}),
        "AnalyserChannelStateMachineType": (
            "OT",
            "ns=1;i=1007",
            {
                "Local": (
                    "O",
                    "ns=1;i=10000",
                    {"StateNumber": ("V", "ns=1;i=10001", {})},
                ),
                "LocalSubStateMachine": (
                    "O",
                    "ns=1;i=9972",
                    {
                        "CurrentState": (
                            "V",
                            "ns=1;i=9973",
                            {"Id": ("V", "ns=1;i=9974", {})},
                        )
                    },
                ),
                "LocalToMaintenanceTransition": (
                    "O",
                    "ns=1;i=10012",
                    {"TransitionNumber": ("V", "ns=1;i=10013", {})},
                ),
                "LocalToOperatingTransition": (
                    "O",
                    "ns=1;i=10010",
                    {"TransitionNumber": ("V", "ns=1;i=10011", {})},
                ),
                "LocalToSlaveModeTransition": (
                    "O",
                    "ns=1;i=10020",
                    {"TransitionNumber": ("V", "ns=1;i=10021", {})},
                ),
                "Maintenance": (
                    "O",
                    "ns=1;i=10002",
                    {"StateNumber": ("V", "ns=1;i=10003", {})},
                ),
                "MaintenanceSubStateMachine": (
                    "O",
                    "ns=1;i=9984",
                    {
                        "CurrentState": (
                            "V",
                            "ns=1;i=9985",
                            {"Id": ("V", "ns=1;i=9986", {})},
                        )
                    },
                ),
                "MaintenanceToLocalTransition": (
                    "O",
                    "ns=1;i=10016",
                    {"TransitionNumber": ("V", "ns=1;i=10017", {})},
                ),
                "MaintenanceToOperatingTransition": (
                    "O",
                    "ns=1;i=10014",
                    {"TransitionNumber": ("V", "ns=1;i=10015", {})},
                ),
                "MaintenanceToSlaveModeTransition": (
                    "O",
                    "ns=1;i=10022",
                    {"TransitionNumber": ("V", "ns=1;i=10023", {})},
                ),
                "Operating": (
                    "O",
                    "ns=1;i=9998",
                    {"StateNumber": ("V", "ns=1;i=9999", {})},
                ),
                "OperatingSubStateMachine": (
                    "O",
                    "ns=1;i=9948",
                    {
                        "CurrentState": (
                            "V",
                            "ns=1;i=9949",
                            {"Id": ("V", "ns=1;i=9950", {})},
                        ),
                        "OperatingExecuteSubStateMachine": (
                            "O",
                            "ns=1;i=9960",
                            {
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=9961",
                                    {"Id": ("V", "ns=1;i=9962", {})},
                                )
                            },
                        ),
                    },
                ),
                "OperatingToLocalTransition": (
                    "O",
                    "ns=1;i=10006",
                    {"TransitionNumber": ("V", "ns=1;i=10007", {})},
                ),
                "OperatingToMaintenanceTransition": (
                    "O",
                    "ns=1;i=10008",
                    {"TransitionNumber": ("V", "ns=1;i=10009", {})},
                ),
                "OperatingToSlaveModeTransition": (
                    "O",
                    "ns=1;i=10018",
                    {"TransitionNumber": ("V", "ns=1;i=10019", {})},
                ),
                "SlaveMode": (
                    "O",
                    "ns=1;i=9996",
                    {"StateNumber": ("V", "ns=1;i=9997", {})},
                ),
                "SlaveModeToOperatingTransition": (
                    "O",
                    "ns=1;i=10004",
                    {"TransitionNumber": ("V", "ns=1;i=10005", {})},
                ),
            },
        ),
        "AnalyserChannelType": (
            "OT",
            "ns=1;i=1003",
            {
                "<AccessorySlotIdentifier>": (
                    "O",
                    "ns=1;i=9916",
                    {
                        "AccessorySlotStateMachine": (
                            "O",
                            "ns=1;i=9920",
                            {
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=9921",
                                    {"Id": ("V", "ns=1;i=9922", {})},
                                )
                            },
                        ),
                        "IsEnabled": ("V", "ns=1;i=9919", {}),
                        "IsHotSwappable": ("V", "ns=1;i=9918", {}),
                        "SupportedTypes": ("O", "ns=1;i=9917", {}),
                    },
                ),
                "<GroupIdentifier>": ("O", "ns=1;i=9788", {}),
                "<StreamIdentifier>": (
                    "O",
                    "ns=1;i=9790",
                    {
                        "AcquisitionData": ("O", "ns=1;i=9910", {}),
                        "AcquisitionSettings": ("O", "ns=1;i=9906", {}),
                        "AcquisitionStatus": ("O", "ns=1;i=9908", {}),
                        "ChemometricModelSettings": ("O", "ns=1;i=9912", {}),
                        "Configuration": ("O", "ns=1;i=9902", {}),
                        "Context": ("O", "ns=1;i=9914", {}),
                        "Status": ("O", "ns=1;i=9904", {}),
                    },
                ),
                "ChannelStateMachine": (
                    "O",
                    "ns=1;i=9728",
                    {
                        "CurrentState": (
                            "V",
                            "ns=1;i=9729",
                            {"Id": ("V", "ns=1;i=9730", {})},
                        ),
                        "OperatingSubStateMachine": (
                            "O",
                            "ns=1;i=9740",
                            {
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=9741",
                                    {"Id": ("V", "ns=1;i=9742", {})},
                                ),
                                "OperatingExecuteSubStateMachine": (
                                    "O",
                                    "ns=1;i=9752",
                                    {
                                        "CurrentState": (
                                            "V",
                                            "ns=1;i=9753",
                                            {"Id": ("V", "ns=1;i=9754", {})},
                                        )
                                    },
                                ),
                            },
                        ),
                    },
                ),
                "Configuration": (
                    "O",
                    "ns=1;i=9724",
                    {"IsEnabled": ("V", "ns=1;i=9715", {})},
                ),
                "MethodSet": (
                    "O",
                    "ns=1;i=9679",
                    {
                        "Abort": ("M", "ns=1;i=9710", {}),
                        "Clear": ("M", "ns=1;i=9711", {}),
                        "GotoMaintenance": ("M", "ns=1;i=9700", {}),
                        "GotoOperating": ("M", "ns=1;i=9699", {}),
                        "Hold": ("M", "ns=1;i=9706", {}),
                        "Reset": ("M", "ns=1;i=9703", {}),
                        "Start": ("M", "ns=1;i=9704", {}),
                        "StartSingleAcquisition": (
                            "M",
                            "ns=1;i=9701",
                            {"InputArguments": ("V", "ns=1;i=9702", {})},
                        ),
                        "Stop": ("M", "ns=1;i=9705", {}),
                        "Suspend": ("M", "ns=1;i=9708", {}),
                        "Unhold": ("M", "ns=1;i=9707", {}),
                        "Unsuspend": ("M", "ns=1;i=9709", {}),
                    },
                ),
                "ParameterSet": (
                    "O",
                    "ns=1;i=9677",
                    {"ChannelId": ("V", "ns=1;i=9712", {})},
                ),
                "Status": (
                    "O",
                    "ns=1;i=9726",
                    {
                        "ActiveStream": ("V", "ns=1;i=9721", {}),
                        "DiagnosticStatus": ("V", "ns=1;i=9718", {}),
                    },
                ),
            },
        ),
        "AnalyserChannel_OperatingModeExecuteSubStateMachineType": (
            "OT",
            "ns=1;i=1009",
            {
                "AnalyseCalibrationSample": (
                    "O",
                    "ns=1;i=10209",
                    {"StateNumber": ("V", "ns=1;i=10210", {})},
                ),
                "AnalyseCalibrationSampleToPublishResultsTransition": (
                    "O",
                    "ns=1;i=10255",
                    {"TransitionNumber": ("V", "ns=1;i=10256", {})},
                ),
                "AnalyseCalibrationSampleTransition": (
                    "O",
                    "ns=1;i=10253",
                    {"TransitionNumber": ("V", "ns=1;i=10254", {})},
                ),
                "AnalyseSample": (
                    "O",
                    "ns=1;i=10225",
                    {"StateNumber": ("V", "ns=1;i=10226", {})},
                ),
                "AnalyseSampleToPublishResultsTransition": (
                    "O",
                    "ns=1;i=10287",
                    {"TransitionNumber": ("V", "ns=1;i=10288", {})},
                ),
                "AnalyseSampleTransition": (
                    "O",
                    "ns=1;i=10285",
                    {"TransitionNumber": ("V", "ns=1;i=10286", {})},
                ),
                "AnalyseValidationSample": (
                    "O",
                    "ns=1;i=10217",
                    {"StateNumber": ("V", "ns=1;i=10218", {})},
                ),
                "AnalyseValidationSampleToPublishResultsTransition": (
                    "O",
                    "ns=1;i=10271",
                    {"TransitionNumber": ("V", "ns=1;i=10272", {})},
                ),
                "AnalyseValidationSampleTransition": (
                    "O",
                    "ns=1;i=10269",
                    {"TransitionNumber": ("V", "ns=1;i=10270", {})},
                ),
                "Cleaning": (
                    "O",
                    "ns=1;i=10233",
                    {"StateNumber": ("V", "ns=1;i=10234", {})},
                ),
                "CleaningToPublishResultsTransition": (
                    "O",
                    "ns=1;i=10303",
                    {"TransitionNumber": ("V", "ns=1;i=10304", {})},
                ),
                "CleaningTransition": (
                    "O",
                    "ns=1;i=10301",
                    {"TransitionNumber": ("V", "ns=1;i=10302", {})},
                ),
                "CleanupSamplingSystem": (
                    "O",
                    "ns=1;i=10239",
                    {"StateNumber": ("V", "ns=1;i=10240", {})},
                ),
                "CleanupSamplingSystemToSelectExecutionCycleTransition": (
                    "O",
                    "ns=1;i=10315",
                    {"TransitionNumber": ("V", "ns=1;i=10316", {})},
                ),
                "CleanupSamplingSystemTransition": (
                    "O",
                    "ns=1;i=10313",
                    {"TransitionNumber": ("V", "ns=1;i=10314", {})},
                ),
                "Diagnostic": (
                    "O",
                    "ns=1;i=10229",
                    {"StateNumber": ("V", "ns=1;i=10230", {})},
                ),
                "DiagnosticToPublishResultsTransition": (
                    "O",
                    "ns=1;i=10295",
                    {"TransitionNumber": ("V", "ns=1;i=10296", {})},
                ),
                "DiagnosticTransition": (
                    "O",
                    "ns=1;i=10293",
                    {"TransitionNumber": ("V", "ns=1;i=10294", {})},
                ),
                "EjectGrabSample": (
                    "O",
                    "ns=1;i=10237",
                    {"StateNumber": ("V", "ns=1;i=10238", {})},
                ),
                "EjectGrabSampleToCleanupSamplingSystemTransition": (
                    "O",
                    "ns=1;i=10311",
                    {"TransitionNumber": ("V", "ns=1;i=10312", {})},
                ),
                "EjectGrabSampleTransition": (
                    "O",
                    "ns=1;i=10309",
                    {"TransitionNumber": ("V", "ns=1;i=10310", {})},
                ),
                "ExtractCalibrationSample": (
                    "O",
                    "ns=1;i=10205",
                    {"StateNumber": ("V", "ns=1;i=10206", {})},
                ),
                "ExtractCalibrationSampleToPrepareCalibrationSampleTransition": (
                    "O",
                    "ns=1;i=10247",
                    {"TransitionNumber": ("V", "ns=1;i=10248", {})},
                ),
                "ExtractCalibrationSampleTransition": (
                    "O",
                    "ns=1;i=10245",
                    {"TransitionNumber": ("V", "ns=1;i=10246", {})},
                ),
                "ExtractSample": (
                    "O",
                    "ns=1;i=10221",
                    {"StateNumber": ("V", "ns=1;i=10222", {})},
                ),
                "ExtractSampleToPrepareSampleTransition": (
                    "O",
                    "ns=1;i=10279",
                    {"TransitionNumber": ("V", "ns=1;i=10280", {})},
                ),
                "ExtractSampleTransition": (
                    "O",
                    "ns=1;i=10277",
                    {"TransitionNumber": ("V", "ns=1;i=10278", {})},
                ),
                "ExtractValidationSample": (
                    "O",
                    "ns=1;i=10213",
                    {"StateNumber": ("V", "ns=1;i=10214", {})},
                ),
                "ExtractValidationSampleToPrepareValidationSampleTransition": (
                    "O",
                    "ns=1;i=10263",
                    {"TransitionNumber": ("V", "ns=1;i=10264", {})},
                ),
                "ExtractValidationSampleTransition": (
                    "O",
                    "ns=1;i=10261",
                    {"TransitionNumber": ("V", "ns=1;i=10262", {})},
                ),
                "PrepareCalibrationSample": (
                    "O",
                    "ns=1;i=10207",
                    {"StateNumber": ("V", "ns=1;i=10208", {})},
                ),
                "PrepareCalibrationSampleToAnalyseCalibrationSampleTransition": (
                    "O",
                    "ns=1;i=10251",
                    {"TransitionNumber": ("V", "ns=1;i=10252", {})},
                ),
                "PrepareCalibrationSampleTransition": (
                    "O",
                    "ns=1;i=10249",
                    {"TransitionNumber": ("V", "ns=1;i=10250", {})},
                ),
                "PrepareSample": (
                    "O",
                    "ns=1;i=10223",
                    {"StateNumber": ("V", "ns=1;i=10224", {})},
                ),
                "PrepareSampleToAnalyseSampleTransition": (
                    "O",
                    "ns=1;i=10283",
                    {"TransitionNumber": ("V", "ns=1;i=10284", {})},
                ),
                "PrepareSampleTransition": (
                    "O",
                    "ns=1;i=10281",
                    {"TransitionNumber": ("V", "ns=1;i=10282", {})},
                ),
                "PrepareValidationSample": (
                    "O",
                    "ns=1;i=10215",
                    {"StateNumber": ("V", "ns=1;i=10216", {})},
                ),
                "PrepareValidationSampleToAnalyseValidationSampleTransition": (
                    "O",
                    "ns=1;i=10267",
                    {"TransitionNumber": ("V", "ns=1;i=10268", {})},
                ),
                "PrepareValidationSampleTransition": (
                    "O",
                    "ns=1;i=10265",
                    {"TransitionNumber": ("V", "ns=1;i=10266", {})},
                ),
                "PublishResults": (
                    "O",
                    "ns=1;i=10235",
                    {"StateNumber": ("V", "ns=1;i=10236", {})},
                ),
                "PublishResultsToCleanupSamplingSystemTransition": (
                    "O",
                    "ns=1;i=10305",
                    {"TransitionNumber": ("V", "ns=1;i=10306", {})},
                ),
                "PublishResultsToEjectGrabSampleTransition": (
                    "O",
                    "ns=1;i=10307",
                    {"TransitionNumber": ("V", "ns=1;i=10308", {})},
                ),
                "SelectExecutionCycle": (
                    "O",
                    "ns=1;i=10201",
                    {"StateNumber": ("V", "ns=1;i=10202", {})},
                ),
                "SelectExecutionCycleToWaitForCalibrationTriggerTransition": (
                    "O",
                    "ns=1;i=10241",
                    {"TransitionNumber": ("V", "ns=1;i=10242", {})},
                ),
                "SelectExecutionCycleToWaitForCleaningTriggerTransition": (
                    "O",
                    "ns=1;i=10297",
                    {"TransitionNumber": ("V", "ns=1;i=10298", {})},
                ),
                "SelectExecutionCycleToWaitForDiagnosticTriggerTransition": (
                    "O",
                    "ns=1;i=10289",
                    {"TransitionNumber": ("V", "ns=1;i=10290", {})},
                ),
                "SelectExecutionCycleToWaitForSampleTriggerTransition": (
                    "O",
                    "ns=1;i=10273",
                    {"TransitionNumber": ("V", "ns=1;i=10274", {})},
                ),
                "SelectExecutionCycleToWaitForValidationTriggerTransition": (
                    "O",
                    "ns=1;i=10257",
                    {"TransitionNumber": ("V", "ns=1;i=10258", {})},
                ),
                "WaitForCalibrationTrigger": (
                    "O",
                    "ns=1;i=10203",
                    {"StateNumber": ("V", "ns=1;i=10204", {})},
                ),
                "WaitForCalibrationTriggerToExtractCalibrationSampleTransition": (
                    "O",
                    "ns=1;i=10243",
                    {"TransitionNumber": ("V", "ns=1;i=10244", {})},
                ),
                "WaitForCleaningTrigger": (
                    "O",
                    "ns=1;i=10231",
                    {"StateNumber": ("V", "ns=1;i=10232", {})},
                ),
                "WaitForCleaningTriggerToCleaningTransition": (
                    "O",
                    "ns=1;i=10299",
                    {"TransitionNumber": ("V", "ns=1;i=10300", {})},
                ),
                "WaitForDiagnosticTrigger": (
                    "O",
                    "ns=1;i=10227",
                    {"StateNumber": ("V", "ns=1;i=10228", {})},
                ),
                "WaitForDiagnosticTriggerToDiagnosticTransition": (
                    "O",
                    "ns=1;i=10291",
                    {"TransitionNumber": ("V", "ns=1;i=10292", {})},
                ),
                "WaitForSampleTrigger": (
                    "O",
                    "ns=1;i=10219",
                    {"StateNumber": ("V", "ns=1;i=10220", {})},
                ),
                "WaitForSampleTriggerToExtractSampleTransition": (
                    "O",
                    "ns=1;i=10275",
                    {"TransitionNumber": ("V", "ns=1;i=10276", {})},
                ),
                "WaitForValidationTrigger": (
                    "O",
                    "ns=1;i=10211",
                    {"StateNumber": ("V", "ns=1;i=10212", {})},
                ),
                "WaitForValidationTriggerToExtractValidationSampleTransition": (
                    "O",
                    "ns=1;i=10259",
                    {"TransitionNumber": ("V", "ns=1;i=10260", {})},
                ),
            },
        ),
        "AnalyserChannel_OperatingModeSubStateMachineType": (
            "OT",
            "ns=1;i=1008",
            {
                "Aborted": (
                    "O",
                    "ns=1;i=10078",
                    {"StateNumber": ("V", "ns=1;i=10079", {})},
                ),
                "AbortedToClearingTransition": (
                    "O",
                    "ns=1;i=10134",
                    {"TransitionNumber": ("V", "ns=1;i=10135", {})},
                ),
                "Aborting": (
                    "O",
                    "ns=1;i=10076",
                    {"StateNumber": ("V", "ns=1;i=10077", {})},
                ),
                "AbortingToAbortedTransition": (
                    "O",
                    "ns=1;i=10132",
                    {"TransitionNumber": ("V", "ns=1;i=10133", {})},
                ),
                "Clearing": (
                    "O",
                    "ns=1;i=10080",
                    {"StateNumber": ("V", "ns=1;i=10081", {})},
                ),
                "ClearingToStoppedTransition": (
                    "O",
                    "ns=1;i=10136",
                    {"TransitionNumber": ("V", "ns=1;i=10137", {})},
                ),
                "Complete": (
                    "O",
                    "ns=1;i=10060",
                    {"StateNumber": ("V", "ns=1;i=10061", {})},
                ),
                "CompleteToAbortingTransition": (
                    "O",
                    "ns=1;i=10174",
                    {"TransitionNumber": ("V", "ns=1;i=10175", {})},
                ),
                "CompleteToStoppedTransition": (
                    "O",
                    "ns=1;i=10100",
                    {"TransitionNumber": ("V", "ns=1;i=10101", {})},
                ),
                "CompleteToStoppingTransition": (
                    "O",
                    "ns=1;i=10148",
                    {"TransitionNumber": ("V", "ns=1;i=10149", {})},
                ),
                "Completing": (
                    "O",
                    "ns=1;i=10058",
                    {"StateNumber": ("V", "ns=1;i=10059", {})},
                ),
                "CompletingToAbortingTransition": (
                    "O",
                    "ns=1;i=10172",
                    {"TransitionNumber": ("V", "ns=1;i=10173", {})},
                ),
                "CompletingToCompleteTransition": (
                    "O",
                    "ns=1;i=10098",
                    {"TransitionNumber": ("V", "ns=1;i=10099", {})},
                ),
                "CompletingToStoppingTransition": (
                    "O",
                    "ns=1;i=10146",
                    {"TransitionNumber": ("V", "ns=1;i=10147", {})},
                ),
                "CompletingTransition": (
                    "O",
                    "ns=1;i=10096",
                    {"TransitionNumber": ("V", "ns=1;i=10097", {})},
                ),
                "Execute": (
                    "O",
                    "ns=1;i=10056",
                    {"StateNumber": ("V", "ns=1;i=10057", {})},
                ),
                "ExecuteToAbortingTransition": (
                    "O",
                    "ns=1;i=10170",
                    {"TransitionNumber": ("V", "ns=1;i=10171", {})},
                ),
                "ExecuteToCompletingTransition": (
                    "O",
                    "ns=1;i=10094",
                    {"TransitionNumber": ("V", "ns=1;i=10095", {})},
                ),
                "ExecuteToHoldingTransition": (
                    "O",
                    "ns=1;i=10102",
                    {"TransitionNumber": ("V", "ns=1;i=10103", {})},
                ),
                "ExecuteToStoppingTransition": (
                    "O",
                    "ns=1;i=10144",
                    {"TransitionNumber": ("V", "ns=1;i=10145", {})},
                ),
                "ExecuteToSuspendingTransition": (
                    "O",
                    "ns=1;i=10116",
                    {"TransitionNumber": ("V", "ns=1;i=10117", {})},
                ),
                "Held": (
                    "O",
                    "ns=1;i=10070",
                    {"StateNumber": ("V", "ns=1;i=10071", {})},
                ),
                "HeldToAbortingTransition": (
                    "O",
                    "ns=1;i=10184",
                    {"TransitionNumber": ("V", "ns=1;i=10185", {})},
                ),
                "HeldToStoppingTransition": (
                    "O",
                    "ns=1;i=10158",
                    {"TransitionNumber": ("V", "ns=1;i=10159", {})},
                ),
                "HeldToUnholdingTransition": (
                    "O",
                    "ns=1;i=10108",
                    {"TransitionNumber": ("V", "ns=1;i=10109", {})},
                ),
                "Holding": (
                    "O",
                    "ns=1;i=10068",
                    {"StateNumber": ("V", "ns=1;i=10069", {})},
                ),
                "HoldingToAbortingTransition": (
                    "O",
                    "ns=1;i=10182",
                    {"TransitionNumber": ("V", "ns=1;i=10183", {})},
                ),
                "HoldingToHeldTransition": (
                    "O",
                    "ns=1;i=10106",
                    {"TransitionNumber": ("V", "ns=1;i=10107", {})},
                ),
                "HoldingToStoppingTransition": (
                    "O",
                    "ns=1;i=10156",
                    {"TransitionNumber": ("V", "ns=1;i=10157", {})},
                ),
                "HoldingTransition": (
                    "O",
                    "ns=1;i=10104",
                    {"TransitionNumber": ("V", "ns=1;i=10105", {})},
                ),
                "Idle": (
                    "O",
                    "ns=1;i=10052",
                    {"StateNumber": ("V", "ns=1;i=10053", {})},
                ),
                "IdleToAbortingTransition": (
                    "O",
                    "ns=1;i=10166",
                    {"TransitionNumber": ("V", "ns=1;i=10167", {})},
                ),
                "IdleToStartingTransition": (
                    "O",
                    "ns=1;i=10088",
                    {"TransitionNumber": ("V", "ns=1;i=10089", {})},
                ),
                "IdleToStoppingTransition": (
                    "O",
                    "ns=1;i=10140",
                    {"TransitionNumber": ("V", "ns=1;i=10141", {})},
                ),
                "OperatingExecuteSubStateMachine": (
                    "O",
                    "ns=1;i=10036",
                    {
                        "CurrentState": (
                            "V",
                            "ns=1;i=10037",
                            {"Id": ("V", "ns=1;i=10038", {})},
                        )
                    },
                ),
                "Resetting": (
                    "O",
                    "ns=1;i=10050",
                    {"StateNumber": ("V", "ns=1;i=10051", {})},
                ),
                "ResettingToAbortingTransition": (
                    "O",
                    "ns=1;i=10164",
                    {"TransitionNumber": ("V", "ns=1;i=10165", {})},
                ),
                "ResettingToIdleTransition": (
                    "O",
                    "ns=1;i=10086",
                    {"TransitionNumber": ("V", "ns=1;i=10087", {})},
                ),
                "ResettingToStoppingTransition": (
                    "O",
                    "ns=1;i=10138",
                    {"TransitionNumber": ("V", "ns=1;i=10139", {})},
                ),
                "ResettingTransition": (
                    "O",
                    "ns=1;i=10084",
                    {"TransitionNumber": ("V", "ns=1;i=10085", {})},
                ),
                "Starting": (
                    "O",
                    "ns=1;i=10054",
                    {"StateNumber": ("V", "ns=1;i=10055", {})},
                ),
                "StartingToAbortingTransition": (
                    "O",
                    "ns=1;i=10168",
                    {"TransitionNumber": ("V", "ns=1;i=10169", {})},
                ),
                "StartingToExecuteTransition": (
                    "O",
                    "ns=1;i=10092",
                    {"TransitionNumber": ("V", "ns=1;i=10093", {})},
                ),
                "StartingToStoppingTransition": (
                    "O",
                    "ns=1;i=10142",
                    {"TransitionNumber": ("V", "ns=1;i=10143", {})},
                ),
                "StartingTransition": (
                    "O",
                    "ns=1;i=10090",
                    {"TransitionNumber": ("V", "ns=1;i=10091", {})},
                ),
                "Stopped": (
                    "O",
                    "ns=1;i=10048",
                    {"StateNumber": ("V", "ns=1;i=10049", {})},
                ),
                "StoppedToAbortingTransition": (
                    "O",
                    "ns=1;i=10162",
                    {"TransitionNumber": ("V", "ns=1;i=10163", {})},
                ),
                "StoppedToResettingTransition": (
                    "O",
                    "ns=1;i=10082",
                    {"TransitionNumber": ("V", "ns=1;i=10083", {})},
                ),
                "Stopping": (
                    "O",
                    "ns=1;i=10074",
                    {"StateNumber": ("V", "ns=1;i=10075", {})},
                ),
                "StoppingToAbortingTransition": (
                    "O",
                    "ns=1;i=10188",
                    {"TransitionNumber": ("V", "ns=1;i=10189", {})},
                ),
                "StoppingToStoppedTransition": (
                    "O",
                    "ns=1;i=10130",
                    {"TransitionNumber": ("V", "ns=1;i=10131", {})},
                ),
                "Suspended": (
                    "O",
                    "ns=1;i=10064",
                    {"StateNumber": ("V", "ns=1;i=10065", {})},
                ),
                "SuspendedToAbortingTransition": (
                    "O",
                    "ns=1;i=10178",
                    {"TransitionNumber": ("V", "ns=1;i=10179", {})},
                ),
                "SuspendedToStoppingTransition": (
                    "O",
                    "ns=1;i=10152",
                    {"TransitionNumber": ("V", "ns=1;i=10153", {})},
                ),
                "SuspendedToUnsuspendingTransition": (
                    "O",
                    "ns=1;i=10122",
                    {"TransitionNumber": ("V", "ns=1;i=10123", {})},
                ),
                "Suspending": (
                    "O",
                    "ns=1;i=10062",
                    {"StateNumber": ("V", "ns=1;i=10063", {})},
                ),
                "SuspendingToAbortingTransition": (
                    "O",
                    "ns=1;i=10176",
                    {"TransitionNumber": ("V", "ns=1;i=10177", {})},
                ),
                "SuspendingToStoppingTransition": (
                    "O",
                    "ns=1;i=10150",
                    {"TransitionNumber": ("V", "ns=1;i=10151", {})},
                ),
                "SuspendingToSuspendedTransition": (
                    "O",
                    "ns=1;i=10120",
                    {"TransitionNumber": ("V", "ns=1;i=10121", {})},
                ),
                "SuspendingTransition": (
                    "O",
                    "ns=1;i=10118",
                    {"TransitionNumber": ("V", "ns=1;i=10119", {})},
                ),
                "Unholding": (
                    "O",
                    "ns=1;i=10072",
                    {"StateNumber": ("V", "ns=1;i=10073", {})},
                ),
                "UnholdingToAbortingTransition": (
                    "O",
                    "ns=1;i=10186",
                    {"TransitionNumber": ("V", "ns=1;i=10187", {})},
                ),
                "UnholdingToExecuteTransition": (
                    "O",
                    "ns=1;i=10114",
                    {"TransitionNumber": ("V", "ns=1;i=10115", {})},
                ),
                "UnholdingToHoldingTransition": (
                    "O",
                    "ns=1;i=10112",
                    {"TransitionNumber": ("V", "ns=1;i=10113", {})},
                ),
                "UnholdingToStoppingTransition": (
                    "O",
                    "ns=1;i=10160",
                    {"TransitionNumber": ("V", "ns=1;i=10161", {})},
                ),
                "UnholdingTransition": (
                    "O",
                    "ns=1;i=10110",
                    {"TransitionNumber": ("V", "ns=1;i=10111", {})},
                ),
                "Unsuspending": (
                    "O",
                    "ns=1;i=10066",
                    {"StateNumber": ("V", "ns=1;i=10067", {})},
                ),
                "UnsuspendingToAbortingTransition": (
                    "O",
                    "ns=1;i=10180",
                    {"TransitionNumber": ("V", "ns=1;i=10181", {})},
                ),
                "UnsuspendingToExecuteTransition": (
                    "O",
                    "ns=1;i=10128",
                    {"TransitionNumber": ("V", "ns=1;i=10129", {})},
                ),
                "UnsuspendingToStoppingTransition": (
                    "O",
                    "ns=1;i=10154",
                    {"TransitionNumber": ("V", "ns=1;i=10155", {})},
                ),
                "UnsuspendingToSuspendingTransition": (
                    "O",
                    "ns=1;i=10126",
                    {"TransitionNumber": ("V", "ns=1;i=10127", {})},
                ),
                "UnsuspendingTransition": (
                    "O",
                    "ns=1;i=10124",
                    {"TransitionNumber": ("V", "ns=1;i=10125", {})},
                ),
            },
        ),
        "AnalyserDeviceStateMachineType": (
            "OT",
            "ns=1;i=1002",
            {
                "Local": (
                    "O",
                    "ns=1;i=9651",
                    {"StateNumber": ("V", "ns=1;i=9652", {})},
                ),
                "LocalToMaintenanceTransition": (
                    "O",
                    "ns=1;i=9665",
                    {"TransitionNumber": ("V", "ns=1;i=9666", {})},
                ),
                "LocalToOperatingTransition": (
                    "O",
                    "ns=1;i=9663",
                    {"TransitionNumber": ("V", "ns=1;i=9664", {})},
                ),
                "LocalToShutdownTransition": (
                    "O",
                    "ns=1;i=9673",
                    {"TransitionNumber": ("V", "ns=1;i=9674", {})},
                ),
                "Maintenance": (
                    "O",
                    "ns=1;i=9653",
                    {"StateNumber": ("V", "ns=1;i=9654", {})},
                ),
                "MaintenanceToLocalTransition": (
                    "O",
                    "ns=1;i=9669",
                    {"TransitionNumber": ("V", "ns=1;i=9670", {})},
                ),
                "MaintenanceToOperatingTransition": (
                    "O",
                    "ns=1;i=9667",
                    {"TransitionNumber": ("V", "ns=1;i=9668", {})},
                ),
                "MaintenanceToShutdownTransition": (
                    "O",
                    "ns=1;i=9675",
                    {"TransitionNumber": ("V", "ns=1;i=9676", {})},
                ),
                "Operating": (
                    "O",
                    "ns=1;i=9649",
                    {"StateNumber": ("V", "ns=1;i=9650", {})},
                ),
                "OperatingToLocalTransition": (
                    "O",
                    "ns=1;i=9659",
                    {"TransitionNumber": ("V", "ns=1;i=9660", {})},
                ),
                "OperatingToMaintenanceTransition": (
                    "O",
                    "ns=1;i=9661",
                    {"TransitionNumber": ("V", "ns=1;i=9662", {})},
                ),
                "OperatingToShutdownTransition": (
                    "O",
                    "ns=1;i=9671",
                    {"TransitionNumber": ("V", "ns=1;i=9672", {})},
                ),
                "Powerup": (
                    "O",
                    "ns=1;i=9647",
                    {"StateNumber": ("V", "ns=1;i=9648", {})},
                ),
                "PowerupToOperatingTransition": (
                    "O",
                    "ns=1;i=9657",
                    {"TransitionNumber": ("V", "ns=1;i=9658", {})},
                ),
                "Shutdown": (
                    "O",
                    "ns=1;i=9655",
                    {"StateNumber": ("V", "ns=1;i=9656", {})},
                ),
            },
        ),
        "AnalyserDeviceType": (
            "OT",
            "ns=1;i=1001",
            {
                "<AccessorySlotIdentifier>": (
                    "O",
                    "ns=1;i=9610",
                    {
                        "AccessorySlotStateMachine": (
                            "O",
                            "ns=1;i=9614",
                            {
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=9615",
                                    {"Id": ("V", "ns=1;i=9616", {})},
                                )
                            },
                        ),
                        "IsEnabled": ("V", "ns=1;i=9613", {}),
                        "IsHotSwappable": ("V", "ns=1;i=9612", {}),
                        "SupportedTypes": ("O", "ns=1;i=9611", {}),
                    },
                ),
                "<ChannelIdentifier>": (
                    "O",
                    "ns=1;i=9500",
                    {
                        "ChannelStateMachine": (
                            "O",
                            "ns=1;i=9550",
                            {
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=9551",
                                    {"Id": ("V", "ns=1;i=9552", {})},
                                ),
                                "OperatingSubStateMachine": (
                                    "O",
                                    "ns=1;i=9562",
                                    {
                                        "CurrentState": (
                                            "V",
                                            "ns=1;i=9563",
                                            {"Id": ("V", "ns=1;i=9564", {})},
                                        ),
                                        "OperatingExecuteSubStateMachine": (
                                            "O",
                                            "ns=1;i=9574",
                                            {
                                                "CurrentState": (
                                                    "V",
                                                    "ns=1;i=9575",
                                                    {"Id": ("V", "ns=1;i=9576", {})},
                                                )
                                            },
                                        ),
                                    },
                                ),
                            },
                        ),
                        "Configuration": ("O", "ns=1;i=9546", {}),
                        "MethodSet": (
                            "O",
                            "ns=1;i=9503",
                            {
                                "Abort": ("M", "ns=1;i=9532", {}),
                                "Clear": ("M", "ns=1;i=9533", {}),
                                "GotoMaintenance": ("M", "ns=1;i=9522", {}),
                                "GotoOperating": ("M", "ns=1;i=9521", {}),
                                "Hold": ("M", "ns=1;i=9528", {}),
                                "Reset": ("M", "ns=1;i=9525", {}),
                                "Start": ("M", "ns=1;i=9526", {}),
                                "StartSingleAcquisition": (
                                    "M",
                                    "ns=1;i=9523",
                                    {"InputArguments": ("V", "ns=1;i=9524", {})},
                                ),
                                "Stop": ("M", "ns=1;i=9527", {}),
                                "Suspend": ("M", "ns=1;i=9530", {}),
                                "Unhold": ("M", "ns=1;i=9529", {}),
                                "Unsuspend": ("M", "ns=1;i=9531", {}),
                            },
                        ),
                        "Status": ("O", "ns=1;i=9548", {}),
                    },
                ),
                "AcousticSpectrometerDeviceType": ("OT", "ns=1;i=1015", {}),
                "AnalyserStateMachine": (
                    "O",
                    "ns=1;i=9488",
                    {
                        "CurrentState": (
                            "V",
                            "ns=1;i=9489",
                            {"Id": ("V", "ns=1;i=9490", {})},
                        )
                    },
                ),
                "ChromatographDeviceType": ("OT", "ns=1;i=1013", {}),
                "Configuration": (
                    "O",
                    "ns=1;i=9482",
                    {
                        "ConfigData": (
                            "O",
                            "ns=1;i=9462",
                            {
                                "Close": (
                                    "M",
                                    "ns=1;i=9470",
                                    {"InputArguments": ("V", "ns=1;i=9471", {})},
                                ),
                                "GetPosition": (
                                    "M",
                                    "ns=1;i=9477",
                                    {
                                        "InputArguments": ("V", "ns=1;i=9478", {}),
                                        "OutputArguments": ("V", "ns=1;i=9479", {}),
                                    },
                                ),
                                "Open": (
                                    "M",
                                    "ns=1;i=9467",
                                    {
                                        "InputArguments": ("V", "ns=1;i=9468", {}),
                                        "OutputArguments": ("V", "ns=1;i=9469", {}),
                                    },
                                ),
                                "OpenCount": ("V", "ns=1;i=9466", {}),
                                "Read": (
                                    "M",
                                    "ns=1;i=9472",
                                    {
                                        "InputArguments": ("V", "ns=1;i=9473", {}),
                                        "OutputArguments": ("V", "ns=1;i=9474", {}),
                                    },
                                ),
                                "SetPosition": (
                                    "M",
                                    "ns=1;i=9480",
                                    {"InputArguments": ("V", "ns=1;i=9481", {})},
                                ),
                                "Size": ("V", "ns=1;i=9463", {}),
                                "UserWritable": ("V", "ns=1;i=13071", {}),
                                "Writable": ("V", "ns=1;i=13070", {}),
                                "Write": (
                                    "M",
                                    "ns=1;i=9475",
                                    {"InputArguments": ("V", "ns=1;i=9476", {})},
                                ),
                            },
                        )
                    },
                ),
                "FactorySettings": ("O", "ns=1;i=9486", {}),
                "Identification": ("O", "ns=1;i=9386", {}),
                "MassSpectrometerDeviceType": ("OT", "ns=1;i=1014", {}),
                "MethodSet": (
                    "O",
                    "ns=1;i=9382",
                    {
                        "AbortAllChannels": ("M", "ns=1;i=9456", {}),
                        "CompareConfigDataDigest": (
                            "M",
                            "ns=1;i=9450",
                            {
                                "InputArguments": ("V", "ns=1;i=9451", {}),
                                "OutputArguments": ("V", "ns=1;i=9452", {}),
                            },
                        ),
                        "GetConfigDataDigest": (
                            "M",
                            "ns=1;i=9448",
                            {"OutputArguments": ("V", "ns=1;i=9449", {})},
                        ),
                        "GetConfiguration": (
                            "M",
                            "ns=1;i=9443",
                            {"OutputArguments": ("V", "ns=1;i=9444", {})},
                        ),
                        "GotoMaintenance": ("M", "ns=1;i=9458", {}),
                        "GotoOperating": ("M", "ns=1;i=9457", {}),
                        "ResetAllChannels": ("M", "ns=1;i=9453", {}),
                        "SetConfiguration": (
                            "M",
                            "ns=1;i=9445",
                            {
                                "InputArguments": ("V", "ns=1;i=9446", {}),
                                "OutputArguments": ("V", "ns=1;i=9447", {}),
                            },
                        ),
                        "StartAllChannels": ("M", "ns=1;i=9454", {}),
                        "StopAllChannels": ("M", "ns=1;i=9455", {}),
                    },
                ),
                "NMRDeviceType": ("OT", "ns=1;i=1016", {}),
                "ParameterSet": ("O", "ns=1;i=5001", {}),
                "ParticleSizeMonitorDeviceType": ("OT", "ns=1;i=1012", {}),
                "SpectrometerDeviceType": (
                    "OT",
                    "ns=1;i=1011",
                    {
                        "FactorySettings": ("O", "ns=1;i=11411", {}),
                        "ParameterSet": (
                            "O",
                            "ns=1;i=11305",
                            {"SpectralRange": ("V", "ns=1;i=11551", {})},
                        ),
                    },
                ),
                "Status": (
                    "O",
                    "ns=1;i=9484",
                    {"DiagnosticStatus": ("V", "ns=1;i=9459", {})},
                ),
            },
        ),
        "StreamType": (
            "OT",
            "ns=1;i=1010",
            {
                "<GroupIdentifier>": ("O", "ns=1;i=10444", {}),
                "AcousticSpectrometerDeviceStreamType": ("OT", "ns=1;i=1033", {}),
                "AcquisitionData": (
                    "O",
                    "ns=1;i=10438",
                    {
                        "AcquisitionCounter": (
                            "V",
                            "ns=1;i=10376",
                            {"EURange": ("V", "ns=1;i=10380", {})},
                        ),
                        "AcquisitionEndTime": ("V", "ns=1;i=10394", {}),
                        "AcquisitionResultStatus": ("V", "ns=1;i=10382", {}),
                        "Offset": ("V", "ns=1;i=10391", {}),
                        "RawData": ("V", "ns=1;i=10385", {}),
                        "ScaledData": ("V", "ns=1;i=10388", {}),
                    },
                ),
                "AcquisitionSettings": (
                    "O",
                    "ns=1;i=10434",
                    {
                        "TimeBetweenSamples": (
                            "V",
                            "ns=1;i=10357",
                            {"EURange": ("V", "ns=1;i=10361", {})},
                        )
                    },
                ),
                "AcquisitionStatus": (
                    "O",
                    "ns=1;i=10436",
                    {
                        "ExecutionCycle": ("V", "ns=1;i=10366", {}),
                        "ExecutionCycleSubcode": (
                            "V",
                            "ns=1;i=10369",
                            {"EnumStrings": ("V", "ns=1;i=10372", {})},
                        ),
                        "IsActive": ("V", "ns=1;i=10363", {}),
                        "Progress": ("V", "ns=1;i=10373", {}),
                    },
                ),
                "ChemometricModelSettings": ("O", "ns=1;i=10440", {}),
                "ChromatographDeviceStreamType": ("OT", "ns=1;i=1034", {}),
                "Configuration": (
                    "O",
                    "ns=1;i=10430",
                    {
                        "IsEnabled": ("V", "ns=1;i=10339", {}),
                        "IsForced": ("V", "ns=1;i=10342", {}),
                    },
                ),
                "Context": (
                    "O",
                    "ns=1;i=10442",
                    {
                        "BatchId": ("V", "ns=1;i=10400", {}),
                        "CampaignId": ("V", "ns=1;i=10397", {}),
                        "LotId": ("V", "ns=1;i=10406", {}),
                        "MaterialId": ("V", "ns=1;i=10409", {}),
                        "Operation": ("V", "ns=1;i=10418", {}),
                        "Phase": ("V", "ns=1;i=10421", {}),
                        "Process": ("V", "ns=1;i=10412", {}),
                        "SampleId": ("V", "ns=1;i=10427", {}),
                        "SubBatchId": ("V", "ns=1;i=10403", {}),
                        "Unit": ("V", "ns=1;i=10415", {}),
                        "UserId": ("V", "ns=1;i=10424", {}),
                    },
                ),
                "MNRDeviceStreamType": ("OT", "ns=1;i=1035", {}),
                "MassSpectrometerDeviceStreamType": ("OT", "ns=1;i=1031", {}),
                "ParameterSet": ("O", "ns=1;i=10317", {}),
                "ParticleSizeMonitorDeviceStreamType": (
                    "OT",
                    "ns=1;i=1032",
                    {
                        "AcquisitionData": (
                            "O",
                            "ns=1;i=10889",
                            {
                                "Background": (
                                    "V",
                                    "ns=1;i=10897",
                                    {
                                        "AxisScaleType": ("V", "ns=1;i=10904", {}),
                                        "EURange": ("V", "ns=1;i=10901", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10902", {}),
                                        "Title": ("V", "ns=1;i=10903", {}),
                                        "XAxisDefinition": ("V", "ns=1;i=10905", {}),
                                    },
                                ),
                                "BackgroundAcquisitionTime": ("V", "ns=1;i=10915", {}),
                                "SizeDistribution": (
                                    "V",
                                    "ns=1;i=10906",
                                    {
                                        "AxisScaleType": ("V", "ns=1;i=10913", {}),
                                        "EURange": ("V", "ns=1;i=10910", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10911", {}),
                                        "Title": ("V", "ns=1;i=10912", {}),
                                        "XAxisDefinition": ("V", "ns=1;i=10914", {}),
                                    },
                                ),
                            },
                        ),
                        "ParameterSet": ("O", "ns=1;i=10768", {}),
                    },
                ),
                "SpectrometerDeviceStreamType": (
                    "OT",
                    "ns=1;i=1030",
                    {
                        "AcquisitionData": (
                            "O",
                            "ns=1;i=10567",
                            {
                                "BackgroundAcquisitionTime": ("V", "ns=1;i=10617", {}),
                                "PendingBackground": (
                                    "V",
                                    "ns=1;i=10620",
                                    {
                                        "AxisScaleType": ("V", "ns=1;i=10627", {}),
                                        "EURange": ("V", "ns=1;i=10624", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10625", {}),
                                        "Title": ("V", "ns=1;i=10626", {}),
                                        "XAxisDefinition": ("V", "ns=1;i=10628", {}),
                                    },
                                ),
                                "PendingBackground1": (
                                    "V",
                                    "ns=1;i=10629",
                                    {
                                        "AxisScaleType": ("V", "ns=1;i=10636", {}),
                                        "EURange": ("V", "ns=1;i=10633", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10634", {}),
                                        "Title": ("V", "ns=1;i=10635", {}),
                                        "XAxisDefinition": ("V", "ns=1;i=10637", {}),
                                    },
                                ),
                                "TotalNumberOfScansDone": ("V", "ns=1;i=10614", {}),
                            },
                        ),
                        "AcquisitionSettings": (
                            "O",
                            "ns=1;i=10563",
                            {
                                "AbsorbanceCutoff": ("V", "ns=1;i=10608", {}),
                                "Gain": ("V", "ns=1;i=10602", {}),
                                "RequestedNumberOfScans": ("V", "ns=1;i=10599", {}),
                                "Resolution": ("V", "ns=1;i=10596", {}),
                                "SpectralRange": ("V", "ns=1;i=10593", {}),
                                "TransmittanceCutoff": ("V", "ns=1;i=10605", {}),
                            },
                        ),
                        "AcquisitionStatus": (
                            "O",
                            "ns=1;i=10565",
                            {"NumberOfScansDone": ("V", "ns=1;i=10611", {})},
                        ),
                        "Configuration": (
                            "O",
                            "ns=1;i=10559",
                            {
                                "ActiveBackground": (
                                    "V",
                                    "ns=1;i=10575",
                                    {
                                        "AxisScaleType": ("V", "ns=1;i=10582", {}),
                                        "EURange": ("V", "ns=1;i=10579", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10580", {}),
                                        "Title": ("V", "ns=1;i=10581", {}),
                                        "XAxisDefinition": ("V", "ns=1;i=10583", {}),
                                    },
                                ),
                                "ActiveBackground1": (
                                    "V",
                                    "ns=1;i=10584",
                                    {
                                        "AxisScaleType": ("V", "ns=1;i=10591", {}),
                                        "EURange": ("V", "ns=1;i=10588", {}),
                                        "EngineeringUnits": ("V", "ns=1;i=10589", {}),
                                        "Title": ("V", "ns=1;i=10590", {}),
                                        "XAxisDefinition": ("V", "ns=1;i=10592", {}),
                                    },
                                ),
                            },
                        ),
                        "FactorySettings": ("O", "ns=1;i=10638", {}),
                        "ParameterSet": ("O", "ns=1;i=10446", {}),
                    },
                ),
                "Status": (
                    "O",
                    "ns=1;i=10432",
                    {
                        "DiagnosticStatus": ("V", "ns=1;i=10345", {}),
                        "LastCalibrationTime": ("V", "ns=1;i=10348", {}),
                        "LastSampleTime": ("V", "ns=1;i=10354", {}),
                        "LastValidationTime": ("V", "ns=1;i=10351", {}),
                    },
                ),
            },
        ),
    },
    "reftypes": {
        "HasDataSource": ("RT", "ns=1;i=4001", {}),
        "HasInput": ("RT", "ns=1;i=4002", {}),
        "HasOutput": ("RT", "ns=1;i=4003", {}),
    },
    "vartypes": {
        "ChemometricModelType": (
            "VT",
            "ns=1;i=2007",
            {
                "CreationDate": ("V", "ns=1;i=13034", {}),
                "MVAModelType": (
                    "VT",
                    "ns=1;i=2009",
                    {"MainDataIndex": ("V", "ns=1;i=13046", {})},
                ),
                "ModelDescription": ("V", "ns=1;i=13035", {}),
                "Name": ("V", "ns=1;i=13033", {}),
            },
        ),
        "EngineeringValueType": (
            "VT",
            "ns=1;i=9380",
            {"<Identifier>": ("V", "ns=1;i=13030", {})},
        ),
        "MVAOutputParameterType": (
            "VT",
            "ns=1;i=2010",
            {
                "AlarmLimits": ("V", "ns=1;i=13055", {}),
                "AlarmState": ("V", "ns=1;i=13056", {}),
                "Statistics": (
                    "V",
                    "ns=1;i=13058",
                    {
                        "AlarmLimits": ("V", "ns=1;i=13060", {}),
                        "AlarmState": ("V", "ns=1;i=13061", {}),
                        "VendorSpecificError": ("V", "ns=1;i=13062", {}),
                        "WarningLimits": ("V", "ns=1;i=13059", {}),
                    },
                ),
                "VendorSpecificError": ("V", "ns=1;i=13057", {}),
                "WarningLimits": ("V", "ns=1;i=13054", {}),
            },
        ),
        "ProcessVariableType": ("VT", "ns=1;i=2008", {}),
    },
}
