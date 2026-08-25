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

"""Generated OPC UA weihenstephan namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
import o6.ns.pack_ml as pack_ml

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(
    nodeId="ns=weihenstephan;i=3000",
    browseName="WSOperatingModeEnumerationType",
    description="The operating mode provides information about the nature and extent of the intervention on the control equipment by the operators, and also via feedback from the equipment (DIN 19 237). This value must be coded in bit form or be documented as an integer for machines which are components of bottling systems:",
)
class WSOperatingModeEnumerationType(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(1, name="Off")
    MANUAL = o6.enumfield(2, name="Manual")
    SEMI_AUTOMATIC = o6.enumfield(4, name="Semi-automatic")
    AUTOMATIC = o6.enumfield(8, name="Automatic")


@o6.enumtype(
    nodeId="ns=weihenstephan;i=3001",
    browseName="WSProgramEnumerationType",
    description="The program is a consequent sequence of control instructions for a self-contained application-oriented function (DIN 19237). For bottling machines, bits or documented integer numbers must be used for machine operation with the following programs:",
)
class WSProgramEnumerationType(ns0.datatypes.Enumeration):
    UNDEFINED___NO__PROGRAM_ = o6.enumfield(0, name="Undefined (No Program)")
    PRODUCTION = o6.enumfield(1, name="Production")
    START__UP = o6.enumfield(2, name="Start Up")
    RUN__DOWN = o6.enumfield(4, name="Run Down")
    CLEAN = o6.enumfield(8, name="Clean")
    CHANGEOVER = o6.enumfield(16, name="Changeover")
    MAINTENANCE = o6.enumfield(32, name="Maintenance")
    BREAK = o6.enumfield(64, name="Break")


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, pack_ml
