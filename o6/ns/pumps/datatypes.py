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
    zoneSpace0 = o6.optionsetbit(0, name="Zone 0")
    zoneSpace1 = o6.optionsetbit(1, name="Zone 1")
    zoneSpace2 = o6.optionsetbit(2, name="Zone 2")
    zoneSpace20 = o6.optionsetbit(3, name="Zone 20")
    zoneSpace21 = o6.optionsetbit(4, name="Zone 21")
    zoneSpace22 = o6.optionsetbit(5, name="Zone 22")


@o6.datatype(
    nodeId="ns=pumps;i=3016",
    browseName="ExplosionProtectionOptionSet",
    description="defines flags for the category of explosion protection for devices according to EU Directive 2014/34/EU (ATEX)",
    defaultEncodingId="ns=pumps;i=5004",
)
class ExplosionProtectionOptionSet(ns0.datatypes.OptionSet):
    value: o6.ByteString
    validBits: o6.ByteString
    m1 = o6.optionsetbit(0, name="M1")
    m2 = o6.optionsetbit(1, name="M2")
    oneG = o6.optionsetbit(2, name="1G")
    twoG = o6.optionsetbit(3, name="2G")
    threeG = o6.optionsetbit(4, name="3G")
    oneD = o6.optionsetbit(5, name="1D")
    twoD = o6.optionsetbit(6, name="2D")
    threeD = o6.optionsetbit(7, name="3D")


@o6.datatype(
    nodeId="ns=pumps;i=3017",
    browseName="OfferedControlModesOptionSet",
    description="defines flags for offerd control modes supported by the manufacturer for the product",
    defaultEncodingId="ns=pumps;i=5007",
)
class OfferedControlModesOptionSet(ns0.datatypes.OptionSet):
    value: o6.ByteString
    validBits: o6.ByteString
    constantSpacePressureSpaceControl = o6.optionsetbit(0, name="Constant pressure control")
    constantSpaceTemperatureSpaceControl = o6.optionsetbit(1, name="Constant temperature control")
    differentialSpacePressureSpaceControl = o6.optionsetbit(2, name="Differential pressure control")
    constantSpaceDifferentialSpacePressureSpaceControl = o6.optionsetbit(3, name="Constant differential pressure control")
    variableSpaceDifferentialSpacePressureSpaceControl = o6.optionsetbit(4, name="Variable differential pressure control")
    flow_dependentSpaceDifferentialSpacePressureSpaceControl = o6.optionsetbit(5, name="Flow_dependent differential pressure control")
    returnSpaceFlowSpaceTemperatureSpaceControl = o6.optionsetbit(6, name="Return flow temperature control")
    flowSpaceTemperatureSpaceControl = o6.optionsetbit(7, name="Flow temperature control")
    flowSpaceRateSpaceControl = o6.optionsetbit(8, name="Flow rate control")
    automatic = o6.optionsetbit(9, name="Automatic")
    uncontrolled = o6.optionsetbit(10, name="Uncontrolled")
    speedSpaceControl = o6.optionsetbit(11, name="Speed control")


