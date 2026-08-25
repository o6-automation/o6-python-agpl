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

"""Generated OPC UA fx_cm namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.fx_data as fx_data
import o6.ns.ns0 as ns0
from . import reftypes as fx_cm_reftypes
from . import datatypes as fx_cm_datypes
from . import vartypes as fx_cm_vartypes
from . import objtypes as fx_cm_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=1114", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=1115", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.PortableKeyValuePair, o6.ns["ns=fx_cm;i=1115"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=1116", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.PortableKeyValuePair, o6.ns["ns=fx_cm;i=1116"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=1117", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=1118", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.ServerAddressDataType, o6.ns["ns=fx_cm;i=1118"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=1119", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.ServerAddressDataType, o6.ns["ns=fx_cm;i=1119"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=1159", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=1160", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.PortableRelativePath, o6.ns["ns=fx_cm;i=1160"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=1161", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.PortableRelativePath, o6.ns["ns=fx_cm;i=1161"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=1222", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=1223", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.PortableRelativePathElement, o6.ns["ns=fx_cm;i=1223"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=1224", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.PortableRelativePathElement, o6.ns["ns=fx_cm;i=1224"])
ns0.objtypes.StateType(
    nodeId="ns=fx_cm;i=1169",
    browseName="ns=fx_cm;Ready",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=1386", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(fx_cm_objtypes.ConnectionConfigurationSetStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=1169"])
ns0.objtypes.StateType(
    nodeId="ns=fx_cm;i=1170",
    browseName="ns=fx_cm;Processing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=1387", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(fx_cm_objtypes.ConnectionConfigurationSetStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=1170"])
ns0.objtypes.StateType(
    nodeId="ns=fx_cm;i=1171",
    browseName="ns=fx_cm;Error",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=1388", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(fx_cm_objtypes.ConnectionConfigurationSetStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=1171"])
ns0.objtypes.TransitionType(
    nodeId="ns=fx_cm;i=1174",
    browseName="ns=fx_cm;ReadyToProcessing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=1391", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(fx_cm_objtypes.ConnectionConfigurationSetStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=1174"])
o6.reference(o6.ns["ns=fx_cm;i=1174"], "i=51", o6.ns["ns=fx_cm;i=1169"])
o6.reference(o6.ns["ns=fx_cm;i=1174"], "i=52", o6.ns["ns=fx_cm;i=1170"])
o6.reference(o6.ns["ns=fx_cm;i=1174"], "i=54", fx_cm_objtypes.ConnectionConfigurationSetProcessingStartedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=fx_cm;i=1175",
    browseName="ns=fx_cm;ProcessingToReady",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=1392", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(fx_cm_objtypes.ConnectionConfigurationSetStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=1175"])
o6.reference(o6.ns["ns=fx_cm;i=1175"], "i=51", o6.ns["ns=fx_cm;i=1170"])
o6.reference(o6.ns["ns=fx_cm;i=1175"], "i=52", o6.ns["ns=fx_cm;i=1169"])
o6.reference(o6.ns["ns=fx_cm;i=1175"], "i=54", fx_cm_objtypes.ConnectionConfigurationSetProcessingSucceededEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=fx_cm;i=1176",
    browseName="ns=fx_cm;ProcessingToError",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=1393", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(fx_cm_objtypes.ConnectionConfigurationSetStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=1176"])
o6.reference(o6.ns["ns=fx_cm;i=1176"], "i=51", o6.ns["ns=fx_cm;i=1170"])
o6.reference(o6.ns["ns=fx_cm;i=1176"], "i=52", o6.ns["ns=fx_cm;i=1171"])
o6.reference(o6.ns["ns=fx_cm;i=1176"], "i=54", fx_cm_objtypes.ConnectionConfigurationSetProcessingFailedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=fx_cm;i=1177",
    browseName="ns=fx_cm;ErrorToProcessing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=1394", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(fx_cm_objtypes.ConnectionConfigurationSetStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=1177"])
o6.reference(o6.ns["ns=fx_cm;i=1177"], "i=51", o6.ns["ns=fx_cm;i=1171"])
o6.reference(o6.ns["ns=fx_cm;i=1177"], "i=52", o6.ns["ns=fx_cm;i=1170"])
o6.reference(o6.ns["ns=fx_cm;i=1177"], "i=54", fx_cm_objtypes.ConnectionConfigurationSetProcessingStartedEventType)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=1459",
    browseName="ns=fx_cm;Address",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=1460", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.NetworkAddressDataType,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_objtypes.PubSubCommunicationFlowConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=1459"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5012", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.PortableNodeIdentifierValuePair, o6.ns["ns=fx_cm;i=5012"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5015", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.PortableNodeIdentifierValuePair, o6.ns["ns=fx_cm;i=5015"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5016", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5017", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5018", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.CommunicationFlowQosDataType, o6.ns["ns=fx_cm;i=5018"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5019", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.CommunicationFlowQosDataType, o6.ns["ns=fx_cm;i=5019"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5025", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5026", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.NodeIdTranslationDataType, o6.ns["ns=fx_cm;i=5026"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5027", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.NodeIdTranslationDataType, o6.ns["ns=fx_cm;i=5027"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5029", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5030", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.ConnectionConfigurationSetConfDataType, o6.ns["ns=fx_cm;i=5030"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5031", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.ConnectionConfigurationSetConfDataType, o6.ns["ns=fx_cm;i=5031"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5032", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5033", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.ConnectionConfigurationConfDataType, o6.ns["ns=fx_cm;i=5033"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5034", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.ConnectionConfigurationConfDataType, o6.ns["ns=fx_cm;i=5034"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5035", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5036", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.ConnectionEndpointConfigurationConfDataType, o6.ns["ns=fx_cm;i=5036"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5037", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.ConnectionEndpointConfigurationConfDataType, o6.ns["ns=fx_cm;i=5037"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5038", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5039", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.PubSubCommunicationFlowConfigurationConfDataType, o6.ns["ns=fx_cm;i=5039"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5040", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.PubSubCommunicationFlowConfigurationConfDataType, o6.ns["ns=fx_cm;i=5040"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5041", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5042", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.SubscriberConfigurationConfDataType, o6.ns["ns=fx_cm;i=5042"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5043", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.SubscriberConfigurationConfDataType, o6.ns["ns=fx_cm;i=5043"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5044", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5048", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.AutomationComponentConfigurationConfDataType, o6.ns["ns=fx_cm;i=5048"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5049", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.AutomationComponentConfigurationConfDataType, o6.ns["ns=fx_cm;i=5049"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5050", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5051", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.SecurityKeyServerAddressConfDataType, o6.ns["ns=fx_cm;i=5051"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5054", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.SecurityKeyServerAddressConfDataType, o6.ns["ns=fx_cm;i=5054"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5055", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5056", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.ServerAddressConfDataType, o6.ns["ns=fx_cm;i=5056"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5057", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5058", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.PortableNodeIdentifier, o6.ns["ns=fx_cm;i=5058"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5059", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.PortableNodeIdentifier, o6.ns["ns=fx_cm;i=5059"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5060", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.ServerAddressConfDataType, o6.ns["ns=fx_cm;i=5060"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5061", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5062", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.AssetVerificationConfDataType, o6.ns["ns=fx_cm;i=5062"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5063", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.AssetVerificationConfDataType, o6.ns["ns=fx_cm;i=5063"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5064", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5065", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.PubSubCommunicationModelConfigurationDataType, o6.ns["ns=fx_cm;i=5065"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5066", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.PubSubCommunicationModelConfigurationDataType, o6.ns["ns=fx_cm;i=5066"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5067", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5068", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.NodeIdentifier, o6.ns["ns=fx_cm;i=5068"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5069", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.NodeIdentifier, o6.ns["ns=fx_cm;i=5069"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5070", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5071", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.NodeIdentifierValuePair, o6.ns["ns=fx_cm;i=5071"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5072", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.NodeIdentifierValuePair, o6.ns["ns=fx_cm;i=5072"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5073", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5074", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.NodeIdTranslationConfDataType, o6.ns["ns=fx_cm;i=5074"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5075", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.NodeIdTranslationConfDataType, o6.ns["ns=fx_cm;i=5075"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5076", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5077", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.AddressSelectionDataType, o6.ns["ns=fx_cm;i=5077"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5078", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.AddressSelectionDataType, o6.ns["ns=fx_cm;i=5078"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5080", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5081", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.ReceiveQosSelectionDataType, o6.ns["ns=fx_cm;i=5081"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5082", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.ReceiveQosSelectionDataType, o6.ns["ns=fx_cm;i=5082"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5088", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5089", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.ConnectionDiagnosticsDataType, o6.ns["ns=fx_cm;i=5089"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5090", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.ConnectionDiagnosticsDataType, o6.ns["ns=fx_cm;i=5090"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5091", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5092", browseName="Default XML")
o6.hasEncoding(fx_cm_datypes.SecurityKeyServerAddressDataType, o6.ns["ns=fx_cm;i=5092"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_cm;i=5093", browseName="Default JSON")
o6.hasEncoding(fx_cm_datypes.SecurityKeyServerAddressDataType, o6.ns["ns=fx_cm;i=5093"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashFXSlashCMSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=fx_cm;i=5001",
    browseName="ns=fx_cm;http://opcfoundation.org/UA/FX/CM/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6001", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6002", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2026-07-22T18:52:36Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6003", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/FX/CM/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6004", browseName="NamespaceVersion", dataType=o6.String, value="1.00.04")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fx_cm;i=6005", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fx_cm;i=6006", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["0:15000"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6007", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6008",
    browseName="ns=fx_cm;AutomationComponentNode",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6011", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=fx_cm_datypes.PortableNodeIdentifier,
    accessLevel=3,
    userAccessLevel=1,
)
fx_cm_objtypes.AutomationComponentConfigurationType(
    nodeId="ns=fx_cm;i=5006",
    browseName="ns=fx_cm;AutomationComponentConfiguration",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=fx_cm;i=6008"]),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_cm;i=6016", browseName="ns=fx_cm;CommandBundleRequired", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1),
            "ns=fx_cm;i=4003",
        ),
    ],
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=fx_cm;i=6017",
    browseName="LastTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6018", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_cm;i=6020", browseName="ns=fx_cm;ServerAddressDataType", dataType=o6.String, value="ServerAddressDataType")
o6.reference(o6.ns["ns=fx_cm;i=1117"], "i=39", o6.ns["ns=fx_cm;i=6020"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_cm;i=6021", browseName="ns=fx_cm;ServerAddressDataType", dataType=o6.String, value="//xs:element[@name='ServerAddressDataType']")
o6.reference(o6.ns["ns=fx_cm;i=1118"], "i=39", o6.ns["ns=fx_cm;i=6021"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_cm;i=6022", browseName="ns=fx_cm;SecurityKeyServerAddressDataType", dataType=o6.String, value="SecurityKeyServerAddressDataType")
o6.reference(o6.ns["ns=fx_cm;i=5091"], "i=39", o6.ns["ns=fx_cm;i=6022"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=6023", browseName="ns=fx_cm;SecurityKeyServerAddressDataType", dataType=o6.String, value="//xs:element[@name='SecurityKeyServerAddressDataType']"
)
o6.reference(o6.ns["ns=fx_cm;i=5092"], "i=39", o6.ns["ns=fx_cm;i=6023"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_cm;i=6025", browseName="ns=fx_cm;PortableNodeIdentifierValuePair", dataType=o6.String, value="PortableNodeIdentifierValuePair")
o6.reference(o6.ns["ns=fx_cm;i=5016"], "i=39", o6.ns["ns=fx_cm;i=6025"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=6026", browseName="ns=fx_cm;PortableNodeIdentifierValuePair", dataType=o6.String, value="//xs:element[@name='PortableNodeIdentifierValuePair']"
)
o6.reference(o6.ns["ns=fx_cm;i=5012"], "i=39", o6.ns["ns=fx_cm;i=6026"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6027",
    browseName="ns=fx_cm;CleanupTimeout",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6028", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.Duration,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_cm;i=6031", browseName="ns=fx_cm;PortableKeyValuePair", dataType=o6.String, value="PortableKeyValuePair")
o6.reference(o6.ns["ns=fx_cm;i=1114"], "i=39", o6.ns["ns=fx_cm;i=6031"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_cm;i=6032", browseName="ns=fx_cm;PortableKeyValuePair", dataType=o6.String, value="//xs:element[@name='PortableKeyValuePair']")
o6.reference(o6.ns["ns=fx_cm;i=1115"], "i=39", o6.ns["ns=fx_cm;i=6032"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_cm;i=6033", browseName="ns=fx_cm;PortableNodeIdentifier", dataType=o6.String, value="PortableNodeIdentifier")
o6.reference(o6.ns["ns=fx_cm;i=5057"], "i=39", o6.ns["ns=fx_cm;i=6033"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=6034", browseName="ns=fx_cm;PortableNodeIdentifier", dataType=o6.String, value="//xs:element[@name='PortableNodeIdentifier']"
)
o6.reference(o6.ns["ns=fx_cm;i=5058"], "i=39", o6.ns["ns=fx_cm;i=6034"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_cm;i=6035", browseName="ns=fx_cm;PortableRelativePath", dataType=o6.String, value="PortableRelativePath")
o6.reference(o6.ns["ns=fx_cm;i=1159"], "i=39", o6.ns["ns=fx_cm;i=6035"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_cm;i=6036", browseName="ns=fx_cm;PortableRelativePath", dataType=o6.String, value="//xs:element[@name='PortableRelativePath']")
o6.reference(o6.ns["ns=fx_cm;i=1160"], "i=39", o6.ns["ns=fx_cm;i=6036"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_cm;i=6037", browseName="ns=fx_cm;PortableRelativePathElement", dataType=o6.String, value="PortableRelativePathElement")
o6.reference(o6.ns["ns=fx_cm;i=1222"], "i=39", o6.ns["ns=fx_cm;i=6037"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6039",
    browseName="ns=fx_cm;Address",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6040", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.UriString,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_vartypes.SecurityKeyServerAddressType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6039"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6041",
    browseName="ns=fx_cm;SecurityPolicyUri",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6042", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.String,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_vartypes.SecurityKeyServerAddressType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6041"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6043",
    browseName="ns=fx_cm;ServerUri",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6044", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.UriString,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_vartypes.SecurityKeyServerAddressType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6043"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6045",
    browseName="ns=fx_cm;AutomationComponentNode",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6046", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=fx_cm_datypes.PortableNodeIdentifier,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_objtypes.AutomationComponentConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6045"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=6047", browseName="ns=fx_cm;PortableRelativePathElement", dataType=o6.String, value="//xs:element[@name='PortableRelativePathElement']"
)
o6.reference(o6.ns["ns=fx_cm;i=1223"], "i=39", o6.ns["ns=fx_cm;i=6047"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6052",
    browseName="ns=fx_cm;AssetToVerify",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6053", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=fx_cm_datypes.PortableNodeIdentifier,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6057",
    browseName="ns=fx_cm;AutomationComponentNode",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6058", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=fx_cm_datypes.PortableNodeIdentifier,
    accessLevel=3,
    userAccessLevel=1,
)
fx_cm_objtypes.AutomationComponentConfigurationType(
    nodeId="ns=fx_cm;i=5004",
    browseName="ns=fx_cm;<AutomationComponentConfiguration>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasComponent(fx_cm_objtypes.CommunicationModelConfigurationType(nodeId="ns=fx_cm;i=5101", browseName="ns=fx_cm;CommunicationModelConfig", _allow_abstract=True)),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6057"]),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_cm;i=6010", browseName="ns=fx_cm;CommandBundleRequired", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1),
            "ns=fx_cm;i=4003",
        ),
    ],
)
o6.reference(fx_cm_objtypes.ConnectionConfigurationSetType, fx_cm_reftypes.HasAutomationComponentConfiguration, o6.ns["ns=fx_cm;i=5004"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6060",
    browseName="ns=fx_cm;IsPersistent",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6061", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.Boolean,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6066",
    browseName="ns=fx_cm;Address",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6067", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.UriString,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_vartypes.ServerAddressType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6066"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6070",
    browseName="ns=fx_cm;Name",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6071", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.String,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_objtypes.ConnectionEndpointParameterType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6070"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6073",
    browseName="ns=fx_cm;CleanupTimeout",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6074", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.Duration,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_objtypes.ConnectionEndpointParameterType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6073"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6069",
    browseName="ns=fx_cm;SecurityMode",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6075", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.MessageSecurityMode,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_vartypes.ServerAddressType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6069"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6072",
    browseName="ns=fx_cm;IsPersistent",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6077", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.Boolean,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_objtypes.ConnectionEndpointParameterType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6072"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6076",
    browseName="ns=fx_cm;SecurityPolicyUri",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6078", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.String,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_vartypes.ServerAddressType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6076"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6079",
    browseName="ns=fx_cm;ServerUri",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6080", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.UriString,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_vartypes.ServerAddressType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6079"])
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=fx_cm;i=6081",
    browseName="LastTransition",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6024", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
o6.reference(fx_cm_objtypes.ConnectionConfigurationSetStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6081"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=fx_cm;i=6019",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6083", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6085",
    browseName="ns=fx_cm;Address",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6086", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.UriString,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6087",
    browseName="ns=fx_cm;SecurityMode",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6088", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.MessageSecurityMode,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6090",
    browseName="EnumValues",
    parent="ns=fx_cm;i=3001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("StartEditing"), description=o6.LocalizedText("The ConnectionManager shall allow editing of the ConnectionConfigurationSets.")
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("CommitUpdates"),
            description=o6.LocalizedText("The ConnectionManager shall commit all updates from the ConnectionConfigurationSets."),
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("DiscardUpdates"),
            description=o6.LocalizedText("The ConnectionManager shall discard the updates to the ConnectionConfigurationSets."),
        ),
    ],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_cm;i=6096", browseName="ns=fx_cm;CommunicationFlowQosDataType", dataType=o6.String, value="CommunicationFlowQosDataType")
o6.reference(o6.ns["ns=fx_cm;i=5017"], "i=39", o6.ns["ns=fx_cm;i=6096"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6097",
    browseName="ns=fx_cm;FunctionalEntityNode",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6098", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=fx_cm_datypes.PortableNodeIdentifier,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_objtypes.ConnectionEndpointConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6097"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6089",
    browseName="ns=fx_cm;SecurityPolicyUri",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6099", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.String,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6100",
    browseName="ns=fx_cm;ServerUri",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6101", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.UriString,
    accessLevel=3,
    userAccessLevel=1,
)
fx_cm_vartypes.ServerAddressType(
    nodeId="ns=fx_cm;i=6038",
    browseName="ns=fx_cm;<ServerAddress>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=fx_cm;i=6085"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6087"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6089"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6100"]),
    ],
    dataType=fx_cm_datypes.ServerAddressDataType,
    value=fx_cm_datypes.ServerAddressDataType(address="", securityMode=ns0.datatypes.MessageSecurityMode.INVALID, securityPolicyUri="", serverUri=""),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_objtypes.ConnectionConfigurationSetType, fx_cm_reftypes.HasServerAddress, o6.ns["ns=fx_cm;i=6038"])
o6.reference(o6.ns["ns=fx_cm;i=6038"], "ns=fx_cm;i=1063", o6.ns["ns=fx_cm;i=5004"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6103",
    browseName="ns=fx_cm;Address",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6104", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.UriString,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6105",
    browseName="ns=fx_cm;SecurityPolicyUri",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6106", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.String,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6110",
    browseName="ns=fx_cm;Address",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6111", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.NetworkAddressDataType,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6113",
    browseName="ns=fx_cm;Qos",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6114", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=fx_cm_datypes.CommunicationFlowQosDataType,
    value=fx_cm_datypes.CommunicationFlowQosDataType(qosCategory="", transmitQos=[], receiveQos=[]),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_objtypes.PubSubCommunicationFlowConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6113"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6112",
    browseName="ns=fx_cm;ServerUri",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6115", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.UriString,
    accessLevel=3,
    userAccessLevel=1,
)
fx_cm_vartypes.SecurityKeyServerAddressType(
    nodeId="ns=fx_cm;i=6102",
    browseName="ns=fx_cm;SecurityKeyServer",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=fx_cm;i=6103"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6105"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6112"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_cm;i=6116", browseName="ns=fx_cm;UsePushModel", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=fx_cm_datypes.SecurityKeyServerAddressDataType,
    value=fx_cm_datypes.SecurityKeyServerAddressDataType(address="", securityPolicyUri="", serverUri="", usePushModel=False),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_objtypes.ConnectionConfigurationSetType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6102"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6117",
    browseName="ns=fx_cm;CleanupTimeout",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6118", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.Duration,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6119",
    browseName="ns=fx_cm;IsPersistent",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6120", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.Boolean,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6123",
    browseName="ns=fx_cm;FunctionalEntityNode",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6124", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=fx_cm_datypes.PortableNodeIdentifier,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6122",
    browseName="ns=fx_cm;Name",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6125", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.String,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6126",
    browseName="ns=fx_cm;CleanupTimeout",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6127", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.Duration,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6128",
    browseName="ns=fx_cm;IsPersistent",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6129", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.Boolean,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6131",
    browseName="ns=fx_cm;Name",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6132", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.String,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6133",
    browseName="ns=fx_cm;FunctionalEntityNode",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6134", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=fx_cm_datypes.PortableNodeIdentifier,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6135",
    browseName="ns=fx_cm;FunctionalEntityNode",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6136", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=fx_cm_datypes.PortableNodeIdentifier,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6138",
    browseName="ns=fx_cm;CleanupTimeout",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6139", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.Duration,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6140",
    browseName="ns=fx_cm;IsPersistent",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6141", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.Boolean,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6143",
    browseName="ns=fx_cm;Name",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6144", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.String,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6145",
    browseName="ns=fx_cm;CleanupTimeout",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6146", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.Duration,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6147",
    browseName="ns=fx_cm;IsPersistent",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6148", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.Boolean,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6150",
    browseName="ns=fx_cm;Name",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6151", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.String,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6152",
    browseName="ns=fx_cm;CleanupTimeout",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6153", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.Duration,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=6155", browseName="ns=fx_cm;CommunicationFlowQosDataType", dataType=o6.String, value="//xs:element[@name='CommunicationFlowQosDataType']"
)
o6.reference(o6.ns["ns=fx_cm;i=5018"], "i=39", o6.ns["ns=fx_cm;i=6155"])
ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6156",
    browseName="EnumValues",
    parent="ns=fx_cm;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("ActionEstablishConnectionsEnabled"),
            description=o6.LocalizedText("The ConnectionManager shall establish enabled Connections from the ConnectionConfigurationSets."),
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("ActionEstablishConnectionsDisabled"),
            description=o6.LocalizedText("The ConnectionManager shall establish disabled Connections from the ConnectionConfigurationSets."),
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("ActionEstablishConnections"),
            description=o6.LocalizedText("The ConnectionManager shall establish Connections from the ConnectionConfigurationSets."),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("ActionRemoveConnections"),
            description=o6.LocalizedText("The ConnectionManager shall disable and remove Connections from the ConnectionConfigurationSets."),
        ),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("ActionEnableConnections"),
            description=o6.LocalizedText("The ConnectionManager shall enable Connections from the ConnectionConfigurationSets."),
        ),
        ns0.datatypes.EnumValueType(
            value=5,
            displayName=o6.LocalizedText("ActionDisableConnections"),
            description=o6.LocalizedText("The ConnectionManager shall disable Connections from the ConnectionConfigurationSets."),
        ),
    ],
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6095",
    browseName="ns=fx_cm;AssetToVerify",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6157", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=fx_cm_datypes.PortableNodeIdentifier,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_objtypes.AssetVerificationType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6095"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6154",
    browseName="ns=fx_cm;IsPersistent",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6161", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.Boolean,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6163",
    browseName="ns=fx_cm;Name",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6164", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.String,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6084",
    browseName="ns=fx_cm;Name",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6165", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.String,
    accessLevel=3,
    userAccessLevel=1,
)
fx_cm_objtypes.ConnectionEndpointParameterType(
    nodeId="ns=fx_cm;i=5053",
    browseName="ns=fx_cm;ConnectionEndpoint",
    references=[
        o6.hasComponent(o6.ns["ns=fx_cm;i=6027"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6059", browseName="ns=fx_cm;ConnectionEndpointTypeId", dataType=ns0.datatypes.PortableNodeId, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6060"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_cm;i=6062", browseName="ns=fx_cm;IsPreconfigured", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6084"]),
    ],
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6166",
    browseName="ns=fx_cm;FunctionalEntityNode",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6167", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=fx_cm_datypes.PortableNodeIdentifier,
    accessLevel=3,
    userAccessLevel=1,
)
fx_cm_objtypes.ConnectionEndpointConfigurationType(
    nodeId="ns=fx_cm;i=5052", browseName="ns=fx_cm;Endpoint1", references=[o6.hasComponent(o6.ns["ns=fx_cm;i=5053"]), o6.hasComponent(o6.ns["ns=fx_cm;i=6166"])]
)
fx_cm_objtypes.ConnectionConfigurationType(
    nodeId="ns=fx_cm;i=5047",
    browseName="ns=fx_cm;Connection",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=fx_cm;i=5052"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_cm;i=6168", browseName="ns=fx_cm;ProcessingResult", dataType=o6.StatusCode)),
    ],
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6170",
    browseName="ns=fx_cm;Address",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6171", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.UriString,
    accessLevel=3,
    userAccessLevel=1,
)
fx_cm_objtypes.ConnectionEndpointParameterType(
    nodeId="ns=fx_cm;i=5002",
    browseName="ns=fx_cm;ConnectionEndpoint",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=fx_cm;i=6117"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6119"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_cm;i=6121", browseName="ns=fx_cm;IsPreconfigured", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6122"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6173", browseName="ns=fx_cm;ConnectionEndpointTypeId", dataType=ns0.datatypes.PortableNodeId, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
)
o6.reference(fx_cm_objtypes.ConnectionEndpointConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=5002"])
fx_cm_objtypes.ConnectionEndpointParameterType(
    nodeId="ns=fx_cm;i=5010",
    browseName="ns=fx_cm;ConnectionEndpoint",
    references=[
        o6.hasComponent(o6.ns["ns=fx_cm;i=6126"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6128"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_cm;i=6130", browseName="ns=fx_cm;IsPreconfigured", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6131"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6174", browseName="ns=fx_cm;ConnectionEndpointTypeId", dataType=ns0.datatypes.PortableNodeId, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
)
fx_cm_objtypes.ConnectionEndpointParameterType(
    nodeId="ns=fx_cm;i=5014",
    browseName="ns=fx_cm;ConnectionEndpoint",
    references=[
        o6.hasComponent(o6.ns["ns=fx_cm;i=6138"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6140"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_cm;i=6142", browseName="ns=fx_cm;IsPreconfigured", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6143"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6175", browseName="ns=fx_cm;ConnectionEndpointTypeId", dataType=ns0.datatypes.PortableNodeId, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
)
fx_cm_objtypes.ConnectionEndpointParameterType(
    nodeId="ns=fx_cm;i=5020",
    browseName="ns=fx_cm;ConnectionEndpoint",
    references=[
        o6.hasComponent(o6.ns["ns=fx_cm;i=6145"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6147"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_cm;i=6149", browseName="ns=fx_cm;IsPreconfigured", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6150"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6177", browseName="ns=fx_cm;ConnectionEndpointTypeId", dataType=ns0.datatypes.PortableNodeId, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
)
fx_cm_objtypes.ConnectionEndpointParameterType(
    nodeId="ns=fx_cm;i=5021",
    browseName="ns=fx_cm;ConnectionEndpoint",
    references=[
        o6.hasComponent(o6.ns["ns=fx_cm;i=6152"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6154"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_cm;i=6162", browseName="ns=fx_cm;IsPreconfigured", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6163"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6178", browseName="ns=fx_cm;ConnectionEndpointTypeId", dataType=ns0.datatypes.PortableNodeId, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6182",
    browseName="ns=fx_cm;MessageReceiveTimeout",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6183", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.Duration,
    accessLevel=3,
    userAccessLevel=1,
)
fx_cm_objtypes.SubscriberConfigurationType(
    nodeId="ns=fx_cm;i=5024",
    browseName="ns=fx_cm;<SubscriberConfiguration>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=fx_cm;i=6110"]), o6.hasComponent(o6.ns["ns=fx_cm;i=6182"])],
)
o6.reference(fx_cm_objtypes.PubSubCommunicationFlowConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=5024"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_cm;i=6186", browseName="ns=fx_cm;NodeIdTranslationDataType", dataType=o6.String, value="NodeIdTranslationDataType")
o6.reference(o6.ns["ns=fx_cm;i=5025"], "i=39", o6.ns["ns=fx_cm;i=6186"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=6187", browseName="ns=fx_cm;NodeIdTranslationDataType", dataType=o6.String, value="//xs:element[@name='NodeIdTranslationDataType']"
)
o6.reference(o6.ns["ns=fx_cm;i=5026"], "i=39", o6.ns["ns=fx_cm;i=6187"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6188",
    browseName="ns=fx_cm;Address",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6189", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.NetworkAddressDataType,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_objtypes.SubscriberConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6188"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6190",
    browseName="ns=fx_cm;MessageReceiveTimeout",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6191", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.Duration,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_objtypes.SubscriberConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6190"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6192",
    browseName="ns=fx_cm;ReceiveQos",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6193", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.ReceiveQosDataType,
    valueRank=1,
    arrayDimensions=[0],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_objtypes.SubscriberConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6192"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6194",
    browseName="ns=fx_cm;TransportProfileUri",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6195", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.String,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_objtypes.PubSubCommunicationFlowConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6194"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6196",
    browseName="ns=fx_cm;HeaderLayoutUri",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6197", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.String,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_objtypes.PubSubCommunicationFlowConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6196"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6210",
    browseName="ns=fx_cm;SecurityMode",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6211", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.MessageSecurityMode,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6212",
    browseName="ns=fx_cm;SecurityPolicyUri",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6213", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.String,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6214",
    browseName="ns=fx_cm;ServerUri",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6215", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.UriString,
    accessLevel=3,
    userAccessLevel=1,
)
fx_cm_vartypes.ServerAddressType(
    nodeId="ns=fx_cm;i=6169",
    browseName="ns=fx_cm;ServerAddress",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=fx_cm;i=6170"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6210"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6212"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6214"]),
    ],
    dataType=fx_cm_datypes.ServerAddressDataType,
    value=fx_cm_datypes.ServerAddressDataType(address="", securityMode=ns0.datatypes.MessageSecurityMode.INVALID, securityPolicyUri="", serverUri=""),
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=fx_cm;i=6216",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6217", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=fx_cm;i=6218",
    browseName="LastTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6220", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
fx_cm_objtypes.ConnectionConfigurationSetStateMachineType(
    nodeId="ns=fx_cm;i=5079",
    browseName="ns=fx_cm;ConnectionConfigurationSetStateMachine",
    references=[o6.hasComponent(o6.ns["ns=fx_cm;i=6216"]), o6.hasComponent(o6.ns["ns=fx_cm;i=6218"])],
)
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6176",
    browseName="ns=fx_cm;FunctionalEntityNode",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6229", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=fx_cm_datypes.PortableNodeIdentifier,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6232",
    browseName="EnumValues",
    parent="ns=fx_cm;i=3011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("ConnectionNotMonitored"), description=o6.LocalizedText("ConnectionManager does not monitor the state of the Connection")
        ),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ConnectionNotEstablished"), description=o6.LocalizedText("Connection does not exist")),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("ConnectionInitial"),
            description=o6.LocalizedText("Connection is being established, but communication model is not linked to ConnectionEndpoint"),
        ),
        ns0.datatypes.EnumValueType(
            value=3, displayName=o6.LocalizedText("ConnectionReady"), description=o6.LocalizedText("Connection is established but communication model is disabled")
        ),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("ConnectionPreOperational"),
            description=o6.LocalizedText("Connection is established and enabled, but communication has not started"),
        ),
        ns0.datatypes.EnumValueType(
            value=5, displayName=o6.LocalizedText("ConnectionOperational"), description=o6.LocalizedText("Connection is established and communication is flowing")
        ),
        ns0.datatypes.EnumValueType(
            value=6,
            displayName=o6.LocalizedText("ConnectionError"),
            description=o6.LocalizedText("Connection is established and enabled, but communication is not possible due to an endpoint error"),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6233",
    browseName="OptionSetValues",
    parent="ns=fx_cm;i=3009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        o6.LocalizedText("EstablishEnabled"),
        o6.LocalizedText("EstablishDisabled"),
        o6.LocalizedText("Establish"),
        o6.LocalizedText("Remove"),
        o6.LocalizedText("Enable"),
        o6.LocalizedText("Disable"),
        o6.LocalizedText("Error"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6234",
    browseName="EnumValues",
    parent="ns=fx_cm;i=3015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[25],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("NoError"), description=o6.LocalizedText("This is returned if no processing has been done or no error exists")
        ),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("UnknownStatus"), description=o6.LocalizedText("The Connection is not monitored and its status is unknown")
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("Rollback"),
            description=o6.LocalizedText("The Connection was successfully established but was rolled back due to errors in related Connections in this ConnectionConfigurationSet"),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("ProcessingStopped"),
            description=o6.LocalizedText("This Connection processing was stopped due to some other error in the ConnectionConfigurationSet"),
        ),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("ConnectionConfigurationSetInvalid"),
            description=o6.LocalizedText("The ConnectionManager could not process this ConnectionConfigurationSet due to a configuration error"),
        ),
        ns0.datatypes.EnumValueType(
            value=5, displayName=o6.LocalizedText("GdsConnectionError"), description=o6.LocalizedText("There was an error related to establishing a session to the GDS")
        ),
        ns0.datatypes.EnumValueType(
            value=6, displayName=o6.LocalizedText("GdsProcessingError"), description=o6.LocalizedText("There was an error related to processing commands with the GDS")
        ),
        ns0.datatypes.EnumValueType(
            value=7, displayName=o6.LocalizedText("AliasNameProcessingError"), description=o6.LocalizedText("There was an error related to resolving AliasNames")
        ),
        ns0.datatypes.EnumValueType(
            value=8, displayName=o6.LocalizedText("ExternalSksConnectionError"), description=o6.LocalizedText("There was an error related to establishing a session to the SKS")
        ),
        ns0.datatypes.EnumValueType(
            value=9, displayName=o6.LocalizedText("ExternalSksProcessingError"), description=o6.LocalizedText("There was an error related to configuring the SKS")
        ),
        ns0.datatypes.EnumValueType(
            value=10,
            displayName=o6.LocalizedText("TargetServerConnectionError"),
            description=o6.LocalizedText("There was an error related to establishing a session to the target Server"),
        ),
        ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("ResolvingNamespacesError"), description=o6.LocalizedText("There was an error resolving Namespaces")),
        ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("ResolvingPathsError"), description=o6.LocalizedText("There was an error resolving BrowsePaths")),
        ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("VerifyAssetError"), description=o6.LocalizedText("There was a verification error on an Asset")),
        ns0.datatypes.EnumValueType(
            value=14, displayName=o6.LocalizedText("VerifyFunctionalEntityError"), description=o6.LocalizedText("There was a verification error on a FunctionalEntity")
        ),
        ns0.datatypes.EnumValueType(
            value=15, displayName=o6.LocalizedText("CreateConnectionEndpointError"), description=o6.LocalizedText("There was an error creating a ConnectionEndpoint")
        ),
        ns0.datatypes.EnumValueType(
            value=16, displayName=o6.LocalizedText("EstablishControlError"), description=o6.LocalizedText("There was an error establishing control of a FunctionalEntity")
        ),
        ns0.datatypes.EnumValueType(
            value=17,
            displayName=o6.LocalizedText("SetConfigurationDataError"),
            description=o6.LocalizedText("There was an error setting configuration information in the FunctionalEntity"),
        ),
        ns0.datatypes.EnumValueType(
            value=18, displayName=o6.LocalizedText("ReassignControlError"), description=o6.LocalizedText("There was an error reassigning the control of a FunctionalEntity")
        ),
        ns0.datatypes.EnumValueType(
            value=19, displayName=o6.LocalizedText("ReserveCommunicationIdsError"), description=o6.LocalizedText("There was an error related to reserving ids")
        ),
        ns0.datatypes.EnumValueType(
            value=20, displayName=o6.LocalizedText("SetCommunicationConfigurationError"), description=o6.LocalizedText("There was an error related to configuring communication")
        ),
        ns0.datatypes.EnumValueType(value=21, displayName=o6.LocalizedText("EnableCommunicationError"), description=o6.LocalizedText("There was an error enabling communication")),
        ns0.datatypes.EnumValueType(value=22, displayName=o6.LocalizedText("CloseConnectionError"), description=o6.LocalizedText("There was an error closing a connection")),
        ns0.datatypes.EnumValueType(
            value=23,
            displayName=o6.LocalizedText("LocalSksKeyPushError"),
            description=o6.LocalizedText("The internal SKS is having a problem with pushing keys to a target Server"),
        ),
        ns0.datatypes.EnumValueType(value=24, displayName=o6.LocalizedText("RuntimeError"), description=o6.LocalizedText("There was an error in a running operation")),
    ],
)
fx_cm_objtypes.ConnectionConfigurationSetStateMachineType(
    nodeId="ns=fx_cm;i=5045",
    browseName="ns=fx_cm;ConnectionConfigurationSetStateMachine",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=fx_cm;i=6017"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6019"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_cm;i=6236", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_cm;i=6237", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
    ],
)
o6.reference(fx_cm_objtypes.ConnectionConfigurationSetType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=5045"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_cm;i=6246", browseName="ns=fx_cm;ConnectionDiagnosticsDataType", dataType=o6.String, value="ConnectionDiagnosticsDataType")
o6.reference(o6.ns["ns=fx_cm;i=5088"], "i=39", o6.ns["ns=fx_cm;i=6246"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=6247", browseName="ns=fx_cm;ConnectionDiagnosticsDataType", dataType=o6.String, value="//xs:element[@name='ConnectionDiagnosticsDataType']"
)
o6.reference(o6.ns["ns=fx_cm;i=5089"], "i=39", o6.ns["ns=fx_cm;i=6247"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=fx_cm;i=5083",
    browseName="ns=di;Diagnostics",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_cm;i=6137", browseName="ns=fx_cm;EstablishCallCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_cm;i=6240", browseName="ns=fx_cm;CloseCallCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_cm;i=6241", browseName="ns=fx_cm;EstablishCallFailedCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_cm;i=6251", browseName="ns=fx_cm;CloseCallFailedCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
    ],
)
o6.reference(fx_cm_objtypes.ConnectionManagerType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=5083"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=1461",
    browseName="ns=fx_cm;PublishingInterval",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=1462", browseName="Selections", valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fx_cm;i=6255",
                browseName="ns=fx_cm;AvailableRanges",
                dataType=fx_data.datatypes.IntervalRange,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
    dataType=ns0.datatypes.Duration,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_objtypes.PubSubCommunicationFlowConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=1461"])
fx_cm_objtypes.ConnectionEndpointConfigurationType(
    nodeId="ns=fx_cm;i=5008",
    browseName="ns=fx_cm;Endpoint1",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=fx_cm;i=5010"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6123"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6280",
                browseName="ns=fx_cm;ConfigurationData",
                dataType=fx_cm_datypes.PortableNodeIdentifierValuePair,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6281",
                browseName="ns=fx_cm;ControlGroups",
                dataType=fx_cm_datypes.PortableNodeIdentifier,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6282",
                browseName="ns=fx_cm;ExpectedVerificationVariables",
                dataType=fx_cm_datypes.PortableNodeIdentifierValuePair,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(fx_cm_objtypes.ConnectionConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=5008"])
fx_cm_objtypes.ConnectionEndpointConfigurationType(
    nodeId="ns=fx_cm;i=5023",
    browseName="ns=fx_cm;Endpoint1",
    references=[
        o6.hasComponent(o6.ns["ns=fx_cm;i=5020"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6135"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6283",
                browseName="ns=fx_cm;ConfigurationData",
                dataType=fx_cm_datypes.PortableNodeIdentifierValuePair,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6284",
                browseName="ns=fx_cm;ControlGroups",
                dataType=fx_cm_datypes.PortableNodeIdentifier,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6285",
                browseName="ns=fx_cm;ExpectedVerificationVariables",
                dataType=fx_cm_datypes.PortableNodeIdentifierValuePair,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=fx_cm;i=5004"], "ns=fx_cm;i=4001", o6.ns["ns=fx_cm;i=5023"])
fx_cm_objtypes.ConnectionEndpointConfigurationType(
    nodeId="ns=fx_cm;i=5009",
    browseName="ns=fx_cm;Endpoint2",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=fx_cm;i=5014"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6133"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6269",
                browseName="ns=fx_cm;ConfigurationData",
                dataType=fx_cm_datypes.PortableNodeIdentifierValuePair,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6270",
                browseName="ns=fx_cm;ControlGroups",
                dataType=fx_cm_datypes.PortableNodeIdentifier,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6298",
                browseName="ns=fx_cm;ExpectedVerificationVariables",
                dataType=fx_cm_datypes.PortableNodeIdentifierValuePair,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(fx_cm_objtypes.ConnectionConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=5009"])
fx_cm_objtypes.ConnectionEndpointConfigurationType(
    nodeId="ns=fx_cm;i=5028",
    browseName="ns=fx_cm;Endpoint2",
    references=[
        o6.hasComponent(o6.ns["ns=fx_cm;i=5021"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6176"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6299",
                browseName="ns=fx_cm;ConfigurationData",
                dataType=fx_cm_datypes.PortableNodeIdentifierValuePair,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6300",
                browseName="ns=fx_cm;ControlGroups",
                dataType=fx_cm_datypes.PortableNodeIdentifier,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6301",
                browseName="ns=fx_cm;ExpectedVerificationVariables",
                dataType=fx_cm_datypes.PortableNodeIdentifierValuePair,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=fx_cm;i=5004"], "ns=fx_cm;i=4001", o6.ns["ns=fx_cm;i=5028"])
o6.reference(o6.ns["ns=fx_cm;i=5028"], "ns=fx_cm;i=4006", o6.ns["ns=fx_cm;i=1202"])
o6.reference(o6.ns["ns=fx_cm;i=5028"], "ns=fx_cm;i=4007", o6.ns["ns=fx_cm;i=1202"])
fx_cm_objtypes.ConnectionConfigurationType(
    nodeId="ns=fx_cm;i=5022",
    browseName="ns=fx_cm;<Connection>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=fx_cm;i=5023"]), o6.hasComponent(o6.ns["ns=fx_cm;i=5028"])],
)
o6.reference(fx_cm_objtypes.ConnectionConfigurationSetType, fx_cm_reftypes.HasConnectionConfiguration, o6.ns["ns=fx_cm;i=5022"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6520",
    browseName="ns=fx_cm;SecurityMode",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6521", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.MessageSecurityMode,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_objtypes.PubSubCommunicationFlowConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6520"])
ns0.vartypes.SelectionListType(
    nodeId="ns=fx_cm;i=6524",
    browseName="ns=fx_cm;SecurityGroupId",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6525", browseName="Selections", valueRank=1, arrayDimensions=[0]))],
    dataType=o6.String,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_cm_objtypes.PubSubCommunicationFlowConfigurationType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=6524"])
fx_cm_objtypes.AssetVerificationType(
    nodeId="ns=fx_cm;i=5007",
    browseName="ns=fx_cm;<AssetVerification>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=fx_cm;i=6052"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6054", browseName="ns=fx_cm;ExpectedVerificationResult", dataType=fx_data.datatypes.AssetVerificationResultEnum, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6055",
                browseName="ns=fx_cm;ExpectedVerificationVariables",
                dataType=fx_cm_datypes.PortableNodeIdentifierValuePair,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6056", browseName="ns=fx_cm;VerificationMode", dataType=fx_data.datatypes.AssetVerificationModeEnum, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_cm;i=6527",
                browseName="ns=fx_cm;ExpectedAdditionalVerificationVariables",
                dataType=fx_cm_datypes.PortableNodeIdentifierValuePair,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(fx_cm_objtypes.AutomationComponentConfigurationType, fx_cm_reftypes.HasAssetToVerify, o6.ns["ns=fx_cm;i=5007"])


ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6012",
    browseName="InputArguments",
    parent="ns=fx_cm;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Action", dataType=o6.NodeId("ns=fx_cm;i=3001"), valueRank=-1),
        ns0.datatypes.Argument(name="ConnectionConfigurationSets", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6013",
    browseName="OutputArguments",
    parent="ns=fx_cm;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Results", dataType=o6.StatusCode, valueRank=1, arrayDimensions=[0])],
)
o6.call(
    nodeId="ns=fx_cm;i=7001",
    browseName="ns=fx_cm;EditConnectionConfigurationSets",
    inputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6012"]),
    outputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6013"]),
)
o6.reference(o6.ns["ns=fx_cm;i=7001"], "i=41", "ns=fx_data;i=1025")

ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6014",
    browseName="InputArguments",
    parent="ns=fx_cm;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Action", dataType=o6.NodeId("ns=fx_cm;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="ConnectionConfigurationSets", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6015",
    browseName="OutputArguments",
    parent="ns=fx_cm;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Results", dataType=o6.StatusCode, valueRank=1, arrayDimensions=[0])],
)
o6.call(
    nodeId="ns=fx_cm;i=7002",
    browseName="ns=fx_cm;ProcessConnectionConfigurationSets",
    inputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6014"]),
    outputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6015"]),
)
o6.reference(o6.ns["ns=fx_cm;i=1174"], "i=53", o6.ns["ns=fx_cm;i=7002"])
o6.reference(o6.ns["ns=fx_cm;i=1177"], "i=53", o6.ns["ns=fx_cm;i=7002"])
o6.reference(o6.ns["ns=fx_cm;i=7002"], "i=41", "ns=fx_data;i=1025")

connectionManager = fx_cm_objtypes.ConnectionManagerType(
    nodeId="ns=fx_cm;i=5011",
    browseName="ns=fx_cm;ConnectionManager",
    references=[
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=fx_cm;i=5003", browseName="ns=fx_cm;ConnectionConfigurationSets")),
        o6.hasComponent(o6.ns["ns=fx_cm;i=7001"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=7002"]),
    ],
    parent="ns=fx_data;i=71",
    referenceType=ns0.reftypes.Organizes,
)


ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6244",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.Argument(name="StartTime", dataType=o6.DateTime, valueRank=-1),
        ns0.datatypes.Argument(name="EndTime", dataType=o6.DateTime, valueRank=-1),
        ns0.datatypes.Argument(name="MaxReturnRecords", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="MinimumSeverity", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="RequestMask", dataType=ns0.datatypes.LogRecordMask, valueRank=-1),
        ns0.datatypes.Argument(name="ContinuationPointIn", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6245",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Results", dataType=ns0.datatypes.LogRecordsDataType, valueRank=-1),
        ns0.datatypes.Argument(name="ContinuationPointOut", dataType=o6.ByteString, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fx_cm;i=7004", browseName="GetRecords", inputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6244"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6245"]))

ns0.objtypes.LogObjectType(
    nodeId="ns=fx_cm;i=5087",
    browseName="ns=fx_cm;ConnectionManagerLog",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6248", browseName="MaxRecords", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6249", browseName="MaxStorageDuration", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6250", browseName="MinimumSeverity", dataType=o6.UInt16)),
        o6.hasComponent(o6.ns["ns=fx_cm;i=7004"]),
    ],
)
o6.reference(fx_cm_objtypes.ConnectionManagerType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=5087"])


ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6029",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="RequireCompleteUpdate", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="Operations", dataType=o6.NodeId("ns=fx_cm;i=13054"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6030",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ChangesApplied", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="OperationResults", dataType=o6.StatusCode, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="ConfigurationObjects", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(nodeId="ns=fx_cm;i=7011", browseName="ns=fx_cm;CloseAndUpdate", inputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6029"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6030"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6048",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_cm;i=7012", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6048"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6049",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6050",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=fx_cm;i=7013", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6049"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6050"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6051",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6063",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_cm;i=7014", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6051"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6063"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6198",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6199",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=fx_cm;i=7015", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6198"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6199"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6200",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=fx_cm;i=7016", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6200"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6204",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=fx_cm;i=7017", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6204"]))

fx_cm_objtypes.ConnectionManagerConfigurationType(
    nodeId="ns=fx_cm;i=5084",
    browseName="ns=fx_cm;ConnectionManagerConfiguration",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6064", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6201", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6202", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6203", browseName="Writable", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=fx_cm;i=7011"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=7012"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=7013"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=7014"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=7015"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=7016"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=7017"]),
    ],
)
o6.reference(fx_cm_objtypes.ConnectionManagerType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=5084"])


ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6221",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_cm;i=7018", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6221"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6222",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_cm;i=7019", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6222"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6223",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6224",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_cm;i=7020", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6223"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6224"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6230",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_cm;i=7021", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6230"]))

di.objtypes.LockingServicesType(
    nodeId="ns=fx_cm;i=5086",
    browseName="ns=di;Lock",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6225", browseName="ns=di;Locked", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6226", browseName="ns=di;LockingClient", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6227", browseName="ns=di;LockingUser", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6228", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=fx_cm;i=7018"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=7019"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=7020"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=7021"]),
    ],
)
fx_cm_objtypes.ConnectionConfigurationSetType(
    nodeId="ns=fx_cm;i=5005",
    browseName="ns=fx_cm;<ConnectionConfigurationSet>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6231", browseName="ns=fx_cm;RollbackOnError", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=fx_cm;i=5079"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=5086"]),
        o6.reference(o6.ns["ns=fx_cm;i=6169"], "ns=fx_cm;i=1053"),
        o6.reference(o6.ns["ns=fx_cm;i=5047"], "ns=fx_cm;i=1057"),
        o6.reference(
            fx_cm_objtypes.CommunicationFlowConfigurationType(
                nodeId="ns=fx_cm;i=5046", browseName="ns=fx_cm;CommunicationFlow", modellingRule="MandatoryPlaceholder", _allow_abstract=True
            ),
            "ns=fx_cm;i=1060",
        ),
        o6.reference(o6.ns["ns=fx_cm;i=5006"], "ns=fx_cm;i=1062"),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=fx_cm;i=1163", browseName="ns=fx_cm;ConnectionConfigurationSets", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=fx_cm;i=5005"])]
)
o6.reference(fx_cm_objtypes.ConnectionManagerType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=1163"])


ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6382",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7037",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_cm;i=7037", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6382"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6383",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7038",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_cm;i=7038", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6383"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6384",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7039",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6385",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7039",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_cm;i=7039", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6384"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6385"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=6390",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7040",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_cm;i=7040", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=6390"]))

di.objtypes.LockingServicesType(
    nodeId="ns=fx_cm;i=5095",
    browseName="ns=di;Lock",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6386", browseName="ns=di;Locked", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6387", browseName="ns=di;LockingClient", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6388", browseName="ns=di;LockingUser", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6389", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=fx_cm;i=7037"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=7038"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=7039"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=7040"]),
    ],
)
o6.reference(fx_cm_objtypes.ConnectionConfigurationSetType, ns0.reftypes.HasComponent, o6.ns["ns=fx_cm;i=5095"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16001", browseName="ns=fx_cm;ConnectionConfigurationSetConfDataType", dataType=o6.String, value="ConnectionConfigurationSetConfDataType"
)
o6.reference(o6.ns["ns=fx_cm;i=5029"], "i=39", o6.ns["ns=fx_cm;i=16001"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16002",
    browseName="ns=fx_cm;ConnectionConfigurationSetConfDataType",
    dataType=o6.String,
    value="//xs:element[@name='ConnectionConfigurationSetConfDataType']",
)
o6.reference(o6.ns["ns=fx_cm;i=5030"], "i=39", o6.ns["ns=fx_cm;i=16002"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16003", browseName="ns=fx_cm;ConnectionConfigurationConfDataType", dataType=o6.String, value="ConnectionConfigurationConfDataType"
)
o6.reference(o6.ns["ns=fx_cm;i=5032"], "i=39", o6.ns["ns=fx_cm;i=16003"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16004", browseName="ns=fx_cm;ConnectionConfigurationConfDataType", dataType=o6.String, value="//xs:element[@name='ConnectionConfigurationConfDataType']"
)
o6.reference(o6.ns["ns=fx_cm;i=5033"], "i=39", o6.ns["ns=fx_cm;i=16004"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16005", browseName="ns=fx_cm;ConnectionEndpointConfigurationConfDataType", dataType=o6.String, value="ConnectionEndpointConfigurationConfDataType"
)
o6.reference(o6.ns["ns=fx_cm;i=5035"], "i=39", o6.ns["ns=fx_cm;i=16005"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16006",
    browseName="ns=fx_cm;ConnectionEndpointConfigurationConfDataType",
    dataType=o6.String,
    value="//xs:element[@name='ConnectionEndpointConfigurationConfDataType']",
)
o6.reference(o6.ns["ns=fx_cm;i=5036"], "i=39", o6.ns["ns=fx_cm;i=16006"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16007", browseName="ns=fx_cm;PubSubCommunicationFlowConfigurationConfDataType", dataType=o6.String, value="PubSubCommunicationFlowConfigurationConfDataType"
)
o6.reference(o6.ns["ns=fx_cm;i=5038"], "i=39", o6.ns["ns=fx_cm;i=16007"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16008",
    browseName="ns=fx_cm;PubSubCommunicationFlowConfigurationConfDataType",
    dataType=o6.String,
    value="//xs:element[@name='PubSubCommunicationFlowConfigurationConfDataType']",
)
o6.reference(o6.ns["ns=fx_cm;i=5039"], "i=39", o6.ns["ns=fx_cm;i=16008"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16009", browseName="ns=fx_cm;SubscriberConfigurationConfDataType", dataType=o6.String, value="SubscriberConfigurationConfDataType"
)
o6.reference(o6.ns["ns=fx_cm;i=5041"], "i=39", o6.ns["ns=fx_cm;i=16009"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16010", browseName="ns=fx_cm;SubscriberConfigurationConfDataType", dataType=o6.String, value="//xs:element[@name='SubscriberConfigurationConfDataType']"
)
o6.reference(o6.ns["ns=fx_cm;i=5042"], "i=39", o6.ns["ns=fx_cm;i=16010"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16011", browseName="ns=fx_cm;AutomationComponentConfigurationConfDataType", dataType=o6.String, value="AutomationComponentConfigurationConfDataType"
)
o6.reference(o6.ns["ns=fx_cm;i=5044"], "i=39", o6.ns["ns=fx_cm;i=16011"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16012",
    browseName="ns=fx_cm;AutomationComponentConfigurationConfDataType",
    dataType=o6.String,
    value="//xs:element[@name='AutomationComponentConfigurationConfDataType']",
)
o6.reference(o6.ns["ns=fx_cm;i=5048"], "i=39", o6.ns["ns=fx_cm;i=16012"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16013", browseName="ns=fx_cm;SecurityKeyServerAddressConfDataType", dataType=o6.String, value="SecurityKeyServerAddressConfDataType"
)
o6.reference(o6.ns["ns=fx_cm;i=5050"], "i=39", o6.ns["ns=fx_cm;i=16013"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16014", browseName="ns=fx_cm;SecurityKeyServerAddressConfDataType", dataType=o6.String, value="//xs:element[@name='SecurityKeyServerAddressConfDataType']"
)
o6.reference(o6.ns["ns=fx_cm;i=5051"], "i=39", o6.ns["ns=fx_cm;i=16014"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_cm;i=16015", browseName="ns=fx_cm;ServerAddressConfDataType", dataType=o6.String, value="ServerAddressConfDataType")
o6.reference(o6.ns["ns=fx_cm;i=5055"], "i=39", o6.ns["ns=fx_cm;i=16015"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16016", browseName="ns=fx_cm;ServerAddressConfDataType", dataType=o6.String, value="//xs:element[@name='ServerAddressConfDataType']"
)
o6.reference(o6.ns["ns=fx_cm;i=5056"], "i=39", o6.ns["ns=fx_cm;i=16016"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_cm;i=16017", browseName="ns=fx_cm;AssetVerificationConfDataType", dataType=o6.String, value="AssetVerificationConfDataType")
o6.reference(o6.ns["ns=fx_cm;i=5061"], "i=39", o6.ns["ns=fx_cm;i=16017"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16018", browseName="ns=fx_cm;AssetVerificationConfDataType", dataType=o6.String, value="//xs:element[@name='AssetVerificationConfDataType']"
)
o6.reference(o6.ns["ns=fx_cm;i=5062"], "i=39", o6.ns["ns=fx_cm;i=16018"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16019", browseName="ns=fx_cm;PubSubCommunicationModelConfigurationDataType", dataType=o6.String, value="PubSubCommunicationModelConfigurationDataType"
)
o6.reference(o6.ns["ns=fx_cm;i=5064"], "i=39", o6.ns["ns=fx_cm;i=16019"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16020",
    browseName="ns=fx_cm;PubSubCommunicationModelConfigurationDataType",
    dataType=o6.String,
    value="//xs:element[@name='PubSubCommunicationModelConfigurationDataType']",
)
o6.reference(o6.ns["ns=fx_cm;i=5065"], "i=39", o6.ns["ns=fx_cm;i=16020"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_cm;i=16021", browseName="ns=fx_cm;NodeIdentifier", dataType=o6.String, value="NodeIdentifier")
o6.reference(o6.ns["ns=fx_cm;i=5067"], "i=39", o6.ns["ns=fx_cm;i=16021"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_cm;i=16022", browseName="ns=fx_cm;NodeIdentifier", dataType=o6.String, value="//xs:element[@name='NodeIdentifier']")
o6.reference(o6.ns["ns=fx_cm;i=5068"], "i=39", o6.ns["ns=fx_cm;i=16022"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_cm;i=16023", browseName="ns=fx_cm;NodeIdentifierValuePair", dataType=o6.String, value="NodeIdentifierValuePair")
o6.reference(o6.ns["ns=fx_cm;i=5070"], "i=39", o6.ns["ns=fx_cm;i=16023"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16024", browseName="ns=fx_cm;NodeIdentifierValuePair", dataType=o6.String, value="//xs:element[@name='NodeIdentifierValuePair']"
)
o6.reference(o6.ns["ns=fx_cm;i=5071"], "i=39", o6.ns["ns=fx_cm;i=16024"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_cm;i=16025", browseName="ns=fx_cm;NodeIdTranslationConfDataType", dataType=o6.String, value="NodeIdTranslationConfDataType")
o6.reference(o6.ns["ns=fx_cm;i=5073"], "i=39", o6.ns["ns=fx_cm;i=16025"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16026", browseName="ns=fx_cm;NodeIdTranslationConfDataType", dataType=o6.String, value="//xs:element[@name='NodeIdTranslationConfDataType']"
)
o6.reference(o6.ns["ns=fx_cm;i=5074"], "i=39", o6.ns["ns=fx_cm;i=16026"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_cm;i=16027", browseName="ns=fx_cm;AddressSelectionDataType", dataType=o6.String, value="AddressSelectionDataType")
o6.reference(o6.ns["ns=fx_cm;i=5076"], "i=39", o6.ns["ns=fx_cm;i=16027"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16028", browseName="ns=fx_cm;AddressSelectionDataType", dataType=o6.String, value="//xs:element[@name='AddressSelectionDataType']"
)
o6.reference(o6.ns["ns=fx_cm;i=5077"], "i=39", o6.ns["ns=fx_cm;i=16028"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_cm;i=16029", browseName="ns=fx_cm;ReceiveQosSelectionDataType", dataType=o6.String, value="ReceiveQosSelectionDataType")
o6.reference(o6.ns["ns=fx_cm;i=5080"], "i=39", o6.ns["ns=fx_cm;i=16029"])
opcDotUaDotFXDotCM = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=fx_cm;i=6091",
    browseName="ns=fx_cm;Opc.Ua.FX.CM",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/FX/CM/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6092", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/FX/CM/")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=fx_cm;i=6242",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6020"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6022"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6025"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6031"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6033"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6035"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6037"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6096"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6186"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6246"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16001"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16003"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16005"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16007"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16009"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16011"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16013"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16015"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16017"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16019"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16021"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16023"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16025"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16027"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16029"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:tns="http://opcfoundation.org/UA/FX/CM/" xmlns:opc="http://opcfoundation.org/BinarySchema/" TargetNamespace="http://opcfoundation.org/UA/FX/CM/" xmlns:ua="http://opcfoundation.org/UA/" xmlns:ns1="http://opcfoundation.org/UA/FX/Data/" DefaultByteOrder="LittleEndian" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:Import Namespace="http://opcfoundation.org/UA/FX/Data/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="AddressSelectionDataType">\n  <opc:Field TypeName="ua:ExtensionObject" Name="Address"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfAddressSelection"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="AddressSelection" LengthField="NoOfAddressSelection"/>\n  <opc:Field TypeName="opc:Boolean" Name="AddressModify"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="AssetVerificationConfDataType">\n  <opc:Field TypeName="opc:Bit" Name="AssetPropertiesSpecified"/>\n  <opc:Field Length="31" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="tns:NodeIdentifier" Name="AssetToVerify"/>\n  <opc:Field TypeName="ns1:AssetVerificationModeEnum" Name="VerificationMode"/>\n  <opc:Field TypeName="ns1:AssetVerificationResultEnum" Name="ExpectedVerificationResult"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfExpectedVerificationVariables"/>\n  <opc:Field TypeName="tns:NodeIdentifierValuePair" Name="ExpectedVerificationVariables" LengthField="NoOfExpectedVerificationVariables"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfExpectedAdditionalVerificationVariables"/>\n  <opc:Field TypeName="tns:NodeIdentifierValuePair" Name="ExpectedAdditionalVerificationVariables" LengthField="NoOfExpectedAdditionalVerificationVariables"/>\n  <opc:Field SwitchField="AssetPropertiesSpecified" TypeName="opc:Int32" Name="NoOfAssetProperties"/>\n  <opc:Field SwitchField="AssetPropertiesSpecified" TypeName="ua:KeyValuePair" Name="AssetProperties" LengthField="NoOfAssetProperties"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="AutomationComponentConfigurationConfDataType">\n  <opc:Field TypeName="opc:CharArray" Name="BrowseName"/>\n  <opc:Field TypeName="tns:NodeIdentifier" Name="AutomationComponentNode"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfAutomationComponentNodeSelection"/>\n  <opc:Field TypeName="tns:NodeIdentifier" Name="AutomationComponentNodeSelection" LengthField="NoOfAutomationComponentNodeSelection"/>\n  <opc:Field TypeName="opc:Boolean" Name="AutomationComponentNodeModify"/>\n  <opc:Field TypeName="opc:Boolean" Name="CommandBundleRequired"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfAssetVerification"/>\n  <opc:Field TypeName="tns:AssetVerificationConfDataType" Name="AssetVerification" LengthField="NoOfAssetVerification"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="CommunicationModelConfig"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfAutomationComponentProperties"/>\n  <opc:Field TypeName="ua:KeyValuePair" Name="AutomationComponentProperties" LengthField="NoOfAutomationComponentProperties"/>\n  <opc:Field TypeName="opc:Int32" Name="ServerAddressIndex"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="CommunicationFlowConfigurationConfDataType">\n  <opc:Field TypeName="opc:Bit" Name="FlowPropertiesSpecified"/>\n  <opc:Field Length="31" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="BrowseName"/>\n  <opc:Field SwitchField="FlowPropertiesSpecified" TypeName="opc:Int32" Name="NoOfFlowProperties"/>\n  <opc:Field SwitchField="FlowPropertiesSpecified" TypeName="ua:KeyValuePair" Name="FlowProperties" LengthField="NoOfFlowProperties"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:CommunicationFlowConfigurationConfDataType" Name="PubSubCommunicationFlowConfigurationConfDataType">\n  <opc:Field TypeName="opc:Bit" Name="FlowPropertiesSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="AddressSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="TransportProfileUriSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="TransportProfileUriSelectionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="TransportProfileUriModifySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="HeaderLayoutUriSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="HeaderLayoutUriSelectionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="HeaderLayoutUriModifySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PublishingIntervalSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PublishingIntervalSelectionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PublishingIntervalModifySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="QosSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="QosSelectionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="QosModifySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SecurityModeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SecurityModeSelectionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SecurityModeModifySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SecurityGroupIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SecurityGroupIdSelectionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SecurityGroupIdModifySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SubscriberConfigurationsSpecified"/>\n  <opc:Field Length="11" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field SourceType="tns:CommunicationFlowConfigurationConfDataType" TypeName="opc:CharArray" Name="BrowseName"/>\n  <opc:Field SourceType="tns:CommunicationFlowConfigurationConfDataType" SwitchField="FlowPropertiesSpecified" TypeName="opc:Int32" Name="NoOfFlowProperties"/>\n  <opc:Field SourceType="tns:CommunicationFlowConfigurationConfDataType" SwitchField="FlowPropertiesSpecified" TypeName="ua:KeyValuePair" Name="FlowProperties" LengthField="NoOfFlowProperties"/>\n  <opc:Field SwitchField="AddressSpecified" TypeName="tns:AddressSelectionDataType" Name="Address"/>\n  <opc:Field SwitchField="TransportProfileUriSpecified" TypeName="opc:CharArray" Name="TransportProfileUri"/>\n  <opc:Field SwitchField="TransportProfileUriSelectionSpecified" TypeName="opc:Int32" Name="NoOfTransportProfileUriSelection"/>\n  <opc:Field SwitchField="TransportProfileUriSelectionSpecified" TypeName="opc:CharArray" Name="TransportProfileUriSelection" LengthField="NoOfTransportProfileUriSelection"/>\n  <opc:Field SwitchField="TransportProfileUriModifySpecified" TypeName="opc:Boolean" Name="TransportProfileUriModify"/>\n  <opc:Field SwitchField="HeaderLayoutUriSpecified" TypeName="opc:CharArray" Name="HeaderLayoutUri"/>\n  <opc:Field SwitchField="HeaderLayoutUriSelectionSpecified" TypeName="opc:Int32" Name="NoOfHeaderLayoutUriSelection"/>\n  <opc:Field SwitchField="HeaderLayoutUriSelectionSpecified" TypeName="opc:CharArray" Name="HeaderLayoutUriSelection" LengthField="NoOfHeaderLayoutUriSelection"/>\n  <opc:Field SwitchField="HeaderLayoutUriModifySpecified" TypeName="opc:Boolean" Name="HeaderLayoutUriModify"/>\n  <opc:Field SwitchField="PublishingIntervalSpecified" TypeName="opc:Double" Name="PublishingInterval"/>\n  <opc:Field SwitchField="PublishingIntervalSelectionSpecified" TypeName="opc:Int32" Name="NoOfPublishingIntervalSelection"/>\n  <opc:Field SwitchField="PublishingIntervalSelectionSpecified" TypeName="opc:Double" Name="PublishingIntervalSelection" LengthField="NoOfPublishingIntervalSelection"/>\n  <opc:Field SwitchField="PublishingIntervalModifySpecified" TypeName="opc:Boolean" Name="PublishingIntervalModify"/>\n  <opc:Field SwitchField="QosSpecified" TypeName="tns:CommunicationFlowQosDataType" Name="Qos"/>\n  <opc:Field SwitchField="QosSelectionSpecified" TypeName="opc:Int32" Name="NoOfQosSelection"/>\n  <opc:Field SwitchField="QosSelectionSpecified" TypeName="tns:CommunicationFlowQosDataType" Name="QosSelection" LengthField="NoOfQosSelection"/>\n  <opc:Field SwitchField="QosModifySpecified" TypeName="opc:Boolean" Name="QosModify"/>\n  <opc:Field SwitchField="SecurityModeSpecified" TypeName="ua:MessageSecurityMode" Name="SecurityMode"/>\n  <opc:Field SwitchField="SecurityModeSelectionSpecified" TypeName="opc:Int32" Name="NoOfSecurityModeSelection"/>\n  <opc:Field SwitchField="SecurityModeSelectionSpecified" TypeName="ua:MessageSecurityMode" Name="SecurityModeSelection" LengthField="NoOfSecurityModeSelection"/>\n  <opc:Field SwitchField="SecurityModeModifySpecified" TypeName="opc:Boolean" Name="SecurityModeModify"/>\n  <opc:Field SwitchField="SecurityGroupIdSpecified" TypeName="opc:CharArray" Name="SecurityGroupId"/>\n  <opc:Field SwitchField="SecurityGroupIdSelectionSpecified" TypeName="opc:Int32" Name="NoOfSecurityGroupIdSelection"/>\n  <opc:Field SwitchField="SecurityGroupIdSelectionSpecified" TypeName="opc:CharArray" Name="SecurityGroupIdSelection" LengthField="NoOfSecurityGroupIdSelection"/>\n  <opc:Field SwitchField="SecurityGroupIdModifySpecified" TypeName="opc:Boolean" Name="SecurityGroupIdModify"/>\n  <opc:Field SwitchField="SubscriberConfigurationsSpecified" TypeName="opc:Int32" Name="NoOfSubscriberConfigurations"/>\n  <opc:Field SwitchField="SubscriberConfigurationsSpecified" TypeName="tns:SubscriberConfigurationConfDataType" Name="SubscriberConfigurations" LengthField="NoOfSubscriberConfigurations"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="CommunicationFlowQosDataType">\n  <opc:Field TypeName="opc:CharArray" Name="QosCategory"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfTransmitQos"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="TransmitQos" LengthField="NoOfTransmitQos"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfReceiveQos"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="ReceiveQos" LengthField="NoOfReceiveQos"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="CommunicationModelConfigurationDataType"/>\n <opc:StructuredType BaseType="tns:CommunicationModelConfigurationDataType" Name="PubSubCommunicationModelConfigurationDataType">\n  <opc:Field TypeName="ua:PubSubConfiguration2DataType" Name="PubSubConfiguration"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfTranslationTable"/>\n  <opc:Field TypeName="tns:NodeIdTranslationDataType" Name="TranslationTable" LengthField="NoOfTranslationTable"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfConfigurationReferences"/>\n  <opc:Field TypeName="ua:PubSubConfigurationRefDataType" Name="ConfigurationReferences" LengthField="NoOfConfigurationReferences"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ConnectionConfigurationConfDataType">\n  <opc:Field TypeName="opc:Bit" Name="Endpoint2Specified"/>\n  <opc:Field TypeName="opc:Bit" Name="ConnectionPropertiesSpecified"/>\n  <opc:Field Length="30" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="BrowseName"/>\n  <opc:Field TypeName="tns:ConnectionEndpointConfigurationConfDataType" Name="Endpoint1"/>\n  <opc:Field SwitchField="Endpoint2Specified" TypeName="tns:ConnectionEndpointConfigurationConfDataType" Name="Endpoint2"/>\n  <opc:Field SwitchField="ConnectionPropertiesSpecified" TypeName="opc:Int32" Name="NoOfConnectionProperties"/>\n  <opc:Field SwitchField="ConnectionPropertiesSpecified" TypeName="ua:KeyValuePair" Name="ConnectionProperties" LengthField="NoOfConnectionProperties"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ConnectionConfigurationSetConfDataType">\n  <opc:Field TypeName="opc:CharArray" Name="BrowseName"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfConnectionConfigurationSetFolder"/>\n  <opc:Field TypeName="opc:CharArray" Name="ConnectionConfigurationSetFolder" LengthField="NoOfConnectionConfigurationSetFolder"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfConnections"/>\n  <opc:Field TypeName="tns:ConnectionConfigurationConfDataType" Name="Connections" LengthField="NoOfConnections"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfCommunicationFlows"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="CommunicationFlows" LengthField="NoOfCommunicationFlows"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfServerAddresses"/>\n  <opc:Field TypeName="tns:ServerAddressConfDataType" Name="ServerAddresses" LengthField="NoOfServerAddresses"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfAutomationComponentConfigurations"/>\n  <opc:Field TypeName="tns:AutomationComponentConfigurationConfDataType" Name="AutomationComponentConfigurations" LengthField="NoOfAutomationComponentConfigurations"/>\n  <opc:Field TypeName="opc:Boolean" Name="RollbackOnError"/>\n  <opc:Field TypeName="tns:SecurityKeyServerAddressConfDataType" Name="SecurityKeyServer"/>\n  <opc:Field TypeName="opc:UInt32" Name="Version"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfConnectionConfigurationSetProperties"/>\n  <opc:Field TypeName="ua:KeyValuePair" Name="ConnectionConfigurationSetProperties" LengthField="NoOfConnectionConfigurationSetProperties"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ConnectionDiagnosticsDataType">\n  <opc:Field TypeName="ua:QualifiedName" Name="Name"/>\n  <opc:Field TypeName="tns:LastActivityMask" Name="LastActivity"/>\n  <opc:Field TypeName="tns:ConnectionStateEnum" Name="ConnectionState"/>\n  <opc:Field TypeName="tns:FxErrorEnum" Name="ErrorEndpoint1"/>\n  <opc:Field TypeName="ua:StatusCode" Name="Endpoint1Status"/>\n  <opc:Field TypeName="tns:FxErrorEnum" Name="ErrorEndpoint2"/>\n  <opc:Field TypeName="ua:StatusCode" Name="Endpoint2Status"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ConnectionEndpointConfigurationConfDataType">\n  <opc:Field TypeName="opc:Bit" Name="FunctionalEntityNodeSelectionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="FunctionalEntityNodeModifySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="NameSelectionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="NameModifySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="InputVariableIdsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="OutputVariableIdsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="CommunicationLinksSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PreconfiguredPublishedDataSetSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PublishedDataSetDataSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PreconfiguredSubscribedDataSetSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SubscribedDataSetDataSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ExpectedVerificationVariablesSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ControlGroupsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ConfigurationDataSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="EndpointPropertiesSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="OutboundFlowIndexSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="InboundFlowIndexSpecified"/>\n  <opc:Field Length="15" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="tns:NodeIdentifier" Name="FunctionalEntityNode"/>\n  <opc:Field SwitchField="FunctionalEntityNodeSelectionSpecified" TypeName="opc:Int32" Name="NoOfFunctionalEntityNodeSelection"/>\n  <opc:Field SwitchField="FunctionalEntityNodeSelectionSpecified" TypeName="tns:NodeIdentifier" Name="FunctionalEntityNodeSelection" LengthField="NoOfFunctionalEntityNodeSelection"/>\n  <opc:Field SwitchField="FunctionalEntityNodeModifySpecified" TypeName="opc:Boolean" Name="FunctionalEntityNodeModify"/>\n  <opc:Field TypeName="opc:CharArray" Name="Name"/>\n  <opc:Field SwitchField="NameSelectionSpecified" TypeName="opc:Int32" Name="NoOfNameSelection"/>\n  <opc:Field SwitchField="NameSelectionSpecified" TypeName="opc:CharArray" Name="NameSelection" LengthField="NoOfNameSelection"/>\n  <opc:Field SwitchField="NameModifySpecified" TypeName="opc:Boolean" Name="NameModify"/>\n  <opc:Field TypeName="ua:NodeId" Name="ConnectionEndpointTypeId"/>\n  <opc:Field SwitchField="InputVariableIdsSpecified" TypeName="opc:Int32" Name="NoOfInputVariableIds"/>\n  <opc:Field SwitchField="InputVariableIdsSpecified" TypeName="tns:NodeIdentifier" Name="InputVariableIds" LengthField="NoOfInputVariableIds"/>\n  <opc:Field SwitchField="OutputVariableIdsSpecified" TypeName="opc:Int32" Name="NoOfOutputVariableIds"/>\n  <opc:Field SwitchField="OutputVariableIdsSpecified" TypeName="tns:NodeIdentifier" Name="OutputVariableIds" LengthField="NoOfOutputVariableIds"/>\n  <opc:Field TypeName="opc:Boolean" Name="IsPersistent"/>\n  <opc:Field TypeName="opc:Double" Name="CleanupTimeout"/>\n  <opc:Field TypeName="opc:Boolean" Name="IsPreconfigured"/>\n  <opc:Field SwitchField="CommunicationLinksSpecified" TypeName="ua:ExtensionObject" Name="CommunicationLinks"/>\n  <opc:Field SwitchField="PreconfiguredPublishedDataSetSpecified" TypeName="opc:CharArray" Name="PreconfiguredPublishedDataSet"/>\n  <opc:Field SwitchField="PublishedDataSetDataSpecified" TypeName="ua:PublishedDataSetDataType" Name="PublishedDataSetData"/>\n  <opc:Field SwitchField="PreconfiguredSubscribedDataSetSpecified" TypeName="opc:CharArray" Name="PreconfiguredSubscribedDataSet"/>\n  <opc:Field SwitchField="SubscribedDataSetDataSpecified" TypeName="ua:StandaloneSubscribedDataSetDataType" Name="SubscribedDataSetData"/>\n  <opc:Field SwitchField="ExpectedVerificationVariablesSpecified" TypeName="opc:Int32" Name="NoOfExpectedVerificationVariables"/>\n  <opc:Field SwitchField="ExpectedVerificationVariablesSpecified" TypeName="tns:NodeIdentifierValuePair" Name="ExpectedVerificationVariables" LengthField="NoOfExpectedVerificationVariables"/>\n  <opc:Field SwitchField="ControlGroupsSpecified" TypeName="opc:Int32" Name="NoOfControlGroups"/>\n  <opc:Field SwitchField="ControlGroupsSpecified" TypeName="tns:NodeIdentifier" Name="ControlGroups" LengthField="NoOfControlGroups"/>\n  <opc:Field SwitchField="ConfigurationDataSpecified" TypeName="opc:Int32" Name="NoOfConfigurationData"/>\n  <opc:Field SwitchField="ConfigurationDataSpecified" TypeName="tns:NodeIdentifierValuePair" Name="ConfigurationData" LengthField="NoOfConfigurationData"/>\n  <opc:Field SwitchField="EndpointPropertiesSpecified" TypeName="opc:Int32" Name="NoOfEndpointProperties"/>\n  <opc:Field SwitchField="EndpointPropertiesSpecified" TypeName="ua:KeyValuePair" Name="EndpointProperties" LengthField="NoOfEndpointProperties"/>\n  <opc:Field TypeName="opc:Int32" Name="AutomationComponentIndex"/>\n  <opc:Field SwitchField="OutboundFlowIndexSpecified" TypeName="opc:Int32" Name="OutboundFlowIndex"/>\n  <opc:Field SwitchField="InboundFlowIndexSpecified" TypeName="opc:Int32" Name="NoOfInboundFlowIndex"/>\n  <opc:Field SwitchField="InboundFlowIndexSpecified" TypeName="opc:Int32" Name="InboundFlowIndex" LengthField="NoOfInboundFlowIndex"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="NodeIdentifierValuePair">\n  <opc:Field TypeName="tns:NodeIdentifier" Name="Key"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfArrayIndex"/>\n  <opc:Field TypeName="opc:UInt32" Name="ArrayIndex" LengthField="NoOfArrayIndex"/>\n  <opc:Field TypeName="ua:Variant" Name="Value"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="NodeIdTranslationConfDataType">\n  <opc:Field TypeName="ua:NodeId" Name="NodePlaceholder"/>\n  <opc:Field TypeName="tns:NodeIdentifier" Name="Node"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="NodeIdTranslationDataType">\n  <opc:Field TypeName="ua:NodeId" Name="NodePlaceholder"/>\n  <opc:Field TypeName="tns:PortableNodeIdentifier" Name="PortableNode"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="PortableKeyValuePair">\n  <opc:Field TypeName="ua:PortableQualifiedName" Name="Key"/>\n  <opc:Field TypeName="ua:Variant" Name="Value"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="PortableNodeIdentifierValuePair">\n  <opc:Field TypeName="tns:PortableNodeIdentifier" Name="Key"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfArrayIndex"/>\n  <opc:Field TypeName="opc:UInt32" Name="ArrayIndex" LengthField="NoOfArrayIndex"/>\n  <opc:Field TypeName="ua:Variant" Name="Value"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="PortableRelativePath">\n  <opc:Field TypeName="opc:Int32" Name="NoOfElements"/>\n  <opc:Field TypeName="tns:PortableRelativePathElement" Name="Elements" LengthField="NoOfElements"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="PortableRelativePathElement">\n  <opc:Field TypeName="ua:PortableNodeId" Name="ReferenceTypeId"/>\n  <opc:Field TypeName="opc:Boolean" Name="IsInverse"/>\n  <opc:Field TypeName="opc:Boolean" Name="IncludeSubtypes"/>\n  <opc:Field TypeName="ua:PortableQualifiedName" Name="TargetName"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ReceiveQosSelectionDataType">\n  <opc:Field TypeName="opc:Int32" Name="NoOfReceiveQos"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="ReceiveQos" LengthField="NoOfReceiveQos"/>\n  <opc:Field TypeName="ua:Variant" Name="ReceiveQosSelection"/>\n  <opc:Field TypeName="opc:Boolean" Name="ReceiveQosModify"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="SecurityKeyServerAddressConfDataType">\n  <opc:Field TypeName="opc:Bit" Name="AddressSelectionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="AddressModifySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SecurityPolicyUriSelectionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SecurityPolicyUriModifySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ServerUriSelectionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ServerUriModifySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SecurityGroupsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PubSubKeyPushTargetsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SksPropertiesSpecified"/>\n  <opc:Field Length="23" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="Address"/>\n  <opc:Field SwitchField="AddressSelectionSpecified" TypeName="opc:Int32" Name="NoOfAddressSelection"/>\n  <opc:Field SwitchField="AddressSelectionSpecified" TypeName="opc:CharArray" Name="AddressSelection" LengthField="NoOfAddressSelection"/>\n  <opc:Field SwitchField="AddressModifySpecified" TypeName="opc:Boolean" Name="AddressModify"/>\n  <opc:Field TypeName="opc:CharArray" Name="SecurityPolicyUri"/>\n  <opc:Field SwitchField="SecurityPolicyUriSelectionSpecified" TypeName="opc:Int32" Name="NoOfSecurityPolicyUriSelection"/>\n  <opc:Field SwitchField="SecurityPolicyUriSelectionSpecified" TypeName="opc:CharArray" Name="SecurityPolicyUriSelection" LengthField="NoOfSecurityPolicyUriSelection"/>\n  <opc:Field SwitchField="SecurityPolicyUriModifySpecified" TypeName="opc:Boolean" Name="SecurityPolicyUriModify"/>\n  <opc:Field TypeName="opc:CharArray" Name="ServerUri"/>\n  <opc:Field SwitchField="ServerUriSelectionSpecified" TypeName="opc:Int32" Name="NoOfServerUriSelection"/>\n  <opc:Field SwitchField="ServerUriSelectionSpecified" TypeName="opc:CharArray" Name="ServerUriSelection" LengthField="NoOfServerUriSelection"/>\n  <opc:Field SwitchField="ServerUriModifySpecified" TypeName="opc:Boolean" Name="ServerUriModify"/>\n  <opc:Field TypeName="opc:Boolean" Name="UsePushModel"/>\n  <opc:Field SwitchField="SecurityGroupsSpecified" TypeName="opc:Int32" Name="NoOfSecurityGroups"/>\n  <opc:Field SwitchField="SecurityGroupsSpecified" TypeName="ua:SecurityGroupDataType" Name="SecurityGroups" LengthField="NoOfSecurityGroups"/>\n  <opc:Field SwitchField="PubSubKeyPushTargetsSpecified" TypeName="opc:Int32" Name="NoOfPubSubKeyPushTargets"/>\n  <opc:Field SwitchField="PubSubKeyPushTargetsSpecified" TypeName="ua:PubSubKeyPushTargetDataType" Name="PubSubKeyPushTargets" LengthField="NoOfPubSubKeyPushTargets"/>\n  <opc:Field SwitchField="SksPropertiesSpecified" TypeName="opc:Int32" Name="NoOfSksProperties"/>\n  <opc:Field SwitchField="SksPropertiesSpecified" TypeName="ua:KeyValuePair" Name="SksProperties" LengthField="NoOfSksProperties"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="SecurityKeyServerAddressDataType">\n  <opc:Field TypeName="opc:CharArray" Name="Address"/>\n  <opc:Field TypeName="opc:CharArray" Name="SecurityPolicyUri"/>\n  <opc:Field TypeName="opc:CharArray" Name="ServerUri"/>\n  <opc:Field TypeName="opc:Boolean" Name="UsePushModel"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ServerAddressConfDataType">\n  <opc:Field TypeName="opc:Bit" Name="AddressSelectionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="AddressModifySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SecurityModeSelectionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SecurityModeModifySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SecurityPolicyUriSelectionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SecurityPolicyUriModifySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ServerUriSelectionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ServerUriModifySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ServerPropertiesSpecified"/>\n  <opc:Field Length="23" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="BrowseName"/>\n  <opc:Field TypeName="opc:CharArray" Name="Address"/>\n  <opc:Field SwitchField="AddressSelectionSpecified" TypeName="opc:Int32" Name="NoOfAddressSelection"/>\n  <opc:Field SwitchField="AddressSelectionSpecified" TypeName="opc:CharArray" Name="AddressSelection" LengthField="NoOfAddressSelection"/>\n  <opc:Field SwitchField="AddressModifySpecified" TypeName="opc:Boolean" Name="AddressModify"/>\n  <opc:Field TypeName="ua:MessageSecurityMode" Name="SecurityMode"/>\n  <opc:Field SwitchField="SecurityModeSelectionSpecified" TypeName="opc:Int32" Name="NoOfSecurityModeSelection"/>\n  <opc:Field SwitchField="SecurityModeSelectionSpecified" TypeName="ua:MessageSecurityMode" Name="SecurityModeSelection" LengthField="NoOfSecurityModeSelection"/>\n  <opc:Field SwitchField="SecurityModeModifySpecified" TypeName="opc:Boolean" Name="SecurityModeModify"/>\n  <opc:Field TypeName="opc:CharArray" Name="SecurityPolicyUri"/>\n  <opc:Field SwitchField="SecurityPolicyUriSelectionSpecified" TypeName="opc:Int32" Name="NoOfSecurityPolicyUriSelection"/>\n  <opc:Field SwitchField="SecurityPolicyUriSelectionSpecified" TypeName="opc:CharArray" Name="SecurityPolicyUriSelection" LengthField="NoOfSecurityPolicyUriSelection"/>\n  <opc:Field SwitchField="SecurityPolicyUriModifySpecified" TypeName="opc:Boolean" Name="SecurityPolicyUriModify"/>\n  <opc:Field TypeName="opc:CharArray" Name="ServerUri"/>\n  <opc:Field SwitchField="ServerUriSelectionSpecified" TypeName="opc:Int32" Name="NoOfServerUriSelection"/>\n  <opc:Field SwitchField="ServerUriSelectionSpecified" TypeName="opc:CharArray" Name="ServerUriSelection" LengthField="NoOfServerUriSelection"/>\n  <opc:Field SwitchField="ServerUriModifySpecified" TypeName="opc:Boolean" Name="ServerUriModify"/>\n  <opc:Field SwitchField="ServerPropertiesSpecified" TypeName="opc:Int32" Name="NoOfServerProperties"/>\n  <opc:Field SwitchField="ServerPropertiesSpecified" TypeName="ua:KeyValuePair" Name="ServerProperties" LengthField="NoOfServerProperties"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfNamespaces"/>\n  <opc:Field TypeName="opc:CharArray" Name="Namespaces" LengthField="NoOfNamespaces"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ServerAddressDataType">\n  <opc:Field TypeName="opc:CharArray" Name="Address"/>\n  <opc:Field TypeName="ua:MessageSecurityMode" Name="SecurityMode"/>\n  <opc:Field TypeName="opc:CharArray" Name="SecurityPolicyUri"/>\n  <opc:Field TypeName="opc:CharArray" Name="ServerUri"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="SubscriberConfigurationConfDataType">\n  <opc:Field TypeName="opc:Bit" Name="AddressSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="MessageReceiveTimeoutSelectionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="MessageReceiveTimeoutModifySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ReceiveQosSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SubscriberPropertiesSpecified"/>\n  <opc:Field Length="27" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="BrowseName"/>\n  <opc:Field SwitchField="AddressSpecified" TypeName="tns:AddressSelectionDataType" Name="Address"/>\n  <opc:Field TypeName="opc:Double" Name="MessageReceiveTimeout"/>\n  <opc:Field SwitchField="MessageReceiveTimeoutSelectionSpecified" TypeName="opc:Int32" Name="NoOfMessageReceiveTimeoutSelection"/>\n  <opc:Field SwitchField="MessageReceiveTimeoutSelectionSpecified" TypeName="opc:Double" Name="MessageReceiveTimeoutSelection" LengthField="NoOfMessageReceiveTimeoutSelection"/>\n  <opc:Field SwitchField="MessageReceiveTimeoutModifySpecified" TypeName="opc:Boolean" Name="MessageReceiveTimeoutModify"/>\n  <opc:Field SwitchField="ReceiveQosSpecified" TypeName="tns:ReceiveQosSelectionDataType" Name="ReceiveQos"/>\n  <opc:Field SwitchField="SubscriberPropertiesSpecified" TypeName="opc:Int32" Name="NoOfSubscriberProperties"/>\n  <opc:Field SwitchField="SubscriberPropertiesSpecified" TypeName="ua:KeyValuePair" Name="SubscriberProperties" LengthField="NoOfSubscriberProperties"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:Union" Name="NodeIdentifier">\n  <opc:Field TypeName="opc:UInt32" Name="SwitchField"/>\n  <opc:Field SwitchField="SwitchField" TypeName="ua:NodeId" Name="Node" SwitchValue="1"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:CharArray" Name="Alias" SwitchValue="2"/>\n  <opc:Field SwitchField="SwitchField" TypeName="ua:RelativePath" Name="IdentifierBrowsePath" SwitchValue="3"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:Union" Name="PortableNodeIdentifier">\n  <opc:Field TypeName="opc:UInt32" Name="SwitchField"/>\n  <opc:Field SwitchField="SwitchField" TypeName="ua:PortableNodeId" Name="Node" SwitchValue="1"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:CharArray" Name="Alias" SwitchValue="2"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:PortableRelativePath" Name="IdentifierBrowsePath" SwitchValue="3"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="ConnectionStateEnum">\n  <opc:EnumeratedValue Value="0" Name="ConnectionNotMonitored"/>\n  <opc:EnumeratedValue Value="1" Name="ConnectionNotEstablished"/>\n  <opc:EnumeratedValue Value="2" Name="ConnectionInitial"/>\n  <opc:EnumeratedValue Value="3" Name="ConnectionReady"/>\n  <opc:EnumeratedValue Value="4" Name="ConnectionPreOperational"/>\n  <opc:EnumeratedValue Value="5" Name="ConnectionOperational"/>\n  <opc:EnumeratedValue Value="6" Name="ConnectionError"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="FxEditEnum">\n  <opc:EnumeratedValue Value="0" Name="StartEditing"/>\n  <opc:EnumeratedValue Value="1" Name="CommitUpdates"/>\n  <opc:EnumeratedValue Value="2" Name="DiscardUpdates"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="FxErrorEnum">\n  <opc:EnumeratedValue Value="0" Name="NoError"/>\n  <opc:EnumeratedValue Value="1" Name="UnknownStatus"/>\n  <opc:EnumeratedValue Value="2" Name="Rollback"/>\n  <opc:EnumeratedValue Value="3" Name="ProcessingStopped"/>\n  <opc:EnumeratedValue Value="4" Name="ConnectionConfigurationSetInvalid"/>\n  <opc:EnumeratedValue Value="5" Name="GdsConnectionError"/>\n  <opc:EnumeratedValue Value="6" Name="GdsProcessingError"/>\n  <opc:EnumeratedValue Value="7" Name="AliasNameProcessingError"/>\n  <opc:EnumeratedValue Value="8" Name="ExternalSksConnectionError"/>\n  <opc:EnumeratedValue Value="9" Name="ExternalSksProcessingError"/>\n  <opc:EnumeratedValue Value="10" Name="TargetServerConnectionError"/>\n  <opc:EnumeratedValue Value="11" Name="ResolvingNamespacesError"/>\n  <opc:EnumeratedValue Value="12" Name="ResolvingPathsError"/>\n  <opc:EnumeratedValue Value="13" Name="VerifyAssetError"/>\n  <opc:EnumeratedValue Value="14" Name="VerifyFunctionalEntityError"/>\n  <opc:EnumeratedValue Value="15" Name="CreateConnectionEndpointError"/>\n  <opc:EnumeratedValue Value="16" Name="EstablishControlError"/>\n  <opc:EnumeratedValue Value="17" Name="SetConfigurationDataError"/>\n  <opc:EnumeratedValue Value="18" Name="ReassignControlError"/>\n  <opc:EnumeratedValue Value="19" Name="ReserveCommunicationIdsError"/>\n  <opc:EnumeratedValue Value="20" Name="SetCommunicationConfigurationError"/>\n  <opc:EnumeratedValue Value="21" Name="EnableCommunicationError"/>\n  <opc:EnumeratedValue Value="22" Name="CloseConnectionError"/>\n  <opc:EnumeratedValue Value="23" Name="LocalSksKeyPushError"/>\n  <opc:EnumeratedValue Value="24" Name="RuntimeError"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="FxProcessEnum">\n  <opc:EnumeratedValue Value="0" Name="ActionEstablishConnectionsEnabled"/>\n  <opc:EnumeratedValue Value="1" Name="ActionEstablishConnectionsDisabled"/>\n  <opc:EnumeratedValue Value="2" Name="ActionEstablishConnections"/>\n  <opc:EnumeratedValue Value="3" Name="ActionRemoveConnections"/>\n  <opc:EnumeratedValue Value="4" Name="ActionEnableConnections"/>\n  <opc:EnumeratedValue Value="5" Name="ActionDisableConnections"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="8" Name="ConnectionConfigurationSetOperation" IsOptionSet="true">\n  <opc:EnumeratedValue Value="0" Name="ElementAdd"/>\n  <opc:EnumeratedValue Value="1" Name="ElementRemove"/>\n  <opc:EnumeratedValue Value="2" Name="ElementReplace"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="16" Name="LastActivityMask" IsOptionSet="true">\n  <opc:EnumeratedValue Value="0" Name="EstablishEnabled"/>\n  <opc:EnumeratedValue Value="1" Name="EstablishDisabled"/>\n  <opc:EnumeratedValue Value="2" Name="Establish"/>\n  <opc:EnumeratedValue Value="3" Name="Remove"/>\n  <opc:EnumeratedValue Value="4" Name="Enable"/>\n  <opc:EnumeratedValue Value="5" Name="Disable"/>\n  <opc:EnumeratedValue Value="15" Name="Error"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_cm;i=16030", browseName="ns=fx_cm;ReceiveQosSelectionDataType", dataType=o6.String, value="//xs:element[@name='ReceiveQosSelectionDataType']"
)
o6.reference(o6.ns["ns=fx_cm;i=5081"], "i=39", o6.ns["ns=fx_cm;i=16030"])
opcDotUaDotFXDotCM_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=fx_cm;i=6093",
    browseName="ns=fx_cm;Opc.Ua.FX.CM",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/FX/CM/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6094", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/FX/CM/Types.xsd")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=fx_cm;i=6243",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6021"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6023"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6026"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6032"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6034"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6036"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6047"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6155"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6187"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=6247"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16002"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16004"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16006"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16008"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16010"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16012"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16014"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16016"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16018"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16020"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16022"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16024"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16026"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16028"]),
        o6.hasComponent(o6.ns["ns=fx_cm;i=16030"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema xmlns:ns2="http://opcfoundation.org/UA/FX/Data/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://opcfoundation.org/UA/FX/CM/Types.xsd" elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/FX/CM/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:import namespace="http://opcfoundation.org/UA/FX/Data/Types.xsd"/>\n <xs:simpleType name="ConnectionStateEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="ConnectionNotMonitored_0"/>\n   <xs:enumeration value="ConnectionNotEstablished_1"/>\n   <xs:enumeration value="ConnectionInitial_2"/>\n   <xs:enumeration value="ConnectionReady_3"/>\n   <xs:enumeration value="ConnectionPreOperational_4"/>\n   <xs:enumeration value="ConnectionOperational_5"/>\n   <xs:enumeration value="ConnectionError_6"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="ConnectionStateEnum" type="tns:ConnectionStateEnum"/>\n <xs:complexType name="ListOfConnectionStateEnum">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="ConnectionStateEnum" nillable="true" type="tns:ConnectionStateEnum" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfConnectionStateEnum" nillable="true" type="tns:ListOfConnectionStateEnum"/>\n <xs:simpleType name="FxEditEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="StartEditing_0"/>\n   <xs:enumeration value="CommitUpdates_1"/>\n   <xs:enumeration value="DiscardUpdates_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="FxEditEnum" type="tns:FxEditEnum"/>\n <xs:complexType name="ListOfFxEditEnum">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="FxEditEnum" nillable="true" type="tns:FxEditEnum" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfFxEditEnum" nillable="true" type="tns:ListOfFxEditEnum"/>\n <xs:simpleType name="FxErrorEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="NoError_0"/>\n   <xs:enumeration value="UnknownStatus_1"/>\n   <xs:enumeration value="Rollback_2"/>\n   <xs:enumeration value="ProcessingStopped_3"/>\n   <xs:enumeration value="ConnectionConfigurationSetInvalid_4"/>\n   <xs:enumeration value="GdsConnectionError_5"/>\n   <xs:enumeration value="GdsProcessingError_6"/>\n   <xs:enumeration value="AliasNameProcessingError_7"/>\n   <xs:enumeration value="ExternalSksConnectionError_8"/>\n   <xs:enumeration value="ExternalSksProcessingError_9"/>\n   <xs:enumeration value="TargetServerConnectionError_10"/>\n   <xs:enumeration value="ResolvingNamespacesError_11"/>\n   <xs:enumeration value="ResolvingPathsError_12"/>\n   <xs:enumeration value="VerifyAssetError_13"/>\n   <xs:enumeration value="VerifyFunctionalEntityError_14"/>\n   <xs:enumeration value="CreateConnectionEndpointError_15"/>\n   <xs:enumeration value="EstablishControlError_16"/>\n   <xs:enumeration value="SetConfigurationDataError_17"/>\n   <xs:enumeration value="ReassignControlError_18"/>\n   <xs:enumeration value="ReserveCommunicationIdsError_19"/>\n   <xs:enumeration value="SetCommunicationConfigurationError_20"/>\n   <xs:enumeration value="EnableCommunicationError_21"/>\n   <xs:enumeration value="CloseConnectionError_22"/>\n   <xs:enumeration value="LocalSksKeyPushError_23"/>\n   <xs:enumeration value="RuntimeError_24"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="FxErrorEnum" type="tns:FxErrorEnum"/>\n <xs:complexType name="ListOfFxErrorEnum">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="FxErrorEnum" nillable="true" type="tns:FxErrorEnum" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfFxErrorEnum" nillable="true" type="tns:ListOfFxErrorEnum"/>\n <xs:simpleType name="FxProcessEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="ActionEstablishConnectionsEnabled_0"/>\n   <xs:enumeration value="ActionEstablishConnectionsDisabled_1"/>\n   <xs:enumeration value="ActionEstablishConnections_2"/>\n   <xs:enumeration value="ActionRemoveConnections_3"/>\n   <xs:enumeration value="ActionEnableConnections_4"/>\n   <xs:enumeration value="ActionDisableConnections_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="FxProcessEnum" type="tns:FxProcessEnum"/>\n <xs:complexType name="ListOfFxProcessEnum">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="FxProcessEnum" nillable="true" type="tns:FxProcessEnum" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfFxProcessEnum" nillable="true" type="tns:ListOfFxProcessEnum"/>\n <xs:complexType name="AddressSelectionDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="Address" type="ua:ExtensionObject" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="AddressSelection" type="ua:ListOfExtensionObject" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="AddressModify" type="xs:boolean" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="AddressSelectionDataType" type="tns:AddressSelectionDataType"/>\n <xs:complexType name="ListOfAddressSelectionDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="AddressSelectionDataType" nillable="true" type="tns:AddressSelectionDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfAddressSelectionDataType" nillable="true" type="tns:ListOfAddressSelectionDataType"/>\n <xs:complexType name="AssetVerificationConfDataType">\n  <xs:sequence>\n   <xs:element name="EncodingMask" type="xs:unsignedInt" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="AssetToVerify" type="tns:NodeIdentifier" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="VerificationMode" type="ns2:AssetVerificationModeEnum" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ExpectedVerificationResult" type="ns2:AssetVerificationResultEnum" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ExpectedVerificationVariables" type="tns:ListOfNodeIdentifierValuePair" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ExpectedAdditionalVerificationVariables" type="tns:ListOfNodeIdentifierValuePair" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="AssetProperties" type="ua:ListOfKeyValuePair" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="AssetVerificationConfDataType" type="tns:AssetVerificationConfDataType"/>\n <xs:complexType name="ListOfAssetVerificationConfDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="AssetVerificationConfDataType" nillable="true" type="tns:AssetVerificationConfDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfAssetVerificationConfDataType" nillable="true" type="tns:ListOfAssetVerificationConfDataType"/>\n <xs:complexType name="AutomationComponentConfigurationConfDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="BrowseName" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="AutomationComponentNode" type="tns:NodeIdentifier" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="AutomationComponentNodeSelection" type="tns:ListOfNodeIdentifier" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="AutomationComponentNodeModify" type="xs:boolean" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="CommandBundleRequired" type="xs:boolean" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="AssetVerification" type="tns:ListOfAssetVerificationConfDataType" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="CommunicationModelConfig" type="ua:ExtensionObject" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="AutomationComponentProperties" type="ua:ListOfKeyValuePair" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ServerAddressIndex" type="xs:int" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="AutomationComponentConfigurationConfDataType" type="tns:AutomationComponentConfigurationConfDataType"/>\n <xs:complexType name="ListOfAutomationComponentConfigurationConfDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="AutomationComponentConfigurationConfDataType" nillable="true" type="tns:AutomationComponentConfigurationConfDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfAutomationComponentConfigurationConfDataType" nillable="true" type="tns:ListOfAutomationComponentConfigurationConfDataType"/>\n <xs:complexType name="CommunicationFlowConfigurationConfDataType">\n  <xs:sequence>\n   <xs:element name="EncodingMask" type="xs:unsignedInt" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="BrowseName" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="FlowProperties" type="ua:ListOfKeyValuePair" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="CommunicationFlowConfigurationConfDataType" type="tns:CommunicationFlowConfigurationConfDataType"/>\n <xs:complexType name="ListOfCommunicationFlowConfigurationConfDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="CommunicationFlowConfigurationConfDataType" nillable="true" type="tns:CommunicationFlowConfigurationConfDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfCommunicationFlowConfigurationConfDataType" nillable="true" type="tns:ListOfCommunicationFlowConfigurationConfDataType"/>\n <xs:complexType name="PubSubCommunicationFlowConfigurationConfDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element maxOccurs="1" name="Address" type="tns:AddressSelectionDataType" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="TransportProfileUri" type="xs:string" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="TransportProfileUriSelection" type="ua:ListOfString" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="TransportProfileUriModify" type="xs:boolean" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="HeaderLayoutUri" type="xs:string" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="HeaderLayoutUriSelection" type="ua:ListOfString" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="HeaderLayoutUriModify" type="xs:boolean" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="PublishingInterval" type="xs:double" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="PublishingIntervalSelection" type="ua:ListOfDouble" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="PublishingIntervalModify" type="xs:boolean" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="Qos" type="tns:CommunicationFlowQosDataType" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="QosSelection" type="tns:ListOfCommunicationFlowQosDataType" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="QosModify" type="xs:boolean" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="SecurityMode" type="ua:MessageSecurityMode" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="SecurityModeSelection" type="ua:ListOfMessageSecurityMode" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="SecurityModeModify" type="xs:boolean" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="SecurityGroupId" type="xs:string" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="SecurityGroupIdSelection" type="ua:ListOfString" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="SecurityGroupIdModify" type="xs:boolean" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="SubscriberConfigurations" type="tns:ListOfSubscriberConfigurationConfDataType" minOccurs="0"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element name="PubSubCommunicationFlowConfigurationConfDataType" type="tns:PubSubCommunicationFlowConfigurationConfDataType"/>\n <xs:complexType name="ListOfPubSubCommunicationFlowConfigurationConfDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="PubSubCommunicationFlowConfigurationConfDataType" nillable="true" type="tns:PubSubCommunicationFlowConfigurationConfDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPubSubCommunicationFlowConfigurationConfDataType" nillable="true" type="tns:ListOfPubSubCommunicationFlowConfigurationConfDataType"/>\n <xs:complexType name="CommunicationFlowQosDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="QosCategory" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="TransmitQos" type="ua:ListOfExtensionObject" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ReceiveQos" type="ua:ListOfExtensionObject" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="CommunicationFlowQosDataType" type="tns:CommunicationFlowQosDataType"/>\n <xs:complexType name="ListOfCommunicationFlowQosDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="CommunicationFlowQosDataType" nillable="true" type="tns:CommunicationFlowQosDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfCommunicationFlowQosDataType" nillable="true" type="tns:ListOfCommunicationFlowQosDataType"/>\n <xs:complexType name="CommunicationModelConfigurationDataType">\n  <xs:sequence/>\n </xs:complexType>\n <xs:element name="CommunicationModelConfigurationDataType" type="tns:CommunicationModelConfigurationDataType"/>\n <xs:complexType name="ListOfCommunicationModelConfigurationDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="CommunicationModelConfigurationDataType" nillable="true" type="tns:CommunicationModelConfigurationDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfCommunicationModelConfigurationDataType" nillable="true" type="tns:ListOfCommunicationModelConfigurationDataType"/>\n <xs:complexType name="PubSubCommunicationModelConfigurationDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element maxOccurs="1" name="PubSubConfiguration" type="ua:PubSubConfiguration2DataType" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="TranslationTable" type="tns:ListOfNodeIdTranslationDataType" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="ConfigurationReferences" type="ua:ListOfPubSubConfigurationRefDataType" minOccurs="0"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element name="PubSubCommunicationModelConfigurationDataType" type="tns:PubSubCommunicationModelConfigurationDataType"/>\n <xs:complexType name="ListOfPubSubCommunicationModelConfigurationDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="PubSubCommunicationModelConfigurationDataType" nillable="true" type="tns:PubSubCommunicationModelConfigurationDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPubSubCommunicationModelConfigurationDataType" nillable="true" type="tns:ListOfPubSubCommunicationModelConfigurationDataType"/>\n <xs:complexType name="ConnectionConfigurationConfDataType">\n  <xs:sequence>\n   <xs:element name="EncodingMask" type="xs:unsignedInt" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="BrowseName" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Endpoint1" type="tns:ConnectionEndpointConfigurationConfDataType" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Endpoint2" type="tns:ConnectionEndpointConfigurationConfDataType" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ConnectionProperties" type="ua:ListOfKeyValuePair" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ConnectionConfigurationConfDataType" type="tns:ConnectionConfigurationConfDataType"/>\n <xs:complexType name="ListOfConnectionConfigurationConfDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="ConnectionConfigurationConfDataType" nillable="true" type="tns:ConnectionConfigurationConfDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfConnectionConfigurationConfDataType" nillable="true" type="tns:ListOfConnectionConfigurationConfDataType"/>\n <xs:complexType name="ConnectionConfigurationSetConfDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="BrowseName" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ConnectionConfigurationSetFolder" type="ua:ListOfString" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Connections" type="tns:ListOfConnectionConfigurationConfDataType" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="CommunicationFlows" type="ua:ListOfExtensionObject" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ServerAddresses" type="tns:ListOfServerAddressConfDataType" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="AutomationComponentConfigurations" type="tns:ListOfAutomationComponentConfigurationConfDataType" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="RollbackOnError" type="xs:boolean" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="SecurityKeyServer" type="tns:SecurityKeyServerAddressConfDataType" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Version" type="xs:unsignedInt" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ConnectionConfigurationSetProperties" type="ua:ListOfKeyValuePair" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ConnectionConfigurationSetConfDataType" type="tns:ConnectionConfigurationSetConfDataType"/>\n <xs:complexType name="ListOfConnectionConfigurationSetConfDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="ConnectionConfigurationSetConfDataType" nillable="true" type="tns:ConnectionConfigurationSetConfDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfConnectionConfigurationSetConfDataType" nillable="true" type="tns:ListOfConnectionConfigurationSetConfDataType"/>\n <xs:complexType name="ConnectionDiagnosticsDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="Name" type="ua:QualifiedName" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="LastActivity" type="xs:unsignedShort" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ConnectionState" type="tns:ConnectionStateEnum" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ErrorEndpoint1" type="tns:FxErrorEnum" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Endpoint1Status" type="ua:StatusCode" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ErrorEndpoint2" type="tns:FxErrorEnum" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Endpoint2Status" type="ua:StatusCode" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ConnectionDiagnosticsDataType" type="tns:ConnectionDiagnosticsDataType"/>\n <xs:complexType name="ListOfConnectionDiagnosticsDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="ConnectionDiagnosticsDataType" nillable="true" type="tns:ConnectionDiagnosticsDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfConnectionDiagnosticsDataType" nillable="true" type="tns:ListOfConnectionDiagnosticsDataType"/>\n <xs:complexType name="ConnectionEndpointConfigurationConfDataType">\n  <xs:sequence>\n   <xs:element name="EncodingMask" type="xs:unsignedInt" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="FunctionalEntityNode" type="tns:NodeIdentifier" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="FunctionalEntityNodeSelection" type="tns:ListOfNodeIdentifier" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="FunctionalEntityNodeModify" type="xs:boolean" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Name" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="NameSelection" type="ua:ListOfString" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="NameModify" type="xs:boolean" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ConnectionEndpointTypeId" type="ua:NodeId" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="InputVariableIds" type="tns:ListOfNodeIdentifier" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="OutputVariableIds" type="tns:ListOfNodeIdentifier" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="IsPersistent" type="xs:boolean" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="CleanupTimeout" type="xs:double" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="IsPreconfigured" type="xs:boolean" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="CommunicationLinks" type="ua:ExtensionObject" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="PreconfiguredPublishedDataSet" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="PublishedDataSetData" type="ua:PublishedDataSetDataType" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="PreconfiguredSubscribedDataSet" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="SubscribedDataSetData" type="ua:StandaloneSubscribedDataSetDataType" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ExpectedVerificationVariables" type="tns:ListOfNodeIdentifierValuePair" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ControlGroups" type="tns:ListOfNodeIdentifier" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ConfigurationData" type="tns:ListOfNodeIdentifierValuePair" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="EndpointProperties" type="ua:ListOfKeyValuePair" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="AutomationComponentIndex" type="xs:int" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="OutboundFlowIndex" type="xs:int" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="InboundFlowIndex" type="ua:ListOfInt32" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ConnectionEndpointConfigurationConfDataType" type="tns:ConnectionEndpointConfigurationConfDataType"/>\n <xs:complexType name="ListOfConnectionEndpointConfigurationConfDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="ConnectionEndpointConfigurationConfDataType" nillable="true" type="tns:ConnectionEndpointConfigurationConfDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfConnectionEndpointConfigurationConfDataType" nillable="true" type="tns:ListOfConnectionEndpointConfigurationConfDataType"/>\n <xs:complexType name="NodeIdentifierValuePair">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="Key" type="tns:NodeIdentifier" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ArrayIndex" type="ua:ListOfUInt32" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Value" type="ua:Variant" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="NodeIdentifierValuePair" type="tns:NodeIdentifierValuePair"/>\n <xs:complexType name="ListOfNodeIdentifierValuePair">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="NodeIdentifierValuePair" nillable="true" type="tns:NodeIdentifierValuePair" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfNodeIdentifierValuePair" nillable="true" type="tns:ListOfNodeIdentifierValuePair"/>\n <xs:complexType name="NodeIdTranslationConfDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="NodePlaceholder" type="ua:NodeId" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Node" type="tns:NodeIdentifier" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="NodeIdTranslationConfDataType" type="tns:NodeIdTranslationConfDataType"/>\n <xs:complexType name="ListOfNodeIdTranslationConfDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="NodeIdTranslationConfDataType" nillable="true" type="tns:NodeIdTranslationConfDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfNodeIdTranslationConfDataType" nillable="true" type="tns:ListOfNodeIdTranslationConfDataType"/>\n <xs:complexType name="NodeIdTranslationDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="NodePlaceholder" type="ua:NodeId" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="PortableNode" type="tns:PortableNodeIdentifier" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="NodeIdTranslationDataType" type="tns:NodeIdTranslationDataType"/>\n <xs:complexType name="ListOfNodeIdTranslationDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="NodeIdTranslationDataType" nillable="true" type="tns:NodeIdTranslationDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfNodeIdTranslationDataType" nillable="true" type="tns:ListOfNodeIdTranslationDataType"/>\n <xs:complexType name="PortableKeyValuePair">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="Key" type="ua:PortableQualifiedName" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Value" type="ua:Variant" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="PortableKeyValuePair" type="tns:PortableKeyValuePair"/>\n <xs:complexType name="ListOfPortableKeyValuePair">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="PortableKeyValuePair" nillable="true" type="tns:PortableKeyValuePair" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPortableKeyValuePair" nillable="true" type="tns:ListOfPortableKeyValuePair"/>\n <xs:complexType name="PortableNodeIdentifierValuePair">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="Key" type="tns:PortableNodeIdentifier" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ArrayIndex" type="ua:ListOfUInt32" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Value" type="ua:Variant" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="PortableNodeIdentifierValuePair" type="tns:PortableNodeIdentifierValuePair"/>\n <xs:complexType name="ListOfPortableNodeIdentifierValuePair">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="PortableNodeIdentifierValuePair" nillable="true" type="tns:PortableNodeIdentifierValuePair" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPortableNodeIdentifierValuePair" nillable="true" type="tns:ListOfPortableNodeIdentifierValuePair"/>\n <xs:complexType name="PortableRelativePath">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="Elements" type="tns:ListOfPortableRelativePathElement" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="PortableRelativePath" type="tns:PortableRelativePath"/>\n <xs:complexType name="ListOfPortableRelativePath">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="PortableRelativePath" nillable="true" type="tns:PortableRelativePath" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPortableRelativePath" nillable="true" type="tns:ListOfPortableRelativePath"/>\n <xs:complexType name="PortableRelativePathElement">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="ReferenceTypeId" type="ua:PortableNodeId" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="IsInverse" type="xs:boolean" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="IncludeSubtypes" type="xs:boolean" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="TargetName" type="ua:PortableQualifiedName" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="PortableRelativePathElement" type="tns:PortableRelativePathElement"/>\n <xs:complexType name="ListOfPortableRelativePathElement">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="PortableRelativePathElement" nillable="true" type="tns:PortableRelativePathElement" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPortableRelativePathElement" nillable="true" type="tns:ListOfPortableRelativePathElement"/>\n <xs:complexType name="ReceiveQosSelectionDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="ReceiveQos" type="ua:ListOfExtensionObject" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ReceiveQosSelection" type="ua:Variant" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ReceiveQosModify" type="xs:boolean" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ReceiveQosSelectionDataType" type="tns:ReceiveQosSelectionDataType"/>\n <xs:complexType name="ListOfReceiveQosSelectionDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="ReceiveQosSelectionDataType" nillable="true" type="tns:ReceiveQosSelectionDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfReceiveQosSelectionDataType" nillable="true" type="tns:ListOfReceiveQosSelectionDataType"/>\n <xs:complexType name="SecurityKeyServerAddressConfDataType">\n  <xs:sequence>\n   <xs:element name="EncodingMask" type="xs:unsignedInt" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Address" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="AddressSelection" type="ua:ListOfString" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="AddressModify" type="xs:boolean" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="SecurityPolicyUri" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="SecurityPolicyUriSelection" type="ua:ListOfString" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="SecurityPolicyUriModify" type="xs:boolean" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ServerUri" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ServerUriSelection" type="ua:ListOfString" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ServerUriModify" type="xs:boolean" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="UsePushModel" type="xs:boolean" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="SecurityGroups" type="ua:ListOfSecurityGroupDataType" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="PubSubKeyPushTargets" type="ua:ListOfPubSubKeyPushTargetDataType" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="SksProperties" type="ua:ListOfKeyValuePair" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="SecurityKeyServerAddressConfDataType" type="tns:SecurityKeyServerAddressConfDataType"/>\n <xs:complexType name="ListOfSecurityKeyServerAddressConfDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="SecurityKeyServerAddressConfDataType" nillable="true" type="tns:SecurityKeyServerAddressConfDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfSecurityKeyServerAddressConfDataType" nillable="true" type="tns:ListOfSecurityKeyServerAddressConfDataType"/>\n <xs:complexType name="SecurityKeyServerAddressDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="Address" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="SecurityPolicyUri" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ServerUri" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="UsePushModel" type="xs:boolean" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="SecurityKeyServerAddressDataType" type="tns:SecurityKeyServerAddressDataType"/>\n <xs:complexType name="ListOfSecurityKeyServerAddressDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="SecurityKeyServerAddressDataType" nillable="true" type="tns:SecurityKeyServerAddressDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfSecurityKeyServerAddressDataType" nillable="true" type="tns:ListOfSecurityKeyServerAddressDataType"/>\n <xs:complexType name="ServerAddressConfDataType">\n  <xs:sequence>\n   <xs:element name="EncodingMask" type="xs:unsignedInt" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="BrowseName" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Address" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="AddressSelection" type="ua:ListOfString" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="AddressModify" type="xs:boolean" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="SecurityMode" type="ua:MessageSecurityMode" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="SecurityModeSelection" type="ua:ListOfMessageSecurityMode" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="SecurityModeModify" type="xs:boolean" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="SecurityPolicyUri" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="SecurityPolicyUriSelection" type="ua:ListOfString" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="SecurityPolicyUriModify" type="xs:boolean" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ServerUri" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ServerUriSelection" type="ua:ListOfString" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ServerUriModify" type="xs:boolean" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ServerProperties" type="ua:ListOfKeyValuePair" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Namespaces" type="ua:ListOfString" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ServerAddressConfDataType" type="tns:ServerAddressConfDataType"/>\n <xs:complexType name="ListOfServerAddressConfDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="ServerAddressConfDataType" nillable="true" type="tns:ServerAddressConfDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfServerAddressConfDataType" nillable="true" type="tns:ListOfServerAddressConfDataType"/>\n <xs:complexType name="ServerAddressDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="Address" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="SecurityMode" type="ua:MessageSecurityMode" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="SecurityPolicyUri" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ServerUri" type="xs:string" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ServerAddressDataType" type="tns:ServerAddressDataType"/>\n <xs:complexType name="ListOfServerAddressDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="ServerAddressDataType" nillable="true" type="tns:ServerAddressDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfServerAddressDataType" nillable="true" type="tns:ListOfServerAddressDataType"/>\n <xs:complexType name="SubscriberConfigurationConfDataType">\n  <xs:sequence>\n   <xs:element name="EncodingMask" type="xs:unsignedInt" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="BrowseName" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Address" type="tns:AddressSelectionDataType" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="MessageReceiveTimeout" type="xs:double" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="MessageReceiveTimeoutSelection" type="ua:ListOfDouble" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="MessageReceiveTimeoutModify" type="xs:boolean" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ReceiveQos" type="tns:ReceiveQosSelectionDataType" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="SubscriberProperties" type="ua:ListOfKeyValuePair" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="SubscriberConfigurationConfDataType" type="tns:SubscriberConfigurationConfDataType"/>\n <xs:complexType name="ListOfSubscriberConfigurationConfDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="SubscriberConfigurationConfDataType" nillable="true" type="tns:SubscriberConfigurationConfDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfSubscriberConfigurationConfDataType" nillable="true" type="tns:ListOfSubscriberConfigurationConfDataType"/>\n <xs:complexType name="NodeIdentifier">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="SwitchField" type="xs:unsignedInt" minOccurs="0"/>\n   <xs:choice>\n    <xs:element maxOccurs="1" name="Node" type="ua:NodeId" minOccurs="0"/>\n    <xs:element maxOccurs="1" name="Alias" type="xs:string" minOccurs="0"/>\n    <xs:element maxOccurs="1" name="IdentifierBrowsePath" type="ua:RelativePath" minOccurs="0"/>\n   </xs:choice>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="NodeIdentifier" type="tns:NodeIdentifier"/>\n <xs:complexType name="ListOfNodeIdentifier">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="NodeIdentifier" nillable="true" type="tns:NodeIdentifier" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfNodeIdentifier" nillable="true" type="tns:ListOfNodeIdentifier"/>\n <xs:complexType name="PortableNodeIdentifier">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="SwitchField" type="xs:unsignedInt" minOccurs="0"/>\n   <xs:choice>\n    <xs:element maxOccurs="1" name="Node" type="ua:PortableNodeId" minOccurs="0"/>\n    <xs:element maxOccurs="1" name="Alias" type="xs:string" minOccurs="0"/>\n    <xs:element maxOccurs="1" name="IdentifierBrowsePath" type="tns:PortableRelativePath" minOccurs="0"/>\n   </xs:choice>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="PortableNodeIdentifier" type="tns:PortableNodeIdentifier"/>\n <xs:complexType name="ListOfPortableNodeIdentifier">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="PortableNodeIdentifier" nillable="true" type="tns:PortableNodeIdentifier" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPortableNodeIdentifier" nillable="true" type="tns:ListOfPortableNodeIdentifier"/>\n</xs:schema>\n',
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=16031",
    browseName="OptionSetValues",
    parent="ns=fx_cm;i=13054",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("ElementAdd"), o6.LocalizedText("ElementRemove"), o6.LocalizedText("ElementReplace")],
)


del Any, TYPE_CHECKING, uuid, o6, di, fx_data, ns0, fx_cm_reftypes, fx_cm_datypes, fx_cm_vartypes, fx_cm_objtypes
