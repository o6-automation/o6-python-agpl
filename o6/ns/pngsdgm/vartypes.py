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

"""Generated OPC UA pngsdgm namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as pngsdgm_reftypes
from . import datatypes as pngsdgm_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(nodeId="ns=pngsdgm;i=2003", browseName="ns=pngsdgm;GsdGenIoBitDataItemVariableType", displayName="GsdGenIoBitDataItemVariableType", dataType=o6.Byte, value=0)
class GsdGenIoBitDataItemVariableType(ns0.vartypes.BaseDataVariableType):
    pass


@o6.variabletype(nodeId="ns=pngsdgm;i=2002", browseName="ns=pngsdgm;GsdGenParameterVariableType", displayName="GsdGenParameterVariableType")
class GsdGenParameterVariableType(ns0.vartypes.BaseDataVariableType):
    bitLength: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6019", browseName="ns=pngsdgm;BitLength", dataType=o6.UInt16))
    bitOffset: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6018", browseName="ns=pngsdgm;BitOffset", dataType=o6.UInt16))
    byteOffset: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6017", browseName="ns=pngsdgm;ByteOffset", dataType=o6.UInt32))
    defaultValue: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6015", browseName="ns=pngsdgm;DefaultValue"))
    index: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6016", browseName="ns=pngsdgm;Index", dataType=o6.UInt16))


@o6.variabletype(nodeId="ns=pngsdgm;i=2004", browseName="ns=pngsdgm;GsdGenIoDataItemVariableType", displayName="GsdGenIoDataItemVariableType")
class GsdGenIoDataItemVariableType(ns0.vartypes.BaseDataVariableType):
    langleBitDataItemRangle: GsdGenIoBitDataItemVariableType | None = o6.hasComponent(
        GsdGenIoBitDataItemVariableType(nodeId="ns=pngsdgm;i=6021", browseName="ns=pngsdgm;<BitDataItem>", modellingRule="OptionalPlaceholder", dataType=o6.Byte, value=0)
    )
    useAsBits: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6020", browseName="ns=pngsdgm;UseAsBits", dataType=o6.Boolean))


del Any, TYPE_CHECKING, uuid, o6, di, ns0, pngsdgm_reftypes, pngsdgm_datypes
