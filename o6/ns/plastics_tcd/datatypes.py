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

"""Generated OPC UA plastics_tcd namespace declarations."""

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


@o6.enumtype(nodeId="ns=plastics_tcd;i=3002", browseName="OperatingModeEnumeration", description="Actual operating mode of the TCD")
class OperatingModeEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    READY_TO_OPERATE = o6.enumfield(1, name="READY_TO_OPERATE")
    NORMAL_OPERATION = o6.enumfield(2, name="NORMAL_OPERATION")
    LEAK_STOPPER = o6.enumfield(3, name="LEAK_STOPPER")
    MOULD_EVACUATION = o6.enumfield(4, name="MOULD_EVACUATION")
    PRESSURE_RELIEF = o6.enumfield(5, name="PRESSURE_RELIEF")
    COOLING = o6.enumfield(6, name="COOLING")
    SAFETY_COOLING = o6.enumfield(7, name="SAFETY_COOLING")
    ECO = o6.enumfield(8, name="ECO")
    BOOST = o6.enumfield(9, name="BOOST")


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_rubber
