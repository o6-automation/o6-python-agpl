# Copyright (c) 2026 o6 Automation GmbH
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""Generated OPC UA gds namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import datatypes as gds_datypes
from . import objtypes as gds_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=gds;i=127", browseName="Default XML")
o6.hasEncoding(gds_datypes.ApplicationRecordDataType, o6.ns["ns=gds;i=127"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=gds;i=131", browseName="ns=gds;ApplicationRecordDataType", dataType=o6.String, value="//xs:element[@name='ApplicationRecordDataType']"
)
o6.reference(o6.ns["ns=gds;i=127"], "i=39", o6.ns["ns=gds;i=131"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=gds;i=134", browseName="Default Binary")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=gds;i=138", browseName="ns=gds;ApplicationRecordDataType", dataType=o6.String, value="ApplicationRecordDataType")
o6.reference(o6.ns["ns=gds;i=134"], "i=39", o6.ns["ns=gds;i=138"])


ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=144",
    browseName="InputArguments",
    parent="ns=gds;i=143",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationUri", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=145",
    browseName="OutputArguments",
    parent="ns=gds;i=143",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Applications", dataType=o6.NodeId("ns=gds;i=1"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=gds;i=143", browseName="ns=gds;FindApplications", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=144"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=145"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=147",
    browseName="InputArguments",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1661": o6.Permission.BROWSE},
    accessRestrictions=1,
    parent="ns=gds;i=146",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Application", dataType=o6.NodeId("ns=gds;i=1"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=148",
    browseName="OutputArguments",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1661": o6.Permission.BROWSE},
    accessRestrictions=1,
    parent="ns=gds;i=146",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=146",
    browseName="ns=gds;RegisterApplication",
    rolePermissions={"i=15644": o6.Permission.BROWSE | o6.Permission.CALL, "ns=1;i=1661": o6.Permission.BROWSE | o6.Permission.CALL},
    accessRestrictions=1,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=147"]),
    outputArgs=o6.hasProperty(o6.ns["ns=gds;i=148"]),
)
o6.reference(o6.ns["ns=gds;i=146"], "i=41", gds_objtypes.ApplicationRegistrationChangedAuditEventType)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=150",
    browseName="InputArguments",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1661": o6.Permission.BROWSE},
    accessRestrictions=1,
    parent="ns=gds;i=149",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=149",
    browseName="ns=gds;UnregisterApplication",
    rolePermissions={"i=15644": o6.Permission.BROWSE | o6.Permission.CALL, "ns=1;i=1661": o6.Permission.BROWSE | o6.Permission.CALL},
    accessRestrictions=1,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=150"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=152",
    browseName="InputArguments",
    parent="ns=gds;i=151",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.Argument(name="StartingRecordId", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="MaxRecordsToReturn", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ApplicationName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ApplicationUri", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ProductUri", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ServerCapabilities", dataType=o6.String, valueRank=1, arrayDimensions=[0]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=153",
    browseName="OutputArguments",
    parent="ns=gds;i=151",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="LastCounterResetTime", dataType=ns0.datatypes.UtcTime, valueRank=-1),
        ns0.datatypes.Argument(name="Servers", dataType=ns0.datatypes.ServerOnNetwork, valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(nodeId="ns=gds;i=151", browseName="ns=gds;QueryServers", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=152"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=153"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=155",
    browseName="InputArguments",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE},
    accessRestrictions=3,
    parent="ns=gds;i=154",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="CertificateGroupId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="CertificateTypeId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="SubjectName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="DomainNames", dataType=o6.String, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="PrivateKeyFormat", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="PrivateKeyPassword", dataType=o6.String, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=156",
    browseName="OutputArguments",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE},
    accessRestrictions=3,
    parent="ns=gds;i=154",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RequestId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=154",
    browseName="ns=gds;StartNewKeyPairRequest",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE | o6.Permission.CALL},
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=155"]),
    outputArgs=o6.hasProperty(o6.ns["ns=gds;i=156"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=158",
    browseName="InputArguments",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE},
    accessRestrictions=1,
    parent="ns=gds;i=157",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="CertificateGroupId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="CertificateTypeId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="CertificateRequest", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=159",
    browseName="OutputArguments",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE},
    accessRestrictions=1,
    parent="ns=gds;i=157",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RequestId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=157",
    browseName="ns=gds;StartSigningRequest",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE | o6.Permission.CALL},
    accessRestrictions=1,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=158"]),
    outputArgs=o6.hasProperty(o6.ns["ns=gds;i=159"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=164",
    browseName="InputArguments",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE},
    accessRestrictions=3,
    parent="ns=gds;i=163",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="RequestId", dataType=o6.NodeId, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=165",
    browseName="OutputArguments",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE},
    accessRestrictions=3,
    parent="ns=gds;i=163",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="Certificate", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="PrivateKey", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="IssuerCertificates", dataType=o6.ByteString, valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(
    nodeId="ns=gds;i=163",
    browseName="ns=gds;FinishRequest",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE | o6.Permission.CALL},
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=164"]),
    outputArgs=o6.hasProperty(o6.ns["ns=gds;i=165"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=171",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=168",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="ApplicationUri", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="PublicKey", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="SecurityPolicyUri", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="RequestedRoles", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=195",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=168",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RequestId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=168", browseName="ns=gds;StartRequest", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=171"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=195"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=175",
    browseName="InputArguments",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE},
    accessRestrictions=1,
    parent="ns=gds;i=174",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="CertificateGroupId", dataType=o6.NodeId, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=176",
    browseName="OutputArguments",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE},
    accessRestrictions=1,
    parent="ns=gds;i=174",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="CertificateTypeIds", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="Certificates", dataType=o6.ByteString, valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(
    nodeId="ns=gds;i=174",
    browseName="ns=gds;GetCertificates",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE | o6.Permission.CALL},
    accessRestrictions=1,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=175"]),
    outputArgs=o6.hasProperty(o6.ns["ns=gds;i=176"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=178",
    browseName="InputArguments",
    parent="ns=gds;i=177",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Certificate", dataType=o6.ByteString, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=179",
    browseName="OutputArguments",
    parent="ns=gds;i=177",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="CertificateStatus", dataType=o6.StatusCode, valueRank=-1),
        ns0.datatypes.Argument(name="ValidityTime", dataType=ns0.datatypes.UtcTime, valueRank=-1),
    ],
)
o6.call(nodeId="ns=gds;i=177", browseName="ns=gds;CheckRevocationStatus", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=178"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=179"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=202",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=196",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="RequestId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="CancelRequest", dataType=o6.Boolean, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=203",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=196",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="CredentialId", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="CredentialSecret", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="CertificateThumbprint", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="SecurityPolicyUri", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="GrantedRoles", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(nodeId="ns=gds;i=196", browseName="ns=gds;FinishRequest", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=202"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=203"]))

gds_objtypes.KeyCredentialServiceType(
    nodeId="ns=gds;i=61",
    browseName="ns=gds;<ServiceName>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=83", browseName="ns=gds;ResourceUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=162", browseName="ns=gds;ProfileUris", dataType=o6.String, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(o6.ns["ns=gds;i=168"]),
        o6.hasComponent(o6.ns["ns=gds;i=196"]),
    ],
)
o6.reference(gds_objtypes.KeyCredentialManagementFolderType, ns0.reftypes.HasComponent, o6.ns["ns=gds;i=61"])


ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=201",
    browseName="InputArguments",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1661": o6.Permission.BROWSE},
    accessRestrictions=1,
    parent="ns=gds;i=200",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Application", dataType=o6.NodeId("ns=gds;i=1"), valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=200",
    browseName="ns=gds;UpdateApplication",
    rolePermissions={"i=15644": o6.Permission.BROWSE | o6.Permission.CALL, "ns=1;i=1661": o6.Permission.BROWSE | o6.Permission.CALL},
    accessRestrictions=1,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=201"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=205",
    browseName="InputArguments",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE},
    accessRestrictions=1,
    parent="ns=gds;i=204",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="CertificateGroupId", dataType=o6.NodeId, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=206",
    browseName="OutputArguments",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE},
    accessRestrictions=1,
    parent="ns=gds;i=204",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TrustListId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=204",
    browseName="ns=gds;GetTrustList",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE | o6.Permission.CALL},
    accessRestrictions=1,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=205"]),
    outputArgs=o6.hasProperty(o6.ns["ns=gds;i=206"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=217",
    browseName="InputArguments",
    parent="ns=gds;i=216",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=218",
    browseName="OutputArguments",
    parent="ns=gds;i=216",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Application", dataType=o6.NodeId("ns=gds;i=1"), valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=216", browseName="ns=gds;GetApplication", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=217"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=218"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=226",
    browseName="InputArguments",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE},
    accessRestrictions=1,
    parent="ns=gds;i=225",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="CertificateGroupId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="CertificateTypeId", dataType=o6.NodeId, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=227",
    browseName="OutputArguments",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE},
    accessRestrictions=1,
    parent="ns=gds;i=225",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="UpdateRequired", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=225",
    browseName="ns=gds;GetCertificateStatus",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE | o6.Permission.CALL},
    accessRestrictions=1,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=226"]),
    outputArgs=o6.hasProperty(o6.ns["ns=gds;i=227"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=239",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=238",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ServiceUri", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ServiceCertificate", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="UserTokenPolicies", dataType=ns0.datatypes.UserTokenPolicy, valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(nodeId="ns=gds;i=238", browseName="ns=gds;GetServiceDescription", outputArgs=o6.hasProperty(o6.ns["ns=gds;i=239"]))

gds_objtypes.AuthorizationServiceType(
    nodeId="ns=gds;i=234",
    browseName="ns=gds;<ServiceName>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=235", browseName="ns=gds;ServiceUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=236", browseName="ns=gds;ServiceCertificate", dataType=o6.ByteString)),
        o6.hasComponent(o6.ns["ns=gds;i=238"]),
    ],
)
o6.reference(gds_objtypes.AuthorizationServicesFolderType, ns0.reftypes.Organizes, o6.ns["ns=gds;i=234"])
o6.reference(o6.ns["ns=gds;i=234"], "i=41", gds_objtypes.AccessTokenRequestedAuditEventType)
o6.reference(o6.ns["ns=gds;i=234"], "i=41", gds_objtypes.AccessTokenIssuedAuditEventType)


ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=509",
    browseName="InputArguments",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE},
    accessRestrictions=1,
    parent="ns=gds;i=508",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=510",
    browseName="OutputArguments",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE},
    accessRestrictions=1,
    parent="ns=gds;i=508",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CertificateGroupIds", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])],
)
o6.call(
    nodeId="ns=gds;i=508",
    browseName="ns=gds;GetCertificateGroups",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE | o6.Permission.CALL},
    accessRestrictions=1,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=509"]),
    outputArgs=o6.hasProperty(o6.ns["ns=gds;i=510"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=520",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=519",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=521",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=519",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=519", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=520"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=521"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=523",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=522",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=522", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=523"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=525",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=524",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=526",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=524",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=524", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=525"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=526"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=528",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=527",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=527", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=528"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=530",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=529",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=531",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=529",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=529", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=530"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=531"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=533",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=532",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=532", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=533"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=536",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=535",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Masks", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=537",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=535",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=535", browseName="OpenWithMasks", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=536"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=537"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=539",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=538",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=540",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=538",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplyChangesRequired", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=538", browseName="CloseAndUpdate", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=539"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=540"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=542",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=541",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Certificate", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="IsTrustedCertificate", dataType=o6.Boolean, valueRank=-1),
    ],
)
o6.call(nodeId="ns=gds;i=541", browseName="AddCertificate", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=542"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=544",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=543",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Thumbprint", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="IsTrustedCertificate", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=543", browseName="RemoveCertificate", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=544"]))

