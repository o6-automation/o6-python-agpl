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

class ActiveStateDataType(enum.IntFlag):
    ACTIVE = 0
    INACTIVE = 1

class AvailabilityDataType(enum.IntFlag):
    AVAILABLE = 0
    UNAVAILABLE = 1

class AxisCouplingDataType(enum.IntFlag):
    MASTER = 0
    SLAVE = 1
    SYNCHRONOUS = 2
    TANDEM = 3

class AxisStateDataType(enum.IntFlag):
    HOME = 0
    PARKED = 1
    STOPPED = 2
    TRAVEL = 3

class OpenStateDataType(enum.IntFlag):
    CLOSED = 0
    OPEN = 1
    UNLATCHED = 2

class CompositionStateDataType(enum.IntFlag):
    ACTIVE = 0
    CLOSED = 1
    DOWN = 2
    INACTIVE = 3
    LEFT = 4
    OFF = 5
    ON = 6
    OPEN = 7
    RIGHT = 8
    TRANSITIONING = 9
    UNLATCHED = 10
    UP = 11

class ControllerModeDataType(enum.IntFlag):
    AUTOMATIC = 0
    EDIT = 1
    MANUAL = 2
    MANUAL_DATA_INPUT = 3
    SEMI_AUTOMATIC = 4

class OnOffDataType(enum.IntFlag):
    OFF = 0
    ON = 1

class DirectionDataType(enum.IntFlag):
    CLOCKWISE = 0
    COUNTER_CLOCKWISE = 1
    NEGATIVE = 2
    POSITIVE = 3

class YesNoDataType(enum.IntFlag):
    NO = 0
    YES = 1

class EmergencyStopDataType(enum.IntFlag):
    ARMED = 0
    TRIGGERED = 1

class FunctionalModeDataType(enum.IntFlag):
    MAINTENANCE = 0
    PRODUCTION = 1
    PROCESS_DEVELOPMENT = 2
    SETUP = 3
    TEARDOWN = 4

class PathModeDataType(enum.IntFlag):
    INDEPENDENT = 0
    MASTER = 1
    MIRROR = 2
    SYNCHRONOUS = 3

class ProgramEditDataType(enum.IntFlag):
    ACTIVE = 0
    NOT_READY = 1
    READY = 2

class RotaryModeDataType(enum.IntFlag):
    CONTOUR = 0
    INDEX = 1
    SPINDLE = 2

class InterfaceStatusDataType(enum.IntFlag):
    DISABLED = 0
    ENABLED = 1

class InterfaceStateDataType(enum.IntFlag):
    ACTIVE = 0
    COMPLETE = 1
    FAIL = 2
    NOT_READY = 4
    READY = 5

class ExecutionDataType(enum.IntFlag):
    ACTIVE = 0
    FEED_HOLD = 1
    INTERRUPTED = 2
    OPTIONAL_STOP = 3
    READY = 4
    PROGRAM_COMPLETED = 5
    PROGRAM_STOPPED = 6
    STOPPED = 7

class AssetEventDataType(ns0.datatypes.Structure):
    """A special \\gls{Variable} data type for asset change with a
    \\mtmodel{AssetType} and \\mtmodel{AssetId}."""

    @property
    def assetId(self) -> o6.String: ...
    @assetId.setter
    def assetId(self, value: o6.String) -> None: ...
    @property
    def assetType(self) -> o6.String: ...
    @assetType.setter
    def assetType(self, value: o6.String) -> None: ...

class MTRepresentationType(enum.IntFlag):
    """Represents the \\mtmodel{representation} attribute of the MTConnect
    \\gls{MTDataItem}."""

    DISCRETE = 0
    TIME_SERIES = 1
    VALUE = 2

class MTCategoryType(enum.IntFlag):
    """Represents the \\gls{category} attribute of the MTConnect \\gls{MTDataItem}."""

    EVENT = 0
    CONDITION = 1
    SAMPLE = 2

class MTCoordinateSystemType(enum.IntFlag):
    """Represents the \\mtmodel{coordinateSystem} attribute of the MTConnect
    \\gls{MTDataItem}. It is a reference system that associates a unique set of
    n parameters with each point in an n-dimensional space. Ref: ISO
    10303-218:2004"""

    MACHINE = 0
    WORK = 1

class MTResetTriggerType(enum.IntFlag):
    """These need to become \\uamodel{Good_} status code in OPC UA. resettrigger
    is an optional XML element that identifies the type of event that may
    cause a reset to occur. It is additional information regarding the meaning
    of the data that establishes an understanding of the time frame that the
    data represents so that the data may be correctly understood by a client
    software application."""

    ACTION_COMPLETE = 0
    ANNUAL = 1
    DAY = 2
    MAINTENANCE = 3
    MANUAL = 4
    MONTH = 5
    POWER_ON = 6
    SHIFT = 7
    WEEK = 8

class ThreeSpaceSampleDataType(ns0.datatypes.Structure):
    """Represents a position in a three space coordinate system. The positions
    must be given in millimeters."""

    @property
    def x(self) -> o6.Double: ...
    @x.setter
    def x(self, value: SupportsFloat) -> None: ...
    @property
    def y(self) -> o6.Double: ...
    @y.setter
    def y(self, value: SupportsFloat) -> None: ...
    @property
    def z(self) -> o6.Double: ...
    @z.setter
    def z(self, value: SupportsFloat) -> None: ...

class MessageDataType(ns0.datatypes.Structure):
    @property
    def nativeCode(self) -> o6.String | None: ...
    @nativeCode.setter
    def nativeCode(self, value: o6.String | None) -> None: ...
    @property
    def text(self) -> o6.String: ...
    @text.setter
    def text(self, value: o6.String) -> None: ...

class MTStatisticType(enum.IntFlag):
    AVERAGE = 0
    MAXIMUM = 1
    MEDIAN = 2
    MINIMUM = 3
    MODE = 4
    RANGE = 5
    ROOT_MEAN_SQUARE = 6
    STANDARD_DEVIATION = 7

class QualifierDataType(enum.IntFlag):
    HIGH = 0
    LOW = 1

class MTSeverityDataType(enum.IntFlag):
    FAULT = 0
    NORMAL = 1
    WARNING = 2
