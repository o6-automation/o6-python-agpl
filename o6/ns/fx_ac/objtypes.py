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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=fx_ac;i=5",
    browseName="ns=fx_ac;AssetConnectorType",
    displayName="AssetConnectorType",
    description="AssetConnectorType provides information about physical connections that are part of an asset",
    isAbstract=True,
)
class AssetConnectorType(ns0.objtypes.BaseObjectType):
    id: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=114", browseName="ns=fx_ac;Id", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=116", browseName="ns=fx_ac;Name", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=fx_ac;i=6", browseName="ns=fx_ac;SlotType", displayName="SlotType", description="SlotType represents a physical slot where a module can attach")
class SlotType(AssetConnectorType):
    id: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=115", browseName="ns=fx_ac;Id", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    logicalId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=159", browseName="ns=fx_ac;LogicalId", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(
    nodeId="ns=fx_ac;i=8", browseName="ns=fx_ac;SocketType", displayName="SocketType", description="SocketType represents a physical socket where a cable can be connected"
)
class SocketType(AssetConnectorType):
    kind: ns0.vartypes.MultiStateValueDiscreteType | None
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=211", browseName="ns=fx_ac;Name", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=fx_ac;i=10", browseName="ns=fx_ac;ClampType", displayName="ClampType", description="ClampType represents a wire connection")
class ClampType(AssetConnectorType):
    kind: ns0.vartypes.MultiStateValueDiscreteType | None
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=214", browseName="ns=fx_ac;Name", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=fx_ac;i=7", browseName="ns=fx_ac;ClampBlockType", displayName="ClampBlockType", description="ClampBlockType represents a wire connection block")
class ClampBlockType(AssetConnectorType):
    blockSize: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=218", browseName="ns=fx_ac;BlockSize", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    kind: ns0.vartypes.MultiStateValueDiscreteType | None
    langleClampRangle: ClampType | None
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=217", browseName="ns=fx_ac;Name", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=1420",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=289",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExpectedVerificationVariables", dataType=o6.NodeId("ns=fx_data;i=1028"), valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=1421",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=289",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="VerificationResult", dataType=o6.NodeId("ns=fx_data;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="VerificationVariablesErrors", dataType=o6.StatusCode, valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(nodeId="ns=fx_ac;i=289", browseName="ns=fx_ac;Verify", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=1420"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=1421"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6093",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=290",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="LockContext", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6094",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=290",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="LockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=290", browseName="ns=fx_ac;EstablishControl", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6093"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6094"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=1303",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=292",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="CommandMask", dataType=o6.NodeId("ns=fx_data;i=1024"), valueRank=-1),
        ns0.datatypes.Argument(name="AssetVerifications", dataType=o6.NodeId("ns=fx_data;i=1048"), valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="ConnectionEndpointConfigurations", dataType=o6.NodeId("ns=fx_data;i=1044"), valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="ReserveCommunicationIds", dataType=o6.NodeId("ns=fx_data;i=3017"), valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="CommunicationConfigurations", dataType=o6.NodeId("ns=fx_data;i=1046"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=1304",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=292",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="AssetVerificationResults", dataType=o6.NodeId("ns=fx_data;i=1038"), valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="ConnectionEndpointConfigurationResults", dataType=o6.NodeId("ns=fx_data;i=3008"), valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="ReserveCommunicationIdsResults", dataType=o6.NodeId("ns=fx_data;i=3019"), valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="CommunicationConfigurationResults", dataType=o6.NodeId("ns=fx_data;i=1033"), valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(
    nodeId="ns=fx_ac;i=292", browseName="ns=fx_ac;EstablishConnections", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=1303"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=1304"])
)
o6.reference(o6.ns["ns=fx_ac;i=292"], "i=41", "ns=fx_data;i=1025")

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=1305",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=293",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ConnectionEndpoints", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="Remove", dataType=o6.Boolean, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=1306",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=293",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Results", dataType=o6.StatusCode, valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=fx_ac;i=293", browseName="ns=fx_ac;CloseConnections", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=1305"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=1306"]))
o6.reference(o6.ns["ns=fx_ac;i=293"], "i=41", "ns=fx_data;i=1025")


@o6.objecttype(nodeId="ns=fx_ac;i=2", browseName="ns=fx_ac;AutomationComponentType", displayName="AutomationComponentType")
class AutomationComponentType(ns0.objtypes.BaseObjectType):
    aggregatedHealth: fx_ac_vartypes.AggregatedHealthType
    assets: ns0.objtypes.FolderType
    automationComponentLog: ns0.objtypes.LogObjectType | None
    closeConnections: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=fx_ac;i=293"])
    componentCapabilities: AutomationComponentCapabilitiesType
    conformanceName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=210", browseName="ns=fx_ac;ConformanceName", dataType=ns0.datatypes.UriString)
    )
    descriptors: ns0.objtypes.FolderType
    diagnostics: di.objtypes.FunctionalGroupType | None
    establishConnections: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=fx_ac;i=292"])
    functionalEntities: ns0.objtypes.FolderType
    publisherCapabilities: PublisherCapabilitiesType | None
    subscriberCapabilities: SubscriberCapabilitiesType | None


ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=1358",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=301",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExpectedVerificationVariables", dataType=o6.NodeId("ns=fx_data;i=1028"), valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=1359",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=301",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="VerificationResult", dataType=o6.NodeId("ns=fx_data;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="VerificationVariablesErrors", dataType=o6.StatusCode, valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(nodeId="ns=fx_ac;i=301", browseName="ns=fx_ac;Verify", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=1358"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=1359"]))


