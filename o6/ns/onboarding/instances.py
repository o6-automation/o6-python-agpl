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

"""Generated OPC UA onboarding namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.gds as gds
import o6.ns.ns0 as ns0
from . import datatypes as onboarding_datypes
from . import objtypes as onboarding_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1191",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1190",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1192",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1190",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1190", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1191"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1192"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1194",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1193",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1193", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1194"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1196",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1195",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1197",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1195",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1195", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1196"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1197"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1199",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1198",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1198", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1199"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1201",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1200",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1202",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1200",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1200", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1201"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1202"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1204",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1203",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1203", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1204"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1209",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1208",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Masks", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1210",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1208",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=onboarding;i=1208", browseName="OpenWithMasks", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1209"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1210"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1212",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1211",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1213",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1211",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplyChangesRequired", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=onboarding;i=1211", browseName="CloseAndUpdate", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1212"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1213"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1215",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1214",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Certificate", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="IsTrustedCertificate", dataType=o6.Boolean, valueRank=-1),
    ],
)
o6.call(nodeId="ns=onboarding;i=1214", browseName="AddCertificate", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1215"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1217",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1216",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Thumbprint", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="IsTrustedCertificate", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1216", browseName="RemoveCertificate", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1217"]))

ns0.objtypes.TrustListType(
    nodeId="ns=onboarding;i=1182",
    browseName="ns=onboarding;TicketAuthorities",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1183", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1184", browseName="Writable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1185", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1186", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1205", browseName="LastUpdateTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasComponent(o6.ns["ns=onboarding;i=1190"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1193"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1195"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1198"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1200"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1203"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1208"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1211"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1214"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1216"]),
    ],
)
o6.reference(onboarding_objtypes.DeviceRegistrarAdminType, ns0.reftypes.HasComponent, o6.ns["ns=onboarding;i=1182"])


ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1227",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1226",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1228",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1226",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1226", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1227"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1228"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1230",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1229",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1229", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1230"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1232",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1231",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1233",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1231",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1231", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1232"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1233"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1235",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1234",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1234", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1235"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1237",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1236",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1238",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1236",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1236", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1237"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1238"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1240",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1239",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1239", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1240"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1245",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1244",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Masks", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1246",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1244",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=onboarding;i=1244", browseName="OpenWithMasks", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1245"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1246"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1248",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1247",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1249",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1247",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplyChangesRequired", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=onboarding;i=1247", browseName="CloseAndUpdate", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1248"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1249"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1251",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1250",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Certificate", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="IsTrustedCertificate", dataType=o6.Boolean, valueRank=-1),
    ],
)
o6.call(nodeId="ns=onboarding;i=1250", browseName="AddCertificate", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1251"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1253",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1252",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Thumbprint", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="IsTrustedCertificate", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1252", browseName="RemoveCertificate", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1253"]))

ns0.objtypes.TrustListType(
    nodeId="ns=onboarding;i=1218",
    browseName="ns=onboarding;DeviceIdentityAuthorities",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1219", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1220", browseName="Writable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1221", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1222", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1241", browseName="LastUpdateTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasComponent(o6.ns["ns=onboarding;i=1226"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1229"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1231"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1234"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1236"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1239"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1244"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1247"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1250"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1252"]),
    ],
)
o6.reference(onboarding_objtypes.DeviceRegistrarAdminType, ns0.reftypes.HasComponent, o6.ns["ns=onboarding;i=1218"])


ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1267",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1266",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Tickets", dataType=ns0.datatypes.EncodedTicket, valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1268",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1266",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Results", dataType=o6.StatusCode, valueRank=1, arrayDimensions=[0])],
)
o6.call(
    nodeId="ns=onboarding;i=1266",
    browseName="ns=onboarding;RegisterTickets",
    inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1267"]),
    outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1268"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1270",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1269",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Tickets", dataType=ns0.datatypes.EncodedTicket, valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1271",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1269",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Results", dataType=o6.StatusCode, valueRank=1, arrayDimensions=[0])],
)
o6.call(
    nodeId="ns=onboarding;i=1269",
    browseName="ns=onboarding;UnregisterTickets",
    inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1270"]),
    outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1271"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1281",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1280",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1282",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1280",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1280", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1281"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1282"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1284",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1283",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1283", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1284"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1286",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1285",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1287",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1285",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1285", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1286"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1287"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1289",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1288",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1288", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1289"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1291",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1290",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1292",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1290",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1290", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1291"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1292"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1294",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1293",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1293", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1294"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1299",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1298",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Masks", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1300",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1298",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=onboarding;i=1298", browseName="OpenWithMasks", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1299"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1300"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1302",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1301",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1303",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1301",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplyChangesRequired", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=onboarding;i=1301", browseName="CloseAndUpdate", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1302"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1303"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1305",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1304",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Certificate", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="IsTrustedCertificate", dataType=o6.Boolean, valueRank=-1),
    ],
)
o6.call(nodeId="ns=onboarding;i=1304", browseName="AddCertificate", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1305"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1307",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1306",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Thumbprint", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="IsTrustedCertificate", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1306", browseName="RemoveCertificate", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1307"]))

ns0.objtypes.TrustListType(
    nodeId="ns=onboarding;i=1272",
    browseName="ns=onboarding;TicketAuthorities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1273", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1274", browseName="Writable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1275", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1276", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1295", browseName="LastUpdateTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasComponent(o6.ns["ns=onboarding;i=1280"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1283"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1285"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1288"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1290"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1293"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1298"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1301"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1304"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1306"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1317",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1316",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1318",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1316",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1316", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1317"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1318"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1320",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1319",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1319", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1320"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1322",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1321",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1323",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1321",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1321", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1322"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1323"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1325",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1324",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1324", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1325"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1327",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1326",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1328",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1326",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1326", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1327"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1328"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1330",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1329",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1329", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1330"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1335",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1334",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Masks", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1336",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1334",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=onboarding;i=1334", browseName="OpenWithMasks", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1335"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1336"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1338",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1337",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1339",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1337",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplyChangesRequired", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=onboarding;i=1337", browseName="CloseAndUpdate", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1338"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1339"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1341",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1340",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Certificate", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="IsTrustedCertificate", dataType=o6.Boolean, valueRank=-1),
    ],
)
o6.call(nodeId="ns=onboarding;i=1340", browseName="AddCertificate", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1341"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1343",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=onboarding;i=1342",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Thumbprint", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="IsTrustedCertificate", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1342", browseName="RemoveCertificate", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1343"]))

ns0.objtypes.TrustListType(
    nodeId="ns=onboarding;i=1308",
    browseName="ns=onboarding;DeviceIdentityAuthorities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1309", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1310", browseName="Writable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1311", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1312", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1331", browseName="LastUpdateTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasComponent(o6.ns["ns=onboarding;i=1316"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1319"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1321"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1324"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1326"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1329"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1334"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1337"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1340"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1342"]),
    ],
)
onboarding_objtypes.DeviceRegistrarAdminType(
    nodeId="ns=onboarding;i=1265",
    browseName="ns=onboarding;Administration",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=onboarding;i=1266"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1269"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1272"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1308"]),
    ],
)
o6.reference(onboarding_objtypes.DeviceRegistrarType, ns0.reftypes.HasComponent, o6.ns["ns=onboarding;i=1265"])


ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1346",
    browseName="InputArguments",
    parent="ns=onboarding;i=1345",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="Identities", dataType=o6.ByteString, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="Issuers", dataType=o6.ByteString, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="Tickets", dataType=ns0.datatypes.EncodedTicket, valueRank=1, arrayDimensions=[0]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1347",
    browseName="OutputArguments",
    parent="ns=onboarding;i=1345",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="SelectedIdentity", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="MatchingTicket", dataType=o6.NodeId("ns=onboarding;i=1165"), valueRank=-1),
        ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="SoftwareUpdateManager", dataType=o6.NodeId("ns=onboarding;i=1495"), valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=onboarding;i=1345",
    browseName="ns=onboarding;ProvideIdentities",
    inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1346"]),
    outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1347"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1349",
    browseName="InputArguments",
    parent="ns=onboarding;i=1348",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Application", dataType=ns0.datatypes.ApplicationDescription, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1348", browseName="ns=onboarding;RegisterDeviceEndpoint", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1349"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1352",
    browseName="InputArguments",
    parent="ns=onboarding;i=1351",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Tickets", dataType=ns0.datatypes.EncodedTicket, valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1353",
    browseName="OutputArguments",
    parent="ns=onboarding;i=1351",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Results", dataType=o6.StatusCode, valueRank=1, arrayDimensions=[0])],
)
o6.call(
    nodeId="ns=onboarding;i=1351",
    browseName="ns=onboarding;RegisterTickets",
    inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1352"]),
    outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1353"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1355",
    browseName="InputArguments",
    parent="ns=onboarding;i=1354",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Tickets", dataType=ns0.datatypes.EncodedTicket, valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1356",
    browseName="OutputArguments",
    parent="ns=onboarding;i=1354",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Results", dataType=o6.StatusCode, valueRank=1, arrayDimensions=[0])],
)
o6.call(
    nodeId="ns=onboarding;i=1354",
    browseName="ns=onboarding;UnregisterTickets",
    inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1355"]),
    outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1356"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1366",
    browseName="InputArguments",
    parent="ns=onboarding;i=1365",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1367",
    browseName="OutputArguments",
    parent="ns=onboarding;i=1365",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1365", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1366"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1367"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1369",
    browseName="InputArguments",
    parent="ns=onboarding;i=1368",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1368", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1369"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1371",
    browseName="InputArguments",
    parent="ns=onboarding;i=1370",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1372",
    browseName="OutputArguments",
    parent="ns=onboarding;i=1370",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1370", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1371"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1372"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1374",
    browseName="InputArguments",
    parent="ns=onboarding;i=1373",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1373", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1374"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1376",
    browseName="InputArguments",
    parent="ns=onboarding;i=1375",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1377",
    browseName="OutputArguments",
    parent="ns=onboarding;i=1375",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1375", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1376"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1377"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1379",
    browseName="InputArguments",
    parent="ns=onboarding;i=1378",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1378", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1379"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1384",
    browseName="InputArguments",
    parent="ns=onboarding;i=1383",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Masks", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1385",
    browseName="OutputArguments",
    parent="ns=onboarding;i=1383",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=onboarding;i=1383", browseName="OpenWithMasks", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1384"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1385"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1387",
    browseName="InputArguments",
    parent="ns=onboarding;i=1386",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1388",
    browseName="OutputArguments",
    parent="ns=onboarding;i=1386",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplyChangesRequired", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=onboarding;i=1386", browseName="CloseAndUpdate", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1387"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1388"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1390",
    browseName="InputArguments",
    parent="ns=onboarding;i=1389",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Certificate", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="IsTrustedCertificate", dataType=o6.Boolean, valueRank=-1),
    ],
)
o6.call(nodeId="ns=onboarding;i=1389", browseName="AddCertificate", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1390"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1392",
    browseName="InputArguments",
    parent="ns=onboarding;i=1391",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Thumbprint", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="IsTrustedCertificate", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1391", browseName="RemoveCertificate", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1392"]))

ns0.objtypes.TrustListType(
    nodeId="ns=onboarding;i=1357",
    browseName="ns=onboarding;TicketAuthorities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1358", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1359", browseName="Writable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1360", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1361", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1380", browseName="LastUpdateTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasComponent(o6.ns["ns=onboarding;i=1365"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1368"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1370"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1373"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1375"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1378"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1383"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1386"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1389"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1391"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1402",
    browseName="InputArguments",
    parent="ns=onboarding;i=1401",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1403",
    browseName="OutputArguments",
    parent="ns=onboarding;i=1401",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1401", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1402"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1403"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1405",
    browseName="InputArguments",
    parent="ns=onboarding;i=1404",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1404", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1405"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1407",
    browseName="InputArguments",
    parent="ns=onboarding;i=1406",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1408",
    browseName="OutputArguments",
    parent="ns=onboarding;i=1406",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1406", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1407"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1408"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1410",
    browseName="InputArguments",
    parent="ns=onboarding;i=1409",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1409", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1410"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1412",
    browseName="InputArguments",
    parent="ns=onboarding;i=1411",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1413",
    browseName="OutputArguments",
    parent="ns=onboarding;i=1411",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1411", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1412"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1413"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1415",
    browseName="InputArguments",
    parent="ns=onboarding;i=1414",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1414", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1415"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1420",
    browseName="InputArguments",
    parent="ns=onboarding;i=1419",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Masks", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1421",
    browseName="OutputArguments",
    parent="ns=onboarding;i=1419",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=onboarding;i=1419", browseName="OpenWithMasks", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1420"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1421"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1423",
    browseName="InputArguments",
    parent="ns=onboarding;i=1422",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1424",
    browseName="OutputArguments",
    parent="ns=onboarding;i=1422",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplyChangesRequired", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=onboarding;i=1422", browseName="CloseAndUpdate", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1423"]), outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1424"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1426",
    browseName="InputArguments",
    parent="ns=onboarding;i=1425",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Certificate", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="IsTrustedCertificate", dataType=o6.Boolean, valueRank=-1),
    ],
)
o6.call(nodeId="ns=onboarding;i=1425", browseName="AddCertificate", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1426"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1428",
    browseName="InputArguments",
    parent="ns=onboarding;i=1427",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Thumbprint", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="IsTrustedCertificate", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=1427", browseName="RemoveCertificate", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1428"]))

ns0.objtypes.TrustListType(
    nodeId="ns=onboarding;i=1393",
    browseName="ns=onboarding;DeviceIdentityAuthorities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1394", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1395", browseName="Writable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1396", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1397", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1416", browseName="LastUpdateTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasComponent(o6.ns["ns=onboarding;i=1401"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1404"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1406"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1409"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1411"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1414"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1419"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1422"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1425"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1427"]),
    ],
)
onboarding_objtypes.DeviceRegistrarAdminType(
    nodeId="ns=onboarding;i=1350",
    browseName="ns=onboarding;Administration",
    references=[
        o6.hasComponent(o6.ns["ns=onboarding;i=1351"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1354"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1357"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1393"]),
    ],
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=onboarding;i=1439", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=onboarding;i=1440", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=onboarding;i=1441", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=onboarding;i=1442", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=onboarding;i=1443", browseName="Default Binary")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=onboarding;i=1448", browseName="ns=onboarding;CertificateAuthorityType", dataType=o6.String, value="CertificateAuthorityType")
o6.reference(o6.ns["ns=onboarding;i=1439"], "i=39", o6.ns["ns=onboarding;i=1448"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=onboarding;i=1451", browseName="ns=onboarding;BaseTicketType", dataType=o6.String, value="BaseTicketType")
o6.reference(o6.ns["ns=onboarding;i=1440"], "i=39", o6.ns["ns=onboarding;i=1451"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=onboarding;i=1454", browseName="ns=onboarding;DeviceIdentityTicketType", dataType=o6.String, value="DeviceIdentityTicketType")
o6.reference(o6.ns["ns=onboarding;i=1441"], "i=39", o6.ns["ns=onboarding;i=1454"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=onboarding;i=1457", browseName="ns=onboarding;CompositeIdentityTicketType", dataType=o6.String, value="CompositeIdentityTicketType")
o6.reference(o6.ns["ns=onboarding;i=1442"], "i=39", o6.ns["ns=onboarding;i=1457"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=onboarding;i=1460", browseName="ns=onboarding;TicketListType", dataType=o6.String, value="TicketListType")
o6.reference(o6.ns["ns=onboarding;i=1443"], "i=39", o6.ns["ns=onboarding;i=1460"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=onboarding;i=1463", browseName="Default XML")
o6.hasEncoding(onboarding_datypes.CertificateAuthorityType, o6.ns["ns=onboarding;i=1463"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=onboarding;i=1464", browseName="Default XML")
o6.hasEncoding(onboarding_datypes.BaseTicketType, o6.ns["ns=onboarding;i=1464"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=onboarding;i=1465", browseName="Default XML")
o6.hasEncoding(onboarding_datypes.DeviceIdentityTicketType, o6.ns["ns=onboarding;i=1465"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=onboarding;i=1466", browseName="Default XML")
o6.hasEncoding(onboarding_datypes.CompositeIdentityTicketType, o6.ns["ns=onboarding;i=1466"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=onboarding;i=1467", browseName="Default XML")
o6.hasEncoding(onboarding_datypes.TicketListType, o6.ns["ns=onboarding;i=1467"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=onboarding;i=1472", browseName="ns=onboarding;CertificateAuthorityType", dataType=o6.String, value="//xs:element[@name='CertificateAuthorityType']"
)
o6.reference(o6.ns["ns=onboarding;i=1463"], "i=39", o6.ns["ns=onboarding;i=1472"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=onboarding;i=1475", browseName="ns=onboarding;BaseTicketType", dataType=o6.String, value="//xs:element[@name='BaseTicketType']")
o6.reference(o6.ns["ns=onboarding;i=1464"], "i=39", o6.ns["ns=onboarding;i=1475"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=onboarding;i=1478", browseName="ns=onboarding;DeviceIdentityTicketType", dataType=o6.String, value="//xs:element[@name='DeviceIdentityTicketType']"
)
o6.reference(o6.ns["ns=onboarding;i=1465"], "i=39", o6.ns["ns=onboarding;i=1478"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=onboarding;i=1481", browseName="ns=onboarding;CompositeIdentityTicketType", dataType=o6.String, value="//xs:element[@name='CompositeIdentityTicketType']"
)
o6.reference(o6.ns["ns=onboarding;i=1466"], "i=39", o6.ns["ns=onboarding;i=1481"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=onboarding;i=1484", browseName="ns=onboarding;TicketListType", dataType=o6.String, value="//xs:element[@name='TicketListType']")
o6.reference(o6.ns["ns=onboarding;i=1467"], "i=39", o6.ns["ns=onboarding;i=1484"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=onboarding;i=1487", browseName="Default JSON")
o6.hasEncoding(onboarding_datypes.CertificateAuthorityType, o6.ns["ns=onboarding;i=1487"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=onboarding;i=1488", browseName="Default JSON")
o6.hasEncoding(onboarding_datypes.BaseTicketType, o6.ns["ns=onboarding;i=1488"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=onboarding;i=1489", browseName="Default JSON")
o6.hasEncoding(onboarding_datypes.DeviceIdentityTicketType, o6.ns["ns=onboarding;i=1489"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=onboarding;i=1490", browseName="Default JSON")
o6.hasEncoding(onboarding_datypes.CompositeIdentityTicketType, o6.ns["ns=onboarding;i=1490"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=onboarding;i=1491", browseName="Default JSON")
o6.hasEncoding(onboarding_datypes.TicketListType, o6.ns["ns=onboarding;i=1491"])


ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1511",
    browseName="InputArguments",
    parent="ns=onboarding;i=1510",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ProductInstanceUri", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Status", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="SoftwareRevision", dataType=o6.String, valueRank=-1),
    ],
)
o6.call(nodeId="ns=onboarding;i=1510", browseName="ns=onboarding;UpdateSoftwareStatus", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1511"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1513",
    browseName="OutputArguments",
    parent="ns=onboarding;i=1512",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Managers", dataType=o6.NodeId("ns=onboarding;i=1495"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=onboarding;i=1512", browseName="ns=onboarding;GetManagers", outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1513"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1515",
    browseName="InputArguments",
    parent="ns=onboarding;i=1514",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Application", dataType=o6.NodeId("ns=gds;i=1"), valueRank=-1),
        ns0.datatypes.Argument(name="ProtocolUri", dataType=ns0.datatypes.UriString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=1516",
    browseName="OutputArguments",
    parent="ns=onboarding;i=1514",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=onboarding;i=1514",
    browseName="ns=onboarding;RegisterManagedApplication",
    inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1515"]),
    outputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=1516"]),
)

deviceRegistrar = onboarding_objtypes.DeviceRegistrarType(
    nodeId="ns=onboarding;i=1344",
    browseName="ns=onboarding;DeviceRegistrar",
    references=[
        o6.hasComponent(o6.ns["ns=onboarding;i=1345"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1348"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1350"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1510"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1512"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1514"]),
    ],
    parent="i=85",
    referenceType=ns0.reftypes.Organizes,
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=onboarding;i=4206", browseName="Default Binary")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=onboarding;i=4208", browseName="ns=onboarding;ManagerDescription", dataType=o6.String, value="ManagerDescription")
o6.reference(o6.ns["ns=onboarding;i=4206"], "i=39", o6.ns["ns=onboarding;i=4208"])
opcDotUaDotOnboarding = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=onboarding;i=1444",
    browseName="ns=onboarding;Opc.Ua.Onboarding",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1446", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Onboarding/")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1447", browseName="Deprecated", dataType=o6.Boolean)
        ),
        o6.hasComponent(o6.ns["ns=onboarding;i=1448"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1451"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1454"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1457"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1460"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=4208"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary\r\n  xmlns:GDS="http://opcfoundation.org/UA/GDS/"\r\n  xmlns:opc="http://opcfoundation.org/BinarySchema/"\r\n  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\r\n  xmlns:ua="http://opcfoundation.org/UA/"\r\n  xmlns:tns="http://opcfoundation.org/UA/Onboarding/"\r\n  DefaultByteOrder="LittleEndian"\r\n  TargetNamespace="http://opcfoundation.org/UA/Onboarding/"\r\n>\r\n  <opc:Import Namespace="http://opcfoundation.org/UA/GDS/" Location="Opc.Ua.Gds.BinarySchema.bsd"/>\r\n  <opc:Import Namespace="http://opcfoundation.org/UA/" Location="Opc.Ua.BinarySchema.bsd"/>\r\n\r\n  <opc:StructuredType Name="CertificateAuthorityType" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="AuthorityCertificate" TypeName="opc:ByteString" />\r\n    <opc:Field Name="NoOfIssuerCertificates" TypeName="opc:Int32" />\r\n    <opc:Field Name="IssuerCertificates" TypeName="opc:ByteString" LengthField="NoOfIssuerCertificates" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="BaseTicketType" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="ManufacturerName" TypeName="opc:String" />\r\n    <opc:Field Name="ModelName" TypeName="opc:String" />\r\n    <opc:Field Name="ModelVersion" TypeName="opc:String" />\r\n    <opc:Field Name="HardwareRevision" TypeName="opc:String" />\r\n    <opc:Field Name="SoftwareRevision" TypeName="opc:String" />\r\n    <opc:Field Name="SerialNumber" TypeName="opc:String" />\r\n    <opc:Field Name="ManufactureDate" TypeName="opc:DateTime" />\r\n    <opc:Field Name="NoOfAuthorities" TypeName="opc:Int32" />\r\n    <opc:Field Name="Authorities" TypeName="tns:CertificateAuthorityType" LengthField="NoOfAuthorities" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="DeviceIdentityTicketType" BaseType="tns:BaseTicketType">\r\n    <opc:Field Name="ManufacturerName" TypeName="opc:String" SourceType="tns:BaseTicketType" />\r\n    <opc:Field Name="ModelName" TypeName="opc:String" SourceType="tns:BaseTicketType" />\r\n    <opc:Field Name="ModelVersion" TypeName="opc:String" SourceType="tns:BaseTicketType" />\r\n    <opc:Field Name="HardwareRevision" TypeName="opc:String" SourceType="tns:BaseTicketType" />\r\n    <opc:Field Name="SoftwareRevision" TypeName="opc:String" SourceType="tns:BaseTicketType" />\r\n    <opc:Field Name="SerialNumber" TypeName="opc:String" SourceType="tns:BaseTicketType" />\r\n    <opc:Field Name="ManufactureDate" TypeName="opc:DateTime" SourceType="tns:BaseTicketType" />\r\n    <opc:Field Name="NoOfAuthorities" TypeName="opc:Int32" />\r\n    <opc:Field Name="Authorities" TypeName="tns:CertificateAuthorityType" LengthField="NoOfAuthorities" />\r\n    <opc:Field Name="ProductInstanceUri" TypeName="opc:String" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="CompositeIdentityTicketType" BaseType="tns:BaseTicketType">\r\n    <opc:Field Name="ManufacturerName" TypeName="opc:String" SourceType="tns:BaseTicketType" />\r\n    <opc:Field Name="ModelName" TypeName="opc:String" SourceType="tns:BaseTicketType" />\r\n    <opc:Field Name="ModelVersion" TypeName="opc:String" SourceType="tns:BaseTicketType" />\r\n    <opc:Field Name="HardwareRevision" TypeName="opc:String" SourceType="tns:BaseTicketType" />\r\n    <opc:Field Name="SoftwareRevision" TypeName="opc:String" SourceType="tns:BaseTicketType" />\r\n    <opc:Field Name="SerialNumber" TypeName="opc:String" SourceType="tns:BaseTicketType" />\r\n    <opc:Field Name="ManufactureDate" TypeName="opc:DateTime" SourceType="tns:BaseTicketType" />\r\n    <opc:Field Name="NoOfAuthorities" TypeName="opc:Int32" />\r\n    <opc:Field Name="Authorities" TypeName="tns:CertificateAuthorityType" LengthField="NoOfAuthorities" />\r\n    <opc:Field Name="CompositeInstanceUri" TypeName="opc:String" />\r\n    <opc:Field Name="NoOfDevices" TypeName="opc:Int32" />\r\n    <opc:Field Name="Devices" TypeName="opc:String" LengthField="NoOfDevices" />\r\n    <opc:Field Name="NoOfComposites" TypeName="opc:Int32" />\r\n    <opc:Field Name="Composites" TypeName="opc:String" LengthField="NoOfComposites" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="TicketListType" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="NoOfDevices" TypeName="opc:Int32" />\r\n    <opc:Field Name="Devices" TypeName="opc:String" LengthField="NoOfDevices" />\r\n    <opc:Field Name="NoOfComposites" TypeName="opc:Int32" />\r\n    <opc:Field Name="Composites" TypeName="opc:String" LengthField="NoOfComposites" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="ManagerDescription" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="Name" TypeName="ua:LocalizedText" />\r\n    <opc:Field Name="IsRequired" TypeName="opc:Boolean" />\r\n    <opc:Field Name="PurposeUri" TypeName="opc:String" />\r\n    <opc:Field Name="ProtocolUri" TypeName="opc:String" />\r\n    <opc:Field Name="NoOfEndpointUrls" TypeName="opc:Int32" />\r\n    <opc:Field Name="EndpointUrls" TypeName="opc:String" LengthField="NoOfEndpointUrls" />\r\n  </opc:StructuredType>\r\n\r\n</opc:TypeDictionary>',
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=onboarding;i=4214", browseName="Default XML")
o6.hasEncoding(onboarding_datypes.ManagerDescription, o6.ns["ns=onboarding;i=4214"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=onboarding;i=4216", browseName="ns=onboarding;ManagerDescription", dataType=o6.String, value="//xs:element[@name='ManagerDescription']"
)
o6.reference(o6.ns["ns=onboarding;i=4214"], "i=39", o6.ns["ns=onboarding;i=4216"])
opcDotUaDotOnboarding_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=onboarding;i=1468",
    browseName="ns=onboarding;Opc.Ua.Onboarding",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1470", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Onboarding/Types.xsd")
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=1471", browseName="Deprecated", dataType=o6.Boolean)
        ),
        o6.hasComponent(o6.ns["ns=onboarding;i=1472"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1475"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1478"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1481"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=1484"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=4216"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema\r\n  xmlns:GDS="http://opcfoundation.org/UA/GDS/Types.xsd"\r\n  xmlns:xs="http://www.w3.org/2001/XMLSchema"\r\n  xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd"\r\n  xmlns:tns="http://opcfoundation.org/UA/Onboarding/Types.xsd"\r\n  targetNamespace="http://opcfoundation.org/UA/Onboarding/Types.xsd"\r\n  elementFormDefault="qualified"\r\n>\r\n  <xs:annotation>\r\n    <xs:appinfo>\r\n      <ua:Model ModelUri="http://opcfoundation.org/UA/Onboarding/" Version="1.05.04" PublicationDate="2025-01-08T00:00:00Z" />\r\n    </xs:appinfo>\r\n  </xs:annotation>\r\n  \r\n  <xs:import namespace="http://opcfoundation.org/UA/GDS/Types.xsd" />\r\n  <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd" />\r\n\r\n  <xs:complexType name="CertificateAuthorityType">\r\n    <xs:sequence>\r\n      <xs:element name="AuthorityCertificate" type="xs:base64Binary" minOccurs="0" nillable="true" />\r\n      <xs:element name="IssuerCertificates" type="ua:ListOfByteString" minOccurs="0" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="CertificateAuthorityType" type="tns:CertificateAuthorityType" />\r\n\r\n  <xs:complexType name="ListOfCertificateAuthorityType">\r\n    <xs:sequence>\r\n      <xs:element name="CertificateAuthorityType" type="tns:CertificateAuthorityType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfCertificateAuthorityType" type="tns:ListOfCertificateAuthorityType" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="BaseTicketType">\r\n    <xs:sequence>\r\n      <xs:element name="ManufacturerName" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="ModelName" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="ModelVersion" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="HardwareRevision" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="SoftwareRevision" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="SerialNumber" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="ManufactureDate" type="xs:dateTime" minOccurs="0" />\r\n      <xs:element name="Authorities" type="tns:ListOfCertificateAuthorityType" minOccurs="0" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="BaseTicketType" type="tns:BaseTicketType" />\r\n\r\n  <xs:complexType name="ListOfBaseTicketType">\r\n    <xs:sequence>\r\n      <xs:element name="BaseTicketType" type="tns:BaseTicketType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfBaseTicketType" type="tns:ListOfBaseTicketType" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="DeviceIdentityTicketType">\r\n    <xs:complexContent mixed="false">\r\n      <xs:extension base="tns:BaseTicketType">\r\n        <xs:sequence>\r\n          <xs:element name="ProductInstanceUri" type="xs:string" minOccurs="0" nillable="true" />\r\n        </xs:sequence>\r\n      </xs:extension>\r\n    </xs:complexContent>\r\n  </xs:complexType>\r\n  <xs:element name="DeviceIdentityTicketType" type="tns:DeviceIdentityTicketType" />\r\n\r\n  <xs:complexType name="ListOfDeviceIdentityTicketType">\r\n    <xs:sequence>\r\n      <xs:element name="DeviceIdentityTicketType" type="tns:DeviceIdentityTicketType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfDeviceIdentityTicketType" type="tns:ListOfDeviceIdentityTicketType" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="CompositeIdentityTicketType">\r\n    <xs:complexContent mixed="false">\r\n      <xs:extension base="tns:BaseTicketType">\r\n        <xs:sequence>\r\n          <xs:element name="CompositeInstanceUri" type="xs:string" minOccurs="0" nillable="true" />\r\n          <xs:element name="Devices" type="ua:ListOfString" minOccurs="0" nillable="true" />\r\n          <xs:element name="Composites" type="ua:ListOfString" minOccurs="0" nillable="true" />\r\n        </xs:sequence>\r\n      </xs:extension>\r\n    </xs:complexContent>\r\n  </xs:complexType>\r\n  <xs:element name="CompositeIdentityTicketType" type="tns:CompositeIdentityTicketType" />\r\n\r\n  <xs:complexType name="ListOfCompositeIdentityTicketType">\r\n    <xs:sequence>\r\n      <xs:element name="CompositeIdentityTicketType" type="tns:CompositeIdentityTicketType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfCompositeIdentityTicketType" type="tns:ListOfCompositeIdentityTicketType" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="TicketListType">\r\n    <xs:sequence>\r\n      <xs:element name="Devices" type="ua:ListOfString" minOccurs="0" nillable="true" />\r\n      <xs:element name="Composites" type="ua:ListOfString" minOccurs="0" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="TicketListType" type="tns:TicketListType" />\r\n\r\n  <xs:complexType name="ListOfTicketListType">\r\n    <xs:sequence>\r\n      <xs:element name="TicketListType" type="tns:TicketListType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfTicketListType" type="tns:ListOfTicketListType" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="ManagerDescription">\r\n    <xs:sequence>\r\n      <xs:element name="Name" type="ua:LocalizedText" minOccurs="0" nillable="true" />\r\n      <xs:element name="IsRequired" type="xs:boolean" minOccurs="0" />\r\n      <xs:element name="PurposeUri" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="ProtocolUri" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="EndpointUrls" type="ua:ListOfString" minOccurs="0" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ManagerDescription" type="tns:ManagerDescription" />\r\n\r\n  <xs:complexType name="ListOfManagerDescription">\r\n    <xs:sequence>\r\n      <xs:element name="ManagerDescription" type="tns:ManagerDescription" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfManagerDescription" type="tns:ListOfManagerDescription" nillable="true"></xs:element>\r\n\r\n</xs:schema>',
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=onboarding;i=4222", browseName="Default JSON")
o6.hasEncoding(onboarding_datypes.ManagerDescription, o6.ns["ns=onboarding;i=4222"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashOnboardingSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=onboarding;i=1",
    browseName="ns=onboarding;http://opcfoundation.org/UA/Onboarding/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=2", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Onboarding/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=3", browseName="NamespaceVersion", dataType=o6.String, value="1.05.04")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=4", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2025-01-08T00:00:00Z"))
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=5", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=onboarding;i=6", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=onboarding;i=7", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["1:2147483647"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=8", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=33", browseName="DefaultRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=onboarding;i=34", browseName="DefaultUserRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=35", browseName="DefaultAccessRestrictions", dataType=ns0.datatypes.AccessRestrictionType)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=4986", browseName="ns=onboarding;ModelVersion", dataType=ns0.datatypes.SemanticVersionString, value="1.5.4")
        ),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)


ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=5042",
    browseName="InputArguments",
    parent="ns=onboarding;i=5041",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Rule", dataType=ns0.datatypes.IdentityMappingRuleType, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=5041", browseName="ns=onboarding;AddIdentity", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=5042"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=5044",
    browseName="InputArguments",
    parent="ns=onboarding;i=5043",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Rule", dataType=ns0.datatypes.IdentityMappingRuleType, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=5043", browseName="ns=onboarding;RemoveIdentity", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=5044"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=5046",
    browseName="InputArguments",
    parent="ns=onboarding;i=5045",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationUri", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=5045", browseName="ns=onboarding;AddApplication", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=5046"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=5048",
    browseName="InputArguments",
    parent="ns=onboarding;i=5047",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationUri", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=5047", browseName="ns=onboarding;RemoveApplication", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=5048"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=5050",
    browseName="InputArguments",
    parent="ns=onboarding;i=5049",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Endpoint", dataType=ns0.datatypes.EndpointType, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=5049", browseName="ns=onboarding;AddEndpoint", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=5050"]))

ns0.vartypes.PropertyType(
    nodeId="ns=onboarding;i=5052",
    browseName="InputArguments",
    parent="ns=onboarding;i=5051",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Endpoint", dataType=ns0.datatypes.EndpointType, valueRank=-1)],
)
o6.call(nodeId="ns=onboarding;i=5051", browseName="ns=onboarding;RemoveEndpoint", inputArgs=o6.hasProperty(o6.ns["ns=onboarding;i=5052"]))

registrarAdmin = ns0.objtypes.RoleType(
    nodeId="ns=onboarding;i=5034",
    browseName="ns=onboarding;RegistrarAdmin",
    description="Has rights to manage the Registrar and approve Devices when automatic authentication was not possible.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=5035", browseName="Identities", dataType=ns0.datatypes.IdentityMappingRuleType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=5036", browseName="ns=onboarding;ApplicationsExclude", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=5037", browseName="ns=onboarding;Applications", dataType=o6.String, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=5038", browseName="ns=onboarding;EndpointsExclude", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=5039", browseName="ns=onboarding;Endpoints", dataType=ns0.datatypes.EndpointType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=onboarding;i=5040", browseName="ns=onboarding;CustomConfiguration", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=onboarding;i=5041"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=5043"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=5045"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=5047"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=5049"]),
        o6.hasComponent(o6.ns["ns=onboarding;i=5051"]),
    ],
    parent="i=15606",
    referenceType=ns0.reftypes.HasComponent,
)


del Any, TYPE_CHECKING, uuid, o6, gds, ns0, onboarding_datypes, onboarding_objtypes
