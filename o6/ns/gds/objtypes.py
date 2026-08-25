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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=16",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=15",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationUri", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=17",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=15",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Applications", dataType=o6.NodeId("ns=gds;i=1"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=gds;i=15", browseName="ns=gds;FindApplications", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=16"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=17"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=19",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=18",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Application", dataType=o6.NodeId("ns=gds;i=1"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=20",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=18",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=18", browseName="ns=gds;RegisterApplication", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=19"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=20"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=22",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=21",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=21", browseName="ns=gds;UnregisterApplication", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=22"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=24",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=23",
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
    nodeId="ns=gds;i=25",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=23",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="LastCounterResetTime", dataType=ns0.datatypes.UtcTime, valueRank=-1),
        ns0.datatypes.Argument(name="Servers", dataType=ns0.datatypes.ServerOnNetwork, valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(nodeId="ns=gds;i=23", browseName="ns=gds;QueryServers", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=24"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=25"]))


@o6.objecttype(
    nodeId="ns=gds;i=26",
    browseName="ns=gds;ApplicationRegistrationChangedAuditEventType",
    displayName="ApplicationRegistrationChangedAuditEventType",
    rolePermissions={
        "i=15644": ns0.datatypes.PermissionType.BROWSE | ns0.datatypes.PermissionType.READ,
        "i=15704": ns0.datatypes.PermissionType.BROWSE | ns0.datatypes.PermissionType.READ | ns0.datatypes.PermissionType.RECEIVE_EVENTS,
    },
    isAbstract=True,
)
class ApplicationRegistrationChangedAuditEventType(ns0.objtypes.AuditUpdateMethodEventType):
    pass


o6.reference(o6.ns["ns=gds;i=18"], "i=41", ApplicationRegistrationChangedAuditEventType)


@o6.objecttype(
    nodeId="ns=gds;i=27",
    browseName="ns=gds;CertificateRevokedAuditEventType",
    displayName="CertificateRevokedAuditEventType",
    rolePermissions={
        "i=15644": ns0.datatypes.PermissionType.BROWSE | ns0.datatypes.PermissionType.READ,
        "i=15704": ns0.datatypes.PermissionType.BROWSE | ns0.datatypes.PermissionType.READ | ns0.datatypes.PermissionType.RECEIVE_EVENTS,
    },
    isAbstract=True,
)
class CertificateRevokedAuditEventType(ns0.objtypes.AuditUpdateMethodEventType):
    pass


@o6.objecttype(nodeId="ns=gds;i=55", browseName="ns=gds;KeyCredentialManagementFolderType", displayName="KeyCredentialManagementFolderType")
class KeyCredentialManagementFolderType(ns0.objtypes.FolderType):
    langleServiceNameRangle: KeyCredentialServiceType | None


ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=65",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=64",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ResourceId", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="CurrentRefreshToken", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=66",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=64",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="AccessToken", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="AccessTokenExpiryTime", dataType=o6.DateTime, valueRank=-1),
        ns0.datatypes.Argument(name="NewRefreshToken", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="NewRefreshTokenExpiryTime", dataType=o6.DateTime, valueRank=-1),
    ],
)
o6.call(nodeId="ns=gds;i=64", browseName="ns=gds;RefreshToken", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=65"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=66"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=77",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=76",
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
    nodeId="ns=gds;i=78",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=76",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RequestId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=76", browseName="ns=gds;StartNewKeyPairRequest", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=77"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=78"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=80",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=79",
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
    nodeId="ns=gds;i=81",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=79",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RequestId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=79", browseName="ns=gds;StartSigningRequest", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=80"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=81"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=86",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=85",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="RequestId", dataType=o6.NodeId, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=87",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=85",
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
o6.call(nodeId="ns=gds;i=85", browseName="ns=gds;FinishRequest", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=86"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=87"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=90",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=89",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="CertificateGroupId", dataType=o6.NodeId, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=108",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=89",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="CertificateTypeIds", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="Certificates", dataType=o6.ByteString, valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(nodeId="ns=gds;i=89", browseName="ns=gds;GetCertificates", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=90"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=108"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=96",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=95",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ResourceId", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="PolicyId", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="RequestorData", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=97",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=95",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ServiceData", dataType=o6.ByteString, valueRank=-1), ns0.datatypes.Argument(name="RequestId", dataType=o6.Guid, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=95", browseName="ns=gds;StartRequestToken", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=96"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=97"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=99",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=98",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="RequestId", dataType=o6.Guid, valueRank=-1),
        ns0.datatypes.Argument(name="RequestedRoles", dataType=o6.String, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="UserIdentityToken", dataType=ns0.datatypes.UserIdentityToken, valueRank=-1),
        ns0.datatypes.Argument(name="UserTokenSignature", dataType=ns0.datatypes.SignatureData, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=100",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=98",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="AccessToken", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="AccessTokenExpiryTime", dataType=o6.DateTime, valueRank=-1),
        ns0.datatypes.Argument(name="RefreshToken", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="RefreshTokenExpiryTime", dataType=o6.DateTime, valueRank=-1),
    ],
)
o6.call(nodeId="ns=gds;i=98", browseName="ns=gds;FinishRequestToken", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=99"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=100"]))


