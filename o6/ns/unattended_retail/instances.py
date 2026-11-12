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

"""Generated OPC UA unattended_retail namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import datatypes as unattended_retail_datypes
from . import objtypes as unattended_retail_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5009", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5010", browseName="Default XML")
o6.hasEncoding(unattended_retail_datypes.OptionDescriptionDataType, o6.ns["ns=unattended_retail;i=5010"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5011", browseName="Default JSON")
o6.hasEncoding(unattended_retail_datypes.OptionDescriptionDataType, o6.ns["ns=unattended_retail;i=5011"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5012", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5013", browseName="Default XML")
o6.hasEncoding(unattended_retail_datypes.SelectionDescriptionDataType, o6.ns["ns=unattended_retail;i=5013"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5014", browseName="Default JSON")
o6.hasEncoding(unattended_retail_datypes.SelectionDescriptionDataType, o6.ns["ns=unattended_retail;i=5014"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5017", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5018", browseName="Default XML")
o6.hasEncoding(unattended_retail_datypes.PriceDataType, o6.ns["ns=unattended_retail;i=5018"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5019", browseName="Default JSON")
o6.hasEncoding(unattended_retail_datypes.PriceDataType, o6.ns["ns=unattended_retail;i=5019"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5020", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5021", browseName="Default XML")
o6.hasEncoding(unattended_retail_datypes.DeliveryRequestDataType, o6.ns["ns=unattended_retail;i=5021"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5022", browseName="Default JSON")
o6.hasEncoding(unattended_retail_datypes.DeliveryRequestDataType, o6.ns["ns=unattended_retail;i=5022"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5023", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5024", browseName="Default XML")
o6.hasEncoding(unattended_retail_datypes.OptionSelectionDataType, o6.ns["ns=unattended_retail;i=5024"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5025", browseName="Default JSON")
o6.hasEncoding(unattended_retail_datypes.OptionSelectionDataType, o6.ns["ns=unattended_retail;i=5025"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5026", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5027", browseName="Default XML")
o6.hasEncoding(unattended_retail_datypes.DeliveryProgressDataType, o6.ns["ns=unattended_retail;i=5027"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5028", browseName="Default JSON")
o6.hasEncoding(unattended_retail_datypes.DeliveryProgressDataType, o6.ns["ns=unattended_retail;i=5028"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5031", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5032", browseName="Default XML")
o6.hasEncoding(unattended_retail_datypes.OutputDeliveryStatusDataType, o6.ns["ns=unattended_retail;i=5032"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5033", browseName="Default JSON")
o6.hasEncoding(unattended_retail_datypes.OutputDeliveryStatusDataType, o6.ns["ns=unattended_retail;i=5033"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5034", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5035", browseName="Default XML")
o6.hasEncoding(unattended_retail_datypes.OutputStatusDataType, o6.ns["ns=unattended_retail;i=5035"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5036", browseName="Default JSON")
o6.hasEncoding(unattended_retail_datypes.OutputStatusDataType, o6.ns["ns=unattended_retail;i=5036"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5037", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5038", browseName="Default XML")
o6.hasEncoding(unattended_retail_datypes.AvailabilityStatusDataType, o6.ns["ns=unattended_retail;i=5038"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5039", browseName="Default JSON")
o6.hasEncoding(unattended_retail_datypes.AvailabilityStatusDataType, o6.ns["ns=unattended_retail;i=5039"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5043", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5044", browseName="Default XML")
o6.hasEncoding(unattended_retail_datypes.BasketProgressDataType, o6.ns["ns=unattended_retail;i=5044"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5045", browseName="Default JSON")
o6.hasEncoding(unattended_retail_datypes.BasketProgressDataType, o6.ns["ns=unattended_retail;i=5045"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5046", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5047", browseName="Default XML")
o6.hasEncoding(unattended_retail_datypes.SelectionPriceDataType, o6.ns["ns=unattended_retail;i=5047"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5048", browseName="Default JSON")
o6.hasEncoding(unattended_retail_datypes.SelectionPriceDataType, o6.ns["ns=unattended_retail;i=5048"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5052", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5053", browseName="Default XML")
o6.hasEncoding(unattended_retail_datypes.SelectionDataType, o6.ns["ns=unattended_retail;i=5053"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5054", browseName="Default JSON")
o6.hasEncoding(unattended_retail_datypes.SelectionDataType, o6.ns["ns=unattended_retail;i=5054"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5065", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5066", browseName="Default XML")
o6.hasEncoding(unattended_retail_datypes.PriceAndContextDataType, o6.ns["ns=unattended_retail;i=5066"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5067", browseName="Default JSON")
o6.hasEncoding(unattended_retail_datypes.PriceAndContextDataType, o6.ns["ns=unattended_retail;i=5067"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5068", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5069", browseName="Default XML")
o6.hasEncoding(unattended_retail_datypes.TransactionProgressDataType, o6.ns["ns=unattended_retail;i=5069"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5070", browseName="Default JSON")
o6.hasEncoding(unattended_retail_datypes.TransactionProgressDataType, o6.ns["ns=unattended_retail;i=5070"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5071", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5072", browseName="Default XML")
o6.hasEncoding(unattended_retail_datypes.ActualPaymentDataType, o6.ns["ns=unattended_retail;i=5072"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5073", browseName="Default JSON")
o6.hasEncoding(unattended_retail_datypes.ActualPaymentDataType, o6.ns["ns=unattended_retail;i=5073"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5082", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5083", browseName="Default XML")
o6.hasEncoding(unattended_retail_datypes.SlotConfigurationDataType, o6.ns["ns=unattended_retail;i=5083"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=unattended_retail;i=5084", browseName="Default JSON")
o6.hasEncoding(unattended_retail_datypes.SlotConfigurationDataType, o6.ns["ns=unattended_retail;i=5084"])
unattended_retail_objtypes.BaseConfigurationType(
    nodeId="ns=unattended_retail;i=5002",
    browseName="ns=unattended_retail;Configuration",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6016", browseName="LocalTime", dataType=ns0.datatypes.TimeZoneDataType))],
)
o6.reference(unattended_retail_objtypes.MachineEngineType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=5002"])
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6023",
    browseName="EnumStrings",
    parent="ns=unattended_retail;i=3004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("Available"), o6.LocalizedText("OutOfOrder"), o6.LocalizedText("TemporaryNotAvailable"), o6.LocalizedText("Empty")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6034",
    browseName="EnumStrings",
    parent="ns=unattended_retail;i=3010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        o6.LocalizedText("Initializing"),
        o6.LocalizedText("WaitingForTemperature"),
        o6.LocalizedText("Ready"),
        o6.LocalizedText("Cleaning"),
        o6.LocalizedText("Dispensing"),
        o6.LocalizedText("Busy"),
        o6.LocalizedText("OutOfOrder"),
        o6.LocalizedText("EnergySavingMode"),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=unattended_retail;i=6035",
    browseName="ns=unattended_retail;<SensorData>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6036", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
)
o6.reference(unattended_retail_objtypes.MachineEngineStatusType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=6035"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6043", browseName="ns=unattended_retail;OptionDescriptionDataType", dataType=o6.String, value="OptionDescriptionDataType"
)
o6.reference(o6.ns["ns=unattended_retail;i=5009"], "i=39", o6.ns["ns=unattended_retail;i=6043"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6044", browseName="ns=unattended_retail;OptionDescriptionDataType", dataType=o6.String, value="//xs:element[@name='OptionDescriptionDataType']"
)
o6.reference(o6.ns["ns=unattended_retail;i=5010"], "i=39", o6.ns["ns=unattended_retail;i=6044"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6047", browseName="ns=unattended_retail;SelectionDescriptionDataType", dataType=o6.String, value="SelectionDescriptionDataType"
)
o6.reference(o6.ns["ns=unattended_retail;i=5012"], "i=39", o6.ns["ns=unattended_retail;i=6047"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6048",
    browseName="ns=unattended_retail;SelectionDescriptionDataType",
    dataType=o6.String,
    value="//xs:element[@name='SelectionDescriptionDataType']",
)
o6.reference(o6.ns["ns=unattended_retail;i=5013"], "i=39", o6.ns["ns=unattended_retail;i=6048"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=unattended_retail;i=6051",
    browseName="ns=unattended_retail;MainColdTemperature",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=unattended_retail;i=6052",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText("°C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        )
    ],
    dataType=o6.Float,
)
o6.reference(unattended_retail_objtypes.MachineEngineStatusType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=6051"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=unattended_retail;i=6053",
    browseName="ns=unattended_retail;MainHotTemperature",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=unattended_retail;i=6054",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText("°C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        )
    ],
    dataType=o6.Float,
)
o6.reference(unattended_retail_objtypes.MachineEngineStatusType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=6053"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=unattended_retail;i=6055", browseName="ns=unattended_retail;PriceDataType", dataType=o6.String, value="PriceDataType")
o6.reference(o6.ns["ns=unattended_retail;i=5017"], "i=39", o6.ns["ns=unattended_retail;i=6055"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6056", browseName="ns=unattended_retail;PriceDataType", dataType=o6.String, value="//xs:element[@name='PriceDataType']"
)
o6.reference(o6.ns["ns=unattended_retail;i=5018"], "i=39", o6.ns["ns=unattended_retail;i=6056"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6059", browseName="ns=unattended_retail;DeliveryRequestDataType", dataType=o6.String, value="DeliveryRequestDataType"
)
o6.reference(o6.ns["ns=unattended_retail;i=5020"], "i=39", o6.ns["ns=unattended_retail;i=6059"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6060", browseName="ns=unattended_retail;DeliveryRequestDataType", dataType=o6.String, value="//xs:element[@name='DeliveryRequestDataType']"
)
o6.reference(o6.ns["ns=unattended_retail;i=5021"], "i=39", o6.ns["ns=unattended_retail;i=6060"])
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6061",
    browseName="EnumStrings",
    parent="ns=unattended_retail;i=3015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        o6.LocalizedText("ReadyToDeliver"),
        o6.LocalizedText("DeliveryStarted"),
        o6.LocalizedText("DeliveryFinished"),
        o6.LocalizedText("DeliveryFailed"),
        o6.LocalizedText("DeliveryCannotStart"),
    ],
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6066", browseName="ns=unattended_retail;OptionSelectionDataType", dataType=o6.String, value="OptionSelectionDataType"
)
o6.reference(o6.ns["ns=unattended_retail;i=5023"], "i=39", o6.ns["ns=unattended_retail;i=6066"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6067", browseName="ns=unattended_retail;OptionSelectionDataType", dataType=o6.String, value="//xs:element[@name='OptionSelectionDataType']"
)
o6.reference(o6.ns["ns=unattended_retail;i=5024"], "i=39", o6.ns["ns=unattended_retail;i=6067"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6068", browseName="ns=unattended_retail;DeliveryProgressDataType", dataType=o6.String, value="DeliveryProgressDataType"
)
o6.reference(o6.ns["ns=unattended_retail;i=5026"], "i=39", o6.ns["ns=unattended_retail;i=6068"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6069", browseName="ns=unattended_retail;DeliveryProgressDataType", dataType=o6.String, value="//xs:element[@name='DeliveryProgressDataType']"
)
o6.reference(o6.ns["ns=unattended_retail;i=5027"], "i=39", o6.ns["ns=unattended_retail;i=6069"])
unattended_retail_objtypes.BaseConfigurationType(
    nodeId="ns=unattended_retail;i=5030",
    browseName="ns=unattended_retail;Configuration",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6076", browseName="LocalTime", dataType=ns0.datatypes.TimeZoneDataType))],
)
o6.reference(unattended_retail_objtypes.PaymentServiceType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=5030"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6077", browseName="ns=unattended_retail;OutputDeliveryStatusDataType", dataType=o6.String, value="OutputDeliveryStatusDataType"
)
o6.reference(o6.ns["ns=unattended_retail;i=5031"], "i=39", o6.ns["ns=unattended_retail;i=6077"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6078",
    browseName="ns=unattended_retail;OutputDeliveryStatusDataType",
    dataType=o6.String,
    value="//xs:element[@name='OutputDeliveryStatusDataType']",
)
o6.reference(o6.ns["ns=unattended_retail;i=5032"], "i=39", o6.ns["ns=unattended_retail;i=6078"])
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6079",
    browseName="EnumStrings",
    parent="ns=unattended_retail;i=3012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        o6.LocalizedText("Free"),
        o6.LocalizedText("ProductNotTaken"),
        o6.LocalizedText("OutOfOrder"),
        o6.LocalizedText("Locked"),
        o6.LocalizedText("CleaningRequired"),
        o6.LocalizedText("VendorSpecific"),
    ],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=unattended_retail;i=6080", browseName="ns=unattended_retail;OutputStatusDataType", dataType=o6.String, value="OutputStatusDataType")
o6.reference(o6.ns["ns=unattended_retail;i=5034"], "i=39", o6.ns["ns=unattended_retail;i=6080"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6081", browseName="ns=unattended_retail;OutputStatusDataType", dataType=o6.String, value="//xs:element[@name='OutputStatusDataType']"
)
o6.reference(o6.ns["ns=unattended_retail;i=5035"], "i=39", o6.ns["ns=unattended_retail;i=6081"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6082", browseName="ns=unattended_retail;AvailabilityStatusDataType", dataType=o6.String, value="AvailabilityStatusDataType"
)
o6.reference(o6.ns["ns=unattended_retail;i=5037"], "i=39", o6.ns["ns=unattended_retail;i=6082"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6083", browseName="ns=unattended_retail;AvailabilityStatusDataType", dataType=o6.String, value="//xs:element[@name='AvailabilityStatusDataType']"
)
o6.reference(o6.ns["ns=unattended_retail;i=5038"], "i=39", o6.ns["ns=unattended_retail;i=6083"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6087", browseName="ns=unattended_retail;BasketProgressDataType", dataType=o6.String, value="BasketProgressDataType"
)
o6.reference(o6.ns["ns=unattended_retail;i=5043"], "i=39", o6.ns["ns=unattended_retail;i=6087"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6088", browseName="ns=unattended_retail;BasketProgressDataType", dataType=o6.String, value="//xs:element[@name='BasketProgressDataType']"
)
o6.reference(o6.ns["ns=unattended_retail;i=5044"], "i=39", o6.ns["ns=unattended_retail;i=6088"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6089", browseName="ns=unattended_retail;SelectionPriceDataType", dataType=o6.String, value="SelectionPriceDataType"
)
o6.reference(o6.ns["ns=unattended_retail;i=5046"], "i=39", o6.ns["ns=unattended_retail;i=6089"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6090", browseName="ns=unattended_retail;SelectionPriceDataType", dataType=o6.String, value="//xs:element[@name='SelectionPriceDataType']"
)
o6.reference(o6.ns["ns=unattended_retail;i=5047"], "i=39", o6.ns["ns=unattended_retail;i=6090"])
http_opcfoundation_org_UA_UnattendedRetail_ = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=unattended_retail;i=5029",
    browseName="ns=unattended_retail;http://opcfoundation.org/UA/UnattendedRetail/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6039", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6040", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2026-07-15T00:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6070", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/UnattendedRetail/")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6071", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=unattended_retail;i=6072",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=unattended_retail;i=6073", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0], value=[]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6074", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6091", browseName="ModelVersion", dataType=ns0.datatypes.SemanticVersionString, value="1.0.0")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=unattended_retail;i=6093", browseName="ns=unattended_retail;SelectionDataType", dataType=o6.String, value="SelectionDataType")
o6.reference(o6.ns["ns=unattended_retail;i=5052"], "i=39", o6.ns["ns=unattended_retail;i=6093"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6094", browseName="ns=unattended_retail;SelectionDataType", dataType=o6.String, value="//xs:element[@name='SelectionDataType']"
)
o6.reference(o6.ns["ns=unattended_retail;i=5053"], "i=39", o6.ns["ns=unattended_retail;i=6094"])
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6095",
    browseName="EnumStrings",
    parent="ns=unattended_retail;i=3036",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("Available"), o6.LocalizedText("Offline"), o6.LocalizedText("OutOfOrder")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6096",
    browseName="EnumStrings",
    parent="ns=unattended_retail;i=3039",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("Available"), o6.LocalizedText("Offline"), o6.LocalizedText("OutOfOrder"), o6.LocalizedText("ExternallyStopped")],
)
unattended_retail_objtypes.MachineEngineCapabilitiesType(
    nodeId="ns=unattended_retail;i=5003",
    browseName="ns=unattended_retail;Capabilities",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=unattended_retail;i=6018",
                browseName="ns=unattended_retail;Options",
                dataType=unattended_retail_datypes.OptionDescriptionDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=unattended_retail;i=6046",
                browseName="ns=unattended_retail;SelectionList",
                dataType=unattended_retail_datypes.SelectionDescriptionDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6050", browseName="ns=unattended_retail;SelectionListVersion", dataType=ns0.datatypes.SemanticVersionString)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6099", browseName="ns=unattended_retail;OutputIds", dataType=o6.UInt16, valueRank=1, arrayDimensions=[0])
        ),
    ],
)
o6.reference(unattended_retail_objtypes.MachineEngineType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=5003"])
unattended_retail_objtypes.BaseConfigurationType(
    nodeId="ns=unattended_retail;i=5057",
    browseName="ns=unattended_retail;Configuration",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6116", browseName="LocalTime", dataType=ns0.datatypes.TimeZoneDataType))],
)
o6.reference(unattended_retail_objtypes.UIType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=5057"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6137", browseName="ns=unattended_retail;PriceAndContextDataType", dataType=o6.String, value="PriceAndContextDataType"
)
o6.reference(o6.ns["ns=unattended_retail;i=5065"], "i=39", o6.ns["ns=unattended_retail;i=6137"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6138", browseName="ns=unattended_retail;PriceAndContextDataType", dataType=o6.String, value="//xs:element[@name='PriceAndContextDataType']"
)
o6.reference(o6.ns["ns=unattended_retail;i=5066"], "i=39", o6.ns["ns=unattended_retail;i=6138"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6139", browseName="ns=unattended_retail;TransactionProgressDataType", dataType=o6.String, value="TransactionProgressDataType"
)
o6.reference(o6.ns["ns=unattended_retail;i=5068"], "i=39", o6.ns["ns=unattended_retail;i=6139"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6140",
    browseName="ns=unattended_retail;TransactionProgressDataType",
    dataType=o6.String,
    value="//xs:element[@name='TransactionProgressDataType']",
)
o6.reference(o6.ns["ns=unattended_retail;i=5069"], "i=39", o6.ns["ns=unattended_retail;i=6140"])
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6141",
    browseName="EnumStrings",
    parent="ns=unattended_retail;i=3026",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[17],
    value=[
        o6.LocalizedText("DeliveryRequestReceived"),
        o6.LocalizedText("PaymentInExecution"),
        o6.LocalizedText("PaymentFinished"),
        o6.LocalizedText("PaymentFailed"),
        o6.LocalizedText("PaymentCancelledByUser"),
        o6.LocalizedText("PaymentFailedWrongPrice"),
        o6.LocalizedText("DeliveryInExecution"),
        o6.LocalizedText("DeliveryAndPaymentSuccess"),
        o6.LocalizedText("DeliveryFailRefundInExecution"),
        o6.LocalizedText("DeliveryFailRefundSuccess"),
        o6.LocalizedText("DeliveryAndRefundFailed"),
        o6.LocalizedText("DeliveryMixResultRefundInExecution"),
        o6.LocalizedText("DeliveryMixResultRefundSuccess"),
        o6.LocalizedText("DeliveryMixResultRefundFailed"),
        o6.LocalizedText("CancelledByUserRefundInExcecution"),
        o6.LocalizedText("CancelledByUserRefundSuccess"),
        o6.LocalizedText("CancelledByUserRefundFailed"),
    ],
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6142", browseName="ns=unattended_retail;ActualPaymentDataType", dataType=o6.String, value="ActualPaymentDataType"
)
o6.reference(o6.ns["ns=unattended_retail;i=5071"], "i=39", o6.ns["ns=unattended_retail;i=6142"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6143", browseName="ns=unattended_retail;ActualPaymentDataType", dataType=o6.String, value="//xs:element[@name='ActualPaymentDataType']"
)
o6.reference(o6.ns["ns=unattended_retail;i=5072"], "i=39", o6.ns["ns=unattended_retail;i=6143"])
unattended_retail_objtypes.MachineEngineStatusType(
    nodeId="ns=unattended_retail;i=5008",
    browseName="ns=unattended_retail;Status",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=unattended_retail;i=6041", browseName="ns=unattended_retail;WorkingStatus", dataType=unattended_retail_datypes.MachineEngineWorkingStatusEnum
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=unattended_retail;i=6042",
                browseName="ns=unattended_retail;SelectionIdStatus",
                dataType=unattended_retail_datypes.AvailabilityStatusDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=unattended_retail;i=6100",
                browseName="ns=unattended_retail;OutputStatus",
                dataType=unattended_retail_datypes.OutputStatusDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=unattended_retail;i=6117",
                browseName="ns=unattended_retail;OptionIdStatus",
                dataType=unattended_retail_datypes.AvailabilityStatusDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=unattended_retail;i=6159", browseName="ns=unattended_retail;ActiveEVADTSStatusCodes", dataType=o6.String, valueRank=1, arrayDimensions=[0]
            )
        ),
    ],
)
o6.reference(unattended_retail_objtypes.MachineEngineType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=5008"])
unattended_retail_objtypes.IdentificationType(
    nodeId="ns=unattended_retail;i=5001",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6133", browseName="ns=di;ProductInstanceUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6173", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6181", browseName="ns=di;ProductCode", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6189", browseName="ns=di;SoftwareRevision", dataType=o6.String)),
    ],
)
o6.reference(unattended_retail_objtypes.MachineEngineType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=5001"])
unattended_retail_objtypes.IdentificationType(
    nodeId="ns=unattended_retail;i=5005",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6030", browseName="ns=di;ProductInstanceUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6174", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6182", browseName="ns=di;ProductCode", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6190", browseName="ns=di;SoftwareRevision", dataType=o6.String)),
    ],
)
o6.reference(unattended_retail_objtypes.AuditCollectType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=5005"])
unattended_retail_objtypes.IdentificationType(
    nodeId="ns=unattended_retail;i=5015",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6134", browseName="ns=di;ProductInstanceUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6175", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6183", browseName="ns=di;ProductCode", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6191", browseName="ns=di;SoftwareRevision", dataType=o6.String)),
    ],
)
o6.reference(unattended_retail_objtypes.UIType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=5015"])
unattended_retail_objtypes.IdentificationType(
    nodeId="ns=unattended_retail;i=5055",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6135", browseName="ns=di;ProductInstanceUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6176", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6184", browseName="ns=di;ProductCode", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6192", browseName="ns=di;SoftwareRevision", dataType=o6.String)),
    ],
)
o6.reference(unattended_retail_objtypes.PaymentServiceType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=5055"])
unattended_retail_objtypes.IdentificationType(
    nodeId="ns=unattended_retail;i=5058",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6136", browseName="ns=di;ProductInstanceUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6177", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6185", browseName="ns=di;ProductCode", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6193", browseName="ns=di;SoftwareRevision", dataType=o6.String)),
    ],
)
o6.reference(unattended_retail_objtypes.PriceServiceType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=5058"])
unattended_retail_objtypes.IdentificationType(
    nodeId="ns=unattended_retail;i=5076",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6166", browseName="ns=di;ProductInstanceUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6178", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6186", browseName="ns=di;ProductCode", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6194", browseName="ns=di;SoftwareRevision", dataType=o6.String)),
    ],
)
o6.reference(unattended_retail_objtypes.PaymentDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=5076"])
unattended_retail_objtypes.IdentificationType(
    nodeId="ns=unattended_retail;i=5077",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6171", browseName="ns=di;ProductInstanceUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6179", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6187", browseName="ns=di;ProductCode", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6195", browseName="ns=di;SoftwareRevision", dataType=o6.String)),
    ],
)
unattended_retail_objtypes.IdentificationType(
    nodeId="ns=unattended_retail;i=5079",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6172", browseName="ns=di;ProductInstanceUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6180", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6188", browseName="ns=di;ProductCode", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6196", browseName="ns=di;SoftwareRevision", dataType=o6.String)),
    ],
)
unattended_retail_objtypes.PaymentModeType(
    nodeId="ns=unattended_retail;i=5056",
    browseName="ns=unattended_retail;<PaymentMode>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=unattended_retail;i=6111", browseName="ns=unattended_retail;PaymentModeId", dataType=o6.String)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=unattended_retail;i=6112", browseName="ns=unattended_retail;Status", dataType=unattended_retail_datypes.PaymentModeOrDeviceStatusEnum
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=unattended_retail;i=6197", browseName="ns=unattended_retail;AvailableCredit", dataType=unattended_retail_datypes.PriceDataType
            )
        ),
    ],
)
o6.reference(unattended_retail_objtypes.PaymentModesType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=5056"])
unattended_retail_objtypes.PaymentModeType(
    nodeId="ns=unattended_retail;i=5063",
    browseName="ns=unattended_retail;PaymentMode",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=unattended_retail;i=6126", browseName="ns=unattended_retail;PaymentModeId", dataType=o6.String)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=unattended_retail;i=6127", browseName="ns=unattended_retail;Status", dataType=unattended_retail_datypes.PaymentModeOrDeviceStatusEnum
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=unattended_retail;i=6198", browseName="ns=unattended_retail;AvailableCredit", dataType=unattended_retail_datypes.PriceDataType
            )
        ),
    ],
)
unattended_retail_objtypes.PaymentModesType(
    nodeId="ns=unattended_retail;i=5062",
    browseName="ns=unattended_retail;PaymentModes",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=unattended_retail;i=5063"])],
)
o6.reference(unattended_retail_objtypes.PaymentServiceType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=5062"])
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6203",
    browseName="EnumStrings",
    parent="ns=unattended_retail;i=3007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        o6.LocalizedText("AcceptToCashboxOrStacker"),
        o6.LocalizedText("AcceptToRecyclerOrTube"),
        o6.LocalizedText("AcceptToEscrowAndStacker"),
        o6.LocalizedText("AcceptToEscrowAndRecycler"),
        o6.LocalizedText("Reject"),
    ],
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6204", browseName="ns=unattended_retail;SlotConfigurationDataType", dataType=o6.String, value="SlotConfigurationDataType"
)
o6.reference(o6.ns["ns=unattended_retail;i=5082"], "i=39", o6.ns["ns=unattended_retail;i=6204"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=unattended_retail;i=6024",
    browseName="ns=unattended_retail;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/UnattendedRetail/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6025", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/UnattendedRetail/")
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=unattended_retail;i=6026",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
                value=True,
            )
        ),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6043"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6047"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6055"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6059"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6066"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6068"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6077"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6080"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6082"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6087"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6089"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6093"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6137"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6139"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6142"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6204"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:tns="http://opcfoundation.org/UA/UnattendedRetail/" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/UnattendedRetail/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" DefaultByteOrder="LittleEndian">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType Name="ActualPaymentDataType" BaseType="ua:ExtensionObject">\n  <opc:Field Name="PaymentMode" TypeName="opc:CharArray"/>\n  <opc:Field Name="PaymentDevice" TypeName="opc:CharArray"/>\n  <opc:Field Name="UserId" TypeName="opc:CharArray"/>\n  <opc:Field Name="MonetaryValue" TypeName="tns:PriceDataType"/>\n </opc:StructuredType>\n <opc:StructuredType Name="AvailabilityStatusDataType" BaseType="ua:ExtensionObject">\n  <opc:Field Name="Id" TypeName="opc:CharArray"/>\n  <opc:Field Name="Status" TypeName="tns:AvailabilityEnum"/>\n  <opc:Field Name="EstimatedRemainingStock" TypeName="opc:UInt32"/>\n </opc:StructuredType>\n <opc:StructuredType Name="BasketProgressDataType" BaseType="ua:ExtensionObject">\n  <opc:Field Name="BasketId" TypeName="opc:UInt64"/>\n  <opc:Field Name="NoOfTransactionIds" TypeName="opc:Int32"/>\n  <opc:Field LengthField="NoOfTransactionIds" Name="TransactionIds" TypeName="opc:UInt64"/>\n  <opc:Field Name="Status" TypeName="tns:DeliveryAndPaymentStatusEnum"/>\n  <opc:Field Name="BasketFinished" TypeName="opc:Boolean"/>\n  <opc:Field Name="PaymentMode" TypeName="opc:CharArray"/>\n  <opc:Field Name="UserId" TypeName="opc:CharArray"/>\n  <opc:Field Name="UsedPrice" TypeName="tns:PriceAndContextDataType"/>\n </opc:StructuredType>\n <opc:StructuredType Name="DeliveryProgressDataType" BaseType="ua:ExtensionObject">\n  <opc:Field Name="ProgressInPercent" TypeName="opc:Byte"/>\n  <opc:Field Name="NoOfStatus" TypeName="opc:Int32"/>\n  <opc:Field LengthField="NoOfStatus" Name="Status" TypeName="tns:OutputDeliveryStatusDataType"/>\n  <opc:Field Name="TransactionId" TypeName="opc:UInt64"/>\n </opc:StructuredType>\n <opc:StructuredType Name="DeliveryRequestDataType" BaseType="ua:ExtensionObject">\n  <opc:Field Name="TransactionId" TypeName="opc:UInt64"/>\n  <opc:Field Name="SelectionId" TypeName="opc:CharArray"/>\n  <opc:Field Name="NoOfOptions" TypeName="opc:Int32"/>\n  <opc:Field LengthField="NoOfOptions" Name="Options" TypeName="tns:OptionSelectionDataType"/>\n </opc:StructuredType>\n <opc:StructuredType Name="OptionDescriptionDataType" BaseType="ua:ExtensionObject">\n  <opc:Field Name="OptionId" TypeName="opc:CharArray"/>\n  <opc:Field Name="Range" TypeName="ua:Range"/>\n  <opc:Field Name="Step" TypeName="opc:Double"/>\n  <opc:Field Name="Default" TypeName="opc:Double"/>\n  <opc:Field Name="EngineeringUnit" TypeName="ua:EUInformation"/>\n </opc:StructuredType>\n <opc:StructuredType Name="OptionSelectionDataType" BaseType="ua:ExtensionObject">\n  <opc:Field Name="OptionId" TypeName="opc:CharArray"/>\n  <opc:Field Name="Value" TypeName="opc:Double"/>\n </opc:StructuredType>\n <opc:StructuredType Name="OutputDeliveryStatusDataType" BaseType="ua:ExtensionObject">\n  <opc:Field Name="Status" TypeName="tns:DeliveryStatusEnum"/>\n  <opc:Field Name="OutputId" TypeName="opc:UInt16"/>\n </opc:StructuredType>\n <opc:StructuredType Name="OutputStatusDataType" BaseType="ua:ExtensionObject">\n  <opc:Field Name="OutputId" TypeName="opc:UInt16"/>\n  <opc:Field Name="Status" TypeName="tns:OutputStatusEnum"/>\n  <opc:Field Name="VendorStatus" TypeName="opc:Int32"/>\n </opc:StructuredType>\n <opc:StructuredType Name="PriceDataType" BaseType="ua:ExtensionObject">\n  <opc:Field Name="Amount" TypeName="opc:UInt32"/>\n  <opc:Field Name="Currency" TypeName="ua:CurrencyUnitType"/>\n </opc:StructuredType>\n <opc:StructuredType Name="PriceAndContextDataType" BaseType="tns:PriceDataType">\n  <opc:Field Name="Amount" SourceType="tns:PriceDataType" TypeName="opc:UInt32"/>\n  <opc:Field Name="Currency" SourceType="tns:PriceDataType" TypeName="ua:CurrencyUnitType"/>\n  <opc:Field Name="PriceListId" TypeName="opc:CharArray"/>\n  <opc:Field Name="Tax" TypeName="opc:Double"/>\n  <opc:Field Name="DiscountSurcharge" TypeName="opc:Int32"/>\n </opc:StructuredType>\n <opc:StructuredType Name="SelectionDataType" BaseType="ua:ExtensionObject">\n  <opc:Field Name="MachineEngineProductInstanceUri" TypeName="opc:CharArray"/>\n  <opc:Field Name="SelectionListVersion" TypeName="opc:CharArray"/>\n  <opc:Field Name="SelectionId" TypeName="opc:CharArray"/>\n  <opc:Field Name="NoOfOptions" TypeName="opc:Int32"/>\n  <opc:Field LengthField="NoOfOptions" Name="Options" TypeName="tns:OptionSelectionDataType"/>\n </opc:StructuredType>\n <opc:StructuredType Name="SelectionDescriptionDataType" BaseType="ua:ExtensionObject">\n  <opc:Field Name="SelectionId" TypeName="opc:CharArray"/>\n  <opc:Field Name="NoOfAvailableOptionIds" TypeName="opc:Int32"/>\n  <opc:Field LengthField="NoOfAvailableOptionIds" Name="AvailableOptionIds" TypeName="opc:CharArray"/>\n  <opc:Field Name="IsStoppable" TypeName="opc:Boolean"/>\n </opc:StructuredType>\n <opc:StructuredType Name="SelectionPriceDataType" BaseType="ua:ExtensionObject">\n  <opc:Field Name="SelectionId" TypeName="opc:CharArray"/>\n  <opc:Field Name="Price" TypeName="tns:PriceAndContextDataType"/>\n  <opc:Field Name="NoOfOptionsThatMayAffectThePrice" TypeName="opc:Int32"/>\n  <opc:Field LengthField="NoOfOptionsThatMayAffectThePrice" Name="OptionsThatMayAffectThePrice" TypeName="opc:CharArray"/>\n </opc:StructuredType>\n <opc:StructuredType Name="SlotConfigurationDataType" BaseType="ua:ExtensionObject">\n  <opc:Field Name="SlotIndex" TypeName="opc:Int32"/>\n  <opc:Field Name="SupportedAssetListIndex" TypeName="opc:UInt32"/>\n </opc:StructuredType>\n <opc:StructuredType Name="TransactionProgressDataType" BaseType="ua:ExtensionObject">\n  <opc:Field Name="TransactionId" TypeName="opc:UInt64"/>\n  <opc:Field Name="Status" TypeName="tns:DeliveryAndPaymentStatusEnum"/>\n  <opc:Field Name="TransactionFinished" TypeName="opc:Boolean"/>\n  <opc:Field Name="PaymentMode" TypeName="opc:CharArray"/>\n  <opc:Field Name="UserId" TypeName="opc:CharArray"/>\n  <opc:Field Name="UsedPrice" TypeName="tns:PriceAndContextDataType"/>\n </opc:StructuredType>\n <opc:EnumeratedType Name="AssetConfigurationEnum" LengthInBits="32">\n  <opc:EnumeratedValue Name="AcceptToCashboxOrStacker" Value="0"/>\n  <opc:EnumeratedValue Name="AcceptToRecyclerOrTube" Value="1"/>\n  <opc:EnumeratedValue Name="AcceptToEscrowAndStacker" Value="2"/>\n  <opc:EnumeratedValue Name="AcceptToEscrowAndRecycler" Value="3"/>\n  <opc:EnumeratedValue Name="Reject" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType Name="AvailabilityEnum" LengthInBits="32">\n  <opc:EnumeratedValue Name="Available" Value="0"/>\n  <opc:EnumeratedValue Name="OutOfOrder" Value="1"/>\n  <opc:EnumeratedValue Name="TemporaryNotAvailable" Value="2"/>\n  <opc:EnumeratedValue Name="Empty" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType Name="DeliveryAndPaymentStatusEnum" LengthInBits="32">\n  <opc:EnumeratedValue Name="DeliveryRequestReceived" Value="0"/>\n  <opc:EnumeratedValue Name="PaymentInExecution" Value="1"/>\n  <opc:EnumeratedValue Name="PaymentFinished" Value="2"/>\n  <opc:EnumeratedValue Name="PaymentFailed" Value="3"/>\n  <opc:EnumeratedValue Name="PaymentCancelledByUser" Value="4"/>\n  <opc:EnumeratedValue Name="PaymentFailedWrongPrice" Value="5"/>\n  <opc:EnumeratedValue Name="DeliveryInExecution" Value="6"/>\n  <opc:EnumeratedValue Name="DeliveryAndPaymentSuccess" Value="7"/>\n  <opc:EnumeratedValue Name="DeliveryFailRefundInExecution" Value="8"/>\n  <opc:EnumeratedValue Name="DeliveryFailRefundSuccess" Value="9"/>\n  <opc:EnumeratedValue Name="DeliveryAndRefundFailed" Value="10"/>\n  <opc:EnumeratedValue Name="DeliveryMixResultRefundInExecution" Value="11"/>\n  <opc:EnumeratedValue Name="DeliveryMixResultRefundSuccess" Value="12"/>\n  <opc:EnumeratedValue Name="DeliveryMixResultRefundFailed" Value="13"/>\n  <opc:EnumeratedValue Name="CancelledByUserRefundInExcecution" Value="14"/>\n  <opc:EnumeratedValue Name="CancelledByUserRefundSuccess" Value="15"/>\n  <opc:EnumeratedValue Name="CancelledByUserRefundFailed" Value="16"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType Name="DeliveryStatusEnum" LengthInBits="32">\n  <opc:EnumeratedValue Name="ReadyToDeliver" Value="0"/>\n  <opc:EnumeratedValue Name="DeliveryStarted" Value="1"/>\n  <opc:EnumeratedValue Name="DeliveryFinished" Value="2"/>\n  <opc:EnumeratedValue Name="DeliveryFailed" Value="3"/>\n  <opc:EnumeratedValue Name="DeliveryCannotStart" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType Name="MachineEngineWorkingStatusEnum" LengthInBits="32">\n  <opc:EnumeratedValue Name="Initializing" Value="0"/>\n  <opc:EnumeratedValue Name="WaitingForTemperature" Value="1"/>\n  <opc:EnumeratedValue Name="Ready" Value="2"/>\n  <opc:EnumeratedValue Name="Cleaning" Value="3"/>\n  <opc:EnumeratedValue Name="Dispensing" Value="4"/>\n  <opc:EnumeratedValue Name="Busy" Value="5"/>\n  <opc:EnumeratedValue Name="OutOfOrder" Value="6"/>\n  <opc:EnumeratedValue Name="EnergySavingMode" Value="7"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType Name="OperationStatusEnum" LengthInBits="32">\n  <opc:EnumeratedValue Name="Idle" Value="0"/>\n  <opc:EnumeratedValue Name="Ongoing" Value="1"/>\n  <opc:EnumeratedValue Name="SuccessfullyFinished" Value="2"/>\n  <opc:EnumeratedValue Name="Failed" Value="3"/>\n  <opc:EnumeratedValue Name="Failed_NoCommunication" Value="4"/>\n  <opc:EnumeratedValue Name="Failed_NotEnoughCredit" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType Name="OutputStatusEnum" LengthInBits="32">\n  <opc:EnumeratedValue Name="Free" Value="0"/>\n  <opc:EnumeratedValue Name="ProductNotTaken" Value="1"/>\n  <opc:EnumeratedValue Name="OutOfOrder" Value="2"/>\n  <opc:EnumeratedValue Name="Locked" Value="3"/>\n  <opc:EnumeratedValue Name="CleaningRequired" Value="4"/>\n  <opc:EnumeratedValue Name="VendorSpecific" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType Name="PaymentModeOrDeviceStatusEnum" LengthInBits="32">\n  <opc:EnumeratedValue Name="Available" Value="0"/>\n  <opc:EnumeratedValue Name="Offline" Value="1"/>\n  <opc:EnumeratedValue Name="OutOfOrder" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType Name="PaymentServiceStatusEnum" LengthInBits="32">\n  <opc:EnumeratedValue Name="Available" Value="0"/>\n  <opc:EnumeratedValue Name="Offline" Value="1"/>\n  <opc:EnumeratedValue Name="OutOfOrder" Value="2"/>\n  <opc:EnumeratedValue Name="ExternallyStopped" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType Name="PayoutStatusEnum" LengthInBits="32">\n  <opc:EnumeratedValue Name="Idle" Value="0"/>\n  <opc:EnumeratedValue Name="Ongoing" Value="1"/>\n  <opc:EnumeratedValue Name="SuccessfullyFinished" Value="2"/>\n  <opc:EnumeratedValue Name="Failed" Value="3"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=unattended_retail;i=6205", browseName="ns=unattended_retail;SlotConfigurationDataType", dataType=o6.String, value="//xs:element[@name='SlotConfigurationDataType']"
)
o6.reference(o6.ns["ns=unattended_retail;i=5083"], "i=39", o6.ns["ns=unattended_retail;i=6205"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=unattended_retail;i=6027",
    browseName="ns=unattended_retail;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/UnattendedRetail/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=unattended_retail;i=6028", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/UnattendedRetail/Types.xsd"
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=unattended_retail;i=6029",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
                value=True,
            )
        ),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6044"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6048"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6056"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6060"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6067"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6069"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6078"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6081"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6083"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6088"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6090"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6094"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6138"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6140"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6143"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=6205"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema xmlns:tns="http://opcfoundation.org/UA/UnattendedRetail/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/UnattendedRetail/Types.xsd">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="AssetConfigurationEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="AcceptToCashboxOrStacker_0"/>\n   <xs:enumeration value="AcceptToRecyclerOrTube_1"/>\n   <xs:enumeration value="AcceptToEscrowAndStacker_2"/>\n   <xs:enumeration value="AcceptToEscrowAndRecycler_3"/>\n   <xs:enumeration value="Reject_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="AssetConfigurationEnum" type="tns:AssetConfigurationEnum"/>\n <xs:complexType name="ListOfAssetConfigurationEnum">\n  <xs:sequence>\n   <xs:element name="AssetConfigurationEnum" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:AssetConfigurationEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfAssetConfigurationEnum" nillable="true" type="tns:ListOfAssetConfigurationEnum"/>\n <xs:simpleType name="AvailabilityEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Available_0"/>\n   <xs:enumeration value="OutOfOrder_1"/>\n   <xs:enumeration value="TemporaryNotAvailable_2"/>\n   <xs:enumeration value="Empty_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="AvailabilityEnum" type="tns:AvailabilityEnum"/>\n <xs:complexType name="ListOfAvailabilityEnum">\n  <xs:sequence>\n   <xs:element name="AvailabilityEnum" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:AvailabilityEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfAvailabilityEnum" nillable="true" type="tns:ListOfAvailabilityEnum"/>\n <xs:simpleType name="DeliveryAndPaymentStatusEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="DeliveryRequestReceived_0"/>\n   <xs:enumeration value="PaymentInExecution_1"/>\n   <xs:enumeration value="PaymentFinished_2"/>\n   <xs:enumeration value="PaymentFailed_3"/>\n   <xs:enumeration value="PaymentCancelledByUser_4"/>\n   <xs:enumeration value="PaymentFailedWrongPrice_5"/>\n   <xs:enumeration value="DeliveryInExecution_6"/>\n   <xs:enumeration value="DeliveryAndPaymentSuccess_7"/>\n   <xs:enumeration value="DeliveryFailRefundInExecution_8"/>\n   <xs:enumeration value="DeliveryFailRefundSuccess_9"/>\n   <xs:enumeration value="DeliveryAndRefundFailed_10"/>\n   <xs:enumeration value="DeliveryMixResultRefundInExecution_11"/>\n   <xs:enumeration value="DeliveryMixResultRefundSuccess_12"/>\n   <xs:enumeration value="DeliveryMixResultRefundFailed_13"/>\n   <xs:enumeration value="CancelledByUserRefundInExcecution_14"/>\n   <xs:enumeration value="CancelledByUserRefundSuccess_15"/>\n   <xs:enumeration value="CancelledByUserRefundFailed_16"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="DeliveryAndPaymentStatusEnum" type="tns:DeliveryAndPaymentStatusEnum"/>\n <xs:complexType name="ListOfDeliveryAndPaymentStatusEnum">\n  <xs:sequence>\n   <xs:element name="DeliveryAndPaymentStatusEnum" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:DeliveryAndPaymentStatusEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfDeliveryAndPaymentStatusEnum" nillable="true" type="tns:ListOfDeliveryAndPaymentStatusEnum"/>\n <xs:simpleType name="DeliveryStatusEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="ReadyToDeliver_0"/>\n   <xs:enumeration value="DeliveryStarted_1"/>\n   <xs:enumeration value="DeliveryFinished_2"/>\n   <xs:enumeration value="DeliveryFailed_3"/>\n   <xs:enumeration value="DeliveryCannotStart_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="DeliveryStatusEnum" type="tns:DeliveryStatusEnum"/>\n <xs:complexType name="ListOfDeliveryStatusEnum">\n  <xs:sequence>\n   <xs:element name="DeliveryStatusEnum" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:DeliveryStatusEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfDeliveryStatusEnum" nillable="true" type="tns:ListOfDeliveryStatusEnum"/>\n <xs:simpleType name="MachineEngineWorkingStatusEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Initializing_0"/>\n   <xs:enumeration value="WaitingForTemperature_1"/>\n   <xs:enumeration value="Ready_2"/>\n   <xs:enumeration value="Cleaning_3"/>\n   <xs:enumeration value="Dispensing_4"/>\n   <xs:enumeration value="Busy_5"/>\n   <xs:enumeration value="OutOfOrder_6"/>\n   <xs:enumeration value="EnergySavingMode_7"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="MachineEngineWorkingStatusEnum" type="tns:MachineEngineWorkingStatusEnum"/>\n <xs:complexType name="ListOfMachineEngineWorkingStatusEnum">\n  <xs:sequence>\n   <xs:element name="MachineEngineWorkingStatusEnum" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:MachineEngineWorkingStatusEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfMachineEngineWorkingStatusEnum" nillable="true" type="tns:ListOfMachineEngineWorkingStatusEnum"/>\n <xs:simpleType name="OperationStatusEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Idle_0"/>\n   <xs:enumeration value="Ongoing_1"/>\n   <xs:enumeration value="SuccessfullyFinished_2"/>\n   <xs:enumeration value="Failed_3"/>\n   <xs:enumeration value="Failed_NoCommunication_4"/>\n   <xs:enumeration value="Failed_NotEnoughCredit_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="OperationStatusEnum" type="tns:OperationStatusEnum"/>\n <xs:complexType name="ListOfOperationStatusEnum">\n  <xs:sequence>\n   <xs:element name="OperationStatusEnum" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:OperationStatusEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfOperationStatusEnum" nillable="true" type="tns:ListOfOperationStatusEnum"/>\n <xs:simpleType name="OutputStatusEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Free_0"/>\n   <xs:enumeration value="ProductNotTaken_1"/>\n   <xs:enumeration value="OutOfOrder_2"/>\n   <xs:enumeration value="Locked_3"/>\n   <xs:enumeration value="CleaningRequired_4"/>\n   <xs:enumeration value="VendorSpecific_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="OutputStatusEnum" type="tns:OutputStatusEnum"/>\n <xs:complexType name="ListOfOutputStatusEnum">\n  <xs:sequence>\n   <xs:element name="OutputStatusEnum" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:OutputStatusEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfOutputStatusEnum" nillable="true" type="tns:ListOfOutputStatusEnum"/>\n <xs:simpleType name="PaymentModeOrDeviceStatusEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Available_0"/>\n   <xs:enumeration value="Offline_1"/>\n   <xs:enumeration value="OutOfOrder_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="PaymentModeOrDeviceStatusEnum" type="tns:PaymentModeOrDeviceStatusEnum"/>\n <xs:complexType name="ListOfPaymentModeOrDeviceStatusEnum">\n  <xs:sequence>\n   <xs:element name="PaymentModeOrDeviceStatusEnum" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:PaymentModeOrDeviceStatusEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPaymentModeOrDeviceStatusEnum" nillable="true" type="tns:ListOfPaymentModeOrDeviceStatusEnum"/>\n <xs:simpleType name="PaymentServiceStatusEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Available_0"/>\n   <xs:enumeration value="Offline_1"/>\n   <xs:enumeration value="OutOfOrder_2"/>\n   <xs:enumeration value="ExternallyStopped_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="PaymentServiceStatusEnum" type="tns:PaymentServiceStatusEnum"/>\n <xs:complexType name="ListOfPaymentServiceStatusEnum">\n  <xs:sequence>\n   <xs:element name="PaymentServiceStatusEnum" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:PaymentServiceStatusEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPaymentServiceStatusEnum" nillable="true" type="tns:ListOfPaymentServiceStatusEnum"/>\n <xs:simpleType name="PayoutStatusEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Idle_0"/>\n   <xs:enumeration value="Ongoing_1"/>\n   <xs:enumeration value="SuccessfullyFinished_2"/>\n   <xs:enumeration value="Failed_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="PayoutStatusEnum" type="tns:PayoutStatusEnum"/>\n <xs:complexType name="ListOfPayoutStatusEnum">\n  <xs:sequence>\n   <xs:element name="PayoutStatusEnum" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:PayoutStatusEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPayoutStatusEnum" nillable="true" type="tns:ListOfPayoutStatusEnum"/>\n <xs:complexType name="ActualPaymentDataType">\n  <xs:sequence>\n   <xs:element name="PaymentMode" maxOccurs="1" minOccurs="0" type="xs:string"/>\n   <xs:element name="PaymentDevice" maxOccurs="1" minOccurs="0" type="xs:string"/>\n   <xs:element name="UserId" maxOccurs="1" minOccurs="0" type="xs:string"/>\n   <xs:element name="MonetaryValue" maxOccurs="1" minOccurs="0" type="tns:PriceDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ActualPaymentDataType" type="tns:ActualPaymentDataType"/>\n <xs:complexType name="ListOfActualPaymentDataType">\n  <xs:sequence>\n   <xs:element name="ActualPaymentDataType" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:ActualPaymentDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfActualPaymentDataType" nillable="true" type="tns:ListOfActualPaymentDataType"/>\n <xs:complexType name="AvailabilityStatusDataType">\n  <xs:sequence>\n   <xs:element name="Id" maxOccurs="1" minOccurs="0" type="xs:string"/>\n   <xs:element name="Status" maxOccurs="1" minOccurs="0" type="tns:AvailabilityEnum"/>\n   <xs:element name="EstimatedRemainingStock" maxOccurs="1" minOccurs="0" type="xs:unsignedInt"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="AvailabilityStatusDataType" type="tns:AvailabilityStatusDataType"/>\n <xs:complexType name="ListOfAvailabilityStatusDataType">\n  <xs:sequence>\n   <xs:element name="AvailabilityStatusDataType" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:AvailabilityStatusDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfAvailabilityStatusDataType" nillable="true" type="tns:ListOfAvailabilityStatusDataType"/>\n <xs:complexType name="BasketProgressDataType">\n  <xs:sequence>\n   <xs:element name="BasketId" maxOccurs="1" minOccurs="0" type="xs:unsignedLong"/>\n   <xs:element name="TransactionIds" maxOccurs="1" minOccurs="0" type="ua:ListOfUInt64"/>\n   <xs:element name="Status" maxOccurs="1" minOccurs="0" type="tns:DeliveryAndPaymentStatusEnum"/>\n   <xs:element name="BasketFinished" maxOccurs="1" minOccurs="0" type="xs:boolean"/>\n   <xs:element name="PaymentMode" maxOccurs="1" minOccurs="0" type="xs:string"/>\n   <xs:element name="UserId" maxOccurs="1" minOccurs="0" type="xs:string"/>\n   <xs:element name="UsedPrice" maxOccurs="1" minOccurs="0" type="tns:PriceAndContextDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="BasketProgressDataType" type="tns:BasketProgressDataType"/>\n <xs:complexType name="ListOfBasketProgressDataType">\n  <xs:sequence>\n   <xs:element name="BasketProgressDataType" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:BasketProgressDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfBasketProgressDataType" nillable="true" type="tns:ListOfBasketProgressDataType"/>\n <xs:complexType name="DeliveryProgressDataType">\n  <xs:sequence>\n   <xs:element name="ProgressInPercent" maxOccurs="1" minOccurs="0" type="xs:unsignedByte"/>\n   <xs:element name="Status" maxOccurs="1" minOccurs="0" type="tns:ListOfOutputDeliveryStatusDataType"/>\n   <xs:element name="TransactionId" maxOccurs="1" minOccurs="0" type="xs:unsignedLong"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="DeliveryProgressDataType" type="tns:DeliveryProgressDataType"/>\n <xs:complexType name="ListOfDeliveryProgressDataType">\n  <xs:sequence>\n   <xs:element name="DeliveryProgressDataType" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:DeliveryProgressDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfDeliveryProgressDataType" nillable="true" type="tns:ListOfDeliveryProgressDataType"/>\n <xs:complexType name="DeliveryRequestDataType">\n  <xs:sequence>\n   <xs:element name="TransactionId" maxOccurs="1" minOccurs="0" type="xs:unsignedLong"/>\n   <xs:element name="SelectionId" maxOccurs="1" minOccurs="0" type="xs:string"/>\n   <xs:element name="Options" maxOccurs="1" minOccurs="0" type="tns:ListOfOptionSelectionDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="DeliveryRequestDataType" type="tns:DeliveryRequestDataType"/>\n <xs:complexType name="ListOfDeliveryRequestDataType">\n  <xs:sequence>\n   <xs:element name="DeliveryRequestDataType" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:DeliveryRequestDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfDeliveryRequestDataType" nillable="true" type="tns:ListOfDeliveryRequestDataType"/>\n <xs:complexType name="OptionDescriptionDataType">\n  <xs:sequence>\n   <xs:element name="OptionId" maxOccurs="1" minOccurs="0" type="xs:string"/>\n   <xs:element name="Range" maxOccurs="1" minOccurs="0" type="ua:Range"/>\n   <xs:element name="Step" maxOccurs="1" minOccurs="0" type="xs:double"/>\n   <xs:element name="Default" maxOccurs="1" minOccurs="0" type="xs:double"/>\n   <xs:element name="EngineeringUnit" maxOccurs="1" minOccurs="0" type="ua:EUInformation"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="OptionDescriptionDataType" type="tns:OptionDescriptionDataType"/>\n <xs:complexType name="ListOfOptionDescriptionDataType">\n  <xs:sequence>\n   <xs:element name="OptionDescriptionDataType" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:OptionDescriptionDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfOptionDescriptionDataType" nillable="true" type="tns:ListOfOptionDescriptionDataType"/>\n <xs:complexType name="OptionSelectionDataType">\n  <xs:sequence>\n   <xs:element name="OptionId" maxOccurs="1" minOccurs="0" type="xs:string"/>\n   <xs:element name="Value" maxOccurs="1" minOccurs="0" type="xs:double"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="OptionSelectionDataType" type="tns:OptionSelectionDataType"/>\n <xs:complexType name="ListOfOptionSelectionDataType">\n  <xs:sequence>\n   <xs:element name="OptionSelectionDataType" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:OptionSelectionDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfOptionSelectionDataType" nillable="true" type="tns:ListOfOptionSelectionDataType"/>\n <xs:complexType name="OutputDeliveryStatusDataType">\n  <xs:sequence>\n   <xs:element name="Status" maxOccurs="1" minOccurs="0" type="tns:DeliveryStatusEnum"/>\n   <xs:element name="OutputId" maxOccurs="1" minOccurs="0" type="xs:unsignedShort"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="OutputDeliveryStatusDataType" type="tns:OutputDeliveryStatusDataType"/>\n <xs:complexType name="ListOfOutputDeliveryStatusDataType">\n  <xs:sequence>\n   <xs:element name="OutputDeliveryStatusDataType" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:OutputDeliveryStatusDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfOutputDeliveryStatusDataType" nillable="true" type="tns:ListOfOutputDeliveryStatusDataType"/>\n <xs:complexType name="OutputStatusDataType">\n  <xs:sequence>\n   <xs:element name="OutputId" maxOccurs="1" minOccurs="0" type="xs:unsignedShort"/>\n   <xs:element name="Status" maxOccurs="1" minOccurs="0" type="tns:OutputStatusEnum"/>\n   <xs:element name="VendorStatus" maxOccurs="1" minOccurs="0" type="xs:int"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="OutputStatusDataType" type="tns:OutputStatusDataType"/>\n <xs:complexType name="ListOfOutputStatusDataType">\n  <xs:sequence>\n   <xs:element name="OutputStatusDataType" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:OutputStatusDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfOutputStatusDataType" nillable="true" type="tns:ListOfOutputStatusDataType"/>\n <xs:complexType name="PriceDataType">\n  <xs:sequence>\n   <xs:element name="Amount" maxOccurs="1" minOccurs="0" type="xs:unsignedInt"/>\n   <xs:element name="Currency" maxOccurs="1" minOccurs="0" type="ua:CurrencyUnitType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="PriceDataType" type="tns:PriceDataType"/>\n <xs:complexType name="ListOfPriceDataType">\n  <xs:sequence>\n   <xs:element name="PriceDataType" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:PriceDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPriceDataType" nillable="true" type="tns:ListOfPriceDataType"/>\n <xs:complexType name="PriceAndContextDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:PriceDataType">\n    <xs:sequence>\n     <xs:element name="PriceListId" maxOccurs="1" minOccurs="0" type="xs:string"/>\n     <xs:element name="Tax" maxOccurs="1" minOccurs="0" type="xs:double"/>\n     <xs:element name="DiscountSurcharge" maxOccurs="1" minOccurs="0" type="xs:int"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element name="PriceAndContextDataType" type="tns:PriceAndContextDataType"/>\n <xs:complexType name="ListOfPriceAndContextDataType">\n  <xs:sequence>\n   <xs:element name="PriceAndContextDataType" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:PriceAndContextDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfPriceAndContextDataType" nillable="true" type="tns:ListOfPriceAndContextDataType"/>\n <xs:complexType name="SelectionDataType">\n  <xs:sequence>\n   <xs:element name="MachineEngineProductInstanceUri" maxOccurs="1" minOccurs="0" type="xs:string"/>\n   <xs:element name="SelectionListVersion" maxOccurs="1" minOccurs="0" type="xs:string"/>\n   <xs:element name="SelectionId" maxOccurs="1" minOccurs="0" type="xs:string"/>\n   <xs:element name="Options" maxOccurs="1" minOccurs="0" type="tns:ListOfOptionSelectionDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="SelectionDataType" type="tns:SelectionDataType"/>\n <xs:complexType name="ListOfSelectionDataType">\n  <xs:sequence>\n   <xs:element name="SelectionDataType" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:SelectionDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfSelectionDataType" nillable="true" type="tns:ListOfSelectionDataType"/>\n <xs:complexType name="SelectionDescriptionDataType">\n  <xs:sequence>\n   <xs:element name="SelectionId" maxOccurs="1" minOccurs="0" type="xs:string"/>\n   <xs:element name="AvailableOptionIds" maxOccurs="1" minOccurs="0" type="ua:ListOfString"/>\n   <xs:element name="IsStoppable" maxOccurs="1" minOccurs="0" type="xs:boolean"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="SelectionDescriptionDataType" type="tns:SelectionDescriptionDataType"/>\n <xs:complexType name="ListOfSelectionDescriptionDataType">\n  <xs:sequence>\n   <xs:element name="SelectionDescriptionDataType" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:SelectionDescriptionDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfSelectionDescriptionDataType" nillable="true" type="tns:ListOfSelectionDescriptionDataType"/>\n <xs:complexType name="SelectionPriceDataType">\n  <xs:sequence>\n   <xs:element name="SelectionId" maxOccurs="1" minOccurs="0" type="xs:string"/>\n   <xs:element name="Price" maxOccurs="1" minOccurs="0" type="tns:PriceAndContextDataType"/>\n   <xs:element name="OptionsThatMayAffectThePrice" maxOccurs="1" minOccurs="0" type="ua:ListOfString"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="SelectionPriceDataType" type="tns:SelectionPriceDataType"/>\n <xs:complexType name="ListOfSelectionPriceDataType">\n  <xs:sequence>\n   <xs:element name="SelectionPriceDataType" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:SelectionPriceDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfSelectionPriceDataType" nillable="true" type="tns:ListOfSelectionPriceDataType"/>\n <xs:complexType name="SlotConfigurationDataType">\n  <xs:sequence>\n   <xs:element name="SlotIndex" maxOccurs="1" minOccurs="0" type="xs:int"/>\n   <xs:element name="SupportedAssetListIndex" maxOccurs="1" minOccurs="0" type="xs:unsignedInt"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="SlotConfigurationDataType" type="tns:SlotConfigurationDataType"/>\n <xs:complexType name="ListOfSlotConfigurationDataType">\n  <xs:sequence>\n   <xs:element name="SlotConfigurationDataType" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:SlotConfigurationDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfSlotConfigurationDataType" nillable="true" type="tns:ListOfSlotConfigurationDataType"/>\n <xs:complexType name="TransactionProgressDataType">\n  <xs:sequence>\n   <xs:element name="TransactionId" maxOccurs="1" minOccurs="0" type="xs:unsignedLong"/>\n   <xs:element name="Status" maxOccurs="1" minOccurs="0" type="tns:DeliveryAndPaymentStatusEnum"/>\n   <xs:element name="TransactionFinished" maxOccurs="1" minOccurs="0" type="xs:boolean"/>\n   <xs:element name="PaymentMode" maxOccurs="1" minOccurs="0" type="xs:string"/>\n   <xs:element name="UserId" maxOccurs="1" minOccurs="0" type="xs:string"/>\n   <xs:element name="UsedPrice" maxOccurs="1" minOccurs="0" type="tns:PriceAndContextDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="TransactionProgressDataType" type="tns:TransactionProgressDataType"/>\n <xs:complexType name="ListOfTransactionProgressDataType">\n  <xs:sequence>\n   <xs:element name="TransactionProgressDataType" maxOccurs="unbounded" minOccurs="0" nillable="true" type="tns:TransactionProgressDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfTransactionProgressDataType" nillable="true" type="tns:ListOfTransactionProgressDataType"/>\n</xs:schema>\n',
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6206",
    browseName="EnumStrings",
    parent="ns=unattended_retail;i=3029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("Idle"), o6.LocalizedText("Ongoing"), o6.LocalizedText("SuccessfullyFinished"), o6.LocalizedText("Failed")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6207",
    browseName="EnumStrings",
    parent="ns=unattended_retail;i=3032",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        o6.LocalizedText("Idle"),
        o6.LocalizedText("Ongoing"),
        o6.LocalizedText("SuccessfullyFinished"),
        o6.LocalizedText("Failed"),
        o6.LocalizedText("Failed_NoCommunication"),
        o6.LocalizedText("Failed_NotEnoughCredit"),
    ],
)
unattended_retail_objtypes.PaymentDeviceType(
    nodeId="ns=unattended_retail;i=5075",
    browseName="ns=unattended_retail;<PaymentDevice>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6201", browseName="ns=unattended_retail;IsEmulated", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=5077"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=unattended_retail;i=6209",
                browseName="ns=unattended_retail;Status",
                dataType=unattended_retail_datypes.PaymentModeOrDeviceStatusEnum,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(unattended_retail_objtypes.PaymentDevicesType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=5075"])
unattended_retail_objtypes.PaymentDeviceType(
    nodeId="ns=unattended_retail;i=5078",
    browseName="ns=unattended_retail;<PaymentDevice>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=unattended_retail;i=6202", browseName="ns=unattended_retail;IsEmulated", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=5079"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=unattended_retail;i=6210",
                browseName="ns=unattended_retail;Status",
                dataType=unattended_retail_datypes.PaymentModeOrDeviceStatusEnum,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
unattended_retail_objtypes.PaymentDevicesType(
    nodeId="ns=unattended_retail;i=5042",
    browseName="ns=unattended_retail;PaymentDevices",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=unattended_retail;i=5078"])],
)
o6.reference(unattended_retail_objtypes.PaymentServiceType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=5042"])


ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6021",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="SelectionId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Options", dataType=o6.NodeId("ns=unattended_retail;i=3006"), valueRank=1, arrayDimensions=[0], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="TransactionId", dataType=o6.NodeId("i=9"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6153",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=unattended_retail;i=7002",
    browseName="ns=unattended_retail;Deliver",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6021"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6153"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6022",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="UserId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="PaymentMode", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Selection", dataType=o6.NodeId("ns=unattended_retail;i=3033"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Price", dataType=o6.NodeId("ns=unattended_retail;i=3005"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6058",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="TransactionId", dataType=o6.NodeId("i=9"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=unattended_retail;i=7004",
    browseName="ns=unattended_retail;DeliverRequest",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6022"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6058"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6118",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="UserId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="PaymentMode", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Selection", dataType=o6.NodeId("ns=unattended_retail;i=3033"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6119",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="PriceInformation", dataType=o6.NodeId("ns=unattended_retail;i=3014"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=unattended_retail;i=7010",
    browseName="ns=unattended_retail;GetPriceForOneSelection",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6118"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6119"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6120",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="UserId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="PaymentMode", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="MachineEngineProductInstanceUri", dataType=o6.NodeId("i=23751"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="SelectionListVersion", dataType=o6.NodeId("i=24263"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6121",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="PriceInformationList", dataType=o6.NodeId("ns=unattended_retail;i=3027"), valueRank=1, arrayDimensions=[0], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=unattended_retail;i=7011",
    browseName="ns=unattended_retail;GetPriceForSelections",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6120"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6121"]),
)

unattended_retail_objtypes.PriceInformationType(
    nodeId="ns=unattended_retail;i=5060",
    browseName="ns=unattended_retail;PriceInformation",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=unattended_retail;i=7010"]), o6.hasComponent(o6.ns["ns=unattended_retail;i=7011"])],
)
o6.reference(unattended_retail_objtypes.PriceServiceType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=5060"])


ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6122",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="UserId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="PaymentMode", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Selection", dataType=o6.NodeId("ns=unattended_retail;i=3033"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6123",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="PriceInformation", dataType=o6.NodeId("ns=unattended_retail;i=3014"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=unattended_retail;i=7012",
    browseName="ns=unattended_retail;GetPriceForOneSelection",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6122"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6123"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6124",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="UserId", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="PaymentMode", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="MachineEngineProductInstanceUri", dataType=o6.NodeId("i=23751"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="SelectionListVersion", dataType=o6.NodeId("i=24263"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6125",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="PriceInformationList", dataType=o6.NodeId("ns=unattended_retail;i=3027"), valueRank=1, arrayDimensions=[0], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=unattended_retail;i=7013",
    browseName="ns=unattended_retail;GetPriceForSelections",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6124"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6125"]),
)

unattended_retail_objtypes.PriceInformationType(
    nodeId="ns=unattended_retail;i=5061",
    browseName="ns=unattended_retail;PriceInformation",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=unattended_retail;i=7012"]), o6.hasComponent(o6.ns["ns=unattended_retail;i=7013"])],
)
o6.reference(unattended_retail_objtypes.PaymentServiceType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=5061"])


ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6128",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RequestedState", dataType=o6.NodeId("ns=unattended_retail;i=3039"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(nodeId="ns=unattended_retail;i=7014", browseName="ns=unattended_retail;RequestStatusChange", inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6128"]))

unattended_retail_objtypes.PaymentServiceStatusType(
    nodeId="ns=unattended_retail;i=5064",
    browseName="ns=unattended_retail;Status",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=unattended_retail;i=6129", browseName="ns=unattended_retail;Status", dataType=unattended_retail_datypes.PaymentServiceStatusEnum
            )
        ),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=7014"]),
    ],
)
o6.reference(unattended_retail_objtypes.PaymentServiceType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=5064"])


ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6155",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TransactionId", dataType=o6.NodeId("i=9"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6157",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=unattended_retail;i=7017",
    browseName="ns=unattended_retail;StopDelivery",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6155"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6157"]),
)

unattended_retail_objtypes.MachineEngineDeliveryType(
    nodeId="ns=unattended_retail;i=5004",
    browseName="ns=unattended_retail;Delivery",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=unattended_retail;i=6038",
                browseName="ns=unattended_retail;DeliveryProgress",
                dataType=unattended_retail_datypes.DeliveryProgressDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=unattended_retail;i=6065",
                browseName="ns=unattended_retail;DeliveryRequests",
                dataType=unattended_retail_datypes.DeliveryRequestDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=7002"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=7017"]),
    ],
)
o6.reference(unattended_retail_objtypes.MachineEngineType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=5004"])


ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6162",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TransactionId", dataType=o6.NodeId("i=9"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=unattended_retail;i=6163",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=unattended_retail;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=unattended_retail;i=7019",
    browseName="ns=unattended_retail;CancelDeliverRequest",
    inputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6162"]),
    outputArgs=o6.hasProperty(o6.ns["ns=unattended_retail;i=6163"]),
)

unattended_retail_objtypes.PaymentServiceDeliveryType(
    nodeId="ns=unattended_retail;i=5016",
    browseName="ns=unattended_retail;Delivery",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=unattended_retail;i=6063",
                browseName="ns=unattended_retail;TransactionProgress",
                dataType=unattended_retail_datypes.TransactionProgressDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=7004"]),
        o6.hasComponent(o6.ns["ns=unattended_retail;i=7019"]),
    ],
)
o6.reference(unattended_retail_objtypes.PaymentServiceType, ns0.reftypes.HasComponent, o6.ns["ns=unattended_retail;i=5016"])


del Any, TYPE_CHECKING, uuid, o6, di, ns0, unattended_retail_datypes, unattended_retail_objtypes
