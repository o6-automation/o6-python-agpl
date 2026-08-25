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

"""Generated OPC UA mining namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
from . import datatypes as mining_datypes
from . import vartypes as mining_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

machinery.objtypes.MachineComponentsType(
    nodeId="ns=mining;i=5010", browseName="ns=mining;Components", description="The components add-in contains placeholders for sub-components of an equipment asset"
)
machinery.objtypes.MonitoringType(nodeId="ns=mining;i=5011", browseName="ns=machinery;Monitoring")
machinery.objtypes.MachineryEquipmentFolderType(nodeId="ns=mining;i=5012", browseName="ns=machinery;MachineryEquipment")
machinery.objtypes.NotificationsType(nodeId="ns=mining;i=5013", browseName="ns=machinery;Notifications")
ns0.objtypes.FolderType(nodeId="ns=mining;i=5016", browseName="ns=machinery;MachineryBuildingBlocks")
o6.reference(o6.ns["ns=mining;i=5016"], "i=17604", o6.ns["ns=mining;i=5010"])
o6.reference(o6.ns["ns=mining;i=5016"], "i=17604", o6.ns["ns=mining;i=5011"])
o6.reference(o6.ns["ns=mining;i=5016"], "i=17604", o6.ns["ns=mining;i=5012"])
o6.reference(o6.ns["ns=mining;i=5016"], "i=17604", o6.ns["ns=mining;i=5013"])


@o6.objecttype(
    nodeId="ns=mining;i=1002",
    browseName="ns=mining;MiningEquipmentType",
    displayName="MiningEquipmentType",
    description="The MiningEquipmentType ObjectType describes the abstract blueprint for any type of mining field equipment or machinery",
    isAbstract=True,
)
class MiningEquipmentType(di.objtypes.TopologyElementType):
    components: machinery.objtypes.MachineComponentsType | None = o6.hasAddIn(o6.ns["ns=mining;i=5010"])
    machineProperties: ns0.objtypes.FolderType | None = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=mining;i=5015", browseName="ns=mining;MachineProperties"))
    machineryBuildingBlocks: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=mining;i=5016"])
    machineryEquipment: machinery.objtypes.MachineryEquipmentFolderType | None = o6.hasComponent(o6.ns["ns=mining;i=5012"])
    methodSet: ns0.objtypes.BaseObjectType | None = o6.hasComponent(
        ns0.objtypes.BaseObjectType(nodeId="ns=mining;i=5014", browseName="ns=di;MethodSet", description="Flat list of Methods")
    )
    miningEquipmentIdentification: MiningEquipmentIdentificationType | None
    monitoring: machinery.objtypes.MonitoringType | None = o6.hasComponent(o6.ns["ns=mining;i=5011"])
    notifications: machinery.objtypes.NotificationsType | None = o6.hasComponent(o6.ns["ns=mining;i=5013"])


@o6.objecttype(
    nodeId="ns=mining;i=1003", browseName="ns=mining;MiningEquipmentIdentificationType", displayName="MiningEquipmentIdentificationType", interfaces=[di.objtypes.ISupportInfoType]
)
class MiningEquipmentIdentificationType(machinery.objtypes.MachineIdentificationType):
    assetId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mining;i=6027",
            browseName="ns=di;AssetId",
            description="To be used by end users to store a unique identification in the context of their overall application. Servers shall support at least 40 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 40 Unicode characters into that field.",
            dataType=o6.String,
            value="",
        )
    )
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mining;i=6026",
            browseName="ns=mining;DefaultInstanceBrowseName",
            description="The default BrowseName for instances of this type",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("mining:MiningEquipmentIdentification"),
        )
    )
    deviceClass: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mining;i=6032",
            browseName="ns=di;DeviceClass",
            description="Indicates in which domain or for what purpose the MachineryItem is used.",
            dataType=o6.String,
            value="",
        )
    )
    deviceTypeImage: ns0.objtypes.FolderType | None
    documentation: ns0.objtypes.FolderType | None
    imageSet: ns0.objtypes.FolderType | None
    manufacturerUri: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mining;i=6028",
            browseName="ns=di;ManufacturerUri",
            description="A globally unique identifier of the manufacturer of the MachineryItem.",
            dataType=o6.String,
            value="",
        )
    )
    model: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mining;i=6029",
            browseName="ns=di;Model",
            description="A human-readable, localized name of the model of the MachineryItem.",
            dataType=o6.LocalizedText,
            value=o6.LocalizedText(),
        )
    )
    protocolSupport: ns0.objtypes.FolderType | None


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, mining_datypes, mining_vartypes
