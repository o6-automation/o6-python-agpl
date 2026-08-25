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

"""Generated OPC UA mining_shearer_loader namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.mining as mining
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=mining_shearer_loader;i=3002", browseName="ShearerDirectionEnum")
class ShearerDirectionEnum(ns0.datatypes.Enumeration):
    STOP = o6.enumfield(0, name="STOP")
    LEFT = o6.enumfield(1, name="LEFT")
    RIGHT = o6.enumfield(2, name="RIGHT")


@o6.enumtype(nodeId="ns=mining_shearer_loader;i=3004", browseName="ShearerDrumMountingPositionEnum")
class ShearerDrumMountingPositionEnum(ns0.datatypes.Enumeration):
    MOUNTING_POSITION_LEFT = o6.enumfield(0, name="MountingPositionLeft")
    MOUNTING_POSITION_RIGHT = o6.enumfield(1, name="MountingPositionRight")
    MOUNTING_POSITION_LEFT_LUMP_BREAKER = o6.enumfield(2, name="MountingPositionLeftLumpBreaker")
    MOUNTING_POSITION_RIGHT_LUMP_BREAKER = o6.enumfield(3, name="MountingPositionRightLumpBreaker")


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, mining, ns0
