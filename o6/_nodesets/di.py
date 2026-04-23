# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 40a02d98a8b2a014ec9f961625a422df3566d4dd783151ec6ae55b47296199de
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/DI/"
_VERSION: str = "1.05.0"
_REQUIRED: list = [{"uri": "http://opcfoundation.org/UA/", "version": "1.05.04"}]
_STRUCTURES: list = [
    (
        "ns=1;i=6522",
        "FetchResultDataType",
        "ns=1;i=6551",
        {"structure_type": 0, "fields": []},
    ),
    (
        "ns=1;i=15888",
        "TransferResultErrorDataType",
        "ns=1;i=15891",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Status", "data_type": "i=6", "value_rank": -1},
                {"name": "Diagnostics", "data_type": "i=25", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=15889",
        "TransferResultDataDataType",
        "ns=1;i=15892",
        {
            "structure_type": 0,
            "fields": [
                {"name": "SequenceNumber", "data_type": "i=6", "value_rank": -1},
                {"name": "EndOfResults", "data_type": "i=1", "value_rank": -1},
                {"name": "ParameterDefs", "data_type": "ns=1;i=6525", "value_rank": 1},
            ],
        },
    ),
    (
        "ns=1;i=6525",
        "ParameterResultDataType",
        "ns=1;i=6554",
        {
            "structure_type": 0,
            "fields": [
                {"name": "NodePath", "data_type": "i=20", "value_rank": 1},
                {"name": "StatusCode", "data_type": "i=19", "value_rank": -1},
                {"name": "Diagnostics", "data_type": "i=25", "value_rank": -1},
            ],
        },
    ),
]
_ENUMS: list = [
    (
        "ns=1;i=6244",
        "DeviceHealthEnumeration",
        {
            "fields": [
                {"name": "NORMAL", "value": 0, "display_name": "NORMAL"},
                {"name": "FAILURE", "value": 1, "display_name": "FAILURE"},
                {
                    "name": "CHECK_FUNCTION",
                    "value": 2,
                    "display_name": "CHECK_FUNCTION",
                },
                {"name": "OFF_SPEC", "value": 3, "display_name": "OFF_SPEC"},
                {
                    "name": "MAINTENANCE_REQUIRED",
                    "value": 4,
                    "display_name": "MAINTENANCE_REQUIRED",
                },
            ]
        },
    ),
    (
        "ns=1;i=408",
        "SoftwareClass",
        {
            "fields": [
                {"name": "Firmware", "value": 0, "display_name": "Firmware"},
                {"name": "Application", "value": 1, "display_name": "Application"},
                {"name": "Configuration", "value": 2, "display_name": "Configuration"},
                {"name": "Solution", "value": 3, "display_name": "Solution"},
            ]
        },
    ),
    (
        "ns=1;i=410",
        "LocationIndicationType",
        {
            "fields": [
                {"name": "Visual", "value": 0, "display_name": "Visual"},
                {"name": "Audible", "value": 1, "display_name": "Audible"},
            ]
        },
    ),
    (
        "ns=1;i=331",
        "SoftwareVersionFileType",
        {
            "fields": [
                {"name": "Current", "value": 0, "display_name": "Current"},
                {"name": "Pending", "value": 1, "display_name": "Pending"},
                {"name": "Fallback", "value": 2, "display_name": "Fallback"},
            ]
        },
    ),
    (
        "ns=1;i=333",
        "UpdateBehavior",
        {
            "fields": [
                {
                    "name": "KeepsParameters",
                    "value": 0,
                    "display_name": "KeepsParameters",
                },
                {
                    "name": "WillDisconnect",
                    "value": 1,
                    "display_name": "WillDisconnect",
                },
                {
                    "name": "RequiresPowerCycle",
                    "value": 2,
                    "display_name": "RequiresPowerCycle",
                },
                {"name": "WillReboot", "value": 3, "display_name": "WillReboot"},
                {
                    "name": "NeedsPreparation",
                    "value": 4,
                    "display_name": "NeedsPreparation",
                },
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = (
    [
        ("ns=1;i=6522", "ns=1;i=6551", []),
        ("ns=1;i=15888", "ns=1;i=15891", ["i=6", "i=25"]),
        ("ns=1;i=15889", "ns=1;i=15892", ["i=6", "i=1", "ns=1;i=6525"]),
        ("ns=1;i=6525", "ns=1;i=6554", ["i=20", "i=19", "i=25"]),
    ],
    ["ns=1;i=6244", "ns=1;i=408", "ns=1;i=410", "ns=1;i=331", "ns=1;i=333"],
)
_NODES: dict = {
    "datatypes": {
        "DeviceHealthEnumeration": (
            "D",
            "ns=1;i=6244",
            {"EnumStrings": ("V", "ns=1;i=6450", {})},
        ),
        "FetchResultDataType": (
            "D",
            "ns=1;i=6522",
            {
                "TransferResultDataDataType": ("D", "ns=1;i=15889", {}),
                "TransferResultErrorDataType": ("D", "ns=1;i=15888", {}),
            },
        ),
        "LocationIndicationType": (
            "D",
            "ns=1;i=410",
            {"OptionSetValues": ("V", "ns=1;i=411", {})},
        ),
        "ParameterResultDataType": ("D", "ns=1;i=6525", {}),
        "SoftwareClass": ("D", "ns=1;i=408", {"EnumStrings": ("V", "ns=1;i=409", {})}),
        "SoftwareVersionFileType": (
            "D",
            "ns=1;i=331",
            {"EnumStrings": ("V", "ns=1;i=332", {})},
        ),
        "UpdateBehavior": (
            "D",
            "ns=1;i=333",
            {"OptionSetValues": ("V", "ns=1;i=388", {})},
        ),
    },
    "ifacetypes": {
        "IAssetLocationIndicationType": (
            "OT",
            "ns=1;i=118",
            {
                "IsIndicating": ("V", "ns=1;i=154", {}),
                "StartLocationIndication": (
                    "M",
                    "ns=1;i=119",
                    {"InputArguments": ("V", "ns=1;i=413", {})},
                ),
                "StopLocationIndication": ("M", "ns=1;i=121", {}),
                "SupportedIndicationTypes": ("V", "ns=1;i=156", {}),
                "UsedIndicationType": ("V", "ns=1;i=155", {}),
            },
        ),
        "IDeviceHealthType": (
            "OT",
            "ns=1;i=15051",
            {
                "DeviceHealth": ("V", "ns=1;i=15052", {}),
                "DeviceHealthAlarms": ("O", "ns=1;i=15053", {}),
            },
        ),
        "IOperationCounterType": (
            "OT",
            "ns=1;i=480",
            {
                "OperationCycleCounter": ("V", "ns=1;i=483", {}),
                "OperationDuration": ("V", "ns=1;i=482", {}),
                "PowerOnDuration": ("V", "ns=1;i=481", {}),
            },
        ),
        "ISupportInfoType": (
            "OT",
            "ns=1;i=15054",
            {
                "DeviceTypeImage": (
                    "O",
                    "ns=1;i=15055",
                    {"<ImageIdentifier>": ("V", "ns=1;i=15056", {})},
                ),
                "Documentation": (
                    "O",
                    "ns=1;i=15057",
                    {"<DocumentIdentifier>": ("V", "ns=1;i=15058", {})},
                ),
                "DocumentationFiles": (
                    "O",
                    "ns=1;i=27",
                    {
                        "<DocumentFileId>": (
                            "O",
                            "ns=1;i=28",
                            {
                                "Close": (
                                    "M",
                                    "ns=1;i=39",
                                    {"InputArguments": ("V", "ns=1;i=62", {})},
                                ),
                                "GetPosition": (
                                    "M",
                                    "ns=1;i=68",
                                    {
                                        "InputArguments": ("V", "ns=1;i=69", {}),
                                        "OutputArguments": ("V", "ns=1;i=70", {}),
                                    },
                                ),
                                "Open": (
                                    "M",
                                    "ns=1;i=36",
                                    {
                                        "InputArguments": ("V", "ns=1;i=37", {}),
                                        "OutputArguments": ("V", "ns=1;i=38", {}),
                                    },
                                ),
                                "OpenCount": ("V", "ns=1;i=32", {}),
                                "Read": (
                                    "M",
                                    "ns=1;i=63",
                                    {
                                        "InputArguments": ("V", "ns=1;i=64", {}),
                                        "OutputArguments": ("V", "ns=1;i=65", {}),
                                    },
                                ),
                                "SetPosition": (
                                    "M",
                                    "ns=1;i=71",
                                    {"InputArguments": ("V", "ns=1;i=72", {})},
                                ),
                                "Size": ("V", "ns=1;i=29", {}),
                                "UserWritable": ("V", "ns=1;i=31", {}),
                                "Writable": ("V", "ns=1;i=30", {}),
                                "Write": (
                                    "M",
                                    "ns=1;i=66",
                                    {"InputArguments": ("V", "ns=1;i=67", {})},
                                ),
                            },
                        )
                    },
                ),
                "ImageSet": (
                    "O",
                    "ns=1;i=15061",
                    {"<ImageIdentifier>": ("V", "ns=1;i=15062", {})},
                ),
                "ProtocolSupport": (
                    "O",
                    "ns=1;i=15059",
                    {"<ProtocolSupportIdentifier>": ("V", "ns=1;i=15060", {})},
                ),
            },
        ),
        "ITagNameplateType": (
            "OT",
            "ns=1;i=15048",
            {
                "AssetId": ("V", "ns=1;i=15049", {}),
                "ComponentName": ("V", "ns=1;i=15050", {}),
            },
        ),
        "IVendorNameplateType": (
            "OT",
            "ns=1;i=15035",
            {
                "DeviceClass": ("V", "ns=1;i=15044", {}),
                "DeviceManual": ("V", "ns=1;i=15043", {}),
                "DeviceRevision": ("V", "ns=1;i=15041", {}),
                "HardwareRevision": ("V", "ns=1;i=15039", {}),
                "Manufacturer": ("V", "ns=1;i=15036", {}),
                "ManufacturerUri": ("V", "ns=1;i=15037", {}),
                "Model": ("V", "ns=1;i=15038", {}),
                "PatchIdentifiers": ("V", "ns=1;i=24", {}),
                "ProductCode": ("V", "ns=1;i=15042", {}),
                "ProductInstanceUri": ("V", "ns=1;i=15046", {}),
                "RevisionCounter": ("V", "ns=1;i=15047", {}),
                "SerialNumber": ("V", "ns=1;i=15045", {}),
                "SoftwareReleaseDate": ("V", "ns=1;i=23", {}),
                "SoftwareRevision": ("V", "ns=1;i=15040", {}),
            },
        ),
    },
    "objects": {
        "<CPIdentifier>": (
            "O",
            "ns=1;i=6248",
            {"NetworkAddress": ("O", "ns=1;i=6292", {})},
        ),
        "<NetworkIdentifier>": ("O", "ns=1;i=6599", {}),
        "Configuration": ("O", "ns=1;i=73", {}),
        "Default Binary": ("O", "ns=1;i=6554", {}),
        "Default JSON": ("O", "ns=1;i=15912", {}),
        "Default XML": ("O", "ns=1;i=6538", {}),
        "DeviceSet": (
            "O",
            "ns=1;i=5001",
            {"DeviceFeatures": ("O", "ns=1;i=15034", {})},
        ),
        "DeviceTopology": (
            "O",
            "ns=1;i=6094",
            {"OnlineAccess": ("V", "ns=1;i=6095", {})},
        ),
        "Diagnostics": ("O", "ns=1;i=90", {}),
        "Identification": ("O", "ns=1;i=95", {}),
        "Maintenance": ("O", "ns=1;i=75", {}),
        "MaxInactiveLockTime": ("V", "ns=1;i=6387", {}),
        "NetworkSet": ("O", "ns=1;i=6078", {}),
        "Opc.Ua.Di": (
            "V",
            "ns=1;i=6423",
            {
                "Deprecated": ("V", "ns=1;i=15902", {}),
                "FetchResultDataType": ("V", "ns=1;i=6539", {}),
                "NamespaceUri": ("V", "ns=1;i=6425", {}),
                "ParameterResultDataType": ("V", "ns=1;i=6548", {}),
                "TransferResultDataDataType": ("V", "ns=1;i=15906", {}),
                "TransferResultErrorDataType": ("V", "ns=1;i=15903", {}),
            },
        ),
        "OperationCounters": ("O", "ns=1;i=94", {}),
        "Operational": ("O", "ns=1;i=93", {}),
        "Statistics": ("O", "ns=1;i=91", {}),
        "Status": ("O", "ns=1;i=92", {}),
        "Tuning": ("O", "ns=1;i=74", {}),
        "http://opcfoundation.org/UA/DI/": (
            "O",
            "ns=1;i=15001",
            {
                "DefaultAccessRestrictions": ("V", "ns=1;i=15033", {}),
                "DefaultRolePermissions": ("V", "ns=1;i=15031", {}),
                "DefaultUserRolePermissions": ("V", "ns=1;i=15032", {}),
                "IsNamespaceSubset": ("V", "ns=1;i=15005", {}),
                "ModelVersion": ("V", "ns=1;i=489", {}),
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
        "BaseLifetimeIndicationType": (
            "OT",
            "ns=1;i=473",
            {
                "DiameterIndicationType": ("OT", "ns=1;i=478", {}),
                "LengthIndicationType": ("OT", "ns=1;i=477", {}),
                "NumberOfPartsIndicationType": ("OT", "ns=1;i=475", {}),
                "NumberOfUsagesIndicationType": ("OT", "ns=1;i=476", {}),
                "SubstanceVolumeIndicationType": ("OT", "ns=1;i=479", {}),
                "TimeIndicationType": ("OT", "ns=1;i=474", {}),
            },
        ),
        "ConfigurableObjectType": (
            "OT",
            "ns=1;i=1004",
            {
                "<ObjectIdentifier>": ("O", "ns=1;i=6026", {}),
                "SupportedTypes": ("O", "ns=1;i=5004", {}),
            },
        ),
        "ConfirmationStateMachineType": (
            "OT",
            "ns=1;i=307",
            {
                "Confirm": ("M", "ns=1;i=321", {}),
                "ConfirmationTimeout": ("V", "ns=1;i=322", {}),
                "NotWaitingForConfirm": (
                    "O",
                    "ns=1;i=323",
                    {"StateNumber": ("V", "ns=1;i=324", {})},
                ),
                "NotWaitingForConfirmToWaitingForConfirm": (
                    "O",
                    "ns=1;i=327",
                    {"TransitionNumber": ("V", "ns=1;i=328", {})},
                ),
                "WaitingForConfirm": (
                    "O",
                    "ns=1;i=325",
                    {"StateNumber": ("V", "ns=1;i=326", {})},
                ),
                "WaitingForConfirmToNotWaitingForConfirm": (
                    "O",
                    "ns=1;i=329",
                    {"TransitionNumber": ("V", "ns=1;i=330", {})},
                ),
            },
        ),
        "DeviceHealthDiagnosticAlarmType": (
            "OT",
            "ns=1;i=15143",
            {
                "CheckFunctionAlarmType": ("OT", "ns=1;i=15441", {}),
                "FailureAlarmType": ("OT", "ns=1;i=15292", {}),
                "MaintenanceRequiredAlarmType": ("OT", "ns=1;i=15739", {}),
                "OffSpecAlarmType": ("OT", "ns=1;i=15590", {}),
            },
        ),
        "FunctionalGroupType": (
            "OT",
            "ns=1;i=1005",
            {
                "<GroupIdentifier>": (
                    "O",
                    "ns=1;i=6027",
                    {"UIElement": ("V", "ns=1;i=6242", {})},
                ),
                "UIElement": ("V", "ns=1;i=6243", {}),
            },
        ),
        "InstallationStateMachineType": (
            "OT",
            "ns=1;i=249",
            {
                "Error": ("O", "ns=1;i=275", {"StateNumber": ("V", "ns=1;i=276", {})}),
                "ErrorToIdle": (
                    "O",
                    "ns=1;i=283",
                    {"TransitionNumber": ("V", "ns=1;i=284", {})},
                ),
                "Idle": ("O", "ns=1;i=271", {"StateNumber": ("V", "ns=1;i=272", {})}),
                "IdleToInstalling": (
                    "O",
                    "ns=1;i=277",
                    {"TransitionNumber": ("V", "ns=1;i=387", {})},
                ),
                "InstallFiles": (
                    "M",
                    "ns=1;i=268",
                    {"InputArguments": ("V", "ns=1;i=269", {})},
                ),
                "InstallSoftwarePackage": (
                    "M",
                    "ns=1;i=265",
                    {"InputArguments": ("V", "ns=1;i=266", {})},
                ),
                "InstallationDelay": ("V", "ns=1;i=264", {}),
                "Installing": (
                    "O",
                    "ns=1;i=273",
                    {"StateNumber": ("V", "ns=1;i=274", {})},
                ),
                "InstallingToError": (
                    "O",
                    "ns=1;i=281",
                    {"TransitionNumber": ("V", "ns=1;i=282", {})},
                ),
                "InstallingToIdle": (
                    "O",
                    "ns=1;i=279",
                    {"TransitionNumber": ("V", "ns=1;i=280", {})},
                ),
                "PercentComplete": ("V", "ns=1;i=263", {}),
                "Resume": ("M", "ns=1;i=270", {}),
                "Uninstall": ("M", "ns=1;i=407", {}),
            },
        ),
        "LockingServicesType": (
            "OT",
            "ns=1;i=6388",
            {
                "BreakLock": (
                    "M",
                    "ns=1;i=6400",
                    {"OutputArguments": ("V", "ns=1;i=6401", {})},
                ),
                "DefaultInstanceBrowseName": ("V", "ns=1;i=15890", {}),
                "ExitLock": (
                    "M",
                    "ns=1;i=6398",
                    {"OutputArguments": ("V", "ns=1;i=6399", {})},
                ),
                "InitLock": (
                    "M",
                    "ns=1;i=6393",
                    {
                        "InputArguments": ("V", "ns=1;i=6394", {}),
                        "OutputArguments": ("V", "ns=1;i=6395", {}),
                    },
                ),
                "Locked": ("V", "ns=1;i=6534", {}),
                "LockingClient": ("V", "ns=1;i=6390", {}),
                "LockingUser": ("V", "ns=1;i=6391", {}),
                "RemainingLockTime": ("V", "ns=1;i=6392", {}),
                "RenewLock": (
                    "M",
                    "ns=1;i=6396",
                    {"OutputArguments": ("V", "ns=1;i=6397", {})},
                ),
            },
        ),
        "NetworkType": (
            "OT",
            "ns=1;i=6247",
            {
                "<ProfileIdentifier>": ("O", "ns=1;i=6596", {}),
                "Lock": (
                    "O",
                    "ns=1;i=6294",
                    {
                        "BreakLock": (
                            "M",
                            "ns=1;i=6306",
                            {"OutputArguments": ("V", "ns=1;i=6307", {})},
                        ),
                        "ExitLock": (
                            "M",
                            "ns=1;i=6304",
                            {"OutputArguments": ("V", "ns=1;i=6305", {})},
                        ),
                        "InitLock": (
                            "M",
                            "ns=1;i=6299",
                            {
                                "InputArguments": ("V", "ns=1;i=6300", {}),
                                "OutputArguments": ("V", "ns=1;i=6301", {}),
                            },
                        ),
                        "Locked": ("V", "ns=1;i=6497", {}),
                        "LockingClient": ("V", "ns=1;i=6296", {}),
                        "LockingUser": ("V", "ns=1;i=6297", {}),
                        "RemainingLockTime": ("V", "ns=1;i=6298", {}),
                        "RenewLock": (
                            "M",
                            "ns=1;i=6302",
                            {"OutputArguments": ("V", "ns=1;i=6303", {})},
                        ),
                    },
                ),
            },
        ),
        "PowerCycleStateMachineType": (
            "OT",
            "ns=1;i=285",
            {
                "NotWaitingForPowerCycle": (
                    "O",
                    "ns=1;i=299",
                    {"StateNumber": ("V", "ns=1;i=300", {})},
                ),
                "NotWaitingForPowerCycleToWaitingForPowerCycle": (
                    "O",
                    "ns=1;i=303",
                    {"TransitionNumber": ("V", "ns=1;i=304", {})},
                ),
                "WaitingForPowerCycle": (
                    "O",
                    "ns=1;i=301",
                    {"StateNumber": ("V", "ns=1;i=302", {})},
                ),
                "WaitingForPowerCycleToNotWaitingForPowerCycle": (
                    "O",
                    "ns=1;i=305",
                    {"TransitionNumber": ("V", "ns=1;i=306", {})},
                ),
            },
        ),
        "PrepareForUpdateStateMachineType": (
            "OT",
            "ns=1;i=213",
            {
                "Abort": ("M", "ns=1;i=229", {}),
                "Idle": ("O", "ns=1;i=231", {"StateNumber": ("V", "ns=1;i=232", {})}),
                "IdleToPreparing": (
                    "O",
                    "ns=1;i=239",
                    {"TransitionNumber": ("V", "ns=1;i=240", {})},
                ),
                "PercentComplete": ("V", "ns=1;i=227", {}),
                "Prepare": ("M", "ns=1;i=228", {}),
                "PreparedForUpdate": (
                    "O",
                    "ns=1;i=235",
                    {"StateNumber": ("V", "ns=1;i=236", {})},
                ),
                "PreparedForUpdateToResuming": (
                    "O",
                    "ns=1;i=245",
                    {"TransitionNumber": ("V", "ns=1;i=246", {})},
                ),
                "Preparing": (
                    "O",
                    "ns=1;i=233",
                    {"StateNumber": ("V", "ns=1;i=234", {})},
                ),
                "PreparingToIdle": (
                    "O",
                    "ns=1;i=241",
                    {"TransitionNumber": ("V", "ns=1;i=242", {})},
                ),
                "PreparingToPreparedForUpdate": (
                    "O",
                    "ns=1;i=243",
                    {"TransitionNumber": ("V", "ns=1;i=244", {})},
                ),
                "Resume": ("M", "ns=1;i=230", {}),
                "Resuming": (
                    "O",
                    "ns=1;i=237",
                    {"StateNumber": ("V", "ns=1;i=238", {})},
                ),
                "ResumingToIdle": (
                    "O",
                    "ns=1;i=247",
                    {"TransitionNumber": ("V", "ns=1;i=248", {})},
                ),
            },
        ),
        "ProtocolType": ("OT", "ns=1;i=1006", {}),
        "SoftwareFolderType": (
            "OT",
            "ns=1;i=364",
            {
                "Add": ("M", "ns=1;i=403", {"InputArguments": ("V", "ns=1;i=404", {})}),
                "Delete": (
                    "M",
                    "ns=1;i=405",
                    {"InputArguments": ("V", "ns=1;i=406", {})},
                ),
                "SoftwareClass": ("V", "ns=1;i=365", {}),
            },
        ),
        "SoftwareLoadingType": (
            "OT",
            "ns=1;i=135",
            {
                "FileSystemLoadingType": (
                    "OT",
                    "ns=1;i=192",
                    {
                        "FileSystem": (
                            "O",
                            "ns=1;i=194",
                            {
                                "CreateDirectory": (
                                    "M",
                                    "ns=1;i=195",
                                    {
                                        "InputArguments": ("V", "ns=1;i=196", {}),
                                        "OutputArguments": ("V", "ns=1;i=197", {}),
                                    },
                                ),
                                "CreateFile": (
                                    "M",
                                    "ns=1;i=198",
                                    {
                                        "InputArguments": ("V", "ns=1;i=199", {}),
                                        "OutputArguments": ("V", "ns=1;i=200", {}),
                                    },
                                ),
                                "Delete": (
                                    "M",
                                    "ns=1;i=201",
                                    {"InputArguments": ("V", "ns=1;i=202", {})},
                                ),
                                "MoveOrCopy": (
                                    "M",
                                    "ns=1;i=203",
                                    {
                                        "InputArguments": ("V", "ns=1;i=204", {}),
                                        "OutputArguments": ("V", "ns=1;i=205", {}),
                                    },
                                ),
                            },
                        ),
                        "GetUpdateBehavior": (
                            "M",
                            "ns=1;i=206",
                            {
                                "InputArguments": ("V", "ns=1;i=207", {}),
                                "OutputArguments": ("V", "ns=1;i=208", {}),
                            },
                        ),
                        "ValidateFiles": (
                            "M",
                            "ns=1;i=209",
                            {
                                "InputArguments": ("V", "ns=1;i=210", {}),
                                "OutputArguments": ("V", "ns=1;i=211", {}),
                            },
                        ),
                    },
                ),
                "PackageLoadingType": (
                    "OT",
                    "ns=1;i=137",
                    {
                        "CachedLoadingType": (
                            "OT",
                            "ns=1;i=171",
                            {
                                "FallbackVersion": (
                                    "O",
                                    "ns=1;i=188",
                                    {
                                        "Manufacturer": ("V", "ns=1;i=373", {}),
                                        "ManufacturerUri": ("V", "ns=1;i=374", {}),
                                        "SoftwareRevision": ("V", "ns=1;i=375", {}),
                                    },
                                ),
                                "GetUpdateBehavior": (
                                    "M",
                                    "ns=1;i=189",
                                    {
                                        "InputArguments": ("V", "ns=1;i=190", {}),
                                        "OutputArguments": ("V", "ns=1;i=191", {}),
                                    },
                                ),
                                "PendingVersion": (
                                    "O",
                                    "ns=1;i=187",
                                    {
                                        "Manufacturer": ("V", "ns=1;i=366", {}),
                                        "ManufacturerUri": ("V", "ns=1;i=367", {}),
                                        "SoftwareRevision": ("V", "ns=1;i=368", {}),
                                    },
                                ),
                            },
                        ),
                        "CurrentVersion": (
                            "O",
                            "ns=1;i=139",
                            {
                                "Manufacturer": ("V", "ns=1;i=345", {}),
                                "ManufacturerUri": ("V", "ns=1;i=346", {}),
                                "SoftwareRevision": ("V", "ns=1;i=347", {}),
                            },
                        ),
                        "DirectLoadingType": (
                            "OT",
                            "ns=1;i=153",
                            {
                                "UpdateBehavior": ("V", "ns=1;i=169", {}),
                                "WriteTimeout": ("V", "ns=1;i=170", {}),
                            },
                        ),
                        "ErrorMessage": ("V", "ns=1;i=151", {}),
                        "FileTransfer": (
                            "O",
                            "ns=1;i=140",
                            {
                                "ClientProcessingTimeout": ("V", "ns=1;i=141", {}),
                                "CloseAndCommit": (
                                    "M",
                                    "ns=1;i=148",
                                    {
                                        "InputArguments": ("V", "ns=1;i=149", {}),
                                        "OutputArguments": ("V", "ns=1;i=150", {}),
                                    },
                                ),
                                "GenerateFileForRead": (
                                    "M",
                                    "ns=1;i=142",
                                    {
                                        "InputArguments": ("V", "ns=1;i=143", {}),
                                        "OutputArguments": ("V", "ns=1;i=144", {}),
                                    },
                                ),
                                "GenerateFileForWrite": (
                                    "M",
                                    "ns=1;i=145",
                                    {
                                        "InputArguments": ("V", "ns=1;i=146", {}),
                                        "OutputArguments": ("V", "ns=1;i=147", {}),
                                    },
                                ),
                            },
                        ),
                        "WriteBlockSize": ("V", "ns=1;i=152", {}),
                    },
                ),
                "UpdateKey": ("V", "ns=1;i=136", {}),
            },
        ),
        "SoftwareUpdateType": (
            "OT",
            "ns=1;i=1",
            {
                "Confirmation": (
                    "O",
                    "ns=1;i=98",
                    {
                        "Confirm": ("M", "ns=1;i=112", {}),
                        "ConfirmationTimeout": ("V", "ns=1;i=113", {}),
                        "CurrentState": (
                            "V",
                            "ns=1;i=99",
                            {"Id": ("V", "ns=1;i=100", {})},
                        ),
                    },
                ),
                "DefaultInstanceBrowseName": ("V", "ns=1;i=134", {}),
                "Installation": (
                    "O",
                    "ns=1;i=40",
                    {
                        "CurrentState": (
                            "V",
                            "ns=1;i=41",
                            {"Id": ("V", "ns=1;i=42", {})},
                        ),
                        "Resume": ("M", "ns=1;i=61", {}),
                    },
                ),
                "Loading": ("O", "ns=1;i=2", {}),
                "Parameters": (
                    "O",
                    "ns=1;i=122",
                    {
                        "ClientProcessingTimeout": ("V", "ns=1;i=123", {}),
                        "CloseAndCommit": (
                            "M",
                            "ns=1;i=130",
                            {
                                "InputArguments": ("V", "ns=1;i=131", {}),
                                "OutputArguments": ("V", "ns=1;i=132", {}),
                            },
                        ),
                        "GenerateFileForRead": (
                            "M",
                            "ns=1;i=124",
                            {
                                "InputArguments": ("V", "ns=1;i=125", {}),
                                "OutputArguments": ("V", "ns=1;i=126", {}),
                            },
                        ),
                        "GenerateFileForWrite": (
                            "M",
                            "ns=1;i=127",
                            {
                                "InputArguments": ("V", "ns=1;i=128", {}),
                                "OutputArguments": ("V", "ns=1;i=129", {}),
                            },
                        ),
                    },
                ),
                "PowerCycle": (
                    "O",
                    "ns=1;i=76",
                    {
                        "CurrentState": (
                            "V",
                            "ns=1;i=77",
                            {"Id": ("V", "ns=1;i=78", {})},
                        )
                    },
                ),
                "PrepareForUpdate": (
                    "O",
                    "ns=1;i=4",
                    {
                        "Abort": ("M", "ns=1;i=20", {}),
                        "CurrentState": (
                            "V",
                            "ns=1;i=5",
                            {"Id": ("V", "ns=1;i=6", {})},
                        ),
                        "Prepare": ("M", "ns=1;i=19", {}),
                    },
                ),
                "SoftwareClass": ("V", "ns=1;i=352", {}),
                "SoftwareName": ("V", "ns=1;i=354", {}),
                "SoftwareSubclass": ("V", "ns=1;i=353", {}),
                "UnsignedPackageAllowed": ("V", "ns=1;i=355", {}),
                "UpdateStatus": ("V", "ns=1;i=133", {}),
                "VendorErrorCode": ("V", "ns=1;i=402", {}),
            },
        ),
        "SoftwareVersionType": (
            "OT",
            "ns=1;i=212",
            {
                "ChangeLogReference": ("V", "ns=1;i=385", {}),
                "Clear": ("M", "ns=1;i=359", {}),
                "Hash": ("V", "ns=1;i=386", {}),
                "Manufacturer": ("V", "ns=1;i=380", {}),
                "ManufacturerUri": ("V", "ns=1;i=381", {}),
                "PatchIdentifiers": ("V", "ns=1;i=383", {}),
                "ReleaseDate": ("V", "ns=1;i=384", {}),
                "SoftwareRevision": ("V", "ns=1;i=382", {}),
            },
        ),
        "TopologyElementType": (
            "OT",
            "ns=1;i=1001",
            {
                "<GroupIdentifier>": ("O", "ns=1;i=6567", {}),
                "BlockType": (
                    "OT",
                    "ns=1;i=1003",
                    {
                        "ActualMode": ("V", "ns=1;i=6010", {}),
                        "NormalMode": ("V", "ns=1;i=6012", {}),
                        "PermittedMode": ("V", "ns=1;i=6011", {}),
                        "RevisionCounter": ("V", "ns=1;i=6009", {}),
                        "TargetMode": ("V", "ns=1;i=6013", {}),
                    },
                ),
                "ComponentType": (
                    "OT",
                    "ns=1;i=15063",
                    {
                        "AssetId": ("V", "ns=1;i=15098", {}),
                        "ComponentName": ("V", "ns=1;i=15099", {}),
                        "DeviceClass": ("V", "ns=1;i=15094", {}),
                        "DeviceManual": ("V", "ns=1;i=15093", {}),
                        "DeviceRevision": ("V", "ns=1;i=15091", {}),
                        "DeviceType": (
                            "OT",
                            "ns=1;i=1002",
                            {
                                "<CPIdentifier>": (
                                    "O",
                                    "ns=1;i=6571",
                                    {"NetworkAddress": ("O", "ns=1;i=6592", {})},
                                ),
                                "DeviceClass": ("V", "ns=1;i=6470", {}),
                                "DeviceHealth": ("V", "ns=1;i=6208", {}),
                                "DeviceHealthAlarms": ("O", "ns=1;i=15105", {}),
                                "DeviceManual": ("V", "ns=1;i=6005", {}),
                                "DeviceRevision": ("V", "ns=1;i=6006", {}),
                                "DeviceTypeImage": (
                                    "O",
                                    "ns=1;i=6209",
                                    {"<ImageIdentifier>": ("V", "ns=1;i=6210", {})},
                                ),
                                "Documentation": (
                                    "O",
                                    "ns=1;i=6211",
                                    {"<DocumentIdentifier>": ("V", "ns=1;i=6212", {})},
                                ),
                                "HardwareRevision": ("V", "ns=1;i=6008", {}),
                                "ImageSet": (
                                    "O",
                                    "ns=1;i=6215",
                                    {"<ImageIdentifier>": ("V", "ns=1;i=6216", {})},
                                ),
                                "Manufacturer": ("V", "ns=1;i=6003", {}),
                                "ManufacturerUri": ("V", "ns=1;i=15100", {}),
                                "Model": ("V", "ns=1;i=6004", {}),
                                "ProductCode": ("V", "ns=1;i=15101", {}),
                                "ProductInstanceUri": ("V", "ns=1;i=15102", {}),
                                "ProtocolSupport": (
                                    "O",
                                    "ns=1;i=6213",
                                    {
                                        "<ProtocolSupportIdentifier>": (
                                            "V",
                                            "ns=1;i=6214",
                                            {},
                                        )
                                    },
                                ),
                                "RevisionCounter": ("V", "ns=1;i=6002", {}),
                                "SerialNumber": ("V", "ns=1;i=6001", {}),
                                "SoftwareRevision": ("V", "ns=1;i=6007", {}),
                            },
                        ),
                        "HardwareRevision": ("V", "ns=1;i=15089", {}),
                        "Manufacturer": ("V", "ns=1;i=15086", {}),
                        "ManufacturerUri": ("V", "ns=1;i=15087", {}),
                        "Model": ("V", "ns=1;i=15088", {}),
                        "ProductCode": ("V", "ns=1;i=15092", {}),
                        "ProductInstanceUri": ("V", "ns=1;i=15096", {}),
                        "RevisionCounter": ("V", "ns=1;i=15097", {}),
                        "SerialNumber": ("V", "ns=1;i=15095", {}),
                        "SoftwareRevision": ("V", "ns=1;i=15090", {}),
                        "SoftwareType": (
                            "OT",
                            "ns=1;i=15106",
                            {
                                "Manufacturer": ("V", "ns=1;i=15129", {}),
                                "Model": ("V", "ns=1;i=15131", {}),
                                "SoftwareRevision": ("V", "ns=1;i=15133", {}),
                            },
                        ),
                    },
                ),
                "ConnectionPointType": (
                    "OT",
                    "ns=1;i=6308",
                    {
                        "<ProfileIdentifier>": ("O", "ns=1;i=6499", {}),
                        "NetworkAddress": ("O", "ns=1;i=6354", {}),
                    },
                ),
                "Identification": ("O", "ns=1;i=6014", {}),
                "Lock": (
                    "O",
                    "ns=1;i=6161",
                    {
                        "BreakLock": (
                            "M",
                            "ns=1;i=6173",
                            {"OutputArguments": ("V", "ns=1;i=6174", {})},
                        ),
                        "ExitLock": (
                            "M",
                            "ns=1;i=6171",
                            {"OutputArguments": ("V", "ns=1;i=6172", {})},
                        ),
                        "InitLock": (
                            "M",
                            "ns=1;i=6166",
                            {
                                "InputArguments": ("V", "ns=1;i=6167", {}),
                                "OutputArguments": ("V", "ns=1;i=6168", {}),
                            },
                        ),
                        "Locked": ("V", "ns=1;i=6468", {}),
                        "LockingClient": ("V", "ns=1;i=6163", {}),
                        "LockingUser": ("V", "ns=1;i=6164", {}),
                        "RemainingLockTime": ("V", "ns=1;i=6165", {}),
                        "RenewLock": (
                            "M",
                            "ns=1;i=6169",
                            {"OutputArguments": ("V", "ns=1;i=6170", {})},
                        ),
                    },
                ),
                "MethodSet": ("O", "ns=1;i=5003", {}),
                "ParameterSet": (
                    "O",
                    "ns=1;i=5002",
                    {"<ParameterIdentifier>": ("V", "ns=1;i=6017", {})},
                ),
            },
        ),
        "TransferServicesType": (
            "OT",
            "ns=1;i=6526",
            {
                "FetchTransferResultData": (
                    "M",
                    "ns=1;i=6531",
                    {
                        "InputArguments": ("V", "ns=1;i=6532", {}),
                        "OutputArguments": ("V", "ns=1;i=6533", {}),
                    },
                ),
                "TransferFromDevice": (
                    "M",
                    "ns=1;i=6529",
                    {"OutputArguments": ("V", "ns=1;i=6530", {})},
                ),
                "TransferToDevice": (
                    "M",
                    "ns=1;i=6527",
                    {"OutputArguments": ("V", "ns=1;i=6528", {})},
                ),
            },
        ),
    },
    "reftypes": {
        "CanUpdate": ("RT", "ns=1;i=97", {}),
        "ConnectsTo": (
            "RT",
            "ns=1;i=6030",
            {"ConnectsToParent": ("RT", "ns=1;i=6467", {})},
        ),
        "IsOnline": ("RT", "ns=1;i=6031", {}),
        "UpdateParent": ("RT", "ns=1;i=96", {}),
    },
    "vartypes": {
        "LifetimeVariableType": (
            "VT",
            "ns=1;i=468",
            {
                "Indication": ("V", "ns=1;i=471", {}),
                "LimitValue": ("V", "ns=1;i=470", {}),
                "StartValue": ("V", "ns=1;i=469", {}),
                "WarningValues": ("V", "ns=1;i=472", {}),
            },
        ),
        "UIElementType": ("VT", "ns=1;i=6246", {}),
    },
}
