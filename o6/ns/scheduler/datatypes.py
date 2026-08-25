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

"""Generated OPC UA scheduler namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(
    nodeId="ns=scheduler;i=74",
    browseName="Month",
    description='This enumeration indicates either a specific Gregorian calendar month, or a relative relationship ("odd", "even", and "unspecified").',
)
class Month(ns0.datatypes.Enumeration):
    UNSPECIFIED = o6.enumfield(0, name="Unspecified")
    JANUARY = o6.enumfield(1, name="January")
    FEBRUARY = o6.enumfield(2, name="February")
    MARCH = o6.enumfield(3, name="March")
    APRIL = o6.enumfield(4, name="April")
    MAY = o6.enumfield(5, name="May")
    JUNE = o6.enumfield(6, name="June")
    JULY = o6.enumfield(7, name="July")
    AUGUST = o6.enumfield(8, name="August")
    SEPTEMBER = o6.enumfield(9, name="September")
    OCTOBER = o6.enumfield(10, name="October")
    NOVEMBER = o6.enumfield(11, name="November")
    DECEMBER = o6.enumfield(12, name="December")
    ODD = o6.enumfield(13, name="Odd")
    EVEN = o6.enumfield(14, name="Even")


@o6.enumtype(
    nodeId="ns=scheduler;i=76",
    browseName="DayOfMonth",
    description='This enumeration indicates specific days of the month by specific date ("1", "22", and so on) or by relative position ("last day of month", "even day of month", and so on).',
)
class DayOfMonth(ns0.datatypes.Enumeration):
    UNSPECIFIED = o6.enumfield(0, name="Unspecified")
    DAY1 = o6.enumfield(1, name="Day1")
    DAY2 = o6.enumfield(2, name="Day2")
    DAY3 = o6.enumfield(3, name="Day3")
    DAY4 = o6.enumfield(4, name="Day4")
    DAY5 = o6.enumfield(5, name="Day5")
    DAY6 = o6.enumfield(6, name="Day6")
    DAY7 = o6.enumfield(7, name="Day7")
    DAY8 = o6.enumfield(8, name="Day8")
    DAY9 = o6.enumfield(9, name="Day9")
    DAY10 = o6.enumfield(10, name="Day10")
    DAY11 = o6.enumfield(11, name="Day11")
    DAY12 = o6.enumfield(12, name="Day12")
    DAY13 = o6.enumfield(13, name="Day13")
    DAY14 = o6.enumfield(14, name="Day14")
    DAY15 = o6.enumfield(15, name="Day15")
    DAY16 = o6.enumfield(16, name="Day16")
    DAY17 = o6.enumfield(17, name="Day17")
    DAY18 = o6.enumfield(18, name="Day18")
    DAY19 = o6.enumfield(19, name="Day19")
    DAY20 = o6.enumfield(20, name="Day20")
    DAY21 = o6.enumfield(21, name="Day21")
    DAY22 = o6.enumfield(22, name="Day22")
    DAY23 = o6.enumfield(23, name="Day23")
    DAY24 = o6.enumfield(24, name="Day24")
    DAY25 = o6.enumfield(25, name="Day25")
    DAY26 = o6.enumfield(26, name="Day26")
    DAY27 = o6.enumfield(27, name="Day27")
    DAY28 = o6.enumfield(28, name="Day28")
    DAY29 = o6.enumfield(29, name="Day29")
    DAY30 = o6.enumfield(30, name="Day30")
    DAY31 = o6.enumfield(31, name="Day31")
    LAST_DAY_OF_MONTH = o6.enumfield(32, name="LastDayOfMonth")
    ODD_DAY_OF_MONTH = o6.enumfield(33, name="OddDayOfMonth")
    EVEN_DAY_OF_MONTH = o6.enumfield(34, name="EvenDayOfMonth")


@o6.enumtype(nodeId="ns=scheduler;i=78", browseName="DayOfWeek", description='This enumeration indicates each of the seven days of the week, or "unspecified".')
class DayOfWeek(ns0.datatypes.Enumeration):
    UNSPECIFIED = o6.enumfield(0, name="Unspecified")
    MONDAY = o6.enumfield(1, name="Monday")
    TUESDAY = o6.enumfield(2, name="Tuesday")
    WEDNESDAY = o6.enumfield(3, name="Wednesday")
    THURSDAY = o6.enumfield(4, name="Thursday")
    FRIDAY = o6.enumfield(5, name="Friday")
    SATURDAY = o6.enumfield(6, name="Saturday")
    SUNDAY = o6.enumfield(7, name="Sunday")


@o6.datatype(
    nodeId="ns=scheduler;i=73",
    browseName="DateType",
    description="This structure defines a calendar date. It allows to define a concrete date, e.g. 2022-02-12. By using wildcards, it also allows to define repeating dates, like every Wednesday, every odd day of a month, every 24th of December, every last day of a month in 2023, etc.",
    defaultEncodingId="ns=scheduler;i=90",
)
class DateType(ns0.datatypes.Structure):
    year: o6.UInt16
    month: Month
    dayOfMonth: DayOfMonth
    dayOfWeek: DayOfWeek


@o6.datatype(
    nodeId="ns=scheduler;i=80",
    browseName="DateRangeType",
    description='This structure defines a time span, with absolute start and end dates. The StartDate and EndDate are limited to specific values, i.e., wild cards like odd months are not allowed. The Year field shall not be 0; the Month field shall be a value between 1 to 12; the DayOfMonth field shall be between 1 to 31 and the DayOfMonth field shall be "unspecified".',
    defaultEncodingId="ns=scheduler;i=91",
)
class DateRangeType(ns0.datatypes.Structure):
    startDate: DateType
    endDate: DateType


@o6.datatype(nodeId="ns=scheduler;i=72", browseName="CalendarEntryType", description="This union that defines various calendar date values", defaultEncodingId="ns=scheduler;i=89")
class CalendarEntryType(ns0.datatypes.Union):
    date: DateType
    dateRange: DateRangeType


@o6.datatype(
    nodeId="ns=scheduler;i=71",
    browseName="SpecialEventPeriodType",
    description="This union contains a calendar entry or a reference to a calendar object",
    defaultEncodingId="ns=scheduler;i=88",
)
class SpecialEventPeriodType(ns0.datatypes.Union):
    calendarEntry: CalendarEntryType
    calendarReference: o6.NodeId


@o6.datatype(
    nodeId="ns=scheduler;i=82",
    browseName="BaseActionType",
    description="This abstract structure defines the base of an action. The base only contains information, if the last execution of the action was successful.",
    defaultEncodingId="ns=scheduler;i=93",
    isAbstract=True,
)
class BaseActionType(ns0.datatypes.Structure):
    lastActionResult: o6.StatusCode


@o6.datatype(
    nodeId="ns=scheduler;i=83",
    browseName="WriteLocalVariableActionType",
    description="This structure defines an action to write the value of a Variable managed in the same Server where the action is used.",
    defaultEncodingId="ns=scheduler;i=94",
)
class WriteLocalVariableActionType(BaseActionType):
    lastActionResult: o6.StatusCode
    variable: o6.NodeId
    value: Any


@o6.datatype(
    nodeId="ns=scheduler;i=84",
    browseName="CallLocalMethodActionType",
    description="This structure defines an action to call a Method of an Object managed in the same Server where the action is used.",
    defaultEncodingId="ns=scheduler;i=95",
)
class CallLocalMethodActionType(BaseActionType):
    lastActionResult: o6.StatusCode
    objectId: o6.NodeId
    methodId: o6.NodeId
    inputValues: list[Any]
    lastOutputValues: list[Any]


@o6.datatype(nodeId="ns=scheduler;i=85", browseName="TimeType", description="This structure that represents a point in time during a day", defaultEncodingId="ns=scheduler;i=96")
class TimeType(ns0.datatypes.Structure):
    hour: o6.Byte
    minute: o6.Byte
    second: o6.Byte


@o6.datatype(
    nodeId="ns=scheduler;i=81",
    browseName="TimeActionsType",
    description="This structure contains a time and an array of actions. It is used to define actions to be executed at a specific point in time.",
    defaultEncodingId="ns=scheduler;i=92",
)
class TimeActionsType(ns0.datatypes.Structure):
    time: TimeType
    actions: list[BaseActionType]


@o6.datatype(
    nodeId="ns=scheduler;i=70",
    browseName="SpecialEventType",
    description="This structure contains a period, a list of time values, and a priority. It is a means to identify moments in time over one or more days.",
    defaultEncodingId="ns=scheduler;i=87",
)
class SpecialEventType(ns0.datatypes.Structure):
    period: SpecialEventPeriodType
    listOfTimeActions: list[TimeActionsType]
    eventPriority: o6.Byte


@o6.datatype(
    nodeId="ns=scheduler;i=86",
    browseName="DailyScheduleType",
    description="This structure defines a sequence of TimeActionsType structures. Each element in the sequence defines a time/actions pair that describes the actions to be executed at a given point in the day.",
    defaultEncodingId="ns=scheduler;i=97",
)
class DailyScheduleType(ns0.datatypes.Structure):
    daySchedule: list[TimeActionsType]


del Any, TYPE_CHECKING, uuid, o6, ns0
