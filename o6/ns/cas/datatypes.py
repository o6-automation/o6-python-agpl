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

"""Generated OPC UA cas namespace declarations."""

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


@o6.enumtype(nodeId="ns=cas;i=3003", browseName="HealthStateEnum")
class HealthStateEnum(ns0.datatypes.Enumeration):
    OK = o6.enumfield(0, name="OK")
    WARNING = o6.enumfield(1, name="Warning")
    ERROR = o6.enumfield(2, name="Error")
    CRITICAL = o6.enumfield(3, name="Critical")


@o6.enumtype(nodeId="ns=cas;i=3004", browseName="ReceiverTypeEnum", description="possible receiver types")
class ReceiverTypeEnum(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="Other")
    DRY_RECEIVER = o6.enumfield(1, name="DryReceiver")
    WET_RECEIVER = o6.enumfield(2, name="WetReceiver")


@o6.enumtype(nodeId="ns=cas;i=3005", browseName="FilterTypeEnum", description="possible filter types")
class FilterTypeEnum(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="Other")
    ACTIVATED_CARBON_FILTER = o6.enumfield(1, name="ActivatedCarbonFilter")
    ADSORPTION_FILTER = o6.enumfield(2, name="AdsorptionFilter")
    COALESCING_FILTER = o6.enumfield(3, name="CoalescingFilter")
    PARTICULATE_FILTER = o6.enumfield(4, name="ParticulateFilter")
    FABRIC_FILTER = o6.enumfield(5, name="FabricFilter")
    STERILE_FILTER = o6.enumfield(6, name="SterileFilter")


@o6.enumtype(nodeId="ns=cas;i=3006", browseName="FluidTypeEnum", description="possible process fluid types")
class FluidTypeEnum(ns0.datatypes.Enumeration):
    AIR = o6.enumfield(0, name="Air")
    CONDENSATE = o6.enumfield(1, name="Condensate")
    OIL = o6.enumfield(2, name="Oil")
    WATER = o6.enumfield(3, name="Water")


@o6.enumtype(nodeId="ns=cas;i=3008", browseName="FilterClassEnum", description="possible filter classes according to ISO 8573-1")
class FilterClassEnum(ns0.datatypes.Enumeration):
    _0 = o6.enumfield(0, name="0")
    _1 = o6.enumfield(1, name="1")
    _2 = o6.enumfield(2, name="2")
    _3 = o6.enumfield(3, name="3")
    _4 = o6.enumfield(4, name="4")
    _5 = o6.enumfield(5, name="5")
    _6 = o6.enumfield(6, name="6")
    _7 = o6.enumfield(7, name="7")
    _8 = o6.enumfield(8, name="8")
    _9 = o6.enumfield(9, name="9")
    X = o6.enumfield(10, name="X")


@o6.datatype(
    nodeId="ns=cas;i=3007",
    browseName="FilterClassDataType",
    description="information about the used filter class according to ISO 8573-1 of a filter",
    defaultEncodingId="ns=cas;i=5042",
)
class FilterClassDataType(ns0.datatypes.Structure):
    a: FilterClassEnum
    b: FilterClassEnum
    c: FilterClassEnum


@o6.enumtype(nodeId="ns=cas;i=3009", browseName="IntegratedStateEnum")
class IntegratedStateEnum(ns0.datatypes.Enumeration):
    FULLY_INTEGRATED = o6.enumfield(0, name="FullyIntegrated")
    PARTIALLY_INTEGRATED = o6.enumfield(1, name="PartiallyIntegrated")
    FULLY_ISOLATED = o6.enumfield(2, name="FullyIsolated")


@o6.datatype(nodeId="ns=cas;i=3010", browseName="SensorTechnologyOptionSet", description="flags for the used sensor technologies for a sensor", defaultEncodingId="ns=cas;i=5175")
class SensorTechnologyOptionSet(ns0.datatypes.OptionSet):
    value: o6.ByteString
    validBits: o6.ByteString


@o6.enumtype(nodeId="ns=cas;i=3011", browseName="ValveTypeEnum", description="possible valve types")
class ValveTypeEnum(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="Other")
    CHECK_VALVE = o6.enumfield(1, name="CheckValve")
    CONTINUOUS_VALVE = o6.enumfield(2, name="ContinuousValve")
    FLOW_CONTROL_VALVE = o6.enumfield(3, name="FlowControlValve")
    PRESSURE_VALVE = o6.enumfield(4, name="PressureValve")
    SWITCHING_VALVE = o6.enumfield(5, name="SwitchingValve")


