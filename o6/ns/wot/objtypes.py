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

"""Generated OPC UA wot namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as wot_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=27",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=26",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AssetName", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=28",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=26",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AssetId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=wot;i=26", browseName="ns=wot;CreateAsset", inputArgs=o6.hasProperty(o6.ns["ns=wot;i=27"]), outputArgs=o6.hasProperty(o6.ns["ns=wot;i=28"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=30",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=29",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AssetId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=wot;i=29", browseName="ns=wot;DeleteAsset", inputArgs=o6.hasProperty(o6.ns["ns=wot;i=30"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=48",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=41",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AssetEndpoints", dataType=o6.String, valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=wot;i=41", browseName="ns=wot;DiscoverAssets", outputArgs=o6.hasProperty(o6.ns["ns=wot;i=48"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=50",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=49",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="AssetName", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="AssetEndpoint", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=170",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=49",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AssetId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=wot;i=49", browseName="ns=wot;CreateAssetForEndpoint", inputArgs=o6.hasProperty(o6.ns["ns=wot;i=50"]), outputArgs=o6.hasProperty(o6.ns["ns=wot;i=170"]))

ns0.vartypes.BaseDataVariableType(nodeId="ns=wot;i=66", browseName="ns=wot;<WoTPropertyName>", modellingRule="OptionalPlaceholder")


ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=76",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=75",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AssetEndpoint", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=77",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=75",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Success", dataType=o6.Boolean, valueRank=-1), ns0.datatypes.Argument(name="Status", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=wot;i=75", browseName="ns=wot;ConnectionTest", inputArgs=o6.hasProperty(o6.ns["ns=wot;i=76"]), outputArgs=o6.hasProperty(o6.ns["ns=wot;i=77"]))


@o6.objecttype(nodeId="ns=wot;i=105", browseName="ns=wot;WoTAssetConfigurationType", displayName="WoTAssetConfigurationType")
class WoTAssetConfigurationType(ns0.objtypes.BaseInterfaceType):
    langleWoTConfigurationParameterNameRangle: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=wot;i=108", browseName="ns=wot;<WoTConfigurationParameterName>", modellingRule="OptionalPlaceholder")
    )
    license: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wot;i=109", browseName="ns=wot;License", dataType=o6.String))


@o6.objecttype(nodeId="ns=wot;i=1", browseName="ns=wot;WoTAssetConnectionManagementType", displayName="WoTAssetConnectionManagementType")
class WoTAssetConnectionManagementType(ns0.objtypes.BaseObjectType):
    configuration: WoTAssetConfigurationType | None = o6.hasComponent(WoTAssetConfigurationType(nodeId="ns=wot;i=78", browseName="ns=wot;Configuration"))
    connectionTest: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=wot;i=75"])
    createAsset: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=wot;i=26"])
    createAssetForEndpoint: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=wot;i=49"])
    deleteAsset: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=wot;i=29"])
    discoverAssets: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=wot;i=41"])
    langleWoTAssetNameRangle: ns0.objtypes.BaseObjectType | None
    supportedWoTBindings: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=wot;i=40", browseName="ns=wot;SupportedWoTBindings", dataType=ns0.datatypes.UriString, valueRank=1, arrayDimensions=[0])
    )


ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=112",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=111",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=wot;i=111", browseName="ns=wot;CloseAndUpdate", inputArgs=o6.hasProperty(o6.ns["ns=wot;i=112"]))


@o6.objecttype(nodeId="ns=wot;i=110", browseName="ns=wot;WoTAssetFileType", displayName="WoTAssetFileType")
class WoTAssetFileType(ns0.objtypes.FileType):
    closeAndUpdate: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=wot;i=111"])


@o6.objecttype(nodeId="ns=wot;i=42", browseName="ns=wot;IWoTAssetType", displayName="IWoTAssetType", isAbstract=True)
class IWoTAssetType(ns0.objtypes.BaseInterfaceType):
    assetEndpoint: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wot;i=122", browseName="ns=wot;AssetEndpoint", dataType=o6.String))
    langleWoTPropertyNameRangle: ns0.vartypes.BaseDataVariableType | None = o6.reference(o6.ns["ns=wot;i=66"], "ns=wot;i=142")
    woTFile: WoTAssetFileType


del Any, TYPE_CHECKING, uuid, o6, ns0, wot_reftypes
