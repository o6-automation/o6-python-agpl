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

"""Generated OPC UA fx_ac namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.fx_data as fx_data
import o6.ns.ns0 as ns0
from . import reftypes as fx_ac_reftypes
from . import datatypes as fx_ac_datypes
from . import vartypes as fx_ac_vartypes
from . import objtypes as fx_ac_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_ac;i=60", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_ac;i=62", browseName="Default XML")
o6.hasEncoding(fx_ac_datypes.ApplicationIdentifierDataType, o6.ns["ns=fx_ac;i=62"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_ac;i=69", browseName="Default JSON")
o6.hasEncoding(fx_ac_datypes.ApplicationIdentifierDataType, o6.ns["ns=fx_ac;i=69"])
fx_ac_objtypes.FunctionalEntityType(nodeId="ns=fx_ac;i=82", browseName="ns=fx_ac;<FunctionalEntity>", modellingRule="OptionalPlaceholder")
ns0.objtypes.FolderType(nodeId="ns=fx_ac;i=67", browseName="ns=fx_ac;FunctionalEntities", modellingRule="Mandatory", references=[o6.organizes(o6.ns["ns=fx_ac;i=82"])])
o6.reference(fx_ac_objtypes.AutomationComponentType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=67"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_ac;i=91", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_ac;i=92", browseName="Default XML")
o6.hasEncoding(fx_ac_datypes.FxVersion, o6.ns["ns=fx_ac;i=92"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_ac;i=93", browseName="Default JSON")
o6.hasEncoding(fx_ac_datypes.FxVersion, o6.ns["ns=fx_ac;i=93"])
fx_ac_objtypes.FxAssetType(
    nodeId="ns=fx_ac;i=73",
    browseName="ns=fx_ac;<Asset>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=200", browseName="ns=di;ManufacturerUri", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=201", browseName="ns=di;ProductCode", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
)
o6.reference(o6.ns["ns=fx_ac;i=82"], "i=25261", o6.ns["ns=fx_ac;i=73"])
ns0.objtypes.FolderType(nodeId="ns=fx_ac;i=68", browseName="ns=fx_ac;Assets", modellingRule="Mandatory", references=[o6.organizes(o6.ns["ns=fx_ac;i=73"])])
o6.reference(fx_ac_objtypes.AutomationComponentType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=68"])
fx_ac_objtypes.ClampType(
    nodeId="ns=fx_ac;i=94",
    browseName="ns=fx_ac;<Clamp>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=220", browseName="ns=fx_ac;Name", dataType=o6.String, accessLevel=3, userAccessLevel=1))],
)
o6.reference(fx_ac_objtypes.ClampBlockType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=94"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=fx_ac;i=1250",
    browseName="ns=fx_ac;Kind",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fx_ac;i=1251",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[2],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Screw"), description=o6.LocalizedText("Screw")),
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Thumb"), description=o6.LocalizedText("Thumb")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=1252", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_ac_objtypes.ClampBlockType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=1250"])
fx_ac_objtypes.AssetConnectorType(
    nodeId="ns=fx_ac;i=76",
    browseName="ns=fx_ac;<AssetConnector>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=1253", browseName="ns=fx_ac;Name", dataType=o6.String, accessLevel=3, userAccessLevel=1))],
    _allow_abstract=True,
)
ns0.objtypes.FolderType(nodeId="ns=fx_ac;i=72", browseName="ns=fx_ac;Connectors", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=fx_ac;i=76"])])
o6.reference(fx_ac_objtypes.FxAssetType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=72"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=fx_ac;i=215",
    browseName="ns=fx_ac;Kind",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fx_ac;i=1254",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[2],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Screw"), description=o6.LocalizedText("Screw")),
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Thumb"), description=o6.LocalizedText("Thumb")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=1255", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_ac_objtypes.ClampType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=215"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_ac;i=5003", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_ac;i=5004", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_ac;i=5005", browseName="Default XML")
o6.hasEncoding(fx_ac_datypes.AggregatedHealthDataType, o6.ns["ns=fx_ac;i=5005"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_ac;i=5006", browseName="Default JSON")
o6.hasEncoding(fx_ac_datypes.AggregatedHealthDataType, o6.ns["ns=fx_ac;i=5006"])
fx_ac_objtypes.FunctionalEntityType(nodeId="ns=fx_ac;i=5011", browseName="ns=fx_ac;<SubFunctionalEntity>", modellingRule="OptionalPlaceholder")
o6.reference(fx_ac_objtypes.FunctionalEntityType, fx_ac_reftypes.HasSubFunctionalEntity, o6.ns["ns=fx_ac;i=5011"])
fx_ac_objtypes.OutputsFolderType(nodeId="ns=fx_ac;i=5014", browseName="ns=fx_ac;<OutputGroup>", modellingRule="OptionalPlaceholder")
o6.reference(fx_ac_objtypes.OutputsFolderType, fx_ac_reftypes.HasOutputGroup, o6.ns["ns=fx_ac;i=5014"])
fx_ac_objtypes.InputsFolderType(nodeId="ns=fx_ac;i=5016", browseName="ns=fx_ac;<InputGroup>", modellingRule="OptionalPlaceholder")
o6.reference(fx_ac_objtypes.InputsFolderType, fx_ac_reftypes.HasInputGroup, o6.ns["ns=fx_ac;i=5016"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_ac;i=5021", browseName="Default XML")
o6.hasEncoding(fx_ac_datypes.ApplicationId, o6.ns["ns=fx_ac;i=5021"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_ac;i=5024", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_ac;i=5025", browseName="Default XML")
o6.hasEncoding(fx_ac_datypes.PublisherQosDataType, o6.ns["ns=fx_ac;i=5025"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_ac;i=5026", browseName="Default JSON")
o6.hasEncoding(fx_ac_datypes.PublisherQosDataType, o6.ns["ns=fx_ac;i=5026"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_ac;i=5027", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_ac;i=5028", browseName="Default XML")
o6.hasEncoding(fx_ac_datypes.SubscriberQosDataType, o6.ns["ns=fx_ac;i=5028"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_ac;i=5029", browseName="Default JSON")
o6.hasEncoding(fx_ac_datypes.SubscriberQosDataType, o6.ns["ns=fx_ac;i=5029"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fx_ac;i=5038", browseName="Default JSON")
o6.hasEncoding(fx_ac_datypes.ApplicationId, o6.ns["ns=fx_ac;i=5038"])
fx_ac_objtypes.ConfigurationDataFolderType(
    nodeId="ns=fx_ac;i=5031",
    browseName="ns=fx_ac;ConfigurationData",
    modellingRule="Optional",
    references=[
        o6.organizes(di.objtypes.FunctionalGroupType(nodeId="ns=fx_ac;i=5055", browseName="ns=di;Configuration")),
        o6.organizes(di.objtypes.FunctionalGroupType(nodeId="ns=fx_ac;i=5056", browseName="ns=di;Tuning")),
    ],
)
o6.reference(fx_ac_objtypes.FunctionalEntityType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5031"])
ns0.objtypes.FolderType(
    nodeId="ns=fx_ac;i=5042",
    browseName="ns=fx_ac;Connectors",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            fx_ac_objtypes.AssetConnectorType(nodeId="ns=fx_ac;i=5060", browseName="ns=fx_ac;<AssetConnector>", modellingRule="OptionalPlaceholder", _allow_abstract=True)
        )
    ],
)
o6.reference(fx_ac_objtypes.IAssetExtensionsType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5042"])
ns0.objtypes.FolderType(
    nodeId="ns=fx_ac;i=5073",
    browseName="ns=fx_ac;Descriptors",
    modellingRule="Mandatory",
    references=[o6.hasComponent(fx_ac_objtypes.AcDescriptorType(nodeId="ns=fx_ac;i=5059", browseName="ns=fx_ac;<Descriptor>", modellingRule="OptionalPlaceholder"))],
)
o6.reference(fx_ac_objtypes.AutomationComponentType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5073"])
fx_ac_objtypes.ConfigurationDataFolderType(
    nodeId="ns=fx_ac;i=5104",
    browseName="ns=fx_ac;ConfigurationData",
    modellingRule="Optional",
    references=[
        o6.organizes(di.objtypes.FunctionalGroupType(nodeId="ns=fx_ac;i=5048", browseName="ns=di;Tuning")),
        o6.organizes(di.objtypes.FunctionalGroupType(nodeId="ns=fx_ac;i=5049", browseName="ns=di;Configuration")),
    ],
)
o6.reference(fx_ac_objtypes.IFunctionalEntityType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5104"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashFXSlashACSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=fx_ac;i=5001",
    browseName="ns=fx_ac;http://opcfoundation.org/UA/FX/AC/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6001", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6002", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2026-07-22T18:52:23Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6003", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/FX/AC/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6004", browseName="NamespaceVersion", dataType=o6.String, value="1.00.04")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fx_ac;i=6005", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fx_ac;i=6006", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["0:15000"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6007", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=fx_ac;i=6008",
    browseName="ns=fx_ac;Kind",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6009", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6010", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_ac_objtypes.SocketType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=6008"])
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6011",
    browseName="EnumValues",
    parent="ns=fx_ac;i=3001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Screw"), description=o6.LocalizedText("This is a screw connector")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Thumb"), description=o6.LocalizedText("This is a thumb connector")),
    ],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_ac;i=6016", browseName="ns=fx_ac;AggregatedHealthDataType", dataType=o6.String, value="AggregatedHealthDataType")
o6.reference(o6.ns["ns=fx_ac;i=5004"], "i=39", o6.ns["ns=fx_ac;i=6016"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_ac;i=6017", browseName="ns=fx_ac;AggregatedHealthDataType", dataType=o6.String, value="//xs:element[@name='AggregatedHealthDataType']"
)
o6.reference(o6.ns["ns=fx_ac;i=5005"], "i=39", o6.ns["ns=fx_ac;i=6017"])
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6018",
    browseName="OptionSetValues",
    parent="ns=fx_ac;i=3004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("CommInitial"), o6.LocalizedText("CommPreOperational"), o6.LocalizedText("CommError")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6019",
    browseName="OptionSetValues",
    parent="ns=fx_ac;i=3005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("DeviceFailure"), o6.LocalizedText("DeviceCheckFunction"), o6.LocalizedText("DeviceMaintenanceRequired"), o6.LocalizedText("DeviceOffSpec")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6029",
    browseName="EnumStrings",
    parent="ns=fx_ac;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("RJ45"), o6.LocalizedText("M12")],
)
fx_ac_objtypes.PublisherCapabilitiesType(
    nodeId="ns=fx_ac;i=5007",
    browseName="ns=fx_ac;PublisherCapabilities",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6030", browseName="ns=fx_ac;PreconfiguredDataSetOnly", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6031",
                browseName="ns=fx_ac;PreconfiguredPublishedDataSets",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6033",
                browseName="ns=fx_ac;SupportedPublishingIntervals",
                dataType=fx_data.datatypes.IntervalRange,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6034",
                browseName="ns=fx_ac;SupportedQos",
                dataType=fx_ac_datypes.PublisherQosDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(fx_ac_objtypes.IFunctionalEntityType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5007"])
fx_ac_objtypes.SubscriberCapabilitiesType(
    nodeId="ns=fx_ac;i=5008",
    browseName="ns=fx_ac;SubscriberCapabilities",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6035", browseName="ns=fx_ac;PreconfiguredDataSetOnly", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6037",
                browseName="ns=fx_ac;PreconfiguredSubscribedDataSets",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6038",
                browseName="ns=fx_ac;SupportedMessageReceiveTimeouts",
                dataType=fx_data.datatypes.IntervalRange,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6039",
                browseName="ns=fx_ac;SupportedPublishingIntervals",
                dataType=fx_data.datatypes.IntervalRange,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6040",
                browseName="ns=fx_ac;SupportedQos",
                dataType=fx_ac_datypes.SubscriberQosDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(fx_ac_objtypes.IFunctionalEntityType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5008"])
fx_ac_objtypes.PublisherCapabilitiesType(
    nodeId="ns=fx_ac;i=5009",
    browseName="ns=fx_ac;PublisherCapabilities",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6032", browseName="ns=fx_ac;PreconfiguredDataSetOnly", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6041",
                browseName="ns=fx_ac;PreconfiguredPublishedDataSets",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6042",
                browseName="ns=fx_ac;SupportedPublishingIntervals",
                dataType=fx_data.datatypes.IntervalRange,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6043",
                browseName="ns=fx_ac;SupportedQos",
                dataType=fx_ac_datypes.PublisherQosDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(fx_ac_objtypes.AutomationComponentType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5009"])
fx_ac_objtypes.SubscriberCapabilitiesType(
    nodeId="ns=fx_ac;i=5010",
    browseName="ns=fx_ac;SubscriberCapabilities",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6036", browseName="ns=fx_ac;PreconfiguredDataSetOnly", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6044",
                browseName="ns=fx_ac;PreconfiguredSubscribedDataSets",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6045",
                browseName="ns=fx_ac;SupportedMessageReceiveTimeouts",
                dataType=fx_data.datatypes.IntervalRange,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6046",
                browseName="ns=fx_ac;SupportedPublishingIntervals",
                dataType=fx_data.datatypes.IntervalRange,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6047",
                browseName="ns=fx_ac;SupportedQos",
                dataType=fx_ac_datypes.SubscriberQosDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(fx_ac_objtypes.AutomationComponentType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5010"])
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6050",
    browseName="EnumValues",
    parent="ns=fx_ac;i=3007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("Initial"), description=o6.LocalizedText("Initial status of the logical connection. No communication-model objects referenced.")
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("Ready"),
            description=o6.LocalizedText("Logical connection is ready to operate, Communication-model objects are referenced but not enabled."),
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("PreOperational"),
            description=o6.LocalizedText("PreOperational status of the logical connection, Data output is active, but no input data received."),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("Operational"),
            description=o6.LocalizedText("Operational status of the logical connection, Data output is active, and input data has been received."),
        ),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Error"), description=o6.LocalizedText("The logical connection has encountered an Error.")),
    ],
)
fx_ac_objtypes.PublisherCapabilitiesType(
    nodeId="ns=fx_ac;i=5012",
    browseName="ns=fx_ac;PublisherCapabilities",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6054", browseName="ns=fx_ac;PreconfiguredDataSetOnly", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6057",
                browseName="ns=fx_ac;PreconfiguredPublishedDataSets",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6058",
                browseName="ns=fx_ac;SupportedPublishingIntervals",
                dataType=fx_data.datatypes.IntervalRange,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6059",
                browseName="ns=fx_ac;SupportedQos",
                dataType=fx_ac_datypes.PublisherQosDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(fx_ac_objtypes.FunctionalEntityType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5012"])
fx_ac_objtypes.SubscriberCapabilitiesType(
    nodeId="ns=fx_ac;i=5013",
    browseName="ns=fx_ac;SubscriberCapabilities",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6055", browseName="ns=fx_ac;PreconfiguredDataSetOnly", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6060",
                browseName="ns=fx_ac;PreconfiguredSubscribedDataSets",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6061",
                browseName="ns=fx_ac;SupportedMessageReceiveTimeouts",
                dataType=fx_data.datatypes.IntervalRange,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6062",
                browseName="ns=fx_ac;SupportedPublishingIntervals",
                dataType=fx_data.datatypes.IntervalRange,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6063",
                browseName="ns=fx_ac;SupportedQos",
                dataType=fx_ac_datypes.SubscriberQosDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(fx_ac_objtypes.FunctionalEntityType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5013"])
fx_ac_objtypes.SubscriberCapabilitiesType(
    nodeId="ns=fx_ac;i=5017",
    browseName="ns=fx_ac;SubscriberCapabilities",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6064", browseName="ns=fx_ac;PreconfiguredDataSetOnly", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6065",
                browseName="ns=fx_ac;PreconfiguredSubscribedDataSets",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6066",
                browseName="ns=fx_ac;SupportedMessageReceiveTimeouts",
                dataType=fx_data.datatypes.IntervalRange,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6067",
                browseName="ns=fx_ac;SupportedPublishingIntervals",
                dataType=fx_data.datatypes.IntervalRange,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6068",
                browseName="ns=fx_ac;SupportedQos",
                dataType=fx_ac_datypes.SubscriberQosDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(fx_ac_objtypes.InputsFolderType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5017"])
fx_ac_vartypes.AggregatedHealthType(
    nodeId="ns=fx_ac;i=6048",
    browseName="ns=fx_ac;AggregatedHealth",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6051", browseName="ns=fx_ac;AggregatedDeviceHealth", dataType=fx_ac_datypes.DeviceHealthOptionSet)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6070", browseName="ns=fx_ac;AggregatedOperationalHealth", dataType=fx_ac_datypes.OperationalHealthOptionSet)
        ),
    ],
    dataType=fx_ac_datypes.AggregatedHealthDataType,
    value=fx_ac_datypes.AggregatedHealthDataType(
        aggregatedDeviceHealth=fx_ac_datypes.DeviceHealthOptionSet(0), aggregatedOperationalHealth=fx_ac_datypes.OperationalHealthOptionSet(0)
    ),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(fx_ac_objtypes.AutomationComponentType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=6048"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_ac;i=6071", browseName="ns=fx_ac;ApplicationId", dataType=o6.String, value="ApplicationId")
o6.reference(o6.ns["ns=fx_ac;i=5003"], "i=39", o6.ns["ns=fx_ac;i=6071"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_ac;i=6072", browseName="ns=fx_ac;ApplicationId", dataType=o6.String, value="//xs:element[@name='ApplicationId']")
o6.reference(o6.ns["ns=fx_ac;i=5021"], "i=39", o6.ns["ns=fx_ac;i=6072"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_ac;i=6074", browseName="ns=fx_ac;FxVersion", dataType=o6.String, value="FxVersion")
o6.reference(o6.ns["ns=fx_ac;i=91"], "i=39", o6.ns["ns=fx_ac;i=6074"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_ac;i=6075", browseName="ns=fx_ac;FxVersion", dataType=o6.String, value="//xs:element[@name='FxVersion']")
o6.reference(o6.ns["ns=fx_ac;i=92"], "i=39", o6.ns["ns=fx_ac;i=6075"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_ac;i=6082", browseName="ns=fx_ac;ApplicationIdentifierDataType", dataType=o6.String, value="ApplicationIdentifierDataType")
o6.reference(o6.ns["ns=fx_ac;i=60"], "i=39", o6.ns["ns=fx_ac;i=6082"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fx_ac;i=6083", browseName="ns=fx_ac;ApplicationIdentifierDataType", dataType=o6.String, value="//xs:element[@name='ApplicationIdentifierDataType']"
)
o6.reference(o6.ns["ns=fx_ac;i=62"], "i=39", o6.ns["ns=fx_ac;i=6083"])
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6084",
    browseName="OptionSetValues",
    parent="ns=fx_ac;i=3010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[20],
    value=[
        o6.LocalizedText(),
        o6.LocalizedText(),
        o6.LocalizedText(),
        o6.LocalizedText(),
        o6.LocalizedText(),
        o6.LocalizedText(),
        o6.LocalizedText(),
        o6.LocalizedText(),
        o6.LocalizedText(),
        o6.LocalizedText(),
        o6.LocalizedText(),
        o6.LocalizedText(),
        o6.LocalizedText(),
        o6.LocalizedText(),
        o6.LocalizedText(),
        o6.LocalizedText(),
        o6.LocalizedText("OperationalWarning"),
        o6.LocalizedText("OperationalError"),
        o6.LocalizedText("SubOperationalWarning"),
        o6.LocalizedText("SubOperationalError"),
    ],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_ac;i=6085", browseName="ns=fx_ac;PublisherQosDataType", dataType=o6.String, value="PublisherQosDataType")
o6.reference(o6.ns["ns=fx_ac;i=5024"], "i=39", o6.ns["ns=fx_ac;i=6085"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_ac;i=6086", browseName="ns=fx_ac;PublisherQosDataType", dataType=o6.String, value="//xs:element[@name='PublisherQosDataType']")
o6.reference(o6.ns["ns=fx_ac;i=5025"], "i=39", o6.ns["ns=fx_ac;i=6086"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_ac;i=6087", browseName="ns=fx_ac;SubscriberQosDataType", dataType=o6.String, value="SubscriberQosDataType")
o6.reference(o6.ns["ns=fx_ac;i=5027"], "i=39", o6.ns["ns=fx_ac;i=6087"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fx_ac;i=6088", browseName="ns=fx_ac;SubscriberQosDataType", dataType=o6.String, value="//xs:element[@name='SubscriberQosDataType']")
o6.reference(o6.ns["ns=fx_ac;i=5028"], "i=39", o6.ns["ns=fx_ac;i=6088"])
fx_ac_objtypes.ConnectionEndpointType(
    nodeId="ns=fx_ac;i=1077",
    browseName="ns=fx_ac;<ConnectionEndpoint>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=1309", browseName="ns=fx_ac;IsPersistent", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=1331", browseName="ns=fx_ac;Status", dataType=fx_ac_datypes.ConnectionEndpointStatusEnum)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6073", browseName="ns=fx_ac;CleanupTimeout", dataType=ns0.datatypes.Duration, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6092", browseName="ns=fx_ac;RelatedEndpoint", dataType=fx_data.datatypes.RelatedEndpointDataType, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
    _allow_abstract=True,
)
o6.reference(fx_ac_objtypes.ConnectionEndpointsFolderType, fx_ac_reftypes.HasConnectionEndpoint, o6.ns["ns=fx_ac;i=1077"])
fx_ac_objtypes.PublisherCapabilitiesType(
    nodeId="ns=fx_ac;i=5015",
    browseName="ns=fx_ac;PublisherCapabilities",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6097", browseName="ns=fx_ac;PreconfiguredDataSetOnly", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6098",
                browseName="ns=fx_ac;PreconfiguredPublishedDataSets",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6099",
                browseName="ns=fx_ac;SupportedPublishingIntervals",
                dataType=fx_data.datatypes.IntervalRange,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=fx_ac;i=6100",
                browseName="ns=fx_ac;SupportedQos",
                dataType=fx_ac_datypes.PublisherQosDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(fx_ac_objtypes.OutputsFolderType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5015"])
fx_ac_objtypes.FunctionalEntityCapabilitiesType(
    nodeId="ns=fx_ac;i=5039",
    browseName="ns=fx_ac;Capabilities",
    modellingRule="Optional",
    references=[
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6121", browseName="ns=fx_ac;FeedbackSignalRequired", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1),
            "ns=fx_ac;i=4002",
        )
    ],
)
o6.reference(fx_ac_objtypes.IFunctionalEntityType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5039"])
fx_ac_objtypes.FunctionalEntityCapabilitiesType(
    nodeId="ns=fx_ac;i=5040",
    browseName="ns=fx_ac;Capabilities",
    modellingRule="Optional",
    references=[
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6122", browseName="ns=fx_ac;FeedbackSignalRequired", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1),
            "ns=fx_ac;i=4002",
        )
    ],
)
o6.reference(fx_ac_objtypes.FunctionalEntityType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5040"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=fx_ac;i=5045",
    browseName="ns=di;Diagnostics",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6131", browseName="ns=fx_ac;OperationalConnectionCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6132", browseName="ns=fx_ac;ExistingConnectionCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6133", browseName="ns=fx_ac;ErrorConnectionCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6134", browseName="ns=fx_ac;FailedConnectionCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6135", browseName="ns=fx_ac;CleanedUpConnectionCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6136", browseName="ns=fx_ac;TotalEstablishAttemptsCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6137", browseName="ns=fx_ac;FailedEstablishAttemptsCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6138", browseName="ns=fx_ac;FailedVerificationCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
    ],
)
o6.reference(fx_ac_objtypes.IFunctionalEntityType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5045"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=fx_ac;i=5050",
    browseName="ns=di;Diagnostics",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6139", browseName="ns=fx_ac;UpTime", dataType=ns0.datatypes.Duration, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6140", browseName="ns=fx_ac;CurrentCPUUtilization", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6141", browseName="ns=fx_ac;MaxCPUUtilization", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6142", browseName="ns=fx_ac;CurrentMemoryUtilization", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6143", browseName="ns=fx_ac;MaxMemoryUtilization", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
        ),
    ],
)
o6.reference(fx_ac_objtypes.FxAssetType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5050"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=fx_ac;i=5053",
    browseName="ns=di;Diagnostics",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6144", browseName="ns=fx_ac;OperationalConnectionCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6145", browseName="ns=fx_ac;ExistingConnectionCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6146", browseName="ns=fx_ac;ErrorConnectionCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6147", browseName="ns=fx_ac;FailedConnectionCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6148", browseName="ns=fx_ac;CleanedUpConnectionCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6149", browseName="ns=fx_ac;TotalEstablishAttemptsCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6150", browseName="ns=fx_ac;FailedEstablishAttemptsCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6151", browseName="ns=fx_ac;FailedVerificationCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
    ],
)
o6.reference(fx_ac_objtypes.FunctionalEntityType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5053"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=fx_ac;i=5057",
    browseName="ns=di;Diagnostics",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6153", browseName="ns=fx_ac;CreationTime", dataType=o6.DateTime, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6154", browseName="ns=fx_ac;ModificationTime", dataType=o6.DateTime, accessLevel=3, userAccessLevel=1)
        ),
    ],
)
o6.reference(fx_ac_objtypes.ConnectionEndpointType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5057"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=fx_ac;i=5044",
    browseName="ns=di;Diagnostics",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6155", browseName="ns=fx_ac;UpTime", dataType=ns0.datatypes.Duration, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6156", browseName="ns=fx_ac;CurrentCPUUtilization", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6157", browseName="ns=fx_ac;MaxCPUUtilization", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6158", browseName="ns=fx_ac;CurrentMemoryUtilization", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6159", browseName="ns=fx_ac;MaxMemoryUtilization", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
        ),
    ],
)
o6.reference(fx_ac_objtypes.IAssetExtensionsType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5044"])
opcDotUaDotFXDotAC = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=fx_ac;i=6012",
    browseName="ns=fx_ac;Opc.Ua.FX.AC",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/FX/AC/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6013", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/FX/AC/")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=fx_ac;i=6160",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=fx_ac;i=6016"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=6071"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=6074"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=6082"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=6085"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=6087"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/FX/AC/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" DefaultByteOrder="LittleEndian" xmlns:tns="http://opcfoundation.org/UA/FX/AC/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="AggregatedHealthDataType">\n  <opc:Field Name="AggregatedDeviceHealth" TypeName="tns:DeviceHealthOptionSet"/>\n  <opc:Field Name="AggregatedOperationalHealth" TypeName="tns:OperationalHealthOptionSet"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ApplicationIdentifierDataType">\n  <opc:Field Name="Name" TypeName="ua:LocalizedText"/>\n  <opc:Field Name="UniqueIdentifier" TypeName="tns:ApplicationId"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="FxVersion">\n  <opc:Field Name="Major" TypeName="opc:UInt16"/>\n  <opc:Field Name="Minor" TypeName="opc:UInt16"/>\n  <opc:Field Name="Build" TypeName="opc:UInt16"/>\n  <opc:Field Name="SubBuild" TypeName="opc:UInt16"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="PublisherQosDataType">\n  <opc:Field Name="QosCategory" TypeName="opc:CharArray"/>\n  <opc:Field Name="NoOfDatagramQos" TypeName="opc:Int32"/>\n  <opc:Field Name="DatagramQos" TypeName="ua:ExtensionObject" LengthField="NoOfDatagramQos"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="SubscriberQosDataType">\n  <opc:Field Name="QosCategory" TypeName="opc:CharArray"/>\n  <opc:Field Name="NoOfDatagramQos" TypeName="opc:Int32"/>\n  <opc:Field Name="DatagramQos" TypeName="ua:ExtensionObject" LengthField="NoOfDatagramQos"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:Union" Name="ApplicationId">\n  <opc:Field Name="SwitchField" TypeName="opc:UInt32"/>\n  <opc:Field Name="IdNumeric" SwitchValue="1" TypeName="opc:UInt32" SwitchField="SwitchField"/>\n  <opc:Field Name="IdString" SwitchValue="2" TypeName="opc:CharArray" SwitchField="SwitchField"/>\n  <opc:Field Name="IdGuid" SwitchValue="3" TypeName="opc:Guid" SwitchField="SwitchField"/>\n  <opc:Field Name="IdByteString" SwitchValue="4" TypeName="opc:ByteString" SwitchField="SwitchField"/>\n </opc:StructuredType>\n <opc:EnumeratedType Name="ClampKindEnum" LengthInBits="32">\n  <opc:EnumeratedValue Value="0" Name="Screw"/>\n  <opc:EnumeratedValue Value="1" Name="Thumb"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType Name="ConnectionEndpointStatusEnum" LengthInBits="32">\n  <opc:Documentation>This enumeration defines the values of the FlcConnectionStatus of an FlcConnectionEndpointType. </opc:Documentation>\n  <opc:EnumeratedValue Value="0" Name="Initial"/>\n  <opc:EnumeratedValue Value="1" Name="Ready"/>\n  <opc:EnumeratedValue Value="2" Name="PreOperational"/>\n  <opc:EnumeratedValue Value="3" Name="Operational"/>\n  <opc:EnumeratedValue Value="4" Name="Error"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType Name="SocketKindEnum" LengthInBits="32">\n  <opc:EnumeratedValue Value="0" Name="RJ45"/>\n  <opc:EnumeratedValue Value="1" Name="M12"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType IsOptionSet="true" Name="CommHealthOptionSet" LengthInBits="16">\n  <opc:EnumeratedValue Value="0" Name="CommInitial"/>\n  <opc:EnumeratedValue Value="1" Name="CommPreOperational"/>\n  <opc:EnumeratedValue Value="2" Name="CommError"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType IsOptionSet="true" Name="DeviceHealthOptionSet" LengthInBits="16">\n  <opc:EnumeratedValue Value="0" Name="DeviceFailure"/>\n  <opc:EnumeratedValue Value="1" Name="DeviceCheckFunction"/>\n  <opc:EnumeratedValue Value="2" Name="DeviceMaintenanceRequired"/>\n  <opc:EnumeratedValue Value="3" Name="DeviceOffSpec"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType IsOptionSet="true" Name="OperationalHealthOptionSet" LengthInBits="32">\n  <opc:EnumeratedValue Value="16" Name="OperationalWarning"/>\n  <opc:EnumeratedValue Value="17" Name="OperationalError"/>\n  <opc:EnumeratedValue Value="18" Name="SubOperationalWarning"/>\n  <opc:EnumeratedValue Value="19" Name="SubOperationalError"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
opcDotUaDotFXDotAC_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=fx_ac;i=6014",
    browseName="ns=fx_ac;Opc.Ua.FX.AC",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/FX/AC/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6015", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/FX/AC/Types.xsd")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=fx_ac;i=6161",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=fx_ac;i=6017"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=6072"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=6075"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=6083"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=6086"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=6088"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema targetNamespace="http://opcfoundation.org/UA/FX/AC/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://opcfoundation.org/UA/FX/AC/Types.xsd" elementFormDefault="qualified">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="ClampKindEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Screw_0"/>\n   <xs:enumeration value="Thumb_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ClampKindEnum" name="ClampKindEnum"/>\n <xs:complexType name="ListOfClampKindEnum">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" minOccurs="0" type="tns:ClampKindEnum" nillable="true" name="ClampKindEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfClampKindEnum" nillable="true" name="ListOfClampKindEnum"/>\n <xs:simpleType name="ConnectionEndpointStatusEnum">\n  <xs:annotation>\n   <xs:documentation>This enumeration defines the values of the FlcConnectionStatus of an FlcConnectionEndpointType. </xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Initial_0"/>\n   <xs:enumeration value="Ready_1"/>\n   <xs:enumeration value="PreOperational_2"/>\n   <xs:enumeration value="Operational_3"/>\n   <xs:enumeration value="Error_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ConnectionEndpointStatusEnum" name="ConnectionEndpointStatusEnum"/>\n <xs:complexType name="ListOfConnectionEndpointStatusEnum">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" minOccurs="0" type="tns:ConnectionEndpointStatusEnum" nillable="true" name="ConnectionEndpointStatusEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfConnectionEndpointStatusEnum" nillable="true" name="ListOfConnectionEndpointStatusEnum"/>\n <xs:simpleType name="SocketKindEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="RJ45_0"/>\n   <xs:enumeration value="M12_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:SocketKindEnum" name="SocketKindEnum"/>\n <xs:complexType name="ListOfSocketKindEnum">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" minOccurs="0" type="tns:SocketKindEnum" nillable="true" name="SocketKindEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSocketKindEnum" nillable="true" name="ListOfSocketKindEnum"/>\n <xs:complexType name="AggregatedHealthDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" minOccurs="0" type="xs:unsignedShort" name="AggregatedDeviceHealth"/>\n   <xs:element maxOccurs="1" minOccurs="0" type="xs:unsignedInt" name="AggregatedOperationalHealth"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:AggregatedHealthDataType" name="AggregatedHealthDataType"/>\n <xs:complexType name="ListOfAggregatedHealthDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" minOccurs="0" type="tns:AggregatedHealthDataType" nillable="true" name="AggregatedHealthDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAggregatedHealthDataType" nillable="true" name="ListOfAggregatedHealthDataType"/>\n <xs:complexType name="ApplicationIdentifierDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" minOccurs="0" type="ua:LocalizedText" name="Name"/>\n   <xs:element maxOccurs="1" minOccurs="0" type="tns:ApplicationId" name="UniqueIdentifier"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ApplicationIdentifierDataType" name="ApplicationIdentifierDataType"/>\n <xs:complexType name="ListOfApplicationIdentifierDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" minOccurs="0" type="tns:ApplicationIdentifierDataType" nillable="true" name="ApplicationIdentifierDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfApplicationIdentifierDataType" nillable="true" name="ListOfApplicationIdentifierDataType"/>\n <xs:complexType name="FxVersion">\n  <xs:sequence>\n   <xs:element maxOccurs="1" minOccurs="0" type="xs:unsignedShort" name="Major"/>\n   <xs:element maxOccurs="1" minOccurs="0" type="xs:unsignedShort" name="Minor"/>\n   <xs:element maxOccurs="1" minOccurs="0" type="xs:unsignedShort" name="Build"/>\n   <xs:element maxOccurs="1" minOccurs="0" type="xs:unsignedShort" name="SubBuild"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:FxVersion" name="FxVersion"/>\n <xs:complexType name="ListOfFxVersion">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" minOccurs="0" type="tns:FxVersion" nillable="true" name="FxVersion"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfFxVersion" nillable="true" name="ListOfFxVersion"/>\n <xs:complexType name="PublisherQosDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" minOccurs="0" type="xs:string" name="QosCategory"/>\n   <xs:element maxOccurs="1" minOccurs="0" type="ua:ListOfExtensionObject" name="DatagramQos"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:PublisherQosDataType" name="PublisherQosDataType"/>\n <xs:complexType name="ListOfPublisherQosDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" minOccurs="0" type="tns:PublisherQosDataType" nillable="true" name="PublisherQosDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPublisherQosDataType" nillable="true" name="ListOfPublisherQosDataType"/>\n <xs:complexType name="SubscriberQosDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="1" minOccurs="0" type="xs:string" name="QosCategory"/>\n   <xs:element maxOccurs="1" minOccurs="0" type="ua:ListOfExtensionObject" name="DatagramQos"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:SubscriberQosDataType" name="SubscriberQosDataType"/>\n <xs:complexType name="ListOfSubscriberQosDataType">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" minOccurs="0" type="tns:SubscriberQosDataType" nillable="true" name="SubscriberQosDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSubscriberQosDataType" nillable="true" name="ListOfSubscriberQosDataType"/>\n <xs:complexType name="ApplicationId">\n  <xs:sequence>\n   <xs:element maxOccurs="1" minOccurs="0" type="xs:unsignedInt" name="SwitchField"/>\n   <xs:choice>\n    <xs:element maxOccurs="1" minOccurs="0" type="xs:unsignedInt" name="IdNumeric"/>\n    <xs:element maxOccurs="1" minOccurs="0" type="xs:string" name="IdString"/>\n    <xs:element maxOccurs="1" minOccurs="0" type="ua:Guid" name="IdGuid"/>\n    <xs:element maxOccurs="1" minOccurs="0" type="xs:base64Binary" name="IdByteString"/>\n   </xs:choice>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ApplicationId" name="ApplicationId"/>\n <xs:complexType name="ListOfApplicationId">\n  <xs:sequence>\n   <xs:element maxOccurs="unbounded" minOccurs="0" type="tns:ApplicationId" nillable="true" name="ApplicationId"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfApplicationId" nillable="true" name="ListOfApplicationId"/>\n</xs:schema>\n',
)
di.objtypes.FunctionalGroupType(
    nodeId="ns=fx_ac;i=5043",
    browseName="ns=di;Diagnostics",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6123", browseName="ns=fx_ac;EstablishCallCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6124", browseName="ns=fx_ac;EstablishCallFailedCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6125", browseName="ns=fx_ac;CloseCallCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6167", browseName="ns=fx_ac;CloseCallFailedCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
        ),
    ],
)
o6.reference(fx_ac_objtypes.AutomationComponentType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5043"])
fx_ac_objtypes.AutomationComponentCapabilitiesType(
    nodeId="ns=fx_ac;i=1066",
    browseName="ns=fx_ac;ComponentCapabilities",
    modellingRule="Mandatory",
    references=[
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6127", browseName="ns=fx_ac;CommandBundleRequired", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1),
            "ns=fx_ac;i=4002",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6128", browseName="ns=fx_ac;MaxConnectionsPerCall", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1),
            "ns=fx_ac;i=4002",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6129", browseName="ns=fx_ac;MaxFunctionalEntities", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1),
            "ns=fx_ac;i=4002",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6130", browseName="ns=fx_ac;MinConnections", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1),
            "ns=fx_ac;i=4002",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6359", browseName="ns=fx_ac;SupportsPersistence", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1),
            "ns=fx_ac;i=4002",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6360", browseName="ns=fx_ac;MaxConnections", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1),
            "ns=fx_ac;i=4002",
        ),
    ],
)
o6.reference(fx_ac_objtypes.AutomationComponentType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=1066"])


ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6337",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7001", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6337"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6338",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6339",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7002", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6338"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6339"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6090",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7003", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6090"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6102",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7004", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6102"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6103",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6104",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7005", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6103"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6104"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6109",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7006", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6109"]))

di.objtypes.LockingServicesType(
    nodeId="ns=fx_ac;i=5034",
    browseName="ns=di;Lock",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6105", browseName="ns=di;Locked", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6106", browseName="ns=di;LockingClient", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6107", browseName="ns=di;LockingUser", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6108", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7003"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7004"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7005"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7006"]),
    ],
)
fx_ac_objtypes.ControlItemFolderType(nodeId="ns=fx_ac;i=5033", browseName="ns=fx_ac;ListToBlock", references=[o6.hasComponent(o6.ns["ns=fx_ac;i=5034"])])


ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6340",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6341",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7007", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6340"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6341"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6343",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6344",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7008", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6343"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6344"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6345",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7009", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6345"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6349",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7010", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6349"]))

ns0.objtypes.FileType(
    nodeId="ns=fx_ac;i=5072",
    browseName="ns=fx_ac;DescriptorFile",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6342", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6346", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6347", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6348", browseName="Writable", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7001"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7002"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7007"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7008"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7009"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7010"]),
    ],
)
o6.reference(fx_ac_objtypes.AcDescriptorType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5072"])


ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6091",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7012", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6091"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6245",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7013", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6245"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6246",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6247",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7014", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6246"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6247"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6252",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7015", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6252"]))

di.objtypes.LockingServicesType(
    nodeId="ns=fx_ac;i=5051",
    browseName="ns=di;Lock",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6248", browseName="ns=di;Locked", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6249", browseName="ns=di;LockingClient", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6250", browseName="ns=di;LockingUser", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6251", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7012"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7013"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7014"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7015"]),
    ],
)
o6.reference(fx_ac_objtypes.ControlItemFolderType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5051"])


ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6253",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7016", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6253"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6264",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7017", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6264"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6265",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6266",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7018", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6265"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6266"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6275",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7019", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6275"]))

di.objtypes.LockingServicesType(
    nodeId="ns=fx_ac;i=5078",
    browseName="ns=di;Lock",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6271", browseName="ns=di;Locked", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6272", browseName="ns=di;LockingClient", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6273", browseName="ns=di;LockingUser", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6274", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7016"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7017"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7018"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7019"]),
    ],
)
fx_ac_objtypes.ControlItemFolderType(nodeId="ns=fx_ac;i=1069", browseName="ns=fx_ac;ListToBlock", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=fx_ac;i=5078"])])
o6.reference(fx_ac_objtypes.ControlGroupType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=1069"])


ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6306",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7020", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6306"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6312",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7021", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6312"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6313",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6314",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7022", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6313"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6314"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6371",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7023", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6371"]))

di.objtypes.LockingServicesType(
    nodeId="ns=fx_ac;i=5080",
    browseName="ns=di;Lock",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6317", browseName="ns=di;Locked", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6368", browseName="ns=di;LockingClient", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6369", browseName="ns=di;LockingUser", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6370", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7020"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7021"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7022"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7023"]),
    ],
)
fx_ac_objtypes.ControlItemFolderType(
    nodeId="ns=fx_ac;i=1070", browseName="ns=fx_ac;ListToRestrict", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=fx_ac;i=5080"])]
)
o6.reference(fx_ac_objtypes.ControlGroupType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=1070"])


ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6110",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7027",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7027", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6110"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6111",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7028",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7028", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6111"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6112",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6113",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7029", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6112"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6113"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6118",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7030", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6118"]))

di.objtypes.LockingServicesType(
    nodeId="ns=fx_ac;i=5037",
    browseName="ns=di;Lock",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6114", browseName="ns=di;Locked", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6115", browseName="ns=di;LockingClient", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6116", browseName="ns=di;LockingUser", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6117", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7027"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7028"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7029"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7030"]),
    ],
)
fx_ac_objtypes.ControlItemFolderType(nodeId="ns=fx_ac;i=5036", browseName="ns=fx_ac;ListToRestrict", references=[o6.hasComponent(o6.ns["ns=fx_ac;i=5037"])])
fx_ac_objtypes.ControlGroupType(
    nodeId="ns=fx_ac;i=5018",
    browseName="ns=fx_ac;<ControlGroup>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6089", browseName="ns=fx_ac;IsControlled", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=fx_ac;i=5030", browseName="ns=fx_ac;ListOfRelated")),
        o6.hasComponent(o6.ns["ns=fx_ac;i=5033"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=5036"]),
    ],
)
o6.reference(fx_ac_objtypes.ControlGroupType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5018"])


ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6162",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7031",
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
    nodeId="ns=fx_ac;i=6163",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7031",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Results", dataType=ns0.datatypes.LogRecordsDataType, valueRank=-1),
        ns0.datatypes.Argument(name="ContinuationPointOut", dataType=o6.ByteString, valueRank=-1),
    ],
)
o6.call(nodeId="ns=fx_ac;i=7031", browseName="GetRecords", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6162"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6163"]))

ns0.objtypes.LogObjectType(
    nodeId="ns=fx_ac;i=5058",
    browseName="ns=fx_ac;AutomationComponentLog",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6164", browseName="MaxRecords", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6165", browseName="MaxStorageDuration", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6166", browseName="MinimumSeverity", dataType=o6.UInt16)),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7031"]),
    ],
)
o6.reference(fx_ac_objtypes.AutomationComponentType, ns0.reftypes.HasComponent, o6.ns["ns=fx_ac;i=5058"])


ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6457",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7053",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7053", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6457"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6458",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7054",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7054", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6458"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6459",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7055",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6460",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7055",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7055", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6459"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6460"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6465",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7056",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7056", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6465"]))

di.objtypes.LockingServicesType(
    nodeId="ns=fx_ac;i=5099",
    browseName="ns=di;Lock",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6461", browseName="ns=di;Locked", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6462", browseName="ns=di;LockingClient", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6463", browseName="ns=di;LockingUser", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6464", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7053"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7054"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7055"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7056"]),
    ],
)
fx_ac_objtypes.ControlItemFolderType(nodeId="ns=fx_ac;i=1081", browseName="ns=fx_ac;ListToBlock", references=[o6.hasComponent(o6.ns["ns=fx_ac;i=5099"])])


ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6466",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7057",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7057", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6466"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6467",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7058",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7058", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6467"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6468",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7059",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6469",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7059",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7059", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6468"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6469"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6474",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7060",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7060", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6474"]))

di.objtypes.LockingServicesType(
    nodeId="ns=fx_ac;i=5103",
    browseName="ns=di;Lock",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6470", browseName="ns=di;Locked", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6471", browseName="ns=di;LockingClient", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6472", browseName="ns=di;LockingUser", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6473", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7057"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7058"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7059"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=7060"]),
    ],
)
fx_ac_objtypes.ControlItemFolderType(nodeId="ns=fx_ac;i=1082", browseName="ns=fx_ac;ListToRestrict", references=[o6.hasComponent(o6.ns["ns=fx_ac;i=5103"])])
fx_ac_objtypes.ControlGroupType(
    nodeId="ns=fx_ac;i=1074",
    browseName="ns=fx_ac;<ControlGroup>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6365", browseName="ns=fx_ac;IsControlled", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=fx_ac;i=1081"]),
        o6.hasComponent(o6.ns["ns=fx_ac;i=1082"]),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=fx_ac;i=5077", browseName="ns=fx_ac;ListOfRelated")),
    ],
)
o6.reference(fx_ac_objtypes.ControlGroupsFolderType, fx_ac_reftypes.HasControlGroup, o6.ns["ns=fx_ac;i=1074"])


del Any, TYPE_CHECKING, uuid, o6, di, fx_data, ns0, fx_ac_reftypes, fx_ac_datypes, fx_ac_vartypes, fx_ac_objtypes
