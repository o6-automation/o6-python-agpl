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

"""Generated OPC UA mdis namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as mdis_reftypes
from . import datatypes as mdis_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(
    nodeId="ns=mdis;i=1279",
    browseName="ns=mdis;InterlockVariableType",
    displayName="InterlockVariableType",
    description="This Variable type returns a Boolean indicating if the interlock is active, it shall also contain an InterlockFor reference",
    dataType=o6.Boolean,
)
class InterlockVariableType(ns0.vartypes.BaseDataVariableType):
    pass


@o6.variabletype(
    nodeId="ns=mdis;i=1290",
    browseName="ns=mdis;MDISVersionVariableType",
    displayName="MDISVersionVariableType",
    description="The standard representation of the version information that is related the MDIS Specification",
    dataType=mdis_datypes.MDISVersionDataType,
)
class MDISVersionVariableType(ns0.vartypes.BaseDataVariableType):
    build: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=1293", browseName="ns=mdis;Build", dataType=o6.Byte))
    majorVersion: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=1291", browseName="ns=mdis;MajorVersion", dataType=o6.Byte))
    minorVersion: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=1292", browseName="ns=mdis;MinorVersion", dataType=o6.Byte))


del Any, TYPE_CHECKING, uuid, o6, ns0, mdis_reftypes, mdis_datypes