@o6.enumtype(nodeId="ns=cas;i=3012", browseName="DrainTypeEnum", description="possible condensate drain types")
class DrainTypeEnum(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="Other")
    CAPACITIVE_DRAIN = o6.enumfield(1, name="CapacitiveDrain")
    LEVEL_CONTROLLED_DRAIN = o6.enumfield(2, name="LevelControlledDrain")
    TIMED_DRAIN = o6.enumfield(3, name="TimedDrain")


@o6.enumtype(nodeId="ns=cas;i=3013", browseName="SeparatorTypeEnum", description="possible condensate separator types")
class SeparatorTypeEnum(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="Other")
    CENTRIFUGAL_OILY_WATER_SEPARATOR = o6.enumfield(1, name="CentrifugalOilyWaterSeparator")
    EMULSION_SPLITTING_SEPARATOR = o6.enumfield(2, name="EmulsionSplittingSeparator")
    FLOTATION_SEPARATOR = o6.enumfield(3, name="FlotationSeparator")
    GRAVITY_PLATE_SEPARATOR = o6.enumfield(4, name="GravityPlateSeparator")
    HYDROCYCLONE_OILY_WATER_SEPARATOR = o6.enumfield(5, name="HydrocycloneOilyWaterSeparator")


@o6.enumtype(nodeId="ns=cas;i=3014", browseName="OperatingStateEnum")
class OperatingStateEnum(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="Other")
    STOPPED = o6.enumfield(1, name="Stopped")
    STARTING = o6.enumfield(2, name="Starting")
    STOPPING = o6.enumfield(3, name="Stopping")
    OPERATIONAL = o6.enumfield(4, name="Operational")


@o6.enumtype(nodeId="ns=cas;i=3015", browseName="ConverterTypeEnum", description="possible converter types")
class ConverterTypeEnum(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="Other")
    CATALYTIC_HC_CONVERTER = o6.enumfield(1, name="CatalyticHCConverter")


@o6.enumtype(nodeId="ns=cas;i=3016", browseName="IpVersionEnum")
class IpVersionEnum(ns0.datatypes.Enumeration):
    I_PV4 = o6.enumfield(0, name="IPv4")
    I_PV6 = o6.enumfield(1, name="IPv6")


@o6.enumtype(nodeId="ns=cas;i=3017", browseName="DryerTypeEnum", description="possible dryer types")
class DryerTypeEnum(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="Other")
    ABSORPTION_DRYER = o6.enumfield(1, name="AbsorptionDryer")
    ADSORPTION_DRYER = o6.enumfield(2, name="AdsorptionDryer")
    MEMBRANE_DRYER = o6.enumfield(3, name="MembraneDryer")
    REFRIGERATION_DRYER = o6.enumfield(4, name="RefrigerationDryer")


@o6.enumtype(nodeId="ns=cas;i=3018", browseName="CompressorTypeEnum", description="possible compressor types")
class CompressorTypeEnum(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="Other")
    AXIAL_TURBO_COMPRESSOR = o6.enumfield(1, name="AxialTurboCompressor")
    BELLOWS_COMPRESSOR = o6.enumfield(2, name="BellowsCompressor")
    DIAPHRAGM_COMPRESSOR = o6.enumfield(3, name="DiaphragmCompressor")
    LIQUID_RING_COMPRESSOR = o6.enumfield(4, name="LiquidRingCompressor")
    PISTON_COMPRESSOR = o6.enumfield(5, name="PistonCompressor")
    RADIAL_TURBO_COMPRESSOR = o6.enumfield(6, name="RadialTurboCompressor")
    ROOTS_COMPRESSOR = o6.enumfield(7, name="RootsCompressor")
    SCREW_COMPRESSOR = o6.enumfield(8, name="ScrewCompressor")
    SCROLL_COMPRESSOR = o6.enumfield(9, name="ScrollCompressor")
    SIDE_CHANNEL_COMPRESSOR = o6.enumfield(10, name="SideChannelCompressor")
    STRAIGHT_LOBE_COMPRESSOR = o6.enumfield(11, name="StraightLobeCompressor")
    VANE_COMPRESSOR = o6.enumfield(12, name="VaneCompressor")


@o6.enumtype(nodeId="ns=cas;i=3019", browseName="LubricationTypeEnum", description="possible lubrication types for the compression process of a compressor")
class LubricationTypeEnum(ns0.datatypes.Enumeration):
    NO_LUBRICATION = o6.enumfield(0, name="NoLubrication")
    OIL_LUBRICATED = o6.enumfield(1, name="OilLubricated")
    WATER_LUBRICATED = o6.enumfield(2, name="WaterLubricated")