ns0.objtypes.TrustListType(
    nodeId="ns=gds;i=513",
    browseName="TrustList",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=514", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=515", browseName="Writable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=516", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=517", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=534", browseName="LastUpdateTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasComponent(o6.ns["ns=gds;i=519"]),
        o6.hasComponent(o6.ns["ns=gds;i=522"]),
        o6.hasComponent(o6.ns["ns=gds;i=524"]),
        o6.hasComponent(o6.ns["ns=gds;i=527"]),
        o6.hasComponent(o6.ns["ns=gds;i=529"]),
        o6.hasComponent(o6.ns["ns=gds;i=532"]),
        o6.hasComponent(o6.ns["ns=gds;i=535"]),
        o6.hasComponent(o6.ns["ns=gds;i=538"]),
        o6.hasComponent(o6.ns["ns=gds;i=541"]),
        o6.hasComponent(o6.ns["ns=gds;i=543"]),
    ],
)
ns0.objtypes.CertificateGroupType(
    nodeId="ns=gds;i=512",
    browseName="DefaultApplicationGroup",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=545", browseName="CertificateTypes", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(o6.ns["ns=gds;i=513"]),
    ],
)
o6.reference(o6.ns["ns=gds;i=512"], "i=9006", "i=13225")
o6.reference(o6.ns["ns=gds;i=512"], "i=9006", "i=19297")
ns0.objtypes.CertificateGroupFolderType(
    nodeId="ns=gds;i=511", browseName="ns=gds;CertificateGroups", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=gds;i=512"])]
)
o6.reference(gds_objtypes.CertificateDirectoryType, ns0.reftypes.Organizes, o6.ns["ns=gds;i=511"])


ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=623",
    browseName="InputArguments",
    parent="ns=gds;i=622",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=624",
    browseName="OutputArguments",
    parent="ns=gds;i=622",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=622", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=623"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=624"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=626",
    browseName="InputArguments",
    parent="ns=gds;i=625",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=625", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=626"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=628",
    browseName="InputArguments",
    parent="ns=gds;i=627",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=629",
    browseName="OutputArguments",
    parent="ns=gds;i=627",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=627", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=628"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=629"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=631",
    browseName="InputArguments",
    parent="ns=gds;i=630",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=630", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=631"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=633",
    browseName="InputArguments",
    parent="ns=gds;i=632",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=634",
    browseName="OutputArguments",
    parent="ns=gds;i=632",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=632", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=633"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=634"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=636",
    browseName="InputArguments",
    parent="ns=gds;i=635",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=635", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=636"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=639",
    browseName="InputArguments",
    parent="ns=gds;i=638",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Masks", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=640",
    browseName="OutputArguments",
    parent="ns=gds;i=638",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=638", browseName="OpenWithMasks", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=639"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=640"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=642",
    browseName="InputArguments",
    parent="ns=gds;i=641",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=643",
    browseName="OutputArguments",
    parent="ns=gds;i=641",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplyChangesRequired", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=641", browseName="CloseAndUpdate", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=642"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=643"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=645",
    browseName="InputArguments",
    parent="ns=gds;i=644",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Certificate", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="IsTrustedCertificate", dataType=o6.Boolean, valueRank=-1),
    ],
)
o6.call(nodeId="ns=gds;i=644", browseName="AddCertificate", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=645"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=647",
    browseName="InputArguments",
    parent="ns=gds;i=646",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Thumbprint", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="IsTrustedCertificate", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=646", browseName="RemoveCertificate", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=647"]))

ns0.objtypes.TrustListType(
    nodeId="ns=gds;i=616",
    browseName="TrustList",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=617", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=618", browseName="Writable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=619", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=620", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=637", browseName="LastUpdateTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasComponent(o6.ns["ns=gds;i=622"]),
        o6.hasComponent(o6.ns["ns=gds;i=625"]),
        o6.hasComponent(o6.ns["ns=gds;i=627"]),
        o6.hasComponent(o6.ns["ns=gds;i=630"]),
        o6.hasComponent(o6.ns["ns=gds;i=632"]),
        o6.hasComponent(o6.ns["ns=gds;i=635"]),
        o6.hasComponent(o6.ns["ns=gds;i=638"]),
        o6.hasComponent(o6.ns["ns=gds;i=641"]),
        o6.hasComponent(o6.ns["ns=gds;i=644"]),
        o6.hasComponent(o6.ns["ns=gds;i=646"]),
    ],
)
ns0.objtypes.CertificateGroupType(
    nodeId="ns=gds;i=615",
    browseName="DefaultApplicationGroup",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=648", browseName="CertificateTypes", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(o6.ns["ns=gds;i=616"]),
    ],
)
o6.reference(o6.ns["ns=gds;i=615"], "i=9006", "i=13225")
o6.reference(o6.ns["ns=gds;i=615"], "i=9006", "i=19297")


ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=657",
    browseName="InputArguments",
    parent="ns=gds;i=656",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=658",
    browseName="OutputArguments",
    parent="ns=gds;i=656",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=656", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=657"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=658"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=660",
    browseName="InputArguments",
    parent="ns=gds;i=659",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=659", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=660"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=662",
    browseName="InputArguments",
    parent="ns=gds;i=661",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=663",
    browseName="OutputArguments",
    parent="ns=gds;i=661",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=661", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=662"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=663"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=665",
    browseName="InputArguments",
    parent="ns=gds;i=664",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=664", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=665"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=667",
    browseName="InputArguments",
    parent="ns=gds;i=666",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=668",
    browseName="OutputArguments",
    parent="ns=gds;i=666",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=666", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=667"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=668"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=670",
    browseName="InputArguments",
    parent="ns=gds;i=669",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=669", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=670"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=673",
    browseName="InputArguments",
    parent="ns=gds;i=672",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Masks", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=674",
    browseName="OutputArguments",
    parent="ns=gds;i=672",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=672", browseName="OpenWithMasks", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=673"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=674"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=676",
    browseName="InputArguments",
    parent="ns=gds;i=675",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=677",
    browseName="OutputArguments",
    parent="ns=gds;i=675",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplyChangesRequired", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=675", browseName="CloseAndUpdate", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=676"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=677"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=679",
    browseName="InputArguments",
    parent="ns=gds;i=678",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Certificate", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="IsTrustedCertificate", dataType=o6.Boolean, valueRank=-1),
    ],
)
o6.call(nodeId="ns=gds;i=678", browseName="AddCertificate", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=679"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=681",
    browseName="InputArguments",
    parent="ns=gds;i=680",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Thumbprint", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="IsTrustedCertificate", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=680", browseName="RemoveCertificate", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=681"]))

ns0.objtypes.TrustListType(
    nodeId="ns=gds;i=650",
    browseName="TrustList",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=651", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=652", browseName="Writable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=653", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=654", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=671", browseName="LastUpdateTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasComponent(o6.ns["ns=gds;i=656"]),
        o6.hasComponent(o6.ns["ns=gds;i=659"]),
        o6.hasComponent(o6.ns["ns=gds;i=661"]),
        o6.hasComponent(o6.ns["ns=gds;i=664"]),
        o6.hasComponent(o6.ns["ns=gds;i=666"]),
        o6.hasComponent(o6.ns["ns=gds;i=669"]),
        o6.hasComponent(o6.ns["ns=gds;i=672"]),
        o6.hasComponent(o6.ns["ns=gds;i=675"]),
        o6.hasComponent(o6.ns["ns=gds;i=678"]),
        o6.hasComponent(o6.ns["ns=gds;i=680"]),
    ],
)
ns0.objtypes.CertificateGroupType(
    nodeId="ns=gds;i=649",
    browseName="DefaultHttpsGroup",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=682", browseName="CertificateTypes", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(o6.ns["ns=gds;i=650"]),
    ],
)
o6.reference(o6.ns["ns=gds;i=649"], "i=9006", "i=13225")
o6.reference(o6.ns["ns=gds;i=649"], "i=9006", "i=19297")


ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=691",
    browseName="InputArguments",
    parent="ns=gds;i=690",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=692",
    browseName="OutputArguments",
    parent="ns=gds;i=690",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=690", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=691"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=692"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=694",
    browseName="InputArguments",
    parent="ns=gds;i=693",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=693", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=694"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=696",
    browseName="InputArguments",
    parent="ns=gds;i=695",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=697",
    browseName="OutputArguments",
    parent="ns=gds;i=695",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=695", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=696"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=697"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=699",
    browseName="InputArguments",
    parent="ns=gds;i=698",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=698", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=699"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=701",
    browseName="InputArguments",
    parent="ns=gds;i=700",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=702",
    browseName="OutputArguments",
    parent="ns=gds;i=700",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=700", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=701"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=702"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=704",
    browseName="InputArguments",
    parent="ns=gds;i=703",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=703", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=704"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=707",
    browseName="InputArguments",
    parent="ns=gds;i=706",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Masks", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=708",
    browseName="OutputArguments",
    parent="ns=gds;i=706",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=706", browseName="OpenWithMasks", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=707"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=708"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=710",
    browseName="InputArguments",
    parent="ns=gds;i=709",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=711",
    browseName="OutputArguments",
    parent="ns=gds;i=709",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplyChangesRequired", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=709", browseName="CloseAndUpdate", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=710"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=711"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=713",
    browseName="InputArguments",
    parent="ns=gds;i=712",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Certificate", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="IsTrustedCertificate", dataType=o6.Boolean, valueRank=-1),
    ],
)
o6.call(nodeId="ns=gds;i=712", browseName="AddCertificate", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=713"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=715",
    browseName="InputArguments",
    parent="ns=gds;i=714",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Thumbprint", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="IsTrustedCertificate", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=714", browseName="RemoveCertificate", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=715"]))

ns0.objtypes.TrustListType(
    nodeId="ns=gds;i=684",
    browseName="TrustList",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=685", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=686", browseName="Writable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=687", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=688", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=705", browseName="LastUpdateTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasComponent(o6.ns["ns=gds;i=690"]),
        o6.hasComponent(o6.ns["ns=gds;i=693"]),
        o6.hasComponent(o6.ns["ns=gds;i=695"]),
        o6.hasComponent(o6.ns["ns=gds;i=698"]),
        o6.hasComponent(o6.ns["ns=gds;i=700"]),
        o6.hasComponent(o6.ns["ns=gds;i=703"]),
        o6.hasComponent(o6.ns["ns=gds;i=706"]),
        o6.hasComponent(o6.ns["ns=gds;i=709"]),
        o6.hasComponent(o6.ns["ns=gds;i=712"]),
        o6.hasComponent(o6.ns["ns=gds;i=714"]),
    ],
)
ns0.objtypes.CertificateGroupType(
    nodeId="ns=gds;i=683",
    browseName="DefaultUserTokenGroup",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=716", browseName="CertificateTypes", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(o6.ns["ns=gds;i=684"]),
    ],
)
o6.reference(o6.ns["ns=gds;i=683"], "i=9006", "i=13225")
o6.reference(o6.ns["ns=gds;i=683"], "i=9006", "i=19297")
certificateGroups = ns0.objtypes.CertificateGroupFolderType(
    nodeId="ns=gds;i=614",
    browseName="ns=gds;CertificateGroups",
    references=[o6.hasComponent(o6.ns["ns=gds;i=615"]), o6.hasComponent(o6.ns["ns=gds;i=649"]), o6.hasComponent(o6.ns["ns=gds;i=683"])],
)
authorizationServices = gds_objtypes.AuthorizationServicesFolderType(
    nodeId="ns=gds;i=959", browseName="ns=gds;AuthorizationServices", parent="i=85", referenceType=ns0.reftypes.Organizes
)


ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=993",
    browseName="InputArguments",
    parent="ns=gds;i=992",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.Argument(name="StartingRecordId", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="MaxRecordsToReturn", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ApplicationName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ApplicationUri", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ApplicationType", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ProductUri", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Capabilities", dataType=o6.String, valueRank=1, arrayDimensions=[0]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=994",
    browseName="OutputArguments",
    parent="ns=gds;i=992",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="LastCounterResetTime", dataType=ns0.datatypes.UtcTime, valueRank=-1),
        ns0.datatypes.Argument(name="NextRecordId", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="Applications", dataType=ns0.datatypes.ApplicationDescription, valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(nodeId="ns=gds;i=992", browseName="ns=gds;QueryApplications", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=993"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=994"]))

