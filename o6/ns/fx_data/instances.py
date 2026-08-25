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

"""Generated OPC UA fx_data namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import datatypes as fx_data_datypes
from . import objtypes as fx_data_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

fxRoot = ns0.objtypes.FolderType(nodeId="ns=fx_data;i=71", browseName="ns=fx_data;FxRoot", parent="i=85", referenceType=ns0.reftypes.Organizes)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashFXSlashDataSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=fx_data;i=81",
    browseName="ns=fx_data;http://opcfoundation.org/UA/FX/Data/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=fx_data;i=177", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fx_data;i=178", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2026-07-22T18:52:04Z"))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_data;i=179", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/FX/Data/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_data;i=180", browseName="NamespaceVersion", dataType=o6.String, value="1.00.04")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fx_data;i=181", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fx_data;i=182", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["0:15000"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_data;i=183", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1093", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1094", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.NodeIdValuePair, o6.ns["ns=fx_data;i=1094"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1095", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.NodeIdValuePair, o6.ns["ns=fx_data;i=1095"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1102", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1103", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.PubSubCommunicationLinkConfigurationDataType, o6.ns["ns=fx_data;i=1103"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1104", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.PubSubCommunicationLinkConfigurationDataType, o6.ns["ns=fx_data;i=1104"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1108", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1109", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.CommunicationConfigurationResultDataType, o6.ns["ns=fx_data;i=1109"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1110", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.CommunicationConfigurationResultDataType, o6.ns["ns=fx_data;i=1110"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1111", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1112", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.NodeIdArray, o6.ns["ns=fx_data;i=1112"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1113", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.NodeIdArray, o6.ns["ns=fx_data;i=1113"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1141", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1142", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.ConnectionEndpointConfigurationDataType, o6.ns["ns=fx_data;i=1142"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1143", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.ConnectionEndpointConfigurationDataType, o6.ns["ns=fx_data;i=1143"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1144", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1145", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.PubSubCommunicationConfigurationDataType, o6.ns["ns=fx_data;i=1145"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1146", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.PubSubCommunicationConfigurationDataType, o6.ns["ns=fx_data;i=1146"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1147", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1148", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.CommunicationConfigurationDataType, o6.ns["ns=fx_data;i=1148"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1149", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.CommunicationConfigurationDataType, o6.ns["ns=fx_data;i=1149"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1153", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1154", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.AssetVerificationDataType, o6.ns["ns=fx_data;i=1154"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1155", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.AssetVerificationDataType, o6.ns["ns=fx_data;i=1155"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1205", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1206", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.AssetVerificationResultDataType, o6.ns["ns=fx_data;i=1206"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1207", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.AssetVerificationResultDataType, o6.ns["ns=fx_data;i=1207"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1208", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1209", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.PubSubCommunicationConfigurationResultDataType, o6.ns["ns=fx_data;i=1209"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=1210", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.PubSubCommunicationConfigurationResultDataType, o6.ns["ns=fx_data;i=1210"])
ns0.vartypes.PropertyType(
    nodeId="ns=fx_data;i=1225",
    browseName="OptionSetValues",
    parent="ns=fx_data;i=1024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[9],
    value=[
        o6.LocalizedText("VerifyAssetCmd"),
        o6.LocalizedText("VerifyFunctionalEntityCmd"),
        o6.LocalizedText("CreateConnectionEndpointCmd"),
        o6.LocalizedText("EstablishControlCmd"),
        o6.LocalizedText("SetConfigurationDataCmd"),
        o6.LocalizedText("ReassignControlCmd"),
        o6.LocalizedText("ReserveCommunicationIdsCmd"),
        o6.LocalizedText("SetCommunicationConfigurationCmd"),
        o6.LocalizedText("EnableCommunicationCmd"),
    ],
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5001", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5002", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.RelatedEndpointDataType, o6.ns["ns=fx_data;i=5002"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5003", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.RelatedEndpointDataType, o6.ns["ns=fx_data;i=5003"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5004", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5005", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.PubSubReserveCommunicationIds2DataType, o6.ns["ns=fx_data;i=5005"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5006", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.PubSubReserveCommunicationIds2DataType, o6.ns["ns=fx_data;i=5006"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5007", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5008", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.PubSubReserveCommunicationIdsResult2DataType, o6.ns["ns=fx_data;i=5008"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5009", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.PubSubReserveCommunicationIdsResult2DataType, o6.ns["ns=fx_data;i=5009"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5010", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5020", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.IntervalRange, o6.ns["ns=fx_data;i=5020"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5022", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.IntervalRange, o6.ns["ns=fx_data;i=5022"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5033", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5034", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.CommunicationLinkConfigurationDataType, o6.ns["ns=fx_data;i=5034"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5035", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.CommunicationLinkConfigurationDataType, o6.ns["ns=fx_data;i=5035"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5036", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5037", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.ConnectionEndpointConfigurationResultDataType, o6.ns["ns=fx_data;i=5037"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5038", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.ConnectionEndpointConfigurationResultDataType, o6.ns["ns=fx_data;i=5038"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5039", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5040", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.ConnectionEndpointParameterDataType, o6.ns["ns=fx_data;i=5040"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5041", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.ConnectionEndpointParameterDataType, o6.ns["ns=fx_data;i=5041"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5054", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5055", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.ConnectionEndpointDefinitionDataType, o6.ns["ns=fx_data;i=5055"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5056", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.ConnectionEndpointDefinitionDataType, o6.ns["ns=fx_data;i=5056"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5060", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5061", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.PubSubConnectionEndpointParameterDataType, o6.ns["ns=fx_data;i=5061"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5062", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.PubSubConnectionEndpointParameterDataType, o6.ns["ns=fx_data;i=5062"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5064", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5065", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.ReserveCommunicationIdsDataType, o6.ns["ns=fx_data;i=5065"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5081", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.ReserveCommunicationIdsDataType, o6.ns["ns=fx_data;i=5081"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5082", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5083", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.PubSubReserveCommunicationIdsDataType, o6.ns["ns=fx_data;i=5083"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5084", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.PubSubReserveCommunicationIdsDataType, o6.ns["ns=fx_data;i=5084"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5085", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5086", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.ReserveCommunicationIdsResultDataType, o6.ns["ns=fx_data;i=5086"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5087", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.ReserveCommunicationIdsResultDataType, o6.ns["ns=fx_data;i=5087"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5088", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5089", browseName="Default XML")
o6.hasEncoding(fx_data_datypes.PubSubReserveCommunicationIdsResultDataType, o6.ns["ns=fx_data;i=5089"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_data;i=5090", browseName="Default JSON")
o6.hasEncoding(fx_data_datypes.PubSubReserveCommunicationIdsResultDataType, o6.ns["ns=fx_data;i=5090"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6003", browseName="ns=fx_data;PubSubReserveCommunicationIds2DataType", dataType=o6.String, value="PubSubReserveCommunicationIds2DataType"
)
o6.reference(o6.ns["ns=fx_data;i=5004"], "i=39", o6.ns["ns=fx_data;i=6003"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6004",
    browseName="ns=fx_data;PubSubReserveCommunicationIds2DataType",
    dataType=o6.String,
    value="//xs:element[@name='PubSubReserveCommunicationIds2DataType']",
)
o6.reference(o6.ns["ns=fx_data;i=5005"], "i=39", o6.ns["ns=fx_data;i=6004"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6005", browseName="ns=fx_data;PubSubReserveCommunicationIdsResult2DataType", dataType=o6.String, value="PubSubReserveCommunicationIdsResult2DataType"
)
o6.reference(o6.ns["ns=fx_data;i=5007"], "i=39", o6.ns["ns=fx_data;i=6005"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6006",
    browseName="ns=fx_data;PubSubReserveCommunicationIdsResult2DataType",
    dataType=o6.String,
    value="//xs:element[@name='PubSubReserveCommunicationIdsResult2DataType']",
)
o6.reference(o6.ns["ns=fx_data;i=5008"], "i=39", o6.ns["ns=fx_data;i=6006"])
ns0.vartypes.PropertyType(
    nodeId="ns=fx_data;i=6007",
    browseName="EnumStrings",
    parent="ns=fx_data;i=3012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("Nanosecond"), o6.LocalizedText("Microsecond"), o6.LocalizedText("Millisecond"), o6.LocalizedText("Second")],
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6008", browseName="ns=fx_data;ConnectionEndpointDefinitionDataType", dataType=o6.String, value="ConnectionEndpointDefinitionDataType"
)
o6.reference(o6.ns["ns=fx_data;i=5054"], "i=39", o6.ns["ns=fx_data;i=6008"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6009", browseName="ns=fx_data;ConnectionEndpointDefinitionDataType", dataType=o6.String, value="//xs:element[@name='ConnectionEndpointDefinitionDataType']"
)
o6.reference(o6.ns["ns=fx_data;i=5055"], "i=39", o6.ns["ns=fx_data;i=6009"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_data;i=6010", browseName="ns=fx_data;IntervalRange", dataType=o6.String, value="IntervalRange")
o6.reference(o6.ns["ns=fx_data;i=5010"], "i=39", o6.ns["ns=fx_data;i=6010"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_data;i=6013", browseName="ns=fx_data;IntervalRange", dataType=o6.String, value="//xs:element[@name='IntervalRange']")
o6.reference(o6.ns["ns=fx_data;i=5020"], "i=39", o6.ns["ns=fx_data;i=6013"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_data;i=6028", browseName="ns=fx_data;AssetVerificationDataType", dataType=o6.String, value="AssetVerificationDataType")
o6.reference(o6.ns["ns=fx_data;i=1153"], "i=39", o6.ns["ns=fx_data;i=6028"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6029", browseName="ns=fx_data;AssetVerificationDataType", dataType=o6.String, value="//xs:element[@name='AssetVerificationDataType']"
)
o6.reference(o6.ns["ns=fx_data;i=1154"], "i=39", o6.ns["ns=fx_data;i=6029"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6161", browseName="ns=fx_data;AssetVerificationResultDataType", dataType=o6.String, value="AssetVerificationResultDataType"
)
o6.reference(o6.ns["ns=fx_data;i=1205"], "i=39", o6.ns["ns=fx_data;i=6161"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6162", browseName="ns=fx_data;AssetVerificationResultDataType", dataType=o6.String, value="//xs:element[@name='AssetVerificationResultDataType']"
)
o6.reference(o6.ns["ns=fx_data;i=1206"], "i=39", o6.ns["ns=fx_data;i=6162"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6163", browseName="ns=fx_data;CommunicationConfigurationDataType", dataType=o6.String, value="CommunicationConfigurationDataType"
)
o6.reference(o6.ns["ns=fx_data;i=1147"], "i=39", o6.ns["ns=fx_data;i=6163"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6164", browseName="ns=fx_data;CommunicationConfigurationDataType", dataType=o6.String, value="//xs:element[@name='CommunicationConfigurationDataType']"
)
o6.reference(o6.ns["ns=fx_data;i=1148"], "i=39", o6.ns["ns=fx_data;i=6164"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6165", browseName="ns=fx_data;PubSubCommunicationConfigurationDataType", dataType=o6.String, value="PubSubCommunicationConfigurationDataType"
)
o6.reference(o6.ns["ns=fx_data;i=1144"], "i=39", o6.ns["ns=fx_data;i=6165"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6166",
    browseName="ns=fx_data;PubSubCommunicationConfigurationDataType",
    dataType=o6.String,
    value="//xs:element[@name='PubSubCommunicationConfigurationDataType']",
)
o6.reference(o6.ns["ns=fx_data;i=1145"], "i=39", o6.ns["ns=fx_data;i=6166"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6167", browseName="ns=fx_data;CommunicationConfigurationResultDataType", dataType=o6.String, value="CommunicationConfigurationResultDataType"
)
o6.reference(o6.ns["ns=fx_data;i=1108"], "i=39", o6.ns["ns=fx_data;i=6167"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6168",
    browseName="ns=fx_data;CommunicationConfigurationResultDataType",
    dataType=o6.String,
    value="//xs:element[@name='CommunicationConfigurationResultDataType']",
)
o6.reference(o6.ns["ns=fx_data;i=1109"], "i=39", o6.ns["ns=fx_data;i=6168"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6171", browseName="ns=fx_data;PubSubCommunicationConfigurationResultDataType", dataType=o6.String, value="PubSubCommunicationConfigurationResultDataType"
)
o6.reference(o6.ns["ns=fx_data;i=1208"], "i=39", o6.ns["ns=fx_data;i=6171"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6172",
    browseName="ns=fx_data;PubSubCommunicationConfigurationResultDataType",
    dataType=o6.String,
    value="//xs:element[@name='PubSubCommunicationConfigurationResultDataType']",
)
o6.reference(o6.ns["ns=fx_data;i=1209"], "i=39", o6.ns["ns=fx_data;i=6172"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6173", browseName="ns=fx_data;CommunicationLinkConfigurationDataType", dataType=o6.String, value="CommunicationLinkConfigurationDataType"
)
o6.reference(o6.ns["ns=fx_data;i=5033"], "i=39", o6.ns["ns=fx_data;i=6173"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6174",
    browseName="ns=fx_data;CommunicationLinkConfigurationDataType",
    dataType=o6.String,
    value="//xs:element[@name='CommunicationLinkConfigurationDataType']",
)
o6.reference(o6.ns["ns=fx_data;i=5034"], "i=39", o6.ns["ns=fx_data;i=6174"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6177", browseName="ns=fx_data;PubSubCommunicationLinkConfigurationDataType", dataType=o6.String, value="PubSubCommunicationLinkConfigurationDataType"
)
o6.reference(o6.ns["ns=fx_data;i=1102"], "i=39", o6.ns["ns=fx_data;i=6177"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6178",
    browseName="ns=fx_data;PubSubCommunicationLinkConfigurationDataType",
    dataType=o6.String,
    value="//xs:element[@name='PubSubCommunicationLinkConfigurationDataType']",
)
o6.reference(o6.ns["ns=fx_data;i=1103"], "i=39", o6.ns["ns=fx_data;i=6178"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6179", browseName="ns=fx_data;ConnectionEndpointConfigurationDataType", dataType=o6.String, value="ConnectionEndpointConfigurationDataType"
)
o6.reference(o6.ns["ns=fx_data;i=1141"], "i=39", o6.ns["ns=fx_data;i=6179"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6180",
    browseName="ns=fx_data;ConnectionEndpointConfigurationDataType",
    dataType=o6.String,
    value="//xs:element[@name='ConnectionEndpointConfigurationDataType']",
)
o6.reference(o6.ns["ns=fx_data;i=1142"], "i=39", o6.ns["ns=fx_data;i=6180"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6181", browseName="ns=fx_data;ConnectionEndpointConfigurationResultDataType", dataType=o6.String, value="ConnectionEndpointConfigurationResultDataType"
)
o6.reference(o6.ns["ns=fx_data;i=5036"], "i=39", o6.ns["ns=fx_data;i=6181"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6182",
    browseName="ns=fx_data;ConnectionEndpointConfigurationResultDataType",
    dataType=o6.String,
    value="//xs:element[@name='ConnectionEndpointConfigurationResultDataType']",
)
o6.reference(o6.ns["ns=fx_data;i=5037"], "i=39", o6.ns["ns=fx_data;i=6182"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6185", browseName="ns=fx_data;ConnectionEndpointParameterDataType", dataType=o6.String, value="ConnectionEndpointParameterDataType"
)
o6.reference(o6.ns["ns=fx_data;i=5039"], "i=39", o6.ns["ns=fx_data;i=6185"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6186", browseName="ns=fx_data;ConnectionEndpointParameterDataType", dataType=o6.String, value="//xs:element[@name='ConnectionEndpointParameterDataType']"
)
o6.reference(o6.ns["ns=fx_data;i=5040"], "i=39", o6.ns["ns=fx_data;i=6186"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_data;i=6193", browseName="ns=fx_data;NodeIdArray", dataType=o6.String, value="NodeIdArray")
o6.reference(o6.ns["ns=fx_data;i=1111"], "i=39", o6.ns["ns=fx_data;i=6193"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_data;i=6194", browseName="ns=fx_data;NodeIdArray", dataType=o6.String, value="//xs:element[@name='NodeIdArray']")
o6.reference(o6.ns["ns=fx_data;i=1112"], "i=39", o6.ns["ns=fx_data;i=6194"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_data;i=6195", browseName="ns=fx_data;NodeIdValuePair", dataType=o6.String, value="NodeIdValuePair")
o6.reference(o6.ns["ns=fx_data;i=1093"], "i=39", o6.ns["ns=fx_data;i=6195"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_data;i=6196", browseName="ns=fx_data;NodeIdValuePair", dataType=o6.String, value="//xs:element[@name='NodeIdValuePair']")
o6.reference(o6.ns["ns=fx_data;i=1094"], "i=39", o6.ns["ns=fx_data;i=6196"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_data;i=6217", browseName="ns=fx_data;RelatedEndpointDataType", dataType=o6.String, value="RelatedEndpointDataType")
o6.reference(o6.ns["ns=fx_data;i=5001"], "i=39", o6.ns["ns=fx_data;i=6217"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6218", browseName="ns=fx_data;RelatedEndpointDataType", dataType=o6.String, value="//xs:element[@name='RelatedEndpointDataType']"
)
o6.reference(o6.ns["ns=fx_data;i=5002"], "i=39", o6.ns["ns=fx_data;i=6218"])
ns0.vartypes.PropertyType(
    nodeId="ns=fx_data;i=6240",
    browseName="EnumValues",
    parent="ns=fx_data;i=31",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("PublisherSubscriber"), description=o6.LocalizedText("reference to DataSetReader and DataSetWriter required.")
        ),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Publisher"), description=o6.LocalizedText("reference to DataSetWriter is required.")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Subscriber"), description=o6.LocalizedText("reference to DataSetReader is required.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_data;i=6326",
    browseName="EnumValues",
    parent="ns=fx_data;i=1037",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("NotSet"), description=o6.LocalizedText("The verification result is not set.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Match"), description=o6.LocalizedText("Asset matches expectation.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Compatible"), description=o6.LocalizedText("Asset does not match expectation but is compatible.")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Mismatch"), description=o6.LocalizedText("Asset does not match expectation and is not compatible.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_data;i=6327",
    browseName="EnumValues",
    parent="ns=fx_data;i=1029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("AssetCompatibility"),
            description=o6.LocalizedText("Verify whether an Asset&#8217;s functionality matches or is compatible to the expectation of system engineering."),
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("AssetIdentity"),
            description=o6.LocalizedText("Verify whether an Asset&#8217;s identity meets the expectation of system engineering."),
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("AssetIdentityAndCompatibility"),
            description=o6.LocalizedText(
                "Verify whether an Asset&#8217;s identity meets the expectation of system engineering and whether its functionality matches or is compatible to the expectation of system engineering."
            ),
        ),
    ],
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6329", browseName="ns=fx_data;PubSubConnectionEndpointParameterDataType", dataType=o6.String, value="PubSubConnectionEndpointParameterDataType"
)
o6.reference(o6.ns["ns=fx_data;i=5060"], "i=39", o6.ns["ns=fx_data;i=6329"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6330",
    browseName="ns=fx_data;PubSubConnectionEndpointParameterDataType",
    dataType=o6.String,
    value="//xs:element[@name='PubSubConnectionEndpointParameterDataType']",
)
o6.reference(o6.ns["ns=fx_data;i=5061"], "i=39", o6.ns["ns=fx_data;i=6330"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6411", browseName="ns=fx_data;ReserveCommunicationIdsDataType", dataType=o6.String, value="ReserveCommunicationIdsDataType"
)
o6.reference(o6.ns["ns=fx_data;i=5064"], "i=39", o6.ns["ns=fx_data;i=6411"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6412", browseName="ns=fx_data;ReserveCommunicationIdsDataType", dataType=o6.String, value="//xs:element[@name='ReserveCommunicationIdsDataType']"
)
o6.reference(o6.ns["ns=fx_data;i=5065"], "i=39", o6.ns["ns=fx_data;i=6412"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6413", browseName="ns=fx_data;PubSubReserveCommunicationIdsDataType", dataType=o6.String, value="PubSubReserveCommunicationIdsDataType"
)
o6.reference(o6.ns["ns=fx_data;i=5082"], "i=39", o6.ns["ns=fx_data;i=6413"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6414",
    browseName="ns=fx_data;PubSubReserveCommunicationIdsDataType",
    dataType=o6.String,
    value="//xs:element[@name='PubSubReserveCommunicationIdsDataType']",
)
o6.reference(o6.ns["ns=fx_data;i=5083"], "i=39", o6.ns["ns=fx_data;i=6414"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6415", browseName="ns=fx_data;ReserveCommunicationIdsResultDataType", dataType=o6.String, value="ReserveCommunicationIdsResultDataType"
)
o6.reference(o6.ns["ns=fx_data;i=5085"], "i=39", o6.ns["ns=fx_data;i=6415"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6416",
    browseName="ns=fx_data;ReserveCommunicationIdsResultDataType",
    dataType=o6.String,
    value="//xs:element[@name='ReserveCommunicationIdsResultDataType']",
)
o6.reference(o6.ns["ns=fx_data;i=5086"], "i=39", o6.ns["ns=fx_data;i=6416"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6417", browseName="ns=fx_data;PubSubReserveCommunicationIdsResultDataType", dataType=o6.String, value="PubSubReserveCommunicationIdsResultDataType"
)
o6.reference(o6.ns["ns=fx_data;i=5088"], "i=39", o6.ns["ns=fx_data;i=6417"])
opcDotUaDotFx = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=fx_data;i=6022",
    browseName="ns=fx_data;Opc.Ua.Fx",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/FX/Data/",
    displayName="Opc.Ua.FX",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=fx_data;i=6011",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_data;i=6023", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/FX/Data/")),
        o6.hasComponent(o6.ns["ns=fx_data;i=6003"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6005"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6008"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6010"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6028"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6161"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6163"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6165"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6167"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6171"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6173"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6177"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6179"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6181"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6185"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6193"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6195"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6217"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6329"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6411"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6413"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6415"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6417"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:tns="http://opcfoundation.org/UA/FX/Data/" xmlns:opc="http://opcfoundation.org/BinarySchema/" TargetNamespace="http://opcfoundation.org/UA/FX/Data/" xmlns:ua="http://opcfoundation.org/UA/" DefaultByteOrder="LittleEndian" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="AssetVerificationDataType">\n  <opc:Field TypeName="ua:NodeId" Name="AssetToVerify"/>\n  <opc:Field TypeName="tns:AssetVerificationModeEnum" Name="VerificationMode"/>\n  <opc:Field TypeName="tns:AssetVerificationResultEnum" Name="ExpectedVerificationResult"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfExpectedVerificationVariables"/>\n  <opc:Field TypeName="ua:KeyValuePair" Name="ExpectedVerificationVariables" LengthField="NoOfExpectedVerificationVariables"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfExpectedAdditionalVerificationVariables"/>\n  <opc:Field TypeName="tns:NodeIdValuePair" Name="ExpectedAdditionalVerificationVariables" LengthField="NoOfExpectedAdditionalVerificationVariables"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="AssetVerificationResultDataType">\n  <opc:Field TypeName="ua:StatusCode" Name="VerificationStatus"/>\n  <opc:Field TypeName="tns:AssetVerificationResultEnum" Name="VerificationResult"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfVerificationVariablesErrors"/>\n  <opc:Field TypeName="ua:StatusCode" Name="VerificationVariablesErrors" LengthField="NoOfVerificationVariablesErrors"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfVerificationAdditionalVariablesErrors"/>\n  <opc:Field TypeName="ua:StatusCode" Name="VerificationAdditionalVariablesErrors" LengthField="NoOfVerificationAdditionalVariablesErrors"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="CommunicationConfigurationDataType"/>\n <opc:StructuredType BaseType="tns:CommunicationConfigurationDataType" Name="PubSubCommunicationConfigurationDataType">\n  <opc:Field TypeName="ua:PubSubConfiguration2DataType" Name="PubSubConfiguration"/>\n  <opc:Field TypeName="opc:Boolean" Name="RequireCompleteUpdate"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfConfigurationReferences"/>\n  <opc:Field TypeName="ua:PubSubConfigurationRefDataType" Name="ConfigurationReferences" LengthField="NoOfConfigurationReferences"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="CommunicationConfigurationResultDataType"/>\n <opc:StructuredType BaseType="tns:CommunicationConfigurationResultDataType" Name="PubSubCommunicationConfigurationResultDataType">\n  <opc:Field TypeName="ua:StatusCode" Name="Result"/>\n  <opc:Field TypeName="opc:Boolean" Name="ChangesApplied"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfReferenceResults"/>\n  <opc:Field TypeName="ua:StatusCode" Name="ReferenceResults" LengthField="NoOfReferenceResults"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfConfigurationValues"/>\n  <opc:Field TypeName="ua:PubSubConfigurationValueDataType" Name="ConfigurationValues" LengthField="NoOfConfigurationValues"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfConfigurationObjects"/>\n  <opc:Field TypeName="ua:NodeId" Name="ConfigurationObjects" LengthField="NoOfConfigurationObjects"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="CommunicationLinkConfigurationDataType"/>\n <opc:StructuredType BaseType="tns:CommunicationLinkConfigurationDataType" Name="PubSubCommunicationLinkConfigurationDataType">\n  <opc:Field TypeName="ua:PubSubConfigurationRefDataType" Name="DataSetReaderRef"/>\n  <opc:Field TypeName="ua:ConfigurationVersionDataType" Name="ExpectedSubscribedDataSetVersion"/>\n  <opc:Field TypeName="ua:PubSubConfigurationRefDataType" Name="DataSetWriterRef"/>\n  <opc:Field TypeName="ua:ConfigurationVersionDataType" Name="ExpectedPublishedDataSetVersion"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ConnectionEndpointConfigurationDataType">\n  <opc:Field TypeName="ua:NodeId" Name="FunctionalEntityNode"/>\n  <opc:Field TypeName="tns:ConnectionEndpointDefinitionDataType" Name="ConnectionEndpoint"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfExpectedVerificationVariables"/>\n  <opc:Field TypeName="tns:NodeIdValuePair" Name="ExpectedVerificationVariables" LengthField="NoOfExpectedVerificationVariables"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfControlGroups"/>\n  <opc:Field TypeName="ua:NodeId" Name="ControlGroups" LengthField="NoOfControlGroups"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfConfigurationData"/>\n  <opc:Field TypeName="tns:NodeIdValuePair" Name="ConfigurationData" LengthField="NoOfConfigurationData"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="CommunicationLinks"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ConnectionEndpointConfigurationResultDataType">\n  <opc:Field TypeName="ua:NodeId" Name="ConnectionEndpointId"/>\n  <opc:Field TypeName="ua:StatusCode" Name="FunctionalEntityNodeResult"/>\n  <opc:Field TypeName="ua:StatusCode" Name="ConnectionEndpointResult"/>\n  <opc:Field TypeName="tns:FunctionalEntityVerificationResultEnum" Name="VerificationResult"/>\n  <opc:Field TypeName="ua:StatusCode" Name="VerificationStatus"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfVerificationVariablesErrors"/>\n  <opc:Field TypeName="ua:StatusCode" Name="VerificationVariablesErrors" LengthField="NoOfVerificationVariablesErrors"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfEstablishControlResult"/>\n  <opc:Field TypeName="ua:StatusCode" Name="EstablishControlResult" LengthField="NoOfEstablishControlResult"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfConfigurationDataResult"/>\n  <opc:Field TypeName="ua:StatusCode" Name="ConfigurationDataResult" LengthField="NoOfConfigurationDataResult"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfReassignControlResult"/>\n  <opc:Field TypeName="ua:StatusCode" Name="ReassignControlResult" LengthField="NoOfReassignControlResult"/>\n  <opc:Field TypeName="ua:StatusCode" Name="CommunicationLinksResult"/>\n  <opc:Field TypeName="ua:StatusCode" Name="EnableCommunicationResult"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ConnectionEndpointParameterDataType">\n  <opc:Field TypeName="opc:CharArray" Name="Name"/>\n  <opc:Field TypeName="ua:NodeId" Name="ConnectionEndpointTypeId"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfInputVariableIds"/>\n  <opc:Field TypeName="ua:NodeId" Name="InputVariableIds" LengthField="NoOfInputVariableIds"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfOutputVariableIds"/>\n  <opc:Field TypeName="ua:NodeId" Name="OutputVariableIds" LengthField="NoOfOutputVariableIds"/>\n  <opc:Field TypeName="opc:Boolean" Name="IsPersistent"/>\n  <opc:Field TypeName="opc:Double" Name="CleanupTimeout"/>\n  <opc:Field TypeName="tns:RelatedEndpointDataType" Name="RelatedEndpoint"/>\n  <opc:Field TypeName="opc:Boolean" Name="IsPreconfigured"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ConnectionEndpointParameterDataType" Name="PubSubConnectionEndpointParameterDataType">\n  <opc:Field SourceType="tns:ConnectionEndpointParameterDataType" TypeName="opc:CharArray" Name="Name"/>\n  <opc:Field SourceType="tns:ConnectionEndpointParameterDataType" TypeName="ua:NodeId" Name="ConnectionEndpointTypeId"/>\n  <opc:Field SourceType="tns:ConnectionEndpointParameterDataType" TypeName="opc:Int32" Name="NoOfInputVariableIds"/>\n  <opc:Field SourceType="tns:ConnectionEndpointParameterDataType" TypeName="ua:NodeId" Name="InputVariableIds" LengthField="NoOfInputVariableIds"/>\n  <opc:Field SourceType="tns:ConnectionEndpointParameterDataType" TypeName="opc:Int32" Name="NoOfOutputVariableIds"/>\n  <opc:Field SourceType="tns:ConnectionEndpointParameterDataType" TypeName="ua:NodeId" Name="OutputVariableIds" LengthField="NoOfOutputVariableIds"/>\n  <opc:Field SourceType="tns:ConnectionEndpointParameterDataType" TypeName="opc:Boolean" Name="IsPersistent"/>\n  <opc:Field SourceType="tns:ConnectionEndpointParameterDataType" TypeName="opc:Double" Name="CleanupTimeout"/>\n  <opc:Field SourceType="tns:ConnectionEndpointParameterDataType" TypeName="tns:RelatedEndpointDataType" Name="RelatedEndpoint"/>\n  <opc:Field SourceType="tns:ConnectionEndpointParameterDataType" TypeName="opc:Boolean" Name="IsPreconfigured"/>\n  <opc:Field TypeName="tns:PubSubConnectionEndpointModeEnum" Name="Mode"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="IntervalRange">\n  <opc:Field TypeName="opc:UInt32" Name="Min"/>\n  <opc:Field TypeName="opc:UInt32" Name="Max"/>\n  <opc:Field TypeName="opc:UInt16" Name="Increment"/>\n  <opc:Field TypeName="opc:UInt16" Name="Multiplier"/>\n  <opc:Field TypeName="tns:FxTimeUnitsEnum" Name="Unit"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="NodeIdArray">\n  <opc:Field TypeName="ua:NodeId" Name="Node"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfArrayIndex"/>\n  <opc:Field TypeName="opc:UInt32" Name="ArrayIndex" LengthField="NoOfArrayIndex"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="NodeIdValuePair">\n  <opc:Field TypeName="tns:NodeIdArray" Name="Key"/>\n  <opc:Field TypeName="ua:Variant" Name="Value"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RelatedEndpointDataType">\n  <opc:Field TypeName="opc:CharArray" Name="Address"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfConnectionEndpointPath"/>\n  <opc:Field TypeName="ua:PortableQualifiedName" Name="ConnectionEndpointPath" LengthField="NoOfConnectionEndpointPath"/>\n  <opc:Field TypeName="opc:CharArray" Name="ConnectionEndpointName"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ReserveCommunicationIdsDataType"/>\n <opc:StructuredType BaseType="tns:ReserveCommunicationIdsDataType" Name="PubSubReserveCommunicationIdsDataType">\n  <opc:Field TypeName="opc:CharArray" Name="TransportProfileUri"/>\n  <opc:Field TypeName="opc:UInt16" Name="NumReqWriterGroupIds"/>\n  <opc:Field TypeName="opc:UInt16" Name="NumReqDataSetWriterIds"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:PubSubReserveCommunicationIdsDataType" Name="PubSubReserveCommunicationIds2DataType">\n  <opc:Field SourceType="tns:PubSubReserveCommunicationIdsDataType" TypeName="opc:CharArray" Name="TransportProfileUri"/>\n  <opc:Field SourceType="tns:PubSubReserveCommunicationIdsDataType" TypeName="opc:UInt16" Name="NumReqWriterGroupIds"/>\n  <opc:Field SourceType="tns:PubSubReserveCommunicationIdsDataType" TypeName="opc:UInt16" Name="NumReqDataSetWriterIds"/>\n  <opc:Field TypeName="opc:Boolean" Name="RequestTransportSpecificInfo"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ReserveCommunicationIdsResultDataType"/>\n <opc:StructuredType BaseType="tns:ReserveCommunicationIdsResultDataType" Name="PubSubReserveCommunicationIdsResultDataType">\n  <opc:Field TypeName="ua:StatusCode" Name="Result"/>\n  <opc:Field TypeName="ua:Variant" Name="DefaultPublisherId"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfWriterGroupIds"/>\n  <opc:Field TypeName="opc:UInt16" Name="WriterGroupIds" LengthField="NoOfWriterGroupIds"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfDataSetWriterIds"/>\n  <opc:Field TypeName="opc:UInt16" Name="DataSetWriterIds" LengthField="NoOfDataSetWriterIds"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:PubSubReserveCommunicationIdsResultDataType" Name="PubSubReserveCommunicationIdsResult2DataType">\n  <opc:Field SourceType="tns:PubSubReserveCommunicationIdsResultDataType" TypeName="ua:StatusCode" Name="Result"/>\n  <opc:Field SourceType="tns:PubSubReserveCommunicationIdsResultDataType" TypeName="ua:Variant" Name="DefaultPublisherId"/>\n  <opc:Field SourceType="tns:PubSubReserveCommunicationIdsResultDataType" TypeName="opc:Int32" Name="NoOfWriterGroupIds"/>\n  <opc:Field SourceType="tns:PubSubReserveCommunicationIdsResultDataType" TypeName="opc:UInt16" Name="WriterGroupIds" LengthField="NoOfWriterGroupIds"/>\n  <opc:Field SourceType="tns:PubSubReserveCommunicationIdsResultDataType" TypeName="opc:Int32" Name="NoOfDataSetWriterIds"/>\n  <opc:Field SourceType="tns:PubSubReserveCommunicationIdsResultDataType" TypeName="opc:UInt16" Name="DataSetWriterIds" LengthField="NoOfDataSetWriterIds"/>\n  <opc:Field TypeName="ua:Variant" Name="TransportSpecificInfo"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:Union" Name="ConnectionEndpointDefinitionDataType">\n  <opc:Field TypeName="opc:UInt32" Name="SwitchField"/>\n  <opc:Field SwitchField="SwitchField" TypeName="ua:ExtensionObject" Name="Parameter" SwitchValue="1"/>\n  <opc:Field SwitchField="SwitchField" TypeName="ua:NodeId" Name="Node" SwitchValue="2"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="AssetVerificationModeEnum">\n  <opc:EnumeratedValue Value="0" Name="AssetCompatibility"/>\n  <opc:EnumeratedValue Value="1" Name="AssetIdentity"/>\n  <opc:EnumeratedValue Value="2" Name="AssetIdentityAndCompatibility"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="AssetVerificationResultEnum">\n  <opc:EnumeratedValue Value="0" Name="NotSet"/>\n  <opc:EnumeratedValue Value="1" Name="Match"/>\n  <opc:EnumeratedValue Value="2" Name="Compatible"/>\n  <opc:EnumeratedValue Value="3" Name="Mismatch"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="FunctionalEntityVerificationResultEnum">\n  <opc:EnumeratedValue Value="0" Name="NotSet"/>\n  <opc:EnumeratedValue Value="1" Name="Match"/>\n  <opc:EnumeratedValue Value="2" Name="Mismatch"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="FxTimeUnitsEnum">\n  <opc:Documentation>This enumeration describes the support units of time</opc:Documentation>\n  <opc:EnumeratedValue Value="0" Name="Nanosecond"/>\n  <opc:EnumeratedValue Value="1" Name="Microsecond"/>\n  <opc:EnumeratedValue Value="2" Name="Millisecond"/>\n  <opc:EnumeratedValue Value="3" Name="Second"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PubSubConnectionEndpointModeEnum">\n  <opc:EnumeratedValue Value="1" Name="PublisherSubscriber"/>\n  <opc:EnumeratedValue Value="2" Name="Publisher"/>\n  <opc:EnumeratedValue Value="3" Name="Subscriber"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="FxCommandMask" IsOptionSet="true">\n  <opc:Documentation>This OptionSet defines flags indicating the commands a ConnectionManager may use in its call to the EstablishConnections Method.</opc:Documentation>\n  <opc:EnumeratedValue Value="0" Name="VerifyAssetCmd"/>\n  <opc:EnumeratedValue Value="1" Name="VerifyFunctionalEntityCmd"/>\n  <opc:EnumeratedValue Value="2" Name="CreateConnectionEndpointCmd"/>\n  <opc:EnumeratedValue Value="3" Name="EstablishControlCmd"/>\n  <opc:EnumeratedValue Value="4" Name="SetConfigurationDataCmd"/>\n  <opc:EnumeratedValue Value="5" Name="ReassignControlCmd"/>\n  <opc:EnumeratedValue Value="6" Name="ReserveCommunicationIdsCmd"/>\n  <opc:EnumeratedValue Value="7" Name="SetCommunicationConfigurationCmd"/>\n  <opc:EnumeratedValue Value="8" Name="EnableCommunicationCmd"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_data;i=6418",
    browseName="ns=fx_data;PubSubReserveCommunicationIdsResultDataType",
    dataType=o6.String,
    value="//xs:element[@name='PubSubReserveCommunicationIdsResultDataType']",
)
o6.reference(o6.ns["ns=fx_data;i=5089"], "i=39", o6.ns["ns=fx_data;i=6418"])
opcDotUaDotFX = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=fx_data;i=6024",
    browseName="ns=fx_data;Opc.Ua.FX",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/FX/Data/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=fx_data;i=6012",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_data;i=6025", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/FX/Data/Types.xsd")),
        o6.hasComponent(o6.ns["ns=fx_data;i=6004"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6006"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6009"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6013"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6029"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6162"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6164"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6166"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6168"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6172"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6174"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6178"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6180"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6182"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6186"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6194"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6196"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6218"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6330"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6412"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6414"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6416"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=6418"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://opcfoundation.org/UA/FX/Data/Types.xsd" elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/FX/Data/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="AssetVerificationModeEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="AssetCompatibility_0"/>\n   <xs:enumeration value="AssetIdentity_1"/>\n   <xs:enumeration value="AssetIdentityAndCompatibility_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="AssetVerificationModeEnum" type="tns:AssetVerificationModeEnum"/>\n <xs:complexType name="ListOfAssetVerificationModeEnum">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="AssetVerificationModeEnum" nillable="true" type="tns:AssetVerificationModeEnum" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfAssetVerificationModeEnum" nillable="true" type="tns:ListOfAssetVerificationModeEnum"/>\n <xs:simpleType name="AssetVerificationResultEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="NotSet_0"/>\n   <xs:enumeration value="Match_1"/>\n   <xs:enumeration value="Compatible_2"/>\n   <xs:enumeration value="Mismatch_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="AssetVerificationResultEnum" type="tns:AssetVerificationResultEnum"/>\n <xs:complexType name="ListOfAssetVerificationResultEnum">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="AssetVerificationResultEnum" nillable="true" type="tns:AssetVerificationResultEnum" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfAssetVerificationResultEnum" nillable="true" type="tns:ListOfAssetVerificationResultEnum"/>\n <xs:simpleType name="FunctionalEntityVerificationResultEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="NotSet_0"/>\n   <xs:enumeration value="Match_1"/>\n   <xs:enumeration value="Mismatch_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="FunctionalEntityVerificationResultEnum" type="tns:FunctionalEntityVerificationResultEnum"/>\n <xs:complexType name="ListOfFunctionalEntityVerificationResultEnum">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="FunctionalEntityVerificationResultEnum" nillable="true" type="tns:FunctionalEntityVerificationResultEnum" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfFunctionalEntityVerificationResultEnum" nillable="true" type="tns:ListOfFunctionalEntityVerificationResultEnum"/>\n <xs:simpleType name="FxTimeUnitsEnum">\n  <xs:annotation>\n   <xs:documentation>This enumeration describes the support units of time</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Nanosecond_0"/>\n   <xs:enumeration value="Microsecond_1"/>\n   <xs:enumeration value="Millisecond_2"/>\n   <xs:enumeration value="Second_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="FxTimeUnitsEnum" type="tns:FxTimeUnitsEnum"/>\n <xs:complexType name="ListOfFxTimeUnitsEnum">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="FxTimeUnitsEnum" nillable="true" type="tns:FxTimeUnitsEnum" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfFxTimeUnitsEnum" nillable="true" type="tns:ListOfFxTimeUnitsEnum"/>\n <xs:simpleType name="PubSubConnectionEndpointModeEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="PublisherSubscriber_1"/>\n   <xs:enumeration value="Publisher_2"/>\n   <xs:enumeration value="Subscriber_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="PubSubConnectionEndpointModeEnum" type="tns:PubSubConnectionEndpointModeEnum"/>\n <xs:complexType name="ListOfPubSubConnectionEndpointModeEnum">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="PubSubConnectionEndpointModeEnum" nillable="true" type="tns:PubSubConnectionEndpointModeEnum" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPubSubConnectionEndpointModeEnum" nillable="true" type="tns:ListOfPubSubConnectionEndpointModeEnum"/>\n <xs:complexType name="AssetVerificationDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="AssetToVerify" type="ua:NodeId" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="VerificationMode" type="tns:AssetVerificationModeEnum" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ExpectedVerificationResult" type="tns:AssetVerificationResultEnum" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ExpectedVerificationVariables" type="ua:ListOfKeyValuePair" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ExpectedAdditionalVerificationVariables" type="tns:ListOfNodeIdValuePair" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="AssetVerificationDataType" type="tns:AssetVerificationDataType"/>\n <xs:complexType name="ListOfAssetVerificationDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="AssetVerificationDataType" nillable="true" type="tns:AssetVerificationDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfAssetVerificationDataType" nillable="true" type="tns:ListOfAssetVerificationDataType"/>\n <xs:complexType name="AssetVerificationResultDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="VerificationStatus" type="ua:StatusCode" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="VerificationResult" type="tns:AssetVerificationResultEnum" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="VerificationVariablesErrors" type="ua:ListOfStatusCode" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="VerificationAdditionalVariablesErrors" type="ua:ListOfStatusCode" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="AssetVerificationResultDataType" type="tns:AssetVerificationResultDataType"/>\n <xs:complexType name="ListOfAssetVerificationResultDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="AssetVerificationResultDataType" nillable="true" type="tns:AssetVerificationResultDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfAssetVerificationResultDataType" nillable="true" type="tns:ListOfAssetVerificationResultDataType"/>\n <xs:complexType name="CommunicationConfigurationDataType">\n  <xs:sequence/>\n </xs:complexType>\n <xs:element name="CommunicationConfigurationDataType" type="tns:CommunicationConfigurationDataType"/>\n <xs:complexType name="ListOfCommunicationConfigurationDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="CommunicationConfigurationDataType" nillable="true" type="tns:CommunicationConfigurationDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfCommunicationConfigurationDataType" nillable="true" type="tns:ListOfCommunicationConfigurationDataType"/>\n <xs:complexType name="PubSubCommunicationConfigurationDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element maxOccurs="1" name="PubSubConfiguration" type="ua:PubSubConfiguration2DataType" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="RequireCompleteUpdate" type="xs:boolean" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="ConfigurationReferences" type="ua:ListOfPubSubConfigurationRefDataType" minOccurs="0"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element name="PubSubCommunicationConfigurationDataType" type="tns:PubSubCommunicationConfigurationDataType"/>\n <xs:complexType name="ListOfPubSubCommunicationConfigurationDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="PubSubCommunicationConfigurationDataType" nillable="true" type="tns:PubSubCommunicationConfigurationDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPubSubCommunicationConfigurationDataType" nillable="true" type="tns:ListOfPubSubCommunicationConfigurationDataType"/>\n <xs:complexType name="CommunicationConfigurationResultDataType">\n  <xs:sequence/>\n </xs:complexType>\n <xs:element name="CommunicationConfigurationResultDataType" type="tns:CommunicationConfigurationResultDataType"/>\n <xs:complexType name="ListOfCommunicationConfigurationResultDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="CommunicationConfigurationResultDataType" nillable="true" type="tns:CommunicationConfigurationResultDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfCommunicationConfigurationResultDataType" nillable="true" type="tns:ListOfCommunicationConfigurationResultDataType"/>\n <xs:complexType name="PubSubCommunicationConfigurationResultDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element maxOccurs="1" name="Result" type="ua:StatusCode" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="ChangesApplied" type="xs:boolean" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="ReferenceResults" type="ua:ListOfStatusCode" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="ConfigurationValues" type="ua:ListOfPubSubConfigurationValueDataType" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="ConfigurationObjects" type="ua:ListOfNodeId" minOccurs="0"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element name="PubSubCommunicationConfigurationResultDataType" type="tns:PubSubCommunicationConfigurationResultDataType"/>\n <xs:complexType name="ListOfPubSubCommunicationConfigurationResultDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="PubSubCommunicationConfigurationResultDataType" nillable="true" type="tns:PubSubCommunicationConfigurationResultDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPubSubCommunicationConfigurationResultDataType" nillable="true" type="tns:ListOfPubSubCommunicationConfigurationResultDataType"/>\n <xs:complexType name="CommunicationLinkConfigurationDataType">\n  <xs:sequence/>\n </xs:complexType>\n <xs:element name="CommunicationLinkConfigurationDataType" type="tns:CommunicationLinkConfigurationDataType"/>\n <xs:complexType name="ListOfCommunicationLinkConfigurationDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="CommunicationLinkConfigurationDataType" nillable="true" type="tns:CommunicationLinkConfigurationDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfCommunicationLinkConfigurationDataType" nillable="true" type="tns:ListOfCommunicationLinkConfigurationDataType"/>\n <xs:complexType name="PubSubCommunicationLinkConfigurationDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element maxOccurs="1" name="DataSetReaderRef" type="ua:PubSubConfigurationRefDataType" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="ExpectedSubscribedDataSetVersion" type="ua:ConfigurationVersionDataType" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="DataSetWriterRef" type="ua:PubSubConfigurationRefDataType" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="ExpectedPublishedDataSetVersion" type="ua:ConfigurationVersionDataType" minOccurs="0"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element name="PubSubCommunicationLinkConfigurationDataType" type="tns:PubSubCommunicationLinkConfigurationDataType"/>\n <xs:complexType name="ListOfPubSubCommunicationLinkConfigurationDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="PubSubCommunicationLinkConfigurationDataType" nillable="true" type="tns:PubSubCommunicationLinkConfigurationDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPubSubCommunicationLinkConfigurationDataType" nillable="true" type="tns:ListOfPubSubCommunicationLinkConfigurationDataType"/>\n <xs:complexType name="ConnectionEndpointConfigurationDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="FunctionalEntityNode" type="ua:NodeId" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ConnectionEndpoint" type="tns:ConnectionEndpointDefinitionDataType" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ExpectedVerificationVariables" type="tns:ListOfNodeIdValuePair" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ControlGroups" type="ua:ListOfNodeId" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ConfigurationData" type="tns:ListOfNodeIdValuePair" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="CommunicationLinks" type="ua:ExtensionObject" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ConnectionEndpointConfigurationDataType" type="tns:ConnectionEndpointConfigurationDataType"/>\n <xs:complexType name="ListOfConnectionEndpointConfigurationDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="ConnectionEndpointConfigurationDataType" nillable="true" type="tns:ConnectionEndpointConfigurationDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfConnectionEndpointConfigurationDataType" nillable="true" type="tns:ListOfConnectionEndpointConfigurationDataType"/>\n <xs:complexType name="ConnectionEndpointConfigurationResultDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="ConnectionEndpointId" type="ua:NodeId" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="FunctionalEntityNodeResult" type="ua:StatusCode" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ConnectionEndpointResult" type="ua:StatusCode" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="VerificationResult" type="tns:FunctionalEntityVerificationResultEnum" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="VerificationStatus" type="ua:StatusCode" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="VerificationVariablesErrors" type="ua:ListOfStatusCode" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="EstablishControlResult" type="ua:ListOfStatusCode" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ConfigurationDataResult" type="ua:ListOfStatusCode" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ReassignControlResult" type="ua:ListOfStatusCode" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="CommunicationLinksResult" type="ua:StatusCode" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="EnableCommunicationResult" type="ua:StatusCode" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ConnectionEndpointConfigurationResultDataType" type="tns:ConnectionEndpointConfigurationResultDataType"/>\n <xs:complexType name="ListOfConnectionEndpointConfigurationResultDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="ConnectionEndpointConfigurationResultDataType" nillable="true" type="tns:ConnectionEndpointConfigurationResultDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfConnectionEndpointConfigurationResultDataType" nillable="true" type="tns:ListOfConnectionEndpointConfigurationResultDataType"/>\n <xs:complexType name="ConnectionEndpointParameterDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="Name" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ConnectionEndpointTypeId" type="ua:NodeId" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="InputVariableIds" type="ua:ListOfNodeId" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="OutputVariableIds" type="ua:ListOfNodeId" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="IsPersistent" type="xs:boolean" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="CleanupTimeout" type="xs:double" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="RelatedEndpoint" type="tns:RelatedEndpointDataType" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="IsPreconfigured" type="xs:boolean" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ConnectionEndpointParameterDataType" type="tns:ConnectionEndpointParameterDataType"/>\n <xs:complexType name="ListOfConnectionEndpointParameterDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="ConnectionEndpointParameterDataType" nillable="true" type="tns:ConnectionEndpointParameterDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfConnectionEndpointParameterDataType" nillable="true" type="tns:ListOfConnectionEndpointParameterDataType"/>\n <xs:complexType name="PubSubConnectionEndpointParameterDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element maxOccurs="1" name="Mode" type="tns:PubSubConnectionEndpointModeEnum" minOccurs="0"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element name="PubSubConnectionEndpointParameterDataType" type="tns:PubSubConnectionEndpointParameterDataType"/>\n <xs:complexType name="ListOfPubSubConnectionEndpointParameterDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="PubSubConnectionEndpointParameterDataType" nillable="true" type="tns:PubSubConnectionEndpointParameterDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPubSubConnectionEndpointParameterDataType" nillable="true" type="tns:ListOfPubSubConnectionEndpointParameterDataType"/>\n <xs:complexType name="IntervalRange">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="Min" type="xs:unsignedInt" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Max" type="xs:unsignedInt" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Increment" type="xs:unsignedShort" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Multiplier" type="xs:unsignedShort" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Unit" type="tns:FxTimeUnitsEnum" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="IntervalRange" type="tns:IntervalRange"/>\n <xs:complexType name="ListOfIntervalRange">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="IntervalRange" nillable="true" type="tns:IntervalRange" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfIntervalRange" nillable="true" type="tns:ListOfIntervalRange"/>\n <xs:complexType name="NodeIdArray">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="Node" type="ua:NodeId" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ArrayIndex" type="ua:ListOfUInt32" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="NodeIdArray" type="tns:NodeIdArray"/>\n <xs:complexType name="ListOfNodeIdArray">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="NodeIdArray" nillable="true" type="tns:NodeIdArray" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfNodeIdArray" nillable="true" type="tns:ListOfNodeIdArray"/>\n <xs:complexType name="NodeIdValuePair">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="Key" type="tns:NodeIdArray" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="Value" type="ua:Variant" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="NodeIdValuePair" type="tns:NodeIdValuePair"/>\n <xs:complexType name="ListOfNodeIdValuePair">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="NodeIdValuePair" nillable="true" type="tns:NodeIdValuePair" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfNodeIdValuePair" nillable="true" type="tns:ListOfNodeIdValuePair"/>\n <xs:complexType name="RelatedEndpointDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="Address" type="xs:string" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ConnectionEndpointPath" type="ua:ListOfPortableQualifiedName" minOccurs="0"/>\n   <xs:element maxOccurs="1" name="ConnectionEndpointName" type="xs:string" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="RelatedEndpointDataType" type="tns:RelatedEndpointDataType"/>\n <xs:complexType name="ListOfRelatedEndpointDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="RelatedEndpointDataType" nillable="true" type="tns:RelatedEndpointDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfRelatedEndpointDataType" nillable="true" type="tns:ListOfRelatedEndpointDataType"/>\n <xs:complexType name="ReserveCommunicationIdsDataType">\n  <xs:sequence/>\n </xs:complexType>\n <xs:element name="ReserveCommunicationIdsDataType" type="tns:ReserveCommunicationIdsDataType"/>\n <xs:complexType name="ListOfReserveCommunicationIdsDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="ReserveCommunicationIdsDataType" nillable="true" type="tns:ReserveCommunicationIdsDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfReserveCommunicationIdsDataType" nillable="true" type="tns:ListOfReserveCommunicationIdsDataType"/>\n <xs:complexType name="PubSubReserveCommunicationIdsDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element maxOccurs="1" name="TransportProfileUri" type="xs:string" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="NumReqWriterGroupIds" type="xs:unsignedShort" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="NumReqDataSetWriterIds" type="xs:unsignedShort" minOccurs="0"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element name="PubSubReserveCommunicationIdsDataType" type="tns:PubSubReserveCommunicationIdsDataType"/>\n <xs:complexType name="ListOfPubSubReserveCommunicationIdsDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="PubSubReserveCommunicationIdsDataType" nillable="true" type="tns:PubSubReserveCommunicationIdsDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPubSubReserveCommunicationIdsDataType" nillable="true" type="tns:ListOfPubSubReserveCommunicationIdsDataType"/>\n <xs:complexType name="PubSubReserveCommunicationIds2DataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:PubSubReserveCommunicationIdsDataType">\n    <xs:sequence>\n     <xs:element maxOccurs="1" name="RequestTransportSpecificInfo" type="xs:boolean" minOccurs="0"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element name="PubSubReserveCommunicationIds2DataType" type="tns:PubSubReserveCommunicationIds2DataType"/>\n <xs:complexType name="ListOfPubSubReserveCommunicationIds2DataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="PubSubReserveCommunicationIds2DataType" nillable="true" type="tns:PubSubReserveCommunicationIds2DataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPubSubReserveCommunicationIds2DataType" nillable="true" type="tns:ListOfPubSubReserveCommunicationIds2DataType"/>\n <xs:complexType name="ReserveCommunicationIdsResultDataType">\n  <xs:sequence/>\n </xs:complexType>\n <xs:element name="ReserveCommunicationIdsResultDataType" type="tns:ReserveCommunicationIdsResultDataType"/>\n <xs:complexType name="ListOfReserveCommunicationIdsResultDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="ReserveCommunicationIdsResultDataType" nillable="true" type="tns:ReserveCommunicationIdsResultDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfReserveCommunicationIdsResultDataType" nillable="true" type="tns:ListOfReserveCommunicationIdsResultDataType"/>\n <xs:complexType name="PubSubReserveCommunicationIdsResultDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element maxOccurs="1" name="Result" type="ua:StatusCode" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="DefaultPublisherId" type="ua:Variant" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="WriterGroupIds" type="ua:ListOfUInt16" minOccurs="0"/>\n     <xs:element maxOccurs="1" name="DataSetWriterIds" type="ua:ListOfUInt16" minOccurs="0"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element name="PubSubReserveCommunicationIdsResultDataType" type="tns:PubSubReserveCommunicationIdsResultDataType"/>\n <xs:complexType name="ListOfPubSubReserveCommunicationIdsResultDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="PubSubReserveCommunicationIdsResultDataType" nillable="true" type="tns:PubSubReserveCommunicationIdsResultDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPubSubReserveCommunicationIdsResultDataType" nillable="true" type="tns:ListOfPubSubReserveCommunicationIdsResultDataType"/>\n <xs:complexType name="PubSubReserveCommunicationIdsResult2DataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:PubSubReserveCommunicationIdsResultDataType">\n    <xs:sequence>\n     <xs:element maxOccurs="1" name="TransportSpecificInfo" type="ua:Variant" minOccurs="0"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element name="PubSubReserveCommunicationIdsResult2DataType" type="tns:PubSubReserveCommunicationIdsResult2DataType"/>\n <xs:complexType name="ListOfPubSubReserveCommunicationIdsResult2DataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="PubSubReserveCommunicationIdsResult2DataType" nillable="true" type="tns:PubSubReserveCommunicationIdsResult2DataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPubSubReserveCommunicationIdsResult2DataType" nillable="true" type="tns:ListOfPubSubReserveCommunicationIdsResult2DataType"/>\n <xs:complexType name="ConnectionEndpointDefinitionDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" name="SwitchField" type="xs:unsignedInt" minOccurs="0"/>\n   <xs:choice>\n    <xs:element maxOccurs="1" name="Parameter" type="ua:ExtensionObject" minOccurs="0"/>\n    <xs:element maxOccurs="1" name="Node" type="ua:NodeId" minOccurs="0"/>\n   </xs:choice>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ConnectionEndpointDefinitionDataType" type="tns:ConnectionEndpointDefinitionDataType"/>\n <xs:complexType name="ListOfConnectionEndpointDefinitionDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" name="ConnectionEndpointDefinitionDataType" nillable="true" type="tns:ConnectionEndpointDefinitionDataType" minOccurs="0"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfConnectionEndpointDefinitionDataType" nillable="true" type="tns:ListOfConnectionEndpointDefinitionDataType"/>\n</xs:schema>\n',
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_data;i=6532",
    browseName="EnumValues",
    parent="ns=fx_data;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("NotSet"), description=o6.LocalizedText("The verification result is not set.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Match"), description=o6.LocalizedText("FunctionalEntity matches expectation.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Mismatch"), description=o6.LocalizedText("FunctionalEntity does not match expectation.")),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=fx_data;i=6170",
    browseName="InputArguments",
    parent="ns=fx_data;i=7027",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationUri", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=fx_data;i=7027", browseName="AddApplication", inputArgs=o6.hasProperty(o6.ns["ns=fx_data;i=6170"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_data;i=6331",
    browseName="InputArguments",
    parent="ns=fx_data;i=7028",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Endpoint", dataType=ns0.datatypes.EndpointType, valueRank=-1)],
)
o6.call(nodeId="ns=fx_data;i=7028", browseName="AddEndpoint", inputArgs=o6.hasProperty(o6.ns["ns=fx_data;i=6331"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_data;i=6332",
    browseName="InputArguments",
    parent="ns=fx_data;i=7029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Rule", dataType=ns0.datatypes.IdentityMappingRuleType, valueRank=-1)],
)
o6.call(nodeId="ns=fx_data;i=7029", browseName="AddIdentity", inputArgs=o6.hasProperty(o6.ns["ns=fx_data;i=6332"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_data;i=6406",
    browseName="InputArguments",
    parent="ns=fx_data;i=7030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationUri", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=fx_data;i=7030", browseName="RemoveApplication", inputArgs=o6.hasProperty(o6.ns["ns=fx_data;i=6406"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_data;i=6407",
    browseName="InputArguments",
    parent="ns=fx_data;i=7031",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Endpoint", dataType=ns0.datatypes.EndpointType, valueRank=-1)],
)
o6.call(nodeId="ns=fx_data;i=7031", browseName="RemoveEndpoint", inputArgs=o6.hasProperty(o6.ns["ns=fx_data;i=6407"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_data;i=6408",
    browseName="InputArguments",
    parent="ns=fx_data;i=7032",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Rule", dataType=ns0.datatypes.IdentityMappingRuleType, valueRank=-1)],
)
o6.call(nodeId="ns=fx_data;i=7032", browseName="RemoveIdentity", inputArgs=o6.hasProperty(o6.ns["ns=fx_data;i=6408"]))

connectionAdmin = ns0.objtypes.RoleType(
    nodeId="ns=fx_data;i=5019",
    browseName="ns=fx_data;ConnectionAdmin",
    description="The Role is allowed to establish, close, and modify Connections between FunctionalEntities. \nThis includes reading and writing connection configuration settings, reading endpoint and connection capabilities, and executing methods related to management of Connections.\nIt is intended to be a non-human Role.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_data;i=6400", browseName="Applications", dataType=o6.String, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_data;i=6402", browseName="ApplicationsExclude", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_data;i=6403", browseName="Endpoints", dataType=ns0.datatypes.EndpointType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_data;i=6404", browseName="EndpointsExclude", dataType=o6.Boolean)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fx_data;i=6405", browseName="Identities", dataType=ns0.datatypes.IdentityMappingRuleType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasComponent(o6.ns["ns=fx_data;i=7027"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=7028"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=7029"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=7030"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=7031"]),
        o6.hasComponent(o6.ns["ns=fx_data;i=7032"]),
    ],
    parent="i=15606",
    referenceType=ns0.reftypes.HasComponent,
)


del Any, TYPE_CHECKING, uuid, o6, ns0, fx_data_datypes, fx_data_objtypes
