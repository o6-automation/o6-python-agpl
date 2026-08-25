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

"""Generated OPC UA weihenstephan namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
import o6.ns.pack_ml as pack_ml
from . import datatypes as weihenstephan_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(nodeId="ns=weihenstephan;i=2001", browseName="ns=weihenstephan;WSBaseDataVariableType", displayName="WSBaseDataVariableType")
class WSBaseDataVariableType(ns0.vartypes.BaseDataVariableType):
    wSTagNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=weihenstephan;i=6022", browseName="ns=weihenstephan;WSTagNumber", dataType=o6.UInt16, valueRank=-2, accessLevel=3)
    )


@o6.variabletype(nodeId="ns=weihenstephan;i=2000", browseName="ns=weihenstephan;WSAnalogUnitType", displayName="WSAnalogUnitType")
class WSAnalogUnitType(ns0.vartypes.AnalogUnitType):
    wSTagNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=weihenstephan;i=6027", browseName="ns=weihenstephan;WSTagNumber", dataType=o6.UInt16, accessLevel=3)
    )


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, pack_ml, weihenstephan_datypes
