# Copyright (c) 2026 o6 Automation GmbH
#
# SPDX-License-Identifier: AGPL-3.0-or-later
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

"""Generated OPC UA woodworking namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=woodworking;i=20", browseName="ns=woodworking;WwUnitModeEnumeration", description="This enumeration represents the generalized mode of a unit.")
class WwUnitModeEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    AUTOMATIC = o6.enumfield(1, name="AUTOMATIC")
    SEMIAUTOMATIC = o6.enumfield(2, name="SEMIAUTOMATIC")
    MANUAL = o6.enumfield(3, name="MANUAL")
    SETUP = o6.enumfield(4, name="SETUP")
    SLEEP = o6.enumfield(5, name="SLEEP")


@o6.enumtype(nodeId="ns=woodworking;i=21", browseName="ns=woodworking;WwUnitStateEnumeration", description="This enumeration represents the generalized state of a unit.")
class WwUnitStateEnumeration(ns0.datatypes.Enumeration):
    OFFLINE = o6.enumfield(0, name="OFFLINE")
    STANDBY = o6.enumfield(1, name="STANDBY")
    READY = o6.enumfield(2, name="READY")
    WORKING = o6.enumfield(3, name="WORKING")
    ERROR = o6.enumfield(4, name="ERROR")


@o6.datatype(
    nodeId="ns=woodworking;i=3002",
    browseName="ns=woodworking;WwMessageArgumentValueDataType",
    description="The WwArgumentValueDataType definition defines the possible types of an argument value.",
    defaultEncodingId="ns=woodworking;i=5010",
)
class WwMessageArgumentValueDataType(ns0.datatypes.Union):
    array: list[WwMessageArgumentValueDataType] = o6.field(name="Array", arrayDimensions=[1])
    boolean: o6.Boolean = o6.field(name="Boolean")
    int16: o6.Int16 = o6.field(name="Int16")
    int32: o6.Int32 = o6.field(name="Int32")
    int64: o6.Int64 = o6.field(name="Int64")
    sByte: o6.SByte = o6.field(name="SByte")
    uInt16: o6.UInt16 = o6.field(name="UInt16")
    uInt32: o6.UInt32 = o6.field(name="UInt32")
    uInt64: o6.UInt64 = o6.field(name="UInt64")
    byte: o6.Byte = o6.field(name="Byte")
    dateTime: o6.DateTime = o6.field(name="DateTime")
    guid: o6.Guid = o6.field(name="Guid")
    localizedText: o6.LocalizedText = o6.field(name="LocalizedText")
    double: o6.Double = o6.field(name="Double")
    float: o6.Float = o6.field(name="Float")
    string: o6.String = o6.field(name="String")
    other: o6.String = o6.field(name="Other")


@o6.datatype(
    nodeId="ns=woodworking;i=3003",
    browseName="ns=woodworking;WwMessageArgumentDataType",
    description="The WwArgumentDataType definition extends the argument structure with an argument value.",
    defaultEncodingId="ns=woodworking;i=5013",
)
class WwMessageArgumentDataType(ns0.datatypes.Argument):
    name: o6.String = o6.field(name="Name")
    dataType: o6.NodeId = o6.field(name="DataType")
    valueRank: o6.Int32 = o6.field(name="ValueRank")
    arrayDimensions: list[o6.UInt32] = o6.field(name="ArrayDimensions")
    description: o6.LocalizedText = o6.field(name="Description")
    value: WwMessageArgumentValueDataType = o6.field(name="Value")


@o6.enumtype(nodeId="ns=woodworking;i=3004", browseName="ns=woodworking;WwEventCategoryEnumeration", description="This enumeration represents the category of an event.")
class WwEventCategoryEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    DIAGNOSTIC = o6.enumfield(1, name="DIAGNOSTIC")
    INFORMATION = o6.enumfield(2, name="INFORMATION")
    WARNING = o6.enumfield(3, name="WARNING")
    ALARM = o6.enumfield(4, name="ALARM")
    ERROR = o6.enumfield(5, name="ERROR")


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, ns0
