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

"""Generated OPC UA fdi namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(nodeId="ns=fdi;i=37", browseName="RegistrationParameters", defaultEncodingId="ns=fdi;i=118")
class RegistrationParameters(ns0.datatypes.Structure):
    path: ns0.datatypes.RelativePath
    selectionFlags: o6.UInt32


@o6.datatype(nodeId="ns=fdi;i=38", browseName="RegisteredNode", defaultEncodingId="ns=fdi;i=119")
class RegisteredNode(ns0.datatypes.Structure):
    nodeStatus: o6.Int32
    onlineContextNodeId: o6.NodeId
    onlineDeviceNodeId: o6.NodeId
    offlineContextNodeId: o6.NodeId
    offlineDeviceNodeId: o6.NodeId


@o6.datatype(nodeId="ns=fdi;i=39", browseName="RegisterNodesResult", defaultEncodingId="ns=fdi;i=120")
class RegisterNodesResult(ns0.datatypes.Structure):
    status: o6.Int32
    registeredNodes: list[RegisteredNode]


@o6.datatype(nodeId="ns=fdi;i=43", browseName="TransferIncident", defaultEncodingId="ns=fdi;i=121")
class TransferIncident(ns0.datatypes.Structure):
    contextNodeId: o6.NodeId
    statusCode: o6.StatusCode
    diagnostics: o6.DiagnosticInfo


@o6.datatype(nodeId="ns=fdi;i=44", browseName="ApplyResult", defaultEncodingId="ns=fdi;i=122")
class ApplyResult(ns0.datatypes.Structure):
    status: o6.Int32
    transferIncidents: list[TransferIncident]


@o6.enumtype(nodeId="ns=fdi;i=194", browseName="WindowModeType")
class WindowModeType(ns0.datatypes.Enumeration):
    MODAL_WINDOW = o6.enumfield(1, name="ModalWindow")
    NON_MODAL_WINDOW = o6.enumfield(2, name="NonModalWindow")
    UIP = o6.enumfield(3, name="UIP")


@o6.enumtype(nodeId="ns=fdi;i=196", browseName="StyleType")
class StyleType(ns0.datatypes.Enumeration):
    WINDOW = o6.enumfield(1, name="Window")
    DIALOG = o6.enumfield(2, name="Dialog")


del Any, TYPE_CHECKING, uuid, o6, di, ns0
