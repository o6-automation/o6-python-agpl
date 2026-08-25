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
from . import objtypes as wot_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=33",
    browseName="InputArguments",
    parent="ns=wot;i=32",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AssetName", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=34",
    browseName="OutputArguments",
    parent="ns=wot;i=32",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AssetId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=wot;i=32", browseName="ns=wot;CreateAsset", inputArgs=o6.hasProperty(o6.ns["ns=wot;i=33"]), outputArgs=o6.hasProperty(o6.ns["ns=wot;i=34"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=36",
    browseName="InputArguments",
    parent="ns=wot;i=35",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AssetId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=wot;i=35", browseName="ns=wot;DeleteAsset", inputArgs=o6.hasProperty(o6.ns["ns=wot;i=36"]))

woTAssetConnectionManagement = wot_objtypes.WoTAssetConnectionManagementType(
    nodeId="ns=wot;i=31",
    browseName="ns=wot;WoTAssetConnectionManagement",
    references=[o6.hasComponent(o6.ns["ns=wot;i=32"]), o6.hasComponent(o6.ns["ns=wot;i=35"])],
    parent="i=85",
    referenceType=ns0.reftypes.Organizes,
)


ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=52",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=51",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=53",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=51",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=wot;i=51", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=wot;i=52"]), outputArgs=o6.hasProperty(o6.ns["ns=wot;i=53"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=55",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=54",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=wot;i=54", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=wot;i=55"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=57",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=56",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=58",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=56",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=wot;i=56", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=wot;i=57"]), outputArgs=o6.hasProperty(o6.ns["ns=wot;i=58"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=60",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=59",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=wot;i=59", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=wot;i=60"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=62",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=61",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=63",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=61",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=wot;i=61", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=wot;i=62"]), outputArgs=o6.hasProperty(o6.ns["ns=wot;i=63"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=65",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=64",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=wot;i=64", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=wot;i=65"]))

httpColonSlashSlashOpcfoundationDotOrgSlashUASlashWoTMinusConSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=wot;i=67",
    browseName="ns=wot;http://opcfoundation.org/UA/WoT-Con/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wot;i=39", browseName="ModelVersion", dataType=ns0.datatypes.SemanticVersionString, value="1.2.0")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wot;i=68", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/WoT-Con/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wot;i=69", browseName="NamespaceVersion", dataType=o6.String, value="1.02.0")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wot;i=70", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2025-12-05T00:00:00Z"))),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=wot;i=71", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wot;i=72", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wot;i=73", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["1:2147483647"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wot;i=74", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=wot;i=99", browseName="DefaultRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=wot;i=100", browseName="DefaultUserRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wot;i=101", browseName="DefaultAccessRestrictions", dataType=ns0.datatypes.AccessRestrictionType)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)


ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=107",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=106",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=wot;i=106", browseName="ns=wot;CloseAndUpdate", inputArgs=o6.hasProperty(o6.ns["ns=wot;i=107"]))

wot_objtypes.WoTAssetFileType(
    nodeId="ns=wot;i=43",
    browseName="ns=wot;WoTFile",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wot;i=44", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wot;i=45", browseName="Writable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wot;i=46", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wot;i=47", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasComponent(o6.ns["ns=wot;i=51"]),
        o6.hasComponent(o6.ns["ns=wot;i=54"]),
        o6.hasComponent(o6.ns["ns=wot;i=56"]),
        o6.hasComponent(o6.ns["ns=wot;i=59"]),
        o6.hasComponent(o6.ns["ns=wot;i=61"]),
        o6.hasComponent(o6.ns["ns=wot;i=64"]),
        o6.hasComponent(o6.ns["ns=wot;i=106"]),
    ],
)
o6.reference(wot_objtypes.IWoTAssetType, ns0.reftypes.HasComponent, o6.ns["ns=wot;i=43"])


ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=153",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=152",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=154",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=152",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=wot;i=152", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=wot;i=153"]), outputArgs=o6.hasProperty(o6.ns["ns=wot;i=154"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=156",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=155",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=wot;i=155", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=wot;i=156"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=158",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=157",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=159",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=157",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=wot;i=157", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=wot;i=158"]), outputArgs=o6.hasProperty(o6.ns["ns=wot;i=159"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=161",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=160",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=wot;i=160", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=wot;i=161"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=163",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=162",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=164",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=162",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=wot;i=162", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=wot;i=163"]), outputArgs=o6.hasProperty(o6.ns["ns=wot;i=164"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=166",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=165",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=wot;i=165", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=wot;i=166"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wot;i=168",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wot;i=167",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=wot;i=167", browseName="ns=wot;CloseAndUpdate", inputArgs=o6.hasProperty(o6.ns["ns=wot;i=168"]))

wot_objtypes.WoTAssetFileType(
    nodeId="ns=wot;i=144",
    browseName="ns=wot;WoTFile",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wot;i=145", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wot;i=146", browseName="Writable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wot;i=147", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wot;i=148", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasComponent(o6.ns["ns=wot;i=152"]),
        o6.hasComponent(o6.ns["ns=wot;i=155"]),
        o6.hasComponent(o6.ns["ns=wot;i=157"]),
        o6.hasComponent(o6.ns["ns=wot;i=160"]),
        o6.hasComponent(o6.ns["ns=wot;i=162"]),
        o6.hasComponent(o6.ns["ns=wot;i=165"]),
        o6.hasComponent(o6.ns["ns=wot;i=167"]),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=wot;i=2",
    browseName="ns=wot;<WoTAssetName>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wot;i=169", browseName="ns=wot;AssetEndpoint", dataType=o6.String)), o6.hasComponent(o6.ns["ns=wot;i=144"])],
)
o6.reference(wot_objtypes.WoTAssetConnectionManagementType, ns0.reftypes.Organizes, o6.ns["ns=wot;i=2"])
o6.reference(o6.ns["ns=wot;i=2"], "i=17603", wot_objtypes.IWoTAssetType)
o6.reference(o6.ns["ns=wot;i=2"], "ns=wot;i=142", o6.ns["ns=wot;i=66"])


del Any, TYPE_CHECKING, uuid, o6, ns0, wot_reftypes, wot_objtypes
