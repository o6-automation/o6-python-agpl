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

"""Generated OPC UA padim namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.irdi as irdi
import o6.ns.ns0 as ns0
from . import datatypes as padim_datypes
from . import vartypes as padim_vartypes
from . import objtypes as padim_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPADIMSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=padim;i=1000",
    browseName="ns=padim;http://opcfoundation.org/UA/PADIM/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1001",
                browseName="IsNamespaceSubset",
                description="If TRUE then the server only supports a subset of the namespace.",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1002",
                browseName="NamespacePublicationDate",
                description="The publication date for the namespace.",
                dataType=o6.DateTime,
                value=o6.DateTime("2025-11-10T00:00:00Z"),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1003", browseName="NamespaceUri", description="The URI of the namespace.", dataType=o6.String, value="http://opcfoundation.org/UA/PADIM/"
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1004",
                browseName="NamespaceVersion",
                description="The human readable string representing version of the namespace.",
                dataType=o6.String,
                value="1.02.0",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1005",
                browseName="StaticNodeIdTypes",
                description="A list of IdTypes for nodes which are the same in every server that exposes them.",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1006",
                browseName="StaticNumericNodeIdRange",
                description="A list of ranges for numeric node ids which are the same in every server that exposes them.",
                dataType=ns0.datatypes.NumericRange,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1007",
                browseName="StaticStringNodeIdPattern",
                description="A regular expression which matches string node ids are the same in every server that exposes them.",
                dataType=o6.String,
                value="",
            )
        ),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
di.objtypes.ConfigurableObjectType(
    nodeId="ns=padim;i=1025",
    browseName="ns=padim;SubDevices",
    modellingRule="Optional",
    references=[o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=padim;i=1026", browseName="ns=di;SupportedTypes"))],
)
o6.reference(padim_objtypes.PADIMType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1025"])
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1157",
    browseName="EnumValues",
    parent="ns=padim;i=1156",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("Application"), description=o6.LocalizedText("Reset only the application device parameters to their factory settings")
        ),
        ns0.datatypes.EnumValueType(
            value=2712, displayName=o6.LocalizedText("Communication"), description=o6.LocalizedText("Reset only the communication device parameters to their factory settings")
        ),
        ns0.datatypes.EnumValueType(value=2713, displayName=o6.LocalizedText("Factory"), description=o6.LocalizedText("Reset all device parameters to their factory settings")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1159",
    browseName="EnumValues",
    parent="ns=padim;i=1158",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Start"), description=o6.LocalizedText("Start the commissioning procedure")),
        ns0.datatypes.EnumValueType(value=255, displayName=o6.LocalizedText("Abort"), description=o6.LocalizedText("Abort the commissioning procedure, if it is being executed")),
    ],
)
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1160", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, value="", accessLevel=3)
o6.reference(o6.ns["ns=padim;i=1160"], "i=17597", "ns=irdi;s=0112/2///61987#ABB271#009")
padim_objtypes.SignalType(
    nodeId="ns=padim;i=1024", browseName="ns=padim;<SignalIdentifier>", modellingRule="OptionalPlaceholder", references=[o6.hasProperty(o6.ns["ns=padim;i=1160"])]
)
o6.reference(padim_objtypes.SignalSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1024"])
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1128",
    browseName="ns=padim;SensorType",
    displayName="Sensor type",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1161",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[27, 1],
                value=[
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK976#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK977#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK978#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK979#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK980#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK981#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK982#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK983#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK984#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK985#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK986#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK987#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK988#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK989#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK993#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK994#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK995#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK996#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK997#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK998#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK999#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABL000#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABL001#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABL002#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABL003#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABL004#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")],
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1162",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[27],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Cu1000", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Cu25", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Ni100", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Ni1000", "en")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Ni120", "en")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("Ni25", "en")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("Ni50", "en")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("Pt10", "en")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("Pt100", "en")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("Pt1000", "en")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("Pt200", "en")),
                    ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("Pt25", "en")),
                    ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("Pt50", "en")),
                    ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("Pt500", "en")),
                    ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("Type B: Pt30Rh-Pt6Rh", "en")),
                    ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("Type E: NiCr-CuNi", "en")),
                    ns0.datatypes.EnumValueType(value=16, displayName=o6.LocalizedText("Type J: Fe-CuNi", "en")),
                    ns0.datatypes.EnumValueType(value=17, displayName=o6.LocalizedText("Type K: NiCr-Ni", "en")),
                    ns0.datatypes.EnumValueType(value=18, displayName=o6.LocalizedText("Type N: NiCrSi-NiSi", "en")),
                    ns0.datatypes.EnumValueType(value=19, displayName=o6.LocalizedText("Type R: Pt13Rh-Pt", "en")),
                    ns0.datatypes.EnumValueType(value=20, displayName=o6.LocalizedText("Type S: Pt10Rh-Pt", "en")),
                    ns0.datatypes.EnumValueType(value=21, displayName=o6.LocalizedText("Type T: Cu-CuNi", "en")),
                    ns0.datatypes.EnumValueType(value=22, displayName=o6.LocalizedText("Type L: Fe-CuNi", "en")),
                    ns0.datatypes.EnumValueType(value=23, displayName=o6.LocalizedText("Type U: Cu-CuNi", "en")),
                    ns0.datatypes.EnumValueType(value=24, displayName=o6.LocalizedText("Type C: W5%-Re", "en")),
                    ns0.datatypes.EnumValueType(value=25, displayName=o6.LocalizedText("Type D: W3%-Re", "en")),
                    ns0.datatypes.EnumValueType(value=26, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1163",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABK984#001")],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1164", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Pt100", "en"))),
    ],
    dataType=o6.UInt32,
    valueRank=-2,
    value=8,
    accessLevel=3,
)
o6.reference(padim_vartypes.TemperatureMeasurementVariableType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1128"])
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1129",
    browseName="ns=padim;SensorConnection",
    displayName="Number of wires",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1165",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[4, 1],
                value=[
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABL113#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABL114#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABL115#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")],
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1166",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("4-wire", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("3-wire", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("2-wire", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1167",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABL113#001")],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1168", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("4-wire", "en"))),
    ],
    dataType=o6.UInt32,
    valueRank=-2,
    value=0,
    accessLevel=3,
)
o6.reference(padim_vartypes.TemperatureMeasurementVariableType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1129"])
o6.reference(o6.ns["ns=padim;i=1129"], "i=17597", "ns=irdi;s=0112/2///61987#ABB091#003")
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1130",
    browseName="ns=padim;SensorReference",
    displayName="Ref. junction",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1169",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[4, 1],
                value=[
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABN416#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABN417#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABK984#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")],
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1170",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("external cold junction", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("internal cold junction", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Pt100", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1171",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABN417#001")],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=padim;i=1172", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("internal cold junction", "en"))
        ),
    ],
    dataType=o6.UInt32,
    valueRank=-2,
    value=1,
    accessLevel=3,
)
o6.reference(padim_vartypes.TemperatureMeasurementVariableType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1130"])
o6.reference(o6.ns["ns=padim;i=1130"], "i=17597", "ns=irdi;s=0112/2///61987#ABB093#003")
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1132",
    browseName="ns=padim;FlowDirection",
    displayName="Flow direction",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1173",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[3, 1],
                value=[[o6.NodeId("ns=irdi;s=0112/2///61987#ABM885#001")], [o6.NodeId("ns=irdi;s=0112/2///61987#ABM886#001")], [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")]],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1174",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[3],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("positive", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("negative", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1175",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABM885#001")],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1176", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("positive", "en"))),
    ],
    dataType=o6.UInt32,
    valueRank=-2,
    value=0,
    accessLevel=3,
)
o6.reference(padim_vartypes.FlowMeasurementVariableType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1132"])
o6.reference(o6.ns["ns=padim;i=1132"], "i=17597", "ns=irdi;s=0112/2///61987#ABN594#003")
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1137",
    browseName="ns=padim;OperatingDirection",
    displayName="Operat. direction",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1177",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[3, 1],
                value=[[o6.NodeId("ns=irdi;s=0112/2///61987#ABL147#001")], [o6.NodeId("ns=irdi;s=0112/2///61987#ABL148#001")], [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")]],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1178",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[3],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("direct", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("reverse", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1179",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABL147#001")],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1180", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("direct", "en"))),
    ],
    dataType=o6.UInt32,
    value=0,
    accessLevel=3,
)
o6.reference(padim_vartypes.ControlVariableType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1137"])
o6.reference(o6.ns["ns=padim;i=1137"], "i=17597", "ns=irdi;s=0112/2///61987#ABD740#003")
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1138",
    browseName="ns=padim;ActuatorType",
    displayName="Actuator type",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1181",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[3, 1],
                value=[[o6.NodeId("ns=irdi;s=0112/2///61987#ABN145#001")], [o6.NodeId("ns=irdi;s=0112/2///61987#ABN146#001")], [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")]],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1182",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[3],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("sliding-stem linear", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("quarter-turn rotary", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1183",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABN145#001")],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=padim;i=1184", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("sliding-stem linear", "en"))
        ),
    ],
    dataType=o6.UInt32,
    value=0,
    accessLevel=3,
)
o6.reference(padim_vartypes.ControlVariableType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1138"])
o6.reference(o6.ns["ns=padim;i=1138"], "i=17597", "ns=irdi;s=0112/2///61987#ABD742#003")
padim_vartypes.TwoStateDiscreteSignalVariableType(
    nodeId="ns=padim;i=1040",
    browseName="ns=padim;TwoStateDiscreteSignal",
    displayName="Two-state I/O value",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1185", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("FALSE"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1186", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("TRUE"))),
    ],
    dataType=o6.Boolean,
    valueRank=-2,
    value=False,
    accessLevel=3,
)
o6.reference(padim_objtypes.TwoStateDiscreteSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1040"])
o6.reference(o6.ns["ns=padim;i=1040"], "i=17597", "ns=irdi;s=0112/2///61987#ABN635#002")
padim_vartypes.MultiStateDiscreteSignalVariableType(
    nodeId="ns=padim;i=1041",
    browseName="ns=padim;MultiStateDiscreteSignal",
    displayName="Multistate I/O value",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1187",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[11, 1],
                value=[
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABL215#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABL216#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABN836#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABM627#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABM625#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABN839#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABN840#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABN841#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABL213#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABL214#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")],
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1188",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[11],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("open", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("closed", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("in-between", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("high", "en")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("low", "en")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("moving", "en")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("true", "en")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("false", "en")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("on", "en")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("off", "en")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1189", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("false"))),
    ],
    dataType=o6.UInt32,
    value=7,
    accessLevel=3,
)
o6.reference(padim_objtypes.MultiStateDiscreteSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1041"])
o6.reference(o6.ns["ns=padim;i=1041"], "i=17597", "ns=irdi;s=0112/2///61987#ABN636#002")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1190", browseName="EngineeringUnits", displayName="Unit", dataType=ns0.datatypes.EUInformation)
o6.reference(o6.ns["ns=padim;i=1190"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
padim_vartypes.AnalogSignalVariableType(
    nodeId="ns=padim;i=1027",
    browseName="ns=padim;AnalogSignal",
    displayName="Value",
    modellingRule="Mandatory",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1190"]), o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1191", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
)
o6.reference(padim_objtypes.AnalogSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1027"])
o6.reference(o6.ns["ns=padim;i=1027"], "i=17597", "ns=irdi;s=0112/2///61987#ABN634#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1193",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741328, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
    ),
)
o6.reference(o6.ns["ns=padim;i=1193"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1192",
    browseName="ns=padim;ActuatorType",
    displayName="Actuator type",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1197",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[3, 1],
                value=[[o6.NodeId("ns=irdi;s=0112/2///61987#ABN145#001")], [o6.NodeId("ns=irdi;s=0112/2///61987#ABN146#001")], [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")]],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1198",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[3],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("sliding-stem linear", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("quarter-turn rotary", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1199",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABN145#001")],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=padim;i=1200", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("sliding-stem linear", "en"))
        ),
    ],
    dataType=o6.UInt32,
    value=0,
    accessLevel=3,
)
o6.reference(o6.ns["ns=padim;i=1192"], "i=17597", "ns=irdi;s=0112/2///61987#ABD742#003")
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1195",
    browseName="ns=padim;OperatingDirection",
    displayName="Operat. direction",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1201",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[3, 1],
                value=[[o6.NodeId("ns=irdi;s=0112/2///61987#ABL147#001")], [o6.NodeId("ns=irdi;s=0112/2///61987#ABL148#001")], [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")]],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1202",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[3],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("direct", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("reverse", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1203",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABL147#001")],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1204", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("direct", "en"))),
    ],
    dataType=o6.UInt32,
    value=0,
    accessLevel=3,
)
o6.reference(o6.ns["ns=padim;i=1195"], "i=17597", "ns=irdi;s=0112/2///61987#ABD740#003")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1205",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741328, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
    ),
)
o6.reference(o6.ns["ns=padim;i=1205"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.BaseAnalogType(
    nodeId="ns=padim;i=1136",
    browseName="ns=padim;Setpoint",
    modellingRule="Mandatory",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1205"])],
    dataType=o6.Float,
    valueRank=-2,
    value=0.0,
    accessLevel=3,
)
o6.reference(padim_vartypes.ControlVariableType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1136"])
o6.reference(o6.ns["ns=padim;i=1136"], "i=17597", "ns=irdi;s=0112/2///61987#ABN607#002")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1207",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741328, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
    ),
)
o6.reference(o6.ns["ns=padim;i=1207"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.BaseAnalogType(
    nodeId="ns=padim;i=1196", browseName="ns=padim;Setpoint", references=[o6.hasProperty(o6.ns["ns=padim;i=1207"])], dataType=o6.Float, value=0.0, accessLevel=3
)
o6.reference(o6.ns["ns=padim;i=1196"], "i=17597", "ns=irdi;s=0112/2///61987#ABN607#002")
padim_vartypes.ControlVariableType(
    nodeId="ns=padim;i=1031",
    browseName="ns=padim;ControlSignal",
    displayName="Readback",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(o6.ns["ns=padim;i=1193"]),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1194", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=100.0))),
        o6.hasComponent(o6.ns["ns=padim;i=1192"]),
        o6.hasComponent(o6.ns["ns=padim;i=1195"]),
        o6.hasComponent(o6.ns["ns=padim;i=1196"]),
    ],
    dataType=o6.Float,
    valueRank=-2,
    value=0.0,
    accessLevel=3,
)
o6.reference(padim_objtypes.ControlSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1031"])
o6.reference(o6.ns["ns=padim;i=1031"], "i=17597", "ns=irdi;s=0112/2///61987#ABJ683#001")
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1210",
    browseName="ns=padim;SensorClass",
    displayName="Set connected probe type",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1211",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[3, 1],
                value=[[o6.NodeId("ns=irdi;s=0112/2///61987#ABL238#001")], [o6.NodeId("ns=irdi;s=0112/2///61987#ABL239#001")], [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")]],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1212",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[3],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("RTD", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("TC", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1213",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABL238#001")],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1214", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("RTD", "en"))),
    ],
    dataType=o6.UInt32,
    valueRank=-2,
    value=0,
    accessLevel=3,
)
o6.reference(padim_vartypes.TemperatureMeasurementVariableType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1210"])
o6.reference(o6.ns["ns=padim;i=1210"], "i=17597", "ns=irdi;s=0112/2///61987#ABF288#004")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1225", browseName="EngineeringUnits", displayName="Unit", dataType=ns0.datatypes.EUInformation)
o6.reference(o6.ns["ns=padim;i=1225"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1228",
    browseName="ns=padim;OperatingDirection",
    displayName="Operating direction",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1234",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[3, 1],
                value=[[o6.NodeId("ns=irdi;s=0112/2///61987#ABL147#001")], [o6.NodeId("ns=irdi;s=0112/2///61987#ABL148#001")], [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")]],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1235",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[3],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("direct", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("reverse", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1236",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABL147#001")],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1237", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("direct", "en"))),
    ],
    dataType=o6.UInt32,
    value=0,
    accessLevel=3,
)
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=padim;i=1243",
    browseName="ns=padim;Setpoint",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1244", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("FALSE"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1245", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("TRUE"))),
    ],
    dataType=o6.Boolean,
    valueRank=-2,
    value=False,
    accessLevel=3,
)
padim_vartypes.TwoStateDiscreteControlVariableType(
    nodeId="ns=padim;i=1224",
    browseName="ns=padim;ControlSignal",
    displayName="Discrete two-state control value",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1241", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("FALSE"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1242", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("TRUE"))),
        o6.hasComponent(o6.ns["ns=padim;i=1228"]),
        o6.hasComponent(o6.ns["ns=padim;i=1243"]),
    ],
    dataType=o6.Boolean,
    valueRank=-2,
    value=False,
    accessLevel=3,
)
o6.reference(padim_objtypes.TwoStateDiscreteControlSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1224"])
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1246",
    browseName="ns=padim;Setpoint",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1250", browseName="EnumDictionaryEntries", dataType=o6.NodeId, valueRank=2, arrayDimensions=[11, 1])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1251", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[11])),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1252",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABN841#001")],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1253", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("false"))),
    ],
    dataType=o6.UInt32,
    value=7,
    accessLevel=3,
)
padim_vartypes.MultiStateDiscreteControlVariableType(
    nodeId="ns=padim;i=1240",
    browseName="ns=padim;ControlSignal",
    displayName="Discrete multi-state control value",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1247", browseName="EnumDictionaryEntries", dataType=o6.NodeId, valueRank=2)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1248", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1249", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("false"))),
        o6.hasComponent(o6.ns["ns=padim;i=1246"]),
    ],
    dataType=o6.UInt32,
    value=7,
    accessLevel=3,
)
o6.reference(padim_objtypes.MultiStateDiscreteControlSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1240"])
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1217",
    browseName="ns=padim;OperatingDirection",
    displayName="Operat. direction",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1254",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[3, 1],
                value=[[o6.NodeId("ns=irdi;s=0112/2///61987#ABL147#001")], [o6.NodeId("ns=irdi;s=0112/2///61987#ABL148#001")], [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")]],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1255",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[3],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("direct", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("reverse", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1256",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABL147#001")],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1257", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("direct", "en"))),
    ],
    dataType=o6.UInt32,
    value=0,
    accessLevel=3,
)
o6.reference(padim_vartypes.TwoStateDiscreteControlVariableType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1217"])
o6.reference(o6.ns["ns=padim;i=1217"], "i=17597", "ns=irdi;s=0112/2///61987#ABD740#003")
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=padim;i=1218",
    browseName="ns=padim;FaultState",
    displayName="Two-state fault value",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1258", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("FALSE"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1259", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("TRUE"))),
    ],
    dataType=o6.Boolean,
    value=False,
    accessLevel=3,
)
o6.reference(padim_vartypes.TwoStateDiscreteControlVariableType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1218"])
o6.reference(o6.ns["ns=padim;i=1218"], "i=17597", "ns=irdi;s=0112/2///61987#ABP543#002")
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=padim;i=1216",
    browseName="ns=padim;Setpoint",
    displayName="Two-state setpoint value",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1260", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("FALSE"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1261", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("TRUE"))),
    ],
    dataType=o6.Boolean,
    valueRank=-2,
    value=False,
    accessLevel=3,
)
o6.reference(padim_vartypes.TwoStateDiscreteControlVariableType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1216"])
o6.reference(o6.ns["ns=padim;i=1216"], "i=17597", "ns=irdi;s=0112/2///61987#ABP542#002")
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1222",
    browseName="ns=padim;FaultState",
    displayName="Multi-state fault value",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1262",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[11, 1],
                value=[
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABL215#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABL216#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABN836#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABM627#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABM625#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABN839#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABN840#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABN841#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABL213#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABL214#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")],
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1263",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[11],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("open", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("closed", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("in-between", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("high", "en")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("low", "en")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("moving", "en")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("true", "en")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("false", "en")),
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("on", "en")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("off", "en")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1264", browseName="ValueAsDictionaryEntries", dataType=o6.NodeId, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1265", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
)
o6.reference(padim_vartypes.MultiStateDiscreteControlVariableType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1222"])
o6.reference(o6.ns["ns=padim;i=1222"], "i=17597", "ns=irdi;s=0112/2///61987#ABP651#002")
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1221",
    browseName="ns=padim;OperatingDirection",
    displayName="Operat. direction",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1266",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[3, 1],
                value=[[o6.NodeId("ns=irdi;s=0112/2///61987#ABL147#001")], [o6.NodeId("ns=irdi;s=0112/2///61987#ABL148#001")], [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")]],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1267",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[3],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("direct", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("reverse", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1268",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABL147#001")],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1269", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("direct", "en"))),
    ],
    dataType=o6.UInt32,
    value=0,
    accessLevel=3,
)
o6.reference(padim_vartypes.MultiStateDiscreteControlVariableType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1221"])
o6.reference(o6.ns["ns=padim;i=1221"], "i=17597", "ns=irdi;s=0112/2///61987#ABD740#003")
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1220",
    browseName="ns=padim;Setpoint",
    displayName="Discrete multi-state setpoint value",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1270",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[11, 1],
                value=[
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABL215#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABL216#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABN836#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABM627#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABM625#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABN839#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABN840#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABN841#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABL213#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABL214#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")],
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1271",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[11],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("open", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("closed", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("in-between", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("high", "en")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("low", "en")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("moving", "en")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("true", "en")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("false", "en")),
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("on", "en")),
                    ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("off", "en")),
                    ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1272",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABN841#001")],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1273", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("false"))),
    ],
    dataType=o6.UInt32,
    value=7,
    accessLevel=3,
)
o6.reference(padim_vartypes.MultiStateDiscreteControlVariableType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1220"])
o6.reference(o6.ns["ns=padim;i=1220"], "i=17597", "ns=irdi;s=0112/2///61987#ABP645#002")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=padim;i=1277", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=padim;i=1278", browseName="Default XML")
o6.hasEncoding(padim_datypes.ChemicalSubstanceDataType, o6.ns["ns=padim;i=1278"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=1280",
    browseName="ns=padim;DeviceComponentConditions",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            padim_objtypes.GeneralDeviceConditionSetType(nodeId="ns=padim;i=1281", browseName="ns=padim;<DeviceComponentIdentifier>", modellingRule="OptionalPlaceholder")
        )
    ],
)
o6.reference(padim_objtypes.IGeneralDeviceConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1280"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=1285",
    browseName="ns=padim;DeviceComponentConditions",
    references=[
        o6.hasComponent(
            padim_objtypes.GeneralDeviceConditionSetType(nodeId="ns=padim;i=1287", browseName="ns=padim;<DeviceComponentIdentifier>", modellingRule="OptionalPlaceholder")
        )
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=1284",
    browseName="ns=padim;DeviceConditionSet",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=padim;i=1285"]),
        o6.hasComponent(padim_objtypes.GeneralDeviceConditionSetType(nodeId="ns=padim;i=1286", browseName="ns=padim;GeneralDeviceConditions")),
    ],
)
o6.reference(padim_objtypes.PADIMType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1284"])
o6.reference(o6.ns["ns=padim;i=1284"], "i=17603", padim_objtypes.IGeneralDeviceConditionSetType)
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1309",
    browseName="ns=padim;CalibrationTimestamp",
    displayName="Timestamp of calibration",
    dataType=o6.DateTime,
    value=o6.DateTime("1601-01-01T00:00:00Z"),
    accessLevel=3,
)
o6.reference(o6.ns["ns=padim;i=1309"], "i=17597", "ns=irdi;s=0112/2///61987#ABP544#001")
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1310",
    browseName="ns=padim;TypeOfCalibration",
    displayName="Type of calibration",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1311",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[4, 1],
                value=[
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP732#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP733#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP734#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")],
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1312",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("adjustment", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("calibration", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("custody transfer", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1313",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABP732#001")],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1314", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("adjustment", "en"))),
    ],
    dataType=o6.UInt32,
    value=0,
    accessLevel=3,
)
o6.reference(o6.ns["ns=padim;i=1310"], "i=17597", "ns=irdi;s=0112/2///61987#ABH609#002")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=1288",
    browseName="ns=padim;<SignalCalibrationIdentifier>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(o6.ns["ns=padim;i=1309"]),
        o6.hasComponent(padim_objtypes.CalibrationPointSetType(nodeId="ns=padim;i=1289", browseName="ns=padim;CalibrationPointSet")),
        o6.hasComponent(o6.ns["ns=padim;i=1310"]),
    ],
)
o6.reference(padim_objtypes.AnalogSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1288"])
o6.reference(o6.ns["ns=padim;i=1288"], "i=17603", padim_objtypes.ICalibrationType)
padim_vartypes.PatMeasurementVariableType(
    nodeId="ns=padim;i=1328",
    browseName="ns=padim;AnalogSignal",
    displayName="Value",
    modellingRule="Mandatory",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1225"]), o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1226", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Float,
    accessLevel=3,
)
o6.reference(padim_objtypes.AnalyticalSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1328"])
o6.reference(o6.ns["ns=padim;i=1328"], "i=17597", "ns=irdi;s=0112/2///61987#ABN634#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1333",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1333"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1329",
    browseName="ns=padim;BlockTemperature",
    displayName="Block temperature",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1333"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1329"], "i=17597", "ns=irdi;s=0112/2///61987#ABP577#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1334",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1334"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1330",
    browseName="ns=padim;CatalystTemperature",
    displayName="Catalyst temperature",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1334"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1330"], "i=17597", "ns=irdi;s=0112/2///61987#ABP576#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1336",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749552, displayName=o6.LocalizedText("mbar"), description=o6.LocalizedText("millibar")
    ),
)
o6.reference(o6.ns["ns=padim;i=1336"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1331",
    browseName="ns=padim;CombustionAirPressure",
    displayName="Air pressure",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1336"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1331"], "i=17597", "ns=irdi;s=0112/2///61987#ABP579#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1337",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749552, displayName=o6.LocalizedText("mbar"), description=o6.LocalizedText("millibar")
    ),
)
o6.reference(o6.ns["ns=padim;i=1337"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1332",
    browseName="ns=padim;FuelGasPressure",
    displayName="Fuel gas pressure",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1337"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1332"], "i=17597", "ns=irdi;s=0112/2///61987#ABP578#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=1298",
    browseName="ns=padim;DeviceConditionSet",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=padim;i=1329"]),
        o6.hasComponent(o6.ns["ns=padim;i=1330"]),
        o6.hasComponent(o6.ns["ns=padim;i=1331"]),
        o6.hasComponent(o6.ns["ns=padim;i=1332"]),
    ],
)
o6.reference(padim_objtypes.FlameIonisationDetectorType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1298"])
o6.reference(o6.ns["ns=padim;i=1298"], "i=17603", padim_objtypes.IFlameIonisationDeviceConditionSetType)
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1363",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749652, displayName=o6.LocalizedText("ml"), description=o6.LocalizedText("millilitre")
    ),
)
o6.reference(o6.ns["ns=padim;i=1363"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1340",
    browseName="ns=padim;ActualInjectedVolume",
    displayName="Injected volume",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1363"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1340"], "i=17597", "ns=irdi;s=0112/2///61987#ABP564#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1367",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749552, displayName=o6.LocalizedText("mbar"), description=o6.LocalizedText("millibar")
    ),
)
o6.reference(o6.ns["ns=padim;i=1367"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1341",
    browseName="ns=padim;CarrierGasGaugePressure",
    displayName="Carrier gas pressure",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1367"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1341"], "i=17597", "ns=irdi;s=0112/2///61987#ABP559#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1371",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705747637, displayName=o6.LocalizedText("l/h"), description=o6.LocalizedText("litre per hour")
    ),
)
o6.reference(o6.ns["ns=padim;i=1371"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1342",
    browseName="ns=padim;CarrierGasVolumeFlow",
    displayName="Carrier gas volume flow",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1371"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1342"], "i=17597", "ns=irdi;s=0112/2///61987#ABP558#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1372",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1372"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1350",
    browseName="ns=padim;CoolerTemperature",
    displayName="Cooler temperature",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1372"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1350"], "i=17597", "ns=irdi;s=0112/2///61987#ABP555#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1373",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1373"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1358",
    browseName="ns=padim;ReactorTemperature",
    displayName="TOC reactor temperature",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1373"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1358"], "i=17597", "ns=irdi;s=0112/2///61987#ABP554#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1375",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749652, displayName=o6.LocalizedText("ml"), description=o6.LocalizedText("millilitre")
    ),
)
o6.reference(o6.ns["ns=padim;i=1375"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1359",
    browseName="ns=padim;ReferenceInjectionVolume",
    displayName="Injection volume",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1375"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1359"], "i=17597", "ns=irdi;s=0112/2///61987#ABP563#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1379",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720",
        unitId=705749685,
        displayName=o6.LocalizedText("ml/min"),
        description=o6.LocalizedText("millilitre per minute"),
    ),
)
o6.reference(o6.ns["ns=padim;i=1379"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1362",
    browseName="ns=padim;SampleWaterVolumeFlow",
    displayName="Sample water volume flow",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1379"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1362"], "i=17597", "ns=irdi;s=0112/2///61987#ABP561#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=1299",
    browseName="ns=padim;DeviceConditionSet",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=padim;i=1340"]),
        o6.hasComponent(o6.ns["ns=padim;i=1341"]),
        o6.hasComponent(o6.ns["ns=padim;i=1342"]),
        o6.hasComponent(o6.ns["ns=padim;i=1350"]),
        o6.hasComponent(o6.ns["ns=padim;i=1358"]),
        o6.hasComponent(o6.ns["ns=padim;i=1359"]),
        o6.hasComponent(o6.ns["ns=padim;i=1362"]),
    ],
)
o6.reference(padim_objtypes.TocAnalyserType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1299"])
o6.reference(o6.ns["ns=padim;i=1299"], "i=17603", padim_objtypes.ITocDeviceConditionSetType)
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1380", browseName="ns=padim;SourceResidualLife", displayName="Residual operational life of radiation source", dataType=o6.Float, value=1.0
)
o6.reference(o6.ns["ns=padim;i=1380"], "i=17597", "ns=irdi;s=0112/2///61987#ABP552#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1381",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749552, displayName=o6.LocalizedText("mbar"), description=o6.LocalizedText("millibar")
    ),
)
o6.reference(o6.ns["ns=padim;i=1381"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1315",
    browseName="ns=padim;AbsoluteSampleGasPressure",
    displayName="Sample gas pressure",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1381"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1315"], "i=17597", "ns=irdi;s=0112/2///61987#ABP560#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1382",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741328, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
    ),
)
o6.reference(o6.ns["ns=padim;i=1382"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.BaseAnalogType(
    nodeId="ns=padim;i=1325",
    browseName="ns=padim;ChopperFrequencyDeviation",
    displayName="Chopper frequency (deviation)",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1382"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1325"], "i=17597", "ns=irdi;s=0112/2///61987#ABP553#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1383",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1383"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1326",
    browseName="ns=padim;SampleCellTemperature",
    displayName="Sample cell temperature",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1383"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1326"], "i=17597", "ns=irdi;s=0112/2///61987#ABP556#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=1293",
    browseName="ns=padim;SignalConditionSet",
    modellingRule="Optional",
    references=[
        o6.hasProperty(o6.ns["ns=padim;i=1380"]),
        o6.hasComponent(o6.ns["ns=padim;i=1315"]),
        o6.hasComponent(o6.ns["ns=padim;i=1325"]),
        o6.hasComponent(o6.ns["ns=padim;i=1326"]),
    ],
)
o6.reference(padim_objtypes.NonDispersiveInfraredSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1293"])
o6.reference(o6.ns["ns=padim;i=1293"], "i=17603", padim_objtypes.INonDispersiveInfraredSignalConditionSetType)
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1407", browseName="ns=padim;SourceResidualLife", displayName="Residual operational life of radiation source", dataType=o6.Float, value=1.0
)
o6.reference(o6.ns["ns=padim;i=1407"], "i=17597", "ns=irdi;s=0112/2///61987#ABP552#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1408",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749552, displayName=o6.LocalizedText("mbar"), description=o6.LocalizedText("millibar")
    ),
)
o6.reference(o6.ns["ns=padim;i=1408"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1388",
    browseName="ns=padim;AbsoluteSampleGasPressure",
    displayName="Sample gas pressure",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1408"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1388"], "i=17597", "ns=irdi;s=0112/2///61987#ABP560#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1409",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741328, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
    ),
)
o6.reference(o6.ns["ns=padim;i=1409"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.BaseAnalogType(
    nodeId="ns=padim;i=1390",
    browseName="ns=padim;ChopperFrequencyDeviation",
    displayName="Chopper frequency (deviation)",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1409"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1390"], "i=17597", "ns=irdi;s=0112/2///61987#ABP553#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1410",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705848917, displayName=o6.LocalizedText("ppm"), description=o6.LocalizedText("parts per million")
    ),
)
o6.reference(o6.ns["ns=padim;i=1410"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1393",
    browseName="ns=padim;DetectorZeroSignal",
    displayName="Detector zero signal",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1410"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1393"], "i=17597", "ns=irdi;s=0112/2///61987#ABP551#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1411",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741328, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
    ),
)
o6.reference(o6.ns["ns=padim;i=1411"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1399",
    browseName="ns=padim;RelativeReagentLevel",
    displayName="Reagent level",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1411"])],
    dataType=o6.Float,
    valueRank=-2,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1399"], "i=17597", "ns=irdi;s=0112/2///61987#ABP557#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1412",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1412"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1405",
    browseName="ns=padim;SampleCellTemperature",
    displayName="Sample cell temperature",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1412"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1405"], "i=17597", "ns=irdi;s=0112/2///61987#ABP556#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1413",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705747637, displayName=o6.LocalizedText("l/h"), description=o6.LocalizedText("litre per hour")
    ),
)
o6.reference(o6.ns["ns=padim;i=1413"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1406",
    browseName="ns=padim;SampleGasVolumeFlow",
    displayName="Sample gas volume flow",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1413"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1406"], "i=17597", "ns=irdi;s=0112/2///61987#ABP562#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=1303",
    browseName="ns=padim;SignalConditionSet",
    modellingRule="Optional",
    references=[
        o6.hasProperty(o6.ns["ns=padim;i=1407"]),
        o6.hasComponent(o6.ns["ns=padim;i=1388"]),
        o6.hasComponent(o6.ns["ns=padim;i=1390"]),
        o6.hasComponent(o6.ns["ns=padim;i=1393"]),
        o6.hasComponent(o6.ns["ns=padim;i=1399"]),
        o6.hasComponent(o6.ns["ns=padim;i=1405"]),
        o6.hasComponent(o6.ns["ns=padim;i=1406"]),
    ],
)
o6.reference(padim_objtypes.TocSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1303"])
o6.reference(o6.ns["ns=padim;i=1303"], "i=17603", padim_objtypes.ITocSignalConditionSetType)
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1416",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1416"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1414",
    browseName="ns=padim;SampleTemperature",
    displayName="Sample temperature",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1416"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1414"], "i=17597", "ns=irdi;s=0112/2///61987#ABP575#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1417",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1417"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1415",
    browseName="ns=padim;SensingElementTemperature",
    displayName="Temperature sensing element",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1417"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1415"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=1304",
    browseName="ns=padim;SignalConditionSet",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=padim;i=1414"]), o6.hasComponent(o6.ns["ns=padim;i=1415"])],
)
o6.reference(padim_objtypes.ParamagneticSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1304"])
o6.reference(o6.ns["ns=padim;i=1304"], "i=17603", padim_objtypes.IParamagneticSignalConditionSetType)
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1419",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1419"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1418",
    browseName="ns=padim;SampleTemperature",
    displayName="Sample temperature",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1419"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1418"], "i=17597", "ns=irdi;s=0112/2///61987#ABP575#001")
ns0.objtypes.BaseObjectType(nodeId="ns=padim;i=1302", browseName="ns=padim;SignalConditionSet", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=padim;i=1418"])])
o6.reference(padim_objtypes.ThermalConductivitySignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1302"])
o6.reference(o6.ns["ns=padim;i=1302"], "i=17603", padim_objtypes.IThermalConductivitySignalConditionSetType)
ns0.vartypes.DataItemType(nodeId="ns=padim;i=1426", browseName="ns=padim;SignalFitQuality", displayName="Signal fit quality", dataType=o6.Float, value=0.0, accessLevel=3)
o6.reference(o6.ns["ns=padim;i=1426"], "i=17597", "ns=irdi;s=0112/2///61987#ABP580#001")
ns0.vartypes.DataItemType(nodeId="ns=padim;i=1428", browseName="ns=padim;SignalNoiseRatio", displayName="Signal/noise ratio", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=1428"], "i=17597", "ns=irdi;s=0112/2///61987#ABP581#001")
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1356",
    browseName="ns=padim;PhMeasuringMethod",
    displayName="pH measuring method",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1397",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[4, 1],
                value=[
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP718#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP719#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP720#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")],
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1404",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("glass electrode", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ISFET", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("ceramic electrode", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1421",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABP718#001")],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1429", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("glass electrode", "en"))),
    ],
    dataType=o6.UInt32,
    value=0,
)
o6.reference(padim_objtypes.IPhSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1356"])
o6.reference(o6.ns["ns=padim;i=1356"], "i=17597", "ns=irdi;s=0112/2///61987#ABP640#002")
ns0.vartypes.DataItemType(nodeId="ns=padim;i=1430", browseName="ns=padim;TransmissionRatio", displayName="Transmission ratio", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=1430"], "i=17597", "ns=irdi;s=0112/2///61987#ABP582#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1431",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749552, displayName=o6.LocalizedText("mbar"), description=o6.LocalizedText("millibar")
    ),
)
o6.reference(o6.ns["ns=padim;i=1431"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1420",
    browseName="ns=padim;AbsoluteSampleGasPressure",
    displayName="Sample gas pressure",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1431"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1420"], "i=17597", "ns=irdi;s=0112/2///61987#ABP560#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1432",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1432"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1422",
    browseName="ns=padim;LaserTemperature",
    displayName="Laser temperature",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1432"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1422"], "i=17597", "ns=irdi;s=0112/2///61987#ABP583#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1433",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1433"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1423",
    browseName="ns=padim;SampleTemperature",
    displayName="Sample temperature",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1433"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1423"], "i=17597", "ns=irdi;s=0112/2///61987#ABP575#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=1305",
    browseName="ns=padim;SignalConditionSet",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=padim;i=1420"]),
        o6.hasComponent(o6.ns["ns=padim;i=1422"]),
        o6.hasComponent(o6.ns["ns=padim;i=1423"]),
        o6.hasComponent(o6.ns["ns=padim;i=1426"]),
        o6.hasComponent(o6.ns["ns=padim;i=1428"]),
        o6.hasComponent(o6.ns["ns=padim;i=1430"]),
    ],
)
o6.reference(padim_objtypes.TunableDiodeLaserSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1305"])
o6.reference(o6.ns["ns=padim;i=1305"], "i=17603", padim_objtypes.ITunableDiodeLaserSignalConditionSetType)
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1437",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705747637, displayName=o6.LocalizedText("l/h"), description=o6.LocalizedText("litre per hour")
    ),
)
o6.reference(o6.ns["ns=padim;i=1437"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1435",
    browseName="ns=padim;SampleGasVolumeFlow",
    displayName="Sample gas volume flow",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1437"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1435"], "i=17597", "ns=irdi;s=0112/2///61987#ABP562#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1438",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1438"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1436",
    browseName="ns=padim;SensingElementTemperature",
    displayName="Temperature sensing element",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1438"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1436"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1442", browseName="ns=padim;SensorT90", displayName="Settling time t90 at calibration", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=1442"], "i=17597", "ns=irdi;s=0112/2///61987#ABP569#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1443",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705746519, displayName=o6.LocalizedText("hPa"), description=o6.LocalizedText("hectopascal")
    ),
)
o6.reference(o6.ns["ns=padim;i=1443"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1439",
    browseName="ns=padim;AbsoluteAirPressure",
    displayName="Absolute air pressure",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1443"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1439"], "i=17597", "ns=irdi;s=0112/2///61987#ABP574#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1444", browseName="EngineeringUnits", displayName="Unit", dataType=ns0.datatypes.EUInformation)
o6.reference(o6.ns["ns=padim;i=1444"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1440",
    browseName="ns=padim;AmperometricSensorSlope",
    displayName="Amperometric sensing element slope",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1444"])],
    dataType=o6.Float,
)
o6.reference(o6.ns["ns=padim;i=1440"], "i=17597", "ns=irdi;s=0112/2///61987#ABP572#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1445",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705750616, displayName=o6.LocalizedText("pA"), description=o6.LocalizedText("picoampere")
    ),
)
o6.reference(o6.ns["ns=padim;i=1445"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1441",
    browseName="ns=padim;AmperometricSensorZeroPoint",
    displayName="Amperometric sensing element zero point",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1445"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1441"], "i=17597", "ns=irdi;s=0112/2///61987#ABP573#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=1291",
    browseName="ns=padim;<SignalCalibrationIdentifier>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(o6.ns["ns=padim;i=1442"]),
        o6.hasComponent(o6.ns["ns=padim;i=1439"]),
        o6.hasComponent(o6.ns["ns=padim;i=1440"]),
        o6.hasComponent(o6.ns["ns=padim;i=1441"]),
    ],
)
o6.reference(padim_objtypes.AmperometricSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1291"])
o6.reference(o6.ns["ns=padim;i=1291"], "i=17603", padim_objtypes.IAmperometricCalibrationType)
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1446", browseName="ns=padim;SensorCleaningsCounter", displayName="CIP counter", dataType=o6.UInt32, value=0)
o6.reference(o6.ns["ns=padim;i=1446"], "i=17597", "ns=irdi;s=0112/2///61987#ABP546#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1448", browseName="ns=padim;SensorSterilisationsCounter", displayName="SIP counter", dataType=o6.UInt32, value=0)
o6.reference(o6.ns["ns=padim;i=1448"], "i=17597", "ns=irdi;s=0112/2///61987#ABP547#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1450",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705745431, displayName=o6.LocalizedText("d"), description=o6.LocalizedText("day")
    ),
)
o6.reference(o6.ns["ns=padim;i=1450"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1447",
    browseName="ns=padim;SensorNextCalibration",
    displayName="Days until next calibration",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1450"])],
    dataType=o6.UInt32,
    value=0,
)
o6.reference(o6.ns["ns=padim;i=1447"], "i=17597", "ns=irdi;s=0112/2///61987#ABP566#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1451",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1451"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1449",
    browseName="ns=padim;SensingElementTemperature",
    displayName="Temperature sensing element",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1451"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1449"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=1296",
    browseName="ns=padim;SignalConditionSet",
    modellingRule="Optional",
    references=[
        o6.hasProperty(o6.ns["ns=padim;i=1446"]),
        o6.hasProperty(o6.ns["ns=padim;i=1448"]),
        o6.hasComponent(o6.ns["ns=padim;i=1447"]),
        o6.hasComponent(o6.ns["ns=padim;i=1449"]),
    ],
)
o6.reference(padim_objtypes.AmperometricSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1296"])
o6.reference(o6.ns["ns=padim;i=1296"], "i=17603", padim_objtypes.IAmperometricSignalConditionSetType)
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1455", browseName="ns=padim;SensorT90", displayName="Settling time t90 at calibration", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=1455"], "i=17597", "ns=irdi;s=0112/2///61987#ABP569#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1456",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705746519, displayName=o6.LocalizedText("hPa"), description=o6.LocalizedText("hectopascal")
    ),
)
o6.reference(o6.ns["ns=padim;i=1456"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1452",
    browseName="ns=padim;AbsoluteAirPressure",
    displayName="Absolute air pressure",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1456"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1452"], "i=17597", "ns=irdi;s=0112/2///61987#ABP574#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1457", browseName="EngineeringUnits", displayName="Unit", dataType=ns0.datatypes.EUInformation)
o6.reference(o6.ns["ns=padim;i=1457"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1453",
    browseName="ns=padim;OpticalFluorescenseQuenchingSensorSlope",
    displayName="Optical fluorescence quenching sensing element slope",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1457"])],
    dataType=o6.Float,
)
o6.reference(o6.ns["ns=padim;i=1453"], "i=17597", "ns=irdi;s=0112/2///61987#ABP586#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1458",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741621, displayName=o6.LocalizedText(";s"), description=o6.LocalizedText("microsecond")
    ),
)
o6.reference(o6.ns["ns=padim;i=1458"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1454",
    browseName="ns=padim;OpticalFluorescenseQuenchingSensorZeroPoint",
    displayName="Optical fluorescence quenching sensing element zero point",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1458"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1454"], "i=17597", "ns=irdi;s=0112/2///61987#ABP587#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=1300",
    browseName="ns=padim;<SignalCalibrationIdentifier>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(o6.ns["ns=padim;i=1455"]),
        o6.hasComponent(o6.ns["ns=padim;i=1452"]),
        o6.hasComponent(o6.ns["ns=padim;i=1453"]),
        o6.hasComponent(o6.ns["ns=padim;i=1454"]),
    ],
)
o6.reference(padim_objtypes.OpticalFluorescenseQuenchingSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1300"])
o6.reference(o6.ns["ns=padim;i=1300"], "i=17603", padim_objtypes.IOpticalFluorescenseQuenchingCalibrationType)
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1459", browseName="ns=padim;SensorCleaningsCounter", displayName="CIP counter", dataType=o6.UInt32, value=0)
o6.reference(o6.ns["ns=padim;i=1459"], "i=17597", "ns=irdi;s=0112/2///61987#ABP546#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1461", browseName="ns=padim;SensorSterilisationsCounter", displayName="SIP counter", dataType=o6.UInt32, value=0)
o6.reference(o6.ns["ns=padim;i=1461"], "i=17597", "ns=irdi;s=0112/2///61987#ABP547#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1463",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705745431, displayName=o6.LocalizedText("d"), description=o6.LocalizedText("day")
    ),
)
o6.reference(o6.ns["ns=padim;i=1463"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1460",
    browseName="ns=padim;SensorNextCalibration",
    displayName="Days until next calibration",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1463"])],
    dataType=o6.UInt32,
    value=0,
)
o6.reference(o6.ns["ns=padim;i=1460"], "i=17597", "ns=irdi;s=0112/2///61987#ABP566#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1464",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1464"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1462",
    browseName="ns=padim;SensingElementTemperature",
    displayName="Temperature sensing element",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1464"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1462"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=1301",
    browseName="ns=padim;SignalConditionSet",
    modellingRule="Optional",
    references=[
        o6.hasProperty(o6.ns["ns=padim;i=1459"]),
        o6.hasProperty(o6.ns["ns=padim;i=1461"]),
        o6.hasComponent(o6.ns["ns=padim;i=1460"]),
        o6.hasComponent(o6.ns["ns=padim;i=1462"]),
    ],
)
o6.reference(padim_objtypes.OpticalFluorescenseQuenchingSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1301"])
o6.reference(o6.ns["ns=padim;i=1301"], "i=17603", padim_objtypes.IOpticalFluorescenseQuenchingSignalConditionSetType)
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1468", browseName="ns=padim;SensorT90", displayName="Settling time t90 at calibration", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=1468"], "i=17597", "ns=irdi;s=0112/2///61987#ABP569#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1469",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749524, displayName=o6.LocalizedText("mV"), description=o6.LocalizedText("millivolt")
    ),
)
o6.reference(o6.ns["ns=padim;i=1469"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1465",
    browseName="ns=padim;SensorAsymmetryPotential",
    displayName="pH sensing element asymmetry potential",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1469"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1465"], "i=17597", "ns=irdi;s=0112/2///61987#ABP568#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1470",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749524, displayName=o6.LocalizedText("mV"), description=o6.LocalizedText("millivolt")
    ),
)
o6.reference(o6.ns["ns=padim;i=1470"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1466",
    browseName="ns=padim;SensorSlope",
    displayName="pH sensing element slope",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1470"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1466"], "i=17597", "ns=irdi;s=0112/2///61987#ABP567#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=1294",
    browseName="ns=padim;<SignalCalibrationIdentifier>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1468"]), o6.hasComponent(o6.ns["ns=padim;i=1465"]), o6.hasComponent(o6.ns["ns=padim;i=1466"])],
)
o6.reference(padim_objtypes.PhSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1294"])
o6.reference(o6.ns["ns=padim;i=1294"], "i=17603", padim_objtypes.IPhCalibrationType)
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1473", browseName="ns=padim;SensorCleaningsCounter", displayName="CIP counter", dataType=o6.UInt32, value=0)
o6.reference(o6.ns["ns=padim;i=1473"], "i=17597", "ns=irdi;s=0112/2///61987#ABP546#001")
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1366",
    browseName="ns=padim;ConductivityMeasuringMethod",
    displayName="Conductivity measuring method",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1467",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[4, 1],
                value=[
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP721#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP722#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP723#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")],
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1476",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("inductive", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("conductive 2-electrodes", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("conductive 4-electrodes", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1477",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABP721#001")],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1478", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("inductive", "en"))),
    ],
    dataType=o6.UInt32,
    value=0,
)
o6.reference(padim_objtypes.IConductivitySignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1366"])
o6.reference(o6.ns["ns=padim;i=1366"], "i=17597", "ns=irdi;s=0112/2///61987#ABP641#002")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1479", browseName="ns=padim;SensorSterilisationsCounter", displayName="SIP counter", dataType=o6.UInt32, value=0)
o6.reference(o6.ns["ns=padim;i=1479"], "i=17597", "ns=irdi;s=0112/2///61987#ABP547#001")
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1471",
    browseName="ns=padim;PhMeasuringMethod",
    displayName="pH measuring method",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1482",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[4, 1],
                value=[
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP718#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP719#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP720#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")],
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1484",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("glass electrode", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ISFET", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("ceramic electrode", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1485",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABP718#001")],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1486", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("glass electrode", "en"))),
    ],
    dataType=o6.UInt32,
    value=0,
)
o6.reference(o6.ns["ns=padim;i=1471"], "i=17597", "ns=irdi;s=0112/2///61987#ABP640#002")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1487",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741367, displayName=o6.LocalizedText(";"), description=o6.LocalizedText("ohm")
    ),
)
o6.reference(o6.ns["ns=padim;i=1487"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1472",
    browseName="ns=padim;SensingElementImpedance",
    displayName="pH sensing element impedance",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1487"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1472"], "i=17597", "ns=irdi;s=0112/2///61987#ABP570#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1489",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705745431, displayName=o6.LocalizedText("d"), description=o6.LocalizedText("day")
    ),
)
o6.reference(o6.ns["ns=padim;i=1489"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1474",
    browseName="ns=padim;SensorNextCalibration",
    displayName="Days until next calibration",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1489"])],
    dataType=o6.UInt32,
    value=0,
)
o6.reference(o6.ns["ns=padim;i=1474"], "i=17597", "ns=irdi;s=0112/2///61987#ABP566#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1490",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741367, displayName=o6.LocalizedText(";"), description=o6.LocalizedText("ohm")
    ),
)
o6.reference(o6.ns["ns=padim;i=1490"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1475",
    browseName="ns=padim;SensorReferenceImpedance",
    displayName="pH reference system impedance",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1490"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1475"], "i=17597", "ns=irdi;s=0112/2///61987#ABP571#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1491",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1491"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1480",
    browseName="ns=padim;SensingElementTemperature",
    displayName="Temperature sensing element",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1491"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1480"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=1297",
    browseName="ns=padim;SignalConditionSet",
    modellingRule="Optional",
    references=[
        o6.hasProperty(o6.ns["ns=padim;i=1473"]),
        o6.hasProperty(o6.ns["ns=padim;i=1479"]),
        o6.hasComponent(o6.ns["ns=padim;i=1471"]),
        o6.hasComponent(o6.ns["ns=padim;i=1472"]),
        o6.hasComponent(o6.ns["ns=padim;i=1474"]),
        o6.hasComponent(o6.ns["ns=padim;i=1475"]),
        o6.hasComponent(o6.ns["ns=padim;i=1480"]),
    ],
)
o6.reference(padim_objtypes.PhSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1297"])
o6.reference(o6.ns["ns=padim;i=1297"], "i=17603", padim_objtypes.IPhSignalConditionSetType)
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1368",
    browseName="ns=padim;TemperatureCompensationStyle",
    displayName="Temperature compensation",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1481",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[9, 1],
                value=[
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP724#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP725#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP726#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP727#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP728#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP729#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP730#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP731#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")],
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1483",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[9],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("no temperature compensation", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("linear compensation", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("NaCl (IEC 60746-3)", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("water ISO 7888 (20&#176;C)", "en")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("water ISO 7888 (25&#176;C)", "en")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("UPW NaCl", "en")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("UPW HCl", "en")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("compensation table", "en")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1488",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABP724#001")],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=padim;i=1492", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("no temperature compensation", "en"))
        ),
    ],
    dataType=o6.UInt32,
    value=0,
)
o6.reference(padim_objtypes.IConductivitySignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1368"])
o6.reference(o6.ns["ns=padim;i=1368"], "i=17597", "ns=irdi;s=0112/2///61987#ABP642#002")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1494",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720",
        unitId=705744658,
        displayName=o6.LocalizedText("cm&#8315;&#185;"),
        description=o6.LocalizedText("reciprocal centimetre"),
    ),
)
o6.reference(o6.ns["ns=padim;i=1494"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1493",
    browseName="ns=padim;ConductivityCellConstant",
    displayName="Cell constant",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1494"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1493"], "i=17597", "ns=irdi;s=0112/2///61987#ABF161#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=1295", browseName="ns=padim;<SignalCalibrationIdentifier>", modellingRule="OptionalPlaceholder", references=[o6.hasComponent(o6.ns["ns=padim;i=1493"])]
)
o6.reference(padim_objtypes.ConductivitySignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1295"])
o6.reference(o6.ns["ns=padim;i=1295"], "i=17603", padim_objtypes.IConductivityCalibrationType)
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1496", browseName="ns=padim;SensorCleaningsCounter", displayName="CIP counter", dataType=o6.UInt32, value=0)
o6.reference(o6.ns["ns=padim;i=1496"], "i=17597", "ns=irdi;s=0112/2///61987#ABP546#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1497", browseName="ns=padim;SensorSterilisationsCounter", displayName="SIP counter", dataType=o6.UInt32, value=0)
o6.reference(o6.ns["ns=padim;i=1497"], "i=17597", "ns=irdi;s=0112/2///61987#ABP547#001")
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1495",
    browseName="ns=padim;ConductivityMeasuringMethod",
    displayName="Conductivity measuring method",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1500",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[4, 1],
                value=[
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP721#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP722#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP723#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")],
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1501",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("inductive", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("conductive 2-electrodes", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("conductive 4-electrodes", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1502",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABP721#001")],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1503", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("inductive", "en"))),
    ],
    dataType=o6.UInt32,
    value=0,
)
o6.reference(o6.ns["ns=padim;i=1495"], "i=17597", "ns=irdi;s=0112/2///61987#ABP641#002")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1504",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1504"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1498",
    browseName="ns=padim;SensingElementTemperature",
    displayName="Temperature sensing element",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1504"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1498"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1499",
    browseName="ns=padim;TemperatureCompensationStyle",
    displayName="Temperature compensation",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1506",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[9, 1],
                value=[
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP724#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP725#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP726#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP727#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP728#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP729#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP730#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP731#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")],
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1508",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[9],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("no temperature compensation", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("linear compensation", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("NaCl (IEC 60746-3)", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("water ISO 7888 (20&#176;C)", "en")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("water ISO 7888 (25&#176;C)", "en")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("UPW NaCl", "en")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("UPW HCl", "en")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("compensation table", "en")),
                    ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1509",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABP724#001")],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=padim;i=1514", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("no temperature compensation", "en"))
        ),
    ],
    dataType=o6.UInt32,
    value=0,
)
o6.reference(o6.ns["ns=padim;i=1499"], "i=17597", "ns=irdi;s=0112/2///61987#ABP642#002")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=1292",
    browseName="ns=padim;SignalConditionSet",
    modellingRule="Optional",
    references=[
        o6.hasProperty(o6.ns["ns=padim;i=1496"]),
        o6.hasProperty(o6.ns["ns=padim;i=1497"]),
        o6.hasComponent(o6.ns["ns=padim;i=1495"]),
        o6.hasComponent(o6.ns["ns=padim;i=1498"]),
        o6.hasComponent(o6.ns["ns=padim;i=1499"]),
    ],
)
o6.reference(padim_objtypes.ConductivitySignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1292"])
o6.reference(o6.ns["ns=padim;i=1292"], "i=17603", padim_objtypes.IConductivitySignalConditionSetType)
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1515",
    browseName="EnumValues",
    parent="ns=padim;i=1276",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("CAS"), description=o6.LocalizedText("Chemical Abstracts Service dictionary")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("PAT"), description=o6.LocalizedText("Process Analyser Technology dictionary")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("user-defined"), description=o6.LocalizedText("User/manufacturer defined")),
    ],
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1524",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749552, displayName=o6.LocalizedText("mbar"), description=o6.LocalizedText("millibar")
    ),
)
o6.reference(o6.ns["ns=padim;i=1524"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1320",
    browseName="ns=padim;AbsoluteSampleGasPressure",
    displayName="Sample gas pressure",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1524"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.INonDispersiveInfraredSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1320"])
o6.reference(o6.ns["ns=padim;i=1320"], "i=17597", "ns=irdi;s=0112/2///61987#ABP560#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1525",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1525"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1322",
    browseName="ns=padim;SampleCellTemperature",
    displayName="Sample cell temperature",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1525"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.INonDispersiveInfraredSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1322"])
o6.reference(o6.ns["ns=padim;i=1322"], "i=17597", "ns=irdi;s=0112/2///61987#ABP556#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1526",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741328, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
    ),
)
o6.reference(o6.ns["ns=padim;i=1526"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.BaseAnalogType(
    nodeId="ns=padim;i=1321",
    browseName="ns=padim;ChopperFrequencyDeviation",
    displayName="Chopper frequency (deviation)",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1526"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.INonDispersiveInfraredSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1321"])
o6.reference(o6.ns["ns=padim;i=1321"], "i=17597", "ns=irdi;s=0112/2///61987#ABP553#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1527",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741328, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
    ),
)
o6.reference(o6.ns["ns=padim;i=1527"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.BaseAnalogType(
    nodeId="ns=padim;i=1403",
    browseName="ns=padim;ChopperFrequencyDeviation",
    displayName="Chopper frequency (deviation)",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1527"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.ITocSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1403"])
o6.reference(o6.ns["ns=padim;i=1403"], "i=17597", "ns=irdi;s=0112/2///61987#ABP553#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1530",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1530"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1392",
    browseName="ns=padim;SampleCellTemperature",
    displayName="Sample cell temperature",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1530"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.ITocSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1392"])
o6.reference(o6.ns["ns=padim;i=1392"], "i=17597", "ns=irdi;s=0112/2///61987#ABP556#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1531",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705848917, displayName=o6.LocalizedText("ppm"), description=o6.LocalizedText("parts per million")
    ),
)
o6.reference(o6.ns["ns=padim;i=1531"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1402",
    browseName="ns=padim;DetectorZeroSignal",
    displayName="Detector zero signal",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1531"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.ITocSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1402"])
o6.reference(o6.ns["ns=padim;i=1402"], "i=17597", "ns=irdi;s=0112/2///61987#ABP551#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1532",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741328, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
    ),
)
o6.reference(o6.ns["ns=padim;i=1532"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1387",
    browseName="ns=padim;RelativeReagentLevel",
    displayName="Reagent level",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1532"])],
    dataType=o6.Float,
    valueRank=-2,
    value=0.0,
)
o6.reference(padim_objtypes.ITocSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1387"])
o6.reference(o6.ns["ns=padim;i=1387"], "i=17597", "ns=irdi;s=0112/2///61987#ABP557#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1533",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749552, displayName=o6.LocalizedText("mbar"), description=o6.LocalizedText("millibar")
    ),
)
o6.reference(o6.ns["ns=padim;i=1533"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1400",
    browseName="ns=padim;AbsoluteSampleGasPressure",
    displayName="Sample gas pressure",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1533"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.ITocSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1400"])
o6.reference(o6.ns["ns=padim;i=1400"], "i=17597", "ns=irdi;s=0112/2///61987#ABP560#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1534",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705747637, displayName=o6.LocalizedText("l/h"), description=o6.LocalizedText("litre per hour")
    ),
)
o6.reference(o6.ns["ns=padim;i=1534"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1401",
    browseName="ns=padim;SampleGasVolumeFlow",
    displayName="Sample gas volume flow",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1534"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.ITocSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1401"])
o6.reference(o6.ns["ns=padim;i=1401"], "i=17597", "ns=irdi;s=0112/2///61987#ABP562#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1535",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749524, displayName=o6.LocalizedText("mV"), description=o6.LocalizedText("millivolt")
    ),
)
o6.reference(o6.ns["ns=padim;i=1535"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1427",
    browseName="ns=padim;SensorAsymmetryPotential",
    displayName="pH sensing element asymmetry potential",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1535"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IPhCalibrationType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1427"])
o6.reference(o6.ns["ns=padim;i=1427"], "i=17597", "ns=irdi;s=0112/2///61987#ABP568#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1536",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749524, displayName=o6.LocalizedText("mV"), description=o6.LocalizedText("millivolt")
    ),
)
o6.reference(o6.ns["ns=padim;i=1536"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1424",
    browseName="ns=padim;SensorSlope",
    displayName="pH sensing element slope",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1536"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IPhCalibrationType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1424"])
o6.reference(o6.ns["ns=padim;i=1424"], "i=17597", "ns=irdi;s=0112/2///61987#ABP567#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1537",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720",
        unitId=705744658,
        displayName=o6.LocalizedText("cm&#8315;&#185;"),
        description=o6.LocalizedText("reciprocal centimetre"),
    ),
)
o6.reference(o6.ns["ns=padim;i=1537"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1505",
    browseName="ns=padim;ConductivityCellConstant",
    displayName="Cell constant",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1537"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IConductivityCalibrationType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1505"])
o6.reference(o6.ns["ns=padim;i=1505"], "i=17597", "ns=irdi;s=0112/2///61987#ABF161#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1538", browseName="EngineeringUnits", displayName="Unit", dataType=ns0.datatypes.EUInformation)
o6.reference(o6.ns["ns=padim;i=1538"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1319",
    browseName="ns=padim;AmperometricSensorSlope",
    displayName="Amperometric sensing element slope",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1538"])],
    dataType=o6.Float,
)
o6.reference(padim_objtypes.IAmperometricCalibrationType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1319"])
o6.reference(o6.ns["ns=padim;i=1319"], "i=17597", "ns=irdi;s=0112/2///61987#ABP572#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1539",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705750616, displayName=o6.LocalizedText("pA"), description=o6.LocalizedText("picoampere")
    ),
)
o6.reference(o6.ns["ns=padim;i=1539"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1511",
    browseName="ns=padim;AmperometricSensorZeroPoint",
    displayName="Amperometric sensing element zero point",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1539"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IAmperometricCalibrationType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1511"])
o6.reference(o6.ns["ns=padim;i=1511"], "i=17597", "ns=irdi;s=0112/2///61987#ABP573#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1540",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705746519, displayName=o6.LocalizedText("hPa"), description=o6.LocalizedText("hectopascal")
    ),
)
o6.reference(o6.ns["ns=padim;i=1540"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1507",
    browseName="ns=padim;AbsoluteAirPressure",
    displayName="Absolute air pressure",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1540"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IAmperometricCalibrationType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1507"])
o6.reference(o6.ns["ns=padim;i=1507"], "i=17597", "ns=irdi;s=0112/2///61987#ABP574#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1541",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705746519, displayName=o6.LocalizedText("hPa"), description=o6.LocalizedText("hectopascal")
    ),
)
o6.reference(o6.ns["ns=padim;i=1541"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1516",
    browseName="ns=padim;AbsoluteAirPressure",
    displayName="Absolute air pressure",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1541"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IOpticalFluorescenseQuenchingCalibrationType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1516"])
o6.reference(o6.ns["ns=padim;i=1516"], "i=17597", "ns=irdi;s=0112/2///61987#ABP574#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1542", browseName="EngineeringUnits", displayName="Unit", dataType=ns0.datatypes.EUInformation)
o6.reference(o6.ns["ns=padim;i=1542"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1517",
    browseName="ns=padim;OpticalFluorescenseQuenchingSensorSlope",
    displayName="Optical fluorescence quenching sensing element slope",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1542"])],
    dataType=o6.Float,
)
o6.reference(padim_objtypes.IOpticalFluorescenseQuenchingCalibrationType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1517"])
o6.reference(o6.ns["ns=padim;i=1517"], "i=17597", "ns=irdi;s=0112/2///61987#ABP586#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1543",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741621, displayName=o6.LocalizedText(";s"), description=o6.LocalizedText("microsecond")
    ),
)
o6.reference(o6.ns["ns=padim;i=1543"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1518",
    browseName="ns=padim;OpticalFluorescenseQuenchingSensorZeroPoint",
    displayName="Optical fluorescence quenching sensing element zero point",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1543"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IOpticalFluorescenseQuenchingCalibrationType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1518"])
o6.reference(o6.ns["ns=padim;i=1518"], "i=17597", "ns=irdi;s=0112/2///61987#ABP587#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1544",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1544"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1324",
    browseName="ns=padim;SampleTemperature",
    displayName="Sample temperature",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1544"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IParamagneticSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1324"])
o6.reference(o6.ns["ns=padim;i=1324"], "i=17597", "ns=irdi;s=0112/2///61987#ABP575#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1545",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1545"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1343",
    browseName="ns=padim;SensingElementTemperature",
    displayName="Temperature sensing element",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1545"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IParamagneticSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1343"])
o6.reference(o6.ns["ns=padim;i=1343"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1546",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1546"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1327",
    browseName="ns=padim;SampleTemperature",
    displayName="Sample temperature",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1546"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IThermalConductivitySignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1327"])
o6.reference(o6.ns["ns=padim;i=1327"], "i=17597", "ns=irdi;s=0112/2///61987#ABP575#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1547",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749552, displayName=o6.LocalizedText("mbar"), description=o6.LocalizedText("millibar")
    ),
)
o6.reference(o6.ns["ns=padim;i=1547"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1353",
    browseName="ns=padim;AbsoluteSampleGasPressure",
    displayName="Sample gas pressure",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1547"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.ITunableDiodeLaserSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1353"])
o6.reference(o6.ns["ns=padim;i=1353"], "i=17597", "ns=irdi;s=0112/2///61987#ABP560#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1548",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1548"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1352",
    browseName="ns=padim;SampleTemperature",
    displayName="Sample temperature",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1548"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.ITunableDiodeLaserSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1352"])
o6.reference(o6.ns["ns=padim;i=1352"], "i=17597", "ns=irdi;s=0112/2///61987#ABP575#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1549",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1549"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1351",
    browseName="ns=padim;LaserTemperature",
    displayName="Laser temperature",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1549"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.ITunableDiodeLaserSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1351"])
o6.reference(o6.ns["ns=padim;i=1351"], "i=17597", "ns=irdi;s=0112/2///61987#ABP583#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1550",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705747637, displayName=o6.LocalizedText("l/h"), description=o6.LocalizedText("litre per hour")
    ),
)
o6.reference(o6.ns["ns=padim;i=1550"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1386",
    browseName="ns=padim;SampleGasVolumeFlow",
    displayName="Sample gas volume flow",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1550"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IZirconiumDioxideSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1386"])
o6.reference(o6.ns["ns=padim;i=1386"], "i=17597", "ns=irdi;s=0112/2///61987#ABP562#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1551",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1551"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1355",
    browseName="ns=padim;SensingElementTemperature",
    displayName="Temperature sensing element",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1551"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IZirconiumDioxideSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1355"])
o6.reference(o6.ns["ns=padim;i=1355"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1552",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1552"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1338",
    browseName="ns=padim;SensingElementTemperature",
    displayName="Temperature sensing element",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1552"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IPhSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1338"])
o6.reference(o6.ns["ns=padim;i=1338"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1553",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705745431, displayName=o6.LocalizedText("d"), description=o6.LocalizedText("day")
    ),
)
o6.reference(o6.ns["ns=padim;i=1553"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1357",
    browseName="ns=padim;SensorNextCalibration",
    displayName="Days until next calibration",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1553"])],
    dataType=o6.UInt32,
    value=0,
)
o6.reference(padim_objtypes.IPhSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1357"])
o6.reference(o6.ns["ns=padim;i=1357"], "i=17597", "ns=irdi;s=0112/2///61987#ABP566#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1554",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749652, displayName=o6.LocalizedText("ml"), description=o6.LocalizedText("millilitre")
    ),
)
o6.reference(o6.ns["ns=padim;i=1554"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1396",
    browseName="ns=padim;ActualInjectedVolume",
    displayName="Injected volume",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1554"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.ITocDeviceConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1396"])
o6.reference(o6.ns["ns=padim;i=1396"], "i=17597", "ns=irdi;s=0112/2///61987#ABP564#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1555",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741367, displayName=o6.LocalizedText(";"), description=o6.LocalizedText("ohm")
    ),
)
o6.reference(o6.ns["ns=padim;i=1555"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1364",
    browseName="ns=padim;SensingElementImpedance",
    displayName="pH sensing element impedance",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1555"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IPhSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1364"])
o6.reference(o6.ns["ns=padim;i=1364"], "i=17597", "ns=irdi;s=0112/2///61987#ABP570#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1556",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741367, displayName=o6.LocalizedText(";"), description=o6.LocalizedText("ohm")
    ),
)
o6.reference(o6.ns["ns=padim;i=1556"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1365",
    browseName="ns=padim;SensorReferenceImpedance",
    displayName="pH reference system impedance",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1556"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IPhSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1365"])
o6.reference(o6.ns["ns=padim;i=1365"], "i=17597", "ns=irdi;s=0112/2///61987#ABP571#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1557",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1557"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1339",
    browseName="ns=padim;SensingElementTemperature",
    displayName="Temperature sensing element",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1557"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IConductivitySignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1339"])
o6.reference(o6.ns["ns=padim;i=1339"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1558",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1558"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1378",
    browseName="ns=padim;SensingElementTemperature",
    displayName="Temperature sensing element",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1558"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IAmperometricSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1378"])
o6.reference(o6.ns["ns=padim;i=1378"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1559",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705745431, displayName=o6.LocalizedText("d"), description=o6.LocalizedText("day")
    ),
)
o6.reference(o6.ns["ns=padim;i=1559"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1374",
    browseName="ns=padim;SensorNextCalibration",
    displayName="Days until next calibration",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1559"])],
    dataType=o6.UInt32,
    value=0,
)
o6.reference(padim_objtypes.IAmperometricSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1374"])
o6.reference(o6.ns["ns=padim;i=1374"], "i=17597", "ns=irdi;s=0112/2///61987#ABP566#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1560",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1560"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1523",
    browseName="ns=padim;SensingElementTemperature",
    displayName="Temperature sensing element",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1560"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IOpticalFluorescenseQuenchingSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1523"])
o6.reference(o6.ns["ns=padim;i=1523"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1561",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705745431, displayName=o6.LocalizedText("d"), description=o6.LocalizedText("day")
    ),
)
o6.reference(o6.ns["ns=padim;i=1561"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1521",
    browseName="ns=padim;SensorNextCalibration",
    displayName="Days until next calibration",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1561"])],
    dataType=o6.UInt32,
    value=0,
)
o6.reference(padim_objtypes.IOpticalFluorescenseQuenchingSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1521"])
o6.reference(o6.ns["ns=padim;i=1521"], "i=17597", "ns=irdi;s=0112/2///61987#ABP566#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1564",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1564"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1528",
    browseName="ns=padim;InternalTemperature",
    displayName="Internal device temperature",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1564"])],
    dataType=o6.Float,
    valueRank=-2,
    value=0.0,
)
o6.reference(padim_objtypes.GeneralDeviceConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1528"])
o6.reference(o6.ns["ns=padim;i=1528"], "i=17597", "ns=irdi;s=0112/2///61987#ABP591#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1565",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749552, displayName=o6.LocalizedText("mbar"), description=o6.LocalizedText("millibar")
    ),
)
o6.reference(o6.ns["ns=padim;i=1565"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1385",
    browseName="ns=padim;CarrierGasGaugePressure",
    displayName="Carrier gas pressure",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1565"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.ITocDeviceConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1385"])
o6.reference(o6.ns["ns=padim;i=1385"], "i=17597", "ns=irdi;s=0112/2///61987#ABP559#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1566",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705747637, displayName=o6.LocalizedText("l/h"), description=o6.LocalizedText("litre per hour")
    ),
)
o6.reference(o6.ns["ns=padim;i=1566"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1389",
    browseName="ns=padim;CarrierGasVolumeFlow",
    displayName="Carrier gas volume flow",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1566"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.ITocDeviceConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1389"])
o6.reference(o6.ns["ns=padim;i=1389"], "i=17597", "ns=irdi;s=0112/2///61987#ABP558#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1567",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1567"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1398",
    browseName="ns=padim;CoolerTemperature",
    displayName="Cooler temperature",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1567"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.ITocDeviceConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1398"])
o6.reference(o6.ns["ns=padim;i=1398"], "i=17597", "ns=irdi;s=0112/2///61987#ABP555#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1568",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1568"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1391",
    browseName="ns=padim;ReactorTemperature",
    displayName="TOC reactor temperature",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1568"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.ITocDeviceConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1391"])
o6.reference(o6.ns["ns=padim;i=1391"], "i=17597", "ns=irdi;s=0112/2///61987#ABP554#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1569",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749652, displayName=o6.LocalizedText("ml"), description=o6.LocalizedText("millilitre")
    ),
)
o6.reference(o6.ns["ns=padim;i=1569"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1395",
    browseName="ns=padim;ReferenceInjectionVolume",
    displayName="Injection volume",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1569"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.ITocDeviceConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1395"])
o6.reference(o6.ns["ns=padim;i=1395"], "i=17597", "ns=irdi;s=0112/2///61987#ABP563#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1570",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720",
        unitId=705749685,
        displayName=o6.LocalizedText("ml/min"),
        description=o6.LocalizedText("millilitre per minute"),
    ),
)
o6.reference(o6.ns["ns=padim;i=1570"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1394",
    browseName="ns=padim;SampleWaterVolumeFlow",
    displayName="Sample water volume flow",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1570"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.ITocDeviceConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1394"])
o6.reference(o6.ns["ns=padim;i=1394"], "i=17597", "ns=irdi;s=0112/2///61987#ABP561#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1571",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1571"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1346",
    browseName="ns=padim;BlockTemperature",
    displayName="Block temperature",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1571"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IFlameIonisationDeviceConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1346"])
o6.reference(o6.ns["ns=padim;i=1346"], "i=17597", "ns=irdi;s=0112/2///61987#ABP577#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1572",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=1572"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1335",
    browseName="ns=padim;CatalystTemperature",
    displayName="Catalyst temperature",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1572"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IFlameIonisationDeviceConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1335"])
o6.reference(o6.ns["ns=padim;i=1335"], "i=17597", "ns=irdi;s=0112/2///61987#ABP576#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1573",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749552, displayName=o6.LocalizedText("mbar"), description=o6.LocalizedText("millibar")
    ),
)
o6.reference(o6.ns["ns=padim;i=1573"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1345",
    browseName="ns=padim;CombustionAirPressure",
    displayName="Air pressure",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1573"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IFlameIonisationDeviceConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1345"])
o6.reference(o6.ns["ns=padim;i=1345"], "i=17597", "ns=irdi;s=0112/2///61987#ABP579#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1574",
    browseName="EngineeringUnits",
    displayName="Unit",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749552, displayName=o6.LocalizedText("mbar"), description=o6.LocalizedText("millibar")
    ),
)
o6.reference(o6.ns["ns=padim;i=1574"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1344",
    browseName="ns=padim;FuelGasPressure",
    displayName="Fuel gas pressure",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=1574"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IFlameIonisationDeviceConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1344"])
o6.reference(o6.ns["ns=padim;i=1344"], "i=17597", "ns=irdi;s=0112/2///61987#ABP578#001")
ns0.vartypes.MultiStateDictionaryEntryDiscreteType(
    nodeId="ns=padim;i=1308",
    browseName="ns=padim;TypeOfCalibration",
    displayName="Type of calibration",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1575",
                browseName="EnumDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=2,
                arrayDimensions=[4, 1],
                value=[
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP732#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP733#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABP734#001")],
                    [o6.NodeId("ns=irdi;s=0112/2///61987#ABI407#004")],
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1576",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[4],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("adjustment", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("calibration", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("custody transfer", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("others", "en")),
                ],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=padim;i=1577",
                browseName="ValueAsDictionaryEntries",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[1],
                value=[o6.NodeId("ns=irdi;s=0112/2///61987#ABP732#001")],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=padim;i=1578", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("adjustment", "en"))),
    ],
    dataType=o6.UInt32,
    value=0,
    accessLevel=3,
)
o6.reference(padim_objtypes.ICalibrationType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1308"])
o6.reference(o6.ns["ns=padim;i=1308"], "i=17597", "ns=irdi;s=0112/2///61987#ABH609#002")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6002",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705848917, displayName=o6.LocalizedText("ppm"), description=o6.LocalizedText("parts per million")
    ),
)
o6.reference(o6.ns["ns=padim;i=6002"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6001",
    browseName="ns=padim;CalibrationRange1LowerRangeValue",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=6002"])],
    dataType=o6.Float,
    value=0.0,
    accessLevel=3,
)
o6.reference(padim_objtypes.IGasChromatographCalibrationType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=6001"])
o6.reference(o6.ns["ns=padim;i=6001"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ025#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6004",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705848917, displayName=o6.LocalizedText("ppm"), description=o6.LocalizedText("parts per million")
    ),
)
o6.reference(o6.ns["ns=padim;i=6004"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6003",
    browseName="ns=padim;CalibrationRange1UpperRangeValue",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=6004"])],
    dataType=o6.Float,
    value=100.0,
    accessLevel=3,
)
o6.reference(padim_objtypes.IGasChromatographCalibrationType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=6003"])
o6.reference(o6.ns["ns=padim;i=6003"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ026#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6007",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705848917, displayName=o6.LocalizedText("ppm"), description=o6.LocalizedText("parts per million")
    ),
)
o6.reference(o6.ns["ns=padim;i=6007"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6006",
    browseName="ns=padim;CalibrationRange2LowerRangeValue",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=6007"])],
    dataType=o6.Float,
    value=0.0,
    accessLevel=3,
)
o6.reference(padim_objtypes.IGasChromatographCalibrationType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=6006"])
o6.reference(o6.ns["ns=padim;i=6006"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ028#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6009",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705848917, displayName=o6.LocalizedText("ppm"), description=o6.LocalizedText("parts per million")
    ),
)
o6.reference(o6.ns["ns=padim;i=6009"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6008",
    browseName="ns=padim;CalibrationRange2UpperRangeValue",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=6009"])],
    dataType=o6.Float,
    value=100.0,
    accessLevel=3,
)
o6.reference(padim_objtypes.IGasChromatographCalibrationType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=6008"])
o6.reference(o6.ns["ns=padim;i=6008"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ029#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6012",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705848917, displayName=o6.LocalizedText("ppm"), description=o6.LocalizedText("parts per million")
    ),
)
o6.reference(o6.ns["ns=padim;i=6012"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6011",
    browseName="ns=padim;CalibrationRange3LowerRangeValue",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=6012"])],
    dataType=o6.Float,
    value=0.0,
    accessLevel=3,
)
o6.reference(padim_objtypes.IGasChromatographCalibrationType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=6011"])
o6.reference(o6.ns["ns=padim;i=6011"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ031#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6014",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705848917, displayName=o6.LocalizedText("ppm"), description=o6.LocalizedText("parts per million")
    ),
)
o6.reference(o6.ns["ns=padim;i=6014"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6013",
    browseName="ns=padim;CalibrationRange3UpperRangeValue",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=6014"])],
    dataType=o6.Float,
    value=100.0,
    accessLevel=3,
)
o6.reference(padim_objtypes.IGasChromatographCalibrationType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=6013"])
o6.reference(o6.ns["ns=padim;i=6013"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ032#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6018",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741328, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
    ),
)
o6.reference(o6.ns["ns=padim;i=6018"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6017",
    browseName="ns=padim;TotalAreaMeasuredPeaks",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=6018"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IGasChromatographDeviceConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=6017"])
o6.reference(o6.ns["ns=padim;i=6017"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ043#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6020",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749524, displayName=o6.LocalizedText("mV"), description=o6.LocalizedText("millivolt")
    ),
)
o6.reference(o6.ns["ns=padim;i=6020"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6019", browseName="ns=padim;BaselineNoise", modellingRule="Optional", references=[o6.hasProperty(o6.ns["ns=padim;i=6020"])], dataType=o6.Float, value=0.0
)
o6.reference(padim_objtypes.IGasChromatographDeviceConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=6019"])
o6.reference(o6.ns["ns=padim;i=6019"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ036#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6030", browseName="ns=padim;ValveName", dataType=o6.LocalizedText, valueRank=1)
o6.reference(o6.ns["ns=padim;i=6030"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ046#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6031", browseName="ns=padim;ValveSwitchingCyclesCounter", dataType=o6.UInt32, valueRank=1, arrayDimensions=[1], value=[0])
o6.reference(o6.ns["ns=padim;i=6031"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ007#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6033",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741328, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
    ),
)
o6.reference(o6.ns["ns=padim;i=6033"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6032", browseName="ns=padim;TotalAreaMeasuredPeaks", references=[o6.hasProperty(o6.ns["ns=padim;i=6033"])], dataType=o6.Float, value=0.0
)
o6.reference(o6.ns["ns=padim;i=6032"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ043#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6035",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749524, displayName=o6.LocalizedText("mV"), description=o6.LocalizedText("millivolt")
    ),
)
o6.reference(o6.ns["ns=padim;i=6035"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(nodeId="ns=padim;i=6034", browseName="ns=padim;BaselineNoise", references=[o6.hasProperty(o6.ns["ns=padim;i=6035"])], dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6034"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ036#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=5000",
    browseName="ns=padim;DeviceConditionSet",
    modellingRule="Optional",
    references=[
        o6.hasProperty(o6.ns["ns=padim;i=6030"]),
        o6.hasProperty(o6.ns["ns=padim;i=6031"]),
        o6.hasComponent(o6.ns["ns=padim;i=6032"]),
        o6.hasComponent(o6.ns["ns=padim;i=6034"]),
    ],
)
o6.reference(padim_objtypes.GasChromatographType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=5000"])
o6.reference(o6.ns["ns=padim;i=5000"], "i=17603", padim_objtypes.IGasChromatographDeviceConditionSetType)
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6050", browseName="ns=padim;Watchdog", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=padim;i=6050"], "i=17597", "ns=irdi;s=0112/2///61987#ABP996#002")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6051", browseName="ns=padim;RemainingDataStorageCapacity", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6051"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ039#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=5040",
    browseName="ns=padim;DeviceConditionSet",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=6050"]), o6.hasProperty(o6.ns["ns=padim;i=6051"])],
)
o6.reference(padim_objtypes.DiodeArraySpectrometerType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=5040"])
o6.reference(o6.ns["ns=padim;i=5040"], "i=17603", padim_objtypes.IDiodeArrayDeviceConditionSetType)
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6060", browseName="ns=padim;Watchdog", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=padim;i=6060"], "i=17597", "ns=irdi;s=0112/2///61987#ABP996#002")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6061", browseName="ns=padim;RemainingDataStorageCapacity", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6061"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ039#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=5050",
    browseName="ns=padim;DeviceConditionSet",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=6060"]), o6.hasProperty(o6.ns["ns=padim;i=6061"])],
)
o6.reference(padim_objtypes.RamanSpectrometerType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=5050"])
o6.reference(o6.ns["ns=padim;i=5050"], "i=17603", padim_objtypes.IRamanDeviceConditionSetType)
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6070", browseName="ns=padim;Watchdog", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=padim;i=6070"], "i=17597", "ns=irdi;s=0112/2///61987#ABP996#002")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6071", browseName="ns=padim;RemainingDataStorageCapacity", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6071"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ039#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=5060",
    browseName="ns=padim;DeviceConditionSet",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=6070"]), o6.hasProperty(o6.ns["ns=padim;i=6071"])],
)
o6.reference(padim_objtypes.FtnirOrFtirSpectrometerType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=5060"])
o6.reference(o6.ns["ns=padim;i=5060"], "i=17603", padim_objtypes.IFtnirOrFtirDeviceConditionSetType)
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6073",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=6073"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6072",
    browseName="ns=padim;SensingElementTemperature",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=6073"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IAmperometricGasDetectorSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=6072"])
o6.reference(o6.ns["ns=padim;i=6072"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6102",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=6102"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6101", browseName="ns=padim;SensingElementTemperature", references=[o6.hasProperty(o6.ns["ns=padim;i=6102"])], dataType=o6.Float, value=0.0
)
o6.reference(o6.ns["ns=padim;i=6101"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6103", browseName="ns=padim;SensorNextCalibrationFixed", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6103"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ016#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6104", browseName="ns=padim;SensorNextCalibrationDynamic", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6104"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ017#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6105", browseName="ns=padim;PowerOnDurationSensor", dataType=ns0.datatypes.Duration, value=0.0)
o6.reference(o6.ns["ns=padim;i=6105"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ010#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6106", browseName="ns=padim;SensingElementResidualLife", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6106"], "i=17597", "ns=irdi;s=0112/2///61987#ABP584#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6107", browseName="ns=padim;RelativeGasFlowRate", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6107"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ011#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6108", browseName="ns=padim;ConsumedSensorCapacity", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6108"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ018#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6109", browseName="ns=padim;RangeExceedancePeakValue", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6109"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ019#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6110", browseName="ns=padim;RangeExceedanceDuration", dataType=ns0.datatypes.Duration, value=0.0)
o6.reference(o6.ns["ns=padim;i=6110"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ020#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6111", browseName="ns=padim;SensingElementResidualSensitivity", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6111"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ040#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=5070",
    browseName="ns=padim;SignalConditionSet",
    modellingRule="Optional",
    references=[
        o6.hasProperty(o6.ns["ns=padim;i=6103"]),
        o6.hasProperty(o6.ns["ns=padim;i=6104"]),
        o6.hasProperty(o6.ns["ns=padim;i=6105"]),
        o6.hasProperty(o6.ns["ns=padim;i=6106"]),
        o6.hasProperty(o6.ns["ns=padim;i=6107"]),
        o6.hasProperty(o6.ns["ns=padim;i=6108"]),
        o6.hasProperty(o6.ns["ns=padim;i=6109"]),
        o6.hasProperty(o6.ns["ns=padim;i=6110"]),
        o6.hasProperty(o6.ns["ns=padim;i=6111"]),
        o6.hasComponent(o6.ns["ns=padim;i=6101"]),
    ],
)
o6.reference(padim_objtypes.AmperometricGasDetectorSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=5070"])
o6.reference(o6.ns["ns=padim;i=5070"], "i=17603", padim_objtypes.IAmperometricGasDetectorSignalConditionSetType)
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6113", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)
o6.reference(o6.ns["ns=padim;i=6113"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(nodeId="ns=padim;i=6112", browseName="ns=padim;AmperometricSensorSlope", references=[o6.hasProperty(o6.ns["ns=padim;i=6113"])], dataType=o6.Float)
o6.reference(o6.ns["ns=padim;i=6112"], "i=17597", "ns=irdi;s=0112/2///61987#ABP572#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6115",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705750616, displayName=o6.LocalizedText("pA"), description=o6.LocalizedText("picoampere")
    ),
)
o6.reference(o6.ns["ns=padim;i=6115"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6114", browseName="ns=padim;AmperometricSensorZeroPoint", references=[o6.hasProperty(o6.ns["ns=padim;i=6115"])], dataType=o6.Float, value=0.0
)
o6.reference(o6.ns["ns=padim;i=6114"], "i=17597", "ns=irdi;s=0112/2///61987#ABP573#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6117",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705746519, displayName=o6.LocalizedText("hPa"), description=o6.LocalizedText("hectopascal")
    ),
)
o6.reference(o6.ns["ns=padim;i=6117"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6116", browseName="ns=padim;AbsoluteAirPressure", references=[o6.hasProperty(o6.ns["ns=padim;i=6117"])], dataType=o6.Float, value=0.0
)
o6.reference(o6.ns["ns=padim;i=6116"], "i=17597", "ns=irdi;s=0112/2///61987#ABP574#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6118", browseName="ns=padim;SensorT90", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6118"], "i=17597", "ns=irdi;s=0112/2///61987#ABP569#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=5071",
    browseName="ns=padim;<SignalCalibrationIdentifier>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(o6.ns["ns=padim;i=6118"]),
        o6.hasComponent(o6.ns["ns=padim;i=6112"]),
        o6.hasComponent(o6.ns["ns=padim;i=6114"]),
        o6.hasComponent(o6.ns["ns=padim;i=6116"]),
    ],
)
o6.reference(padim_objtypes.AmperometricGasDetectorSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=5071"])
o6.reference(o6.ns["ns=padim;i=5071"], "i=17603", padim_objtypes.IAmperometricCalibrationType)
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6120",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705750770, displayName=o6.LocalizedText("s"), description=o6.LocalizedText("second")
    ),
)
o6.reference(o6.ns["ns=padim;i=6120"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6119", browseName="ns=padim;PeakWidth", modellingRule="Optional", references=[o6.hasProperty(o6.ns["ns=padim;i=6120"])], dataType=o6.Float, value=0.0
)
o6.reference(padim_objtypes.IGasChromatographSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=6119"])
o6.reference(o6.ns["ns=padim;i=6119"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ022#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6122",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705743670, displayName=o6.LocalizedText("V"), description=o6.LocalizedText("volt")
    ),
)
o6.reference(o6.ns["ns=padim;i=6122"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6121", browseName="ns=padim;PeakHeight", modellingRule="Optional", references=[o6.hasProperty(o6.ns["ns=padim;i=6122"])], dataType=o6.Float, value=0.0
)
o6.reference(padim_objtypes.IGasChromatographSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=6121"])
o6.reference(o6.ns["ns=padim;i=6121"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ023#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6124",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741328, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
    ),
)
o6.reference(o6.ns["ns=padim;i=6124"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6123", browseName="ns=padim;PeakArea", modellingRule="Optional", references=[o6.hasProperty(o6.ns["ns=padim;i=6124"])], dataType=o6.Float, value=0.0
)
o6.reference(padim_objtypes.IGasChromatographSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=6123"])
o6.reference(o6.ns["ns=padim;i=6123"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ042#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6127",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705750770, displayName=o6.LocalizedText("s"), description=o6.LocalizedText("second")
    ),
)
o6.reference(o6.ns["ns=padim;i=6127"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6126",
    browseName="ns=padim;ExpectedRetentionTime",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=6127"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IGasChromatographSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=6126"])
o6.reference(o6.ns["ns=padim;i=6126"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ034#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6129",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705750770, displayName=o6.LocalizedText("s"), description=o6.LocalizedText("second")
    ),
)
o6.reference(o6.ns["ns=padim;i=6129"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6128",
    browseName="ns=padim;ActualRetentionTime",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=6129"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IGasChromatographSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=6128"])
o6.reference(o6.ns["ns=padim;i=6128"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ035#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6140", browseName="ns=padim;CalibrationRange1ResponseFactor", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6140"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ024#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6142",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705848917, displayName=o6.LocalizedText("ppm"), description=o6.LocalizedText("parts per million")
    ),
)
o6.reference(o6.ns["ns=padim;i=6142"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6141", browseName="ns=padim;CalibrationRange1LowerRangeValue", references=[o6.hasProperty(o6.ns["ns=padim;i=6142"])], dataType=o6.Float, value=0.0
)
o6.reference(o6.ns["ns=padim;i=6141"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ025#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6144",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705848917, displayName=o6.LocalizedText("ppm"), description=o6.LocalizedText("parts per million")
    ),
)
o6.reference(o6.ns["ns=padim;i=6144"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6143", browseName="ns=padim;CalibrationRange1UpperRangeValue", references=[o6.hasProperty(o6.ns["ns=padim;i=6144"])], dataType=o6.Float, value=100.0
)
o6.reference(o6.ns["ns=padim;i=6143"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ026#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6145", browseName="ns=padim;CalibrationRange2ResponseFactor", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6145"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ027#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6147",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705848917, displayName=o6.LocalizedText("ppm"), description=o6.LocalizedText("parts per million")
    ),
)
o6.reference(o6.ns["ns=padim;i=6147"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6146", browseName="ns=padim;CalibrationRange2LowerRangeValue", references=[o6.hasProperty(o6.ns["ns=padim;i=6147"])], dataType=o6.Float, value=0.0
)
o6.reference(o6.ns["ns=padim;i=6146"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ028#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6149",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705848917, displayName=o6.LocalizedText("ppm"), description=o6.LocalizedText("parts per million")
    ),
)
o6.reference(o6.ns["ns=padim;i=6149"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6148", browseName="ns=padim;CalibrationRange2UpperRangeValue", references=[o6.hasProperty(o6.ns["ns=padim;i=6149"])], dataType=o6.Float, value=100.0
)
o6.reference(o6.ns["ns=padim;i=6148"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ029#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6150", browseName="ns=padim;CalibrationRange3ResponseFactor", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6150"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ030#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6152",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705848917, displayName=o6.LocalizedText("ppm"), description=o6.LocalizedText("parts per million")
    ),
)
o6.reference(o6.ns["ns=padim;i=6152"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6151", browseName="ns=padim;CalibrationRange3LowerRangeValue", references=[o6.hasProperty(o6.ns["ns=padim;i=6152"])], dataType=o6.Float, value=0.0
)
o6.reference(o6.ns["ns=padim;i=6151"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ031#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6154",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705848917, displayName=o6.LocalizedText("ppm"), description=o6.LocalizedText("parts per million")
    ),
)
o6.reference(o6.ns["ns=padim;i=6154"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6153", browseName="ns=padim;CalibrationRange3UpperRangeValue", references=[o6.hasProperty(o6.ns["ns=padim;i=6154"])], dataType=o6.Float, value=100.0
)
o6.reference(o6.ns["ns=padim;i=6153"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ032#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=5072",
    browseName="ns=padim;<SignalCalibrationIdentifier>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(o6.ns["ns=padim;i=6140"]),
        o6.hasProperty(o6.ns["ns=padim;i=6145"]),
        o6.hasProperty(o6.ns["ns=padim;i=6150"]),
        o6.hasComponent(o6.ns["ns=padim;i=6141"]),
        o6.hasComponent(o6.ns["ns=padim;i=6143"]),
        o6.hasComponent(o6.ns["ns=padim;i=6146"]),
        o6.hasComponent(o6.ns["ns=padim;i=6148"]),
        o6.hasComponent(o6.ns["ns=padim;i=6151"]),
        o6.hasComponent(o6.ns["ns=padim;i=6153"]),
    ],
)
o6.reference(padim_objtypes.GasChromatographSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=5072"])
o6.reference(o6.ns["ns=padim;i=5072"], "i=17603", padim_objtypes.IGasChromatographCalibrationType)
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6156",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705750770, displayName=o6.LocalizedText("s"), description=o6.LocalizedText("second")
    ),
)
o6.reference(o6.ns["ns=padim;i=6156"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(nodeId="ns=padim;i=6155", browseName="ns=padim;PeakWidth", references=[o6.hasProperty(o6.ns["ns=padim;i=6156"])], dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6155"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ022#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6158",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705743670, displayName=o6.LocalizedText("V"), description=o6.LocalizedText("volt")
    ),
)
o6.reference(o6.ns["ns=padim;i=6158"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(nodeId="ns=padim;i=6157", browseName="ns=padim;PeakHeight", references=[o6.hasProperty(o6.ns["ns=padim;i=6158"])], dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6157"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ023#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6160",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741328, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
    ),
)
o6.reference(o6.ns["ns=padim;i=6160"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(nodeId="ns=padim;i=6159", browseName="ns=padim;PeakArea", references=[o6.hasProperty(o6.ns["ns=padim;i=6160"])], dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6159"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ042#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6161", browseName="ns=padim;TailingFactor", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6161"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ033#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6163",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705750770, displayName=o6.LocalizedText("s"), description=o6.LocalizedText("second")
    ),
)
o6.reference(o6.ns["ns=padim;i=6163"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6162", browseName="ns=padim;ExpectedRetentionTime", references=[o6.hasProperty(o6.ns["ns=padim;i=6163"])], dataType=o6.Float, value=0.0
)
o6.reference(o6.ns["ns=padim;i=6162"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ034#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6165",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705750770, displayName=o6.LocalizedText("s"), description=o6.LocalizedText("second")
    ),
)
o6.reference(o6.ns["ns=padim;i=6165"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6164", browseName="ns=padim;ActualRetentionTime", references=[o6.hasProperty(o6.ns["ns=padim;i=6165"])], dataType=o6.Float, value=0.0
)
o6.reference(o6.ns["ns=padim;i=6164"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ035#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6166", browseName="ns=padim;InjectionTime", dataType=o6.DateTime, value=o6.DateTime("1601-01-01T00:00:00Z"))
o6.reference(o6.ns["ns=padim;i=6166"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ006#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6167", browseName="ns=padim;ComponentName", dataType=o6.String)
o6.reference(o6.ns["ns=padim;i=6167"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ045#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=5073",
    browseName="ns=padim;SignalConditionSet",
    modellingRule="Optional",
    references=[
        o6.hasProperty(o6.ns["ns=padim;i=6161"]),
        o6.hasProperty(o6.ns["ns=padim;i=6166"]),
        o6.hasProperty(o6.ns["ns=padim;i=6167"]),
        o6.hasComponent(o6.ns["ns=padim;i=6155"]),
        o6.hasComponent(o6.ns["ns=padim;i=6157"]),
        o6.hasComponent(o6.ns["ns=padim;i=6159"]),
        o6.hasComponent(o6.ns["ns=padim;i=6162"]),
        o6.hasComponent(o6.ns["ns=padim;i=6164"]),
    ],
)
o6.reference(padim_objtypes.GasChromatographSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=5073"])
o6.reference(o6.ns["ns=padim;i=5073"], "i=17603", padim_objtypes.IGasChromatographSignalConditionSetType)
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6170",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=6170"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6169",
    browseName="ns=padim;SensingElementTemperature",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=6170"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IFtnirOrFtirSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=6169"])
o6.reference(o6.ns["ns=padim;i=6169"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.vartypes.DataItemType(nodeId="ns=padim;i=6180", browseName="ns=padim;TransmissionRatio", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6180"], "i=17597", "ns=irdi;s=0112/2///61987#ABP582#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6182",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=6182"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6181", browseName="ns=padim;SensingElementTemperature", references=[o6.hasProperty(o6.ns["ns=padim;i=6182"])], dataType=o6.Float, value=0.0
)
o6.reference(o6.ns["ns=padim;i=6181"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6183", browseName="ns=padim;MahalanobisDistance", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6183"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ037#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6184", browseName="ns=padim;SpectralResidual", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6184"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ038#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6185", browseName="ns=padim;ElectronicsReadNoise", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6185"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ057#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6186", browseName="ns=padim;LaserResidualLife", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6186"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ044#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=5075",
    browseName="ns=padim;SignalConditionSet",
    modellingRule="Optional",
    references=[
        o6.hasProperty(o6.ns["ns=padim;i=6183"]),
        o6.hasProperty(o6.ns["ns=padim;i=6184"]),
        o6.hasProperty(o6.ns["ns=padim;i=6185"]),
        o6.hasProperty(o6.ns["ns=padim;i=6186"]),
        o6.hasComponent(o6.ns["ns=padim;i=6180"]),
        o6.hasComponent(o6.ns["ns=padim;i=6181"]),
    ],
)
o6.reference(padim_objtypes.FtnirOrFtirSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=5075"])
o6.reference(o6.ns["ns=padim;i=5075"], "i=17603", padim_objtypes.IFtnirOrFtirSignalConditionSetType)
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6189",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=6189"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6188",
    browseName="ns=padim;SensingElementTemperature",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=6189"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IDiodeArraySignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=6188"])
o6.reference(o6.ns["ns=padim;i=6188"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6200", browseName="ns=padim;SourceResidualLife", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6200"], "i=17597", "ns=irdi;s=0112/2///61987#ABP552#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6202",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=6202"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6201", browseName="ns=padim;SensingElementTemperature", references=[o6.hasProperty(o6.ns["ns=padim;i=6202"])], dataType=o6.Float, value=0.0
)
o6.reference(o6.ns["ns=padim;i=6201"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6203", browseName="ns=padim;MahalanobisDistance", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6203"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ037#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6204", browseName="ns=padim;SpectralResidual", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6204"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ038#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6205", browseName="ns=padim;ElectronicsReadNoise", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6205"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ057#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=5077",
    browseName="ns=padim;SignalConditionSet",
    modellingRule="Optional",
    references=[
        o6.hasProperty(o6.ns["ns=padim;i=6200"]),
        o6.hasProperty(o6.ns["ns=padim;i=6203"]),
        o6.hasProperty(o6.ns["ns=padim;i=6204"]),
        o6.hasProperty(o6.ns["ns=padim;i=6205"]),
        o6.hasComponent(o6.ns["ns=padim;i=6201"]),
    ],
)
o6.reference(padim_objtypes.DiodeArraySignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=5077"])
o6.reference(o6.ns["ns=padim;i=5077"], "i=17603", padim_objtypes.IDiodeArraySignalConditionSetType)
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6208",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=6208"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6207",
    browseName="ns=padim;SensingElementTemperature",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=6208"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IRamanSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=6207"])
o6.reference(o6.ns["ns=padim;i=6207"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6220", browseName="ns=padim;SourceResidualLife", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6220"], "i=17597", "ns=irdi;s=0112/2///61987#ABP552#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6222",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=6222"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6221", browseName="ns=padim;SensingElementTemperature", references=[o6.hasProperty(o6.ns["ns=padim;i=6222"])], dataType=o6.Float, value=0.0
)
o6.reference(o6.ns["ns=padim;i=6221"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6223", browseName="ns=padim;MahalanobisDistance", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6223"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ037#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6224", browseName="ns=padim;SpectralResidual", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6224"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ038#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6225", browseName="ns=padim;ElectronicsReadNoise", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6225"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ057#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=5079",
    browseName="ns=padim;SignalConditionSet",
    modellingRule="Optional",
    references=[
        o6.hasProperty(o6.ns["ns=padim;i=6220"]),
        o6.hasProperty(o6.ns["ns=padim;i=6223"]),
        o6.hasProperty(o6.ns["ns=padim;i=6224"]),
        o6.hasProperty(o6.ns["ns=padim;i=6225"]),
        o6.hasComponent(o6.ns["ns=padim;i=6221"]),
    ],
)
o6.reference(padim_objtypes.RamanSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=5079"])
o6.reference(o6.ns["ns=padim;i=5079"], "i=17603", padim_objtypes.IRamanSignalConditionSetType)
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6227",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=6227"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6226",
    browseName="ns=padim;SensingElementTemperature",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=6227"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IInfraredSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=6226"])
o6.reference(o6.ns["ns=padim;i=6226"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6241",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=6241"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6240", browseName="ns=padim;SensingElementTemperature", references=[o6.hasProperty(o6.ns["ns=padim;i=6241"])], dataType=o6.Float, value=0.0
)
o6.reference(o6.ns["ns=padim;i=6240"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6242", browseName="ns=padim;SourceResidualLife", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6242"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ041#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6243", browseName="ns=padim;TransmissionRatio", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6243"], "i=17597", "ns=irdi;s=0112/2///61987#ABP582#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6244", browseName="ns=padim;SensorNextCalibrationFixed", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6244"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ016#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6245", browseName="ns=padim;SensorNextCalibrationDynamic", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6245"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ017#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6246", browseName="ns=padim;PowerOnDurationSensor", dataType=ns0.datatypes.Duration, value=0.0)
o6.reference(o6.ns["ns=padim;i=6246"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ010#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6247", browseName="ns=padim;SensingElementResidualLife", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6247"], "i=17597", "ns=irdi;s=0112/2///61987#ABP584#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6248", browseName="ns=padim;RelativeGasFlowRate", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6248"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ011#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6249", browseName="ns=padim;SensingElementResidualSensitivity", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6249"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ040#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=5080",
    browseName="ns=padim;SignalConditionSet",
    modellingRule="Optional",
    references=[
        o6.hasProperty(o6.ns["ns=padim;i=6242"]),
        o6.hasProperty(o6.ns["ns=padim;i=6243"]),
        o6.hasProperty(o6.ns["ns=padim;i=6244"]),
        o6.hasProperty(o6.ns["ns=padim;i=6245"]),
        o6.hasProperty(o6.ns["ns=padim;i=6246"]),
        o6.hasProperty(o6.ns["ns=padim;i=6247"]),
        o6.hasProperty(o6.ns["ns=padim;i=6248"]),
        o6.hasProperty(o6.ns["ns=padim;i=6249"]),
        o6.hasComponent(o6.ns["ns=padim;i=6240"]),
    ],
)
o6.reference(padim_objtypes.InfraredSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=5080"])
o6.reference(o6.ns["ns=padim;i=5080"], "i=17603", padim_objtypes.IInfraredSignalConditionSetType)
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6252", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)
o6.reference(o6.ns["ns=padim;i=6252"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6251", browseName="ns=padim;CellResistance", modellingRule="Optional", references=[o6.hasProperty(o6.ns["ns=padim;i=6252"])], dataType=o6.Float, value=0.0
)
o6.reference(padim_objtypes.IZirconiumDioxideSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=6251"])
o6.reference(o6.ns["ns=padim;i=6251"], "i=17597", "ns=irdi;s=0112/2///61987#ABP596#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6254",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=6254"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6253",
    browseName="ns=padim;SensingElementTemperature",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=6254"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.ICatalyticBeadSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=6253"])
o6.reference(o6.ns["ns=padim;i=6253"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6261",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749524, displayName=o6.LocalizedText("mV"), description=o6.LocalizedText("millivolt")
    ),
)
o6.reference(o6.ns["ns=padim;i=6261"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6260", browseName="ns=padim;SensorValue", modellingRule="Optional", references=[o6.hasProperty(o6.ns["ns=padim;i=6261"])], dataType=o6.Float, value=0.0
)
o6.reference(padim_objtypes.ICatalyticBeadSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=6260"])
o6.reference(o6.ns["ns=padim;i=6260"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ021#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6282",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741427, displayName=o6.LocalizedText(";C"), description=o6.LocalizedText("degree Celsius")
    ),
)
o6.reference(o6.ns["ns=padim;i=6282"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=6281", browseName="ns=padim;SensingElementTemperature", references=[o6.hasProperty(o6.ns["ns=padim;i=6282"])], dataType=o6.Float, value=0.0
)
o6.reference(o6.ns["ns=padim;i=6281"], "i=17597", "ns=irdi;s=0112/2///61987#ABP565#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6283", browseName="ns=padim;SensorNextCalibrationFixed", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6283"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ016#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6284", browseName="ns=padim;SensorNextCalibrationDynamic", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6284"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ017#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6285", browseName="ns=padim;PowerOnDurationSensor", dataType=ns0.datatypes.Duration, value=0.0)
o6.reference(o6.ns["ns=padim;i=6285"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ010#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6286", browseName="ns=padim;SensingElementResidualLife", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6286"], "i=17597", "ns=irdi;s=0112/2///61987#ABP584#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6287", browseName="ns=padim;RelativeGasFlowRate", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6287"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ011#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6289",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705749524, displayName=o6.LocalizedText("mV"), description=o6.LocalizedText("millivolt")
    ),
)
o6.reference(o6.ns["ns=padim;i=6289"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(nodeId="ns=padim;i=6288", browseName="ns=padim;SensorValue", references=[o6.hasProperty(o6.ns["ns=padim;i=6289"])], dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=padim;i=6288"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ021#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=6290", browseName="ns=padim;SensingElementResidualSensitivity", dataType=o6.Float, value=1.0)
o6.reference(o6.ns["ns=padim;i=6290"], "i=17597", "ns=irdi;s=0112/2///61987#ABQ040#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=5081",
    browseName="ns=padim;SignalConditionSet",
    modellingRule="Optional",
    references=[
        o6.hasProperty(o6.ns["ns=padim;i=6283"]),
        o6.hasProperty(o6.ns["ns=padim;i=6284"]),
        o6.hasProperty(o6.ns["ns=padim;i=6285"]),
        o6.hasProperty(o6.ns["ns=padim;i=6286"]),
        o6.hasProperty(o6.ns["ns=padim;i=6287"]),
        o6.hasProperty(o6.ns["ns=padim;i=6290"]),
        o6.hasComponent(o6.ns["ns=padim;i=6281"]),
        o6.hasComponent(o6.ns["ns=padim;i=6288"]),
    ],
)
o6.reference(padim_objtypes.CatalyticBeadSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=5081"])
o6.reference(o6.ns["ns=padim;i=5081"], "i=17603", padim_objtypes.ICatalyticBeadSignalConditionSetType)
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6291",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741328, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
    ),
)
o6.reference(o6.ns["ns=padim;i=6291"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1354",
    browseName="ns=padim;RelativeHeatOutput",
    displayName="Relative heat output",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=padim;i=6291"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(padim_objtypes.IZirconiumDioxideSignalConditionSetType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1354"])
o6.reference(o6.ns["ns=padim;i=1354"], "i=17597", "ns=irdi;s=0112/2///61987#ABP585#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=6292",
    browseName="EngineeringUnits",
    dataType=ns0.datatypes.EUInformation,
    value=ns0.datatypes.EUInformation(
        namespaceUri="http://www.opcfoundation.org/UA/units/cdd/IEC62720", unitId=705741328, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
    ),
)
o6.reference(o6.ns["ns=padim;i=6292"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=padim;i=1434",
    browseName="ns=padim;RelativeHeatOutput",
    displayName="Relative heat output",
    references=[o6.hasProperty(o6.ns["ns=padim;i=6292"])],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(o6.ns["ns=padim;i=1434"], "i=17597", "ns=irdi;s=0112/2///61987#ABP585#001")
ns0.objtypes.BaseObjectType(
    nodeId="ns=padim;i=1306",
    browseName="ns=padim;SignalConditionSet",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=padim;i=1434"]), o6.hasComponent(o6.ns["ns=padim;i=1435"]), o6.hasComponent(o6.ns["ns=padim;i=1436"])],
)
o6.reference(padim_objtypes.ZirconiumDioxideSignalType, ns0.reftypes.HasComponent, o6.ns["ns=padim;i=1306"])
o6.reference(o6.ns["ns=padim;i=1306"], "i=17603", padim_objtypes.IZirconiumDioxideSignalConditionSetType)


del Any, TYPE_CHECKING, uuid, o6, di, irdi, ns0, padim_datypes, padim_vartypes, padim_objtypes
