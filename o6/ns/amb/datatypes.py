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

"""Generated OPC UA amb namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as amb_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(nodeId="ns=amb;i=3002", browseName="RootCauseDataType", description="Root cause of an alarm", defaultEncodingId="ns=amb;i=5001")
class RootCauseDataType(ns0.datatypes.Structure):
    rootCauseId: o6.NodeId
    rootCause: o6.LocalizedText


@o6.datatype(
    nodeId="ns=amb;i=3003",
    browseName="NameNodeIdDataType",
    description="A human-readable name of something plus optionally the NodeId in case the something is represented in the AddressSpace",
    defaultEncodingId="ns=amb;i=5012",
)
class NameNodeIdDataType(ns0.datatypes.Structure):
    name: o6.LocalizedText
    nodeId: o6.NodeId


@o6.enumtype(nodeId="ns=amb;i=3004", browseName="MaintenanceMethodEnum")
class MaintenanceMethodEnum(ns0.datatypes.Enumeration):
    LOCAL = o6.enumfield(0, name="Local")
    REMOTE = o6.enumfield(1, name="Remote")


del Any, TYPE_CHECKING, uuid, o6, ns0, amb_reftypes
