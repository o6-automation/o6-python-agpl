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

"""Generated OPC UA ia namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as ia_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=ia;i=3002", browseName="StacklightOperationMode", description="Contains the values used to indicate how a stacklight (as a whole unit) is used.")
class StacklightOperationMode(ns0.datatypes.Enumeration):
    SEGMENTED = o6.enumfield(0, name="Segmented")
    LEVELMETER = o6.enumfield(1, name="Levelmeter")
    RUNNING__LIGHT = o6.enumfield(2, name="Running_Light")
    OTHER = o6.enumfield(3, name="Other")


@o6.enumtype(
    nodeId="ns=ia;i=3003",
    browseName="LevelDisplayMode",
    description="Contains the values used to indicate how a percentual value is displayed if the stacklight unit works in Levelmeter mode.",
)
class LevelDisplayMode(ns0.datatypes.Enumeration):
    DIMMED = o6.enumfield(0, name="Dimmed")
    BLINKING = o6.enumfield(1, name="Blinking")
    OTHER = o6.enumfield(2, name="Other")


@o6.enumtype(nodeId="ns=ia;i=3004", browseName="SignalColor", description="Holds the possible colour values for stacklight lamps.")
class SignalColor(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(0, name="Off")
    RED = o6.enumfield(1, name="Red")
    GREEN = o6.enumfield(2, name="Green")
    BLUE = o6.enumfield(3, name="Blue")
    YELLOW = o6.enumfield(4, name="Yellow")
    PURPLE = o6.enumfield(5, name="Purple")
    CYAN = o6.enumfield(6, name="Cyan")
    WHITE = o6.enumfield(7, name="White")


@o6.enumtype(nodeId="ns=ia;i=3005", browseName="SignalModeLight", description="Contains the values used to indicate in what way a lamp behaves when switched on.")
class SignalModeLight(ns0.datatypes.Enumeration):
    CONTINUOUS = o6.enumfield(0, name="Continuous")
    BLINKING = o6.enumfield(1, name="Blinking")
    FLASHING = o6.enumfield(2, name="Flashing")
    OTHER = o6.enumfield(3, name="Other")


@o6.datatype(nodeId="ns=ia;i=3007", browseName="RGBWDataType", defaultEncodingId="ns=ia;i=5009")
class RGBWDataType(ns0.datatypes.Structure):
    red: o6.Byte
    green: o6.Byte
    blue: o6.Byte
    white: o6.Byte | None


del Any, TYPE_CHECKING, uuid, o6, di, ns0, ia_reftypes
