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

"""Generated OPC UA io_link namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as io_link_reftypes
from . import datatypes as io_link_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(nodeId="ns=io_link;i=2002", browseName="ns=io_link;ProcessDataVariableType", displayName="ProcessDataVariableType", valueRank=o6.ValueRank.ARRAY_1D)
class ProcessDataVariableType(ns0.vartypes.BaseDataVariableType):
    pDDescriptor: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6146", browseName="ns=io_link;PDDescriptor", dataType=o6.Byte, valueRank=2)
    )
    processDataLength: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6147", browseName="ns=io_link;ProcessDataLength", dataType=o6.Byte, value=0)
    )


del Any, TYPE_CHECKING, uuid, o6, di, ns0, io_link_reftypes, io_link_datypes