@o6.objecttype(
    nodeId="ns=gds;i=111",
    browseName="ns=gds;AccessTokenRequestedAuditEventType",
    displayName="AccessTokenRequestedAuditEventType",
    rolePermissions={
        "i=15644": ns0.datatypes.PermissionType.BROWSE | ns0.datatypes.PermissionType.READ,
        "i=15704": ns0.datatypes.PermissionType.BROWSE | ns0.datatypes.PermissionType.READ | ns0.datatypes.PermissionType.RECEIVE_EVENTS,
    },
    isAbstract=True,
)
class AccessTokenRequestedAuditEventType(ns0.objtypes.AuditUpdateMethodEventType):
    pass


ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=160",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=126",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Certificate", dataType=o6.ByteString, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=161",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=126",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="CertificateStatus", dataType=o6.StatusCode, valueRank=-1),
        ns0.datatypes.Argument(name="ValidityTime", dataType=ns0.datatypes.UtcTime, valueRank=-1),
    ],
)
o6.call(nodeId="ns=gds;i=126", browseName="ns=gds;CheckRevocationStatus", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=160"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=161"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=189",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=188",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Application", dataType=o6.NodeId("ns=gds;i=1"), valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=188", browseName="ns=gds;UpdateApplication", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=189"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=198",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=197",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="CertificateGroupId", dataType=o6.NodeId, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=199",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=197",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TrustListId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=197", browseName="ns=gds;GetTrustList", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=198"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=199"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=211",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=210",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=212",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=210",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Application", dataType=o6.NodeId("ns=gds;i=1"), valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=210", browseName="ns=gds;GetApplication", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=211"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=212"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=223",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=222",
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
    nodeId="ns=gds;i=224",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=222",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="UpdateRequired", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=222", browseName="ns=gds;GetCertificateStatus", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=223"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=224"]))


@o6.objecttype(nodeId="ns=gds;i=233", browseName="ns=gds;AuthorizationServicesFolderType", displayName="AuthorizationServicesFolderType")
class AuthorizationServicesFolderType(ns0.objtypes.FolderType):
    langleServiceNameRangle: AuthorizationServiceType | None


ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=370",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=369",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=371",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=369",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CertificateGroupIds", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=gds;i=369", browseName="ns=gds;GetCertificateGroups", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=370"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=371"]))


@o6.objecttype(
    nodeId="ns=gds;i=91",
    browseName="ns=gds;CertificateRequestedAuditEventType",
    displayName="CertificateRequestedAuditEventType",
    rolePermissions={
        "i=15644": ns0.datatypes.PermissionType.BROWSE | ns0.datatypes.PermissionType.READ,
        "i=15704": ns0.datatypes.PermissionType.BROWSE | ns0.datatypes.PermissionType.READ | ns0.datatypes.PermissionType.RECEIVE_EVENTS,
    },
    isAbstract=True,
)
class CertificateRequestedAuditEventType(ns0.objtypes.AuditUpdateMethodEventType):
    certificateGroup: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=717", browseName="ns=gds;CertificateGroup", dataType=o6.NodeId))
    certificateType: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=718", browseName="ns=gds;CertificateType", dataType=o6.NodeId))


