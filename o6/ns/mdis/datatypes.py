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

"""Generated OPC UA mdis namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as mdis_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=mdis;i=3", browseName="CommandEnum")
class CommandEnum(ns0.datatypes.Enumeration):
    CLOSE = o6.enumfield(1, name="Close")
    OPEN = o6.enumfield(2, name="Open")
    NONE = o6.enumfield(4, name="None")


@o6.enumtype(nodeId="ns=mdis;i=5", browseName="SEMEnum")
class SEMEnum(ns0.datatypes.Enumeration):
    SEM_A = o6.enumfield(1, name="SEM_A")
    SEM_B = o6.enumfield(2, name="SEM_B")
    AUTO = o6.enumfield(4, name="Auto")


@o6.enumtype(nodeId="ns=mdis;i=602", browseName="ChokeMoveEnum")
class ChokeMoveEnum(ns0.datatypes.Enumeration):
    MOVING = o6.enumfield(1, name="Moving")
    STOPPED = o6.enumfield(2, name="Stopped")


@o6.enumtype(nodeId="ns=mdis;i=699", browseName="SignatureStatusEnum")
class SignatureStatusEnum(ns0.datatypes.Enumeration):
    NOT_AVAILABLE = o6.enumfield(1, name="NotAvailable")
    COMPLETED = o6.enumfield(2, name="Completed")
    FAILED = o6.enumfield(4, name="Failed")


@o6.enumtype(nodeId="ns=mdis;i=701", browseName="ChokeCommandEnum")
class ChokeCommandEnum(ns0.datatypes.Enumeration):
    CLOSE = o6.enumfield(1, name="Close")
    OPEN = o6.enumfield(2, name="Open")


@o6.enumtype(nodeId="ns=mdis;i=703", browseName="ValvePositionEnum")
class ValvePositionEnum(ns0.datatypes.Enumeration):
    CLOSED = o6.enumfield(1, name="Closed")
    OPEN = o6.enumfield(2, name="Open")
    MOVING = o6.enumfield(4, name="Moving")
    UNKNOWN = o6.enumfield(8, name="Unknown")


@o6.enumtype(nodeId="ns=mdis;i=1287", browseName="SetCalculatedPositionEnum")
class SetCalculatedPositionEnum(ns0.datatypes.Enumeration):
    INITIAL = o6.enumfield(0, name="Initial")
    INPROGRESS = o6.enumfield(1, name="Inprogress")
    COMPLETE = o6.enumfield(2, name="Complete")
    FAULT = o6.enumfield(4, name="Fault")


@o6.datatype(nodeId="ns=mdis;i=1289", browseName="MDISVersionDataType", defaultEncodingId="ns=mdis;i=1484")
class MDISVersionDataType(ns0.datatypes.Structure):
    majorVersion: o6.Byte
    minorVersion: o6.Byte
    build: o6.Byte


@o6.enumtype(nodeId="ns=mdis;i=15007", browseName="CIMVMoveEnum")
class CIMVMoveEnum(ns0.datatypes.Enumeration):
    MOVE_CLOSE = o6.enumfield(1, name="MoveClose")
    MOVE_OPEN = o6.enumfield(2, name="MoveOpen")
    STOP = o6.enumfield(4, name="Stop")


@o6.enumtype(nodeId="ns=mdis;i=15009", browseName="ArbitrationModeEnum")
class ArbitrationModeEnum(ns0.datatypes.Enumeration):
    AVERAGE = o6.enumfield(1, name="Average")
    DEFAULT_A = o6.enumfield(2, name="DefaultA")
    DEFAULT_B = o6.enumfield(4, name="DefaultB")
    FORCE_A = o6.enumfield(8, name="ForceA")
    FORCE_B = o6.enumfield(16, name="ForceB")
    HIGH = o6.enumfield(32, name="High")
    LOW = o6.enumfield(64, name="Low")


@o6.enumtype(nodeId="ns=mdis;i=15011", browseName="MotorStateEnum")
class MotorStateEnum(ns0.datatypes.Enumeration):
    ACTIVE = o6.enumfield(1, name="Active")
    NON_ACTIVE = o6.enumfield(2, name="NonActive")


@o6.enumtype(nodeId="ns=mdis;i=15013", browseName="MotorOperationEnum")
class MotorOperationEnum(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(1, name="Off")
    AUTO = o6.enumfield(2, name="Auto")
    MANUAL = o6.enumfield(4, name="Manual")


@o6.enumtype(nodeId="ns=mdis;i=15102", browseName="CIMVOperationModeEnum")
class CIMVOperationModeEnum(ns0.datatypes.Enumeration):
    POSITION = o6.enumfield(1, name="Position")
    FLOW = o6.enumfield(2, name="Flow")
    MANUAL = o6.enumfield(4, name="Manual")


del Any, TYPE_CHECKING, uuid, o6, ns0, mdis_reftypes