@o6.objecttype(nodeId="ns=fx_ac;i=1009", browseName="ns=fx_ac;IAssetExtensionsType", displayName="IAssetExtensionsType", isAbstract=True)
class IAssetExtensionsType(ns0.objtypes.BaseInterfaceType):
    connectors: ns0.objtypes.FolderType | None
    diagnostics: di.objtypes.FunctionalGroupType | None


@o6.objecttype(nodeId="ns=fx_ac;i=1010", browseName="ns=fx_ac;ControlGroupsFolderType", displayName="ControlGroupsFolderType")
class ControlGroupsFolderType(ns0.objtypes.FolderType):
    langleControlGroupRangle: ControlGroupType | None


@o6.objecttype(nodeId="ns=fx_ac;i=1030", browseName="ns=fx_ac;AuditUaFxEventType", displayName="AuditUaFxEventType", isAbstract=True)
class AuditUaFxEventType(ns0.objtypes.AuditEventType):
    pass


ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=1422",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=1476",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="VerificationMode", dataType=o6.NodeId("ns=fx_data;i=1029"), valueRank=-1),
        ns0.datatypes.Argument(name="ExpectedVerificationVariables", dataType=ns0.datatypes.KeyValuePair, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="ExpectedAdditionalVerificationVariables", dataType=o6.NodeId("ns=fx_data;i=1028"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=1423",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=1476",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="VerificationResult", dataType=o6.NodeId("ns=fx_data;i=1037"), valueRank=-1),
        ns0.datatypes.Argument(name="VerificationVariablesErrors", dataType=o6.StatusCode, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="VerificationAdditionalVariablesErrors", dataType=o6.StatusCode, valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(nodeId="ns=fx_ac;i=1476", browseName="ns=fx_ac;VerifyAsset", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=1422"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=1423"]))


@o6.objecttype(nodeId="ns=fx_ac;i=9", browseName="ns=fx_ac;IAssetRevisionType", displayName="IAssetRevisionType", isAbstract=True)
class IAssetRevisionType(ns0.objtypes.BaseInterfaceType):
    buildAssetNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=119", browseName="ns=fx_ac;BuildAssetNumber", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    majorAssetVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=117", browseName="ns=fx_ac;MajorAssetVersion", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    minorAssetVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=118", browseName="ns=fx_ac;MinorAssetVersion", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    subBuildAssetNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=120", browseName="ns=fx_ac;SubBuildAssetNumber", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    verifyAsset: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=fx_ac;i=1476"])


ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=1356",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=1502",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="VerificationMode", dataType=o6.NodeId("ns=fx_data;i=1029"), valueRank=-1),
        ns0.datatypes.Argument(name="ExpectedVerificationVariables", dataType=ns0.datatypes.KeyValuePair, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="ExpectedAdditionalVerificationVariables", dataType=o6.NodeId("ns=fx_data;i=1028"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=1357",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=1502",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="VerificationResult", dataType=o6.NodeId("ns=fx_data;i=1037"), valueRank=-1),
        ns0.datatypes.Argument(name="VerificationVariablesErrors", dataType=o6.StatusCode, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="VerificationAdditionalVariablesErrors", dataType=o6.StatusCode, valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(nodeId="ns=fx_ac;i=1502", browseName="ns=fx_ac;VerifyAsset", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=1356"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=1357"]))


