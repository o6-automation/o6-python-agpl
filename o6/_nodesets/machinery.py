# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 1bc4ba9f70d07c51d3310123f2ae2186703eb6cf4f2d26aea4a2853423b61b41
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/Machinery/"
_VERSION: str = "1.04.1"
_REQUIRED: list = [
    {"uri": "http://opcfoundation.org/UA/", "version": "1.05.02"},
    {"uri": "http://opcfoundation.org/UA/DI/", "version": "1.04.0"},
    {"uri": "http://opcfoundation.org/UA/IA/", "version": "1.01.2"},
]
_STRUCTURES: list = []
_ENUMS: list = []
_ORIGINAL_NODEIDS: tuple = ([], [])
_NODES: dict = {
    "objects": {
        "Identification": (
            "O",
            "ns=1;i=5003",
            {
                "Manufacturer": ("V", "ns=1;i=6019", {}),
                "SerialNumber": ("V", "ns=1;i=6020", {}),
            },
        ),
        "Machines": ("O", "ns=1;i=1001", {}),
        "http://opcfoundation.org/UA/Machinery/": (
            "O",
            "ns=1;i=5001",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=6031", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=6032", {}),
                "NamespaceUri": ("V", "ns=1;i=6033", {}),
                "NamespaceVersion": ("V", "ns=1;i=6034", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=6035", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=6036", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=6037", {}),
            },
        ),
    },
    "objtypes": {
        "IMachineTagNameplateType": (
            "OT",
            "ns=1;i=1011",
            {
                "IMachineryEquipmentType": (
                    "OT",
                    "ns=1;i=1007",
                    {
                        "Description": ("V", "ns=1;i=6107", {}),
                        "EquipmentLife": (
                            "V",
                            "ns=1;i=6109",
                            {
                                "EngineeringUnits": ("V", "ns=1;i=6112", {}),
                                "LimitValue": ("V", "ns=1;i=6110", {}),
                                "StartValue": ("V", "ns=1;i=6111", {}),
                            },
                        ),
                        "MachineryEquipmentTypeId": ("V", "ns=1;i=6108", {}),
                    },
                ),
                "Location": ("V", "ns=1;i=6028", {}),
            },
        ),
        "IMachineryItemVendorNameplateType": (
            "OT",
            "ns=1;i=1003",
            {
                "IMachineVendorNameplateType": (
                    "OT",
                    "ns=1;i=1010",
                    {"ProductInstanceUri": ("V", "ns=1;i=6023", {})},
                ),
                "InitialOperationDate": ("V", "ns=1;i=6027", {}),
                "Manufacturer": ("V", "ns=1;i=6022", {}),
                "MonthOfConstruction": ("V", "ns=1;i=6026", {}),
                "SerialNumber": ("V", "ns=1;i=6024", {}),
                "YearOfConstruction": ("V", "ns=1;i=6025", {}),
            },
        ),
        "MachineComponentsType": (
            "OT",
            "ns=1;i=1006",
            {
                "<Component>": ("O", "ns=1;i=5002", {}),
                "DefaultInstanceBrowseName": ("V", "ns=1;i=6018", {}),
            },
        ),
        "MachineryEquipmentFolderType": (
            "OT",
            "ns=1;i=1013",
            {
                "<MachineryEquipment>": (
                    "O",
                    "ns=1;i=5052",
                    {
                        "AssetId": ("V", "ns=1;i=6096", {}),
                        "ComponentName": ("V", "ns=1;i=6097", {}),
                        "Description": ("V", "ns=1;i=6098", {}),
                        "DeviceClass": ("V", "ns=1;i=6099", {}),
                        "Location": ("V", "ns=1;i=6100", {}),
                        "MachineryEquipmentTypeId": ("V", "ns=1;i=6101", {}),
                        "ManufacturerUri": ("V", "ns=1;i=6102", {}),
                        "Model": ("V", "ns=1;i=6103", {}),
                        "SerialNumber": ("V", "ns=1;i=6104", {}),
                    },
                ),
                "DefaultInstanceBrowseName": ("V", "ns=1;i=6105", {}),
            },
        ),
        "MachineryItemIdentificationType": (
            "OT",
            "ns=1;i=1004",
            {
                "AssetId": ("V", "ns=1;i=6013", {}),
                "ComponentName": ("V", "ns=1;i=6014", {}),
                "DefaultInstanceBrowseName": ("V", "ns=1;i=6088", {}),
                "DeviceClass": ("V", "ns=1;i=6012", {}),
                "HardwareRevision": ("V", "ns=1;i=6010", {}),
                "InitialOperationDate": ("V", "ns=1;i=6006", {}),
                "MachineIdentificationType": (
                    "OT",
                    "ns=1;i=1012",
                    {
                        "DefaultInstanceBrowseName": ("V", "ns=1;i=6030", {}),
                        "Location": ("V", "ns=1;i=6029", {}),
                        "ProductInstanceUri": ("V", "ns=1;i=6015", {}),
                    },
                ),
                "MachineryComponentIdentificationType": (
                    "OT",
                    "ns=1;i=1005",
                    {
                        "DefaultInstanceBrowseName": ("V", "ns=1;i=6016", {}),
                        "DeviceRevision": ("V", "ns=1;i=6017", {}),
                    },
                ),
                "Manufacturer": ("V", "ns=1;i=6002", {}),
                "ManufacturerUri": ("V", "ns=1;i=6007", {}),
                "Model": ("V", "ns=1;i=6008", {}),
                "MonthOfConstruction": ("V", "ns=1;i=6005", {}),
                "ProductCode": ("V", "ns=1;i=6009", {}),
                "ProductInstanceUri": ("V", "ns=1;i=6001", {}),
                "SerialNumber": ("V", "ns=1;i=6003", {}),
                "SoftwareRevision": ("V", "ns=1;i=6011", {}),
                "YearOfConstruction": ("V", "ns=1;i=6004", {}),
            },
        ),
        "MachineryItemState_StateMachineType": (
            "OT",
            "ns=1;i=1002",
            {
                "DefaultInstanceBrowseName": ("V", "ns=1;i=6021", {}),
                "Executing": (
                    "O",
                    "ns=1;i=5006",
                    {"StateNumber": ("V", "ns=1;i=6040", {})},
                ),
                "FromExecutingToExecuting": (
                    "O",
                    "ns=1;i=5023",
                    {"TransitionNumber": ("V", "ns=1;i=6057", {})},
                ),
                "FromExecutingToNotAvailable": (
                    "O",
                    "ns=1;i=5020",
                    {"TransitionNumber": ("V", "ns=1;i=6054", {})},
                ),
                "FromExecutingToNotExecuting": (
                    "O",
                    "ns=1;i=5022",
                    {"TransitionNumber": ("V", "ns=1;i=6056", {})},
                ),
                "FromExecutingToOutOfService": (
                    "O",
                    "ns=1;i=5021",
                    {"TransitionNumber": ("V", "ns=1;i=6055", {})},
                ),
                "FromNotAvailableToExecuting": (
                    "O",
                    "ns=1;i=5010",
                    {"TransitionNumber": ("V", "ns=1;i=6044", {})},
                ),
                "FromNotAvailableToNotAvailable": (
                    "O",
                    "ns=1;i=5011",
                    {"TransitionNumber": ("V", "ns=1;i=6045", {})},
                ),
                "FromNotAvailableToNotExecuting": (
                    "O",
                    "ns=1;i=5009",
                    {"TransitionNumber": ("V", "ns=1;i=6043", {})},
                ),
                "FromNotAvailableToOutOfService": (
                    "O",
                    "ns=1;i=5008",
                    {"TransitionNumber": ("V", "ns=1;i=6042", {})},
                ),
                "FromNotExecutingToExecuting": (
                    "O",
                    "ns=1;i=5018",
                    {"TransitionNumber": ("V", "ns=1;i=6052", {})},
                ),
                "FromNotExecutingToNotAvailable": (
                    "O",
                    "ns=1;i=5016",
                    {"TransitionNumber": ("V", "ns=1;i=6050", {})},
                ),
                "FromNotExecutingToNotExecuting": (
                    "O",
                    "ns=1;i=5019",
                    {"TransitionNumber": ("V", "ns=1;i=6053", {})},
                ),
                "FromNotExecutingToOutOfService": (
                    "O",
                    "ns=1;i=5017",
                    {"TransitionNumber": ("V", "ns=1;i=6051", {})},
                ),
                "FromOutOfServiceToExecuting": (
                    "O",
                    "ns=1;i=5014",
                    {"TransitionNumber": ("V", "ns=1;i=6048", {})},
                ),
                "FromOutOfServiceToNotAvailable": (
                    "O",
                    "ns=1;i=5012",
                    {"TransitionNumber": ("V", "ns=1;i=6046", {})},
                ),
                "FromOutOfServiceToNotExecuting": (
                    "O",
                    "ns=1;i=5013",
                    {"TransitionNumber": ("V", "ns=1;i=6047", {})},
                ),
                "FromOutOfServiceToOutOfService": (
                    "O",
                    "ns=1;i=5015",
                    {"TransitionNumber": ("V", "ns=1;i=6049", {})},
                ),
                "NotAvailable": (
                    "O",
                    "ns=1;i=5005",
                    {"StateNumber": ("V", "ns=1;i=6039", {})},
                ),
                "NotExecuting": (
                    "O",
                    "ns=1;i=5007",
                    {"StateNumber": ("V", "ns=1;i=6041", {})},
                ),
                "OutOfService": (
                    "O",
                    "ns=1;i=5004",
                    {"StateNumber": ("V", "ns=1;i=6038", {})},
                ),
            },
        ),
        "MachineryLifetimeCounterType": (
            "OT",
            "ns=1;i=1015",
            {
                "<LifetimeVariable>": (
                    "V",
                    "ns=1;i=6083",
                    {
                        "EngineeringUnits": ("V", "ns=1;i=6086", {}),
                        "LimitValue": ("V", "ns=1;i=6084", {}),
                        "StartValue": ("V", "ns=1;i=6085", {}),
                    },
                ),
                "DefaultInstanceBrowseName": ("V", "ns=1;i=6087", {}),
            },
        ),
        "MachineryOperationCounterType": (
            "OT",
            "ns=1;i=1009",
            {
                "DefaultInstanceBrowseName": ("V", "ns=1;i=6082", {}),
                "OperationCycleCounter": ("V", "ns=1;i=6081", {}),
                "OperationDuration": ("V", "ns=1;i=6080", {}),
                "PowerOnDuration": ("V", "ns=1;i=6079", {}),
            },
        ),
        "MachineryOperationModeStateMachineType": (
            "OT",
            "ns=1;i=1008",
            {
                "DefaultInstanceBrowseName": ("V", "ns=1;i=6058", {}),
                "FromMaintenanceToMaintenance": (
                    "O",
                    "ns=1;i=5035",
                    {"TransitionNumber": ("V", "ns=1;i=6070", {})},
                ),
                "FromMaintenanceToNone": (
                    "O",
                    "ns=1;i=5032",
                    {"TransitionNumber": ("V", "ns=1;i=6067", {})},
                ),
                "FromMaintenanceToProcessing": (
                    "O",
                    "ns=1;i=5034",
                    {"TransitionNumber": ("V", "ns=1;i=6069", {})},
                ),
                "FromMaintenanceToSetup": (
                    "O",
                    "ns=1;i=5033",
                    {"TransitionNumber": ("V", "ns=1;i=6068", {})},
                ),
                "FromNoneToMaintenance": (
                    "O",
                    "ns=1;i=5028",
                    {"TransitionNumber": ("V", "ns=1;i=6063", {})},
                ),
                "FromNoneToNone": (
                    "O",
                    "ns=1;i=5031",
                    {"TransitionNumber": ("V", "ns=1;i=6066", {})},
                ),
                "FromNoneToProcessing": (
                    "O",
                    "ns=1;i=5030",
                    {"TransitionNumber": ("V", "ns=1;i=6065", {})},
                ),
                "FromNoneToSetup": (
                    "O",
                    "ns=1;i=5029",
                    {"TransitionNumber": ("V", "ns=1;i=6064", {})},
                ),
                "FromProcessingToMaintenance": (
                    "O",
                    "ns=1;i=5041",
                    {"TransitionNumber": ("V", "ns=1;i=6076", {})},
                ),
                "FromProcessingToNone": (
                    "O",
                    "ns=1;i=5040",
                    {"TransitionNumber": ("V", "ns=1;i=6075", {})},
                ),
                "FromProcessingToProcessing": (
                    "O",
                    "ns=1;i=5043",
                    {"TransitionNumber": ("V", "ns=1;i=6078", {})},
                ),
                "FromProcessingToSetup": (
                    "O",
                    "ns=1;i=5042",
                    {"TransitionNumber": ("V", "ns=1;i=6077", {})},
                ),
                "FromSetupToMaintenance": (
                    "O",
                    "ns=1;i=5037",
                    {"TransitionNumber": ("V", "ns=1;i=6072", {})},
                ),
                "FromSetupToNone": (
                    "O",
                    "ns=1;i=5036",
                    {"TransitionNumber": ("V", "ns=1;i=6071", {})},
                ),
                "FromSetupToProcessing": (
                    "O",
                    "ns=1;i=5038",
                    {"TransitionNumber": ("V", "ns=1;i=6073", {})},
                ),
                "FromSetupToSetup": (
                    "O",
                    "ns=1;i=5039",
                    {"TransitionNumber": ("V", "ns=1;i=6074", {})},
                ),
                "Maintenance": (
                    "O",
                    "ns=1;i=5025",
                    {"StateNumber": ("V", "ns=1;i=6060", {})},
                ),
                "None": ("O", "ns=1;i=5024", {"StateNumber": ("V", "ns=1;i=6059", {})}),
                "Processing": (
                    "O",
                    "ns=1;i=5026",
                    {"StateNumber": ("V", "ns=1;i=6061", {})},
                ),
                "Setup": (
                    "O",
                    "ns=1;i=5027",
                    {"StateNumber": ("V", "ns=1;i=6062", {})},
                ),
            },
        ),
        "MonitoringType": (
            "OT",
            "ns=1;i=1014",
            {
                "Consumption": ("O", "ns=1;i=5047", {}),
                "DefaultInstanceBrowseName": ("V", "ns=1;i=6089", {}),
                "Health": (
                    "O",
                    "ns=1;i=5045",
                    {
                        "DeviceHealth": ("V", "ns=1;i=6095", {}),
                        "DeviceHealthAlarms": ("O", "ns=1;i=5051", {}),
                    },
                ),
                "Process": ("O", "ns=1;i=5046", {}),
                "Status": (
                    "O",
                    "ns=1;i=5044",
                    {
                        "MachineryItemState": (
                            "O",
                            "ns=1;i=5048",
                            {
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=6090",
                                    {"Id": ("V", "ns=1;i=6091", {})},
                                )
                            },
                        ),
                        "MachineryOperationMode": (
                            "O",
                            "ns=1;i=5049",
                            {
                                "CurrentState": (
                                    "V",
                                    "ns=1;i=6092",
                                    {"Id": ("V", "ns=1;i=6093", {})},
                                )
                            },
                        ),
                        "Stacklight": (
                            "O",
                            "ns=1;i=5050",
                            {"StacklightMode": ("V", "ns=1;i=6094", {})},
                        ),
                    },
                ),
            },
        ),
        "NotificationsType": (
            "OT",
            "ns=1;i=1017",
            {"DefaultInstanceBrowseName": ("V", "ns=1;i=6106", {})},
        ),
    },
}
