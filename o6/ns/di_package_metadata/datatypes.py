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

"""Generated OPC UA di_package_metadata namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=di_package_metadata;i=5", browseName="PackageType")
class PackageType(ns0.datatypes.Enumeration):
    FIRMWARE = o6.enumfield(0, name="Firmware")
    APPLICATION = o6.enumfield(1, name="Application")
    CONFIGURATION = o6.enumfield(2, name="Configuration")
    SOLUTION = o6.enumfield(3, name="Solution")


@o6.enumtype(nodeId="ns=di_package_metadata;i=7", browseName="FileType")
class FileType(ns0.datatypes.Enumeration):
    DEPLOYMENT_ITEM = o6.enumfield(0, name="DeploymentItem")
    RELEASE_NOTES = o6.enumfield(1, name="ReleaseNotes")
    LICENSE_INFO = o6.enumfield(2, name="LicenseInfo")
    PRE_INSTALL_NOTE = o6.enumfield(3, name="PreInstallNote")


@o6.datatype(nodeId="ns=di_package_metadata;i=2", browseName="FileDescriptor", defaultEncodingId="ns=di_package_metadata;i=15")
class FileDescriptor(ns0.datatypes.Structure):
    fileType: FileType
    fileName: o6.String
    mimeType: o6.String | None
    language: o6.String | None


@o6.enumtype(nodeId="ns=di_package_metadata;i=9", browseName="ComparisonOperation")
class ComparisonOperation(ns0.datatypes.Enumeration):
    EQUAL_TO = o6.enumfield(0, name="EqualTo")
    GREATER_THAN = o6.enumfield(1, name="GreaterThan")
    GREATER_EQUAL = o6.enumfield(2, name="GreaterEqual")
    LESS_THEN = o6.enumfield(3, name="LessThen")
    LESS_EQUAL = o6.enumfield(4, name="LessEqual")
    REGULAR_EXPRESSION = o6.enumfield(5, name="RegularExpression")
    ONE_OF = o6.enumfield(6, name="OneOf")
    EXIST = o6.enumfield(7, name="Exist")


@o6.datatype(nodeId="ns=di_package_metadata;i=4", browseName="CompatibilityRequirement", defaultEncodingId="ns=di_package_metadata;i=17")
class CompatibilityRequirement(ns0.datatypes.Structure):
    variable: o6.String
    values: list[Any]
    operation: ComparisonOperation


@o6.datatype(nodeId="ns=di_package_metadata;i=3", browseName="CompatibilityOption", defaultEncodingId="ns=di_package_metadata;i=16")
class CompatibilityOption(ns0.datatypes.Structure):
    compatibilityRequirements: list[CompatibilityRequirement]


@o6.datatype(nodeId="ns=di_package_metadata;i=13", browseName="FxPathElement", defaultEncodingId="ns=di_package_metadata;i=20")
class FxPathElement(ns0.datatypes.Structure):
    assetConnectorType: o6.NodeId
    connectorId: o6.UInt16 | None
    connectorName: o6.String | None


@o6.datatype(nodeId="ns=di_package_metadata;i=12", browseName="PackageTarget", defaultEncodingId="ns=di_package_metadata;i=19")
class PackageTarget(ns0.datatypes.Structure):
    targetType: o6.NodeId | None
    targetNode: o6.NodeId | None
    productInstanceUri: o6.String | None
    assetId: o6.String | None
    manufacturerUri: o6.String | None
    productCode: o6.String | None
    serialNumber: o6.String | None
    fxPath: list[FxPathElement] | None
    fxScope: list[FxPathElement] | None
    browsePath: list[ns0.datatypes.RelativePathElement] | None
    targetServer: o6.String | None


@o6.datatype(nodeId="ns=di_package_metadata;i=239", browseName="UpdateTarget", defaultEncodingId="ns=di_package_metadata;i=240")
class UpdateTarget(ns0.datatypes.Structure):
    productCode: o6.String
    model: o6.String


@o6.datatype(nodeId="ns=di_package_metadata;i=255", browseName="Assignment", defaultEncodingId="ns=di_package_metadata;i=256")
class Assignment(ns0.datatypes.Structure):
    subpackage: o6.String
    installationOrder: o6.UInt32 | None
    targets: list[PackageTarget]


@o6.datatype(nodeId="ns=di_package_metadata;i=1", browseName="PackageMetadata", defaultEncodingId="ns=di_package_metadata;i=14")
class PackageMetadata(ns0.datatypes.Structure):
    name: o6.String
    description: o6.String | None
    manufacturerUri: o6.String
    manufacturer: o6.String
    packageRevision: o6.String
    packageType: PackageType
    softwareSubClass: o6.String | None
    deployCompletePackage: o6.Boolean | None
    softwareRevision: o6.String | None
    releaseDate: o6.DateTime | None
    targetManufacturerUri: o6.String | None
    targetManufacturer: o6.String | None
    updateTargets: list[UpdateTarget] | None
    files: list[FileDescriptor] | None
    compatibilities: list[CompatibilityOption] | None
    assignments: list[Assignment] | None


del Any, TYPE_CHECKING, uuid, o6, ns0