@o6.objecttype(nodeId="ns=fx_ac;i=1000", browseName="ns=fx_ac;InputsFolderType", displayName="InputsFolderType")
class InputsFolderType(ns0.objtypes.FolderType):
    langleInputGroupRangle: InputsFolderType | None
    langleInputVariable1Rangle: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6078", browseName="ns=fx_ac;<InputVariable1>", modellingRule="OptionalPlaceholder", accessLevel=3, userAccessLevel=1)
    )
    langleInputVariableRangle: ns0.vartypes.BaseDataVariableType | None = o6.organizes(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=1319", browseName="ns=fx_ac;<InputVariable>", modellingRule="OptionalPlaceholder", accessLevel=3, userAccessLevel=1)
    )
    subscriberCapabilities: SubscriberCapabilitiesType | None


@o6.objecttype(nodeId="ns=fx_ac;i=1019", browseName="ns=fx_ac;OutputsFolderType", displayName="OutputsFolderType")
class OutputsFolderType(ns0.objtypes.FolderType):
    langleOutputGroupRangle: OutputsFolderType | None
    langleOutputVariable1Rangle: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6079", browseName="ns=fx_ac;<OutputVariable1>", modellingRule="OptionalPlaceholder", accessLevel=3, userAccessLevel=1)
    )
    langleOutputVariableRangle: ns0.vartypes.BaseDataVariableType | None = o6.organizes(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=1425", browseName="ns=fx_ac;<OutputVariable>", modellingRule="OptionalPlaceholder", accessLevel=3, userAccessLevel=1)
    )
    publisherCapabilities: PublisherCapabilitiesType | None


@o6.objecttype(
    nodeId="ns=fx_ac;i=3",
    browseName="ns=fx_ac;FxAssetType",
    displayName="FxAssetType",
    interfaces=[di.objtypes.IVendorNameplateType, di.objtypes.ITagNameplateType, di.objtypes.IDeviceHealthType, IAssetRevisionType, IAssetExtensionsType],
)
class FxAssetType(ns0.objtypes.BaseObjectType):
    assetId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=195", browseName="ns=di;AssetId", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    buildAssetNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=198", browseName="ns=fx_ac;BuildAssetNumber", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    componentName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=184", browseName="ns=di;ComponentName", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
    )
    connectors: ns0.objtypes.FolderType | None
    deviceClass: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=191", browseName="ns=di;DeviceClass", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    deviceHealth: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_ac;i=6081", browseName="ns=di;DeviceHealth", dataType=di.datatypes.DeviceHealthEnumeration, accessLevel=3, userAccessLevel=1
        )
    )
    deviceHealthAlarms: ns0.objtypes.FolderType | None = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=fx_ac;i=5023", browseName="ns=di;DeviceHealthAlarms"))
    deviceManual: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=190", browseName="ns=di;DeviceManual", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    deviceRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=189", browseName="ns=di;DeviceRevision", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    diagnostics: di.objtypes.FunctionalGroupType | None
    hardwareRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=187", browseName="ns=di;HardwareRevision", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    majorAssetVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=196", browseName="ns=fx_ac;MajorAssetVersion", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    manufacturer: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=175", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
    )
    manufacturerUri: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=185", browseName="ns=di;ManufacturerUri", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
    )
    minorAssetVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=197", browseName="ns=fx_ac;MinorAssetVersion", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    model: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=176", browseName="ns=di;Model", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
    )
    productCode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=186", browseName="ns=di;ProductCode", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    productInstanceUri: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=193", browseName="ns=di;ProductInstanceUri", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    revisionCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=194", browseName="ns=di;RevisionCounter", dataType=o6.Int32, accessLevel=3, userAccessLevel=1)
    )
    serialNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=192", browseName="ns=di;SerialNumber", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    softwareRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=188", browseName="ns=di;SoftwareRevision", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    softwareUpdate: di.objtypes.SoftwareUpdateType | None = o6.hasAddIn(di.objtypes.SoftwareUpdateType(nodeId="ns=fx_ac;i=5002", browseName="ns=di;SoftwareUpdate"))
    subBuildAssetNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=199", browseName="ns=fx_ac;SubBuildAssetNumber", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    verifyAsset: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=fx_ac;i=1502"])