@o6.objecttype(
    nodeId="ns=gds;i=109",
    browseName="ns=gds;CertificateDeliveredAuditEventType",
    displayName="CertificateDeliveredAuditEventType",
    rolePermissions={
        "i=15644": ns0.datatypes.PermissionType.BROWSE | ns0.datatypes.PermissionType.READ,
        "i=15704": ns0.datatypes.PermissionType.BROWSE | ns0.datatypes.PermissionType.READ | ns0.datatypes.PermissionType.RECEIVE_EVENTS,
    },
    isAbstract=True,
)
class CertificateDeliveredAuditEventType(ns0.objtypes.AuditUpdateMethodEventType):
    certificateGroup: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=719", browseName="ns=gds;CertificateGroup", dataType=o6.NodeId))
    certificateType: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=720", browseName="ns=gds;CertificateType", dataType=o6.NodeId))


ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=869",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=868",
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
    nodeId="ns=gds;i=870",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=868",
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
o6.call(nodeId="ns=gds;i=868", browseName="ns=gds;QueryApplications", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=869"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=870"]))


@o6.objecttype(nodeId="ns=gds;i=13", browseName="ns=gds;DirectoryType", displayName="DirectoryType")
class DirectoryType(ns0.objtypes.FolderType):
    applications: ns0.objtypes.FolderType = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=gds;i=14", browseName="ns=gds;Applications"))
    findApplications: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=gds;i=15"])
    getApplication: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=gds;i=210"])
    queryApplications: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=gds;i=868"])
    queryServers: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=gds;i=23"])
    registerApplication: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=gds;i=18"])
    unregisterApplication: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=gds;i=21"])
    updateApplication: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=gds;i=188"])


ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=970",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=969",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="IdentityToken", dataType=ns0.datatypes.UserIdentityToken, valueRank=-1),
        ns0.datatypes.Argument(name="ResourceId", dataType=o6.String, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=971",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=969",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AccessToken", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=969", browseName="ns=gds;RequestAccessToken", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=970"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=971"]))


@o6.objecttype(
    nodeId="ns=gds;i=975",
    browseName="ns=gds;AccessTokenIssuedAuditEventType",
    displayName="AccessTokenIssuedAuditEventType",
    rolePermissions={
        "i=15644": ns0.datatypes.PermissionType.BROWSE | ns0.datatypes.PermissionType.READ,
        "i=15704": ns0.datatypes.PermissionType.BROWSE | ns0.datatypes.PermissionType.READ | ns0.datatypes.PermissionType.RECEIVE_EVENTS,
    },
    isAbstract=True,
)
class AccessTokenIssuedAuditEventType(ns0.objtypes.AuditUpdateMethodEventType):
    pass


ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1005",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=1004",
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
o6.call(nodeId="ns=gds;i=1004", browseName="ns=gds;GetServiceDescription", outputArgs=o6.hasProperty(o6.ns["ns=gds;i=1005"]))


@o6.objecttype(nodeId="ns=gds;i=966", browseName="ns=gds;AuthorizationServiceType", displayName="AuthorizationServiceType")
class AuthorizationServiceType(ns0.objtypes.BaseObjectType):
    finishRequestToken: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=gds;i=98"])
    getServiceDescription: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=gds;i=1004"])
    refreshToken: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=gds;i=64"])
    requestAccessToken: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=gds;i=969"])
    serviceCertificate: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=968", browseName="ns=gds;ServiceCertificate", dataType=o6.ByteString))
    serviceUri: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=1003", browseName="ns=gds;ServiceUri", dataType=o6.String))
    startRequestToken: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=gds;i=95"])
    supportedRoles: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gds;i=110", browseName="ns=gds;SupportedRoles", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    userTokenPolicies: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gds;i=967", browseName="ns=gds;UserTokenPolicies", dataType=ns0.datatypes.UserTokenPolicy, valueRank=1, arrayDimensions=[0])
    )


