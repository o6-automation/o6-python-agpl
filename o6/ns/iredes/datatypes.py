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

"""Generated OPC UA iredes namespace declarations."""

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


@o6.datatype(nodeId="ns=iredes;i=3000", browseName="ns=iredes;IRtextShort", parent="i=12")
class IRtextShort:
    pass


@o6.datatype(nodeId="ns=iredes;i=3001", browseName="ns=iredes;IRtext", parent="i=12")
class IRtext:
    pass


@o6.datatype(nodeId="ns=iredes;i=3002", browseName="ns=iredes;IRtextLong", parent="i=12")
class IRtextLong:
    pass


@o6.datatype(nodeId="ns=iredes;i=3003", browseName="ns=iredes;IRLengthDataType", defaultEncodingId="ns=iredes;i=5001")
class IRLengthDataType(ns0.datatypes.Structure):
    value: o6.Double = o6.field(name="Value")
    unit: ns0.datatypes.EUInformation = o6.field(name="Unit")


@o6.datatype(nodeId="ns=iredes;i=3004", browseName="ns=iredes;JobAssignmentTimeDataType", defaultEncodingId="ns=iredes;i=5004")
class JobAssignmentTimeDataType(ns0.datatypes.Union):
    expectedFinishTime: o6.DateTime = o6.field(name="ExpectedFinishTime")
    expectedDuration: o6.Double = o6.field(name="ExpectedDuration")


@o6.datatype(nodeId="ns=iredes;i=3005", browseName="ns=iredes;IRangle", parent="i=10")
class IRangle:
    pass


@o6.enumtype(nodeId="ns=iredes;i=3006", browseName="ns=iredes;DispFlag")
class DispFlag(ns0.datatypes.Enumeration):
    MACH_START = o6.enumfield(0, name="MachStart")
    FILE_LOAD = o6.enumfield(1, name="FileLoad")


@o6.datatype(nodeId="ns=iredes;i=3007", browseName="ns=iredes;IRVersion", parent="i=12")
class IRVersion:
    pass


@o6.datatype(nodeId="ns=iredes;i=3008", browseName="ns=iredes;AnyURI", parent="i=12")
class AnyURI:
    pass


@o6.enumtype(nodeId="ns=iredes;i=3009", browseName="ns=iredes;Answer")
class Answer(ns0.datatypes.Enumeration):
    ACCEPTED = o6.enumfield(0, name="Accepted")
    DELAYED = o6.enumfield(1, name="Delayed")
    ACCEPTED_WITH_CONDITION = o6.enumfield(2, name="AcceptedWithCondition")
    DENIED = o6.enumfield(3, name="Denied")


@o6.enumtype(nodeId="ns=iredes;i=3012", browseName="ns=iredes;LTPPMptFromType")
class LTPPMptFromType(ns0.datatypes.Enumeration):
    LOAD_PT = o6.enumfield(0, name="LoadPt")
    DUMP_PT = o6.enumfield(1, name="DumpPt")
    PARKING = o6.enumfield(2, name="Parking")
    WORKSHOP = o6.enumfield(3, name="Workshop")
    OTHERS = o6.enumfield(4, name="Others")


@o6.enumtype(nodeId="ns=iredes;i=3015", browseName="ns=iredes;LTPPMptToType")
class LTPPMptToType(ns0.datatypes.Enumeration):
    LOAD_PT = o6.enumfield(0, name="LoadPt")
    DUMP_PT = o6.enumfield(1, name="DumpPt")
    PARKING = o6.enumfield(2, name="Parking")
    BOULDER = o6.enumfield(3, name="Boulder")
    WORKSHOP = o6.enumfield(4, name="Workshop")
    OTHERS = o6.enumfield(5, name="Others")


@o6.enumtype(nodeId="ns=iredes;i=3018", browseName="ns=iredes;LTPPMaction")
class LTPPMaction(ns0.datatypes.Enumeration):
    LOAD = o6.enumfield(0, name="Load")
    DUMP = o6.enumfield(1, name="Dump")
    PARKING = o6.enumfield(2, name="Parking")
    WORKSHOP = o6.enumfield(3, name="Workshop")
    OTHER = o6.enumfield(4, name="Other")


del Any, TYPE_CHECKING, uuid, o6, ns0