@o6.objecttype(nodeId="ns=fx_ac;i=20", browseName="ns=fx_ac;ConnectionEndpointsFolderType", displayName="ConnectionEndpointsFolderType")
class ConnectionEndpointsFolderType(ns0.objtypes.FolderType):
    commHealth: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6096", browseName="ns=fx_ac;CommHealth", dataType=fx_ac_datypes.CommHealthOptionSet)
    )
    langleConnectionEndpointRangle: ConnectionEndpointType | None


@o6.objecttype(nodeId="ns=fx_ac;i=11", browseName="ns=fx_ac;IFunctionalEntityType", displayName="IFunctionalEntityType", isAbstract=True)
class IFunctionalEntityType(ns0.objtypes.BaseInterfaceType):
    applicationIdentifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fx_ac;i=129",
            browseName="ns=fx_ac;ApplicationIdentifier",
            dataType=fx_ac_datypes.ApplicationIdentifierDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    authorAssignedIdentifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=127", browseName="ns=fx_ac;AuthorAssignedIdentifier", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    authorAssignedVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fx_ac;i=128",
            browseName="ns=fx_ac;AuthorAssignedVersion",
            dataType=fx_ac_datypes.FxVersion,
            value=fx_ac_datypes.FxVersion(major=0, minor=0, build=0, subBuild=0),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    authorUri: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=126", browseName="ns=fx_ac;AuthorUri", dataType=ns0.datatypes.UriString, accessLevel=3, userAccessLevel=1)
    )
    capabilities: FunctionalEntityCapabilitiesType | None
    configurationData: ConfigurationDataFolderType | None
    connectionEndpoints: ConnectionEndpointsFolderType | None = o6.hasComponent(ConnectionEndpointsFolderType(nodeId="ns=fx_ac;i=52", browseName="ns=fx_ac;ConnectionEndpoints"))
    controlGroups: ControlGroupsFolderType | None = o6.hasComponent(ControlGroupsFolderType(nodeId="ns=fx_ac;i=1064", browseName="ns=fx_ac;ControlGroups"))
    diagnostics: di.objtypes.FunctionalGroupType | None
    inputData: InputsFolderType | None = o6.hasComponent(InputsFolderType(nodeId="ns=fx_ac;i=1203", browseName="ns=fx_ac;InputData"))
    operational: di.objtypes.FunctionalGroupType | None = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=fx_ac;i=5047", browseName="ns=di;Operational"))
    operationalHealth: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6101", browseName="ns=fx_ac;OperationalHealth", dataType=fx_ac_datypes.OperationalHealthOptionSet)
    )
    operationalHealthAlarms: ns0.objtypes.FolderType | None = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=fx_ac;i=5035", browseName="ns=fx_ac;OperationalHealthAlarms"))
    outputData: OutputsFolderType | None = o6.hasComponent(OutputsFolderType(nodeId="ns=fx_ac;i=1204", browseName="ns=fx_ac;OutputData"))
    publisherCapabilities: PublisherCapabilitiesType | None
    status: di.objtypes.FunctionalGroupType | None = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=fx_ac;i=5046", browseName="ns=di;Status"))
    subscriberCapabilities: SubscriberCapabilitiesType | None
    verify: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=fx_ac;i=289"])


