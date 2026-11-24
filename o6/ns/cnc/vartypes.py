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

"""Generated OPC UA cnc namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import datatypes as cnc_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(
    nodeId="ns=cnc;i=2001",
    browseName="ns=cnc;CncPositionVariableType",
    displayName="CncPositionVariableType",
    description="Group of position values.",
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
)
class CncPositionVariableType(ns0.vartypes.BaseDataVariableType):
    actPos: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=cnc;i=6046", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
        )
    )
    cmdPos: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=cnc;i=6044", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
        )
    )
    eURange: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6881", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)
    )
    engineeringUnits: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6829", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
    )
    remDist: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=cnc;i=6050", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
        )
    )


del Any, TYPE_CHECKING, uuid, o6, ns0, cnc_datypes
