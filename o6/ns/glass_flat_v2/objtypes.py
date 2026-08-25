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

"""Generated OPC UA glass_flat_v2 namespace declarations."""

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
from . import datatypes as glass_flat_v2_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

machinery.objtypes.MachineryOperationCounterType(nodeId="ns=glass_flat_v2;i=5026", browseName="ns=di;OperationCounters")


@o6.objecttype(nodeId="ns=glass_flat_v2;i=1041", browseName="ns=glass_flat_v2;ManualFolderType", displayName="ManualFolderType")
class ManualFolderType(ns0.objtypes.FolderType):
    externalManuals: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat_v2;i=6176", browseName="ns=glass_flat_v2;ExternalManuals", dataType=ns0.datatypes.UriString, valueRank=1, arrayDimensions=[0]
        )
    )
    langleLocalManualsRangle: ns0.objtypes.FileType | None


@o6.objecttype(nodeId="ns=glass_flat_v2;i=1015", browseName="ns=glass_flat_v2;GlassMachineType", displayName="GlassMachineType")
class GlassMachineType(ns0.objtypes.BaseObjectType):
    components: machinery.objtypes.MachineComponentsType | None = o6.hasAddIn(
        machinery.objtypes.MachineComponentsType(nodeId="ns=glass_flat_v2;i=5002", browseName="ns=isa95_jobcontrol_v2;Components")
    )
    configurationRules: ConfigurationRulesType
    fileSystem: ns0.objtypes.FileDirectoryType
    identification: GlassMachineIdentificationType
    machineryBuildingBlocks: ns0.objtypes.FolderType
    maintenanceManuals: ManualFolderType | None = o6.hasComponent(ManualFolderType(nodeId="ns=glass_flat_v2;i=5009", browseName="ns=glass_flat_v2;MaintenanceManuals"))
    operationCounters: machinery.objtypes.MachineryOperationCounterType = o6.hasAddIn(o6.ns["ns=glass_flat_v2;i=5026"])
    operationManuals: ManualFolderType | None = o6.hasComponent(ManualFolderType(nodeId="ns=glass_flat_v2;i=5011", browseName="ns=glass_flat_v2;OperationManuals"))


@o6.objecttype(nodeId="ns=glass_flat_v2;i=1063", browseName="ns=glass_flat_v2;ConfigurationRulesType", displayName="ConfigurationRulesType")
class ConfigurationRulesType(ns0.objtypes.BaseObjectType):
    allowedEngineeringUnits: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat_v2;i=6186", browseName="ns=glass_flat_v2;AllowedEngineeringUnits", dataType=ns0.datatypes.EUInformation, valueRank=1, arrayDimensions=[0]
        )
    )
    allowedFileFormats: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat_v2;i=6174", browseName="ns=glass_flat_v2;AllowedFileFormats", dataType=glass_flat_v2_datypes.FileFormatDataType, valueRank=1, arrayDimensions=[0]
        )
    )
    machineProcessingCoordinateSystem: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat_v2;i=6188",
            browseName="ns=glass_flat_v2;MachineProcessingCoordinateSystem",
            dataType=glass_flat_v2_datypes.CoordinateSystemEnumeration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=glass_flat_v2;i=1030", browseName="ns=glass_flat_v2;GlassEventType", displayName="GlassEventType", isAbstract=True)
class GlassEventType(ns0.objtypes.BaseEventType):
    identifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=glass_flat_v2;i=6405", browseName="ns=glass_flat_v2;Identifier", accessLevel=3, userAccessLevel=1)
    )
    jobdIdentifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=glass_flat_v2;i=6410", browseName="ns=glass_flat_v2;JobdIdentifier", accessLevel=3, userAccessLevel=1)
    )
    location: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=glass_flat_v2;i=6406", browseName="ns=glass_flat_v2;Location", accessLevel=3, userAccessLevel=1)
    )
    materialIdentifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=glass_flat_v2;i=6411", browseName="ns=glass_flat_v2;MaterialIdentifier", accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=glass_flat_v2;i=1020", browseName="ns=glass_flat_v2;GlassMachineIdentificationType", displayName="GlassMachineIdentificationType")
class GlassMachineIdentificationType(machinery.objtypes.MachineIdentificationType):
    loggedInProfiles: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat_v2;i=6414", browseName="ns=glass_flat_v2;LoggedInProfiles", dataType=glass_flat_v2_datypes.UserProfileDataType, valueRank=1, arrayDimensions=[0]
        )
    )
    processingCategories: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat_v2;i=6029",
            browseName="ns=glass_flat_v2;ProcessingCategories",
            dataType=glass_flat_v2_datypes.ProcessingCategoryDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, ns0, glass_flat_v2_datypes
