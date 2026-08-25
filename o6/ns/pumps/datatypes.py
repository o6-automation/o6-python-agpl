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

"""Generated OPC UA pumps namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=pumps;i=3003", browseName="StateOfTheItemEnum", description="describes the state of the pump")
class StateOfTheItemEnum(ns0.datatypes.Enumeration):
    IDLE_STATE = o6.enumfield(0, name="IdleState")
    STAND_BY_STATE = o6.enumfield(1, name="StandByState")
    OPERATING_STATE = o6.enumfield(2, name="OperatingState")
    EXTERNAL_DISABLED_STATE = o6.enumfield(3, name="ExternalDisabledState")
    DOWN_STATE = o6.enumfield(4, name="DownState")


@o6.enumtype(nodeId="ns=pumps;i=3004", browseName="MaintenanceLevelEnum", description="defines maintenance levels for the pump")
class MaintenanceLevelEnum(ns0.datatypes.Enumeration):
    LEVEL1 = o6.enumfield(0, name="Level1")
    LEVEL2 = o6.enumfield(1, name="Level2")
    LEVEL3 = o6.enumfield(2, name="Level3")
    LEVEL4 = o6.enumfield(3, name="Level4")
    LEVEL5 = o6.enumfield(4, name="Level5")


@o6.enumtype(nodeId="ns=pumps;i=3005", browseName="FieldbusEnum", description="defines possible field buses")
class FieldbusEnum(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="Other")
    ARCNET = o6.enumfield(1, name="ARCNET")
    AS__INTERFACE = o6.enumfield(2, name="AS-Interface")
    BA_CNET_IP = o6.enumfield(3, name="BACnet/IP")
    BA_CNET_MSTP = o6.enumfield(4, name="BACnet/MSTP")
    BLUETOOTH = o6.enumfield(5, name="Bluetooth")
    BLUETOOTH_LOW_ENERGY = o6.enumfield(6, name="BluetoothLowEnergy")
    CAN = o6.enumfield(7, name="CAN")
    CA_NOPEN = o6.enumfield(8, name="CANopen")
    CC__LINK = o6.enumfield(9, name="CC-Link")
    CONTROL_NET = o6.enumfield(10, name="ControlNet")
    DALI = o6.enumfield(11, name="DALI")
    DECTULE = o6.enumfield(12, name="DECTULE")
    DEVICE_NET = o6.enumfield(13, name="DeviceNet")
    DMX = o6.enumfield(14, name="DMX")
    KNX = o6.enumfield(15, name="KNX")
    EN_OCEAN = o6.enumfield(16, name="EnOcean")
    ETHER_CAT = o6.enumfield(17, name="EtherCAT")
    ETHERNET_IP = o6.enumfield(18, name="Ethernet/IP")
    ETHERNET_TCP_IP = o6.enumfield(19, name="EthernetTCP/IP")
    IEEE1588 = o6.enumfield(20, name="IEEE1588")
    GSM = o6.enumfield(21, name="GSM")
    INTERBUS = o6.enumfield(22, name="Interbus")
    IO__LINK = o6.enumfield(23, name="IO-Link")
    HART = o6.enumfield(24, name="HART")
    LON = o6.enumfield(25, name="LON")
    LO_RA_WAN = o6.enumfield(26, name="LoRaWAN")
    LIN__BUS = o6.enumfield(27, name="LIN-Bus")
    LTE = o6.enumfield(28, name="LTE")
    LTE_M = o6.enumfield(29, name="LTE-M")
    M__BUS = o6.enumfield(30, name="M-Bus")
    MODBUS_TCP = o6.enumfield(31, name="ModbusTCP")
    MODBUS_RTU = o6.enumfield(32, name="ModbusRTU")
    MP__BUS = o6.enumfield(33, name="MP-Bus")
    NB_IOT = o6.enumfield(34, name="NB-IOT")
    NFC = o6.enumfield(35, name="NFC")
    OPCUA = o6.enumfield(36, name="OPCUA")
    OPCDA = o6.enumfield(37, name="OPCDA")
    PROFIBUSDP = o6.enumfield(38, name="PROFIBUSDP")
    PROFINETRT = o6.enumfield(39, name="PROFINETRT")
    POWERLINK = o6.enumfield(40, name="Powerlink")
    SERCOS = o6.enumfield(41, name="SERCOS")
    SMI = o6.enumfield(42, name="SMI")
    THREAD = o6.enumfield(43, name="Thread")
    UMTS = o6.enumfield(44, name="UMTS")
    WIFI = o6.enumfield(45, name="WIFI")
    X2_X__LINK = o6.enumfield(46, name="X2X-Link")
    VARAN = o6.enumfield(47, name="VARAN")
    ZIG_BEE = o6.enumfield(48, name="ZigBee")
    Z__WAVE = o6.enumfield(49, name="Z-Wave")


@o6.enumtype(nodeId="ns=pumps;i=3006", browseName="OperatingModeEnum", description="specifies whether the pump is to be operated in single, parallel or series connection")
class OperatingModeEnum(ns0.datatypes.Enumeration):
    SINGLE_OPERATION = o6.enumfield(0, name="SingleOperation")
    SERIES_OPERATION = o6.enumfield(1, name="SeriesOperation")
    PARALLEL_OPERATION = o6.enumfield(2, name="ParallelOperation")


@o6.enumtype(nodeId="ns=pumps;i=3007", browseName="OperationModeEnum", description="describes the possible operation modes of the pump")
class OperationModeEnum(ns0.datatypes.Enumeration):
    AUTO_CONTROL = o6.enumfield(0, name="AutoControl")
    CLOSED_LOOP_STANDARD_PID = o6.enumfield(1, name="ClosedLoopStandardPID")
    ADVANCED = o6.enumfield(2, name="Advanced")
    STAND_BY = o6.enumfield(3, name="StandBy")
    OPEN_LOOP_MIN = o6.enumfield(4, name="OpenLoopMin")
    OPEN_LOOP_VALUE = o6.enumfield(5, name="OpenLoopValue")
    OPEN_LOOP_MAX = o6.enumfield(6, name="OpenLoopMax")
    CLOSED_LOOP_MIN = o6.enumfield(7, name="ClosedLoopMin")
    CLOSED_LOOP_MAX = o6.enumfield(8, name="ClosedLoopMax")
    TEST = o6.enumfield(9, name="Test")
    CALIBRATION = o6.enumfield(10, name="Calibration")


@o6.enumtype(nodeId="ns=pumps;i=3008", browseName="ControlModeEnum", description="describes the possible control modes of the pump")
class ControlModeEnum(ns0.datatypes.Enumeration):
    CONSTANT_PRESSURE_CONTROL = o6.enumfield(0, name="ConstantPressureControl")
    CONSTANT_TEMPERATURE_CONTROL = o6.enumfield(1, name="ConstantTemperatureControl")
    DIFFERENTIAL_PRESSURE_CONTROL = o6.enumfield(2, name="DifferentialPressureControl")
    CONSTANT_DIFFERENTIAL_PRESSURE_CONTROL = o6.enumfield(3, name="ConstantDifferentialPressureControl")
    VARIABLE_DIFFERENTIAL_PRESSURE_CONTROL = o6.enumfield(4, name="VariableDifferentialPressureControl")
    FLOW_DEPENDENT_DIFFERENTIAL_PRESSURE_CONTROL = o6.enumfield(5, name="FlowDependentDifferentialPressureControl")
    RETURN_FLOW_TEMPERATURE_CONTROL = o6.enumfield(6, name="ReturnFlowTemperatureControl")
    FLOW_TEMPERATURE_CONTROL = o6.enumfield(7, name="FlowTemperatureControl")
    FLOW_RATE_CONTROL = o6.enumfield(8, name="FlowRateControl")
    SPEED_CONTROL = o6.enumfield(9, name="SpeedControl")
    AUTOMATIC = o6.enumfield(10, name="Automatic")
    UNCONTROLLED = o6.enumfield(11, name="Uncontrolled")


@o6.enumtype(nodeId="ns=pumps;i=3009", browseName="PumpKickModeEnum", description="describes the pump kick mode of the pump")
class PumpKickModeEnum(ns0.datatypes.Enumeration):
    MANUFACTURER_SPECIFIC = o6.enumfield(0, name="ManufacturerSpecific")
    DISABLED = o6.enumfield(1, name="Disabled")
    OPERATOR_SPECIFIC = o6.enumfield(2, name="OperatorSpecific")


@o6.enumtype(nodeId="ns=pumps;i=3010", browseName="PumpRoleEnum", description="identifies the role rsp. task of the pump within the multi pump management")
class PumpRoleEnum(ns0.datatypes.Enumeration):
    SLAVE = o6.enumfield(0, name="Slave")
    MASTER = o6.enumfield(1, name="Master")
    SLAVE_AND_AUXILIARY_MASTER = o6.enumfield(2, name="SlaveAndAuxiliaryMaster")


@o6.enumtype(nodeId="ns=pumps;i=3011", browseName="MultiPumpOperationModeEnum", description="specifies the actual multi pump operation mode")
class MultiPumpOperationModeEnum(ns0.datatypes.Enumeration):
    STANDALONE = o6.enumfield(0, name="Standalone")
    REDUNDANCY_OPERATION = o6.enumfield(1, name="RedundancyOperation")
    ADDITION_OPERATION = o6.enumfield(2, name="AdditionOperation")
    MIXED_REDUNDANCY = o6.enumfield(3, name="MixedRedundancy")


@o6.enumtype(nodeId="ns=pumps;i=3012", browseName="ExchangeModeEnum", description="specifies the exchange mode of the pump")
class ExchangeModeEnum(ns0.datatypes.Enumeration):
    MANUFACTURER_SPECIFIC = o6.enumfield(0, name="ManufacturerSpecific")
    EXCHANGE_DISABLED = o6.enumfield(1, name="ExchangeDisabled")
    OPERATOR_SPECIFIC = o6.enumfield(2, name="OperatorSpecific")


@o6.enumtype(
    nodeId="ns=pumps;i=3013",
    browseName="DistributionTypeEnum",
    description="describes the share of operation time of different pumps of the pump system in addition operation mode",
)
class DistributionTypeEnum(ns0.datatypes.Enumeration):
    MANUFACTURER_SPECIFIC = o6.enumfield(0, name="ManufacturerSpecific")
    OPERATOR_SPECIFIC = o6.enumfield(1, name="OperatorSpecific")
    CONCERNING_TIME_DISTRIBUTION = o6.enumfield(2, name="ConcerningTimeDistribution")
    CONCERNING_LOAD_DISTRIBUTION = o6.enumfield(3, name="ConcerningLoadDistribution")


@o6.enumtype(nodeId="ns=pumps;i=3014", browseName="PortDirectionEnum", description="determines whether the port is an inlet and outlet or both")
class PortDirectionEnum(ns0.datatypes.Enumeration):
    IN = o6.enumfield(0, name="In")
    OUT = o6.enumfield(1, name="Out")
    IN_OUT = o6.enumfield(2, name="InOut")


@o6.datatype(
    nodeId="ns=pumps;i=3015", browseName="ExplosionZoneOptionSet", description="defines flags for the category of explosion zones for devices", defaultEncodingId="ns=pumps;i=5001"
)
class ExplosionZoneOptionSet(ns0.datatypes.OptionSet):
    value: o6.ByteString
    validBits: o6.ByteString


@o6.datatype(
    nodeId="ns=pumps;i=3016",
    browseName="ExplosionProtectionOptionSet",
    description="defines flags for the category of explosion protection for devices according to EU Directive 2014/34/EU (ATEX)",
    defaultEncodingId="ns=pumps;i=5004",
)
class ExplosionProtectionOptionSet(ns0.datatypes.OptionSet):
    value: o6.ByteString
    validBits: o6.ByteString


@o6.datatype(
    nodeId="ns=pumps;i=3017",
    browseName="OfferedControlModesOptionSet",
    description="defines flags for offerd control modes supported by the manufacturer for the product",
    defaultEncodingId="ns=pumps;i=5007",
)
class OfferedControlModesOptionSet(ns0.datatypes.OptionSet):
    value: o6.ByteString
    validBits: o6.ByteString


@o6.datatype(
    nodeId="ns=pumps;i=3018",
    browseName="OfferedFieldbusesOptionSet",
    description="defines flags for fieldbuses supported by the manufacturer for the product",
    defaultEncodingId="ns=pumps;i=5010",
)
class OfferedFieldbusesOptionSet(ns0.datatypes.OptionSet):
    value: o6.ByteString
    validBits: o6.ByteString


@o6.datatype(
    nodeId="ns=pumps;i=3019",
    browseName="DeclarationOfConformityOptionSet",
    description="defines flags for directives on the basis of which conformity was determined",
    defaultEncodingId="ns=pumps;i=5013",
)
class DeclarationOfConformityOptionSet(ns0.datatypes.OptionSet):
    value: o6.ByteString
    validBits: o6.ByteString


@o6.datatype(nodeId="ns=pumps;i=3020", browseName="PhysicalAddressDataType", description="Physical address of the manufacturer.", defaultEncodingId="ns=pumps;i=5016")
class PhysicalAddressDataType(ns0.datatypes.Structure):
    street: o6.LocalizedText | None
    number: o6.LocalizedText | None
    city: o6.LocalizedText | None
    postalCode: o6.LocalizedText | None
    state: o6.LocalizedText | None
    country: o6.LocalizedText | None


@o6.enumtype(nodeId="ns=pumps;i=3021", browseName="PumpClassEnum", description="defines possible pump types")
class PumpClassEnum(ns0.datatypes.Enumeration):
    ROTODYNAMIC_PUMP = o6.enumfield(0, name="RotodynamicPump")
    POSITIVE_DISPLACEMENT_PUMP = o6.enumfield(1, name="PositiveDisplacementPump")
    PROCESS_VACUUM_PUMP = o6.enumfield(2, name="ProcessVacuumPump")
    TURBO_VACUUM_PUMP = o6.enumfield(3, name="TurboVacuumPump")
    VACUUM_PUMP = o6.enumfield(4, name="VacuumPump")
    LIQUID_PUMP = o6.enumfield(5, name="LiquidPump")
    PUMP = o6.enumfield(6, name="Pump")


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0
