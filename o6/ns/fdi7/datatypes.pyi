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

import o6.ns.di as di

import o6.ns.ns0 as ns0

class EddDataTypeEnum(enum.IntFlag):
    BOOLEAN = 1
    DOUBLE = 2
    FLOAT = 3
    INTEGER = 4
    UNSIGNED_INTEGER = 5
    DATE = 6
    DATE_AND_TIME = 7
    DURATION = 8
    TIME = 9
    TIME_VALUE = 10
    BIT_ENUMERATED = 11
    ENUMERATED = 12
    ASCII = 13
    BITSTRING = 14
    EUC = 15
    OCTET = 16
    PACKED_ASCII = 17
    PASSWORD = 18
    VISIBLE = 19

class EddDataTypeInfo(ns0.datatypes.Structure):
    @property
    def eddDataType(self) -> EddDataTypeEnum: ...
    @eddDataType.setter
    def eddDataType(self, value: _Integer) -> None: ...
    @property
    def size(self) -> o6.UInt32: ...
    @size.setter
    def size(self, value: _Integer) -> None: ...
