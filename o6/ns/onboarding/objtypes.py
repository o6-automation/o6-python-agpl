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

"""Generated OPC UA onboarding namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.gds as gds
import o6.ns.ns0 as ns0
from . import datatypes as onboarding_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1177",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1176",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Tickets", dataType=ns0.datatypes.EncodedTicket, valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1178",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1176",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Results", dataType=o6.StatusCode, valueRank=1, arrayDimensions=[0])],
)
o6.call(
    nodeId="ns=onboarding;i=1176",
    browseName="ns=onboarding;RegisterTickets",
    inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1177"]),
    outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1178"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1180",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1179",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Tickets", dataType=ns0.datatypes.EncodedTicket, valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1181",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1179",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Results", dataType=o6.StatusCode, valueRank=1, arrayDimensions=[0])],
)
o6.call(
    nodeId="ns=onboarding;i=1179",
    browseName="ns=onboarding;UnregisterTickets",
    inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1180"]),
    outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1181"]),
)


@o6.objecttype(nodeId="ns=onboarding;i=1175", browseName="ns=onboarding;DeviceRegistrarAdminType", displayName="DeviceRegistrarAdminType")
class DeviceRegistrarAdminType(ns0.objtypes.BaseObjectType):
    deviceIdentityAuthorities: ns0.objtypes.TrustListType
    registerTickets: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=onboarding;i=1176"])
    ticketAuthorities: ns0.objtypes.TrustListType
    unregisterTickets: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=onboarding;i=1179"])


ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1261",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1260",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="Identities", dataType=o6.ByteString, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="Issuers", dataType=o6.ByteString, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="Tickets", dataType=ns0.datatypes.EncodedTicket, valueRank=1, arrayDimensions=[0]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1262",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1260",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="SelectedIdentity", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="MatchingTicket", dataType=o6.NodeId("ns=onboarding;i=1165"), valueRank=-1),
        ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="SoftwareUpdateManager", dataType=o6.NodeId("ns=onboarding;i=1495"), valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=onboarding;i=1260",
    browseName="ns=onboarding;ProvideIdentities",
    inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1261"]),
    outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1262"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1264",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1263",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Application", dataType=ns0.datatypes.ApplicationDescription, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1263", browseName="ns=onboarding;RegisterDeviceEndpoint", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1264"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1504",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1503",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ProductInstanceUri", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Status", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="SoftwareRevision", dataType=o6.String, valueRank=-1),
    ],
)
o6.call(nodeId="ns=onboarding;i=1503", browseName="ns=onboarding;UpdateSoftwareStatus", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1504"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1506",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1505",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Managers", dataType=o6.NodeId("ns=onboarding;i=1495"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=onboarding;i=1505", browseName="ns=onboarding;GetManagers", outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1506"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1508",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1507",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Application", dataType=o6.NodeId("ns=gds;i=1"), valueRank=-1),
        ns0.datatypes.Argument(name="ProtocolUri", dataType=ns0.datatypes.UriString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1509",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1507",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=onboarding;i=1507",
    browseName="ns=onboarding;RegisterManagedApplication",
    inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1508"]),
    outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1509"]),
)


@o6.objecttype(nodeId="ns=onboarding;i=1259", browseName="ns=onboarding;DeviceRegistrarType", displayName="DeviceRegistrarType")
class DeviceRegistrarType(ns0.objtypes.BaseObjectType):
    administration: DeviceRegistrarAdminType | None
    getManagers: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=onboarding;i=1505"])
    provideIdentities: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=onboarding;i=1260"])
    registerDeviceEndpoint: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=onboarding;i=1263"])
    registerManagedApplication: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=onboarding;i=1507"])
    updateSoftwareStatus: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=onboarding;i=1503"])


@o6.objecttype(nodeId="ns=onboarding;i=1517", browseName="ns=onboarding;DeviceRegistrationAuditEventType", displayName="DeviceRegistrationAuditEventType", isAbstract=True)
class DeviceRegistrationAuditEventType(ns0.objtypes.AuditEventType):
    productInstanceUri: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1532", browseName="ns=onboarding;ProductInstanceUri", dataType=ns0.datatypes.UriString)
    )


@o6.objecttype(nodeId="ns=onboarding;i=1533", browseName="ns=onboarding;DeviceIdentityAcceptedAuditEventType", displayName="DeviceIdentityAcceptedAuditEventType", isAbstract=True)
class DeviceIdentityAcceptedAuditEventType(DeviceRegistrationAuditEventType):
    certificate: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1549", browseName="ns=onboarding;Certificate", dataType=o6.ByteString)
    )
    composite: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1551", browseName="ns=onboarding;Composite", dataType=ns0.datatypes.EncodedTicket)
    )
    ticket: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1550", browseName="ns=onboarding;Ticket", dataType=ns0.datatypes.EncodedTicket)
    )


@o6.objecttype(nodeId="ns=onboarding;i=1552", browseName="ns=onboarding;DeviceSoftwareUpdatedAuditEventType", displayName="DeviceSoftwareUpdatedAuditEventType", isAbstract=True)
class DeviceSoftwareUpdatedAuditEventType(DeviceRegistrationAuditEventType):
    softwareRevision: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1568", browseName="ns=onboarding;SoftwareRevision", dataType=o6.String)
    )
    status: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1563", browseName="ns=onboarding;Status", dataType=o6.Boolean))


del Any, TYPE_CHECKING, uuid, o6, gds, ns0, onboarding_datypes