@o6.objecttype(nodeId="ns=fx_ac;i=4", browseName="ns=fx_ac;FunctionalEntityType", displayName="FunctionalEntityType", interfaces=[IFunctionalEntityType])
class FunctionalEntityType(ns0.objtypes.BaseObjectType):
    applicationIdentifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fx_ac;i=205",
            browseName="ns=fx_ac;ApplicationIdentifier",
            dataType=fx_ac_datypes.ApplicationIdentifierDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    authorAssignedIdentifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=203", browseName="ns=fx_ac;AuthorAssignedIdentifier", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    authorAssignedVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fx_ac;i=204",
            browseName="ns=fx_ac;AuthorAssignedVersion",
            dataType=fx_ac_datypes.FxVersion,
            value=fx_ac_datypes.FxVersion(major=0, minor=0, build=0, subBuild=0),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    authorUri: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=202", browseName="ns=fx_ac;AuthorUri", dataType=ns0.datatypes.UriString, accessLevel=3, userAccessLevel=1)
    )
    capabilities: FunctionalEntityCapabilitiesType | None
    configurationData: ConfigurationDataFolderType | None
    connectionEndpoints: ConnectionEndpointsFolderType | None = o6.hasComponent(ConnectionEndpointsFolderType(nodeId="ns=fx_ac;i=5032", browseName="ns=fx_ac;ConnectionEndpoints"))
    controlGroups: ControlGroupsFolderType | None = o6.hasComponent(ControlGroupsFolderType(nodeId="ns=fx_ac;i=1065", browseName="ns=fx_ac;ControlGroups"))
    diagnostics: di.objtypes.FunctionalGroupType | None
    inputData: InputsFolderType | None = o6.hasComponent(InputsFolderType(nodeId="ns=fx_ac;i=1125", browseName="ns=fx_ac;InputData"))
    langleSubFunctionalEntityRangle: FunctionalEntityType | None
    operational: di.objtypes.FunctionalGroupType | None = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=fx_ac;i=5054", browseName="ns=di;Operational"))
    operationalHealth: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6056", browseName="ns=fx_ac;OperationalHealth", dataType=fx_ac_datypes.OperationalHealthOptionSet)
    )
    operationalHealthAlarms: ns0.objtypes.FolderType | None = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=fx_ac;i=5041", browseName="ns=fx_ac;OperationalHealthAlarms"))
    outputData: OutputsFolderType | None = o6.hasComponent(OutputsFolderType(nodeId="ns=fx_ac;i=1126", browseName="ns=fx_ac;OutputData"))
    publisherCapabilities: PublisherCapabilitiesType | None
    status: di.objtypes.FunctionalGroupType | None = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=fx_ac;i=5052", browseName="ns=di;Status"))
    subscriberCapabilities: SubscriberCapabilitiesType | None
    verify: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=fx_ac;i=301"])


@o6.objecttype(nodeId="ns=fx_ac;i=1008", browseName="ns=fx_ac;FunctionalEntityCapabilitiesType", displayName="FunctionalEntityCapabilitiesType")
class FunctionalEntityCapabilitiesType(ns0.objtypes.FolderType):
    feedbackSignalRequired: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6119", browseName="ns=fx_ac;FeedbackSignalRequired", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1),
        "ns=fx_ac;i=4002",
    )
    langleCapabilityRangle: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6120", browseName="ns=fx_ac;<Capability>", modellingRule="OptionalPlaceholder", accessLevel=3, userAccessLevel=1),
        "ns=fx_ac;i=4002",
    )


@o6.objecttype(nodeId="ns=fx_ac;i=1003", browseName="ns=fx_ac;PublisherCapabilitiesType", displayName="PublisherCapabilitiesType")
class PublisherCapabilitiesType(ns0.objtypes.BaseObjectType):
    preconfiguredDataSetOnly: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6023", browseName="ns=fx_ac;PreconfiguredDataSetOnly", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    preconfiguredPublishedDataSets: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_ac;i=6022", browseName="ns=fx_ac;PreconfiguredPublishedDataSets", dataType=o6.String, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
        )
    )
    supportedPublishingIntervals: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_ac;i=6020",
            browseName="ns=fx_ac;SupportedPublishingIntervals",
            dataType=fx_data.datatypes.IntervalRange,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    supportedQos: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_ac;i=6021",
            browseName="ns=fx_ac;SupportedQos",
            dataType=fx_ac_datypes.PublisherQosDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    supportedTransportProtocolMappings: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_ac;i=6168",
            browseName="ns=fx_ac;SupportedTransportProtocolMappings",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=fx_ac;i=1004", browseName="ns=fx_ac;SubscriberCapabilitiesType", displayName="SubscriberCapabilitiesType")
class SubscriberCapabilitiesType(ns0.objtypes.BaseObjectType):
    preconfiguredDataSetOnly: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6028", browseName="ns=fx_ac;PreconfiguredDataSetOnly", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    preconfiguredSubscribedDataSets: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_ac;i=6027", browseName="ns=fx_ac;PreconfiguredSubscribedDataSets", dataType=o6.String, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
        )
    )
    supportedMessageReceiveTimeouts: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_ac;i=6026",
            browseName="ns=fx_ac;SupportedMessageReceiveTimeouts",
            dataType=fx_data.datatypes.IntervalRange,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    supportedPublishingIntervals: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_ac;i=6024",
            browseName="ns=fx_ac;SupportedPublishingIntervals",
            dataType=fx_data.datatypes.IntervalRange,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    supportedQos: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_ac;i=6025",
            browseName="ns=fx_ac;SupportedQos",
            dataType=fx_ac_datypes.SubscriberQosDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    supportedTransportProtocolMappings: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_ac;i=6169",
            browseName="ns=fx_ac;SupportedTransportProtocolMappings",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=fx_ac;i=1002", browseName="ns=fx_ac;ConnectionEndpointType", displayName="ConnectionEndpointType", isAbstract=True)
