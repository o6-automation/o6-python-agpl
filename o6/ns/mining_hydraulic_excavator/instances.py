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

"""Generated OPC UA mining_hydraulic_excavator namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.mining as mining
import o6.ns.mining_loading as mining_loading
import o6.ns.ns0 as ns0
from . import objtypes as mining_hydraulic_excavator_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes._3DCartesianCoordinatesType(
    nodeId="ns=mining_hydraulic_excavator;i=6008",
    browseName="CartesianCoordinates",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_hydraulic_excavator;i=6009", browseName="X", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_hydraulic_excavator;i=6010", browseName="Y", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_hydraulic_excavator;i=6011", browseName="Z", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes._3DCartesianCoordinates,
)
ns0.vartypes._3DOrientationType(
    nodeId="ns=mining_hydraulic_excavator;i=6012",
    browseName="Orientation",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_hydraulic_excavator;i=6013", browseName="A", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_hydraulic_excavator;i=6014", browseName="B", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_hydraulic_excavator;i=6015", browseName="C", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes._3DOrientation,
)
ns0.vartypes._3DFrameType(
    nodeId="ns=mining_hydraulic_excavator;i=6007",
    browseName="ns=mining_loading;ExclusionZone",
    description="The ExclusionZone property describes the area that haulage machines, which are to be loaded, are not allowed to enter when approaching the loading machine",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_hydraulic_excavator;i=6002", browseName="Constant", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_hydraulic_excavator;i=6003", browseName="FixedBase", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_hydraulic_excavator;i=6001", browseName="BaseFrame", dataType=o6.NodeId)),
        o6.hasComponent(o6.ns["ns=mining_hydraulic_excavator;i=6008"]),
        o6.hasComponent(o6.ns["ns=mining_hydraulic_excavator;i=6012"]),
    ],
    dataType=ns0.datatypes._3DFrame,
    valueRank=1,
    arrayDimensions=[0],
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMiningSlashLoadingSlashHydraulicExcavatorSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=mining_hydraulic_excavator;i=5005",
    browseName="ns=mining_hydraulic_excavator;http://opcfoundation.org/UA/Mining/Loading/HydraulicExcavator/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_hydraulic_excavator;i=6016", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_hydraulic_excavator;i=6017", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2022-09-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_hydraulic_excavator;i=6018", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Mining/Loading/HydraulicExcavator/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_hydraulic_excavator;i=6019", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_hydraulic_excavator;i=6020",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[2],
                value=[ns0.datatypes.IdType.NUMERIC, ns0.datatypes.IdType.STRING],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_hydraulic_excavator;i=6021", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_hydraulic_excavator;i=6022", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes._3DCartesianCoordinatesType(
    nodeId="ns=mining_hydraulic_excavator;i=6025",
    browseName="CartesianCoordinates",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_hydraulic_excavator;i=6026", browseName="X", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_hydraulic_excavator;i=6027", browseName="Y", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_hydraulic_excavator;i=6028", browseName="Z", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes._3DCartesianCoordinates,
)
ns0.vartypes._3DOrientationType(
    nodeId="ns=mining_hydraulic_excavator;i=6029",
    browseName="Orientation",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_hydraulic_excavator;i=6036", browseName="A", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_hydraulic_excavator;i=6037", browseName="B", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_hydraulic_excavator;i=6038", browseName="C", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes._3DOrientation,
)
ns0.vartypes._3DFrameType(
    nodeId="ns=mining_hydraulic_excavator;i=6024",
    browseName="ns=mining_loading;MachinePose",
    description="The MachinePose variable describes the pose of the loading machine in terms of location coordinates, orientation and (optional) base frame.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_hydraulic_excavator;i=6040", browseName="Constant", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_hydraulic_excavator;i=6041", browseName="FixedBase", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=mining_hydraulic_excavator;i=6025"]),
        o6.hasComponent(o6.ns["ns=mining_hydraulic_excavator;i=6029"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_hydraulic_excavator;i=6039", browseName="BaseFrame", dataType=o6.NodeId)),
    ],
    dataType=ns0.datatypes._3DFrame,
    value=ns0.datatypes._3DFrame(cartesianCoordinates=ns0.datatypes._3DCartesianCoordinates(x=0.0, y=0.0, z=0.0), orientation=ns0.datatypes._3DOrientation(a=0.0, b=0.0, c=0.0)),
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=mining_hydraulic_excavator;i=5004",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    references=[o6.hasComponent(o6.ns["ns=mining_hydraulic_excavator;i=6007"]), o6.hasComponent(o6.ns["ns=mining_hydraulic_excavator;i=6024"])],
)
mining.objtypes.MiningEquipmentIdentificationType(
    nodeId="ns=mining_hydraulic_excavator;i=5001",
    browseName="ns=mining_hydraulic_excavator;MiningEquipmentIdentification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_hydraulic_excavator;i=6004",
                browseName="ns=di;AssetId",
                description="To be used by end users to store a unique identification in the context of their overall application. Servers shall support at least 40 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 40 Unicode characters into that field.",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_hydraulic_excavator;i=6031",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose the MachineryItem is used.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_hydraulic_excavator;i=6032",
                browseName="ns=di;ManufacturerUri",
                description="A globally unique identifier of the manufacturer of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_hydraulic_excavator;i=6033",
                browseName="ns=di;Model",
                description="A human-readable, localized name of the model of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_hydraulic_excavator;i=6034",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_hydraulic_excavator;i=6035",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_hydraulic_excavator;i=6042",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(mining_hydraulic_excavator_objtypes.HydraulicExcavatorType, ns0.reftypes.HasAddIn, o6.ns["ns=mining_hydraulic_excavator;i=5001"])


ns0.vartypes.PropertyType(
    nodeId="ns=mining_hydraulic_excavator;i=6005",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_hydraulic_excavator;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="LoadingStartAcknowledged",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("The LoadingStartAcknowledged variable indicates whether the loading request was successful or not", "en"),
        )
    ],
)
o6.call(
    nodeId="ns=mining_hydraulic_excavator;i=7001",
    browseName="ns=mining_loading;RequestForLoading",
    description="The RequestForLoading method is called by a partnering machine when they want to start the loading procedure.",
    outputArgs=o6.hasProperty(o6.ns["ns=mining_hydraulic_excavator;i=6005"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=mining_hydraulic_excavator;i=6006",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_hydraulic_excavator;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="LoadingStopAcknowledged",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("The LoadingStartAcknowledged variable indicates whether the loading request was successful or not", "en"),
        )
    ],
)
o6.call(
    nodeId="ns=mining_hydraulic_excavator;i=7002",
    browseName="ns=mining_loading;StopLoading",
    description="The StopLoading method is called by a partnering machine when they want to abort the loading procedure",
    outputArgs=o6.hasProperty(o6.ns["ns=mining_hydraulic_excavator;i=6006"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=mining_hydraulic_excavator;i=6043",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_hydraulic_excavator;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="PositioningCompleteResult",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("The PositioningComplete method is called by a partnering machine when they have completed the positioning procedure.", "en"),
        )
    ],
)
o6.call(
    nodeId="ns=mining_hydraulic_excavator;i=7003",
    browseName="ns=mining_loading;PositioningComplete",
    description="The PositioningComplete method is called by a partnering machine when they have finished to position themselves in front of the loading machine",
    outputArgs=o6.hasProperty(o6.ns["ns=mining_hydraulic_excavator;i=6043"]),
)

ns0.objtypes.BaseObjectType(
    nodeId="ns=mining_hydraulic_excavator;i=5003",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    references=[
        o6.hasComponent(o6.ns["ns=mining_hydraulic_excavator;i=7001"]),
        o6.hasComponent(o6.ns["ns=mining_hydraulic_excavator;i=7002"]),
        o6.hasComponent(o6.ns["ns=mining_hydraulic_excavator;i=7003"]),
    ],
)
mining_loading.objtypes.LoadingMachineType(
    nodeId="ns=mining_hydraulic_excavator;i=5002",
    browseName="ns=mining_hydraulic_excavator;LoadingMachine",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=mining_hydraulic_excavator;i=5003"]), o6.hasComponent(o6.ns["ns=mining_hydraulic_excavator;i=5004"])],
)
o6.reference(mining_hydraulic_excavator_objtypes.HydraulicExcavatorType, ns0.reftypes.HasAddIn, o6.ns["ns=mining_hydraulic_excavator;i=5002"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, mining, mining_loading, ns0, mining_hydraulic_excavator_objtypes
