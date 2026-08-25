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

"""Generated OPC UA pnenc namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=pnenc;i=3002", browseName="EncoderChannelStateEnumeration")
class EncoderChannelStateEnumeration(ns0.datatypes.Enumeration):
    NORMAL_OPERATION = o6.enumfield(0, name="NORMAL_OPERATION")
    ERROR_ACKNOWLEDGEMENT = o6.enumfield(1, name="ERROR_ACKNOWLEDGEMENT")
    ERROR = o6.enumfield(2, name="ERROR")
    REFERENCE_VALUE__GX_XIST2 = o6.enumfield(3, name="REFERENCE_VALUE_Gx_XIST2")
    WAIT_FOR_REFERENCE_MARKS = o6.enumfield(4, name="WAIT_FOR_REFERENCE_MARKS")
    SET_SHIFT_HOME_POSITION = o6.enumfield(5, name="SET_SHIFT_HOME_POSITION")
    WAIT_FOR_MEASURED_VALUE = o6.enumfield(6, name="WAIT_FOR_MEASURED_VALUE")
    MEASURED_VALUE_IN_XIST2 = o6.enumfield(7, name="MEASURED_VALUE_IN_XIST2")
    PARKING = o6.enumfield(8, name="PARKING")
    PARKING_ERROR = o6.enumfield(9, name="PARKING_ERROR")
    PARKING_ERROR_ACK = o6.enumfield(10, name="PARKING_ERROR_ACK")


@o6.enumtype(nodeId="ns=pnenc;i=3003", browseName="EventTypeEnumeration")
class EventTypeEnumeration(ns0.datatypes.Enumeration):
    FAULT = o6.enumfield(0, name="FAULT")
    WARNING = o6.enumfield(1, name="WARNING")
    UNSPECIFIED = o6.enumfield(255, name="UNSPECIFIED")


@o6.enumtype(nodeId="ns=pnenc;i=3004", browseName="EncoderAxisTypeEnumeration")
class EncoderAxisTypeEnumeration(ns0.datatypes.Enumeration):
    ROTARY = o6.enumfield(0, name="ROTARY")
    LINEAR = o6.enumfield(1, name="LINEAR")


@o6.enumtype(nodeId="ns=pnenc;i=3005", browseName="EncoderCodeSequenceEnumeration")
class EncoderCodeSequenceEnumeration(ns0.datatypes.Enumeration):
    INCREASING_CLOCKWISE = o6.enumfield(0, name="INCREASING_CLOCKWISE")
    INCREASING_COUNTERCLOCKWISE = o6.enumfield(1, name="INCREASING_COUNTERCLOCKWISE")


@o6.enumtype(nodeId="ns=pnenc;i=3006", browseName="EncoderAlarmChannelControlEnumeration")
class EncoderAlarmChannelControlEnumeration(ns0.datatypes.Enumeration):
    ALARM_CHANNEL_DISABLED = o6.enumfield(0, name="ALARM_CHANNEL_DISABLED")
    ALARM_CHANNEL_ENABLED = o6.enumfield(1, name="ALARM_CHANNEL_ENABLED")


@o6.enumtype(nodeId="ns=pnenc;i=3007", browseName="EncoderPresetControlEnumeration")
class EncoderPresetControlEnumeration(ns0.datatypes.Enumeration):
    ENABLE_PRESET_CONTROL = o6.enumfield(0, name="ENABLE_PRESET_CONTROL")
    DISABLE_PRESET_CONTROL = o6.enumfield(1, name="DISABLE_PRESET_CONTROL")


@o6.enumtype(nodeId="ns=pnenc;i=3008", browseName="EncoderSensorAbsoluteTypeEnumeration")
class EncoderSensorAbsoluteTypeEnumeration(ns0.datatypes.Enumeration):
    SINGLETURN = o6.enumfield(0, name="SINGLETURN")
    MULTITURN = o6.enumfield(1, name="MULTITURN")


@o6.enumtype(nodeId="ns=pnenc;i=3009", browseName="EncoderSignalTypeEnumeration")
class EncoderSignalTypeEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    BISS_C = o6.enumfield(1, name="BISS_C")
    ENDAT2_1 = o6.enumfield(2, name="ENDAT2.1")
    ENDAT2_2 = o6.enumfield(3, name="ENDAT2.2")
    HIPERFACE = o6.enumfield(4, name="HIPERFACE")
    HIPERFACE_DSL = o6.enumfield(5, name="HIPERFACE_DSL")
    SSI_BINARY = o6.enumfield(6, name="SSI_BINARY")
    SSI_GRAY_CODE = o6.enumfield(7, name="SSI_GRAY_CODE")
    SINCOS_1_VSS = o6.enumfield(8, name="SINCOS_1VSS")
    SCS_OPEN_LINK = o6.enumfield(9, name="SCS_OPEN_LINK")
    DRIVECLIQ = o6.enumfield(10, name="DRIVECLIQ")
    BISS_LINE = o6.enumfield(11, name="BISS_LINE")
    FANUC_37_BIT_SERIAL_COMM = o6.enumfield(12, name="FANUC_37BIT_SERIAL_COMM")
    MITSUBISHI_40_BIT_SERIAL_COMM = o6.enumfield(13, name="MITSUBISHI_40BIT_SERIAL_COMM")
    OMRON_PANASONIC_48_BIT_SERIAL_COMM = o6.enumfield(14, name="OMRON/PANASONIC_48BIT_SERIAL_COMM")
    YASKAWA_36_BIT_SERIAL_COMM = o6.enumfield(15, name="YASKAWA_36BIT_SERIAL_COMM")
    RS422_5_V_TTL = o6.enumfield(16, name="RS422_5V_TTL")
    RS422_5__30_V = o6.enumfield(17, name="RS422_5..30V")
    SINCOS_1_VPP = o6.enumfield(18, name="SINCOS_1VPP")
    RESOLVER = o6.enumfield(19, name="RESOLVER")
    HTL_PUSH_PULL = o6.enumfield(20, name="HTL_PUSH-PULL")
    RS485 = o6.enumfield(21, name="RS485")
    RS485_SINCOS = o6.enumfield(22, name="RS485_SINCOS")
    RS485_HTL = o6.enumfield(23, name="RS485_HTL")
    RS485_TTL = o6.enumfield(24, name="RS485_TTL")


@o6.enumtype(nodeId="ns=pnenc;i=3010", browseName="EncoderConfigParameterResultEnumeration")
class EncoderConfigParameterResultEnumeration(ns0.datatypes.Enumeration):
    INVALID = o6.enumfield(0, name="INVALID")
    NOT_SUPPORTED = o6.enumfield(1, name="NOT_SUPPORTED")
    READ_ONLY = o6.enumfield(2, name="READ_ONLY")


@o6.enumtype(nodeId="ns=pnenc;i=3011", browseName="EncoderConfigTypeEnumeration")
class EncoderConfigTypeEnumeration(ns0.datatypes.Enumeration):
    STATIC = o6.enumfield(0, name="STATIC")
    DYNAMIC = o6.enumfield(1, name="DYNAMIC")


@o6.enumtype(nodeId="ns=pnenc;i=3012", browseName="EncoderDiagnosisReasonEnumeration")
class EncoderDiagnosisReasonEnumeration(ns0.datatypes.Enumeration):
    ALL_DISAPPEARS = o6.enumfield(0, name="ALL_DISAPPEARS")
    APPEARS = o6.enumfield(1, name="APPEARS")
    DISAPPEARS = o6.enumfield(2, name="DISAPPEARS")
    DISAPPEARS_OTHER_REMAIN = o6.enumfield(3, name="DISAPPEARS_OTHER_REMAIN")


@o6.datatype(nodeId="ns=pnenc;i=3013", browseName="LogEntryDataType", defaultEncodingId="ns=pnenc;i=5002")
class LogEntryDataType(ns0.datatypes.Structure):
    faultSituationNumber: o6.Byte
    eventNumber: o6.UInt32
    eventType: EventTypeEnumeration
    eventCode: o6.Int32
    eventText: o6.LocalizedText
    eventComing: o6.DateTime
    eventGoing: o6.DateTime
    eventAcknowledged: o6.DateTime


del Any, TYPE_CHECKING, uuid, o6, di, ns0
