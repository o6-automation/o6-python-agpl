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

"""Generated OPC UA plastics_extrusion_v1 namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_rubber as plastics_rubber

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=plastics_extrusion_v1;i=3001", browseName="ExtrusionMessageClassificationEnumeration")
class ExtrusionMessageClassificationEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    LINE_CONTROL = o6.enumfield(1, name="LINE_CONTROL")
    MATERIAL_HANDLING = o6.enumfield(2, name="MATERIAL_HANDLING")
    PRE_HEATING = o6.enumfield(3, name="PRE_HEATING")
    FEEDING = o6.enumfield(4, name="FEEDING")
    DOSING = o6.enumfield(5, name="DOSING")
    EXTRUDER = o6.enumfield(6, name="EXTRUDER")
    VACUUM_STATION = o6.enumfield(7, name="VACUUM_STATION")
    FILTER = o6.enumfield(8, name="FILTER")
    MELT_PUMP = o6.enumfield(9, name="MELT_PUMP")
    DIE = o6.enumfield(10, name="DIE")
    COOLING = o6.enumfield(11, name="COOLING")
    HAUL_OFF = o6.enumfield(12, name="HAUL_OFF")
    CORRUGATOR = o6.enumfield(13, name="CORRUGATOR")
    SAW = o6.enumfield(14, name="SAW")
    CALIBRATION = o6.enumfield(15, name="CALIBRATION")
    ROLL_STACK = o6.enumfield(16, name="ROLL_STACK")
    MDO = o6.enumfield(17, name="MDO")
    BIAX = o6.enumfield(18, name="BIAX")
    CUTTING = o6.enumfield(19, name="CUTTING")
    WINDER = o6.enumfield(20, name="WINDER")
    PELLETIZING = o6.enumfield(21, name="PELLETIZING")
    DRYER = o6.enumfield(22, name="DRYER")
    HANDLING_SYSTEM = o6.enumfield(23, name="HANDLING_SYSTEM")
    LAMINATION_SYSTEM = o6.enumfield(24, name="LAMINATION_SYSTEM")
    MEASURING_SYSTEM = o6.enumfield(25, name="MEASURING_SYSTEM")
    QUALITY_SYSTEM = o6.enumfield(26, name="QUALITY_SYSTEM")
    MANUAL_INSPECTION = o6.enumfield(27, name="MANUAL_INSPECTION")
    MANUAL_OPERATION = o6.enumfield(28, name="MANUAL_OPERATION")


@o6.enumtype(nodeId="ns=plastics_extrusion_v1;i=3003", browseName="ComponentStatusEnumeration")
class ComponentStatusEnumeration(ns0.datatypes.Enumeration):
    OFFLINE = o6.enumfield(0, name="OFFLINE")
    IDLE = o6.enumfield(1, name="IDLE")
    PREPARING = o6.enumfield(2, name="PREPARING")
    READY_TO_RUN = o6.enumfield(3, name="READY_TO_RUN")
    MANUAL_RUN = o6.enumfield(4, name="MANUAL_RUN")
    CONTROLLED_RUN = o6.enumfield(5, name="CONTROLLED_RUN")
    MALFUNCTION = o6.enumfield(6, name="MALFUNCTION")
    MAINTENANCE = o6.enumfield(7, name="MAINTENANCE")


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_rubber
