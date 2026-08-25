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

"""Generated OPC UA lads namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.amb as amb
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


@o6.enumtype(nodeId="ns=lads;i=3000", browseName="MaintenanceTaskResultEnum", description="This enumeration defines the different results when executing a Task..")
class MaintenanceTaskResultEnum(ns0.datatypes.Enumeration):
    SUCCESS = o6.enumfield(0, name="Success")
    FAILURE = o6.enumfield(1, name="Failure")
    UNDETERMINED = o6.enumfield(2, name="Undetermined")


@o6.datatype(
    nodeId="ns=lads;i=3002",
    browseName="SampleInfoType",
    description="This DataType contains metadata for a sample, specifically data on the identification and location of the sample in a container.",
    defaultEncodingId="ns=lads;i=5042",
)
class SampleInfoType(ns0.datatypes.Structure):
    containerId: o6.String
    sampleId: o6.String
    position: o6.String
    customData: o6.String


@o6.datatype(
    nodeId="ns=lads;i=3003",
    browseName="KeyValueType",
    description="A key-value pair similar to 0:KeyValuePair which uses 0:String instead of 0:Qualifiedname for easu of use.",
    defaultEncodingId="ns=lads;i=5045",
)
class KeyValueType(ns0.datatypes.Structure):
    key: o6.String
    value: o6.String


del Any, TYPE_CHECKING, uuid, o6, amb, di, ia, machinery, ns0
