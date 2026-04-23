# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 743b36a8bdffec11f51cd34012bf3acc8ad3df90a7bdb42b5c3309a56732a75f
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/GDS/"
_VERSION: str = "1.05.06"
_REQUIRED: list = [{"uri": "http://opcfoundation.org/UA/", "version": "1.05.06"}]
_STRUCTURES: list = [
    (
        "ns=1;i=1",
        "ApplicationRecordDataType",
        "ns=1;i=134",
        {
            "structure_type": 0,
            "fields": [
                {"name": "ApplicationId", "data_type": "i=17", "value_rank": -1},
                {"name": "ApplicationUri", "data_type": "i=12", "value_rank": -1},
                {"name": "ApplicationType", "data_type": "i=307", "value_rank": -1},
                {"name": "ApplicationNames", "data_type": "i=21", "value_rank": 1},
                {"name": "ProductUri", "data_type": "i=12", "value_rank": -1},
                {"name": "DiscoveryUrls", "data_type": "i=12", "value_rank": 1},
                {"name": "ServerCapabilities", "data_type": "i=12", "value_rank": 1},
            ],
        },
    )
]
_ENUMS: list = []
_ORIGINAL_NODEIDS: tuple = (
    [
        (
            "ns=1;i=1",
            "ns=1;i=134",
            ["i=17", "i=12", "i=307", "i=21", "i=12", "i=12", "i=12"],
        )
    ],
    [],
)
_NODES: dict = {
    "datatypes": {"ApplicationRecordDataType": ("D", "ns=1;i=1", {})},
    "eventtypes": {
        "AccessTokenIssuedAuditEventType": ("OT", "ns=1;i=975", {}),
        "ApplicationRegistrationChangedAuditEventType": ("OT", "ns=1;i=26", {}),
        "CertificateDeliveredAuditEventType": (
            "OT",
            "ns=1;i=109",
            {
                "CertificateGroup": ("V", "ns=1;i=719", {}),
                "CertificateType": ("V", "ns=1;i=720", {}),
            },
        ),
        "CertificateRequestedAuditEventType": (
            "OT",
            "ns=1;i=91",
            {
                "CertificateGroup": ("V", "ns=1;i=717", {}),
                "CertificateType": ("V", "ns=1;i=718", {}),
            },
        ),
        "CertificateRevokedAuditEventType": ("OT", "ns=1;i=27", {}),
        "KeyCredentialDeliveredAuditEventType": ("OT", "ns=1;i=1057", {}),
        "KeyCredentialRequestedAuditEventType": ("OT", "ns=1;i=1039", {}),
        "KeyCredentialRevokedAuditEventType": ("OT", "ns=1;i=1075", {}),
    },
    "objects": {
        "AuthorizationServiceAdmin": (
            "O",
            "ns=1;i=1737",
            {
                "AddApplication": (
                    "M",
                    "ns=1;i=1748",
                    {"InputArguments": ("V", "ns=1;i=1749", {})},
                ),
                "AddEndpoint": (
                    "M",
                    "ns=1;i=1752",
                    {"InputArguments": ("V", "ns=1;i=1753", {})},
                ),
                "AddIdentity": (
                    "M",
                    "ns=1;i=1744",
                    {"InputArguments": ("V", "ns=1;i=1745", {})},
                ),
                "Applications": ("V", "ns=1;i=1740", {}),
                "ApplicationsExclude": ("V", "ns=1;i=1739", {}),
                "Endpoints": ("V", "ns=1;i=1742", {}),
                "EndpointsExclude": ("V", "ns=1;i=1741", {}),
                "Identities": ("V", "ns=1;i=1738", {}),
                "RemoveApplication": (
                    "M",
                    "ns=1;i=1750",
                    {"InputArguments": ("V", "ns=1;i=1751", {})},
                ),
                "RemoveEndpoint": (
                    "M",
                    "ns=1;i=1754",
                    {"InputArguments": ("V", "ns=1;i=1755", {})},
                ),
                "RemoveIdentity": (
                    "M",
                    "ns=1;i=1746",
                    {"InputArguments": ("V", "ns=1;i=1747", {})},
                ),
            },
        ),
        "AuthorizationServices": ("O", "ns=1;i=959", {}),
        "CertificateAuthorityAdmin": (
            "O",
            "ns=1;i=1680",
            {
                "AddApplication": (
                    "M",
                    "ns=1;i=1691",
                    {"InputArguments": ("V", "ns=1;i=1692", {})},
                ),
                "AddEndpoint": (
                    "M",
                    "ns=1;i=1695",
                    {"InputArguments": ("V", "ns=1;i=1696", {})},
                ),
                "AddIdentity": (
                    "M",
                    "ns=1;i=1687",
                    {"InputArguments": ("V", "ns=1;i=1688", {})},
                ),
                "Applications": ("V", "ns=1;i=1683", {}),
                "ApplicationsExclude": ("V", "ns=1;i=1682", {}),
                "Endpoints": ("V", "ns=1;i=1685", {}),
                "EndpointsExclude": ("V", "ns=1;i=1684", {}),
                "Identities": ("V", "ns=1;i=1681", {}),
                "RemoveApplication": (
                    "M",
                    "ns=1;i=1693",
                    {"InputArguments": ("V", "ns=1;i=1694", {})},
                ),
                "RemoveEndpoint": (
                    "M",
                    "ns=1;i=1697",
                    {"InputArguments": ("V", "ns=1;i=1698", {})},
                ),
                "RemoveIdentity": (
                    "M",
                    "ns=1;i=1689",
                    {"InputArguments": ("V", "ns=1;i=1690", {})},
                ),
            },
        ),
        "Default Binary": ("O", "ns=1;i=134", {}),
        "Default JSON": ("O", "ns=1;i=8001", {}),
        "Default XML": ("O", "ns=1;i=127", {}),
        "Directory": (
            "O",
            "ns=1;i=141",
            {
                "Applications": ("O", "ns=1;i=142", {}),
                "CertificateGroups": (
                    "O",
                    "ns=1;i=614",
                    {
                        "DefaultApplicationGroup": (
                            "O",
                            "ns=1;i=615",
                            {
                                "CertificateTypes": ("V", "ns=1;i=648", {}),
                                "TrustList": (
                                    "O",
                                    "ns=1;i=616",
                                    {
                                        "AddCertificate": (
                                            "M",
                                            "ns=1;i=644",
                                            {"InputArguments": ("V", "ns=1;i=645", {})},
                                        ),
                                        "Close": (
                                            "M",
                                            "ns=1;i=625",
                                            {"InputArguments": ("V", "ns=1;i=626", {})},
                                        ),
                                        "CloseAndUpdate": (
                                            "M",
                                            "ns=1;i=641",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=642",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=643",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "GetPosition": (
                                            "M",
                                            "ns=1;i=632",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=633",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=634",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "LastUpdateTime": ("V", "ns=1;i=637", {}),
                                        "Open": (
                                            "M",
                                            "ns=1;i=622",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=623",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=624",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "OpenCount": ("V", "ns=1;i=620", {}),
                                        "OpenWithMasks": (
                                            "M",
                                            "ns=1;i=638",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=639",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=640",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Read": (
                                            "M",
                                            "ns=1;i=627",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=628",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=629",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "RemoveCertificate": (
                                            "M",
                                            "ns=1;i=646",
                                            {"InputArguments": ("V", "ns=1;i=647", {})},
                                        ),
                                        "SetPosition": (
                                            "M",
                                            "ns=1;i=635",
                                            {"InputArguments": ("V", "ns=1;i=636", {})},
                                        ),
                                        "Size": ("V", "ns=1;i=617", {}),
                                        "UserWritable": ("V", "ns=1;i=619", {}),
                                        "Writable": ("V", "ns=1;i=618", {}),
                                        "Write": (
                                            "M",
                                            "ns=1;i=630",
                                            {"InputArguments": ("V", "ns=1;i=631", {})},
                                        ),
                                    },
                                ),
                            },
                        ),
                        "DefaultHttpsGroup": (
                            "O",
                            "ns=1;i=649",
                            {
                                "CertificateTypes": ("V", "ns=1;i=682", {}),
                                "TrustList": (
                                    "O",
                                    "ns=1;i=650",
                                    {
                                        "AddCertificate": (
                                            "M",
                                            "ns=1;i=678",
                                            {"InputArguments": ("V", "ns=1;i=679", {})},
                                        ),
                                        "Close": (
                                            "M",
                                            "ns=1;i=659",
                                            {"InputArguments": ("V", "ns=1;i=660", {})},
                                        ),
                                        "CloseAndUpdate": (
                                            "M",
                                            "ns=1;i=675",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=676",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=677",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "GetPosition": (
                                            "M",
                                            "ns=1;i=666",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=667",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=668",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "LastUpdateTime": ("V", "ns=1;i=671", {}),
                                        "Open": (
                                            "M",
                                            "ns=1;i=656",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=657",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=658",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "OpenCount": ("V", "ns=1;i=654", {}),
                                        "OpenWithMasks": (
                                            "M",
                                            "ns=1;i=672",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=673",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=674",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Read": (
                                            "M",
                                            "ns=1;i=661",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=662",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=663",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "RemoveCertificate": (
                                            "M",
                                            "ns=1;i=680",
                                            {"InputArguments": ("V", "ns=1;i=681", {})},
                                        ),
                                        "SetPosition": (
                                            "M",
                                            "ns=1;i=669",
                                            {"InputArguments": ("V", "ns=1;i=670", {})},
                                        ),
                                        "Size": ("V", "ns=1;i=651", {}),
                                        "UserWritable": ("V", "ns=1;i=653", {}),
                                        "Writable": ("V", "ns=1;i=652", {}),
                                        "Write": (
                                            "M",
                                            "ns=1;i=664",
                                            {"InputArguments": ("V", "ns=1;i=665", {})},
                                        ),
                                    },
                                ),
                            },
                        ),
                        "DefaultUserTokenGroup": (
                            "O",
                            "ns=1;i=683",
                            {
                                "CertificateTypes": ("V", "ns=1;i=716", {}),
                                "TrustList": (
                                    "O",
                                    "ns=1;i=684",
                                    {
                                        "AddCertificate": (
                                            "M",
                                            "ns=1;i=712",
                                            {"InputArguments": ("V", "ns=1;i=713", {})},
                                        ),
                                        "Close": (
                                            "M",
                                            "ns=1;i=693",
                                            {"InputArguments": ("V", "ns=1;i=694", {})},
                                        ),
                                        "CloseAndUpdate": (
                                            "M",
                                            "ns=1;i=709",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=710",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=711",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "GetPosition": (
                                            "M",
                                            "ns=1;i=700",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=701",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=702",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "LastUpdateTime": ("V", "ns=1;i=705", {}),
                                        "Open": (
                                            "M",
                                            "ns=1;i=690",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=691",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=692",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "OpenCount": ("V", "ns=1;i=688", {}),
                                        "OpenWithMasks": (
                                            "M",
                                            "ns=1;i=706",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=707",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=708",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Read": (
                                            "M",
                                            "ns=1;i=695",
                                            {
                                                "InputArguments": (
                                                    "V",
                                                    "ns=1;i=696",
                                                    {},
                                                ),
                                                "OutputArguments": (
                                                    "V",
                                                    "ns=1;i=697",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "RemoveCertificate": (
                                            "M",
                                            "ns=1;i=714",
                                            {"InputArguments": ("V", "ns=1;i=715", {})},
                                        ),
                                        "SetPosition": (
                                            "M",
                                            "ns=1;i=703",
                                            {"InputArguments": ("V", "ns=1;i=704", {})},
                                        ),
                                        "Size": ("V", "ns=1;i=685", {}),
                                        "UserWritable": ("V", "ns=1;i=687", {}),
                                        "Writable": ("V", "ns=1;i=686", {}),
                                        "Write": (
                                            "M",
                                            "ns=1;i=698",
                                            {"InputArguments": ("V", "ns=1;i=699", {})},
                                        ),
                                    },
                                ),
                            },
                        ),
                    },
                ),
                "FindApplications": (
                    "M",
                    "ns=1;i=143",
                    {
                        "InputArguments": ("V", "ns=1;i=144", {}),
                        "OutputArguments": ("V", "ns=1;i=145", {}),
                    },
                ),
                "FinishRequest": (
                    "M",
                    "ns=1;i=163",
                    {
                        "InputArguments": ("V", "ns=1;i=164", {}),
                        "OutputArguments": ("V", "ns=1;i=165", {}),
                    },
                ),
                "GetApplication": (
                    "M",
                    "ns=1;i=216",
                    {
                        "InputArguments": ("V", "ns=1;i=217", {}),
                        "OutputArguments": ("V", "ns=1;i=218", {}),
                    },
                ),
                "GetCertificateGroups": (
                    "M",
                    "ns=1;i=508",
                    {
                        "InputArguments": ("V", "ns=1;i=509", {}),
                        "OutputArguments": ("V", "ns=1;i=510", {}),
                    },
                ),
                "GetCertificateStatus": (
                    "M",
                    "ns=1;i=225",
                    {
                        "InputArguments": ("V", "ns=1;i=226", {}),
                        "OutputArguments": ("V", "ns=1;i=227", {}),
                    },
                ),
                "GetTrustList": (
                    "M",
                    "ns=1;i=204",
                    {
                        "InputArguments": ("V", "ns=1;i=205", {}),
                        "OutputArguments": ("V", "ns=1;i=206", {}),
                    },
                ),
                "QueryApplications": (
                    "M",
                    "ns=1;i=992",
                    {
                        "InputArguments": ("V", "ns=1;i=993", {}),
                        "OutputArguments": ("V", "ns=1;i=994", {}),
                    },
                ),
                "QueryServers": (
                    "M",
                    "ns=1;i=151",
                    {
                        "InputArguments": ("V", "ns=1;i=152", {}),
                        "OutputArguments": ("V", "ns=1;i=153", {}),
                    },
                ),
                "RegisterApplication": (
                    "M",
                    "ns=1;i=146",
                    {
                        "InputArguments": ("V", "ns=1;i=147", {}),
                        "OutputArguments": ("V", "ns=1;i=148", {}),
                    },
                ),
                "StartNewKeyPairRequest": (
                    "M",
                    "ns=1;i=154",
                    {
                        "InputArguments": ("V", "ns=1;i=155", {}),
                        "OutputArguments": ("V", "ns=1;i=156", {}),
                    },
                ),
                "StartSigningRequest": (
                    "M",
                    "ns=1;i=157",
                    {
                        "InputArguments": ("V", "ns=1;i=158", {}),
                        "OutputArguments": ("V", "ns=1;i=159", {}),
                    },
                ),
                "UnregisterApplication": (
                    "M",
                    "ns=1;i=149",
                    {"InputArguments": ("V", "ns=1;i=150", {})},
                ),
                "UpdateApplication": (
                    "M",
                    "ns=1;i=200",
                    {"InputArguments": ("V", "ns=1;i=201", {})},
                ),
            },
        ),
        "DiscoveryAdmin": (
            "O",
            "ns=1;i=1661",
            {
                "AddApplication": (
                    "M",
                    "ns=1;i=1672",
                    {"InputArguments": ("V", "ns=1;i=1673", {})},
                ),
                "AddEndpoint": (
                    "M",
                    "ns=1;i=1676",
                    {"InputArguments": ("V", "ns=1;i=1677", {})},
                ),
                "AddIdentity": (
                    "M",
                    "ns=1;i=1668",
                    {"InputArguments": ("V", "ns=1;i=1669", {})},
                ),
                "Applications": ("V", "ns=1;i=1664", {}),
                "ApplicationsExclude": ("V", "ns=1;i=1663", {}),
                "Endpoints": ("V", "ns=1;i=1666", {}),
                "EndpointsExclude": ("V", "ns=1;i=1665", {}),
                "Identities": ("V", "ns=1;i=1662", {}),
                "RemoveApplication": (
                    "M",
                    "ns=1;i=1674",
                    {"InputArguments": ("V", "ns=1;i=1675", {})},
                ),
                "RemoveEndpoint": (
                    "M",
                    "ns=1;i=1678",
                    {"InputArguments": ("V", "ns=1;i=1679", {})},
                ),
                "RemoveIdentity": (
                    "M",
                    "ns=1;i=1670",
                    {"InputArguments": ("V", "ns=1;i=1671", {})},
                ),
            },
        ),
        "KeyCredentialAdmin": (
            "O",
            "ns=1;i=1718",
            {
                "AddApplication": (
                    "M",
                    "ns=1;i=1729",
                    {"InputArguments": ("V", "ns=1;i=1730", {})},
                ),
                "AddEndpoint": (
                    "M",
                    "ns=1;i=1733",
                    {"InputArguments": ("V", "ns=1;i=1734", {})},
                ),
                "AddIdentity": (
                    "M",
                    "ns=1;i=1725",
                    {"InputArguments": ("V", "ns=1;i=1726", {})},
                ),
                "Applications": ("V", "ns=1;i=1721", {}),
                "ApplicationsExclude": ("V", "ns=1;i=1720", {}),
                "Endpoints": ("V", "ns=1;i=1723", {}),
                "EndpointsExclude": ("V", "ns=1;i=1722", {}),
                "Identities": ("V", "ns=1;i=1719", {}),
                "RemoveApplication": (
                    "M",
                    "ns=1;i=1731",
                    {"InputArguments": ("V", "ns=1;i=1732", {})},
                ),
                "RemoveEndpoint": (
                    "M",
                    "ns=1;i=1735",
                    {"InputArguments": ("V", "ns=1;i=1736", {})},
                ),
                "RemoveIdentity": (
                    "M",
                    "ns=1;i=1727",
                    {"InputArguments": ("V", "ns=1;i=1728", {})},
                ),
            },
        ),
        "KeyCredentialManagement": ("O", "ns=1;i=1008", {}),
        "Opc.Ua.Gds": (
            "V",
            "ns=1;i=128",
            {
                "ApplicationRecordDataType": ("V", "ns=1;i=131", {}),
                "Deprecated": ("V", "ns=1;i=8004", {}),
                "NamespaceUri": ("V", "ns=1;i=130", {}),
            },
        ),
        "RegistrationAuthorityAdmin": (
            "O",
            "ns=1;i=1699",
            {
                "AddApplication": (
                    "M",
                    "ns=1;i=1710",
                    {"InputArguments": ("V", "ns=1;i=1711", {})},
                ),
                "AddEndpoint": (
                    "M",
                    "ns=1;i=1714",
                    {"InputArguments": ("V", "ns=1;i=1715", {})},
                ),
                "AddIdentity": (
                    "M",
                    "ns=1;i=1706",
                    {"InputArguments": ("V", "ns=1;i=1707", {})},
                ),
                "Applications": ("V", "ns=1;i=1702", {}),
                "ApplicationsExclude": ("V", "ns=1;i=1701", {}),
                "Endpoints": ("V", "ns=1;i=1704", {}),
                "EndpointsExclude": ("V", "ns=1;i=1703", {}),
                "Identities": ("V", "ns=1;i=1700", {}),
                "RemoveApplication": (
                    "M",
                    "ns=1;i=1712",
                    {"InputArguments": ("V", "ns=1;i=1713", {})},
                ),
                "RemoveEndpoint": (
                    "M",
                    "ns=1;i=1716",
                    {"InputArguments": ("V", "ns=1;i=1717", {})},
                ),
                "RemoveIdentity": (
                    "M",
                    "ns=1;i=1708",
                    {"InputArguments": ("V", "ns=1;i=1709", {})},
                ),
            },
        ),
        "http://opcfoundation.org/UA/GDS/": (
            "O",
            "ns=1;i=721",
            {
                "DefaultAccessRestrictions": ("V", "ns=1;i=864", {}),
                "DefaultRolePermissions": ("V", "ns=1;i=862", {}),
                "DefaultUserRolePermissions": ("V", "ns=1;i=863", {}),
                "IsNamespaceSubset": ("V", "ns=1;i=725", {}),
                "ModelVersion": ("V", "ns=1;i=1756", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=724", {}),
                "NamespaceUri": ("V", "ns=1;i=722", {}),
                "NamespaceVersion": ("V", "ns=1;i=723", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=726", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=727", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=728", {}),
            },
        ),
    },
    "objtypes": {
        "AuthorizationServiceType": (
            "OT",
            "ns=1;i=966",
            {
                "GetServiceDescription": (
                    "M",
                    "ns=1;i=1004",
                    {"OutputArguments": ("V", "ns=1;i=1005", {})},
                ),
                "RequestAccessToken": (
                    "M",
                    "ns=1;i=969",
                    {
                        "InputArguments": ("V", "ns=1;i=970", {}),
                        "OutputArguments": ("V", "ns=1;i=971", {}),
                    },
                ),
                "ServiceCertificate": ("V", "ns=1;i=968", {}),
                "ServiceUri": ("V", "ns=1;i=1003", {}),
                "UserTokenPolicies": ("V", "ns=1;i=967", {}),
            },
        ),
        "AuthorizationServicesFolderType": (
            "OT",
            "ns=1;i=233",
            {
                "<ServiceName>": (
                    "O",
                    "ns=1;i=234",
                    {
                        "GetServiceDescription": (
                            "M",
                            "ns=1;i=238",
                            {"OutputArguments": ("V", "ns=1;i=239", {})},
                        ),
                        "ServiceCertificate": ("V", "ns=1;i=236", {}),
                        "ServiceUri": ("V", "ns=1;i=235", {}),
                    },
                )
            },
        ),
        "DirectoryType": (
            "OT",
            "ns=1;i=13",
            {
                "Applications": ("O", "ns=1;i=14", {}),
                "CertificateDirectoryType": (
                    "OT",
                    "ns=1;i=63",
                    {
                        "CertificateGroups": (
                            "O",
                            "ns=1;i=511",
                            {
                                "DefaultApplicationGroup": (
                                    "O",
                                    "ns=1;i=512",
                                    {
                                        "CertificateTypes": ("V", "ns=1;i=545", {}),
                                        "TrustList": (
                                            "O",
                                            "ns=1;i=513",
                                            {
                                                "AddCertificate": (
                                                    "M",
                                                    "ns=1;i=541",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=1;i=542",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "Close": (
                                                    "M",
                                                    "ns=1;i=522",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=1;i=523",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "CloseAndUpdate": (
                                                    "M",
                                                    "ns=1;i=538",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=1;i=539",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "ns=1;i=540",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "GetPosition": (
                                                    "M",
                                                    "ns=1;i=529",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=1;i=530",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "ns=1;i=531",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "LastUpdateTime": (
                                                    "V",
                                                    "ns=1;i=534",
                                                    {},
                                                ),
                                                "Open": (
                                                    "M",
                                                    "ns=1;i=519",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=1;i=520",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "ns=1;i=521",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "OpenCount": ("V", "ns=1;i=517", {}),
                                                "OpenWithMasks": (
                                                    "M",
                                                    "ns=1;i=535",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=1;i=536",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "ns=1;i=537",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "Read": (
                                                    "M",
                                                    "ns=1;i=524",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=1;i=525",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "ns=1;i=526",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "RemoveCertificate": (
                                                    "M",
                                                    "ns=1;i=543",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=1;i=544",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "SetPosition": (
                                                    "M",
                                                    "ns=1;i=532",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=1;i=533",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "Size": ("V", "ns=1;i=514", {}),
                                                "UserWritable": ("V", "ns=1;i=516", {}),
                                                "Writable": ("V", "ns=1;i=515", {}),
                                                "Write": (
                                                    "M",
                                                    "ns=1;i=527",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "ns=1;i=528",
                                                            {},
                                                        )
                                                    },
                                                ),
                                            },
                                        ),
                                    },
                                )
                            },
                        ),
                        "CheckRevocationStatus": (
                            "M",
                            "ns=1;i=126",
                            {
                                "InputArguments": ("V", "ns=1;i=160", {}),
                                "OutputArguments": ("V", "ns=1;i=161", {}),
                            },
                        ),
                        "FinishRequest": (
                            "M",
                            "ns=1;i=85",
                            {
                                "InputArguments": ("V", "ns=1;i=86", {}),
                                "OutputArguments": ("V", "ns=1;i=87", {}),
                            },
                        ),
                        "GetCertificateGroups": (
                            "M",
                            "ns=1;i=369",
                            {
                                "InputArguments": ("V", "ns=1;i=370", {}),
                                "OutputArguments": ("V", "ns=1;i=371", {}),
                            },
                        ),
                        "GetCertificateStatus": (
                            "M",
                            "ns=1;i=222",
                            {
                                "InputArguments": ("V", "ns=1;i=223", {}),
                                "OutputArguments": ("V", "ns=1;i=224", {}),
                            },
                        ),
                        "GetCertificates": (
                            "M",
                            "ns=1;i=89",
                            {
                                "InputArguments": ("V", "ns=1;i=90", {}),
                                "OutputArguments": ("V", "ns=1;i=108", {}),
                            },
                        ),
                        "GetTrustList": (
                            "M",
                            "ns=1;i=197",
                            {
                                "InputArguments": ("V", "ns=1;i=198", {}),
                                "OutputArguments": ("V", "ns=1;i=199", {}),
                            },
                        ),
                        "RevokeCertificate": (
                            "M",
                            "ns=1;i=15003",
                            {"InputArguments": ("V", "ns=1;i=15004", {})},
                        ),
                        "StartNewKeyPairRequest": (
                            "M",
                            "ns=1;i=76",
                            {
                                "InputArguments": ("V", "ns=1;i=77", {}),
                                "OutputArguments": ("V", "ns=1;i=78", {}),
                            },
                        ),
                        "StartSigningRequest": (
                            "M",
                            "ns=1;i=79",
                            {
                                "InputArguments": ("V", "ns=1;i=80", {}),
                                "OutputArguments": ("V", "ns=1;i=81", {}),
                            },
                        ),
                    },
                ),
                "FindApplications": (
                    "M",
                    "ns=1;i=15",
                    {
                        "InputArguments": ("V", "ns=1;i=16", {}),
                        "OutputArguments": ("V", "ns=1;i=17", {}),
                    },
                ),
                "GetApplication": (
                    "M",
                    "ns=1;i=210",
                    {
                        "InputArguments": ("V", "ns=1;i=211", {}),
                        "OutputArguments": ("V", "ns=1;i=212", {}),
                    },
                ),
                "QueryApplications": (
                    "M",
                    "ns=1;i=868",
                    {
                        "InputArguments": ("V", "ns=1;i=869", {}),
                        "OutputArguments": ("V", "ns=1;i=870", {}),
                    },
                ),
                "QueryServers": (
                    "M",
                    "ns=1;i=23",
                    {
                        "InputArguments": ("V", "ns=1;i=24", {}),
                        "OutputArguments": ("V", "ns=1;i=25", {}),
                    },
                ),
                "RegisterApplication": (
                    "M",
                    "ns=1;i=18",
                    {
                        "InputArguments": ("V", "ns=1;i=19", {}),
                        "OutputArguments": ("V", "ns=1;i=20", {}),
                    },
                ),
                "UnregisterApplication": (
                    "M",
                    "ns=1;i=21",
                    {"InputArguments": ("V", "ns=1;i=22", {})},
                ),
                "UpdateApplication": (
                    "M",
                    "ns=1;i=188",
                    {"InputArguments": ("V", "ns=1;i=189", {})},
                ),
            },
        ),
        "KeyCredentialManagementFolderType": (
            "OT",
            "ns=1;i=55",
            {
                "<ServiceName>": (
                    "O",
                    "ns=1;i=61",
                    {
                        "FinishRequest": (
                            "M",
                            "ns=1;i=196",
                            {
                                "InputArguments": ("V", "ns=1;i=202", {}),
                                "OutputArguments": ("V", "ns=1;i=203", {}),
                            },
                        ),
                        "ProfileUris": ("V", "ns=1;i=162", {}),
                        "ResourceUri": ("V", "ns=1;i=83", {}),
                        "StartRequest": (
                            "M",
                            "ns=1;i=168",
                            {
                                "InputArguments": ("V", "ns=1;i=171", {}),
                                "OutputArguments": ("V", "ns=1;i=195", {}),
                            },
                        ),
                    },
                )
            },
        ),
        "KeyCredentialServiceType": (
            "OT",
            "ns=1;i=1020",
            {
                "FinishRequest": (
                    "M",
                    "ns=1;i=1026",
                    {
                        "InputArguments": ("V", "ns=1;i=1027", {}),
                        "OutputArguments": ("V", "ns=1;i=1028", {}),
                    },
                ),
                "ProfileUris": ("V", "ns=1;i=1022", {}),
                "ResourceUri": ("V", "ns=1;i=1021", {}),
                "Revoke": (
                    "M",
                    "ns=1;i=1029",
                    {"InputArguments": ("V", "ns=1;i=1030", {})},
                ),
                "SecurityPolicyUris": ("V", "ns=1;i=495", {}),
                "StartRequest": (
                    "M",
                    "ns=1;i=1023",
                    {
                        "InputArguments": ("V", "ns=1;i=1024", {}),
                        "OutputArguments": ("V", "ns=1;i=1025", {}),
                    },
                ),
            },
        ),
    },
}
