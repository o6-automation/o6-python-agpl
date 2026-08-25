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

"""Generated OPC UA di namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as di_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=di;i=331", browseName="SoftwareVersionFileType")
class SoftwareVersionFileType(ns0.datatypes.Enumeration):
    CURRENT = o6.enumfield(0, name="Current")
    PENDING = o6.enumfield(1, name="Pending")
    FALLBACK = o6.enumfield(2, name="Fallback")


@o6.enumtype(nodeId="ns=di;i=333", browseName="UpdateBehavior")
class UpdateBehavior:
    KEEPS_PARAMETERS = o6.enumfield(0, name="KeepsParameters")
    WILL_DISCONNECT = o6.enumfield(1, name="WillDisconnect")
    REQUIRES_POWER_CYCLE = o6.enumfield(2, name="RequiresPowerCycle")
    WILL_REBOOT = o6.enumfield(3, name="WillReboot")
    NEEDS_PREPARATION = o6.enumfield(4, name="NeedsPreparation")


@o6.enumtype(nodeId="ns=di;i=408", browseName="SoftwareClass")
class SoftwareClass(ns0.datatypes.Enumeration):
    FIRMWARE = o6.enumfield(0, name="Firmware")
    APPLICATION = o6.enumfield(1, name="Application")
    CONFIGURATION = o6.enumfield(2, name="Configuration")
    SOLUTION = o6.enumfield(3, name="Solution")


@o6.enumtype(nodeId="ns=di;i=410", browseName="LocationIndicationType")
class LocationIndicationType:
    VISUAL = o6.enumfield(0, name="Visual")
    AUDIBLE = o6.enumfield(1, name="Audible")


@o6.enumtype(nodeId="ns=di;i=6244", browseName="DeviceHealthEnumeration")
class DeviceHealthEnumeration(ns0.datatypes.Enumeration):
    NORMAL = o6.enumfield(0, name="NORMAL")
    FAILURE = o6.enumfield(1, name="FAILURE")
    CHECK_FUNCTION = o6.enumfield(2, name="CHECK_FUNCTION")
    OFF_SPEC = o6.enumfield(3, name="OFF_SPEC")
    MAINTENANCE_REQUIRED = o6.enumfield(4, name="MAINTENANCE_REQUIRED")


@o6.datatype(nodeId="ns=di;i=6522", browseName="FetchResultDataType", defaultEncodingId="ns=di;i=6551", isAbstract=True)
class FetchResultDataType(ns0.datatypes.Structure):
    pass


@o6.datatype(nodeId="ns=di;i=6525", browseName="ParameterResultDataType", defaultEncodingId="ns=di;i=6554")
class ParameterResultDataType(ns0.datatypes.Structure):
    nodePath: list[o6.QualifiedName]
    statusCode: o6.StatusCode
    diagnostics: o6.DiagnosticInfo


@o6.datatype(nodeId="ns=di;i=15888", browseName="TransferResultErrorDataType", defaultEncodingId="ns=di;i=15891")
class TransferResultErrorDataType(FetchResultDataType):
    status: o6.Int32
    diagnostics: o6.DiagnosticInfo


@o6.datatype(nodeId="ns=di;i=15889", browseName="TransferResultDataDataType", defaultEncodingId="ns=di;i=15892")
class TransferResultDataDataType(FetchResultDataType):
    sequenceNumber: o6.Int32
    endOfResults: o6.Boolean
    parameterDefs: list[ParameterResultDataType]


del Any, TYPE_CHECKING, uuid, o6, ns0, di_reftypes
