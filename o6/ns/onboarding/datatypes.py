# Copyright (c) 2026 o6 Automation GmbH
#
# SPDX-License-Identifier: AGPL-3.0-or-later
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


@o6.datatype(nodeId="ns=onboarding;i=1164", browseName="ns=onboarding;CertificateAuthorityType", defaultEncodingId="ns=onboarding;i=1439")
class CertificateAuthorityType(ns0.datatypes.Structure):
    authorityCertificate: o6.ByteString = o6.field(name="AuthorityCertificate")
    issuerCertificates: list[o6.ByteString] = o6.field(name="IssuerCertificates")


@o6.datatype(nodeId="ns=onboarding;i=1165", browseName="ns=onboarding;BaseTicketType", defaultEncodingId="ns=onboarding;i=1440", isAbstract=True)
class BaseTicketType(ns0.datatypes.Structure):
    manufacturerName: o6.String = o6.field(name="ManufacturerName")
    modelName: o6.String = o6.field(name="ModelName")
    modelVersion: o6.String = o6.field(name="ModelVersion")
    hardwareRevision: o6.String = o6.field(name="HardwareRevision")
    softwareRevision: o6.String = o6.field(name="SoftwareRevision")
    serialNumber: o6.String = o6.field(name="SerialNumber")
    manufactureDate: o6.DateTime = o6.field(name="ManufactureDate")
    authorities: list[CertificateAuthorityType] = o6.field(name="Authorities")


@o6.datatype(nodeId="ns=onboarding;i=1166", browseName="ns=onboarding;DeviceIdentityTicketType", defaultEncodingId="ns=onboarding;i=1441")
class DeviceIdentityTicketType(BaseTicketType):
    manufacturerName: o6.String = o6.field(name="ManufacturerName")
    modelName: o6.String = o6.field(name="ModelName")
    modelVersion: o6.String = o6.field(name="ModelVersion")
    hardwareRevision: o6.String = o6.field(name="HardwareRevision")
    softwareRevision: o6.String = o6.field(name="SoftwareRevision")
    serialNumber: o6.String = o6.field(name="SerialNumber")
    manufactureDate: o6.DateTime = o6.field(name="ManufactureDate")
    authorities: list[CertificateAuthorityType] = o6.field(name="Authorities")
    productInstanceUri: o6.String = o6.field(name="ProductInstanceUri")


@o6.datatype(nodeId="ns=onboarding;i=1167", browseName="ns=onboarding;CompositeIdentityTicketType", defaultEncodingId="ns=onboarding;i=1442")
class CompositeIdentityTicketType(BaseTicketType):
    manufacturerName: o6.String = o6.field(name="ManufacturerName")
    modelName: o6.String = o6.field(name="ModelName")
    modelVersion: o6.String = o6.field(name="ModelVersion")
    hardwareRevision: o6.String = o6.field(name="HardwareRevision")
    softwareRevision: o6.String = o6.field(name="SoftwareRevision")
    serialNumber: o6.String = o6.field(name="SerialNumber")
    manufactureDate: o6.DateTime = o6.field(name="ManufactureDate")
    authorities: list[CertificateAuthorityType] = o6.field(name="Authorities")
    compositeInstanceUri: o6.String = o6.field(name="CompositeInstanceUri")
    devices: list[o6.String] = o6.field(name="Devices")
    composites: list[o6.String] = o6.field(name="Composites")


@o6.datatype(nodeId="ns=onboarding;i=1168", browseName="ns=onboarding;TicketListType", defaultEncodingId="ns=onboarding;i=1443")
class TicketListType(ns0.datatypes.Structure):
    devices: list[o6.String] = o6.field(name="Devices")
    composites: list[o6.String] = o6.field(name="Composites")


@o6.datatype(nodeId="ns=onboarding;i=1495", browseName="ns=onboarding;ManagerDescription", defaultEncodingId="ns=onboarding;i=4206")
class ManagerDescription(ns0.datatypes.Structure):
    name: o6.LocalizedText = o6.field(name="Name")
    isRequired: o6.Boolean = o6.field(name="IsRequired")
    purposeUri: o6.String = o6.field(name="PurposeUri")
    protocolUri: o6.String = o6.field(name="ProtocolUri")
    endpointUrls: list[o6.String] = o6.field(name="EndpointUrls")


del Any, TYPE_CHECKING, uuid, o6, gds, ns0
