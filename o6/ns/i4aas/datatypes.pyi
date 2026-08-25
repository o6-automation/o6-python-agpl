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

from typing import Any, Sequence, SupportsFloat

import numpy as np

_Integer = int | np.integer[Any]

_Boolean = bool | np.bool_

import enum

from o6.node import ObjectNode as _ObjectNode, VariableNode as _VariableNode

import uuid

import o6

import o6.ns.ns0 as ns0

class AASKeyTypeDataType(enum.IntFlag):
    ID_SHORT = 0
    FRAGMENT_ID = 1
    CUSTOM = 2
    IRDI = 3
    IRI = 4

class AASAssetKindDataType(enum.IntFlag):
    TYPE = 0
    INSTANCE = 1

class AASValueTypeDataType(enum.IntFlag):
    BOOLEAN = 0
    S_BYTE = 1
    BYTE = 2
    INT16 = 3
    U_INT16 = 4
    INT32 = 5
    U_INT32 = 6
    INT64 = 7
    U_INT64 = 8
    FLOAT = 9
    DOUBLE = 10
    STRING = 11
    DATE_TIME = 12
    BYTE_STRING = 13
    LOCALIZED_TEXT = 14
    UTC_TIME = 15

class AASPathDataType:
    pass

class AASEntityTypeDataType(enum.IntFlag):
    CO_MANAGED_ENTITY = 0
    SELF_MANAGED_ENTITY = 1

class AASCategoryDataType(enum.IntFlag):
    CONSTANT = 0
    PARAMETER = 1
    VARIABLE = 2
    RELATIONSHIP = 3

class AASDataTypeIEC61360DataType(enum.IntFlag):
    BOOLEAN = 0
    DATE = 1
    RATIONAL = 2
    RATIONAL_MEASURE = 3
    REAL_COUNT = 4
    REAL_CURRENCY = 5
    REAL_MEASURE = 6
    STRING = 7
    STRING_TRANSLATABLE = 8
    TIME = 9
    TIME_STAMP = 10
    URL = 11
    INTEGER = 12
    INTEGER_COUNT = 13
    INTEGER_CURRENCY = 14

class AASLevelTypeDataType(enum.IntFlag):
    MIN = 0
    MAX = 1
    NUM = 2
    TYPE = 3

class AASIdentifierTypeDataType(enum.IntFlag):
    IRDI = 0
    IRI = 1
    CUSTOM = 2

class AASKeyElementsDataType(enum.IntFlag):
    ACCESS_PERMISSION_RULE = 0
    ANNOTATED_RELATIONSHIP_ELEMENT = 1
    ASSET = 2
    ASSET_ADMINISTRATION_SHELL = 3
    BLOB = 4
    CAPABILITY = 5
    CONCEPT_DESCRIPTION = 6
    CONCEPT_DICTIONARY = 7
    DATA_ELEMENT = 8
    ENTITY = 9
    EVENT = 10
    FILE = 11
    FRAGMENT_REFERENCE = 12
    GLOBAL_REFERENCE = 13
    MULTI_LANGUAGE_PROPERTY = 14
    OPERATION = 15
    PROPERTY = 16
    RANGE = 17
    REFERENCE_ELEMENT = 18
    RELATIONSHIP_ELEMENT = 19
    SUBMODEL = 20
    SUBMODEL_ELEMENT = 21
    SUBMODEL_ELEMENT_COLLECTION = 22
    VIEW = 23

class AASKeyDataType(ns0.datatypes.Structure):
    @property
    def type(self) -> AASKeyElementsDataType: ...
    @type.setter
    def type(self, value: _Integer) -> None: ...
    @property
    def local(self) -> o6.Boolean: ...
    @local.setter
    def local(self, value: _Boolean) -> None: ...
    @property
    def value(self) -> o6.String: ...
    @value.setter
    def value(self, value: o6.String) -> None: ...
    @property
    def idType(self) -> AASKeyTypeDataType: ...
    @idType.setter
    def idType(self, value: _Integer) -> None: ...

class AASQualifierDataType:
    pass

class AASPropertyValueDataType:
    pass

class AASModelingKindDataType(enum.IntFlag):
    TEMPLATE = 0
    INSTANCE = 1

class AASMimeDataType:
    pass
