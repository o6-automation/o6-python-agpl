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


@o6.enumtype(nodeId="ns=di_package_metadata;i=5", browseName="ns=di_package_metadata;PackageType")
class PackageType(ns0.datatypes.Enumeration):
    FIRMWARE = o6.enumfield(0, name="Firmware")
    APPLICATION = o6.enumfield(1, name="Application")
    CONFIGURATION = o6.enumfield(2, name="Configuration")
    SOLUTION = o6.enumfield(3, name="Solution")


@o6.enumtype(nodeId="ns=di_package_metadata;i=7", browseName="ns=di_package_metadata;FileType")
class FileType(ns0.datatypes.Enumeration):
    DEPLOYMENT_ITEM = o6.enumfield(0, name="DeploymentItem")
    RELEASE_NOTES = o6.enumfield(1, name="ReleaseNotes")
    LICENSE_INFO = o6.enumfield(2, name="LicenseInfo")
    PRE_INSTALL_NOTE = o6.enumfield(3, name="PreInstallNote")


@o6.datatype(nodeId="ns=di_package_metadata;i=2", browseName="ns=di_package_metadata;FileDescriptor", defaultEncodingId="ns=di_package_metadata;i=15")
class FileDescriptor(ns0.datatypes.Structure):
    fileType: FileType = o6.field(name="FileType")
    fileName: o6.String = o6.field(name="FileName")
    mimeType: o6.String | None = o6.field(name="MimeType")
    language: o6.String | None = o6.field(name="Language")


@o6.enumtype(nodeId="ns=di_package_metadata;i=9", browseName="ns=di_package_metadata;ComparisonOperation")
class ComparisonOperation(ns0.datatypes.Enumeration):
    EQUAL_TO = o6.enumfield(0, name="EqualTo")
    GREATER_THAN = o6.enumfield(1, name="GreaterThan")
    GREATER_EQUAL = o6.enumfield(2, name="GreaterEqual")
    LESS_THEN = o6.enumfield(3, name="LessThen")
    LESS_EQUAL = o6.enumfield(4, name="LessEqual")
    REGULAR_EXPRESSION = o6.enumfield(5, name="RegularExpression")
    ONE_OF = o6.enumfield(6, name="OneOf")
    EXIST = o6.enumfield(7, name="Exist")


@o6.datatype(nodeId="ns=di_package_metadata;i=4", browseName="ns=di_package_metadata;CompatibilityRequirement", defaultEncodingId="ns=di_package_metadata;i=17")
class CompatibilityRequirement(ns0.datatypes.Structure):
    variable: o6.String = o6.field(name="Variable")
    values: list[Any] = o6.field(name="Values")
    operation: ComparisonOperation = o6.field(name="Operation")


@o6.datatype(nodeId="ns=di_package_metadata;i=3", browseName="ns=di_package_metadata;CompatibilityOption", defaultEncodingId="ns=di_package_metadata;i=16")
class CompatibilityOption(ns0.datatypes.Structure):
    compatibilityRequirements: list[CompatibilityRequirement] = o6.field(name="CompatibilityRequirements")


@o6.datatype(nodeId="ns=di_package_metadata;i=13", browseName="ns=di_package_metadata;FxPathElement", defaultEncodingId="ns=di_package_metadata;i=20")
class FxPathElement(ns0.datatypes.Structure):
    assetConnectorType: o6.NodeId = o6.field(name="AssetConnectorType")
    connectorId: o6.UInt16 | None = o6.field(name="ConnectorId")
    connectorName: o6.String | None = o6.field(name="ConnectorName")


@o6.datatype(nodeId="ns=di_package_metadata;i=12", browseName="ns=di_package_metadata;PackageTarget", defaultEncodingId="ns=di_package_metadata;i=19")
class PackageTarget(ns0.datatypes.Structure):
    targetType: o6.NodeId | None = o6.field(name="TargetType")
    targetNode: o6.NodeId | None = o6.field(name="TargetNode")
    productInstanceUri: o6.String | None = o6.field(name="ProductInstanceUri")
    assetId: o6.String | None = o6.field(name="AssetId")
    manufacturerUri: o6.String | None = o6.field(name="ManufacturerUri")
    productCode: o6.String | None = o6.field(name="ProductCode")
    serialNumber: o6.String | None = o6.field(name="SerialNumber")
    fxPath: list[FxPathElement] | None = o6.field(name="FxPath")
    fxScope: list[FxPathElement] | None = o6.field(name="FxScope")
    browsePath: list[ns0.datatypes.RelativePathElement] | None = o6.field(name="BrowsePath")
    targetServer: o6.String | None = o6.field(name="TargetServer")


@o6.datatype(nodeId="ns=di_package_metadata;i=239", browseName="ns=di_package_metadata;UpdateTarget", defaultEncodingId="ns=di_package_metadata;i=240")
class UpdateTarget(ns0.datatypes.Structure):
    productCode: o6.String = o6.field(name="ProductCode")
    model: o6.String = o6.field(name="Model")


@o6.datatype(nodeId="ns=di_package_metadata;i=255", browseName="ns=di_package_metadata;Assignment", defaultEncodingId="ns=di_package_metadata;i=256")
class Assignment(ns0.datatypes.Structure):
    subpackage: o6.String = o6.field(name="Subpackage")
    installationOrder: o6.UInt32 | None = o6.field(name="InstallationOrder")
    targets: list[PackageTarget] = o6.field(name="Targets")


@o6.datatype(nodeId="ns=di_package_metadata;i=1", browseName="ns=di_package_metadata;PackageMetadata", defaultEncodingId="ns=di_package_metadata;i=14")
class PackageMetadata(ns0.datatypes.Structure):
    name: o6.String = o6.field(name="Name")
    description: o6.String | None = o6.field(name="Description")
    manufacturerUri: o6.String = o6.field(name="ManufacturerUri")
    manufacturer: o6.String = o6.field(name="Manufacturer")
    packageRevision: o6.String = o6.field(name="PackageRevision")
    packageType: PackageType = o6.field(name="PackageType")
    softwareSubClass: o6.String | None = o6.field(name="SoftwareSubClass")
    deployCompletePackage: o6.Boolean | None = o6.field(name="DeployCompletePackage")
    softwareRevision: o6.String | None = o6.field(name="SoftwareRevision")
    releaseDate: o6.DateTime | None = o6.field(name="ReleaseDate")
    targetManufacturerUri: o6.String | None = o6.field(name="TargetManufacturerUri")
    targetManufacturer: o6.String | None = o6.field(name="TargetManufacturer")
    updateTargets: list[UpdateTarget] | None = o6.field(name="UpdateTargets")
    files: list[FileDescriptor] | None = o6.field(name="Files")
    compatibilities: list[CompatibilityOption] | None = o6.field(name="Compatibilities")
    assignments: list[Assignment] | None = o6.field(name="Assignments")


del Any, TYPE_CHECKING, uuid, o6, ns0
