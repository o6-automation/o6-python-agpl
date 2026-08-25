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

"""Generated OPC UA pnrio namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as pnrio_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=pnrio;i=3002", browseName="PnIoTelegramStatusEnumeration")
class PnIoTelegramStatusEnumeration(ns0.datatypes.Enumeration):
    GOOD = o6.enumfield(0, name="GOOD")
    BAD_BY_SUBSLOT = o6.enumfield(1, name="BAD_BY_SUBSLOT")
    BAD_BY_SLOT = o6.enumfield(2, name="BAD_BY_SLOT")
    BAD_BY_DEVICE = o6.enumfield(3, name="BAD_BY_DEVICE")
    BAD_BY_CONTROLLER = o6.enumfield(4, name="BAD_BY_CONTROLLER")


@o6.datatype(nodeId="ns=pnrio;i=3003", browseName="RioPaDigitalValueDataType", defaultEncodingId="ns=pnrio;i=5055")
class RioPaDigitalValueDataType(ns0.datatypes.Structure):
    value: o6.Boolean
    qualifier: o6.Byte


@o6.datatype(nodeId="ns=pnrio;i=3004", browseName="RioFaDigitalValueDataType", defaultEncodingId="ns=pnrio;i=5058")
class RioFaDigitalValueDataType(ns0.datatypes.Structure):
    value: o6.Boolean
    qualifier: o6.Boolean


@o6.enumtype(nodeId="ns=pnrio;i=3005", browseName="RioSignalTypeEnumeration")
class RioSignalTypeEnumeration(ns0.datatypes.Enumeration):
    CURRENT_4_20_M_A = o6.enumfield(0, name="CURRENT-4-20_mA")
    CURRENT_0_20_M_A = o6.enumfield(1, name="CURRENT-0-20_mA")
    VOLTAGE_0_10_V = o6.enumfield(2, name="VOLTAGE-0-10_V")
    VOLTAGE_10_10_V = o6.enumfield(3, name="VOLTAGE-10-10_V")
    HART = o6.enumfield(4, name="HART")
    DIGITAL_0_24_V = o6.enumfield(5, name="DIGITAL-0/24V")
    NAMUR = o6.enumfield(6, name="NAMUR")
    MANUFACTURER_SPECIFIC = o6.enumfield(7, name="MANUFACTURER_SPECIFIC")


@o6.enumtype(nodeId="ns=pnrio;i=3006", browseName="RioSubstitutePolicyEnumeration")
class RioSubstitutePolicyEnumeration(ns0.datatypes.Enumeration):
    USE_SUBSTITUTE_VALUE = o6.enumfield(0, name="USE_SUBSTITUTE_VALUE")
    USE_LAST_VALID_VALUE = o6.enumfield(1, name="USE_LAST_VALID_VALUE")
    USE_ACTUAL_VALUE = o6.enumfield(2, name="USE_ACTUAL_VALUE")
    UNSPECIFIED = o6.enumfield(255, name="Unspecified")


@o6.enumtype(nodeId="ns=pnrio;i=3007", browseName="RioChannelModeEnumeration")
class RioChannelModeEnumeration(ns0.datatypes.Enumeration):
    AUTO = o6.enumfield(0, name="AUTO")
    MANUAL = o6.enumfield(1, name="MANUAL")
    OUT_OF_SERVICE = o6.enumfield(2, name="OUT_OF_SERVICE")


@o6.enumtype(nodeId="ns=pnrio;i=3008", browseName="RioQualityEnumeration")
class RioQualityEnumeration(ns0.datatypes.Enumeration):
    GOOD = o6.enumfield(0, name="GOOD")
    UNCERTAIN = o6.enumfield(1, name="UNCERTAIN")
    BAD = o6.enumfield(2, name="BAD")
    UNSPECIFIED = o6.enumfield(255, name="UNSPECIFIED")


@o6.enumtype(nodeId="ns=pnrio;i=3009", browseName="RioSpecifierEnumeration")
class RioSpecifierEnumeration(ns0.datatypes.Enumeration):
    NORMAL = o6.enumfield(0, name="NORMAL")
    FAILURE = o6.enumfield(1, name="FAILURE")
    FUNCTION_CHECK = o6.enumfield(2, name="FUNCTION_CHECK")
    MAINTENANCE_REQUEST = o6.enumfield(3, name="MAINTENANCE_REQUEST")
    OUT_OF_SPECIFICATION = o6.enumfield(4, name="OUT_OF_SPECIFICATION")
    UNSPECIFIED = o6.enumfield(255, name="UNSPECIFIED")


@o6.enumtype(nodeId="ns=pnrio;i=3010", browseName="RioQualifierEnumeration")
class RioQualifierEnumeration(ns0.datatypes.Enumeration):
    BAD_NOT_SPECIFIC = o6.enumfield(0, name="BAD_NOT_SPECIFIC")
    BAD_NOT_CONNECTED = o6.enumfield(8, name="BAD_NOT_CONNECTED")
    BAD_NOT_CONNECTED_SIMULATION_ACTIVE = o6.enumfield(9, name="BAD_NOT_CONNECTED_SIMULATION_ACTIVE")
    BAD_PASSIVATED = o6.enumfield(32, name="BAD_PASSIVATED")
    BAD_PASSIVATED_SIMULATION_ACTIVE = o6.enumfield(33, name="BAD_PASSIVATED_SIMULATION_ACTIVE")
    BAD_MAINTENANCE_ALARM = o6.enumfield(36, name="BAD_MAINTENANCE_ALARM")
    BAD_MAINTENANCE_ALARM_SIMULATION_ACTIVE = o6.enumfield(37, name="BAD_MAINTENANCE_ALARM_SIMULATION_ACTIVE")
    BAD_PROCESS = o6.enumfield(40, name="BAD_PROCESS")
    BAD_PROCESS_SIMULATION_ACTIVE = o6.enumfield(41, name="BAD_PROCESS_SIMULATION_ACTIVE")
    BAD_FUNCTION_CHECK = o6.enumfield(60, name="BAD_FUNCTION_CHECK")
    BAD_FUNCTION_CHECK_SIMULATION_ACTIVE = o6.enumfield(61, name="BAD_FUNCTION_CHECK_SIMULATION_ACTIVE")
    UNCERTAIN_SUBSTITUTE_SET = o6.enumfield(72, name="UNCERTAIN_SUBSTITUTE_SET")
    UNCERTAIN_SUBSTITUTE_SET_SIMULATION_ACTIVE = o6.enumfield(73, name="UNCERTAIN_SUBSTITUTE_SET_SIMULATION_ACTIVE")
    UNCERTAIN_INITIAL_VALUE = o6.enumfield(76, name="UNCERTAIN_INITIAL_VALUE")
    UNCERTAIN_INITIAL_VALUE_SIMULATION_ACTIVE = o6.enumfield(77, name="UNCERTAIN_INITIAL_VALUE_SIMULATION_ACTIVE")
    UNCERTAIN_MAINTENANCE_DEMANDED = o6.enumfield(104, name="UNCERTAIN_MAINTENANCE_DEMANDED")
    UNCERTAIN_MAINTENANCE_DEMANDED_SIMULATION_ACTIVE = o6.enumfield(105, name="UNCERTAIN_MAINTENANCE_DEMANDED_SIMULATION_ACTIVE")
    UNCERTAIN_NO_MAINTENANCE = o6.enumfield(120, name="UNCERTAIN_NO_MAINTENANCE")
    UNCERTAIN_NO_MAINTENANCE_SIMULATION_ACTIVE = o6.enumfield(121, name="UNCERTAIN_NO_MAINTENANCE_SIMULATION_ACTIVE")
    GOOD = o6.enumfield(128, name="GOOD")
    GOOD_SIMULATION_ACTIVE = o6.enumfield(129, name="GOOD_SIMULATION_ACTIVE")
    UPDATE = o6.enumfield(130, name="UPDATE")
    GOOD_LOCAL_OVERRIDE = o6.enumfield(156, name="GOOD_LOCAL_OVERRIDE")
    GOOD_LOCAL_OVERRIDE_SIMULATION_ACTIVE = o6.enumfield(157, name="GOOD_LOCAL_OVERRIDE_SIMULATION_ACTIVE")
    GOOD_INITIATE_FAULT_STATE = o6.enumfield(160, name="GOOD_INITIATE_FAULT_STATE")
    GOOD_MAINTENANCE_REQUIRED = o6.enumfield(164, name="GOOD_MAINTENANCE_REQUIRED")
    GOOD_MAINTENANCE_REQUIRED_SIMULATION_ACTIVE = o6.enumfield(165, name="GOOD_MAINTENANCE_REQUIRED_SIMULATION_ACTIVE")
    GOOD_MAINTENANCE_DEMANDED = o6.enumfield(168, name="GOOD_MAINTENANCE_DEMANDED")
    GOOD_MAINTENANCE_DEMANDED_SIMULATION_ACTIVE = o6.enumfield(169, name="GOOD_MAINTENANCE_DEMANDED_SIMULATION_ACTIVE")
    GOOD_FUNCTION_CHECK = o6.enumfield(188, name="GOOD_FUNCTION_CHECK")
    GOOD_FUNCTION_CHECK_SIMULATION_ACTIVE = o6.enumfield(189, name="GOOD_FUNCTION_CHECK_SIMULATION_ACTIVE")
    UNSPECIFIED = o6.enumfield(255, name="UNSPECIFIED")


@o6.enumtype(nodeId="ns=pnrio;i=3011", browseName="RioChannelDiagnosisStatusEnumeration")
class RioChannelDiagnosisStatusEnumeration(ns0.datatypes.Enumeration):
    HI_LIM_EXCEEDED = o6.enumfield(0, name="HI_LIM_EXCEEDED")
    LO_LIM_EXCEEDED = o6.enumfield(1, name="LO_LIM_EXCEEDED")
    SIMULATION_ACTIVE = o6.enumfield(2, name="SIMULATION_ACTIVE")
    MODE_CHANGED = o6.enumfield(3, name="MODE_CHANGED")
    SUBSTITUTE_VALUE_USED = o6.enumfield(4, name="SUBSTITUTE_VALUE_USED")
    Q_BAD_SUBSTITUTE_VALUE_USED = o6.enumfield(5, name="Q_BAD_SUBSTITUTE_VALUE_USED")
    OUT_OF_SERVICE = o6.enumfield(6, name="OUT_OF_SERVICE")


@o6.datatype(nodeId="ns=pnrio;i=3012", browseName="RioPaDigitalInputConfigDataType", defaultEncodingId="ns=pnrio;i=5001")
class RioPaDigitalInputConfigDataType(ns0.datatypes.Structure):
    signalType: RioSignalTypeEnumeration
    wireCheckEnabled: o6.Boolean
    inversionEnabled: o6.Boolean
    substitutePolicy: RioSubstitutePolicyEnumeration
    substituteValue: o6.Boolean


@o6.datatype(nodeId="ns=pnrio;i=3013", browseName="RioFaDigitalInputConfigDataType", defaultEncodingId="ns=pnrio;i=5004")
class RioFaDigitalInputConfigDataType(ns0.datatypes.Structure):
    signalType: RioSignalTypeEnumeration
    wireCheckEnabled: o6.Boolean
    supplyVoltageCheckEnabled: o6.Boolean
    substitutePolicy: RioSubstitutePolicyEnumeration
    substituteValue: o6.Boolean


@o6.datatype(nodeId="ns=pnrio;i=3014", browseName="RioPaDigitalOutputConfigDataType", defaultEncodingId="ns=pnrio;i=5007")
class RioPaDigitalOutputConfigDataType(ns0.datatypes.Structure):
    signalType: RioSignalTypeEnumeration
    wireCheckEnabled: o6.Boolean
    inversionEnabled: o6.Boolean
    substitutePolicy: RioSubstitutePolicyEnumeration
    substituteValue: o6.Boolean
    substituteTime: o6.Float


@o6.datatype(nodeId="ns=pnrio;i=3015", browseName="RioFaDigitalOutputConfigDataType", defaultEncodingId="ns=pnrio;i=5010")
class RioFaDigitalOutputConfigDataType(ns0.datatypes.Structure):
    signalType: RioSignalTypeEnumeration
    wireCheckEnabled: o6.Boolean
    supplyVoltageCheckEnabled: o6.Boolean
    loadVoltageCheckEnabled: o6.Boolean
    substitutePolicy: RioSubstitutePolicyEnumeration
    substituteValue: o6.Boolean
    substituteTime: o6.Float


@o6.datatype(nodeId="ns=pnrio;i=3020", browseName="RioAnalogDataType", defaultEncodingId="ns=pnrio;i=5026")
class RioAnalogDataType(ns0.datatypes.Union):
    float_32: o6.Float
    int_16: o6.Int16
    int_32: o6.Int32
    uInt_16: o6.UInt16
    uInt_32: o6.UInt32


@o6.datatype(nodeId="ns=pnrio;i=3016", browseName="RioPaAnalogInputConfigDataType", defaultEncodingId="ns=pnrio;i=5013")
class RioPaAnalogInputConfigDataType(ns0.datatypes.Structure):
    damping: o6.Float
    signalType: RioSignalTypeEnumeration
    wireCheckEnabled: o6.Boolean
    substitutePolicy: RioSubstitutePolicyEnumeration
    substituteValue: RioAnalogDataType
    highLimit: RioAnalogDataType
    lowLimit: RioAnalogDataType


@o6.datatype(nodeId="ns=pnrio;i=3017", browseName="RioFaAnalogInputConfigDataType", defaultEncodingId="ns=pnrio;i=5016")
class RioFaAnalogInputConfigDataType(ns0.datatypes.Structure):
    damping: o6.Float
    signalType: RioSignalTypeEnumeration
    wireCheckEnabled: o6.Boolean
    supplyVoltageCheckEnabled: o6.Boolean
    substitutePolicy: RioSubstitutePolicyEnumeration
    substituteValue: RioAnalogDataType


@o6.datatype(nodeId="ns=pnrio;i=3018", browseName="RioPaAnalogOutputConfigDataType", defaultEncodingId="ns=pnrio;i=5019")
class RioPaAnalogOutputConfigDataType(ns0.datatypes.Structure):
    signalType: RioSignalTypeEnumeration
    wireCheckEnabled: o6.Boolean
    substitutePolicy: RioSubstitutePolicyEnumeration
    substituteValue: RioAnalogDataType
    substituteTime: o6.Float


@o6.datatype(nodeId="ns=pnrio;i=3019", browseName="RioFaAnalogOutputConfigDataType", defaultEncodingId="ns=pnrio;i=5022")
class RioFaAnalogOutputConfigDataType(ns0.datatypes.Structure):
    signalType: RioSignalTypeEnumeration
    wireCheckEnabled: o6.Boolean
    supplyVoltageCheckEnabled: o6.Boolean
    loadVoltageCheckEnabled: o6.Boolean
    substitutePolicy: RioSubstitutePolicyEnumeration
    substituteValue: RioAnalogDataType
    substituteTime: o6.Float


@o6.datatype(nodeId="ns=pnrio;i=3021", browseName="RioPaDigitalProcessValueDataType", defaultEncodingId="ns=pnrio;i=5028")
class RioPaDigitalProcessValueDataType(RioPaDigitalValueDataType):
    value: o6.Boolean
    qualifier: o6.Byte
    quality: o6.Byte
    nE_107: o6.Byte
    status_full: o6.Byte


@o6.datatype(nodeId="ns=pnrio;i=3022", browseName="RioFaDigitalProcessValueDataType", defaultEncodingId="ns=pnrio;i=5031")
class RioFaDigitalProcessValueDataType(RioFaDigitalValueDataType):
    value: o6.Boolean
    qualifier: o6.Boolean
    quality: o6.Byte


@o6.datatype(nodeId="ns=pnrio;i=3023", browseName="RioBitFieldDataType", defaultEncodingId="ns=pnrio;i=5035")
class RioBitFieldDataType(ns0.datatypes.Structure):
    bitData: o6.UInt32
    bitUsed: o6.UInt32


@o6.enumtype(nodeId="ns=pnrio;i=3026", browseName="RioChannelDiagnosisReasonEnumeration")
class RioChannelDiagnosisReasonEnumeration(ns0.datatypes.Enumeration):
    ALL_DISAPPEARS = o6.enumfield(0, name="ALL_DISAPPEARS")
    APPEARS = o6.enumfield(1, name="APPEARS")
    DISAPPEARS = o6.enumfield(2, name="DISAPPEARS")
    DISAPPEARS_OTHER_REMAIN = o6.enumfield(3, name="DISAPPEARS_OTHER_REMAIN")


@o6.datatype(nodeId="ns=pnrio;i=3027", browseName="RioPaAnalogValueDataType", defaultEncodingId="ns=pnrio;i=5061")
class RioPaAnalogValueDataType(ns0.datatypes.Structure):
    value: RioAnalogDataType
    qualifier: o6.Byte


@o6.datatype(nodeId="ns=pnrio;i=3024", browseName="RioPaAnalogProcessValueDataType", defaultEncodingId="ns=pnrio;i=5037")
class RioPaAnalogProcessValueDataType(RioPaAnalogValueDataType):
    value: RioAnalogDataType
    qualifier: o6.Byte
    quality: o6.Byte
    nE_107: o6.Byte
    status_full: o6.Byte


@o6.datatype(nodeId="ns=pnrio;i=3028", browseName="RioFaAnalogValueDataType", defaultEncodingId="ns=pnrio;i=5064")
class RioFaAnalogValueDataType(ns0.datatypes.Structure):
    value: RioAnalogDataType
    qualifier: o6.Boolean


@o6.datatype(nodeId="ns=pnrio;i=3025", browseName="RioFaAnalogProcessValueDataType", defaultEncodingId="ns=pnrio;i=5040")
class RioFaAnalogProcessValueDataType(RioFaAnalogValueDataType):
    value: RioAnalogDataType
    qualifier: o6.Boolean
    quality: o6.Byte


del Any, TYPE_CHECKING, uuid, o6, di, ns0, pnrio_reftypes
