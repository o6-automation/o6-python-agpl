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

"""Generated OPC UA auto_id namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import datatypes as auto_id_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(nodeId="ns=auto_id;i=2002", browseName="ns=auto_id;LocationVariableType", displayName="LocationVariableType", dataType=auto_id_datypes.Location)
class LocationVariableType(ns0.vartypes.BaseDataVariableType):
    geographicalUnit: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6199", browseName="ns=auto_id;GeographicalUnit", dataType=ns0.datatypes.EUInformation, accessLevel=3)
    )
    lengthUnit: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6197", browseName="ns=auto_id;LengthUnit", dataType=ns0.datatypes.EUInformation, accessLevel=3)
    )
    rotationalUnit: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6198", browseName="ns=auto_id;RotationalUnit", dataType=ns0.datatypes.EUInformation, accessLevel=3)
    )
    speedUnit: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6200", browseName="ns=auto_id;SpeedUnit", dataType=ns0.datatypes.EUInformation, accessLevel=3)
    )


del Any, TYPE_CHECKING, uuid, o6, di, ns0, auto_id_datypes