@o6.datatype(
    nodeId="ns=pumps;i=3018",
    browseName="OfferedFieldbusesOptionSet",
    description="defines flags for fieldbuses supported by the manufacturer for the product",
    defaultEncodingId="ns=pumps;i=5010",
)
class OfferedFieldbusesOptionSet(ns0.datatypes.OptionSet):
    value: o6.ByteString
    validBits: o6.ByteString
    other = o6.optionsetbit(0, name="Other")
    aRCNET = o6.optionsetbit(1, name="ARCNET")
    aS_Interface = o6.optionsetbit(2, name="AS_Interface")
    bACnet_IP = o6.optionsetbit(3, name="BACnet_IP")
    bACnet_MSTP = o6.optionsetbit(4, name="BACnet_MSTP")
    bluetooth = o6.optionsetbit(5, name="Bluetooth")
    bluetoothSpaceLowSpaceEnergy = o6.optionsetbit(6, name="Bluetooth Low Energy")
    cAN = o6.optionsetbit(7, name="CAN")
    cANopen = o6.optionsetbit(8, name="CANopen")
    cC_Link = o6.optionsetbit(9, name="CC_Link")
    controlNet = o6.optionsetbit(10, name="ControlNet")
    dALI = o6.optionsetbit(11, name="DALI")
    dECTSpaceULE = o6.optionsetbit(12, name="DECT ULE")
    deviceNet = o6.optionsetbit(13, name="DeviceNet")
    dMX = o6.optionsetbit(14, name="DMX")
    kNX = o6.optionsetbit(15, name="KNX")
    enOcean = o6.optionsetbit(16, name="EnOcean")
    etherCAT = o6.optionsetbit(17, name="EtherCAT")
    ethernet_IP = o6.optionsetbit(18, name="Ethernet_IP")
    ethernetSpaceTCP_IP = o6.optionsetbit(19, name="Ethernet TCP_IP")
    iEEE1588 = o6.optionsetbit(20, name="IEEE1588")
    gSM = o6.optionsetbit(21, name="GSM")
    interbus = o6.optionsetbit(22, name="Interbus")
    iO_Link = o6.optionsetbit(23, name="IO_Link")
    hART = o6.optionsetbit(24, name="HART")
    lON = o6.optionsetbit(25, name="LON")
    loRaWAN = o6.optionsetbit(26, name="LoRaWAN")
    lIN_Bus = o6.optionsetbit(27, name="LIN_Bus")
    lTE = o6.optionsetbit(28, name="LTE")
    lTE_M = o6.optionsetbit(29, name="LTE_M")
    m_Bus = o6.optionsetbit(30, name="M_Bus")
    modbusSpaceTCP = o6.optionsetbit(31, name="Modbus TCP")
    modbusSpaceRTU = o6.optionsetbit(32, name="Modbus RTU")
    mP_Bus = o6.optionsetbit(33, name="MP_Bus")
    nB_IOT = o6.optionsetbit(34, name="NB_IOT")
    nFC = o6.optionsetbit(35, name="NFC")
    oPCSpaceUA = o6.optionsetbit(36, name="OPC UA")
    oPCSpaceDA = o6.optionsetbit(37, name="OPC DA")
    pROFIBUSSpaceDP = o6.optionsetbit(38, name="PROFIBUS DP")
    pROFINETSpaceRT = o6.optionsetbit(39, name="PROFINET RT")
    powerlink = o6.optionsetbit(40, name="Powerlink")
    sERCOS = o6.optionsetbit(41, name="SERCOS")
    sMI = o6.optionsetbit(42, name="SMI")
    thread = o6.optionsetbit(43, name="Thread")
    uMTS = o6.optionsetbit(44, name="UMTS")
    wIFI = o6.optionsetbit(45, name="WIFI")
    x2X_Link = o6.optionsetbit(46, name="X2X_Link")
    vARAN = o6.optionsetbit(47, name="VARAN")
    zigBee = o6.optionsetbit(48, name="ZigBee")
    z_Wave = o6.optionsetbit(49, name="Z_Wave")


@o6.datatype(
    nodeId="ns=pumps;i=3019",
    browseName="DeclarationOfConformityOptionSet",
    description="defines flags for directives on the basis of which conformity was determined",
    defaultEncodingId="ns=pumps;i=5013",
)
class DeclarationOfConformityOptionSet(ns0.datatypes.OptionSet):
    value: o6.ByteString
    validBits: o6.ByteString
    two006_42_EC = o6.optionsetbit(0, name="2006_42_EC")
    two009_125_EC = o6.optionsetbit(1, name="2009_125_EC")
    two011_65_EU = o6.optionsetbit(2, name="2011_65_EU")
    two014_35_EU = o6.optionsetbit(3, name="2014_35_EU")
    two014_34_EU = o6.optionsetbit(4, name="2014_34_EU")
    two014_30_EU = o6.optionsetbit(5, name="2014_30_EU")
    two014_68_EU = o6.optionsetbit(6, name="2014_68_EU")
    two014_29_EU = o6.optionsetbit(7, name="2014_29_EU")


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
