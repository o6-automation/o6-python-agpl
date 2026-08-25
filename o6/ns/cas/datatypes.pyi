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

class HealthStateEnum(enum.IntFlag):
    OK = 0
    WARNING = 1
    ERROR = 2
    CRITICAL = 3

class ReceiverTypeEnum(enum.IntFlag):
    """possible receiver types"""

    OTHER = 0
    DRY_RECEIVER = 1
    WET_RECEIVER = 2

class FilterTypeEnum(enum.IntFlag):
    """possible filter types"""

    OTHER = 0
    ACTIVATED_CARBON_FILTER = 1
    ADSORPTION_FILTER = 2
    COALESCING_FILTER = 3
    PARTICULATE_FILTER = 4
    FABRIC_FILTER = 5
    STERILE_FILTER = 6

class FluidTypeEnum(enum.IntFlag):
    """possible process fluid types"""

    AIR = 0
    CONDENSATE = 1
    OIL = 2
    WATER = 3

class FilterClassEnum(enum.IntFlag):
    """possible filter classes according to ISO 8573-1"""

    X = 10

class FilterClassDataType(ns0.datatypes.Structure):
    """information about the used filter class according to ISO 8573-1 of a filter"""

    @property
    def a(self) -> FilterClassEnum: ...
    @a.setter
    def a(self, value: _Integer) -> None: ...
    @property
    def b(self) -> FilterClassEnum: ...
    @b.setter
    def b(self, value: _Integer) -> None: ...
    @property
    def c(self) -> FilterClassEnum: ...
    @c.setter
    def c(self, value: _Integer) -> None: ...

class IntegratedStateEnum(enum.IntFlag):
    FULLY_INTEGRATED = 0
    PARTIALLY_INTEGRATED = 1
    FULLY_ISOLATED = 2

class SensorTechnologyOptionSet(ns0.datatypes.OptionSet):
    """flags for the used sensor technologies for a sensor"""

    @property
    def value(self) -> o6.ByteString: ...
    @value.setter
    def value(self, value: o6.ByteString) -> None: ...
    @property
    def validBits(self) -> o6.ByteString: ...
    @validBits.setter
    def validBits(self, value: o6.ByteString) -> None: ...

class ValveTypeEnum(enum.IntFlag):
    """possible valve types"""

    OTHER = 0
    CHECK_VALVE = 1
    CONTINUOUS_VALVE = 2
    FLOW_CONTROL_VALVE = 3
    PRESSURE_VALVE = 4
    SWITCHING_VALVE = 5

class DrainTypeEnum(enum.IntFlag):
    """possible condensate drain types"""

    OTHER = 0
    CAPACITIVE_DRAIN = 1
    LEVEL_CONTROLLED_DRAIN = 2
    TIMED_DRAIN = 3

class SeparatorTypeEnum(enum.IntFlag):
    """possible condensate separator types"""

    OTHER = 0
    CENTRIFUGAL_OILY_WATER_SEPARATOR = 1
    EMULSION_SPLITTING_SEPARATOR = 2
    FLOTATION_SEPARATOR = 3
    GRAVITY_PLATE_SEPARATOR = 4
    HYDROCYCLONE_OILY_WATER_SEPARATOR = 5

class OperatingStateEnum(enum.IntFlag):
    OTHER = 0
    STOPPED = 1
    STARTING = 2
    STOPPING = 3
    OPERATIONAL = 4

class ConverterTypeEnum(enum.IntFlag):
    """possible converter types"""

    OTHER = 0
    CATALYTIC_HC_CONVERTER = 1

class IpVersionEnum(enum.IntFlag):
    I_PV4 = 0
    I_PV6 = 1

class DryerTypeEnum(enum.IntFlag):
    """possible dryer types"""

    OTHER = 0
    ABSORPTION_DRYER = 1
    ADSORPTION_DRYER = 2
    MEMBRANE_DRYER = 3
    REFRIGERATION_DRYER = 4

class CompressorTypeEnum(enum.IntFlag):
    """possible compressor types"""

    OTHER = 0
    AXIAL_TURBO_COMPRESSOR = 1
    BELLOWS_COMPRESSOR = 2
    DIAPHRAGM_COMPRESSOR = 3
    LIQUID_RING_COMPRESSOR = 4
    PISTON_COMPRESSOR = 5
    RADIAL_TURBO_COMPRESSOR = 6
    ROOTS_COMPRESSOR = 7
    SCREW_COMPRESSOR = 8
    SCROLL_COMPRESSOR = 9
    SIDE_CHANNEL_COMPRESSOR = 10
    STRAIGHT_LOBE_COMPRESSOR = 11
    VANE_COMPRESSOR = 12

class LubricationTypeEnum(enum.IntFlag):
    """possible lubrication types for the compression process of a compressor"""

    NO_LUBRICATION = 0
    OIL_LUBRICATED = 1
    WATER_LUBRICATED = 2

class DisplacementTypeEnum(enum.IntFlag):
    """possible displacement types for a compressor"""

    POSITIVE_DISPLACEMENT = 0
    DYNAMIC_DISPLACEMENT = 1

class SensorTypeEnum(enum.IntFlag):
    """possible sensor types"""

    OTHER = 0
    AMMETER = 1
    DEW_POINT_SENSOR = 2
    FLOW_RATE_SENSOR = 3
    FLOW_SPEED_SENSOR = 4
    HUMIDITY_SENSOR = 5
    OIL_CONCENTRATION_SENSOR = 6
    PARTICLE_COUNTER = 7
    PRESSURE_SENSOR = 8
    TEMPERATURE_SENSOR = 9
    VOLTMETER = 10
    VOLUME_SENSOR = 11
    WATTMETER = 12

class AirnetHealthStateEnum(enum.IntFlag):
    OK = 0
    WARNING = 1
    ERROR = 2
    CRITICAL = 3

class AirnetIntegratedStateEnum(enum.IntFlag):
    FULLY_INTEGRATED = 0
    PARTIALLY_INTEGRATED = 1
    FULLY_ISOLATED = 2

class AirnetOperatingStateEnum(enum.IntFlag):
    OTHER = 0
    STOPPED = 1
    STARTING = 2
    STOPPING = 3
    OPERATIONAL = 4

class CompressorOperatingStateEnum(enum.IntFlag):
    OTHER = 0
    STOPPED = 1
    STARTING = 2
    STOPPING = 3
    UNLOADED = 4
    LOADING = 5
    UNLOADING = 6
    LOADED = 7

class DryerOperatingStateEnum(enum.IntFlag):
    OTHER = 0
    STOPPED = 1
    RUNNING = 2
    REFRIGERANT_COMPRESSOR_STOPPED = 3
    REFRIGERANT_COMPRESSOR_RUNNING = 4
    PURGE_VALVE_CLOSED = 5
    PURGE_VALVE_OPEN = 6
    PARALLEL_MODE_OF_BOTH_VESSELS = 7
    DEPRESSURIZING = 8
    DESORBING = 9
    COOLING = 10
    PRESSURIZING = 11
    REGENERATED_VESSEL_IN_STAND_BY = 12
