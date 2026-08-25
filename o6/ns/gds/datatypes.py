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

"""Generated OPC UA gds namespace declarations."""

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


@o6.datatype(nodeId="ns=gds;i=1", browseName="ApplicationRecordDataType", defaultEncodingId="ns=gds;i=134")
class ApplicationRecordDataType(ns0.datatypes.Structure):
    applicationId: o6.NodeId
    applicationUri: o6.String
    applicationType: ns0.datatypes.ApplicationType
    applicationNames: list[o6.LocalizedText]
    productUri: o6.String
    discoveryUrls: list[o6.String]
    serverCapabilities: list[o6.String]


del Any, TYPE_CHECKING, uuid, o6, ns0
