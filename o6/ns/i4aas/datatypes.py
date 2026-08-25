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

"""Generated OPC UA i4aas namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as i4aas_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=i4aas;i=3002", browseName="AASKeyTypeDataType")
class AASKeyTypeDataType(ns0.datatypes.Enumeration):
    ID_SHORT = o6.enumfield(0, name="IdShort")
    FRAGMENT_ID = o6.enumfield(1, name="FragmentId")
    CUSTOM = o6.enumfield(2, name="Custom")
    IRDI = o6.enumfield(3, name="IRDI")
    IRI = o6.enumfield(4, name="IRI")


@o6.enumtype(nodeId="ns=i4aas;i=3003", browseName="AASAssetKindDataType")
class AASAssetKindDataType(ns0.datatypes.Enumeration):
    TYPE = o6.enumfield(0, name="Type")
    INSTANCE = o6.enumfield(1, name="Instance")


@o6.enumtype(nodeId="ns=i4aas;i=3004", browseName="AASValueTypeDataType")
class AASValueTypeDataType(ns0.datatypes.Enumeration):
    BOOLEAN = o6.enumfield(0, name="Boolean")
    S_BYTE = o6.enumfield(1, name="SByte")
    BYTE = o6.enumfield(2, name="Byte")
    INT16 = o6.enumfield(3, name="Int16")
    U_INT16 = o6.enumfield(4, name="UInt16")
    INT32 = o6.enumfield(5, name="Int32")
    U_INT32 = o6.enumfield(6, name="UInt32")
    INT64 = o6.enumfield(7, name="Int64")
    U_INT64 = o6.enumfield(8, name="UInt64")
    FLOAT = o6.enumfield(9, name="Float")
    DOUBLE = o6.enumfield(10, name="Double")
    STRING = o6.enumfield(11, name="String")
    DATE_TIME = o6.enumfield(12, name="DateTime")
    BYTE_STRING = o6.enumfield(13, name="ByteString")
    LOCALIZED_TEXT = o6.enumfield(14, name="LocalizedText")
    UTC_TIME = o6.enumfield(15, name="UtcTime")


@o6.datatype(nodeId="ns=i4aas;i=3005", browseName="AASPathDataType", parent="i=12")
class AASPathDataType:
    pass


@o6.enumtype(nodeId="ns=i4aas;i=3006", browseName="AASEntityTypeDataType")
class AASEntityTypeDataType(ns0.datatypes.Enumeration):
    CO_MANAGED_ENTITY = o6.enumfield(0, name="CoManagedEntity")
    SELF_MANAGED_ENTITY = o6.enumfield(1, name="SelfManagedEntity")


@o6.enumtype(nodeId="ns=i4aas;i=3007", browseName="AASCategoryDataType")
class AASCategoryDataType(ns0.datatypes.Enumeration):
    CONSTANT = o6.enumfield(0, name="CONSTANT")
    PARAMETER = o6.enumfield(1, name="PARAMETER")
    VARIABLE = o6.enumfield(2, name="VARIABLE")
    RELATIONSHIP = o6.enumfield(3, name="RELATIONSHIP")


@o6.enumtype(nodeId="ns=i4aas;i=3008", browseName="AASDataTypeIEC61360DataType")
class AASDataTypeIEC61360DataType(ns0.datatypes.Enumeration):
    BOOLEAN = o6.enumfield(0, name="BOOLEAN")
    DATE = o6.enumfield(1, name="DATE")
    RATIONAL = o6.enumfield(2, name="RATIONAL")
    RATIONAL_MEASURE = o6.enumfield(3, name="RATIONAL_MEASURE")
    REAL_COUNT = o6.enumfield(4, name="REAL_COUNT")
    REAL_CURRENCY = o6.enumfield(5, name="REAL_CURRENCY")
    REAL_MEASURE = o6.enumfield(6, name="REAL_MEASURE")
    STRING = o6.enumfield(7, name="STRING")
    STRING_TRANSLATABLE = o6.enumfield(8, name="STRING_TRANSLATABLE")
    TIME = o6.enumfield(9, name="TIME")
    TIME_STAMP = o6.enumfield(10, name="TIME_STAMP")
    URL = o6.enumfield(11, name="URL")
    INTEGER = o6.enumfield(12, name="INTEGER")
    INTEGER_COUNT = o6.enumfield(13, name="INTEGER_COUNT")
    INTEGER_CURRENCY = o6.enumfield(14, name="INTEGER_CURRENCY")


@o6.enumtype(nodeId="ns=i4aas;i=3009", browseName="AASLevelTypeDataType")
class AASLevelTypeDataType(ns0.datatypes.Enumeration):
    MIN = o6.enumfield(0, name="Min")
    MAX = o6.enumfield(1, name="Max")
    NUM = o6.enumfield(2, name="Num")
    TYPE = o6.enumfield(3, name="Type")


@o6.enumtype(nodeId="ns=i4aas;i=3010", browseName="AASIdentifierTypeDataType")
class AASIdentifierTypeDataType(ns0.datatypes.Enumeration):
    IRDI = o6.enumfield(0, name="IRDI")
    IRI = o6.enumfield(1, name="IRI")
    CUSTOM = o6.enumfield(2, name="Custom")


@o6.enumtype(nodeId="ns=i4aas;i=3012", browseName="AASKeyElementsDataType")
class AASKeyElementsDataType(ns0.datatypes.Enumeration):
    ACCESS_PERMISSION_RULE = o6.enumfield(0, name="AccessPermissionRule")
    ANNOTATED_RELATIONSHIP_ELEMENT = o6.enumfield(1, name="AnnotatedRelationshipElement")
    ASSET = o6.enumfield(2, name="Asset")
    ASSET_ADMINISTRATION_SHELL = o6.enumfield(3, name="AssetAdministrationShell")
    BLOB = o6.enumfield(4, name="Blob")
    CAPABILITY = o6.enumfield(5, name="Capability")
    CONCEPT_DESCRIPTION = o6.enumfield(6, name="ConceptDescription")
    CONCEPT_DICTIONARY = o6.enumfield(7, name="ConceptDictionary")
    DATA_ELEMENT = o6.enumfield(8, name="DataElement")
    ENTITY = o6.enumfield(9, name="Entity")
    EVENT = o6.enumfield(10, name="Event")
    FILE = o6.enumfield(11, name="File")
    FRAGMENT_REFERENCE = o6.enumfield(12, name="FragmentReference")
    GLOBAL_REFERENCE = o6.enumfield(13, name="GlobalReference")
    MULTI_LANGUAGE_PROPERTY = o6.enumfield(14, name="MultiLanguageProperty")
    OPERATION = o6.enumfield(15, name="Operation")
    PROPERTY = o6.enumfield(16, name="Property")
    RANGE = o6.enumfield(17, name="Range")
    REFERENCE_ELEMENT = o6.enumfield(18, name="ReferenceElement")
    RELATIONSHIP_ELEMENT = o6.enumfield(19, name="RelationshipElement")
    SUBMODEL = o6.enumfield(20, name="Submodel")
    SUBMODEL_ELEMENT = o6.enumfield(21, name="SubmodelElement")
    SUBMODEL_ELEMENT_COLLECTION = o6.enumfield(22, name="SubmodelElementCollection")
    VIEW = o6.enumfield(23, name="View")


@o6.datatype(nodeId="ns=i4aas;i=3011", browseName="AASKeyDataType", defaultEncodingId="ns=i4aas;i=5038")
class AASKeyDataType(ns0.datatypes.Structure):
    type: AASKeyElementsDataType
    local: o6.Boolean
    value: o6.String
    idType: AASKeyTypeDataType


@o6.datatype(nodeId="ns=i4aas;i=3013", browseName="AASQualifierDataType", parent="i=12")
class AASQualifierDataType:
    pass


@o6.datatype(nodeId="ns=i4aas;i=3014", browseName="AASPropertyValueDataType", parent="i=12")
class AASPropertyValueDataType:
    pass


@o6.enumtype(nodeId="ns=i4aas;i=3015", browseName="AASModelingKindDataType")
class AASModelingKindDataType(ns0.datatypes.Enumeration):
    TEMPLATE = o6.enumfield(0, name="Template")
    INSTANCE = o6.enumfield(1, name="Instance")


@o6.datatype(nodeId="ns=i4aas;i=3016", browseName="AASMimeDataType", parent="i=12")
class AASMimeDataType:
    pass


del Any, TYPE_CHECKING, uuid, o6, ns0, i4aas_reftypes
