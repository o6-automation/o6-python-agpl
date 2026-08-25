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


@o6.enumtype(nodeId="ns=woodworking;i=20", browseName="WwUnitModeEnumeration", description="This enumeration represents the generalized mode of a unit.")
class WwUnitModeEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    AUTOMATIC = o6.enumfield(1, name="AUTOMATIC")
    SEMIAUTOMATIC = o6.enumfield(2, name="SEMIAUTOMATIC")
    MANUAL = o6.enumfield(3, name="MANUAL")
    SETUP = o6.enumfield(4, name="SETUP")
    SLEEP = o6.enumfield(5, name="SLEEP")


@o6.enumtype(nodeId="ns=woodworking;i=21", browseName="WwUnitStateEnumeration", description="This enumeration represents the generalized state of a unit.")
class WwUnitStateEnumeration(ns0.datatypes.Enumeration):
    OFFLINE = o6.enumfield(0, name="OFFLINE")
    STANDBY = o6.enumfield(1, name="STANDBY")
    READY = o6.enumfield(2, name="READY")
    WORKING = o6.enumfield(3, name="WORKING")
    ERROR = o6.enumfield(4, name="ERROR")


@o6.datatype(
    nodeId="ns=woodworking;i=3002",
    browseName="WwMessageArgumentValueDataType",
    description="The WwArgumentValueDataType definition defines the possible types of an argument value.",
    defaultEncodingId="ns=woodworking;i=5010",
)
class WwMessageArgumentValueDataType(ns0.datatypes.Union):
    array: list[WwMessageArgumentValueDataType]
    boolean: o6.Boolean
    int16: o6.Int16
    int32: o6.Int32
    int64: o6.Int64
    sByte: o6.SByte
    uInt16: o6.UInt16
    uInt32: o6.UInt32
    uInt64: o6.UInt64
    byte: o6.Byte
    dateTime: o6.DateTime
    guid: o6.Guid
    localizedText: o6.LocalizedText
    double: o6.Double
    float: o6.Float
    string: o6.String
    other: o6.String


@o6.datatype(
    nodeId="ns=woodworking;i=3003",
    browseName="WwMessageArgumentDataType",
    description="The WwArgumentDataType definition extends the argument structure with an argument value.",
    defaultEncodingId="ns=woodworking;i=5013",
)
class WwMessageArgumentDataType(ns0.datatypes.Argument):
    name: o6.String
    dataType: o6.NodeId
    valueRank: o6.Int32
    arrayDimensions: list[o6.UInt32]
    description: o6.LocalizedText
    value: WwMessageArgumentValueDataType


@o6.enumtype(nodeId="ns=woodworking;i=3004", browseName="WwEventCategoryEnumeration", description="This enumeration represents the category of an event.")
class WwEventCategoryEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    DIAGNOSTIC = o6.enumfield(1, name="DIAGNOSTIC")
    INFORMATION = o6.enumfield(2, name="INFORMATION")
    WARNING = o6.enumfield(3, name="WARNING")
    ALARM = o6.enumfield(4, name="ALARM")
    ERROR = o6.enumfield(5, name="ERROR")


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, ns0
