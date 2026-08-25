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

"""Generated OPC UA paefs namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.irdi as irdi
import o6.ns.machinery as machinery
import o6.ns.machinery_processvalues as machinery_processvalues
import o6.ns.ns0 as ns0
import o6.ns.padim as padim
from . import reftypes as paefs_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=paefs;i=3002", browseName="AnalogDigitalEnum", description="Specifies the type of a sensor")
class AnalogDigitalEnum(ns0.datatypes.Enumeration):
    ANALOG = o6.enumfield(0, name="Analog")
    DIGITAL = o6.enumfield(1, name="Digital")


@o6.enumtype(nodeId="ns=paefs;i=3003", browseName="ControlModeEnum", description="Describes the possibility of controlling the system externally")
class ControlModeEnum(ns0.datatypes.Enumeration):
    AUTOMATIC = o6.enumfield(0, name="Automatic")
    MANUAL = o6.enumfield(1, name="Manual")
    OTHER = o6.enumfield(2, name="Other")


@o6.enumtype(
    nodeId="ns=paefs;i=3005",
    browseName="AirConnectionOpenEnum",
    description="Describes whether the air connection is open, i.e., it is in a state in which air can be passed through",
)
class AirConnectionOpenEnum(ns0.datatypes.Enumeration):
    OPEN = o6.enumfield(0, name="Open")
    CLOSED = o6.enumfield(1, name="Closed")
    OPENING = o6.enumfield(2, name="Opening")
    CLOSING = o6.enumfield(3, name="Closing")


@o6.enumtype(nodeId="ns=paefs;i=3006", browseName="FilterAidDeviceStatusEnum", description="Describes the action performed by the device for filter aid")
class FilterAidDeviceStatusEnum(ns0.datatypes.Enumeration):
    DEVICE_ACTIVE = o6.enumfield(0, name="DeviceActive")
    DEVICE_INACTIVE = o6.enumfield(1, name="DeviceInactive")
    FILLING_ACTIVE = o6.enumfield(2, name="FillingActive")
    DISCHARGE_ACTIVE = o6.enumfield(3, name="DischargeActive")


del Any, TYPE_CHECKING, uuid, o6, di, ia, irdi, machinery, machinery_processvalues, ns0, padim, paefs_reftypes
