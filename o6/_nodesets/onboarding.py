# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 45427b28130c819710ddbe5dd6a38b2c4dd82458a00693ee912e3ed4e934cbb8
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/Onboarding/"
_VERSION: str = "1.05.04"
_REQUIRED: list = [
    {"uri": "http://opcfoundation.org/UA/GDS/", "version": ""},
    {"uri": "http://opcfoundation.org/UA/", "version": "1.05.04"},
]
_STRUCTURES: list = [
    (
        "ns=1;i=1164",
        "CertificateAuthorityType",
        "ns=1;i=1439",
        {
            "structure_type": 0,
            "fields": [
                {"name": "AuthorityCertificate", "data_type": "i=15", "value_rank": -1},
                {"name": "IssuerCertificates", "data_type": "i=15", "value_rank": 1},
            ],
        },
    ),
    (
        "ns=1;i=1165",
        "BaseTicketType",
        "ns=1;i=1440",
        {
            "structure_type": 0,
            "fields": [
                {"name": "ManufacturerName", "data_type": "i=12", "value_rank": -1},
                {"name": "ModelName", "data_type": "i=12", "value_rank": -1},
                {"name": "ModelVersion", "data_type": "i=12", "value_rank": -1},
                {"name": "HardwareRevision", "data_type": "i=12", "value_rank": -1},
                {"name": "SoftwareRevision", "data_type": "i=12", "value_rank": -1},
                {"name": "SerialNumber", "data_type": "i=12", "value_rank": -1},
                {"name": "ManufactureDate", "data_type": "i=13", "value_rank": -1},
                {"name": "Authorities", "data_type": "ns=1;i=1164", "value_rank": 1},
            ],
        },
    ),
    (
        "ns=1;i=1166",
        "DeviceIdentityTicketType",
        "ns=1;i=1441",
        {
            "structure_type": 0,
            "fields": [
                {"name": "ProductInstanceUri", "data_type": "i=23751", "value_rank": -1}
            ],
        },
    ),
    (
        "ns=1;i=1167",
        "CompositeIdentityTicketType",
        "ns=1;i=1442",
        {
            "structure_type": 0,
            "fields": [
                {
                    "name": "CompositeInstanceUri",
                    "data_type": "i=23751",
                    "value_rank": -1,
                },
                {"name": "Devices", "data_type": "i=23751", "value_rank": 1},
                {"name": "Composites", "data_type": "i=23751", "value_rank": 1},
            ],
        },
    ),
    (
        "ns=1;i=1168",
        "TicketListType",
        "ns=1;i=1443",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Devices", "data_type": "i=12", "value_rank": 1},
                {"name": "Composites", "data_type": "i=12", "value_rank": 1},
            ],
        },
    ),
    (
        "ns=1;i=1495",
        "ManagerDescription",
        "ns=1;i=4206",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Name", "data_type": "i=21", "value_rank": -1},
                {"name": "IsRequired", "data_type": "i=1", "value_rank": -1},
                {"name": "PurposeUri", "data_type": "i=23751", "value_rank": -1},
                {"name": "ProtocolUri", "data_type": "i=23751", "value_rank": -1},
                {"name": "EndpointUrls", "data_type": "i=12", "value_rank": 1},
            ],
        },
    ),
]
_ENUMS: list = []
_ORIGINAL_NODEIDS: tuple = (
    [
        ("ns=1;i=1164", "ns=1;i=1439", ["i=15", "i=15"]),
        (
            "ns=1;i=1165",
            "ns=1;i=1440",
            ["i=12", "i=12", "i=12", "i=12", "i=12", "i=12", "i=13", "ns=1;i=1164"],
        ),
        ("ns=1;i=1166", "ns=1;i=1441", ["i=23751"]),
        ("ns=1;i=1167", "ns=1;i=1442", ["i=23751", "i=23751", "i=23751"]),
        ("ns=1;i=1168", "ns=1;i=1443", ["i=12", "i=12"]),
        ("ns=1;i=1495", "ns=1;i=4206", ["i=21", "i=1", "i=23751", "i=23751", "i=12"]),
    ],
    [],
)
_NODES: dict = {
    "datatypes": {
        "BaseTicketType": (
            "D",
            "ns=1;i=1165",
            {
                "CompositeIdentityTicketType": ("D", "ns=1;i=1167", {}),
                "DeviceIdentityTicketType": ("D", "ns=1;i=1166", {}),
            },
        ),
        "CertificateAuthorityType": ("D", "ns=1;i=1164", {}),
        "ManagerDescription": ("D", "ns=1;i=1495", {}),
        "TicketListType": ("D", "ns=1;i=1168", {}),
    },
    "eventtypes": {
        "DeviceRegistrationAuditEventType": (
            "OT",
            "ns=1;i=1517",
            {
                "DeviceIdentityAcceptedAuditEventType": (
                    "OT",
                    "ns=1;i=1533",
                    {
                        "Certificate": ("V", "ns=1;i=1549", {}),
                        "Composite": ("V", "ns=1;i=1551", {}),
                        "Ticket": ("V", "ns=1;i=1550", {}),
                    },
                ),
                "DeviceSoftwareUpdatedAuditEventType": (
                    "OT",
                    "ns=1;i=1552",
                    {
                        "SoftwareRevision": ("V", "ns=1;i=1568", {}),
                        "Status": ("V", "ns=1;i=1563", {}),
                    },
                ),
                "ProductInstanceUri": ("V", "ns=1;i=1532", {}),
            },
        )
    },
    "objects": {
        "Default Binary": ("O", "ns=1;i=4206", {}),
        "Default JSON": ("O", "ns=1;i=4222", {}),
        "Default XML": ("O", "ns=1;i=4214", {}),
        "DeviceRegistrar": (
            "O",
            "ns=1;i=1344",
            {
                "Administration": (
                    "O",
                    "ns=1;i=1350",
                    {
                        "DeviceIdentityAuthorities": (
                            "O",
                            "ns=1;i=1393",
                            {
                                "AddCertificate": (
                                    "M",
                                    "ns=1;i=1425",
                                    {"InputArguments": ("V", "ns=1;i=1426", {})},
                                ),
                                "Close": (
                                    "M",
                                    "ns=1;i=1404",
                                    {"InputArguments": ("V", "ns=1;i=1405", {})},
                                ),
                                "CloseAndUpdate": (
                                    "M",
                                    "ns=1;i=1422",
                                    {
                                        "InputArguments": ("V", "ns=1;i=1423", {}),
                                        "OutputArguments": ("V", "ns=1;i=1424", {}),
                                    },
                                ),
                                "GetPosition": (
                                    "M",
                                    "ns=1;i=1411",
                                    {
                                        "InputArguments": ("V", "ns=1;i=1412", {}),
                                        "OutputArguments": ("V", "ns=1;i=1413", {}),
                                    },
                                ),
                                "LastUpdateTime": ("V", "ns=1;i=1416", {}),
                                "Open": (
                                    "M",
                                    "ns=1;i=1401",
                                    {
                                        "InputArguments": ("V", "ns=1;i=1402", {}),
                                        "OutputArguments": ("V", "ns=1;i=1403", {}),
                                    },
                                ),
                                "OpenCount": ("V", "ns=1;i=1397", {}),
                                "OpenWithMasks": (
                                    "M",
                                    "ns=1;i=1419",
                                    {
                                        "InputArguments": ("V", "ns=1;i=1420", {}),
                                        "OutputArguments": ("V", "ns=1;i=1421", {}),
                                    },
                                ),
                                "Read": (
                                    "M",
                                    "ns=1;i=1406",
                                    {
                                        "InputArguments": ("V", "ns=1;i=1407", {}),
                                        "OutputArguments": ("V", "ns=1;i=1408", {}),
                                    },
                                ),
                                "RemoveCertificate": (
                                    "M",
                                    "ns=1;i=1427",
                                    {"InputArguments": ("V", "ns=1;i=1428", {})},
                                ),
                                "SetPosition": (
                                    "M",
                                    "ns=1;i=1414",
                                    {"InputArguments": ("V", "ns=1;i=1415", {})},
                                ),
                                "Size": ("V", "ns=1;i=1394", {}),
                                "UserWritable": ("V", "ns=1;i=1396", {}),
                                "Writable": ("V", "ns=1;i=1395", {}),
                                "Write": (
                                    "M",
                                    "ns=1;i=1409",
                                    {"InputArguments": ("V", "ns=1;i=1410", {})},
                                ),
                            },
                        ),
                        "RegisterTickets": (
                            "M",
                            "ns=1;i=1351",
                            {
                                "InputArguments": ("V", "ns=1;i=1352", {}),
                                "OutputArguments": ("V", "ns=1;i=1353", {}),
                            },
                        ),
                        "TicketAuthorities": (
                            "O",
                            "ns=1;i=1357",
                            {
                                "AddCertificate": (
                                    "M",
                                    "ns=1;i=1389",
                                    {"InputArguments": ("V", "ns=1;i=1390", {})},
                                ),
                                "Close": (
                                    "M",
                                    "ns=1;i=1368",
                                    {"InputArguments": ("V", "ns=1;i=1369", {})},
                                ),
                                "CloseAndUpdate": (
                                    "M",
                                    "ns=1;i=1386",
                                    {
                                        "InputArguments": ("V", "ns=1;i=1387", {}),
                                        "OutputArguments": ("V", "ns=1;i=1388", {}),
                                    },
                                ),
                                "GetPosition": (
                                    "M",
                                    "ns=1;i=1375",
                                    {
                                        "InputArguments": ("V", "ns=1;i=1376", {}),
                                        "OutputArguments": ("V", "ns=1;i=1377", {}),
                                    },
                                ),
                                "LastUpdateTime": ("V", "ns=1;i=1380", {}),
                                "Open": (
                                    "M",
                                    "ns=1;i=1365",
                                    {
                                        "InputArguments": ("V", "ns=1;i=1366", {}),
                                        "OutputArguments": ("V", "ns=1;i=1367", {}),
                                    },
                                ),
                                "OpenCount": ("V", "ns=1;i=1361", {}),
                                "OpenWithMasks": (
                                    "M",
                                    "ns=1;i=1383",
                                    {
                                        "InputArguments": ("V", "ns=1;i=1384", {}),
                                        "OutputArguments": ("V", "ns=1;i=1385", {}),
                                    },
                                ),
                                "Read": (
                                    "M",
                                    "ns=1;i=1370",
                                    {
                                        "InputArguments": ("V", "ns=1;i=1371", {}),
                                        "OutputArguments": ("V", "ns=1;i=1372", {}),
                                    },
                                ),
                                "RemoveCertificate": (
                                    "M",
                                    "ns=1;i=1391",
                                    {"InputArguments": ("V", "ns=1;i=1392", {})},
                                ),
                                "SetPosition": (
                                    "M",
                                    "ns=1;i=1378",
                                    {"InputArguments": ("V", "ns=1;i=1379", {})},
                                ),
                                "Size": ("V", "ns=1;i=1358", {}),
                                "UserWritable": ("V", "ns=1;i=1360", {}),
                                "Writable": ("V", "ns=1;i=1359", {}),
                                "Write": (
                                    "M",
                                    "ns=1;i=1373",
                                    {"InputArguments": ("V", "ns=1;i=1374", {})},
                                ),
                            },
                        ),
                        "UnregisterTickets": (
                            "M",
                            "ns=1;i=1354",
                            {
                                "InputArguments": ("V", "ns=1;i=1355", {}),
                                "OutputArguments": ("V", "ns=1;i=1356", {}),
                            },
                        ),
                    },
                ),
                "GetManagers": (
                    "M",
                    "ns=1;i=1512",
                    {"OutputArguments": ("V", "ns=1;i=1513", {})},
                ),
                "ProvideIdentities": (
                    "M",
                    "ns=1;i=1345",
                    {
                        "InputArguments": ("V", "ns=1;i=1346", {}),
                        "OutputArguments": ("V", "ns=1;i=1347", {}),
                    },
                ),
                "RegisterDeviceEndpoint": (
                    "M",
                    "ns=1;i=1348",
                    {"InputArguments": ("V", "ns=1;i=1349", {})},
                ),
                "RegisterManagedApplication": (
                    "M",
                    "ns=1;i=1514",
                    {
                        "InputArguments": ("V", "ns=1;i=1515", {}),
                        "OutputArguments": ("V", "ns=1;i=1516", {}),
                    },
                ),
                "UpdateSoftwareStatus": (
                    "M",
                    "ns=1;i=1510",
                    {"InputArguments": ("V", "ns=1;i=1511", {})},
                ),
            },
        ),
        "Opc.Ua.Onboarding": (
            "V",
            "ns=1;i=1468",
            {
                "BaseTicketType": ("V", "ns=1;i=1475", {}),
                "CertificateAuthorityType": ("V", "ns=1;i=1472", {}),
                "CompositeIdentityTicketType": ("V", "ns=1;i=1481", {}),
                "Deprecated": ("V", "ns=1;i=1471", {}),
                "DeviceIdentityTicketType": ("V", "ns=1;i=1478", {}),
                "ManagerDescription": ("V", "ns=1;i=4216", {}),
                "NamespaceUri": ("V", "ns=1;i=1470", {}),
                "TicketListType": ("V", "ns=1;i=1484", {}),
            },
        ),
        "RegistrarAdmin": (
            "O",
            "ns=1;i=5034",
            {
                "AddApplication": (
                    "M",
                    "ns=1;i=5045",
                    {"InputArguments": ("V", "ns=1;i=5046", {})},
                ),
                "AddEndpoint": (
                    "M",
                    "ns=1;i=5049",
                    {"InputArguments": ("V", "ns=1;i=5050", {})},
                ),
                "AddIdentity": (
                    "M",
                    "ns=1;i=5041",
                    {"InputArguments": ("V", "ns=1;i=5042", {})},
                ),
                "Applications": ("V", "ns=1;i=5037", {}),
                "ApplicationsExclude": ("V", "ns=1;i=5036", {}),
                "CustomConfiguration": ("V", "ns=1;i=5040", {}),
                "Endpoints": ("V", "ns=1;i=5039", {}),
                "EndpointsExclude": ("V", "ns=1;i=5038", {}),
                "Identities": ("V", "ns=1;i=5035", {}),
                "RemoveApplication": (
                    "M",
                    "ns=1;i=5047",
                    {"InputArguments": ("V", "ns=1;i=5048", {})},
                ),
                "RemoveEndpoint": (
                    "M",
                    "ns=1;i=5051",
                    {"InputArguments": ("V", "ns=1;i=5052", {})},
                ),
                "RemoveIdentity": (
                    "M",
                    "ns=1;i=5043",
                    {"InputArguments": ("V", "ns=1;i=5044", {})},
                ),
            },
        ),
        "http://opcfoundation.org/UA/Onboarding/": (
            "O",
            "ns=1;i=1",
            {
                "DefaultAccessRestrictions": ("V", "ns=1;i=35", {}),
                "DefaultRolePermissions": ("V", "ns=1;i=33", {}),
                "DefaultUserRolePermissions": ("V", "ns=1;i=34", {}),
                "IsNamespaceSubset": ("V", "ns=1;i=5", {}),
                "ModelVersion": ("V", "ns=1;i=4986", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=4", {}),
                "NamespaceUri": ("V", "ns=1;i=2", {}),
                "NamespaceVersion": ("V", "ns=1;i=3", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=6", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=7", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=8", {}),
            },
        ),
    },
    "objtypes": {
        "DeviceRegistrarAdminType": (
            "OT",
            "ns=1;i=1175",
            {
                "DeviceIdentityAuthorities": (
                    "O",
                    "ns=1;i=1218",
                    {
                        "AddCertificate": (
                            "M",
                            "ns=1;i=1250",
                            {"InputArguments": ("V", "ns=1;i=1251", {})},
                        ),
                        "Close": (
                            "M",
                            "ns=1;i=1229",
                            {"InputArguments": ("V", "ns=1;i=1230", {})},
                        ),
                        "CloseAndUpdate": (
                            "M",
                            "ns=1;i=1247",
                            {
                                "InputArguments": ("V", "ns=1;i=1248", {}),
                                "OutputArguments": ("V", "ns=1;i=1249", {}),
                            },
                        ),
                        "GetPosition": (
                            "M",
                            "ns=1;i=1236",
                            {
                                "InputArguments": ("V", "ns=1;i=1237", {}),
                                "OutputArguments": ("V", "ns=1;i=1238", {}),
                            },
                        ),
                        "LastUpdateTime": ("V", "ns=1;i=1241", {}),
                        "Open": (
                            "M",
                            "ns=1;i=1226",
                            {
                                "InputArguments": ("V", "ns=1;i=1227", {}),
                                "OutputArguments": ("V", "ns=1;i=1228", {}),
                            },
                        ),
                        "OpenCount": ("V", "ns=1;i=1222", {}),
                        "OpenWithMasks": (
                            "M",
                            "ns=1;i=1244",
                            {
                                "InputArguments": ("V", "ns=1;i=1245", {}),
                                "OutputArguments": ("V", "ns=1;i=1246", {}),
                            },
                        ),
                        "Read": (
                            "M",
                            "ns=1;i=1231",
                            {
                                "InputArguments": ("V", "ns=1;i=1232", {}),
                                "OutputArguments": ("V", "ns=1;i=1233", {}),
                            },
                        ),
                        "RemoveCertificate": (
                            "M",
                            "ns=1;i=1252",
                            {"InputArguments": ("V", "ns=1;i=1253", {})},
                        ),
                        "SetPosition": (
                            "M",
                            "ns=1;i=1239",
                            {"InputArguments": ("V", "ns=1;i=1240", {})},
                        ),
                        "Size": ("V", "ns=1;i=1219", {}),
                        "UserWritable": ("V", "ns=1;i=1221", {}),
                        "Writable": ("V", "ns=1;i=1220", {}),
                        "Write": (
                            "M",
                            "ns=1;i=1234",
                            {"InputArguments": ("V", "ns=1;i=1235", {})},
                        ),
                    },
                ),
                "RegisterTickets": (
                    "M",
                    "ns=1;i=1176",
                    {
                        "InputArguments": ("V", "ns=1;i=1177", {}),
                        "OutputArguments": ("V", "ns=1;i=1178", {}),
                    },
                ),
                "TicketAuthorities": (
                    "O",
                    "ns=1;i=1182",
                    {
                        "AddCertificate": (
                            "M",
                            "ns=1;i=1214",
                            {"InputArguments": ("V", "ns=1;i=1215", {})},
                        ),
                        "Close": (
                            "M",
                            "ns=1;i=1193",
                            {"InputArguments": ("V", "ns=1;i=1194", {})},
                        ),
                        "CloseAndUpdate": (
                            "M",
                            "ns=1;i=1211",
                            {
                                "InputArguments": ("V", "ns=1;i=1212", {}),
                                "OutputArguments": ("V", "ns=1;i=1213", {}),
                            },
                        ),
                        "GetPosition": (
                            "M",
                            "ns=1;i=1200",
                            {
                                "InputArguments": ("V", "ns=1;i=1201", {}),
                                "OutputArguments": ("V", "ns=1;i=1202", {}),
                            },
                        ),
                        "LastUpdateTime": ("V", "ns=1;i=1205", {}),
                        "Open": (
                            "M",
                            "ns=1;i=1190",
                            {
                                "InputArguments": ("V", "ns=1;i=1191", {}),
                                "OutputArguments": ("V", "ns=1;i=1192", {}),
                            },
                        ),
                        "OpenCount": ("V", "ns=1;i=1186", {}),
                        "OpenWithMasks": (
                            "M",
                            "ns=1;i=1208",
                            {
                                "InputArguments": ("V", "ns=1;i=1209", {}),
                                "OutputArguments": ("V", "ns=1;i=1210", {}),
                            },
                        ),
                        "Read": (
                            "M",
                            "ns=1;i=1195",
                            {
                                "InputArguments": ("V", "ns=1;i=1196", {}),
                                "OutputArguments": ("V", "ns=1;i=1197", {}),
                            },
                        ),
                        "RemoveCertificate": (
                            "M",
                            "ns=1;i=1216",
                            {"InputArguments": ("V", "ns=1;i=1217", {})},
                        ),
                        "SetPosition": (
                            "M",
                            "ns=1;i=1203",
                            {"InputArguments": ("V", "ns=1;i=1204", {})},
                        ),
                        "Size": ("V", "ns=1;i=1183", {}),
                        "UserWritable": ("V", "ns=1;i=1185", {}),
                        "Writable": ("V", "ns=1;i=1184", {}),
                        "Write": (
                            "M",
                            "ns=1;i=1198",
                            {"InputArguments": ("V", "ns=1;i=1199", {})},
                        ),
                    },
                ),
                "UnregisterTickets": (
                    "M",
                    "ns=1;i=1179",
                    {
                        "InputArguments": ("V", "ns=1;i=1180", {}),
                        "OutputArguments": ("V", "ns=1;i=1181", {}),
                    },
                ),
            },
        ),
        "DeviceRegistrarType": (
            "OT",
            "ns=1;i=1259",
            {
                "Administration": (
                    "O",
                    "ns=1;i=1265",
                    {
                        "DeviceIdentityAuthorities": (
                            "O",
                            "ns=1;i=1308",
                            {
                                "AddCertificate": (
                                    "M",
                                    "ns=1;i=1340",
                                    {"InputArguments": ("V", "ns=1;i=1341", {})},
                                ),
                                "Close": (
                                    "M",
                                    "ns=1;i=1319",
                                    {"InputArguments": ("V", "ns=1;i=1320", {})},
                                ),
                                "CloseAndUpdate": (
                                    "M",
                                    "ns=1;i=1337",
                                    {
                                        "InputArguments": ("V", "ns=1;i=1338", {}),
                                        "OutputArguments": ("V", "ns=1;i=1339", {}),
                                    },
                                ),
                                "GetPosition": (
                                    "M",
                                    "ns=1;i=1326",
                                    {
                                        "InputArguments": ("V", "ns=1;i=1327", {}),
                                        "OutputArguments": ("V", "ns=1;i=1328", {}),
                                    },
                                ),
                                "LastUpdateTime": ("V", "ns=1;i=1331", {}),
                                "Open": (
                                    "M",
                                    "ns=1;i=1316",
                                    {
                                        "InputArguments": ("V", "ns=1;i=1317", {}),
                                        "OutputArguments": ("V", "ns=1;i=1318", {}),
                                    },
                                ),
                                "OpenCount": ("V", "ns=1;i=1312", {}),
                                "OpenWithMasks": (
                                    "M",
                                    "ns=1;i=1334",
                                    {
                                        "InputArguments": ("V", "ns=1;i=1335", {}),
                                        "OutputArguments": ("V", "ns=1;i=1336", {}),
                                    },
                                ),
                                "Read": (
                                    "M",
                                    "ns=1;i=1321",
                                    {
                                        "InputArguments": ("V", "ns=1;i=1322", {}),
                                        "OutputArguments": ("V", "ns=1;i=1323", {}),
                                    },
                                ),
                                "RemoveCertificate": (
                                    "M",
                                    "ns=1;i=1342",
                                    {"InputArguments": ("V", "ns=1;i=1343", {})},
                                ),
                                "SetPosition": (
                                    "M",
                                    "ns=1;i=1329",
                                    {"InputArguments": ("V", "ns=1;i=1330", {})},
                                ),
                                "Size": ("V", "ns=1;i=1309", {}),
                                "UserWritable": ("V", "ns=1;i=1311", {}),
                                "Writable": ("V", "ns=1;i=1310", {}),
                                "Write": (
                                    "M",
                                    "ns=1;i=1324",
                                    {"InputArguments": ("V", "ns=1;i=1325", {})},
                                ),
                            },
                        ),
                        "RegisterTickets": (
                            "M",
                            "ns=1;i=1266",
                            {
                                "InputArguments": ("V", "ns=1;i=1267", {}),
                                "OutputArguments": ("V", "ns=1;i=1268", {}),
                            },
                        ),
                        "TicketAuthorities": (
                            "O",
                            "ns=1;i=1272",
                            {
                                "AddCertificate": (
                                    "M",
                                    "ns=1;i=1304",
                                    {"InputArguments": ("V", "ns=1;i=1305", {})},
                                ),
                                "Close": (
                                    "M",
                                    "ns=1;i=1283",
                                    {"InputArguments": ("V", "ns=1;i=1284", {})},
                                ),
                                "CloseAndUpdate": (
                                    "M",
                                    "ns=1;i=1301",
                                    {
                                        "InputArguments": ("V", "ns=1;i=1302", {}),
                                        "OutputArguments": ("V", "ns=1;i=1303", {}),
                                    },
                                ),
                                "GetPosition": (
                                    "M",
                                    "ns=1;i=1290",
                                    {
                                        "InputArguments": ("V", "ns=1;i=1291", {}),
                                        "OutputArguments": ("V", "ns=1;i=1292", {}),
                                    },
                                ),
                                "LastUpdateTime": ("V", "ns=1;i=1295", {}),
                                "Open": (
                                    "M",
                                    "ns=1;i=1280",
                                    {
                                        "InputArguments": ("V", "ns=1;i=1281", {}),
                                        "OutputArguments": ("V", "ns=1;i=1282", {}),
                                    },
                                ),
                                "OpenCount": ("V", "ns=1;i=1276", {}),
                                "OpenWithMasks": (
                                    "M",
                                    "ns=1;i=1298",
                                    {
                                        "InputArguments": ("V", "ns=1;i=1299", {}),
                                        "OutputArguments": ("V", "ns=1;i=1300", {}),
                                    },
                                ),
                                "Read": (
                                    "M",
                                    "ns=1;i=1285",
                                    {
                                        "InputArguments": ("V", "ns=1;i=1286", {}),
                                        "OutputArguments": ("V", "ns=1;i=1287", {}),
                                    },
                                ),
                                "RemoveCertificate": (
                                    "M",
                                    "ns=1;i=1306",
                                    {"InputArguments": ("V", "ns=1;i=1307", {})},
                                ),
                                "SetPosition": (
                                    "M",
                                    "ns=1;i=1293",
                                    {"InputArguments": ("V", "ns=1;i=1294", {})},
                                ),
                                "Size": ("V", "ns=1;i=1273", {}),
                                "UserWritable": ("V", "ns=1;i=1275", {}),
                                "Writable": ("V", "ns=1;i=1274", {}),
                                "Write": (
                                    "M",
                                    "ns=1;i=1288",
                                    {"InputArguments": ("V", "ns=1;i=1289", {})},
                                ),
                            },
                        ),
                        "UnregisterTickets": (
                            "M",
                            "ns=1;i=1269",
                            {
                                "InputArguments": ("V", "ns=1;i=1270", {}),
                                "OutputArguments": ("V", "ns=1;i=1271", {}),
                            },
                        ),
                    },
                ),
                "GetManagers": (
                    "M",
                    "ns=1;i=1505",
                    {"OutputArguments": ("V", "ns=1;i=1506", {})},
                ),
                "ProvideIdentities": (
                    "M",
                    "ns=1;i=1260",
                    {
                        "InputArguments": ("V", "ns=1;i=1261", {}),
                        "OutputArguments": ("V", "ns=1;i=1262", {}),
                    },
                ),
                "RegisterDeviceEndpoint": (
                    "M",
                    "ns=1;i=1263",
                    {"InputArguments": ("V", "ns=1;i=1264", {})},
                ),
                "RegisterManagedApplication": (
                    "M",
                    "ns=1;i=1507",
                    {
                        "InputArguments": ("V", "ns=1;i=1508", {}),
                        "OutputArguments": ("V", "ns=1;i=1509", {}),
                    },
                ),
                "UpdateSoftwareStatus": (
                    "M",
                    "ns=1;i=1503",
                    {"InputArguments": ("V", "ns=1;i=1504", {})},
                ),
            },
        ),
    },
}
