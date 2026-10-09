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

"""Generated OPC UA surface_technology_mss namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.irdi as irdi
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.machinery_processvalues as machinery_processvalues
import o6.ns.ns0 as ns0
import o6.ns.padim as padim
import o6.ns.surface_technology as surface_technology

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=surface_technology_mss;i=1003", browseName="ns=surface_technology_mss;STSysMaterialTransportLineType", displayName="STSysMaterialTransportLineType")
class STSysMaterialTransportLineType(surface_technology.objtypes.STSysType):
    description: ns0.objtypes.FolderType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology_mss;i=1004", browseName="ns=surface_technology_mss;STCompPowderVibrationType", displayName="STCompPowderVibrationType")
class STCompPowderVibrationType(surface_technology.objtypes.STCompType):
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology_mss;i=1005", browseName="ns=surface_technology_mss;STSysVesselType", displayName="STSysVesselType")
class STSysVesselType(surface_technology.objtypes.STSysType):
    components: machinery.objtypes.MachineComponentsType | None
    description: ns0.objtypes.FolderType | None
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology_mss;i=1006", browseName="ns=surface_technology_mss;STSysRamType", displayName="STSysRamType")
class STSysRamType(surface_technology.objtypes.STSysType):
    components: machinery.objtypes.MachineComponentsType | None


@o6.objecttype(nodeId="ns=surface_technology_mss;i=1007", browseName="ns=surface_technology_mss;STCompStirrerType", displayName="STCompStirrerType")
class STCompStirrerType(surface_technology.objtypes.STCompType):
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology_mss;i=1008", browseName="ns=surface_technology_mss;STCompPowderSieveType", displayName="STCompPowderSieveType")
class STCompPowderSieveType(surface_technology.objtypes.STCompType):
    description: ns0.objtypes.FolderType | None


@o6.objecttype(nodeId="ns=surface_technology_mss;i=1009", browseName="ns=surface_technology_mss;STCompRamType", displayName="STCompRamType")
class STCompRamType(surface_technology.objtypes.STCompType):
    description: ns0.objtypes.FolderType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology_mss;i=1012", browseName="ns=surface_technology_mss;STCompProcessValveType", displayName="STCompProcessValveType")
class STCompProcessValveType(surface_technology.objtypes.STCompType):
    description: ns0.objtypes.FolderType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology_mss;i=1013", browseName="ns=surface_technology_mss;STCompHeaterType", displayName="STCompHeaterType")
class STCompHeaterType(surface_technology.objtypes.STCompType):
    description: ns0.objtypes.FolderType | None
    monitoring: machinery.objtypes.MonitoringType | None


del Any, TYPE_CHECKING, uuid, o6, di, ia, irdi, isa95_jobcontrol_v2, machinery, machinery_jobs, machinery_processvalues, ns0, padim, surface_technology
