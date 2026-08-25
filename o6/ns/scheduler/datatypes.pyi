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

class Month(enum.IntFlag):
    """This enumeration indicates either a specific Gregorian calendar month, or a relative relationship ("odd", "even", and "unspecified")."""

    UNSPECIFIED = 0
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12
    ODD = 13
    EVEN = 14

class DayOfMonth(enum.IntFlag):
    """This enumeration indicates specific days of the month by specific date ("1", "22", and so on) or by relative position ("last day of month", "even day of month", and so on)."""

    UNSPECIFIED = 0
    DAY1 = 1
    DAY2 = 2
    DAY3 = 3
    DAY4 = 4
    DAY5 = 5
    DAY6 = 6
    DAY7 = 7
    DAY8 = 8
    DAY9 = 9
    DAY10 = 10
    DAY11 = 11
    DAY12 = 12
    DAY13 = 13
    DAY14 = 14
    DAY15 = 15
    DAY16 = 16
    DAY17 = 17
    DAY18 = 18
    DAY19 = 19
    DAY20 = 20
    DAY21 = 21
    DAY22 = 22
    DAY23 = 23
    DAY24 = 24
    DAY25 = 25
    DAY26 = 26
    DAY27 = 27
    DAY28 = 28
    DAY29 = 29
    DAY30 = 30
    DAY31 = 31
    LAST_DAY_OF_MONTH = 32
    ODD_DAY_OF_MONTH = 33
    EVEN_DAY_OF_MONTH = 34

class DayOfWeek(enum.IntFlag):
    """This enumeration indicates each of the seven days of the week, or "unspecified"."""

    UNSPECIFIED = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

class DateType(ns0.datatypes.Structure):
    """This structure defines a calendar date. It allows to define a concrete date, e.g. 2022-02-12. By using wildcards, it also allows to define repeating dates, like every Wednesday, every odd day of a month, every 24th of December, every last day of a month in 2023, etc."""

    @property
    def year(self) -> o6.UInt16: ...
    @year.setter
    def year(self, value: _Integer) -> None: ...
    @property
    def month(self) -> Month: ...
    @month.setter
    def month(self, value: _Integer) -> None: ...
    @property
    def dayOfMonth(self) -> DayOfMonth: ...
    @dayOfMonth.setter
    def dayOfMonth(self, value: _Integer) -> None: ...
    @property
    def dayOfWeek(self) -> DayOfWeek: ...
    @dayOfWeek.setter
    def dayOfWeek(self, value: _Integer) -> None: ...

class DateRangeType(ns0.datatypes.Structure):
    """This structure defines a time span, with absolute start and end dates. The StartDate and EndDate are limited to specific values, i.e., wild cards like odd months are not allowed. The Year field shall not be 0; the Month field shall be a value between 1 to 12; the DayOfMonth field shall be between 1 to 31 and the DayOfMonth field shall be "unspecified"."""

    @property
    def startDate(self) -> DateType: ...
    @startDate.setter
    def startDate(self, value: DateType) -> None: ...
    @property
    def endDate(self) -> DateType: ...
    @endDate.setter
    def endDate(self, value: DateType) -> None: ...

class CalendarEntryType(ns0.datatypes.Union):
    """This union that defines various calendar date values"""

    @property
    def date(self) -> DateType: ...
    @date.setter
    def date(self, value: DateType) -> None: ...
    @property
    def dateRange(self) -> DateRangeType: ...
    @dateRange.setter
    def dateRange(self, value: DateRangeType) -> None: ...

class SpecialEventPeriodType(ns0.datatypes.Union):
    """This union contains a calendar entry or a reference to a calendar object"""

    @property
    def calendarEntry(self) -> CalendarEntryType: ...
    @calendarEntry.setter
    def calendarEntry(self, value: CalendarEntryType) -> None: ...
    @property
    def calendarReference(self) -> o6.NodeId: ...
    @calendarReference.setter
    def calendarReference(self, value: o6.NodeId) -> None: ...

