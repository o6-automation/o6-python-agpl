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

"""Generated OPC UA surface_technology_cleaning namespace declarations."""

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


@o6.objecttype(nodeId="ns=surface_technology_cleaning;i=1003", browseName="ns=surface_technology_cleaning;STCompCoolerType", displayName="STCompCoolerType")
class STCompCoolerType(surface_technology.objtypes.STCompType):
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology_cleaning;i=1004", browseName="ns=surface_technology_cleaning;STCompCondenserType", displayName="STCompCondenserType")
class STCompCondenserType(surface_technology.objtypes.STCompType):
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology_cleaning;i=1005", browseName="ns=surface_technology_cleaning;STSysTreatmentType", displayName="STSysTreatmentType")
class STSysTreatmentType(surface_technology.objtypes.STSysType):
    components: machinery.objtypes.MachineComponentsType | None


@o6.objecttype(nodeId="ns=surface_technology_cleaning;i=1007", browseName="ns=surface_technology_cleaning;STCompDryerType", displayName="STCompDryerType")
class STCompDryerType(surface_technology.objtypes.STCompType):
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology_cleaning;i=1010", browseName="ns=surface_technology_cleaning;STCompHeaterType", displayName="STCompHeaterType")
class STCompHeaterType(surface_technology.objtypes.STCompType):
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology_cleaning;i=1013", browseName="ns=surface_technology_cleaning;STCompPressurizedAirType", displayName="STCompPressurizedAirType")
class STCompPressurizedAirType(surface_technology.objtypes.STCompType):
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology_cleaning;i=1016", browseName="ns=surface_technology_cleaning;STCompPumpType", displayName="STCompPumpType")
class STCompPumpType(surface_technology.objtypes.STCompType):
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology_cleaning;i=1019", browseName="ns=surface_technology_cleaning;STCompStirrerType", displayName="STCompStirrerType")
class STCompStirrerType(surface_technology.objtypes.STCompType):
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology_cleaning;i=1022", browseName="ns=surface_technology_cleaning;STCompUltrasonicEmitterType", displayName="STCompUltrasonicEmitterType")
class STCompUltrasonicEmitterType(surface_technology.objtypes.STCompType):
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology_cleaning;i=1025", browseName="ns=surface_technology_cleaning;STCompValveType", displayName="STCompValveType")
class STCompValveType(surface_technology.objtypes.STCompType):
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology_cleaning;i=1028", browseName="ns=surface_technology_cleaning;STCompVesselType", displayName="STCompVesselType")
class STCompVesselType(surface_technology.objtypes.STCompType):
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology_cleaning;i=1031", browseName="ns=surface_technology_cleaning;STSysAuxiliaryType", displayName="STSysAuxiliaryType")
class STSysAuxiliaryType(surface_technology.objtypes.STSysType):
    components: machinery.objtypes.MachineComponentsType | None
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology_cleaning;i=1034", browseName="ns=surface_technology_cleaning;STSysCleaningType", displayName="STSysCleaningType")
class STSysCleaningType(surface_technology.objtypes.STSysType):
    components: machinery.objtypes.MachineComponentsType | None


@o6.objecttype(nodeId="ns=surface_technology_cleaning;i=1037", browseName="ns=surface_technology_cleaning;STSysConveyorType", displayName="STSysConveyorType")
class STSysConveyorType(surface_technology.objtypes.STSysType):
    components: machinery.objtypes.MachineComponentsType | None
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology_cleaning;i=1040", browseName="ns=surface_technology_cleaning;STSysDryingType", displayName="STSysDryingType")
class STSysDryingType(surface_technology.objtypes.STSysType):
    components: machinery.objtypes.MachineComponentsType | None
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology_cleaning;i=1043", browseName="ns=surface_technology_cleaning;STSysHandlingType", displayName="STSysHandlingType")
class STSysHandlingType(surface_technology.objtypes.STSysType):
    components: machinery.objtypes.MachineComponentsType | None
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology_cleaning;i=1046", browseName="ns=surface_technology_cleaning;STSysMaterialSupplyType", displayName="STSysMaterialSupplyType")
class STSysMaterialSupplyType(surface_technology.objtypes.STSysType):
    components: machinery.objtypes.MachineComponentsType | None


@o6.objecttype(nodeId="ns=surface_technology_cleaning;i=1049", browseName="ns=surface_technology_cleaning;STSysQualityControlType", displayName="STSysQualityControlType")
class STSysQualityControlType(surface_technology.objtypes.STSysType):
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology_cleaning;i=1052", browseName="ns=surface_technology_cleaning;STSysRinsingType", displayName="STSysRinsingType")
class STSysRinsingType(surface_technology.objtypes.STSysType):
    components: machinery.objtypes.MachineComponentsType | None


del Any, TYPE_CHECKING, uuid, o6, di, ia, irdi, isa95_jobcontrol_v2, machinery, machinery_jobs, machinery_processvalues, ns0, padim, surface_technology