keyCredentialManagement = gds_objtypes.KeyCredentialManagementFolderType(
    nodeId="ns=gds;i=1008", browseName="ns=gds;KeyCredentialManagement", parent="i=85", referenceType=ns0.reftypes.Organizes
)


ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1669",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1668",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Rule", dataType=ns0.datatypes.IdentityMappingRuleType, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1668",
    browseName="AddIdentity",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1669"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1671",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1670",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Rule", dataType=ns0.datatypes.IdentityMappingRuleType, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1670",
    browseName="RemoveIdentity",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1671"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1673",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1672",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationUri", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1672",
    browseName="AddApplication",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1673"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1675",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1674",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationUri", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1674",
    browseName="RemoveApplication",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1675"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1677",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1676",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Endpoint", dataType=ns0.datatypes.EndpointType, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1676",
    browseName="AddEndpoint",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1677"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1679",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1678",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Endpoint", dataType=ns0.datatypes.EndpointType, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1678",
    browseName="RemoveEndpoint",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1679"]),
)

discoveryAdmin = ns0.objtypes.RoleType(
    nodeId="ns=gds;i=1661",
    browseName="ns=gds;DiscoveryAdmin",
    description="This Role grants rights to register, update and unregister any OPC UA Application.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1662",
                browseName="Identities",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=ns0.datatypes.IdentityMappingRuleType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1663",
                browseName="ApplicationsExclude",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1664",
                browseName="Applications",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1665",
                browseName="EndpointsExclude",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1666",
                browseName="Endpoints",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=ns0.datatypes.EndpointType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(o6.ns["ns=gds;i=1668"]),
        o6.hasComponent(o6.ns["ns=gds;i=1670"]),
        o6.hasComponent(o6.ns["ns=gds;i=1672"]),
        o6.hasComponent(o6.ns["ns=gds;i=1674"]),
        o6.hasComponent(o6.ns["ns=gds;i=1676"]),
        o6.hasComponent(o6.ns["ns=gds;i=1678"]),
    ],
    parent="i=15606",
    referenceType=ns0.reftypes.HasComponent,
)


ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1688",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1687",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Rule", dataType=ns0.datatypes.IdentityMappingRuleType, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1687",
    browseName="AddIdentity",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1688"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1690",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1689",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Rule", dataType=ns0.datatypes.IdentityMappingRuleType, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1689",
    browseName="RemoveIdentity",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1690"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1692",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1691",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationUri", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1691",
    browseName="AddApplication",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1692"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1694",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1693",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationUri", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1693",
    browseName="RemoveApplication",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1694"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1696",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1695",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Endpoint", dataType=ns0.datatypes.EndpointType, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1695",
    browseName="AddEndpoint",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1696"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1698",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1697",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Endpoint", dataType=ns0.datatypes.EndpointType, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1697",
    browseName="RemoveEndpoint",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1698"]),
)

