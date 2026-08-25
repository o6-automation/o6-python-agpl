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

"""Generated OPC UA safety namespace declarations."""

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


@o6.datatype(
    nodeId="ns=safety;i=3002",
    browseName="NonSafetyDataPlaceholderDataType",
    description="Dummy structure to be used when no non-safety data are used",
    defaultEncodingId="ns=safety;i=5003",
)
class NonSafetyDataPlaceholderDataType(ns0.datatypes.Structure):
    dummy: o6.Boolean


@o6.enumtype(nodeId="ns=safety;i=3005", browseName="InFlagsType", description="Byte with Non safety Flags from SafetyConsumer")
class InFlagsType:
    COMMUNICATION_ERROR = o6.enumfield(0, name="CommunicationError")
    OPERATOR_ACK_REQUESTED = o6.enumfield(1, name="OperatorAckRequested")
    FSV__ACTIVATED = o6.enumfield(2, name="FSV_Activated")


@o6.datatype(nodeId="ns=safety;i=3003", browseName="RequestSPDUDataType", defaultEncodingId="ns=safety;i=5010")
class RequestSPDUDataType(ns0.datatypes.Structure):
    inSafetyConsumerID: o6.UInt32
    inMonitoringNumber: o6.UInt32
    inFlags: InFlagsType


@o6.enumtype(nodeId="ns=safety;i=3006", browseName="OutFlagsType", description="Byte with Safety Flags from SafetyProvider")
class OutFlagsType:
    OPERATOR_ACK_PROVIDER = o6.enumfield(0, name="OperatorAckProvider")
    ACTIVATE_FSV = o6.enumfield(1, name="ActivateFSV")
    TEST_MODE_ACTIVATED = o6.enumfield(2, name="TestModeActivated")


@o6.datatype(nodeId="ns=safety;i=3004", browseName="ResponseSPDUDataType", isAbstract=True)
class ResponseSPDUDataType(ns0.datatypes.Structure):
    outFlags: OutFlagsType
    outSPDU_ID_1: o6.UInt32
    outSPDU_ID_2: o6.UInt32
    outSPDU_ID_3: o6.UInt32
    outSafetyConsumerID: o6.UInt32
    outMonitoringNumber: o6.UInt32
    outCRC: o6.UInt32


del Any, TYPE_CHECKING, uuid, o6, ns0
