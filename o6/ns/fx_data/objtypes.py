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

"""Generated OPC UA fx_data namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import datatypes as fx_data_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=fx_data;i=1025", browseName="ns=fx_data;AuditUpdateMethodResultEventType", displayName="AuditUpdateMethodResultEventType", isAbstract=True)
class AuditUpdateMethodResultEventType(ns0.objtypes.AuditUpdateMethodEventType):
    outputArguments: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_data;i=6001", browseName="OutputArguments", valueRank=1, arrayDimensions=[0])
    )
    statusCodeId: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_data;i=6002", browseName="StatusCodeId", dataType=o6.StatusCode))


del Any, TYPE_CHECKING, uuid, o6, ns0, fx_data_datypes