class ConnectionEndpointType(ns0.objtypes.BaseObjectType):
    cleanupTimeout: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=1316", browseName="ns=fx_ac;CleanupTimeout", dataType=ns0.datatypes.Duration, accessLevel=3, userAccessLevel=1)
    )
    connectionManagerApplicationUri: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6152", browseName="ns=fx_ac;ConnectionManagerApplicationUri", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    diagnostics: di.objtypes.FunctionalGroupType | None
    inputVariables: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_ac;i=6197", browseName="ns=fx_ac;InputVariables", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
        )
    )
    isPersistent: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=1308", browseName="ns=fx_ac;IsPersistent", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    outputVariables: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_ac;i=6198", browseName="ns=fx_ac;OutputVariables", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
        )
    )
    relatedEndpoint: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_ac;i=6069", browseName="ns=fx_ac;RelatedEndpoint", dataType=fx_data.datatypes.RelatedEndpointDataType, accessLevel=3, userAccessLevel=1
        )
    )
    status: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=1300", browseName="ns=fx_ac;Status", dataType=fx_ac_datypes.ConnectionEndpointStatusEnum)
    )


@o6.objecttype(nodeId="ns=fx_ac;i=1005", browseName="ns=fx_ac;PubSubConnectionEndpointType", displayName="PubSubConnectionEndpointType")
class PubSubConnectionEndpointType(ConnectionEndpointType):
    dataSetReaderPath: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_ac;i=6170", browseName="ns=fx_ac;DataSetReaderPath", dataType=o6.String, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
        )
    )
    dataSetWriterPath: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_ac;i=6171", browseName="ns=fx_ac;DataSetWriterPath", dataType=o6.String, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
        )
    )
    mode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_ac;i=1352", browseName="ns=fx_ac;Mode", dataType=fx_data.datatypes.PubSubConnectionEndpointModeEnum, accessLevel=3, userAccessLevel=1
        )
    )


o6.reference(PubSubConnectionEndpointType, "ns=fx_ac;i=42", "i=18076")
o6.reference(PubSubConnectionEndpointType, "ns=fx_ac;i=46", "i=17743")


@o6.objecttype(nodeId="ns=fx_ac;i=1027", browseName="ns=fx_ac;AcDescriptorType", displayName="AcDescriptorType")
class AcDescriptorType(ns0.objtypes.BaseObjectType):
    descriptorFile: ns0.objtypes.FileType | None
    descriptorIdentifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6335", browseName="ns=fx_ac;DescriptorIdentifier", dataType=ns0.datatypes.UriString, accessLevel=3, userAccessLevel=1)
    )
    descriptorVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fx_ac;i=6336",
            browseName="ns=fx_ac;DescriptorVersion",
            dataType=fx_ac_datypes.FxVersion,
            value=fx_ac_datypes.FxVersion(major=0, minor=0, build=0, subBuild=0),
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=fx_ac;i=1040", browseName="ns=fx_ac;AuditConnectionCleanupEventType", displayName="AuditConnectionCleanupEventType", isAbstract=True)
class AuditConnectionCleanupEventType(AuditUaFxEventType):
    relatedEndpoint: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fx_ac;i=6351",
            browseName="ns=fx_ac;RelatedEndpoint",
            dataType=fx_data.datatypes.RelatedEndpointDataType,
            value=fx_data.datatypes.RelatedEndpointDataType(address="", connectionEndpointPath=[], connectionEndpointName=""),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    removedEndpoint: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6350", browseName="ns=fx_ac;RemovedEndpoint", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


o6.reference(ConnectionEndpointType, "i=41", AuditConnectionCleanupEventType)


