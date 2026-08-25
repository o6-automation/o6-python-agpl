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

"""Generated OPC UA machine_tool namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.ns0 as ns0
from . import datatypes as machine_tool_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(nodeId="ns=machine_tool;i=61", browseName="ns=machine_tool;ToolLifeType", displayName="ToolLifeType", dataType=ns0.datatypes.Number)
class ToolLifeType(ns0.vartypes.BaseDataVariableType):
    engineeringUnits: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=285", browseName="ns=machine_tool;EngineeringUnits", dataType=ns0.datatypes.EUInformation)
    )
    indication: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=286", browseName="ns=machine_tool;Indication", dataType=machine_tool_datypes.ToolLifeIndication)
    )
    isCountingUp: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=411", browseName="ns=machine_tool;IsCountingUp", dataType=o6.Boolean)
    )
    limitValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=305", browseName="ns=machine_tool;LimitValue", dataType=ns0.datatypes.Number)
    )
    startValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=304", browseName="ns=machine_tool;StartValue", dataType=ns0.datatypes.Number)
    )
    warningValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=306", browseName="ns=machine_tool;WarningValue", dataType=ns0.datatypes.Number)
    )


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, ns0, machine_tool_datypes
