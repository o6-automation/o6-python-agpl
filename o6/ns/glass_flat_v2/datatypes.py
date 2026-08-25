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

"""Generated OPC UA glass_flat_v2 namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=glass_flat_v2;i=3003", browseName="SignificantSideEnumeration")
class SignificantSideEnumeration(ns0.datatypes.Enumeration):
    INDIFFERENT = o6.enumfield(0, name="Indifferent")
    TOP = o6.enumfield(1, name="Top")
    DOWN = o6.enumfield(2, name="Down")


@o6.enumtype(nodeId="ns=glass_flat_v2;i=3004", browseName="StructureAlignmentEnumeration")
class StructureAlignmentEnumeration(ns0.datatypes.Enumeration):
    INDIFFERENT = o6.enumfield(0, name="Indifferent")
    LONGITUDINAL = o6.enumfield(1, name="Longitudinal")
    TRANSVERSE = o6.enumfield(2, name="Transverse")


@o6.enumtype(nodeId="ns=glass_flat_v2;i=3005", browseName="SpacerMaterialClass")
class SpacerMaterialClass(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="Other")
    METALLIC = o6.enumfield(1, name="Metallic")
    TPS = o6.enumfield(2, name="TPS")
    PLASTIC = o6.enumfield(3, name="Plastic")
    ELASTIC = o6.enumfield(4, name="Elastic")


@o6.datatype(nodeId="ns=glass_flat_v2;i=3006", browseName="UserProfileDataType", defaultEncodingId="ns=glass_flat_v2;i=5082")
class UserProfileDataType(ns0.datatypes.Structure):
    name: o6.String
    loginTime: o6.DateTime
    language: o6.String
    measurementFormat: o6.String
    accessLevel: o6.String
    opcUaUser: o6.Boolean


@o6.datatype(nodeId="ns=glass_flat_v2;i=3007", browseName="FileFormatDataType", defaultEncodingId="ns=glass_flat_v2;i=5037")
class FileFormatDataType(ns0.datatypes.Structure):
    name: o6.String
    fileExtension: o6.String
    version: o6.String


@o6.enumtype(nodeId="ns=glass_flat_v2;i=3008", browseName="CoordinateSystemEnumeration")
class CoordinateSystemEnumeration(ns0.datatypes.Enumeration):
    UNKNOWN = o6.enumfield(0, name="Unknown")
    SYSTEM1 = o6.enumfield(1, name="System1")
    SYSTEM2 = o6.enumfield(2, name="System2")
    SYSTEM3 = o6.enumfield(3, name="System3")
    SYSTEM4 = o6.enumfield(4, name="System4")
    SYSTEM5 = o6.enumfield(5, name="System5")
    SYSTEM6 = o6.enumfield(6, name="System6")
    SYSTEM7 = o6.enumfield(7, name="System7")
    SYSTEM8 = o6.enumfield(8, name="System8")


@o6.enumtype(nodeId="ns=glass_flat_v2;i=3009", browseName="CoatingClassEnumeration")
class CoatingClassEnumeration(ns0.datatypes.Enumeration):
    HARD_COATING = o6.enumfield(0, name="HardCoating")
    SOFT_COATING = o6.enumfield(1, name="SoftCoating")
    COATED_WITH_FOIL_PROTECTION = o6.enumfield(2, name="CoatedWithFoilProtection")
    USER_DEFINED = o6.enumfield(3, name="UserDefined")


@o6.datatype(nodeId="ns=glass_flat_v2;i=3012", browseName="ReasonDescriptionType", defaultEncodingId="ns=glass_flat_v2;i=5003")
class ReasonDescriptionType(ns0.datatypes.Structure):
    description: o6.LocalizedText
    reference: o6.String | None
    category: o6.String | None
    vendorCode: o6.String | None


@o6.datatype(nodeId="ns=glass_flat_v2;i=3017", browseName="EClassTermDataType", defaultEncodingId="ns=glass_flat_v2;i=5013")
class EClassTermDataType(ns0.datatypes.Structure):
    iD: o6.String
    description: o6.String
    eClass: o6.String


@o6.datatype(nodeId="ns=glass_flat_v2;i=3020", browseName="ValueDataType", defaultEncodingId="ns=glass_flat_v2;i=5019")
class ValueDataType(ns0.datatypes.Structure):
    name: o6.String
    description: o6.String
    baseUnit: o6.String
    possibleValue: o6.String


@o6.datatype(nodeId="ns=glass_flat_v2;i=3011", browseName="ProcessingParameterDataType", defaultEncodingId="ns=glass_flat_v2;i=5004")
class ProcessingParameterDataType(ns0.datatypes.Structure):
    name: o6.String
    description: o6.String
    valueType: ValueDataType
    typicalValue: o6.String
    mandatory: o6.Boolean
    eClass: EClassTermDataType


@o6.datatype(nodeId="ns=glass_flat_v2;i=3014", browseName="ProcessingCategoryDataType", defaultEncodingId="ns=glass_flat_v2;i=5007")
class ProcessingCategoryDataType(ns0.datatypes.Structure):
    iD: o6.String
    description: o6.String
    supportedParameter: list[ProcessingParameterDataType]
    supportedAssignment: list[o6.String]
    supportedVariable: list[ProcessingParameterDataType]
    supportsTransformation: o6.Int32
    supportsSubProcessing: o6.Int32


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, ns0