@o6.objecttype(nodeId="ns=fx_ac;i=1001", browseName="ns=fx_ac;AutomationComponentCapabilitiesType", displayName="AutomationComponentCapabilitiesType")
class AutomationComponentCapabilitiesType(ns0.objtypes.FolderType):
    commandBundleRequired: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6077", browseName="ns=fx_ac;CommandBundleRequired", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1),
        "ns=fx_ac;i=4002",
    )
    langleCapabilityRangle: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=1249", browseName="ns=fx_ac;<Capability>", modellingRule="OptionalPlaceholder", accessLevel=3, userAccessLevel=1),
        "ns=fx_ac;i=4002",
    )
    maxConnections: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6358", browseName="ns=fx_ac;MaxConnections", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1), "ns=fx_ac;i=4002"
    )
    maxConnectionsPerCall: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6076", browseName="ns=fx_ac;MaxConnectionsPerCall", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1),
        "ns=fx_ac;i=4002",
    )
    maxFunctionalEntities: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6357", browseName="ns=fx_ac;MaxFunctionalEntities", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1),
        "ns=fx_ac;i=4002",
    )
    minConnections: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6126", browseName="ns=fx_ac;MinConnections", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1), "ns=fx_ac;i=4002"
    )
    supportsPersistence: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6356", browseName="ns=fx_ac;SupportsPersistence", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1),
        "ns=fx_ac;i=4002",
    )


@o6.objecttype(nodeId="ns=fx_ac;i=1011", browseName="ns=fx_ac;ControlItemFolderType", displayName="ControlItemFolderType")
class ControlItemFolderType(di.objtypes.FunctionalGroupType):
    lock: di.objtypes.LockingServicesType
    maxInactiveLockTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6485", browseName="ns=di;MaxInactiveLockTime", dataType=ns0.datatypes.Duration, accessLevel=3, userAccessLevel=1)
    )


ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6366",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="LockContext", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6367",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="LockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fx_ac;i=7011", browseName="ns=fx_ac;ReassignControl", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6366"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6367"]))


@o6.objecttype(nodeId="ns=fx_ac;i=15", browseName="ns=fx_ac;ControlGroupType", displayName="ControlGroupType")
class ControlGroupType(ns0.objtypes.BaseObjectType):
    establishControl: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=fx_ac;i=290"])
    isControlled: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_ac;i=6095", browseName="ns=fx_ac;IsControlled", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    langleControlGroupRangle: ControlGroupType | None
    listOfRelated: ns0.objtypes.FolderType = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=fx_ac;i=5075", browseName="ns=fx_ac;ListOfRelated"))
    listToBlock: ControlItemFolderType
    listToRestrict: ControlItemFolderType
    reassignControl: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=fx_ac;i=7011"])
    releaseControl: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=fx_ac;i=1493", browseName="ns=fx_ac;ReleaseControl"))


ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6396",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="VariablesToStore", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6397",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Results", dataType=o6.StatusCode, valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=fx_ac;i=7024", browseName="ns=fx_ac;SetStoredVariables", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6396"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6397"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6398",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="VariablesToClear", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6399",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Results", dataType=o6.StatusCode, valueRank=1, arrayDimensions=[0])],
)
o6.call(
    nodeId="ns=fx_ac;i=7025", browseName="ns=fx_ac;ClearStoredVariables", inputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6398"]), outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6399"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=fx_ac;i=6401",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_ac;i=7026",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="StoredVariables", dataType=o6.NodeId("ns=fx_data;i=1028"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=fx_ac;i=7026", browseName="ns=fx_ac;ListStoredVariables", outputArgs=o6.hasProperty(o6.ns["ns=fx_ac;i=6401"]))


@o6.objecttype(nodeId="ns=fx_ac;i=1041", browseName="ns=fx_ac;ConfigurationDataFolderType", displayName="ConfigurationDataFolderType")
class ConfigurationDataFolderType(di.objtypes.FunctionalGroupType):
    clearStoredVariables: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=fx_ac;i=7025"])
    langleConfigurationVariable1Rangle: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_ac;i=6080", browseName="ns=fx_ac;<ConfigurationVariable1>", modellingRule="OptionalPlaceholder", accessLevel=3, userAccessLevel=1
        )
    )
    langleConfigurationVariableRangle: ns0.vartypes.BaseDataVariableType | None = o6.organizes(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_ac;i=6049", browseName="ns=fx_ac;<ConfigurationVariable>", modellingRule="OptionalPlaceholder", accessLevel=3, userAccessLevel=1
        )
    )
    listStoredVariables: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=fx_ac;i=7026"])
    setStoredVariables: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=fx_ac;i=7024"])


del Any, TYPE_CHECKING, uuid, o6, di, fx_data, ns0, fx_ac_reftypes, fx_ac_datypes, fx_ac_vartypes
