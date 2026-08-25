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
from . import datatypes as scheduler_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.PropertyType(
    nodeId="ns=scheduler;i=41",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scheduler;i=40",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CalendarEntries", dataType=o6.NodeId("ns=scheduler;i=72"), valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scheduler;i=42",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scheduler;i=40",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="EntryResults", dataType=o6.Int32, valueRank=1, arrayDimensions=[0])],
)
o6.call(
    nodeId="ns=scheduler;i=40",
    browseName="ns=scheduler;AddDateListElements",
    description="Adds elements to the DateList",
    inputArgs=o6.hasProperty(o6.ns["ns=scheduler;i=41"]),
    outputArgs=o6.hasProperty(o6.ns["ns=scheduler;i=42"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=scheduler;i=44",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scheduler;i=43",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CalendarEntries", dataType=o6.NodeId("ns=scheduler;i=72"), valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scheduler;i=45",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scheduler;i=43",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="EntryResults", dataType=o6.Int32, valueRank=1, arrayDimensions=[0])],
)
o6.call(
    nodeId="ns=scheduler;i=43",
    browseName="ns=scheduler;RemoveDateListElements",
    description="Removes elements of the DateList",
    inputArgs=o6.hasProperty(o6.ns["ns=scheduler;i=44"]),
    outputArgs=o6.hasProperty(o6.ns["ns=scheduler;i=45"]),
)


@o6.objecttype(
    nodeId="ns=scheduler;i=37",
    browseName="ns=scheduler;CalendarType",
    displayName="CalendarType",
    description="Provides a list of calendar dates. Each entry in the list describes a specific date or date pattern, or range of dates",
)
class CalendarType(ns0.objtypes.BaseObjectType):
    addDateListElements: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scheduler;i=40"])
    dateList: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scheduler;i=39",
            browseName="ns=scheduler;DateList",
            description="Array of elements each defining either a specific date or date pattern, or range of dates",
            dataType=scheduler_datypes.CalendarEntryType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    presentValue: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scheduler;i=38",
            browseName="ns=scheduler;PresentValue",
            description="Indicates if the current date is in the DateList (true) or not (false)",
            dataType=o6.Boolean,
        )
    )
    removeDateListElements: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scheduler;i=43"])


ns0.vartypes.PropertyType(
    nodeId="ns=scheduler;i=55",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scheduler;i=54",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="SpecialEvents", dataType=o6.NodeId("ns=scheduler;i=70"), valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scheduler;i=56",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scheduler;i=54",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="EntryResults", dataType=o6.Int32, valueRank=1, arrayDimensions=[0])],
)
o6.call(
    nodeId="ns=scheduler;i=54",
    browseName="ns=scheduler;AddExceptionScheduleElements",
    description="Adds elements to the ExceptionSchedule",
    inputArgs=o6.hasProperty(o6.ns["ns=scheduler;i=55"]),
    outputArgs=o6.hasProperty(o6.ns["ns=scheduler;i=56"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=scheduler;i=58",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scheduler;i=57",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="SpecialEvents", dataType=o6.NodeId("ns=scheduler;i=70"), valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scheduler;i=59",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scheduler;i=57",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="EntryResults", dataType=o6.Int32, valueRank=1, arrayDimensions=[0])],
)
o6.call(
    nodeId="ns=scheduler;i=57",
    browseName="ns=scheduler;RemoveExceptionScheduleElements",
    description="Removes elements from the ExceptionSchedule",
    inputArgs=o6.hasProperty(o6.ns["ns=scheduler;i=58"]),
    outputArgs=o6.hasProperty(o6.ns["ns=scheduler;i=59"]),
)


@o6.objecttype(
    nodeId="ns=scheduler;i=52",
    browseName="ns=scheduler;ScheduleType",
    displayName="ScheduleType",
    description="Defines a periodic schedule that can recur over a range of dates. The schedule may have optional exceptions at arbitrary times or dates. The basic unit of a schedule is days, which are divided into two types: normal days within a week and exception days. A priority mechanism defines which scheduled event is currently valid. The schedule includes a PresentValue Variable whose value describes the current state of the schedule, including a default value when no schedules are in effect.",
)
class ScheduleType(ns0.objtypes.BaseObjectType):
    addExceptionScheduleElements: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scheduler;i=54"])
    applyLastAfterStart: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scheduler;i=63",
            browseName="ns=scheduler;ApplyLastAfterStart",
            description="The ApplyLastAfterStart Property defines if the last set of actions shall be applied when starting the schedule Object",
            dataType=o6.Boolean,
        )
    )
    effectivePeriod: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scheduler;i=62",
            browseName="ns=scheduler;EffectivePeriod",
            description="Specifies the range of dates within which the schedule Object is active. Upon entering its effective period, the object shall execute the defined actions at the defined times, otherwise it shall not execute any actions.",
            dataType=scheduler_datypes.DateRangeType,
        )
    )
    exceptionSchedule: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scheduler;i=53",
            browseName="ns=scheduler;ExceptionSchedule",
            description="An array of special events. If present, each of those special events describes a sequence of schedule actions that take precedence over a normal day's behaviour on a special day or days.",
            dataType=scheduler_datypes.SpecialEventType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    localTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scheduler;i=61",
            browseName="LocalTime",
            description="Provides information about the local time of the schedule Object. All scheduled times are UTC time. Clients need to consider this Property to calculate the local time of the schedule. If this Property is changed, it is server-specific whether the times of the schedule are adjusted or not.",
            dataType=ns0.datatypes.TimeZoneDataType,
        )
    )
    removeExceptionScheduleElements: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scheduler;i=57"])
    weeklySchedule: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scheduler;i=60",
            browseName="ns=scheduler;WeeklySchedule",
            description="Each entry represents one day of the week. The first entry in the array represents Monday, the last Sunday. Each element describes a sequence of times and a list of actions that provides a sequence of schedule actions on one day of the week when no ExceptionSchedule is in effect.",
            dataType=scheduler_datypes.DailyScheduleType,
            valueRank=1,
            arrayDimensions=[7],
        )
    )


del Any, TYPE_CHECKING, uuid, o6, ns0, scheduler_datypes