certificateAuthorityAdmin = ns0.objtypes.RoleType(
    nodeId="ns=gds;i=1680",
    browseName="ns=gds;CertificateAuthorityAdmin",
    description="This Role grants rights to request or revoke any Certificate, update any TrustList or assign CertificateGroups to OPC UA Applications.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1681",
                browseName="Identities",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=ns0.datatypes.IdentityMappingRuleType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1682",
                browseName="ApplicationsExclude",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1683",
                browseName="Applications",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1684",
                browseName="EndpointsExclude",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1685",
                browseName="Endpoints",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=ns0.datatypes.EndpointType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(o6.ns["ns=gds;i=1687"]),
        o6.hasComponent(o6.ns["ns=gds;i=1689"]),
        o6.hasComponent(o6.ns["ns=gds;i=1691"]),
        o6.hasComponent(o6.ns["ns=gds;i=1693"]),
        o6.hasComponent(o6.ns["ns=gds;i=1695"]),
        o6.hasComponent(o6.ns["ns=gds;i=1697"]),
    ],
    parent="i=15606",
    referenceType=ns0.reftypes.HasComponent,
)


ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1707",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1706",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Rule", dataType=ns0.datatypes.IdentityMappingRuleType, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1706",
    browseName="AddIdentity",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1707"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1709",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1708",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Rule", dataType=ns0.datatypes.IdentityMappingRuleType, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1708",
    browseName="RemoveIdentity",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1709"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1711",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1710",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationUri", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1710",
    browseName="AddApplication",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1711"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1713",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1712",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationUri", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1712",
    browseName="RemoveApplication",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1713"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1715",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1714",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Endpoint", dataType=ns0.datatypes.EndpointType, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1714",
    browseName="AddEndpoint",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1715"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1717",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1716",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Endpoint", dataType=ns0.datatypes.EndpointType, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1716",
    browseName="RemoveEndpoint",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1717"]),
)

