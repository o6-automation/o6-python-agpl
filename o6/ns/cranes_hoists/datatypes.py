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

"""Generated OPC UA cranes_hoists namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
import o6.ns.robotics as robotics
from . import reftypes as cranes_hoists_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=cranes_hoists;i=3000", browseName="CraneOperationalModeEnum")
class CraneOperationalModeEnum(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    MANUAL = o6.enumfield(1, name="MANUAL")
    SEMIAUTOMATIC = o6.enumfield(2, name="SEMIAUTOMATIC")
    FULLAUTOMATIC = o6.enumfield(3, name="FULLAUTOMATIC")
    BYPASS_ON = o6.enumfield(4, name="BYPASS_ON")
    MAINTENANCE = o6.enumfield(5, name="MAINTENANCE")


@o6.enumtype(nodeId="ns=cranes_hoists;i=3001", browseName="ExternalControlRequestEnum")
class ExternalControlRequestEnum(ns0.datatypes.Enumeration):
    NOT_REQUESTED = o6.enumfield(0, name="NOT_REQUESTED")
    REQUESTED_AND_CONTROL_ACTIVE = o6.enumfield(1, name="REQUESTED_AND_CONTROL_ACTIVE")
    REQUESTED_AND_CONTROL_INACTIVE = o6.enumfield(2, name="REQUESTED_AND_CONTROL_INACTIVE")
    REQUESTED_AND_CONTROL_BYPASSED = o6.enumfield(3, name="REQUESTED_AND_CONTROL_BYPASSED")


@o6.enumtype(nodeId="ns=cranes_hoists;i=3002", browseName="ProtectiveFunctionEnum")
class ProtectiveFunctionEnum(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    FORCE_LIMITER = o6.enumfield(1, name="FORCE_LIMITER")
    OVERSPEED_CONTROL = o6.enumfield(2, name="OVERSPEED_CONTROL")
    MOTION_LIMITER = o6.enumfield(3, name="MOTION_LIMITER")
    ANTICOLLISION = o6.enumfield(4, name="ANTICOLLISION")


@o6.enumtype(nodeId="ns=cranes_hoists;i=3003", browseName="CraneMotionDeviceCategoryEnum")
class CraneMotionDeviceCategoryEnum(ns0.datatypes.Enumeration):
    HOIST = o6.enumfield(0, name="HOIST")
    TROLLEY_TRAVERSE = o6.enumfield(1, name="TROLLEY_TRAVERSE")
    BRIDGE_OR_GANTRY_TRAVEL = o6.enumfield(2, name="BRIDGE_OR_GANTRY_TRAVEL")
    LOAD_LIFTING_ATTACHMENT = o6.enumfield(3, name="LOAD_LIFTING_ATTACHMENT")
    ROTATING_OR_SLEWING = o6.enumfield(4, name="ROTATING_OR_SLEWING")
    LUFFING = o6.enumfield(5, name="LUFFING")
    POWER_SUPPLY_MACHINERY = o6.enumfield(6, name="POWER_SUPPLY_MACHINERY")
    OTHER = o6.enumfield(7, name="OTHER")


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, robotics, cranes_hoists_reftypes
