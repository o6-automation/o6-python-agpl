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

"""Generated OPC UA plastics_extrusion_haul_off namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
import o6.ns.plastics_extrusion as plastics_extrusion
import o6.ns.plastics_rubber as plastics_rubber

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=plastics_extrusion_haul_off;i=1002", browseName="ns=plastics_extrusion_haul_off;HaulOff_InterfaceType", displayName="HaulOff_InterfaceType")
class HaulOff_InterfaceType(plastics_extrusion.objtypes.ExtrusionDeviceType):
    clampClosed: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_haul_off;i=6013", browseName="ns=plastics_extrusion_haul_off;ClampClosed", dataType=o6.Boolean)
    )
    closeClamp: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_haul_off;i=7002", browseName="ns=plastics_extrusion_haul_off;CloseClamp"))
    drives: plastics_rubber.objtypes.DrivesType
    force: plastics_rubber.objtypes.MonitoredParameterType | None
    openClamp: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_haul_off;i=7001", browseName="ns=plastics_extrusion_haul_off;OpenClamp"))
    temperatureZones: plastics_extrusion.objtypes.ExtrusionTemperatureZonesType | None


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, plastics_extrusion, plastics_rubber
