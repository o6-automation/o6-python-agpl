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

"""Generated OPC UA robotics namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.ns0 as ns0
from . import reftypes as robotics_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=robotics;i=3006", browseName="OperationalModeEnumeration")
class OperationalModeEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    MANUAL_REDUCED_SPEED = o6.enumfield(1, name="MANUAL_REDUCED_SPEED")
    MANUAL_HIGH_SPEED = o6.enumfield(2, name="MANUAL_HIGH_SPEED")
    AUTOMATIC = o6.enumfield(3, name="AUTOMATIC")
    AUTOMATIC_EXTERNAL = o6.enumfield(4, name="AUTOMATIC_EXTERNAL")


@o6.enumtype(nodeId="ns=robotics;i=3008", browseName="AxisMotionProfileEnumeration")
class AxisMotionProfileEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    ROTARY = o6.enumfield(1, name="ROTARY")
    ROTARY_ENDLESS = o6.enumfield(2, name="ROTARY_ENDLESS")
    LINEAR = o6.enumfield(3, name="LINEAR")
    LINEAR_ENDLESS = o6.enumfield(4, name="LINEAR_ENDLESS")


@o6.enumtype(nodeId="ns=robotics;i=18191", browseName="ExecutionModeEnumeration")
class ExecutionModeEnumeration(ns0.datatypes.Enumeration):
    CYCLE = o6.enumfield(0, name="CYCLE")
    CONTINUOUS = o6.enumfield(1, name="CONTINUOUS")
    STEP = o6.enumfield(2, name="STEP")


@o6.enumtype(nodeId="ns=robotics;i=18193", browseName="MotionDeviceCategoryEnumeration")
class MotionDeviceCategoryEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    ARTICULATED_ROBOT = o6.enumfield(1, name="ARTICULATED_ROBOT")
    SCARA_ROBOT = o6.enumfield(2, name="SCARA_ROBOT")
    CARTESIAN_ROBOT = o6.enumfield(3, name="CARTESIAN_ROBOT")
    SPHERICAL_ROBOT = o6.enumfield(4, name="SPHERICAL_ROBOT")
    PARALLEL_ROBOT = o6.enumfield(5, name="PARALLEL_ROBOT")
    CYLINDRICAL_ROBOT = o6.enumfield(6, name="CYLINDRICAL_ROBOT")


del Any, TYPE_CHECKING, uuid, o6, di, ia, ns0, robotics_reftypes
