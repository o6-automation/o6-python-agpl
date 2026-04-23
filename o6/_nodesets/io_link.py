# AUTO-GENERATED — DO NOT EDIT
# source-sha256: c14aff63a0be722eb648562ac1ef6c699615bd494a1111c117047f5b6d5cdd83
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/IOLink/"
_VERSION: str = "1.00.1"
_REQUIRED: list = [
    {"uri": "http://opcfoundation.org/UA/", "version": "1.04.10"},
    {"uri": "http://opcfoundation.org/UA/DI/", "version": "1.03.0"},
]
_STRUCTURES: list = []
_ENUMS: list = [
    (
        "ns=1;i=3000",
        "EncodingEnum",
        {
            "fields": [
                {"name": "ASCII_0", "value": 0, "display_name": "ASCII_0"},
                {"name": "UTF8_1", "value": 1, "display_name": "UTF8_1"},
            ]
        },
    )
]
_ORIGINAL_NODEIDS: tuple = ([], ["ns=1;i=3000"])
_NODES: dict = {
    "datatypes": {
        "EncodingEnum": ("D", "ns=1;i=3000", {"EnumValues": ("V", "ns=1;i=6000", {})})
    },
    "eventtypes": {
        "IOLinkEventType": (
            "OT",
            "ns=1;i=1003",
            {
                "IOLinkDeviceEventType": (
                    "OT",
                    "ns=1;i=1004",
                    {
                        "IOLinkIODDDeviceEventType": (
                            "OT",
                            "ns=1;i=1021",
                            {"Name": ("V", "ns=1;i=6205", {})},
                        )
                    },
                ),
                "IOLinkEventCode": ("V", "ns=1;i=6018", {}),
                "IOLinkMasterEventType": ("OT", "ns=1;i=1006", {}),
                "IOLinkPortEventType": (
                    "OT",
                    "ns=1;i=1005",
                    {"IOLinkEventCode": ("V", "ns=1;i=6338", {})},
                ),
            },
        )
    },
    "objects": {
        "IODDManagement": (
            "O",
            "ns=1;i=10000",
            {
                "IODDs": ("O", "ns=1;i=10001", {}),
                "RemoveIODD": (
                    "M",
                    "ns=1;i=10002",
                    {
                        "InputArguments": ("V", "ns=1;i=10003", {}),
                        "OutputArguments": ("V", "ns=1;i=10004", {}),
                    },
                ),
                "TemporaryFileTransfer": (
                    "O",
                    "ns=1;i=10005",
                    {
                        "ClientProcessingTimeout": ("V", "ns=1;i=10006", {}),
                        "CloseAndCommit": (
                            "M",
                            "ns=1;i=10007",
                            {
                                "InputArguments": ("V", "ns=1;i=10008", {}),
                                "OutputArguments": ("V", "ns=1;i=10009", {}),
                            },
                        ),
                        "GenerateFileForRead": (
                            "M",
                            "ns=1;i=10010",
                            {
                                "InputArguments": ("V", "ns=1;i=10011", {}),
                                "OutputArguments": ("V", "ns=1;i=10012", {}),
                            },
                        ),
                        "GenerateFileForWrite": (
                            "M",
                            "ns=1;i=10013",
                            {
                                "InputArguments": ("V", "ns=1;i=10014", {}),
                                "OutputArguments": ("V", "ns=1;i=10015", {}),
                            },
                        ),
                    },
                ),
                "TransferIODD": (
                    "O",
                    "ns=1;i=10016",
                    {
                        "ClientProcessingTimeout": ("V", "ns=1;i=10017", {}),
                        "CloseAndCommit": (
                            "M",
                            "ns=1;i=10018",
                            {
                                "InputArguments": ("V", "ns=1;i=10019", {}),
                                "OutputArguments": ("V", "ns=1;i=10020", {}),
                            },
                        ),
                        "GenerateFileForRead": (
                            "M",
                            "ns=1;i=10021",
                            {
                                "InputArguments": ("V", "ns=1;i=10022", {}),
                                "OutputArguments": ("V", "ns=1;i=10023", {}),
                            },
                        ),
                        "GenerateFileForWrite": (
                            "M",
                            "ns=1;i=10024",
                            {
                                "InputArguments": ("V", "ns=1;i=10025", {}),
                                "OutputArguments": ("V", "ns=1;i=10026", {}),
                            },
                        ),
                    },
                ),
            },
        ),
        "IOLinkMasterSet": ("O", "ns=1;i=5005", {}),
        "http://opcfoundation.org/UA/IOLink/": (
            "O",
            "ns=1;i=5021",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=6001", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=6011", {}),
                "NamespaceUri": ("V", "ns=1;i=6012", {}),
                "NamespaceVersion": ("V", "ns=1;i=6013", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=6014", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=6015", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=6016", {}),
            },
        ),
    },
    "objtypes": {
        "DeviceVariantType": (
            "OT",
            "ns=1;i=1013",
            {
                "Description": ("V", "ns=1;i=6068", {}),
                "DeviceIcon": ("V", "ns=1;i=6070", {}),
                "DeviceSymbol": ("V", "ns=1;i=6069", {}),
                "Name": ("V", "ns=1;i=6067", {}),
                "ProductId": ("V", "ns=1;i=6066", {}),
            },
        ),
        "IOLinkAlarmType": (
            "OT",
            "ns=1;i=1007",
            {
                "IOLinkDeviceAlarmType": (
                    "OT",
                    "ns=1;i=1008",
                    {
                        "IOLinkIODDDeviceAlarmType": (
                            "OT",
                            "ns=1;i=1009",
                            {"Name": ("V", "ns=1;i=6020", {})},
                        )
                    },
                ),
                "IOLinkEventCode": ("V", "ns=1;i=6019", {}),
                "IOLinkMasterAlarmType": ("OT", "ns=1;i=1011", {}),
                "IOLinkPortAlarmType": ("OT", "ns=1;i=1010", {}),
            },
        ),
        "IOLinkDeviceType": (
            "OT",
            "ns=1;i=1002",
            {
                "Alarms": ("O", "ns=1;i=5006", {}),
                "DeviceAccessLocks": ("V", "ns=1;i=6006", {}),
                "DeviceHealth": ("V", "ns=1;i=6142", {}),
                "DeviceID": ("V", "ns=1;i=6005", {}),
                "General": ("O", "ns=1;i=5004", {}),
                "HardwareRevision": ("V", "ns=1;i=6140", {}),
                "IOLinkIODDDeviceType": (
                    "OT",
                    "ns=1;i=1012",
                    {
                        "DeviceName": ("V", "ns=1;i=6057", {}),
                        "DeviceTypeImage": (
                            "O",
                            "ns=1;i=5014",
                            {"<ImageIdentifier>": ("V", "ns=1;i=6059", {})},
                        ),
                        "DeviceVariant": (
                            "O",
                            "ns=1;i=5013",
                            {
                                "Description": ("V", "ns=1;i=6071", {}),
                                "DeviceIcon": ("V", "ns=1;i=6074", {}),
                                "DeviceSymbol": ("V", "ns=1;i=6075", {}),
                                "Name": ("V", "ns=1;i=6072", {}),
                                "ProductId": ("V", "ns=1;i=6073", {}),
                            },
                        ),
                        "DeviceVariants": ("O", "ns=1;i=5012", {}),
                        "IODDInformation": (
                            "O",
                            "ns=1;i=5011",
                            {
                                "Copyright": ("V", "ns=1;i=6064", {}),
                                "IOLinkRevision": ("V", "ns=1;i=6065", {}),
                                "ReleaseDate": ("V", "ns=1;i=6063", {}),
                                "Version": ("V", "ns=1;i=6062", {}),
                            },
                        ),
                        "Maintenance": ("O", "ns=1;i=5009", {}),
                        "Observer": ("O", "ns=1;i=5010", {}),
                        "ParameterSet": (
                            "O",
                            "ns=1;i=5007",
                            {
                                "SupportedAccessLocks": (
                                    "V",
                                    "ns=1;i=6060",
                                    {"OptionSetValues": ("V", "ns=1;i=6061", {})},
                                )
                            },
                        ),
                        "Specialist": ("O", "ns=1;i=5008", {}),
                        "VendorLogo": ("V", "ns=1;i=6058", {}),
                        "VendorURL": ("V", "ns=1;i=6056", {}),
                    },
                ),
                "Identification": (
                    "O",
                    "ns=1;i=5001",
                    {
                        "ApplicationSpecificTag": (
                            "V",
                            "ns=1;i=6021",
                            {"StoredInDevice": ("V", "ns=1;i=6030", {})},
                        ),
                        "FunctionTag": (
                            "V",
                            "ns=1;i=6022",
                            {"StoredInDevice": ("V", "ns=1;i=6031", {})},
                        ),
                        "LocationTag": (
                            "V",
                            "ns=1;i=6023",
                            {"StoredInDevice": ("V", "ns=1;i=6032", {})},
                        ),
                    },
                ),
                "Manufacturer": ("V", "ns=1;i=6129", {}),
                "MethodSet": (
                    "O",
                    "ns=1;i=5002",
                    {
                        "ApplicationReset": (
                            "M",
                            "ns=1;i=7015",
                            {"OutputArguments": ("V", "ns=1;i=6046", {})},
                        ),
                        "DeviceReset": (
                            "M",
                            "ns=1;i=7014",
                            {"OutputArguments": ("V", "ns=1;i=6045", {})},
                        ),
                        "ParamBreak": (
                            "M",
                            "ns=1;i=7013",
                            {"OutputArguments": ("V", "ns=1;i=6044", {})},
                        ),
                        "ParamDownloadToDeviceStart": (
                            "M",
                            "ns=1;i=7010",
                            {"OutputArguments": ("V", "ns=1;i=6041", {})},
                        ),
                        "ParamDownloadToDeviceStop": (
                            "M",
                            "ns=1;i=7011",
                            {"OutputArguments": ("V", "ns=1;i=6042", {})},
                        ),
                        "ParamDownloadToDeviceStore": (
                            "M",
                            "ns=1;i=7012",
                            {"OutputArguments": ("V", "ns=1;i=6043", {})},
                        ),
                        "ParamUploadFromDeviceStart": (
                            "M",
                            "ns=1;i=7008",
                            {"OutputArguments": ("V", "ns=1;i=6039", {})},
                        ),
                        "ParamUploadFromDeviceStop": (
                            "M",
                            "ns=1;i=7009",
                            {"OutputArguments": ("V", "ns=1;i=6040", {})},
                        ),
                        "ReadISDU": (
                            "M",
                            "ns=1;i=7005",
                            {
                                "InputArguments": ("V", "ns=1;i=6033", {}),
                                "OutputArguments": ("V", "ns=1;i=6034", {}),
                            },
                        ),
                        "RestoreFactorySettings": (
                            "M",
                            "ns=1;i=7016",
                            {"OutputArguments": ("V", "ns=1;i=6047", {})},
                        ),
                        "SystemCommand": (
                            "M",
                            "ns=1;i=7007",
                            {
                                "InputArguments": ("V", "ns=1;i=6037", {}),
                                "OutputArguments": ("V", "ns=1;i=6038", {}),
                            },
                        ),
                        "WriteISDU": (
                            "M",
                            "ns=1;i=7006",
                            {
                                "InputArguments": ("V", "ns=1;i=6035", {}),
                                "OutputArguments": ("V", "ns=1;i=6036", {}),
                            },
                        ),
                    },
                ),
                "MinCycleTime": ("V", "ns=1;i=6002", {}),
                "Model": ("V", "ns=1;i=6139", {}),
                "ParameterSet": (
                    "O",
                    "ns=1;i=5003",
                    {
                        "DetailedDeviceStatus": ("V", "ns=1;i=6025", {}),
                        "ErrorCount": ("V", "ns=1;i=6024", {}),
                        "OffsetTime": ("V", "ns=1;i=6028", {}),
                        "ProcessDataInput": (
                            "V",
                            "ns=1;i=6027",
                            {"ProcessDataLength": ("V", "ns=1;i=6133", {})},
                        ),
                        "ProcessDataOutput": (
                            "V",
                            "ns=1;i=6026",
                            {"ProcessDataLength": ("V", "ns=1;i=6134", {})},
                        ),
                    },
                ),
                "ProductID": ("V", "ns=1;i=6009", {}),
                "ProductText": ("V", "ns=1;i=6010", {}),
                "ProfileCharacteristic": ("V", "ns=1;i=6007", {}),
                "RevisionID": ("V", "ns=1;i=6003", {}),
                "SerialNumber": ("V", "ns=1;i=6029", {}),
                "SoftwareRevision": ("V", "ns=1;i=6141", {}),
                "VendorID": ("V", "ns=1;i=6004", {}),
                "VendorText": ("V", "ns=1;i=6008", {}),
            },
        ),
        "IOLinkMasterType": (
            "OT",
            "ns=1;i=1014",
            {
                "Alarms": ("O", "ns=1;i=5025", {}),
                "Capabilities": ("O", "ns=1;i=5018", {}),
                "DeviceID": ("V", "ns=1;i=6078", {}),
                "IOLinkStackRevision": ("V", "ns=1;i=6084", {}),
                "Identification": (
                    "O",
                    "ns=1;i=5015",
                    {
                        "ApplicationSpecificTag": ("V", "ns=1;i=6102", {}),
                        "FunctionTag": ("V", "ns=1;i=6103", {}),
                        "LocationTag": ("V", "ns=1;i=6104", {}),
                        "MasterType": (
                            "V",
                            "ns=1;i=6105",
                            {"EnumStrings": ("V", "ns=1;i=6108", {})},
                        ),
                    },
                ),
                "Management": ("O", "ns=1;i=5019", {}),
                "MasterConfigurationDisabled": ("V", "ns=1;i=6085", {}),
                "MethodSet": (
                    "O",
                    "ns=1;i=5016",
                    {
                        "ResetStatisticsOnAllPorts": (
                            "M",
                            "ns=1;i=7025",
                            {"OutputArguments": ("V", "ns=1;i=6111", {})},
                        ),
                        "Restart": (
                            "M",
                            "ns=1;i=7024",
                            {
                                "InputArguments": ("V", "ns=1;i=6109", {}),
                                "OutputArguments": ("V", "ns=1;i=6110", {}),
                            },
                        ),
                    },
                ),
                "ParameterSet": (
                    "O",
                    "ns=1;i=5017",
                    {
                        "DateOfLastStatisticsReset": ("V", "ns=1;i=6106", {}),
                        "MaxNumberOfPorts": ("V", "ns=1;i=6100", {}),
                        "MaxPowerSupply": (
                            "V",
                            "ns=1;i=6101",
                            {"EngineeringUnits": ("V", "ns=1;i=6048", {})},
                        ),
                        "NumberOfIOLinkMasterStarts": ("V", "ns=1;i=6107", {}),
                    },
                ),
                "Port<n>": ("O", "ns=1;i=5023", {}),
                "ProductID": ("V", "ns=1;i=6079", {}),
                "ProductText": ("V", "ns=1;i=6080", {}),
                "RevisionID": ("V", "ns=1;i=6081", {}),
                "Statistics": ("O", "ns=1;i=5020", {}),
                "VendorID": ("V", "ns=1;i=6082", {}),
                "VendorURL": ("V", "ns=1;i=6083", {}),
            },
        ),
        "IOLinkPortType": (
            "OT",
            "ns=1;i=1015",
            {
                "Alarms": ("O", "ns=1;i=5038", {}),
                "Capabilities": ("O", "ns=1;i=5028", {}),
                "Configuration": (
                    "O",
                    "ns=1;i=5031",
                    {"ConfiguredDevice": ("O", "ns=1;i=5039", {})},
                ),
                "Device": ("O", "ns=1;i=5033", {}),
                "DeviceConfigurationDisabled": ("V", "ns=1;i=6113", {}),
                "Information": ("O", "ns=1;i=5029", {}),
                "MethodSet": (
                    "O",
                    "ns=1;i=5026",
                    {
                        "ResetStatistics": (
                            "M",
                            "ns=1;i=7040",
                            {"OutputArguments": ("V", "ns=1;i=6179", {})},
                        ),
                        "UpdateConfiguration": (
                            "M",
                            "ns=1;i=7041",
                            {
                                "InputArguments": ("V", "ns=1;i=6180", {}),
                                "OutputArguments": ("V", "ns=1;i=6181", {}),
                            },
                        ),
                    },
                ),
                "ParameterSet": (
                    "O",
                    "ns=1;i=5027",
                    {
                        "ActualCycleTime": ("V", "ns=1;i=6166", {}),
                        "Baudrate": (
                            "V",
                            "ns=1;i=6164",
                            {"EnumStrings": ("V", "ns=1;i=6165", {})},
                        ),
                        "CycleTime": ("V", "ns=1;i=6154", {}),
                        "DateOfLastStatisticsReset": ("V", "ns=1;i=6173", {}),
                        "DeviceID": ("V", "ns=1;i=6162", {}),
                        "MaxPowerSupply": (
                            "V",
                            "ns=1;i=6152",
                            {"EngineeringUnits": ("V", "ns=1;i=6178", {})},
                        ),
                        "NumberOfAborts": ("V", "ns=1;i=6174", {}),
                        "NumberOfCycles": ("V", "ns=1;i=6175", {}),
                        "NumberOfDeviceHasBeenExchanged": ("V", "ns=1;i=6176", {}),
                        "NumberOfRetries": ("V", "ns=1;i=6177", {}),
                        "Pin2Configuration": (
                            "V",
                            "ns=1;i=6159",
                            {"EnumStrings": ("V", "ns=1;i=6160", {})},
                        ),
                        "Pin2ProcessData": ("V", "ns=1;i=6171", {}),
                        "Pin2Support": ("V", "ns=1;i=6153", {}),
                        "Pin4ProcessData": ("V", "ns=1;i=6172", {}),
                        "PortClass": (
                            "V",
                            "ns=1;i=6150",
                            {"EnumStrings": ("V", "ns=1;i=6151", {})},
                        ),
                        "PortMode": (
                            "V",
                            "ns=1;i=6157",
                            {"EnumStrings": ("V", "ns=1;i=6158", {})},
                        ),
                        "Quality": (
                            "V",
                            "ns=1;i=6167",
                            {"OptionSetValues": ("V", "ns=1;i=6168", {})},
                        ),
                        "Status": (
                            "V",
                            "ns=1;i=6169",
                            {"EnumStrings": ("V", "ns=1;i=6170", {})},
                        ),
                        "UseIODD": ("V", "ns=1;i=6161", {}),
                        "ValidationAndBackup": (
                            "V",
                            "ns=1;i=6155",
                            {"EnumStrings": ("V", "ns=1;i=6156", {})},
                        ),
                        "VendorID": ("V", "ns=1;i=6163", {}),
                    },
                ),
                "SIOProcessData": ("O", "ns=1;i=5032", {}),
                "Statistics": ("O", "ns=1;i=5030", {}),
            },
        ),
    },
    "reftypes": {
        "HasDiagnosisMenu": ("RT", "ns=1;i=4005", {}),
        "HasIdentificationMenu": ("RT", "ns=1;i=4002", {}),
        "HasObservationMenu": ("RT", "ns=1;i=4004", {}),
        "HasParameterMenu": ("RT", "ns=1;i=4003", {}),
    },
    "vartypes": {
        "ProcessDataVariableType": (
            "VT",
            "ns=1;i=2002",
            {
                "PDDescriptor": ("V", "ns=1;i=6146", {}),
                "ProcessDataLength": ("V", "ns=1;i=6147", {}),
            },
        )
    },
}