class BaseActionType(ns0.datatypes.Structure):
    """This abstract structure defines the base of an action. The base only contains information, if the last execution of the action was successful."""

    @property
    def lastActionResult(self) -> o6.StatusCode: ...
    @lastActionResult.setter
    def lastActionResult(self, value: _Integer) -> None: ...

class WriteLocalVariableActionType(BaseActionType):
    """This structure defines an action to write the value of a Variable managed in the same Server where the action is used."""

    @property
    def lastActionResult(self) -> o6.StatusCode: ...
    @lastActionResult.setter
    def lastActionResult(self, value: _Integer) -> None: ...
    @property
    def variable(self) -> o6.NodeId: ...
    @variable.setter
    def variable(self, value: o6.NodeId) -> None: ...
    @property
    def value(self) -> Any: ...
    @value.setter
    def value(self, value: Any) -> None: ...

class CallLocalMethodActionType(BaseActionType):
    """This structure defines an action to call a Method of an Object managed in the same Server where the action is used."""

    @property
    def lastActionResult(self) -> o6.StatusCode: ...
    @lastActionResult.setter
    def lastActionResult(self, value: _Integer) -> None: ...
    @property
    def objectId(self) -> o6.NodeId: ...
    @objectId.setter
    def objectId(self, value: o6.NodeId) -> None: ...
    @property
    def methodId(self) -> o6.NodeId: ...
    @methodId.setter
    def methodId(self, value: o6.NodeId) -> None: ...
    @property
    def inputValues(self) -> list[Any]: ...
    @inputValues.setter
    def inputValues(self, value: Sequence[Any]) -> None: ...
    @property
    def lastOutputValues(self) -> list[Any]: ...
    @lastOutputValues.setter
    def lastOutputValues(self, value: Sequence[Any]) -> None: ...

class TimeType(ns0.datatypes.Structure):
    """This structure that represents a point in time during a day"""

    @property
    def hour(self) -> o6.Byte: ...
    @hour.setter
    def hour(self, value: _Integer) -> None: ...
    @property
    def minute(self) -> o6.Byte: ...
    @minute.setter
    def minute(self, value: _Integer) -> None: ...
    @property
    def second(self) -> o6.Byte: ...
    @second.setter
    def second(self, value: _Integer) -> None: ...

class TimeActionsType(ns0.datatypes.Structure):
    """This structure contains a time and an array of actions. It is used to define actions to be executed at a specific point in time."""

    @property
    def time(self) -> TimeType: ...
    @time.setter
    def time(self, value: TimeType) -> None: ...
    @property
    def actions(self) -> list[BaseActionType]: ...
    @actions.setter
    def actions(self, value: Sequence[BaseActionType]) -> None: ...

class SpecialEventType(ns0.datatypes.Structure):
    """This structure contains a period, a list of time values, and a priority. It is a means to identify moments in time over one or more days."""

    @property
    def period(self) -> SpecialEventPeriodType: ...
    @period.setter
    def period(self, value: SpecialEventPeriodType) -> None: ...
    @property
    def listOfTimeActions(self) -> list[TimeActionsType]: ...
    @listOfTimeActions.setter
    def listOfTimeActions(self, value: Sequence[TimeActionsType]) -> None: ...
    @property
    def eventPriority(self) -> o6.Byte: ...
    @eventPriority.setter
    def eventPriority(self, value: _Integer) -> None: ...

class DailyScheduleType(ns0.datatypes.Structure):
    """This structure defines a sequence of TimeActionsType structures. Each element in the sequence defines a time/actions pair that describes the actions to be executed at a given point in the day."""

    @property
    def daySchedule(self) -> list[TimeActionsType]: ...
    @daySchedule.setter
    def daySchedule(self, value: Sequence[TimeActionsType]) -> None: ...
