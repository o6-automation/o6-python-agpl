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

"""Generated OPC UA plastics_extrusion_calender namespace declarations."""

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


@o6.objecttype(nodeId="ns=plastics_extrusion_calender;i=1002", browseName="ns=plastics_extrusion_calender;Calender_InterfaceType", displayName="Calender_InterfaceType")
class Calender_InterfaceType(plastics_extrusion.objtypes.ExtrusionDeviceType):
    couplingProductForces: CouplingProductForcesType | None
    couplingProductTensions: CouplingProductTensionsType | None
    gaps: plastics_extrusion.objtypes.GapsType
    horizontalPosition: plastics_rubber.objtypes.MonitoredParameterType | None
    productForce: plastics_rubber.objtypes.MonitoredParameterType | None
    productTension: plastics_rubber.objtypes.MonitoredParameterType | None
    rolls: plastics_extrusion.objtypes.RollsType
    verticalPosition: plastics_rubber.objtypes.MonitoredParameterType | None


@o6.objecttype(nodeId="ns=plastics_extrusion_calender;i=1003", browseName="ns=plastics_extrusion_calender;CouplingProductForcesType", displayName="CouplingProductForcesType")
class CouplingProductForcesType(ns0.objtypes.BaseObjectType):
    couplingProductForce_LangleNrRangle: plastics_rubber.objtypes.MonitoredParameterType | None
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calender;i=6076", browseName="NodeVersion", dataType=o6.String))


o6.reference(CouplingProductForcesType, "i=41", "i=2133")


@o6.objecttype(nodeId="ns=plastics_extrusion_calender;i=1004", browseName="ns=plastics_extrusion_calender;CouplingProductTensionsType", displayName="CouplingProductTensionsType")
class CouplingProductTensionsType(ns0.objtypes.BaseObjectType):
    couplingProductTension_LangleNrRangle: plastics_rubber.objtypes.MonitoredParameterType | None
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_calender;i=6105", browseName="NodeVersion", dataType=o6.String))


o6.reference(CouplingProductTensionsType, "i=41", "i=2133")


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, plastics_extrusion, plastics_rubber
