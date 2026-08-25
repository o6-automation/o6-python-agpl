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

"""Generated OPC UA auto_id namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import datatypes as auto_id_datypes
from . import vartypes as auto_id_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=auto_id;i=1004", browseName="ns=auto_id;AutoIdScanEventType", displayName="AutoIdScanEventType", isAbstract=True)
class AutoIdScanEventType(ns0.objtypes.BaseEventType):
    deviceName: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6049", browseName="ns=auto_id;DeviceName", dataType=o6.String))
    scanResult: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6024", browseName="ns=auto_id;ScanResult", dataType=auto_id_datypes.ScanResult, valueRank=1)
    )


@o6.objecttype(nodeId="ns=auto_id;i=1005", browseName="ns=auto_id;OcrScanEventType", displayName="OcrScanEventType", isAbstract=True)
class OcrScanEventType(AutoIdScanEventType):
    scanResult: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6041", browseName="ns=auto_id;ScanResult", dataType=auto_id_datypes.OcrScanResult, valueRank=1)
    )


@o6.objecttype(nodeId="ns=auto_id;i=1006", browseName="ns=auto_id;RfidScanEventType", displayName="RfidScanEventType", isAbstract=True)
class RfidScanEventType(AutoIdScanEventType):
    scanResult: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6042", browseName="ns=auto_id;ScanResult", dataType=auto_id_datypes.RfidScanResult, valueRank=1)
    )


@o6.objecttype(
    nodeId="ns=auto_id;i=1010", browseName="ns=auto_id;AutoIdDiagnosticsEventType", displayName="AutoIdDiagnosticsEventType", description="AutoID diagnostic data", isAbstract=True
)
class AutoIdDiagnosticsEventType(ns0.objtypes.BaseEventType):
    deviceName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6090", browseName="ns=auto_id;DeviceName", description="Name of the device of the diagnostic data.", dataType=o6.String)
    )


@o6.objecttype(
    nodeId="ns=auto_id;i=1017",
    browseName="ns=auto_id;AutoIdLogEntryEventType",
    displayName="AutoIdLogEntryEventType",
    description="One entry written to the log of the device.",
    isAbstract=True,
)
class AutoIdLogEntryEventType(AutoIdDiagnosticsEventType):
    pass


@o6.objecttype(
    nodeId="ns=auto_id;i=1015",
    browseName="ns=auto_id;AutoIdAccessEventType",
    displayName="AutoIdAccessEventType",
    description="Data of the access on one or more AutoID Identifier.",
    isAbstract=True,
)
class AutoIdAccessEventType(AutoIdDiagnosticsEventType):
    accessResult: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=auto_id;i=6091",
            browseName="ns=auto_id;AccessResult",
            description="Result values of the access.",
            dataType=auto_id_datypes.AccessResult,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    client: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6092", browseName="ns=auto_id;Client", description="Client which was the originator of the command.", dataType=o6.String)
    )
    command: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6093", browseName="ns=auto_id;Command", description="Access command", dataType=o6.String)
    )


@o6.objecttype(
    nodeId="ns=auto_id;i=1016",
    browseName="ns=auto_id;RfidAccessEventType",
    displayName="RfidAccessEventType",
    description="Data of the access on one or more Rfid Transponder.",
    isAbstract=True,
)
class RfidAccessEventType(AutoIdAccessEventType):
    accessResult: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=auto_id;i=6094",
            browseName="ns=auto_id;AccessResult",
            description="Result values of the access.",
            dataType=auto_id_datypes.RfidAccessResult,
            valueRank=1,
            arrayDimensions=[0],
        )
    )


@o6.objecttype(
    nodeId="ns=auto_id;i=1018",
    browseName="ns=auto_id;AutoIdPresenceEventType",
    displayName="AutoIdPresenceEventType",
    description="Current presence of AutoID Identifier.",
    isAbstract=True,
)
class AutoIdPresenceEventType(AutoIdDiagnosticsEventType):
    presence: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6095", browseName="ns=auto_id;Presence", description="Current presence of AutoID Identifier.", dataType=o6.UInt16)
    )


@o6.objecttype(nodeId="ns=auto_id;i=1009", browseName="ns=auto_id;OpticalScanEventType", displayName="OpticalScanEventType", isAbstract=True)
class OpticalScanEventType(AutoIdScanEventType):
    scanResult: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6147", browseName="ns=auto_id;ScanResult", dataType=auto_id_datypes.OpticalScanResult, valueRank=1)
    )


@o6.objecttype(nodeId="ns=auto_id;i=1013", browseName="ns=auto_id;OpticalVerifierScanEventType", displayName="OpticalVerifierScanEventType", isAbstract=True)
class OpticalVerifierScanEventType(OpticalScanEventType):
    scanResult: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6227", browseName="ns=auto_id;ScanResult", dataType=auto_id_datypes.OpticalVerifierScanResult, valueRank=1)
    )


@o6.objecttype(nodeId="ns=auto_id;i=1014", browseName="ns=auto_id;RtlsLocationEventType", displayName="RtlsLocationEventType", isAbstract=True)
class RtlsLocationEventType(AutoIdScanEventType):
    scanResult: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6228", browseName="ns=auto_id;ScanResult", dataType=auto_id_datypes.RtlsLocationResult, valueRank=1)
    )


ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6015",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Results", dataType=o6.NodeId("ns=auto_id;i=3002"), valueRank=1),
        ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("ns=auto_id;i=3013"), valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6027",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Settings", dataType=o6.NodeId("ns=auto_id;i=3010"), valueRank=-1)],
)
o6.call(nodeId="ns=auto_id;i=7001", browseName="ns=auto_id;Scan", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6027"]), outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6015"]))

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6001",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Results", dataType=o6.NodeId("ns=auto_id;i=3001"), valueRank=1),
        ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("ns=auto_id;i=3013"), valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6050",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Settings", dataType=o6.NodeId("ns=auto_id;i=3010"), valueRank=-1)],
)
o6.call(nodeId="ns=auto_id;i=7008", browseName="ns=auto_id;Scan", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6050"]), outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6001"]))

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6051",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Settings", dataType=o6.NodeId("ns=auto_id;i=3010"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6208",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("ns=auto_id;i=3013"), valueRank=-1)],
)
o6.call(nodeId="ns=auto_id;i=7009", browseName="ns=auto_id;ScanStart", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6051"]), outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6208"]))

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6043",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Results", dataType=o6.NodeId("ns=auto_id;i=3007"), valueRank=1),
        ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("ns=auto_id;i=3013"), valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6052",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Setting", dataType=o6.NodeId("ns=auto_id;i=3010"), valueRank=-1)],
)
o6.call(nodeId="ns=auto_id;i=7013", browseName="ns=auto_id;Scan", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6052"]), outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6043"]))

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6054",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.Argument(name="Identifier", dataType=o6.NodeId("ns=auto_id;i=3020"), valueRank=-1),
        ns0.datatypes.Argument(name="CodeType", dataType=o6.NodeId("ns=auto_id;i=3031"), valueRank=-1),
        ns0.datatypes.Argument(name="Region", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="Offset", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="Length", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="Password", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6056",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ResultData", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("ns=auto_id;i=3013"), valueRank=-1),
    ],
)
o6.call(nodeId="ns=auto_id;i=7014", browseName="ns=auto_id;ReadTag", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6054"]), outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6056"]))

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6057",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.Argument(name="Identifier", dataType=o6.NodeId("ns=auto_id;i=3020"), valueRank=-1),
        ns0.datatypes.Argument(name="CodeType", dataType=o6.NodeId("ns=auto_id;i=3031"), valueRank=-1),
        ns0.datatypes.Argument(name="Region", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="Offset", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="Password", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6058",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("ns=auto_id;i=3013"), valueRank=-1)],
)
o6.call(nodeId="ns=auto_id;i=7015", browseName="ns=auto_id;WriteTag", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6057"]), outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6058"]))

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6059",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="Identifier", dataType=o6.NodeId("ns=auto_id;i=3020"), valueRank=-1),
        ns0.datatypes.Argument(name="CodeType", dataType=o6.NodeId("ns=auto_id;i=3031"), valueRank=-1),
        ns0.datatypes.Argument(name="PasswordType", dataType=o6.NodeId("ns=auto_id;i=3014"), valueRank=-1),
        ns0.datatypes.Argument(name="AccessPassword", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="NewPassword", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6060",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("ns=auto_id;i=3013"), valueRank=-1)],
)
o6.call(
    nodeId="ns=auto_id;i=7016", browseName="ns=auto_id;SetTagPassword", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6059"]), outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6060"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6062",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="Identifier", dataType=o6.NodeId("ns=auto_id;i=3020"), valueRank=-1),
        ns0.datatypes.Argument(name="CodeType", dataType=o6.NodeId("ns=auto_id;i=3031"), valueRank=-1),
        ns0.datatypes.Argument(name="KillPassword", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6063",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("ns=auto_id;i=3013"), valueRank=-1)],
)
o6.call(nodeId="ns=auto_id;i=7017", browseName="ns=auto_id;KillTag", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6062"]), outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6063"]))

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6064",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.Argument(name="Identifier", dataType=o6.NodeId("ns=auto_id;i=3020"), valueRank=-1),
        ns0.datatypes.Argument(name="CodeType", dataType=o6.NodeId("ns=auto_id;i=3031"), valueRank=-1),
        ns0.datatypes.Argument(name="Password", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="Region", dataType=o6.NodeId("ns=auto_id;i=3015"), valueRank=-1),
        ns0.datatypes.Argument(name="Lock", dataType=o6.NodeId("ns=auto_id;i=3016"), valueRank=-1),
        ns0.datatypes.Argument(name="Offset", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="Length", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6065",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("ns=auto_id;i=3013"), valueRank=-1)],
)
o6.call(nodeId="ns=auto_id;i=7018", browseName="ns=auto_id;LockTag", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6064"]), outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6065"]))

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6137",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.Argument(name="Identifier", dataType=o6.NodeId("ns=auto_id;i=3020"), valueRank=-1),
        ns0.datatypes.Argument(name="CodeType", dataType=o6.NodeId("ns=auto_id;i=3031"), valueRank=-1),
        ns0.datatypes.Argument(name="NewUId", dataType=o6.ByteString, valueRank=-1),
        ns0.datatypes.Argument(name="AFI", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="Toggle", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="Password", dataType=o6.ByteString, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6140",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("ns=auto_id;i=3013"), valueRank=-1)],
)
o6.call(nodeId="ns=auto_id;i=7023", browseName="ns=auto_id;WriteTagID", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6137"]), outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6140"]))

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6129",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7042",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Location", dataType=o6.NodeId("ns=auto_id;i=3008"), valueRank=-1, description=o6.LocalizedText("Union of GPS, UTM or Local"))],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6130",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7042",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="LocationType", dataType=o6.NodeId("ns=auto_id;i=3009"), valueRank=-1)],
)
o6.call(
    nodeId="ns=auto_id;i=7042",
    browseName="ns=auto_id;GetDeviceLocation",
    inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6130"]),
    outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6129"]),
)


@o6.objecttype(nodeId="ns=auto_id;i=1001", browseName="ns=auto_id;AutoIdDeviceType", displayName="AutoIdDeviceType", isAbstract=True)
class AutoIdDeviceType(di.objtypes.DeviceType):
    autoIdModelVersion: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6193", browseName="ns=auto_id;AutoIdModelVersion", dataType=o6.String, value="1.01", accessLevel=3)
    )
    deviceInfo: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6026", browseName="ns=auto_id;DeviceInfo", description="Device status information.", dataType=o6.String, accessLevel=3)
    )
    deviceLocation: auto_id_vartypes.LocationVariableType | None = o6.hasComponent(
        auto_id_vartypes.LocationVariableType(
            nodeId="ns=auto_id;i=6128", browseName="ns=auto_id;DeviceLocation", description="Union of GPS, UTM, Local.", dataType=auto_id_datypes.Location, accessLevel=3
        )
    )
    deviceLocationName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=auto_id;i=6127", browseName="ns=auto_id;DeviceLocationName", description="Symbolic name of the device location.", dataType=o6.String, accessLevel=3
        )
    )
    deviceName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=auto_id;i=6124",
            browseName="ns=auto_id;DeviceName",
            description="Default could be also host name, IP address or MAC. This should be a field that can be configured for a device.",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    deviceStatus: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=auto_id;i=6030", browseName="ns=auto_id;DeviceStatus", dataType=auto_id_datypes.DeviceStatusEnumeration)
    )
    diagnostics: di.objtypes.FunctionalGroupType | None
    getDeviceLocation: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=auto_id;i=7042"])
    iOData: di.objtypes.FunctionalGroupType | None = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=auto_id;i=5054", browseName="ns=auto_id;IOData"))
    lastScanData: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=auto_id;i=6055", browseName="ns=auto_id;LastScanData", description="The last scanned AutoID Identifier.", accessLevel=3)
    )
    lastScanTimestamp: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=auto_id;i=6096",
            browseName="ns=auto_id;LastScanTimestamp",
            description="Point of time the last AutoID Identifier was scanned.",
            dataType=ns0.datatypes.UtcTime,
            accessLevel=3,
        )
    )
    runtimeParameters: di.objtypes.FunctionalGroupType | None
    scan: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=auto_id;i=7008"])
    scanActive: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=auto_id;i=6099", browseName="ns=auto_id;ScanActive", description="Triggers the scan process.", dataType=o6.Boolean, accessLevel=3
        )
    )
    scanStart: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=auto_id;i=7009"])
    scanStop: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=auto_id;i=7010", browseName="ns=auto_id;ScanStop"))


o6.reference(AutoIdDeviceType, "i=41", AutoIdScanEventType)
o6.reference(AutoIdDeviceType, "i=41", AutoIdAccessEventType)
o6.reference(AutoIdDeviceType, "i=41", AutoIdLogEntryEventType)
o6.reference(AutoIdDeviceType, "i=41", AutoIdPresenceEventType)


@o6.objecttype(nodeId="ns=auto_id;i=1002", browseName="ns=auto_id;OcrReaderDeviceType", displayName="OcrReaderDeviceType")
class OcrReaderDeviceType(AutoIdDeviceType):
    images: ns0.objtypes.FolderType | None
    runtimeParameters: di.objtypes.FunctionalGroupType | None
    scan: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=auto_id;i=7001"])


o6.reference(OcrReaderDeviceType, "i=41", OcrScanEventType)


@o6.objecttype(nodeId="ns=auto_id;i=1003", browseName="ns=auto_id;RfidReaderDeviceType", displayName="RfidReaderDeviceType")
class RfidReaderDeviceType(AutoIdDeviceType):
    antennaNames: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6048", browseName="ns=auto_id;AntennaNames", dataType=auto_id_datypes.AntennaNameIdPair, valueRank=1, accessLevel=3)
    )
    diagnostics: di.objtypes.FunctionalGroupType | None
    killTag: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=auto_id;i=7017"])
    lastScanAntenna: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=auto_id;i=6097",
            browseName="ns=auto_id;LastScanAntenna",
            description="ID of the antenna with which the last AutoID Identifier was scanned.",
            dataType=o6.Int32,
            accessLevel=3,
        )
    )
    lastScanRSSI: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=auto_id;i=6098",
            browseName="ns=auto_id;LastScanRSSI",
            description="RSSI Value with which the last AutoID Identifier was scanned.",
            dataType=o6.Int32,
            accessLevel=3,
        )
    )
    lockTag: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=auto_id;i=7018"])
    readTag: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=auto_id;i=7014"])
    runtimeParameters: di.objtypes.FunctionalGroupType | None
    scan: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=auto_id;i=7013"])
    setTagPassword: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=auto_id;i=7016"])
    writeTag: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=auto_id;i=7015"])
    writeTagID: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=auto_id;i=7023"])


o6.reference(RfidReaderDeviceType, "i=41", RfidScanEventType)
o6.reference(RfidReaderDeviceType, "i=41", RfidAccessEventType)


ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6144",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7043",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Settings", dataType=o6.NodeId("ns=auto_id;i=3010"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6145",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7043",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Results", dataType=o6.NodeId("ns=auto_id;i=3026"), valueRank=1),
        ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("ns=auto_id;i=3013"), valueRank=-1),
    ],
)
o6.call(nodeId="ns=auto_id;i=7043", browseName="ns=auto_id;Scan", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6144"]), outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6145"]))


@o6.objecttype(nodeId="ns=auto_id;i=1008", browseName="ns=auto_id;OpticalReaderDeviceType", displayName="OpticalReaderDeviceType")
class OpticalReaderDeviceType(AutoIdDeviceType):
    images: ns0.objtypes.FolderType | None
    runtimeParameters: di.objtypes.FunctionalGroupType | None
    scan: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=auto_id;i=7043"])


o6.reference(OpticalReaderDeviceType, "i=41", OpticalScanEventType)


ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6031",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7054",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Settings", dataType=o6.NodeId("ns=auto_id;i=3010"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6076",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7054",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Results", dataType=o6.NodeId("ns=auto_id;i=3027"), valueRank=1),
        ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("ns=auto_id;i=3013"), valueRank=-1),
    ],
)
o6.call(nodeId="ns=auto_id;i=7054", browseName="ns=auto_id;Scan", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6031"]), outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6076"]))


@o6.objecttype(nodeId="ns=auto_id;i=1011", browseName="ns=auto_id;OpticalVerifierDeviceType", displayName="OpticalVerifierDeviceType")
class OpticalVerifierDeviceType(OpticalReaderDeviceType):
    scan: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=auto_id;i=7054"])


o6.reference(OpticalVerifierDeviceType, "i=41", OpticalVerifierScanEventType)


ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6218",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7055",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Settings", dataType=o6.NodeId("ns=auto_id;i=3010"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6219",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7055",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Results", dataType=o6.NodeId("ns=auto_id;i=3028"), valueRank=1),
        ns0.datatypes.Argument(name="Status", dataType=o6.NodeId("ns=auto_id;i=3013"), valueRank=-1),
    ],
)
o6.call(nodeId="ns=auto_id;i=7055", browseName="ns=auto_id;Scan", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6218"]), outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6219"]))

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6224",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7056",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="Identifier", dataType=o6.NodeId("ns=auto_id;i=3020"), valueRank=-1),
        ns0.datatypes.Argument(name="LocationType", dataType=o6.NodeId("ns=auto_id;i=3009"), valueRank=-1),
        ns0.datatypes.Argument(name="CodeType", dataType=o6.NodeId("ns=auto_id;i=3031"), valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6225",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7056",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Result", dataType=o6.NodeId("ns=auto_id;i=3028"), valueRank=-1)],
)
o6.call(
    nodeId="ns=auto_id;i=7056", browseName="ns=auto_id;GetLocation", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6224"]), outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6225"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6226",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7058",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="SupportedLocationTypes", dataType=o6.NodeId("ns=auto_id;i=3009"), valueRank=1)],
)
o6.call(nodeId="ns=auto_id;i=7058", browseName="ns=auto_id;GetSupportedLocationTypes", outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6226"]))


@o6.objecttype(nodeId="ns=auto_id;i=1012", browseName="ns=auto_id;RtlsDeviceType", displayName="RtlsDeviceType")
class RtlsDeviceType(AutoIdDeviceType):
    geographicalUnit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6214", browseName="ns=auto_id;GeographicalUnit", dataType=ns0.datatypes.EUInformation, accessLevel=3)
    )
    getLocation: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=auto_id;i=7056"])
    getSupportedLocationTypes: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=auto_id;i=7058"])
    getUnits: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=auto_id;i=7057", browseName="ns=auto_id;GetUnits"))
    lengthUnit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6217", browseName="ns=auto_id;LengthUnit", dataType=ns0.datatypes.EUInformation, accessLevel=3)
    )
    rotationalUnit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6216", browseName="ns=auto_id;RotationalUnit", dataType=ns0.datatypes.EUInformation, accessLevel=3)
    )
    scan: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=auto_id;i=7055"])
    speedUnit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6215", browseName="ns=auto_id;SpeedUnit", dataType=ns0.datatypes.EUInformation, accessLevel=3)
    )


o6.reference(RtlsDeviceType, "i=41", RtlsLocationEventType)


del Any, TYPE_CHECKING, uuid, o6, di, ns0, auto_id_datypes, auto_id_vartypes