registrationAuthorityAdmin = ns0.objtypes.RoleType(
    nodeId="ns=gds;i=1699",
    browseName="ns=gds;RegistrationAuthorityAdmin",
    description="This Role grants rights to approve Certificate Signing requests or NewKeyPair requests.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1700",
                browseName="Identities",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=ns0.datatypes.IdentityMappingRuleType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1701",
                browseName="ApplicationsExclude",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1702",
                browseName="Applications",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1703",
                browseName="EndpointsExclude",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1704",
                browseName="Endpoints",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=ns0.datatypes.EndpointType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(o6.ns["ns=gds;i=1706"]),
        o6.hasComponent(o6.ns["ns=gds;i=1708"]),
        o6.hasComponent(o6.ns["ns=gds;i=1710"]),
        o6.hasComponent(o6.ns["ns=gds;i=1712"]),
        o6.hasComponent(o6.ns["ns=gds;i=1714"]),
        o6.hasComponent(o6.ns["ns=gds;i=1716"]),
    ],
    parent="i=15606",
    referenceType=ns0.reftypes.HasComponent,
)


ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1726",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1725",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Rule", dataType=ns0.datatypes.IdentityMappingRuleType, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1725",
    browseName="AddIdentity",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1726"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1728",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1727",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Rule", dataType=ns0.datatypes.IdentityMappingRuleType, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1727",
    browseName="RemoveIdentity",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1728"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1730",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1729",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationUri", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1729",
    browseName="AddApplication",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1730"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1732",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1731",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationUri", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1731",
    browseName="RemoveApplication",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1732"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1734",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1733",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Endpoint", dataType=ns0.datatypes.EndpointType, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1733",
    browseName="AddEndpoint",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1734"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1736",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1735",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Endpoint", dataType=ns0.datatypes.EndpointType, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1735",
    browseName="RemoveEndpoint",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1736"]),
)