o6.reference(AuthorizationServiceType, "i=41", AccessTokenRequestedAuditEventType)
o6.reference(AuthorizationServiceType, "i=41", AccessTokenIssuedAuditEventType)


ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1024",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=1023",
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
    nodeId="ns=gds;i=1025",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=1023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RequestId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=1023", browseName="ns=gds;StartRequest", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1024"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=1025"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1027",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=1026",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="RequestId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="CancelRequest", dataType=o6.Boolean, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1028",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=1026",
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
o6.call(nodeId="ns=gds;i=1026", browseName="ns=gds;FinishRequest", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1027"]), outputArgs=o6.hasProperty(o6.ns["ns=gds;i=1028"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=1030",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=1029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CredentialId", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=1029", browseName="ns=gds;Revoke", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=1030"]))


@o6.objecttype(nodeId="ns=gds;i=1020", browseName="ns=gds;KeyCredentialServiceType", displayName="KeyCredentialServiceType")
class KeyCredentialServiceType(ns0.objtypes.BaseObjectType):
    finishRequest: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=gds;i=1026"])
    profileUris: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gds;i=1022", browseName="ns=gds;ProfileUris", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    resourceUri: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gds;i=1021", browseName="ns=gds;ResourceUri", dataType=o6.String))
    revoke: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=gds;i=1029"])
    securityPolicyUris: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gds;i=495", browseName="ns=gds;SecurityPolicyUris", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    startRequest: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=gds;i=1023"])


@o6.objecttype(
    nodeId="ns=gds;i=1039",
    browseName="ns=gds;KeyCredentialRequestedAuditEventType",
    displayName="KeyCredentialRequestedAuditEventType",
    rolePermissions={
        "i=15644": ns0.datatypes.PermissionType.BROWSE | ns0.datatypes.PermissionType.READ,
        "i=15704": ns0.datatypes.PermissionType.BROWSE | ns0.datatypes.PermissionType.READ | ns0.datatypes.PermissionType.RECEIVE_EVENTS,
    },
)
class KeyCredentialRequestedAuditEventType(ns0.objtypes.KeyCredentialAuditEventType):
    pass


@o6.objecttype(
    nodeId="ns=gds;i=1057",
    browseName="ns=gds;KeyCredentialDeliveredAuditEventType",
    displayName="KeyCredentialDeliveredAuditEventType",
    rolePermissions={
        "i=15644": ns0.datatypes.PermissionType.BROWSE | ns0.datatypes.PermissionType.READ,
        "i=15704": ns0.datatypes.PermissionType.BROWSE | ns0.datatypes.PermissionType.READ | ns0.datatypes.PermissionType.RECEIVE_EVENTS,
    },
)
class KeyCredentialDeliveredAuditEventType(ns0.objtypes.KeyCredentialAuditEventType):
    pass


@o6.objecttype(
    nodeId="ns=gds;i=1075",
    browseName="ns=gds;KeyCredentialRevokedAuditEventType",
    displayName="KeyCredentialRevokedAuditEventType",
    rolePermissions={
        "i=15644": ns0.datatypes.PermissionType.BROWSE | ns0.datatypes.PermissionType.READ,
        "i=15704": ns0.datatypes.PermissionType.BROWSE | ns0.datatypes.PermissionType.READ | ns0.datatypes.PermissionType.RECEIVE_EVENTS,
    },
)
class KeyCredentialRevokedAuditEventType(ns0.objtypes.KeyCredentialAuditEventType):
    pass


ns0.vartypes.PropertyType(
    nodeId="ns=gds;i=15004",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gds;i=15003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="Certificate", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=gds;i=15003", browseName="ns=gds;RevokeCertificate", inputArgs=o6.hasProperty(o6.ns["ns=gds;i=15004"]))


@o6.objecttype(nodeId="ns=gds;i=63", browseName="ns=gds;CertificateDirectoryType", displayName="CertificateDirectoryType")
class CertificateDirectoryType(DirectoryType):
    certificateGroups: ns0.objtypes.CertificateGroupFolderType
    checkRevocationStatus: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=gds;i=126"])
    finishRequest: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=gds;i=85"])
    getCertificateGroups: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=gds;i=369"])
    getCertificateStatus: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=gds;i=222"])
    getCertificates: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=gds;i=89"])
    getTrustList: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=gds;i=197"])
    revokeCertificate: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=gds;i=15003"])
    startNewKeyPairRequest: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=gds;i=76"])
    startSigningRequest: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=gds;i=79"])


del Any, TYPE_CHECKING, uuid, o6, ns0, gds_datypes
