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

"""Generated OPC UA cutting_tool namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.gms as gms
import o6.ns.ia as ia
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machine_tool as machine_tool
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.machinery_result as machinery_result
import o6.ns.ns0 as ns0
from . import datatypes as cutting_tool_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=cutting_tool;i=1021", browseName="ns=cutting_tool;ToolMeasuringMachineType", displayName="ToolMeasuringMachineType")
class ToolMeasuringMachineType(gms.objtypes.GMSType):
    fileSystem: ns0.objtypes.FileDirectoryType
    machineryBuildingBlocks: ns0.objtypes.FolderType


@o6.objecttype(nodeId="ns=cutting_tool;i=1025", browseName="ns=cutting_tool;ToolManufacturingMachineType", displayName="ToolManufacturingMachineType")
class ToolManufacturingMachineType(machine_tool.objtypes.MachineToolType):
    fileSystem: ns0.objtypes.FileDirectoryType
    machineryBuildingBlocks: ns0.objtypes.FolderType


@o6.objecttype(nodeId="ns=cutting_tool;i=1003", browseName="ns=cutting_tool;CuttingToolFileType", displayName="CuttingToolFileType")
class CuttingToolFileType(ns0.objtypes.FileType):
    fileFormat: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=cutting_tool;i=6070", browseName="ns=cutting_tool;FileFormat", dataType=cutting_tool_datypes.FileFormatDataType, accessLevel=3, userAccessLevel=1
        )
    )


del Any, TYPE_CHECKING, uuid, o6, di, gms, ia, isa95_jobcontrol_v2, machine_tool, machinery, machinery_jobs, machinery_result, ns0, cutting_tool_datypes
