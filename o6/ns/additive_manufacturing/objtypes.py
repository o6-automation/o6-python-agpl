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

"""Generated OPC UA additive_manufacturing namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.irdi as irdi
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machine_tool as machine_tool
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.machinery_processvalues as machinery_processvalues
import o6.ns.ns0 as ns0
import o6.ns.padim as padim
from . import datatypes as additive_manufacturing_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=additive_manufacturing;i=1003", browseName="ns=additive_manufacturing;EquipmentAMType", displayName="EquipmentAMType")
class EquipmentAMType(machine_tool.objtypes.EquipmentType):
    feedstock: FeedstockListType | None


@o6.objecttype(
    nodeId="ns=additive_manufacturing;i=1005",
    browseName="ns=additive_manufacturing;AdditiveManufacturingType",
    displayName="AdditiveManufacturingType",
    description="The AdditiveManufacturingType represents the entire additive manufacturing interface of this information model. It is the entry point to the OPC UA interface of an AM machine and provides a basic structure. An instance of this type aggregates all information related to one AM machine.",
)
class AdditiveManufacturingType(machine_tool.objtypes.MachineToolType):
    equipment: EquipmentAMType
    identification: MachineIdentificationAMType
    machineryBuildingBlocks: ns0.objtypes.FolderType | None
    monitoring: machine_tool.objtypes.MonitoringType


@o6.objecttype(nodeId="ns=additive_manufacturing;i=1000", browseName="ns=additive_manufacturing;FeedstockType", displayName="FeedstockType")
class FeedstockType(ns0.objtypes.BaseObjectType):
    cycle: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=additive_manufacturing;i=6012", browseName="ns=additive_manufacturing;Cycle", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1
        )
    )
    externalIdentifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=additive_manufacturing;i=6009", browseName="ns=additive_manufacturing;ExternalIdentifier", dataType=o6.String, accessLevel=3, userAccessLevel=1
        )
    )
    function: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=additive_manufacturing;i=6015",
            browseName="ns=additive_manufacturing;Function",
            dataType=additive_manufacturing_datypes.FeedstockFunction,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    identifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=additive_manufacturing;i=6008", browseName="ns=additive_manufacturing;Identifier", dataType=o6.String, accessLevel=3, userAccessLevel=1
        )
    )
    manufacturer: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=additive_manufacturing;i=6011", browseName="ns=additive_manufacturing;Manufacturer", dataType=o6.String, accessLevel=3, userAccessLevel=1
        )
    )
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=additive_manufacturing;i=6010", browseName="ns=additive_manufacturing;Name", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    readyForProduction: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=additive_manufacturing;i=6013", browseName="ns=additive_manufacturing;ReadyForProduction", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
        )
    )
    remainingQuantity: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=additive_manufacturing;i=1002",
    browseName="ns=additive_manufacturing;ProcessValueAMType",
    displayName="ProcessValueAMType",
    description="The ProcessValueAMType provides sensor monitoring information of an AM machine.",
)
class ProcessValueAMType(machinery_processvalues.objtypes.ProcessValueType):
    category: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=additive_manufacturing;i=6063",
            browseName="ns=additive_manufacturing;Category",
            dataType=additive_manufacturing_datypes.SensorCategory,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    severity: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=additive_manufacturing;i=6064",
            browseName="ns=additive_manufacturing;Severity",
            dataType=additive_manufacturing_datypes.SensorSeverity,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=additive_manufacturing;i=1001",
    browseName="ns=additive_manufacturing;FeedstockListType",
    displayName="FeedstockListType",
    description="The MaterialListType represents a list of materials",
)
class FeedstockListType(ns0.objtypes.BaseObjectType):
    langleFeedstockRangle: FeedstockType
    nodeVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=additive_manufacturing;i=6073", browseName="NodeVersion", dataType=o6.String)
    )


@o6.objecttype(
    nodeId="ns=additive_manufacturing;i=1004",
    browseName="ns=additive_manufacturing;MachineIdentificationAMType",
    displayName="MachineIdentificationAMType",
    description="The MachineIdentificationAMType of the Additive Manufacturing information model holds static data which shall uniquely identify an AM machine among a pool of the AM machine operating entity.",
)
class MachineIdentificationAMType(machine_tool.objtypes.MachineToolIdentificationType):
    aMTechnologyIdentifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=additive_manufacturing;i=6078", browseName="ns=additive_manufacturing;AMTechnologyIdentifier", dataType=o6.String, accessLevel=3, userAccessLevel=1
        )
    )


del Any, TYPE_CHECKING, uuid, o6, di, ia, irdi, isa95_jobcontrol_v2, machine_tool, machinery, machinery_jobs, machinery_processvalues, ns0, padim, additive_manufacturing_datypes
