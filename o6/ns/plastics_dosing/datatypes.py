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

"""Generated OPC UA plastics_dosing namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
import o6.ns.plastics_rubber as plastics_rubber

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=plastics_dosing;i=3003", browseName="ns=plastics_dosing;ActivateRemoteControl")
class ActivateRemoteControl(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(0, name="OFF")
    SEPARATE_INTERFACE = o6.enumfield(1, name="SEPARATE_INTERFACE")
    OPC_UA = o6.enumfield(2, name="OPC_UA")


@o6.enumtype(nodeId="ns=plastics_dosing;i=3006", browseName="ns=plastics_dosing;RemoteControlActivated")
class RemoteControlActivated(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(0, name="OFF")
    SEPARATE_INTERFACE = o6.enumfield(1, name="SEPARATE_INTERFACE")
    OPC_UA = o6.enumfield(2, name="OPC_UA")


@o6.enumtype(nodeId="ns=plastics_dosing;i=3008", browseName="ns=plastics_dosing;ComponentStateEnumeration")
class ComponentStateEnumeration(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(0, name="Off")
    READY = o6.enumfield(1, name="Ready")
    DOSING = o6.enumfield(2, name="Dosing")
    CALIBRATION = o6.enumfield(3, name="Calibration")
    ERROR = o6.enumfield(4, name="Error")
    CLEANING = o6.enumfield(5, name="Cleaning")
    PURGING = o6.enumfield(6, name="Purging")
    PRIMING = o6.enumfield(7, name="Priming")


@o6.enumtype(nodeId="ns=plastics_dosing;i=3011", browseName="ns=plastics_dosing;DosingModeEnumeration")
class DosingModeEnumeration(ns0.datatypes.Enumeration):
    ONLY_CONVEYING = o6.enumfield(0, name="ONLY_CONVEYING")
    VOLUMETRIC = o6.enumfield(1, name="VOLUMETRIC")
    GRAVIMETRIC = o6.enumfield(2, name="GRAVIMETRIC")
    OTHER = o6.enumfield(3, name="OTHER")


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, plastics_rubber