keyCredentialAdmin = ns0.objtypes.RoleType(
    nodeId="ns=gds;i=1718",
    browseName="ns=gds;KeyCredentialAdmin",
    description="This Role grants rights to request or revoke any KeyCredential.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1719",
                browseName="Identities",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=ns0.datatypes.IdentityMappingRuleType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1720",
                browseName="ApplicationsExclude",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1721",
                browseName="Applications",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1722",
                browseName="EndpointsExclude",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1723",
                browseName="Endpoints",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=ns0.datatypes.EndpointType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(o6.ns["ns=gds;i=1725"]),
        o6.hasComponent(o6.ns["ns=gds;i=1727"]),
        o6.hasComponent(o6.ns["ns=gds;i=1729"]),
        o6.hasComponent(o6.ns["ns=gds;i=1731"]),
        o6.hasComponent(o6.ns["ns=gds;i=1733"]),
        o6.hasComponent(o6.ns["ns=gds;i=1735"]),
    ],
    parent="i=15606",
    referenceType=ns0.reftypes.HasComponent,
)


ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1745",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1744",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Rule", dataType=ns0.datatypes.IdentityMappingRuleType, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1744",
    browseName="AddIdentity",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1745"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1747",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1746",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Rule", dataType=ns0.datatypes.IdentityMappingRuleType, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1746",
    browseName="RemoveIdentity",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1747"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1749",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1748",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationUri", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1748",
    browseName="AddApplication",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1749"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1751",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1750",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationUri", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1750",
    browseName="RemoveApplication",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1751"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1753",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1752",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Endpoint", dataType=ns0.datatypes.EndpointType, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1752",
    browseName="AddEndpoint",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1753"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1755",
    browseName="InputArguments",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.WRITE_HISTORIZING
        | o6.Permission.READ
        | o6.Permission.WRITE
        | o6.Permission.READ_HISTORY
        | o6.Permission.INSERT_HISTORY
        | o6.Permission.MODIFY_HISTORY
        | o6.Permission.DELETE_HISTORY
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    parent="ns=gds;i=1754",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Endpoint", dataType=ns0.datatypes.EndpointType, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=1754",
    browseName="RemoveEndpoint",
    rolePermissions={
        "i=15704": o6.Permission.BROWSE
        | o6.Permission.READ_ROLE_PERMISSIONS
        | o6.Permission.WRITE_ATTRIBUTE
        | o6.Permission.WRITE_ROLE_PERMISSIONS
        | o6.Permission.CALL
        | o6.Permission.ADD_REFERENCE
        | o6.Permission.REMOVE_REFERENCE
        | o6.Permission.DELETE_NODE
    },
    accessRestrictions=3,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1755"]),
)

