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

from typing import Any, Sequence, SupportsFloat

import numpy as np

_Integer = int | np.integer[Any]

_Boolean = bool | np.bool_

import enum

from o6.node import ObjectNode as _ObjectNode, VariableNode as _VariableNode

import uuid

import o6

import o6.ns.ns0 as ns0

class NonSafetyDataPlaceholderDataType(ns0.datatypes.Structure):
    """Dummy structure to be used when no non-safety data are used"""

    @property
    def dummy(self) -> o6.Boolean: ...
    @dummy.setter
    def dummy(self, value: _Boolean) -> None: ...

class InFlagsType(enum.IntFlag):
    """Byte with Non safety Flags from SafetyConsumer"""

    COMMUNICATION_ERROR = 0
    OPERATOR_ACK_REQUESTED = 1
    FSV__ACTIVATED = 2

class RequestSPDUDataType(ns0.datatypes.Structure):
    @property
    def inSafetyConsumerID(self) -> o6.UInt32: ...
    @inSafetyConsumerID.setter
    def inSafetyConsumerID(self, value: _Integer) -> None: ...
    @property
    def inMonitoringNumber(self) -> o6.UInt32: ...
    @inMonitoringNumber.setter
    def inMonitoringNumber(self, value: _Integer) -> None: ...
    @property
    def inFlags(self) -> InFlagsType: ...
    @inFlags.setter
    def inFlags(self, value: _Integer) -> None: ...

class OutFlagsType(enum.IntFlag):
    """Byte with Safety Flags from SafetyProvider"""

    OPERATOR_ACK_PROVIDER = 0
    ACTIVATE_FSV = 1
    TEST_MODE_ACTIVATED = 2

class ResponseSPDUDataType(ns0.datatypes.Structure):
    @property
    def outFlags(self) -> OutFlagsType: ...
    @outFlags.setter
    def outFlags(self, value: _Integer) -> None: ...
    @property
    def outSPDU_ID_1(self) -> o6.UInt32: ...
    @outSPDU_ID_1.setter
    def outSPDU_ID_1(self, value: _Integer) -> None: ...
    @property
    def outSPDU_ID_2(self) -> o6.UInt32: ...
    @outSPDU_ID_2.setter
    def outSPDU_ID_2(self, value: _Integer) -> None: ...
    @property
    def outSPDU_ID_3(self) -> o6.UInt32: ...
    @outSPDU_ID_3.setter
    def outSPDU_ID_3(self, value: _Integer) -> None: ...
    @property
    def outSafetyConsumerID(self) -> o6.UInt32: ...
    @outSafetyConsumerID.setter
    def outSafetyConsumerID(self, value: _Integer) -> None: ...
    @property
    def outMonitoringNumber(self) -> o6.UInt32: ...
    @outMonitoringNumber.setter
    def outMonitoringNumber(self, value: _Integer) -> None: ...
    @property
    def outCRC(self) -> o6.UInt32: ...
    @outCRC.setter
    def outCRC(self, value: _Integer) -> None: ...
