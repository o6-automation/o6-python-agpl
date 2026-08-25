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

"""Generated OPC UA fdi7 namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=fdi7;i=2048", browseName="EddDataTypeEnum")
class EddDataTypeEnum(ns0.datatypes.Enumeration):
    BOOLEAN = o6.enumfield(1, name="BOOLEAN")
    DOUBLE = o6.enumfield(2, name="DOUBLE")
    FLOAT = o6.enumfield(3, name="FLOAT")
    INTEGER = o6.enumfield(4, name="INTEGER")
    UNSIGNED_INTEGER = o6.enumfield(5, name="UNSIGNED_INTEGER")
    DATE = o6.enumfield(6, name="DATE")
    DATE_AND_TIME = o6.enumfield(7, name="DATE_AND_TIME")
    DURATION = o6.enumfield(8, name="DURATION")
    TIME = o6.enumfield(9, name="TIME")
    TIME_VALUE = o6.enumfield(10, name="TIME_VALUE")
    BIT_ENUMERATED = o6.enumfield(11, name="BIT_ENUMERATED")
    ENUMERATED = o6.enumfield(12, name="ENUMERATED")
    ASCII = o6.enumfield(13, name="ASCII")
    BITSTRING = o6.enumfield(14, name="BITSTRING")
    EUC = o6.enumfield(15, name="EUC")
    OCTET = o6.enumfield(16, name="OCTET")
    PACKED_ASCII = o6.enumfield(17, name="PACKED_ASCII")
    PASSWORD = o6.enumfield(18, name="PASSWORD")
    VISIBLE = o6.enumfield(19, name="VISIBLE")


@o6.datatype(nodeId="ns=fdi7;i=2050", browseName="EddDataTypeInfo", defaultEncodingId="ns=fdi7;i=2213")
class EddDataTypeInfo(ns0.datatypes.Structure):
    eddDataType: EddDataTypeEnum
    size: o6.UInt32


del Any, TYPE_CHECKING, uuid, o6, di, ns0
