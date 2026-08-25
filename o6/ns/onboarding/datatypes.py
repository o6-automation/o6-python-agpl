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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(nodeId="ns=onboarding;i=1164", browseName="CertificateAuthorityType", defaultEncodingId="ns=onboarding;i=1439")
class CertificateAuthorityType(ns0.datatypes.Structure):
    authorityCertificate: o6.ByteString
    issuerCertificates: list[o6.ByteString]


@o6.datatype(nodeId="ns=onboarding;i=1165", browseName="BaseTicketType", defaultEncodingId="ns=onboarding;i=1440", isAbstract=True)
class BaseTicketType(ns0.datatypes.Structure):
    manufacturerName: o6.String
    modelName: o6.String
    modelVersion: o6.String
    hardwareRevision: o6.String
    softwareRevision: o6.String
    serialNumber: o6.String
    manufactureDate: o6.DateTime
    authorities: list[CertificateAuthorityType]


@o6.datatype(nodeId="ns=onboarding;i=1166", browseName="DeviceIdentityTicketType", defaultEncodingId="ns=onboarding;i=1441")
class DeviceIdentityTicketType(BaseTicketType):
    manufacturerName: o6.String
    modelName: o6.String
    modelVersion: o6.String
    hardwareRevision: o6.String
    softwareRevision: o6.String
    serialNumber: o6.String
    manufactureDate: o6.DateTime
    authorities: list[CertificateAuthorityType]
    productInstanceUri: o6.String


@o6.datatype(nodeId="ns=onboarding;i=1167", browseName="CompositeIdentityTicketType", defaultEncodingId="ns=onboarding;i=1442")
class CompositeIdentityTicketType(BaseTicketType):
    manufacturerName: o6.String
    modelName: o6.String
    modelVersion: o6.String
    hardwareRevision: o6.String
    softwareRevision: o6.String
    serialNumber: o6.String
    manufactureDate: o6.DateTime
    authorities: list[CertificateAuthorityType]
    compositeInstanceUri: o6.String
    devices: list[o6.String]
    composites: list[o6.String]


@o6.datatype(nodeId="ns=onboarding;i=1168", browseName="TicketListType", defaultEncodingId="ns=onboarding;i=1443")
class TicketListType(ns0.datatypes.Structure):
    devices: list[o6.String]
    composites: list[o6.String]


@o6.datatype(nodeId="ns=onboarding;i=1495", browseName="ManagerDescription", defaultEncodingId="ns=onboarding;i=4206")
class ManagerDescription(ns0.datatypes.Structure):
    name: o6.LocalizedText
    isRequired: o6.Boolean
    purposeUri: o6.String
    protocolUri: o6.String
    endpointUrls: list[o6.String]


del Any, TYPE_CHECKING, uuid, o6, gds, ns0
