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

import o6.ns.di as di

import o6.ns.ia as ia

import o6.ns.machinery as machinery

import o6.ns.ns0 as ns0

class StateOfTheItemEnum(enum.IntFlag):
    """describes the state of the pump"""

    IDLE_STATE = 0
    STAND_BY_STATE = 1
    OPERATING_STATE = 2
    EXTERNAL_DISABLED_STATE = 3
    DOWN_STATE = 4

class MaintenanceLevelEnum(enum.IntFlag):
    """defines maintenance levels for the pump"""

    LEVEL1 = 0
    LEVEL2 = 1
    LEVEL3 = 2
    LEVEL4 = 3
    LEVEL5 = 4

class FieldbusEnum(enum.IntFlag):
    """defines possible field buses"""

    OTHER = 0
    ARCNET = 1
    AS__INTERFACE = 2
    BA_CNET_IP = 3
    BA_CNET_MSTP = 4
    BLUETOOTH = 5
    BLUETOOTH_LOW_ENERGY = 6
    CAN = 7
    CA_NOPEN = 8
    CC__LINK = 9
    CONTROL_NET = 10
    DALI = 11
    DECTULE = 12
    DEVICE_NET = 13
    DMX = 14
    KNX = 15
    EN_OCEAN = 16
    ETHER_CAT = 17
    ETHERNET_IP = 18
    ETHERNET_TCP_IP = 19
    IEEE1588 = 20
    GSM = 21
    INTERBUS = 22
    IO__LINK = 23
    HART = 24
    LON = 25
    LO_RA_WAN = 26
    LIN__BUS = 27
    LTE = 28
    LTE_M = 29
    M__BUS = 30
    MODBUS_TCP = 31
    MODBUS_RTU = 32
    MP__BUS = 33
    NB_IOT = 34
    NFC = 35
    OPCUA = 36
    OPCDA = 37
    PROFIBUSDP = 38
    PROFINETRT = 39
    POWERLINK = 40
    SERCOS = 41
    SMI = 42
    THREAD = 43
    UMTS = 44
    WIFI = 45
    X2_X__LINK = 46
    VARAN = 47
    ZIG_BEE = 48
    Z__WAVE = 49

class OperatingModeEnum(enum.IntFlag):
    """specifies whether the pump is to be operated in single, parallel or series connection"""

    SINGLE_OPERATION = 0
    SERIES_OPERATION = 1
    PARALLEL_OPERATION = 2

class OperationModeEnum(enum.IntFlag):
    """describes the possible operation modes of the pump"""

    AUTO_CONTROL = 0
    CLOSED_LOOP_STANDARD_PID = 1
    ADVANCED = 2
    STAND_BY = 3
    OPEN_LOOP_MIN = 4
    OPEN_LOOP_VALUE = 5
    OPEN_LOOP_MAX = 6
    CLOSED_LOOP_MIN = 7
    CLOSED_LOOP_MAX = 8
    TEST = 9
    CALIBRATION = 10

class ControlModeEnum(enum.IntFlag):
    """describes the possible control modes of the pump"""

    CONSTANT_PRESSURE_CONTROL = 0
    CONSTANT_TEMPERATURE_CONTROL = 1
    DIFFERENTIAL_PRESSURE_CONTROL = 2
    CONSTANT_DIFFERENTIAL_PRESSURE_CONTROL = 3
    VARIABLE_DIFFERENTIAL_PRESSURE_CONTROL = 4
    FLOW_DEPENDENT_DIFFERENTIAL_PRESSURE_CONTROL = 5
    RETURN_FLOW_TEMPERATURE_CONTROL = 6
    FLOW_TEMPERATURE_CONTROL = 7
    FLOW_RATE_CONTROL = 8
    SPEED_CONTROL = 9
    AUTOMATIC = 10
    UNCONTROLLED = 11

class PumpKickModeEnum(enum.IntFlag):
    """describes the pump kick mode of the pump"""

    MANUFACTURER_SPECIFIC = 0
    DISABLED = 1
    OPERATOR_SPECIFIC = 2

class PumpRoleEnum(enum.IntFlag):
    """identifies the role rsp. task of the pump within the multi pump management"""

    SLAVE = 0
    MASTER = 1
    SLAVE_AND_AUXILIARY_MASTER = 2

class MultiPumpOperationModeEnum(enum.IntFlag):
    """specifies the actual multi pump operation mode"""

    STANDALONE = 0
    REDUNDANCY_OPERATION = 1
    ADDITION_OPERATION = 2
    MIXED_REDUNDANCY = 3

