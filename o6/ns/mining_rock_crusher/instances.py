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

"""Generated OPC UA mining_rock_crusher namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.mining as mining
import o6.ns.ns0 as ns0
from . import objtypes as mining_rock_crusher_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

mining.objtypes.MiningEquipmentIdentificationType(
    nodeId="ns=mining_rock_crusher;i=5002",
    browseName="ns=mining;MiningEquipmentIdentification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rock_crusher;i=6001",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose the MachineryItem is used.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rock_crusher;i=6002",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rock_crusher;i=6003",
                browseName="ns=di;ManufacturerUri",
                description="A globally unique identifier of the manufacturer of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rock_crusher;i=6004",
                browseName="ns=di;Model",
                description="A human-readable, localized name of the model of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rock_crusher;i=6005",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rock_crusher;i=6006",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(mining_rock_crusher_objtypes.RockCrusherType, ns0.reftypes.HasAddIn, o6.ns["ns=mining_rock_crusher;i=5002"])
mining.objtypes.MiningEquipmentIdentificationType(
    nodeId="ns=mining_rock_crusher;i=5003",
    browseName="ns=mining;MiningEquipmentIdentification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rock_crusher;i=6007",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose the MachineryItem is used.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rock_crusher;i=6008",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rock_crusher;i=6009",
                browseName="ns=di;ManufacturerUri",
                description="A globally unique identifier of the manufacturer of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rock_crusher;i=6010",
                browseName="ns=di;Model",
                description="A human-readable, localized name of the model of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rock_crusher;i=6011",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rock_crusher;i=6012",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(mining_rock_crusher_objtypes.RockCrusherControlType, ns0.reftypes.HasAddIn, o6.ns["ns=mining_rock_crusher;i=5003"])
ns0.vartypes._3DCartesianCoordinatesType(
    nodeId="ns=mining_rock_crusher;i=6014",
    browseName="CartesianCoordinates",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rock_crusher;i=6015", browseName="X", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rock_crusher;i=6016", browseName="Y", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rock_crusher;i=6017", browseName="Z", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes._3DCartesianCoordinates,
)
ns0.vartypes._3DOrientationType(
    nodeId="ns=mining_rock_crusher;i=6018",
    browseName="Orientation",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rock_crusher;i=6019", browseName="A", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rock_crusher;i=6020", browseName="B", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rock_crusher;i=6021", browseName="C", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes._3DOrientation,
)
ns0.vartypes._3DFrameType(
    nodeId="ns=mining_rock_crusher;i=6013",
    browseName="ns=mining_rock_crusher;ExclusionZone",
    description="The ExclusionZone property describes the area that haulage machines, which are to be unloaded, are not allowed to enter when approaching the rock crusher system",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_rock_crusher;i=6024", browseName="Constant", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_rock_crusher;i=6025", browseName="FixedBase", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=mining_rock_crusher;i=6014"]),
        o6.hasComponent(o6.ns["ns=mining_rock_crusher;i=6018"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rock_crusher;i=6023", browseName="BaseFrame", dataType=o6.NodeId)),
    ],
    dataType=ns0.datatypes._3DFrame,
    valueRank=1,
    arrayDimensions=[0],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=mining_rock_crusher;i=5005",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=mining_rock_crusher;i=6013"])],
)
o6.reference(mining_rock_crusher_objtypes.RockCrusherControlType, ns0.reftypes.HasComponent, o6.ns["ns=mining_rock_crusher;i=5005"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMiningSlashMineralProcessingSlashRockCrusherSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=mining_rock_crusher;i=5006",
    browseName="ns=mining_rock_crusher;http://opcfoundation.org/UA/Mining/MineralProcessing/RockCrusher/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_rock_crusher;i=6026", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rock_crusher;i=6027", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2022-09-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rock_crusher;i=6028", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Mining/MineralProcessing/RockCrusher/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_rock_crusher;i=6029", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rock_crusher;i=6030",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[2],
                value=[ns0.datatypes.IdType.NUMERIC, ns0.datatypes.IdType.STRING],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rock_crusher;i=6031", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_rock_crusher;i=6032", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)


ns0.vartypes.PropertyType(
    nodeId="ns=mining_rock_crusher;i=6022",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_rock_crusher;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RequestUnloadingAcknowledged", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=mining_rock_crusher;i=7001", browseName="ns=mining_rock_crusher;RequestUnloading", outputArgs=o6.hasProperty(o6.ns["ns=mining_rock_crusher;i=6022"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=mining_rock_crusher;i=5004",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=mining_rock_crusher;i=7001"])],
)
o6.reference(mining_rock_crusher_objtypes.RockCrusherControlType, ns0.reftypes.HasComponent, o6.ns["ns=mining_rock_crusher;i=5004"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, mining, ns0, mining_rock_crusher_objtypes
