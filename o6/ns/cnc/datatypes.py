# Copyright (c) 2026 o6 Automation GmbH
#
# SPDX-License-Identifier: AGPL-3.0-or-later
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

"""Generated OPC UA cnc namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=cnc;i=3001", browseName="CncSpindleTurnDirection", description="Turn direction of a CNC spindle.")
class CncSpindleTurnDirection(ns0.datatypes.Enumeration):
    NONE = o6.enumfield(0, name="None")
    CW = o6.enumfield(1, name="CW")
    CCW = o6.enumfield(2, name="CCW")


@o6.enumtype(nodeId="ns=cnc;i=3002", browseName="CncChannelProgramStatus", description="Status of program execution within a channel.")
class CncChannelProgramStatus(ns0.datatypes.Enumeration):
    STOPPED = o6.enumfield(0, name="Stopped")
    RUNNING = o6.enumfield(1, name="Running")
    WAITING = o6.enumfield(2, name="Waiting")
    INTERRUPTED = o6.enumfield(3, name="Interrupted")
    CANCELED = o6.enumfield(4, name="Canceled")


@o6.enumtype(nodeId="ns=cnc;i=3003", browseName="CncChannelStatus", description="Status of a CNC channel.")
class CncChannelStatus(ns0.datatypes.Enumeration):
    ACTIVE = o6.enumfield(0, name="Active")
    INTERRUPTED = o6.enumfield(1, name="Interrupted")
    RESET = o6.enumfield(2, name="Reset")


@o6.enumtype(nodeId="ns=cnc;i=3004", browseName="CncAxisStatus", description="Status of a CNC axis.")
class CncAxisStatus(ns0.datatypes.Enumeration):
    IN_POSITION = o6.enumfield(0, name="InPosition")
    MOVING = o6.enumfield(1, name="Moving")
    PARKED = o6.enumfield(2, name="Parked")


@o6.enumtype(nodeId="ns=cnc;i=3005", browseName="CncSpindleStatus", description="Status of a CNC spindle.")
class CncSpindleStatus(ns0.datatypes.Enumeration):
    STOPPED = o6.enumfield(0, name="Stopped")
    IN_TARGET_AREA = o6.enumfield(1, name="InTargetArea")
    ACCELERATING = o6.enumfield(2, name="Accelerating")
    DECELERATING = o6.enumfield(3, name="Decelerating")
    PARKED = o6.enumfield(4, name="Parked")


@o6.enumtype(nodeId="ns=cnc;i=3006", browseName="CncOperationMode", description="Modes of operation.")
class CncOperationMode(ns0.datatypes.Enumeration):
    MANUAL = o6.enumfield(0, name="Manual")
    MDA = o6.enumfield(1, name="MDA")
    AUTOMATIC = o6.enumfield(2, name="Automatic")


@o6.datatype(nodeId="ns=cnc;i=3007", browseName="CncPositionDataType", description="Structure of position elements.", defaultEncodingId="ns=cnc;i=5001")
class CncPositionDataType(ns0.datatypes.Structure):
    actPos: o6.Double
    cmdPos: o6.Double
    remDist: o6.Double


del Any, TYPE_CHECKING, uuid, o6, ns0