class ExchangeModeEnum(enum.IntFlag):
    """specifies the exchange mode of the pump"""

    MANUFACTURER_SPECIFIC = 0
    EXCHANGE_DISABLED = 1
    OPERATOR_SPECIFIC = 2

class DistributionTypeEnum(enum.IntFlag):
    """describes the share of operation time of different pumps of the pump system in addition operation mode"""

    MANUFACTURER_SPECIFIC = 0
    OPERATOR_SPECIFIC = 1
    CONCERNING_TIME_DISTRIBUTION = 2
    CONCERNING_LOAD_DISTRIBUTION = 3

class PortDirectionEnum(enum.IntFlag):
    """determines whether the port is an inlet and outlet or both"""

    IN = 0
    OUT = 1
    IN_OUT = 2

class ExplosionZoneOptionSet(ns0.datatypes.OptionSet):
    """defines flags for the category of explosion zones for devices"""

    @property
    def value(self) -> o6.ByteString: ...
    @value.setter
    def value(self, value: o6.ByteString) -> None: ...
    @property
    def validBits(self) -> o6.ByteString: ...
    @validBits.setter
    def validBits(self, value: o6.ByteString) -> None: ...

class ExplosionProtectionOptionSet(ns0.datatypes.OptionSet):
    """defines flags for the category of explosion protection for devices according to EU Directive 2014/34/EU (ATEX)"""

    @property
    def value(self) -> o6.ByteString: ...
    @value.setter
    def value(self, value: o6.ByteString) -> None: ...
    @property
    def validBits(self) -> o6.ByteString: ...
    @validBits.setter
    def validBits(self, value: o6.ByteString) -> None: ...

class OfferedControlModesOptionSet(ns0.datatypes.OptionSet):
    """defines flags for offerd control modes supported by the manufacturer for the product"""

    @property
    def value(self) -> o6.ByteString: ...
    @value.setter
    def value(self, value: o6.ByteString) -> None: ...
    @property
    def validBits(self) -> o6.ByteString: ...
    @validBits.setter
    def validBits(self, value: o6.ByteString) -> None: ...

class OfferedFieldbusesOptionSet(ns0.datatypes.OptionSet):
    """defines flags for fieldbuses supported by the manufacturer for the product"""

    @property
    def value(self) -> o6.ByteString: ...
    @value.setter
    def value(self, value: o6.ByteString) -> None: ...
    @property
    def validBits(self) -> o6.ByteString: ...
    @validBits.setter
    def validBits(self, value: o6.ByteString) -> None: ...

class DeclarationOfConformityOptionSet(ns0.datatypes.OptionSet):
    """defines flags for directives on the basis of which conformity was determined"""

    @property
    def value(self) -> o6.ByteString: ...
    @value.setter
    def value(self, value: o6.ByteString) -> None: ...
    @property
    def validBits(self) -> o6.ByteString: ...
    @validBits.setter
    def validBits(self, value: o6.ByteString) -> None: ...

class PhysicalAddressDataType(ns0.datatypes.Structure):
    """Physical address of the manufacturer."""

    @property
    def street(self) -> o6.LocalizedText | None: ...
    @street.setter
    def street(self, value: o6.LocalizedText | None) -> None: ...
    @property
    def number(self) -> o6.LocalizedText | None: ...
    @number.setter
    def number(self, value: o6.LocalizedText | None) -> None: ...
    @property
    def city(self) -> o6.LocalizedText | None: ...
    @city.setter
    def city(self, value: o6.LocalizedText | None) -> None: ...
    @property
    def postalCode(self) -> o6.LocalizedText | None: ...
    @postalCode.setter
    def postalCode(self, value: o6.LocalizedText | None) -> None: ...
    @property
    def state(self) -> o6.LocalizedText | None: ...
    @state.setter
    def state(self, value: o6.LocalizedText | None) -> None: ...
    @property
    def country(self) -> o6.LocalizedText | None: ...
    @country.setter
    def country(self, value: o6.LocalizedText | None) -> None: ...

class PumpClassEnum(enum.IntFlag):
    """defines possible pump types"""

    ROTODYNAMIC_PUMP = 0
    POSITIVE_DISPLACEMENT_PUMP = 1
    PROCESS_VACUUM_PUMP = 2
    TURBO_VACUUM_PUMP = 3
    VACUUM_PUMP = 4
    LIQUID_PUMP = 5
    PUMP = 6
