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

"""Generated OPC UA mt_connect namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as mt_connect_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=mt_connect;i=2197", browseName="ActiveStateDataType")
class ActiveStateDataType(ns0.datatypes.Enumeration):
    ACTIVE = o6.enumfield(0, name="ACTIVE")
    INACTIVE = o6.enumfield(1, name="INACTIVE")


@o6.enumtype(nodeId="ns=mt_connect;i=2198", browseName="AvailabilityDataType")
class AvailabilityDataType(ns0.datatypes.Enumeration):
    AVAILABLE = o6.enumfield(0, name="AVAILABLE")
    UNAVAILABLE = o6.enumfield(1, name="UNAVAILABLE")


@o6.enumtype(nodeId="ns=mt_connect;i=2199", browseName="AxisCouplingDataType")
class AxisCouplingDataType(ns0.datatypes.Enumeration):
    MASTER = o6.enumfield(0, name="MASTER")
    SLAVE = o6.enumfield(1, name="SLAVE")
    SYNCHRONOUS = o6.enumfield(2, name="SYNCHRONOUS")
    TANDEM = o6.enumfield(3, name="TANDEM")


@o6.enumtype(nodeId="ns=mt_connect;i=2200", browseName="AxisStateDataType")
class AxisStateDataType(ns0.datatypes.Enumeration):
    HOME = o6.enumfield(0, name="HOME")
    PARKED = o6.enumfield(1, name="PARKED")
    STOPPED = o6.enumfield(2, name="STOPPED")
    TRAVEL = o6.enumfield(3, name="TRAVEL")


@o6.enumtype(nodeId="ns=mt_connect;i=2201", browseName="OpenStateDataType")
class OpenStateDataType(ns0.datatypes.Enumeration):
    CLOSED = o6.enumfield(0, name="CLOSED")
    OPEN = o6.enumfield(1, name="OPEN")
    UNLATCHED = o6.enumfield(2, name="UNLATCHED")


@o6.enumtype(nodeId="ns=mt_connect;i=2202", browseName="CompositionStateDataType")
class CompositionStateDataType(ns0.datatypes.Enumeration):
    ACTIVE = o6.enumfield(0, name="ACTIVE")
    CLOSED = o6.enumfield(1, name="CLOSED")
    DOWN = o6.enumfield(2, name="DOWN")
    INACTIVE = o6.enumfield(3, name="INACTIVE")
    LEFT = o6.enumfield(4, name="LEFT")
    OFF = o6.enumfield(5, name="OFF")
    ON = o6.enumfield(6, name="ON")
    OPEN = o6.enumfield(7, name="OPEN")
    RIGHT = o6.enumfield(8, name="RIGHT")
    TRANSITIONING = o6.enumfield(9, name="TRANSITIONING")
    UNLATCHED = o6.enumfield(10, name="UNLATCHED")
    UP = o6.enumfield(11, name="UP")


@o6.enumtype(nodeId="ns=mt_connect;i=2203", browseName="ControllerModeDataType")
class ControllerModeDataType(ns0.datatypes.Enumeration):
    AUTOMATIC = o6.enumfield(0, name="AUTOMATIC")
    EDIT = o6.enumfield(1, name="EDIT")
    MANUAL = o6.enumfield(2, name="MANUAL")
    MANUAL_DATA_INPUT = o6.enumfield(3, name="MANUAL_DATA_INPUT")
    SEMI_AUTOMATIC = o6.enumfield(4, name="SEMI_AUTOMATIC")


@o6.enumtype(nodeId="ns=mt_connect;i=2204", browseName="OnOffDataType")
class OnOffDataType(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(0, name="OFF")
    ON = o6.enumfield(1, name="ON")


@o6.enumtype(nodeId="ns=mt_connect;i=2205", browseName="DirectionDataType")
class DirectionDataType(ns0.datatypes.Enumeration):
    CLOCKWISE = o6.enumfield(0, name="CLOCKWISE")
    COUNTER_CLOCKWISE = o6.enumfield(1, name="COUNTER_CLOCKWISE")
    NEGATIVE = o6.enumfield(2, name="NEGATIVE")
    POSITIVE = o6.enumfield(3, name="POSITIVE")


@o6.enumtype(nodeId="ns=mt_connect;i=2206", browseName="YesNoDataType")
class YesNoDataType(ns0.datatypes.Enumeration):
    NO = o6.enumfield(0, name="NO")
    YES = o6.enumfield(1, name="YES")


@o6.enumtype(nodeId="ns=mt_connect;i=2207", browseName="EmergencyStopDataType")
class EmergencyStopDataType(ns0.datatypes.Enumeration):
    ARMED = o6.enumfield(0, name="ARMED")
    TRIGGERED = o6.enumfield(1, name="TRIGGERED")


@o6.enumtype(nodeId="ns=mt_connect;i=2208", browseName="FunctionalModeDataType")
class FunctionalModeDataType(ns0.datatypes.Enumeration):
    MAINTENANCE = o6.enumfield(0, name="MAINTENANCE")
    PRODUCTION = o6.enumfield(1, name="PRODUCTION")
    PROCESS_DEVELOPMENT = o6.enumfield(2, name="PROCESS_DEVELOPMENT")
    SETUP = o6.enumfield(3, name="SETUP")
    TEARDOWN = o6.enumfield(4, name="TEARDOWN")


@o6.enumtype(nodeId="ns=mt_connect;i=2209", browseName="PathModeDataType")
class PathModeDataType(ns0.datatypes.Enumeration):
    INDEPENDENT = o6.enumfield(0, name="INDEPENDENT")
    MASTER = o6.enumfield(1, name="MASTER")
    MIRROR = o6.enumfield(2, name="MIRROR")
    SYNCHRONOUS = o6.enumfield(3, name="SYNCHRONOUS")


@o6.enumtype(nodeId="ns=mt_connect;i=2210", browseName="ProgramEditDataType")
class ProgramEditDataType(ns0.datatypes.Enumeration):
    ACTIVE = o6.enumfield(0, name="ACTIVE")
    NOT_READY = o6.enumfield(1, name="NOT_READY")
    READY = o6.enumfield(2, name="READY")


@o6.enumtype(nodeId="ns=mt_connect;i=2211", browseName="RotaryModeDataType")
class RotaryModeDataType(ns0.datatypes.Enumeration):
    CONTOUR = o6.enumfield(0, name="CONTOUR")
    INDEX = o6.enumfield(1, name="INDEX")
    SPINDLE = o6.enumfield(2, name="SPINDLE")


@o6.enumtype(nodeId="ns=mt_connect;i=2230", browseName="InterfaceStatusDataType")
class InterfaceStatusDataType(ns0.datatypes.Enumeration):
    DISABLED = o6.enumfield(0, name="DISABLED")
    ENABLED = o6.enumfield(1, name="ENABLED")


@o6.enumtype(nodeId="ns=mt_connect;i=2234", browseName="InterfaceStateDataType")
class InterfaceStateDataType(ns0.datatypes.Enumeration):
    ACTIVE = o6.enumfield(0, name="ACTIVE")
    COMPLETE = o6.enumfield(1, name="COMPLETE")
    FAIL = o6.enumfield(2, name="FAIL")
    NOT_READY = o6.enumfield(4, name="NOT_READY")
    READY = o6.enumfield(5, name="READY")


@o6.enumtype(nodeId="ns=mt_connect;i=2262", browseName="ExecutionDataType")
class ExecutionDataType(ns0.datatypes.Enumeration):
    ACTIVE = o6.enumfield(0, name="ACTIVE")
    FEED_HOLD = o6.enumfield(1, name="FEED_HOLD")
    INTERRUPTED = o6.enumfield(2, name="INTERRUPTED")
    OPTIONAL_STOP = o6.enumfield(3, name="OPTIONAL_STOP")
    READY = o6.enumfield(4, name="READY")
    PROGRAM_COMPLETED = o6.enumfield(5, name="PROGRAM_COMPLETED")
    PROGRAM_STOPPED = o6.enumfield(6, name="PROGRAM_STOPPED")
    STOPPED = o6.enumfield(7, name="STOPPED")


@o6.datatype(
    nodeId="ns=mt_connect;i=2618",
    browseName="AssetEventDataType",
    description="A special \\gls{Variable} data type for asset change with a\n      \\mtmodel{AssetType} and \\mtmodel{AssetId}.",
    defaultEncodingId="ns=mt_connect;i=2745",
)
class AssetEventDataType(ns0.datatypes.Structure):
    assetId: o6.String
    assetType: o6.String


@o6.enumtype(
    nodeId="ns=mt_connect;i=2633", browseName="MTRepresentationType", description="Represents the \\mtmodel{representation} attribute of the MTConnect\n      \\gls{MTDataItem}."
)
class MTRepresentationType(ns0.datatypes.Enumeration):
    DISCRETE = o6.enumfield(0, name="DISCRETE")
    TIME_SERIES = o6.enumfield(1, name="TIME_SERIES")
    VALUE = o6.enumfield(2, name="VALUE")


@o6.enumtype(nodeId="ns=mt_connect;i=2634", browseName="MTCategoryType", description="Represents the \\gls{category} attribute of the MTConnect \\gls{MTDataItem}.")
class MTCategoryType(ns0.datatypes.Enumeration):
    EVENT = o6.enumfield(0, name="EVENT")
    CONDITION = o6.enumfield(1, name="CONDITION")
    SAMPLE = o6.enumfield(2, name="SAMPLE")


@o6.enumtype(
    nodeId="ns=mt_connect;i=2635",
    browseName="MTCoordinateSystemType",
    description="Represents the \\mtmodel{coordinateSystem} attribute of the MTConnect\n      \\gls{MTDataItem}. It is a reference system that associates a unique set of\n      n parameters with each point in an n-dimensional space. Ref: ISO\n      10303-218:2004",
)
class MTCoordinateSystemType(ns0.datatypes.Enumeration):
    MACHINE = o6.enumfield(0, name="MACHINE")
    WORK = o6.enumfield(1, name="WORK")


@o6.enumtype(
    nodeId="ns=mt_connect;i=2636",
    browseName="MTResetTriggerType",
    description="These need to become \\uamodel{Good_} status code in OPC UA. resettrigger\n      is an optional XML element that identifies the type of event that may\n      cause a reset to occur. It is additional information regarding the meaning\n      of the data that establishes an understanding of the time frame that the\n      data represents so that the data may be correctly understood by a client\n      software application.",
)
class MTResetTriggerType(ns0.datatypes.Enumeration):
    ACTION_COMPLETE = o6.enumfield(0, name="ACTION_COMPLETE")
    ANNUAL = o6.enumfield(1, name="ANNUAL")
    DAY = o6.enumfield(2, name="DAY")
    MAINTENANCE = o6.enumfield(3, name="MAINTENANCE")
    MANUAL = o6.enumfield(4, name="MANUAL")
    MONTH = o6.enumfield(5, name="MONTH")
    POWER_ON = o6.enumfield(6, name="POWER_ON")
    SHIFT = o6.enumfield(7, name="SHIFT")
    WEEK = o6.enumfield(8, name="WEEK")


@o6.datatype(
    nodeId="ns=mt_connect;i=2637",
    browseName="ThreeSpaceSampleDataType",
    description="Represents a position in a three space coordinate system. The positions\n      must be given in millimeters.",
    defaultEncodingId="ns=mt_connect;i=2909",
)
class ThreeSpaceSampleDataType(ns0.datatypes.Structure):
    x: o6.Double
    y: o6.Double
    z: o6.Double


@o6.datatype(nodeId="ns=mt_connect;i=2653", browseName="MessageDataType", defaultEncodingId="ns=mt_connect;i=2903")
class MessageDataType(ns0.datatypes.Structure):
    nativeCode: o6.String | None
    text: o6.String


@o6.enumtype(nodeId="ns=mt_connect;i=2659", browseName="MTStatisticType")
class MTStatisticType(ns0.datatypes.Enumeration):
    AVERAGE = o6.enumfield(0, name="AVERAGE")
    MAXIMUM = o6.enumfield(1, name="MAXIMUM")
    MEDIAN = o6.enumfield(2, name="MEDIAN")
    MINIMUM = o6.enumfield(3, name="MINIMUM")
    MODE = o6.enumfield(4, name="MODE")
    RANGE = o6.enumfield(5, name="RANGE")
    ROOT_MEAN_SQUARE = o6.enumfield(6, name="ROOT_MEAN_SQUARE")
    STANDARD_DEVIATION = o6.enumfield(7, name="STANDARD_DEVIATION")


@o6.enumtype(nodeId="ns=mt_connect;i=2668", browseName="QualifierDataType")
class QualifierDataType(ns0.datatypes.Enumeration):
    HIGH = o6.enumfield(0, name="HIGH")
    LOW = o6.enumfield(1, name="LOW")


@o6.enumtype(nodeId="ns=mt_connect;i=2669", browseName="MTSeverityDataType")
class MTSeverityDataType(ns0.datatypes.Enumeration):
    FAULT = o6.enumfield(0, name="FAULT")
    NORMAL = o6.enumfield(1, name="NORMAL")
    WARNING = o6.enumfield(2, name="WARNING")


del Any, TYPE_CHECKING, uuid, o6, ns0, mt_connect_reftypes
