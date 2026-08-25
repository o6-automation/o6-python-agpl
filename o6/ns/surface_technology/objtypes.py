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

"""Generated OPC UA surface_technology namespace declarations."""

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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

machinery.objtypes.MachineComponentsType(nodeId="ns=surface_technology;i=5003", browseName="ns=machinery;Components")


@o6.objecttype(nodeId="ns=surface_technology;i=1003", browseName="ns=surface_technology;STSysType", displayName="STSysType", isAbstract=True)
class STSysType(ns0.objtypes.BaseObjectType):
    components: machinery.objtypes.MachineComponentsType | None = o6.hasAddIn(o6.ns["ns=surface_technology;i=5003"])
    description: ns0.objtypes.FolderType | None = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology;i=5006", browseName="ns=surface_technology;Description"))
    identification: machinery.objtypes.MachineIdentificationType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType
    monitoring: machinery.objtypes.MonitoringType | None


@o6.objecttype(nodeId="ns=surface_technology;i=1006", browseName="ns=surface_technology;STCompType", displayName="STCompType", isAbstract=True)
class STCompType(ns0.objtypes.BaseObjectType):
    description: ns0.objtypes.FolderType | None = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=surface_technology;i=5016", browseName="ns=surface_technology;Description"))
    identification: machinery.objtypes.MachineryComponentIdentificationType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType
    monitoring: machinery.objtypes.MonitoringType | None


ns0.objtypes.FolderType(nodeId="ns=surface_technology;i=5026", browseName="ns=machinery;MachineryBuildingBlocks")


@o6.objecttype(nodeId="ns=surface_technology;i=1009", browseName="ns=surface_technology;STSystemControllerType", displayName="STSystemControllerType", isAbstract=True)
class STSystemControllerType(ns0.objtypes.BaseObjectType):
    machineryBuildingBlocks: ns0.objtypes.FolderType = o6.hasComponent(o6.ns["ns=surface_technology;i=5026"])
    state: ns0.objtypes.FolderType


@o6.objecttype(nodeId="ns=surface_technology;i=1004", browseName="ns=surface_technology;STBaseControllerType", displayName="STBaseControllerType")
class STBaseControllerType(STSystemControllerType):
    shutDown: ns0.objtypes.ProgramStateMachineType | None
    startUp: ns0.objtypes.ProgramStateMachineType | None


ns0.vartypes.PropertyType(
    nodeId="ns=surface_technology;i=6091",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=surface_technology;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="AliasName", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("The alias to be assigned to a particular node")),
        ns0.datatypes.Argument(name="ReferenceID", dataType=o6.NodeId, valueRank=-1, description=o6.LocalizedText("The ID of the reference that should apply to the new alias")),
        ns0.datatypes.Argument(name="Target", dataType=o6.ExpandedNodeId, valueRank=-1, description=o6.LocalizedText("The exact node to which the alias should be assigned to")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=surface_technology;i=6092",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=surface_technology;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AliasNode", dataType=o6.NodeId, valueRank=-1, description=o6.LocalizedText("The ID of the node that has now been assigned the alias"))],
)
o6.call(
    nodeId="ns=surface_technology;i=7002",
    browseName="ns=surface_technology;AddAlias",
    inputArgs=o6.hasProperty(o6.ns["ns=surface_technology;i=6091"]),
    outputArgs=o6.hasProperty(o6.ns["ns=surface_technology;i=6092"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=surface_technology;i=6093",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=surface_technology;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="AliasName", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("The alias that has to be removed")),
        ns0.datatypes.Argument(name="ReferenceID", dataType=o6.NodeId, valueRank=-1, description=o6.LocalizedText("The ID of the reference that has to be removed")),
    ],
)
o6.call(nodeId="ns=surface_technology;i=7003", browseName="ns=surface_technology;RemoveAlias", inputArgs=o6.hasProperty(o6.ns["ns=surface_technology;i=6093"]))


@o6.objecttype(nodeId="ns=surface_technology;i=1008", browseName="ns=surface_technology;STJobManagementType", displayName="STJobManagementType")
class STJobManagementType(machinery_jobs.objtypes.JobManagementType):
    addAlias: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=surface_technology;i=7002"])
    removeAlias: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=surface_technology;i=7003"])
    sTJobManagementAliases: ns0.objtypes.AliasNameCategoryType | None


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, ns0
