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

"""Generated OPC UA plastics_lds namespace declarations."""

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


@o6.enumtype(
    nodeId="ns=plastics_lds;i=3002",
    browseName="AdditiveStatusEnumeration",
    description="Actual status of the additive provides a minimal error handling for devices without event support.",
)
class AdditiveStatusEnumeration(ns0.datatypes.Enumeration):
    GOOD = o6.enumfield(0, name="GOOD")
    WARNING = o6.enumfield(1, name="WARNING")
    ADVANCE_WARNING_ADDITIVE_CHANGE = o6.enumfield(2, name="ADVANCE_WARNING_ADDITIVE_CHANGE")
    ERROR_EMPTY = o6.enumfield(3, name="ERROR_EMPTY")
    ERROR = o6.enumfield(4, name="ERROR")


@o6.enumtype(
    nodeId="ns=plastics_lds;i=3003",
    browseName="ComponentStatusEnumeration",
    description="Actual status of the component provides a minimal error handling for devices without event support.",
)
class ComponentStatusEnumeration(ns0.datatypes.Enumeration):
    GOOD = o6.enumfield(0, name="GOOD")
    WARNING = o6.enumfield(1, name="WARNING")
    WARNING_PRESSURE_TOO_HIGH = o6.enumfield(2, name="WARNING_PRESSURE_TOO_HIGH")
    WARNING_PRESSURE_TOO_LOW = o6.enumfield(3, name="WARNING_PRESSURE_TOO_LOW")
    ADVANCE_WARNING_DRUM_CHANGE = o6.enumfield(4, name="ADVANCE_WARNING_DRUM_CHANGE")
    ERROR_DRUM_EMPTY = o6.enumfield(5, name="ERROR_DRUM_EMPTY")
    ERROR = o6.enumfield(6, name="ERROR")


@o6.enumtype(nodeId="ns=plastics_lds;i=3004", browseName="PurgeStatusEnumeration")
class PurgeStatusEnumeration(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(0, name="OFF")
    COMPONENT_A = o6.enumfield(1, name="COMPONENT_A")
    COMPONENT_B = o6.enumfield(2, name="COMPONENT_B")
    COMPONENT_A_AND_B = o6.enumfield(3, name="COMPONENT_A_AND_B")
    COMPONENT_A_AND_B_CYCLIC = o6.enumfield(4, name="COMPONENT_A_AND_B_CYCLIC")


@o6.enumtype(nodeId="ns=plastics_lds;i=3005", browseName="MaterialBalanceSystemTypeEnumeration")
class MaterialBalanceSystemTypeEnumeration(ns0.datatypes.Enumeration):
    NOT_AVAILABLE = o6.enumfield(0, name="NOT_AVAILABLE")
    ALWAYS_ACTIVE = o6.enumfield(1, name="ALWAYS_ACTIVE")
    SELECTABLE = o6.enumfield(2, name="SELECTABLE")


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_rubber