@o6.enumtype(nodeId="ns=cas;i=3020", browseName="DisplacementTypeEnum", description="possible displacement types for a compressor")
class DisplacementTypeEnum(ns0.datatypes.Enumeration):
    POSITIVE_DISPLACEMENT = o6.enumfield(0, name="PositiveDisplacement")
    DYNAMIC_DISPLACEMENT = o6.enumfield(1, name="DynamicDisplacement")


@o6.enumtype(nodeId="ns=cas;i=3021", browseName="SensorTypeEnum", description="possible sensor types")
class SensorTypeEnum(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="Other")
    AMMETER = o6.enumfield(1, name="Ammeter")
    DEW_POINT_SENSOR = o6.enumfield(2, name="DewPointSensor")
    FLOW_RATE_SENSOR = o6.enumfield(3, name="FlowRateSensor")
    FLOW_SPEED_SENSOR = o6.enumfield(4, name="FlowSpeedSensor")
    HUMIDITY_SENSOR = o6.enumfield(5, name="HumiditySensor")
    OIL_CONCENTRATION_SENSOR = o6.enumfield(6, name="OilConcentrationSensor")
    PARTICLE_COUNTER = o6.enumfield(7, name="ParticleCounter")
    PRESSURE_SENSOR = o6.enumfield(8, name="PressureSensor")
    TEMPERATURE_SENSOR = o6.enumfield(9, name="TemperatureSensor")
    VOLTMETER = o6.enumfield(10, name="Voltmeter")
    VOLUME_SENSOR = o6.enumfield(11, name="VolumeSensor")
    WATTMETER = o6.enumfield(12, name="Wattmeter")


@o6.enumtype(nodeId="ns=cas;i=3022", browseName="AirnetHealthStateEnum")
class AirnetHealthStateEnum(ns0.datatypes.Enumeration):
    OK = o6.enumfield(0, name="OK")
    WARNING = o6.enumfield(1, name="Warning")
    ERROR = o6.enumfield(2, name="Error")
    CRITICAL = o6.enumfield(3, name="Critical")


@o6.enumtype(nodeId="ns=cas;i=3023", browseName="AirnetIntegratedStateEnum")
class AirnetIntegratedStateEnum(ns0.datatypes.Enumeration):
    FULLY_INTEGRATED = o6.enumfield(0, name="FullyIntegrated")
    PARTIALLY_INTEGRATED = o6.enumfield(1, name="PartiallyIntegrated")
    FULLY_ISOLATED = o6.enumfield(2, name="FullyIsolated")


@o6.enumtype(nodeId="ns=cas;i=3024", browseName="AirnetOperatingStateEnum")
class AirnetOperatingStateEnum(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="Other")
    STOPPED = o6.enumfield(1, name="Stopped")
    STARTING = o6.enumfield(2, name="Starting")
    STOPPING = o6.enumfield(3, name="Stopping")
    OPERATIONAL = o6.enumfield(4, name="Operational")


@o6.enumtype(nodeId="ns=cas;i=3025", browseName="CompressorOperatingStateEnum")
class CompressorOperatingStateEnum(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="Other")
    STOPPED = o6.enumfield(1, name="Stopped")
    STARTING = o6.enumfield(2, name="Starting")
    STOPPING = o6.enumfield(3, name="Stopping")
    UNLOADED = o6.enumfield(4, name="Unloaded")
    LOADING = o6.enumfield(5, name="Loading")
    UNLOADING = o6.enumfield(6, name="Unloading")
    LOADED = o6.enumfield(7, name="Loaded")


@o6.enumtype(nodeId="ns=cas;i=3026", browseName="DryerOperatingStateEnum")
class DryerOperatingStateEnum(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="Other")
    STOPPED = o6.enumfield(1, name="Stopped")
    RUNNING = o6.enumfield(2, name="Running")
    REFRIGERANT_COMPRESSOR_STOPPED = o6.enumfield(3, name="RefrigerantCompressorStopped")
    REFRIGERANT_COMPRESSOR_RUNNING = o6.enumfield(4, name="RefrigerantCompressorRunning")
    PURGE_VALVE_CLOSED = o6.enumfield(5, name="PurgeValveClosed")
    PURGE_VALVE_OPEN = o6.enumfield(6, name="PurgeValveOpen")
    PARALLEL_MODE_OF_BOTH_VESSELS = o6.enumfield(7, name="ParallelModeOfBothVessels")
    DEPRESSURIZING = o6.enumfield(8, name="Depressurizing")
    DESORBING = o6.enumfield(9, name="Desorbing")
    COOLING = o6.enumfield(10, name="Cooling")
    PRESSURIZING = o6.enumfield(11, name="Pressurizing")
    REGENERATED_VESSEL_IN_STAND_BY = o6.enumfield(12, name="RegeneratedVesselInStand-by")


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0
