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

"""Generated OPC UA plastics_extrusion_v1_corrugator namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_extrusion_v1 as plastics_extrusion_v1
import o6.ns.plastics_extrusion_v1_haul_off as plastics_extrusion_v1_haul_off
import o6.ns.plastics_rubber as plastics_rubber

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=plastics_extrusion_v1_corrugator;i=1003", browseName="ns=plastics_extrusion_v1_corrugator;Corrugator_InterfaceType", displayName="Corrugator_InterfaceType"
)
class Corrugator_InterfaceType(plastics_extrusion_v1_haul_off.objtypes.HaulOff_InterfaceType):
    extruderEnabled: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_extrusion_v1_corrugator;i=6002", browseName="ns=plastics_extrusion_v1_corrugator;ExtruderEnabled", dataType=o6.Boolean
        )
    )
    mouldId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_corrugator;i=6001", browseName="ns=plastics_extrusion_v1_corrugator;MouldId", dataType=o6.String)
    )


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_extrusion_v1, plastics_extrusion_v1_haul_off, plastics_rubber