authorizationServiceAdmin = ns0.objtypes.RoleType(
    nodeId="ns=gds;i=1737",
    browseName="ns=gds;AuthorizationServiceAdmin",
    description="This Role grants rights to request or revoke any KeyCredential.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1738",
                browseName="Identities",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=ns0.datatypes.IdentityMappingRuleType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1739",
                browseName="ApplicationsExclude",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1740",
                browseName="Applications",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1741",
                browseName="EndpointsExclude",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=1742",
                browseName="Endpoints",
                rolePermissions={
                    "i=15704": o6.Permission.BROWSE
                    | o6.Permission.READ_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_ATTRIBUTE
                    | o6.Permission.WRITE_ROLE_PERMISSIONS
                    | o6.Permission.WRITE_HISTORIZING
                    | o6.Permission.READ
                    | o6.Permission.WRITE
                    | o6.Permission.READ_HISTORY
                    | o6.Permission.INSERT_HISTORY
                    | o6.Permission.MODIFY_HISTORY
                    | o6.Permission.DELETE_HISTORY
                    | o6.Permission.ADD_REFERENCE
                    | o6.Permission.REMOVE_REFERENCE
                    | o6.Permission.DELETE_NODE
                },
                accessRestrictions=3,
                dataType=ns0.datatypes.EndpointType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(o6.ns["ns=gds;i=1744"]),
        o6.hasComponent(o6.ns["ns=gds;i=1746"]),
        o6.hasComponent(o6.ns["ns=gds;i=1748"]),
        o6.hasComponent(o6.ns["ns=gds;i=1750"]),
        o6.hasComponent(o6.ns["ns=gds;i=1752"]),
        o6.hasComponent(o6.ns["ns=gds;i=1754"]),
    ],
    parent="i=15606",
    referenceType=ns0.reftypes.HasComponent,
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashGDSSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=gds;i=721",
    browseName="ns=gds;http://opcfoundation.org/UA/GDS/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=722", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/GDS/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=723", browseName="NamespaceVersion", dataType=o6.String, value="1.05.07")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=724", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2026-05-01T00:00:00Z"))),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=gds;i=725", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=726", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gds;i=727", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["1:2147483647"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=728", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=gds;i=862", browseName="DefaultRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=gds;i=863", browseName="DefaultUserRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=864", browseName="DefaultAccessRestrictions", dataType=ns0.datatypes.AccessRestrictionType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=1756", browseName="ModelVersion", dataType=ns0.datatypes.SemanticVersionString, value="1.5.7")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=gds;i=8001", browseName="Default JSON")
o6.hasEncoding(gds_datypes.ApplicationRecordDataType, o6.ns["ns=gds;i=8001"])
opcDotUaDotGds_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=gds;i=135",
    browseName="ns=gds;Opc.Ua.Gds",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=137", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/GDS/")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=gds;i=8002", browseName="Deprecated", dataType=o6.Boolean)
        ),
        o6.hasComponent(o6.ns["ns=gds;i=138"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary\r\n  xmlns:opc="http://opcfoundation.org/BinarySchema/"\r\n  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\r\n  xmlns:ua="http://opcfoundation.org/UA/"\r\n  xmlns:tns="http://opcfoundation.org/UA/GDS/"\r\n  DefaultByteOrder="LittleEndian"\r\n  TargetNamespace="http://opcfoundation.org/UA/GDS/"\r\n>\r\n  <opc:Import Namespace="http://opcfoundation.org/UA/" Location="Opc.Ua.BinarySchema.bsd"/>\r\n\r\n  <opc:StructuredType Name="ApplicationRecordDataType" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="ApplicationId" TypeName="ua:NodeId" />\r\n    <opc:Field Name="ApplicationUri" TypeName="opc:String" />\r\n    <opc:Field Name="ApplicationType" TypeName="ua:ApplicationType" />\r\n    <opc:Field Name="NoOfApplicationNames" TypeName="opc:Int32" />\r\n    <opc:Field Name="ApplicationNames" TypeName="ua:LocalizedText" LengthField="NoOfApplicationNames" />\r\n    <opc:Field Name="ProductUri" TypeName="opc:String" />\r\n    <opc:Field Name="NoOfDiscoveryUrls" TypeName="opc:Int32" />\r\n    <opc:Field Name="DiscoveryUrls" TypeName="opc:String" LengthField="NoOfDiscoveryUrls" />\r\n    <opc:Field Name="NoOfServerCapabilities" TypeName="opc:Int32" />\r\n    <opc:Field Name="ServerCapabilities" TypeName="opc:String" LengthField="NoOfServerCapabilities" />\r\n  </opc:StructuredType>\r\n\r\n</opc:TypeDictionary>',
)
opcDotUaDotGds = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=gds;i=128",
    browseName="ns=gds;Opc.Ua.Gds",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=130", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/GDS/Types.xsd")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=gds;i=8004", browseName="Deprecated", dataType=o6.Boolean)
        ),
        o6.hasComponent(o6.ns["ns=gds;i=131"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema\r\n  xmlns:xs="http://www.w3.org/2001/XMLSchema"\r\n  xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd"\r\n  xmlns:tns="http://opcfoundation.org/UA/GDS/Types.xsd"\r\n  targetNamespace="http://opcfoundation.org/UA/GDS/Types.xsd"\r\n  elementFormDefault="qualified"\r\n>\r\n  <xs:annotation>\r\n    <xs:appinfo>\r\n      <ua:Model ModelUri="http://opcfoundation.org/UA/GDS/" Version="1.05.07" PublicationDate="2026-05-01T00:00:00Z" />\r\n    </xs:appinfo>\r\n  </xs:annotation>\r\n  \r\n  <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd" />\r\n\r\n  <xs:complexType name="ApplicationRecordDataType">\r\n    <xs:sequence>\r\n      <xs:element name="ApplicationId" type="ua:NodeId" minOccurs="0" nillable="true" />\r\n      <xs:element name="ApplicationUri" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="ApplicationType" type="ua:ApplicationType" minOccurs="0" />\r\n      <xs:element name="ApplicationNames" type="ua:ListOfLocalizedText" minOccurs="0" nillable="true" />\r\n      <xs:element name="ProductUri" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="DiscoveryUrls" type="ua:ListOfString" minOccurs="0" nillable="true" />\r\n      <xs:element name="ServerCapabilities" type="ua:ListOfString" minOccurs="0" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ApplicationRecordDataType" type="tns:ApplicationRecordDataType" />\r\n\r\n  <xs:complexType name="ListOfApplicationRecordDataType">\r\n    <xs:sequence>\r\n      <xs:element name="ApplicationRecordDataType" type="tns:ApplicationRecordDataType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfApplicationRecordDataType" type="tns:ListOfApplicationRecordDataType" nillable="true"></xs:element>\r\n\r\n</xs:schema>',
)


ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=15006",
    browseName="InputArguments",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE},
    accessRestrictions=1,
    parent="ns=gds;i=15005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="Certificate", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(
    nodeId="ns=gds;i=15005",
    browseName="ns=gds;RevokeCertificate",
    rolePermissions={"i=15644": o6.Permission.BROWSE, "ns=1;i=1680": o6.Permission.BROWSE | o6.Permission.CALL},
    accessRestrictions=1,
    inputArgs=o6.hasProperty(o6.ns["ns=gds;i=15006"]),
)

directory = gds_objtypes.CertificateDirectoryType(
    nodeId="ns=gds;i=141",
    browseName="ns=gds;Directory",
    references=[
        o6.organizes(certificateGroups),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=gds;i=142", browseName="ns=gds;Applications")),
        o6.hasComponent(o6.ns["ns=gds;i=143"]),
        o6.hasComponent(o6.ns["ns=gds;i=146"]),
        o6.hasComponent(o6.ns["ns=gds;i=149"]),
        o6.hasComponent(o6.ns["ns=gds;i=151"]),
        o6.hasComponent(o6.ns["ns=gds;i=154"]),
        o6.hasComponent(o6.ns["ns=gds;i=157"]),
        o6.hasComponent(o6.ns["ns=gds;i=163"]),
        o6.hasComponent(o6.ns["ns=gds;i=174"]),
        o6.hasComponent(o6.ns["ns=gds;i=177"]),
        o6.hasComponent(o6.ns["ns=gds;i=200"]),
        o6.hasComponent(o6.ns["ns=gds;i=204"]),
        o6.hasComponent(o6.ns["ns=gds;i=216"]),
        o6.hasComponent(o6.ns["ns=gds;i=225"]),
        o6.hasComponent(o6.ns["ns=gds;i=508"]),
        o6.hasComponent(o6.ns["ns=gds;i=992"]),
        o6.hasComponent(o6.ns["ns=gds;i=15005"]),
    ],
    parent="i=85",
    referenceType=ns0.reftypes.Organizes,
)


del Any, TYPE_CHECKING, uuid, o6, ns0, gds_datypes, gds_objtypes
