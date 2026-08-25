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
from . import objtypes as auto_id_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5002", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5003", browseName="Default XML")
o6.hasEncoding(auto_id_datypes.ScanResult, o6.ns["ns=auto_id;i=5003"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5004", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5005", browseName="Default XML")
o6.hasEncoding(auto_id_datypes.OcrScanResult, o6.ns["ns=auto_id;i=5005"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5007", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5008", browseName="Default XML")
o6.hasEncoding(auto_id_datypes.Position, o6.ns["ns=auto_id;i=5008"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5009", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5010", browseName="Default XML")
o6.hasEncoding(auto_id_datypes.RfidSighting, o6.ns["ns=auto_id;i=5010"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5011", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5012", browseName="Default XML")
o6.hasEncoding(auto_id_datypes.RfidScanResult, o6.ns["ns=auto_id;i=5012"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5013", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5014", browseName="Default XML")
o6.hasEncoding(auto_id_datypes.Location, o6.ns["ns=auto_id;i=5014"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5015", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5016", browseName="Default XML")
o6.hasEncoding(auto_id_datypes.ScanSettings, o6.ns["ns=auto_id;i=5016"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5017", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5018", browseName="Default XML")
o6.hasEncoding(auto_id_datypes.AntennaNameIdPair, o6.ns["ns=auto_id;i=5018"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5022", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5023", browseName="Default XML")
o6.hasEncoding(auto_id_datypes.AccessResult, o6.ns["ns=auto_id;i=5023"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5024", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5025", browseName="Default XML")
o6.hasEncoding(auto_id_datypes.RfidAccessResult, o6.ns["ns=auto_id;i=5025"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5028", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5029", browseName="Default XML")
o6.hasEncoding(auto_id_datypes.LocalCoordinate, o6.ns["ns=auto_id;i=5029"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5030", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5031", browseName="Default XML")
o6.hasEncoding(auto_id_datypes.ScanData, o6.ns["ns=auto_id;i=5031"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5034", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5035", browseName="Default XML")
o6.hasEncoding(auto_id_datypes.DhcpGeoConfCoordinate, o6.ns["ns=auto_id;i=5035"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5036", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5037", browseName="Default XML")
o6.hasEncoding(auto_id_datypes.ScanDataEpc, o6.ns["ns=auto_id;i=5037"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5040", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5041", browseName="Default XML")
o6.hasEncoding(auto_id_datypes.OpticalScanResult, o6.ns["ns=auto_id;i=5041"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5046", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5047", browseName="Default XML")
o6.hasEncoding(auto_id_datypes.WGS84Coordinate, o6.ns["ns=auto_id;i=5047"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5048", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5049", browseName="Default XML")
o6.hasEncoding(auto_id_datypes.RtlsLocationResult, o6.ns["ns=auto_id;i=5049"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5050", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5051", browseName="Default XML")
o6.hasEncoding(auto_id_datypes.Rotation, o6.ns["ns=auto_id;i=5051"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5052", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=auto_id;i=5053", browseName="Default XML")
o6.hasEncoding(auto_id_datypes.OpticalVerifierScanResult, o6.ns["ns=auto_id;i=5053"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6020", browseName="ns=auto_id;ScanResult", dataType=o6.String, value="ScanResult")
o6.reference(o6.ns["ns=auto_id;i=5002"], "i=39", o6.ns["ns=auto_id;i=6020"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6021", browseName="ns=auto_id;ScanResult", dataType=o6.String, value="//xs:element[@name='ScanResult']")
o6.reference(o6.ns["ns=auto_id;i=5003"], "i=39", o6.ns["ns=auto_id;i=6021"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6022", browseName="ns=auto_id;OcrScanResult", dataType=o6.String, value="OcrScanResult")
o6.reference(o6.ns["ns=auto_id;i=5004"], "i=39", o6.ns["ns=auto_id;i=6022"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6023", browseName="ns=auto_id;OcrScanResult", dataType=o6.String, value="//xs:element[@name='OcrScanResult']")
o6.reference(o6.ns["ns=auto_id;i=5005"], "i=39", o6.ns["ns=auto_id;i=6023"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6025", browseName="ns=auto_id;RfidSighting", dataType=o6.String, value="RfidSighting")
o6.reference(o6.ns["ns=auto_id;i=5009"], "i=39", o6.ns["ns=auto_id;i=6025"])
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6029",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("Idle"), o6.LocalizedText("Error"), o6.LocalizedText("Scanning"), o6.LocalizedText("Busy")],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6032", browseName="ns=auto_id;Position", dataType=o6.String, value="Position")
o6.reference(o6.ns["ns=auto_id;i=5007"], "i=39", o6.ns["ns=auto_id;i=6032"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6033", browseName="ns=auto_id;Position", dataType=o6.String, value="//xs:element[@name='Position']")
o6.reference(o6.ns["ns=auto_id;i=5008"], "i=39", o6.ns["ns=auto_id;i=6033"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6034", browseName="ns=auto_id;Location", dataType=o6.String, value="Location")
o6.reference(o6.ns["ns=auto_id;i=5013"], "i=39", o6.ns["ns=auto_id;i=6034"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6035", browseName="ns=auto_id;RfidSighting", dataType=o6.String, value="//xs:element[@name='RfidSighting']")
o6.reference(o6.ns["ns=auto_id;i=5010"], "i=39", o6.ns["ns=auto_id;i=6035"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6036", browseName="ns=auto_id;Location", dataType=o6.String, value="//xs:element[@name='Location']")
o6.reference(o6.ns["ns=auto_id;i=5014"], "i=39", o6.ns["ns=auto_id;i=6036"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6037", browseName="ns=auto_id;RfidScanResult", dataType=o6.String, value="RfidScanResult")
o6.reference(o6.ns["ns=auto_id;i=5011"], "i=39", o6.ns["ns=auto_id;i=6037"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6038", browseName="ns=auto_id;RfidScanResult", dataType=o6.String, value="//xs:element[@name='RfidScanResult']")
o6.reference(o6.ns["ns=auto_id;i=5012"], "i=39", o6.ns["ns=auto_id;i=6038"])
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6040",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=3009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("NMEA"), o6.LocalizedText("LOCAL"), o6.LocalizedText("WGS84"), o6.LocalizedText("NAME")],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6044", browseName="ns=auto_id;ScanSettings", dataType=o6.String, value="ScanSettings")
o6.reference(o6.ns["ns=auto_id;i=5015"], "i=39", o6.ns["ns=auto_id;i=6044"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6045", browseName="ns=auto_id;ScanSettings", dataType=o6.String, value="//xs:element[@name='ScanSettings']")
o6.reference(o6.ns["ns=auto_id;i=5016"], "i=39", o6.ns["ns=auto_id;i=6045"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6046", browseName="ns=auto_id;AntennaNameIdPair", dataType=o6.String, value="AntennaNameIdPair")
o6.reference(o6.ns["ns=auto_id;i=5017"], "i=39", o6.ns["ns=auto_id;i=6046"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6047", browseName="ns=auto_id;AntennaNameIdPair", dataType=o6.String, value="//xs:element[@name='AntennaNameIdPair']")
o6.reference(o6.ns["ns=auto_id;i=5018"], "i=39", o6.ns["ns=auto_id;i=6047"])
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6061",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=3014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("Access"), o6.LocalizedText("Kill"), o6.LocalizedText("Read"), o6.LocalizedText("Write")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6066",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=3015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[5],
    value=[o6.LocalizedText("Kill"), o6.LocalizedText("Access"), o6.LocalizedText("EPC"), o6.LocalizedText("TID"), o6.LocalizedText("User")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6067",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=3016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("Lock"), o6.LocalizedText("Unlock"), o6.LocalizedText("PermanentLock"), o6.LocalizedText("PermanentUnlock")],
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashAutoIDSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=auto_id;i=5019",
    browseName="ns=auto_id;http://opcfoundation.org/UA/AutoID/",
    description="Provides the metadata for a namespace used by the server.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=auto_id;i=6028",
                browseName="IsNamespaceSubset",
                description="If TRUE then the server only supports a subset of the namespace.",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=auto_id;i=6039",
                browseName="NamespacePublicationDate",
                description="The publication date for the namespace.",
                dataType=o6.DateTime,
                value=o6.DateTime("2020-06-18T13:52:03Z"),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=auto_id;i=6053", browseName="NamespaceUri", description="The URI of the namespace.", dataType=o6.String, value="http://opcfoundation.org/UA/AutoID/"
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=auto_id;i=6068",
                browseName="NamespaceVersion",
                description="The human readable string representing version of the namespace.",
                dataType=o6.String,
                value="1.01",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=auto_id;i=6069",
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
                nodeId="ns=auto_id;i=6070",
                browseName="StaticNumericNodeIdRange",
                description="A list of ranges for numeric node ids which are the same in every server that exposes them.",
                dataType=ns0.datatypes.NumericRange,
                valueRank=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=auto_id;i=6071",
                browseName="StaticStringNodeIdPattern",
                description="A regular expression which matches string node ids are the same in every server that exposes them.",
                dataType=o6.String,
            )
        ),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6086", browseName="ns=auto_id;AccessResult", dataType=o6.String, value="AccessResult")
o6.reference(o6.ns["ns=auto_id;i=5022"], "i=39", o6.ns["ns=auto_id;i=6086"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6087", browseName="ns=auto_id;AccessResult", dataType=o6.String, value="//xs:element[@name='AccessResult']")
o6.reference(o6.ns["ns=auto_id;i=5023"], "i=39", o6.ns["ns=auto_id;i=6087"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6088", browseName="ns=auto_id;RfidAccessResult", dataType=o6.String, value="RfidAccessResult")
o6.reference(o6.ns["ns=auto_id;i=5024"], "i=39", o6.ns["ns=auto_id;i=6088"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6089", browseName="ns=auto_id;RfidAccessResult", dataType=o6.String, value="//xs:element[@name='RfidAccessResult']")
o6.reference(o6.ns["ns=auto_id;i=5025"], "i=39", o6.ns["ns=auto_id;i=6089"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=auto_id;i=5032",
    browseName="ns=auto_id;Logbook",
    description="Values of the logbook.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6101", browseName="ns=auto_id;LogColumns", description="Last Entry of the Loogbook.", dataType=o6.String, accessLevel=3
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6102", browseName="ns=auto_id;LastLogEntry", description="Column headings of the Loogbook.", dataType=o6.String, accessLevel=3
            )
        ),
    ],
)
di.objtypes.FunctionalGroupType(
    nodeId="ns=auto_id;i=5027",
    browseName="ns=auto_id;LastAccess",
    description="Values of the last AutoID Identifier access.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6103", browseName="ns=auto_id;Client", description="Client which was the originator of the command.", dataType=o6.String, accessLevel=3
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=auto_id;i=6104", browseName="ns=auto_id;Command", description="Access command", dataType=o6.String, accessLevel=3)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6105",
                browseName="ns=auto_id;Identifier",
                description="The AutoID Identifier (e.g. a code or a transponder) which was accessed by a command.",
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6106",
                browseName="ns=auto_id;Timestamp",
                description="The point of time the AutoID Identifier was accessed by the command.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
            )
        ),
    ],
)
di.objtypes.FunctionalGroupType(
    nodeId="ns=auto_id;i=5026",
    browseName="ns=auto_id;Diagnostics",
    description="Diagnostic data from AutoID Devices.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=auto_id;i=5027"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=5032"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6100",
                browseName="ns=auto_id;Presence",
                description="Current presence of AutoID Identifier (e.g. a code or a transponder).",
                dataType=o6.UInt16,
                accessLevel=3,
            )
        ),
    ],
)
o6.reference(auto_id_objtypes.AutoIdDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=auto_id;i=5026"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=auto_id;i=6107",
    browseName="ns=auto_id;CodeTypes",
    description="Supported CodeTypes and selected CodeType for the ScanData.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6108", browseName="EnumStrings", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0]))],
    dataType=o6.UInt32,
    valueRank=1,
    arrayDimensions=[0],
    accessLevel=3,
)
di.objtypes.FunctionalGroupType(
    nodeId="ns=auto_id;i=5033",
    browseName="ns=auto_id;ScanSettings",
    description="Scan settings used together with ScanActive Variable.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6109",
                browseName="ns=auto_id;CodeType",
                description="The format of LastScanData Variable as string.",
                dataType=auto_id_datypes.CodeTypeDataType,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6110",
                browseName="ns=auto_id;DataAvailable",
                description="Finish scan operation as soon as scan data is available.",
                dataType=o6.Boolean,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6111", browseName="ns=auto_id;Cycles", description="Duration of the scan operation in number of scan cycles.", dataType=o6.Int32, accessLevel=3
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6112",
                browseName="ns=auto_id;Duration",
                description="Duration of the scan operation in milliseconds.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
            )
        ),
    ],
)
di.objtypes.FunctionalGroupType(
    nodeId="ns=auto_id;i=5044",
    browseName="ns=auto_id;RuntimeParameters",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=auto_id;i=5033"]), o6.hasComponent(o6.ns["ns=auto_id;i=6107"])],
)
o6.reference(auto_id_objtypes.AutoIdDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=auto_id;i=5044"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=auto_id;i=5039",
    browseName="ns=auto_id;LastAccess",
    description="Values of the last AutoID Identifier access.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6113",
                browseName="ns=auto_id;RWData",
                description="The user data which was written to / was read from the Rfid Transponder by the command.",
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6114",
                browseName="ns=auto_id;Antenna",
                description="The antenna by which the transponder was accessed by the command.",
                dataType=o6.Int32,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6115",
                browseName="ns=auto_id;CurrentPowerLevel",
                description="The power level with which the transponder was accessed by the command.",
                dataType=o6.Int32,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6116",
                browseName="ns=auto_id;PC",
                description="The Protocol Control Word of the transponder accessed by the command.",
                dataType=o6.UInt16,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6117",
                browseName="ns=auto_id;Polarization",
                description="The polarization with which the last transponder was accessed by the command.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6118",
                browseName="ns=auto_id;Strength",
                description="The Rssi value with which the transponder was accessed by the command.",
                dataType=o6.Int32,
                accessLevel=3,
            )
        ),
    ],
)
di.objtypes.FunctionalGroupType(
    nodeId="ns=auto_id;i=5038",
    browseName="ns=auto_id;Diagnostics",
    description="Diagnostic data from AutoID Devices.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=auto_id;i=5039"])],
)
o6.reference(auto_id_objtypes.RfidReaderDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=auto_id;i=5038"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=auto_id;i=6119",
    browseName="ns=auto_id;CodeTypesRWData",
    description="Supported CodeTypes and selected CodeType for the diagnostics value RWData.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6120", browseName="EnumStrings", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0]))],
    dataType=o6.UInt32,
    valueRank=1,
    arrayDimensions=[0],
    accessLevel=3,
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6122", browseName="ns=auto_id;LocalCoordinate", dataType=o6.String, value="LocalCoordinate", historizing=True)
o6.reference(o6.ns["ns=auto_id;i=5028"], "i=39", o6.ns["ns=auto_id;i=6122"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=auto_id;i=6123", browseName="ns=auto_id;LocalCoordinate", dataType=o6.String, value="//xs:element[@name='LocalCoordinate']", historizing=True
)
o6.reference(o6.ns["ns=auto_id;i=5029"], "i=39", o6.ns["ns=auto_id;i=6123"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=auto_id;i=6121",
    browseName="ns=auto_id;TagTypes",
    description="Expected tags in a multi-type environment.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6125", browseName="EnumStrings", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0]))],
    dataType=o6.UInt32,
    valueRank=1,
    arrayDimensions=[0],
    accessLevel=3,
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6131", browseName="ns=auto_id;ScanData", dataType=o6.String, value="ScanData")
o6.reference(o6.ns["ns=auto_id;i=5030"], "i=39", o6.ns["ns=auto_id;i=6131"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6132", browseName="ns=auto_id;ScanData", dataType=o6.String, value="//xs:element[@name='ScanData']")
o6.reference(o6.ns["ns=auto_id;i=5031"], "i=39", o6.ns["ns=auto_id;i=6132"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=auto_id;i=5043",
    browseName="ns=auto_id;RuntimeParameters",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6133",
                browseName="ns=auto_id;TemplateName",
                description="Activate template which defines a specific identification task.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6134", browseName="ns=auto_id;MatchCode", description="Target value for 2D or OCR decoding.", dataType=o6.String, accessLevel=3
            )
        ),
    ],
)
o6.reference(auto_id_objtypes.OcrReaderDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=auto_id;i=5043"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=auto_id;i=5045",
    browseName="ns=auto_id;RuntimeParameters",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6135",
                browseName="ns=auto_id;TemplateName",
                description="Activate template which defines a specific identification task.",
                dataType=o6.String,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6136", browseName="ns=auto_id;MatchCode", description="Target value for 2D or OCR decoding.", dataType=o6.String, accessLevel=3
            )
        ),
    ],
)
o6.reference(auto_id_objtypes.OpticalReaderDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=auto_id;i=5045"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6138", browseName="ns=auto_id;ScanDataEpc", dataType=o6.String, value="ScanDataEpc")
o6.reference(o6.ns["ns=auto_id;i=5036"], "i=39", o6.ns["ns=auto_id;i=6138"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6139", browseName="ns=auto_id;ScanDataEpc", dataType=o6.String, value="//xs:element[@name='ScanDataEpc']")
o6.reference(o6.ns["ns=auto_id;i=5037"], "i=39", o6.ns["ns=auto_id;i=6139"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6142", browseName="ns=auto_id;OpticalScanResult", dataType=o6.String, value="OpticalScanResult")
o6.reference(o6.ns["ns=auto_id;i=5040"], "i=39", o6.ns["ns=auto_id;i=6142"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6143", browseName="ns=auto_id;OpticalScanResult", dataType=o6.String, value="//xs:element[@name='OpticalScanResult']")
o6.reference(o6.ns["ns=auto_id;i=5041"], "i=39", o6.ns["ns=auto_id;i=6143"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=auto_id;i=5042",
    browseName="ns=auto_id;RuntimeParameters",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=auto_id;i=6119"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6121"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6126",
                browseName="ns=auto_id;EnableAntennas",
                description="Antennas that shall be used by the device for its operation.",
                dataType=o6.UInt32,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6141", browseName="ns=auto_id;RfPower", description="Radio transmission power of the antenna.", dataType=o6.SByte, accessLevel=3
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=auto_id;i=6146", browseName="ns=auto_id;MinRssi", description="Lowest acceptable RSSI value.", dataType=o6.Int32, accessLevel=3
            )
        ),
    ],
)
o6.reference(auto_id_objtypes.RfidReaderDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=auto_id;i=5042"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6189", browseName="ns=auto_id;DhcpGeoConfCoordinate", dataType=o6.String, value="DhcpGeoConfCoordinate")
o6.reference(o6.ns["ns=auto_id;i=5034"], "i=39", o6.ns["ns=auto_id;i=6189"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=auto_id;i=6190", browseName="ns=auto_id;DhcpGeoConfCoordinate", dataType=o6.String, value="//xs:element[@name='DhcpGeoConfCoordinate']"
)
o6.reference(o6.ns["ns=auto_id;i=5035"], "i=39", o6.ns["ns=auto_id;i=6190"])
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6201",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=3013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[22],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("SUCCESS"), description=o6.LocalizedText("Successful operation")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("MISC_ERROR_TOTAL"), description=o6.LocalizedText("The operation has not be executed in total")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("MISC_ERROR_PARTIAL"), description=o6.LocalizedText("The operation has been executed only partial")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("PERMISSON_ERROR"), description=o6.LocalizedText("Password required")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("PASSWORD_ERROR"), description=o6.LocalizedText("Password is wrong")),
        ns0.datatypes.EnumValueType(
            value=5, displayName=o6.LocalizedText("REGION_NOT_FOUND_ERROR"), description=o6.LocalizedText("Memory region not available for the actual tag")
        ),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("OP_NOT_POSSIBLE_ERROR"), description=o6.LocalizedText("Operation not supported by the actual tag")),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("OUT_OF_RANGE_ERROR"), description=o6.LocalizedText("Addressed memory not available for the actual tag")),
        ns0.datatypes.EnumValueType(
            value=8,
            displayName=o6.LocalizedText("NO_IDENTIFIER"),
            description=o6.LocalizedText(
                "The operation cannot be executed because no tag or code was inside the range of the AutoID Device or the tag or code has been moved out of the range during execution"
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=9,
            displayName=o6.LocalizedText("MULTIPLE_IDENTIFIERS"),
            description=o6.LocalizedText("Multiple tags or codes have been selected, but the command can only be used with a single tag or code"),
        ),
        ns0.datatypes.EnumValueType(
            value=10,
            displayName=o6.LocalizedText("READ_ERROR"),
            description=o6.LocalizedText(
                "The tag or code exists and has a valid format, but there was a problem reading the data (e.g. still CRC error after maximum number of retries)"
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=11, displayName=o6.LocalizedText("DECODING_ERROR"), description=o6.LocalizedText("The (optical) code or plain text has too many failures and cannot be detected")
        ),
        ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("MATCH_ERROR"), description=o6.LocalizedText("The code doesn&#8217;t match the given target value")),
        ns0.datatypes.EnumValueType(
            value=13, displayName=o6.LocalizedText("CODE_NOT_SUPPORTED"), description=o6.LocalizedText("The code format is not supported by the AutoID Device")
        ),
        ns0.datatypes.EnumValueType(
            value=14, displayName=o6.LocalizedText("WRITE_ERROR"), description=o6.LocalizedText("The tag exists, but there was a problem writing the data")
        ),
        ns0.datatypes.EnumValueType(
            value=15,
            displayName=o6.LocalizedText("NOT_SUPPORTED_BY_DEVICE"),
            description=o6.LocalizedText("The command or a parameter combination is not supported by the AutoID Device"),
        ),
        ns0.datatypes.EnumValueType(
            value=16, displayName=o6.LocalizedText("NOT_SUPPORTED_BY_TAG"), description=o6.LocalizedText("The command or a parameter combination is not supported by the tag")
        ),
        ns0.datatypes.EnumValueType(
            value=17, displayName=o6.LocalizedText("DEVICE_NOT_READY"), description=o6.LocalizedText("The AutoID Device is in a state not ready to execute the command")
        ),
        ns0.datatypes.EnumValueType(value=18, displayName=o6.LocalizedText("INVALID_CONFIGURATION"), description=o6.LocalizedText("The AutoID Device configuration is not valid")),
        ns0.datatypes.EnumValueType(
            value=19,
            displayName=o6.LocalizedText("RF_COMMUNICATION_ERROR"),
            description=o6.LocalizedText("This error indicates that there is a general error in the communication between the transponder and the reader"),
        ),
        ns0.datatypes.EnumValueType(value=20, displayName=o6.LocalizedText("DEVICE_FAULT"), description=o6.LocalizedText("The AutoID Device has a hardware fault")),
        ns0.datatypes.EnumValueType(value=21, displayName=o6.LocalizedText("TAG_HAS_LOW_BATTERY"), description=o6.LocalizedText("The battery of the (active) tag is low")),
    ],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6212", browseName="ns=auto_id;WGS84Coordinate", dataType=o6.String, value="WGS84Coordinate")
o6.reference(o6.ns["ns=auto_id;i=5046"], "i=39", o6.ns["ns=auto_id;i=6212"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6213", browseName="ns=auto_id;WGS84Coordinate", dataType=o6.String, value="//xs:element[@name='WGS84Coordinate']")
o6.reference(o6.ns["ns=auto_id;i=5047"], "i=39", o6.ns["ns=auto_id;i=6213"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6220", browseName="ns=auto_id;RtlsLocationResult", dataType=o6.String, value="RtlsLocationResult")
o6.reference(o6.ns["ns=auto_id;i=5048"], "i=39", o6.ns["ns=auto_id;i=6220"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6221", browseName="ns=auto_id;RtlsLocationResult", dataType=o6.String, value="//xs:element[@name='RtlsLocationResult']")
o6.reference(o6.ns["ns=auto_id;i=5049"], "i=39", o6.ns["ns=auto_id;i=6221"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6222", browseName="ns=auto_id;Rotation", dataType=o6.String, value="Rotation")
o6.reference(o6.ns["ns=auto_id;i=5050"], "i=39", o6.ns["ns=auto_id;i=6222"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6223", browseName="ns=auto_id;Rotation", dataType=o6.String, value="//xs:element[@name='Rotation']")
o6.reference(o6.ns["ns=auto_id;i=5051"], "i=39", o6.ns["ns=auto_id;i=6223"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=auto_id;i=6229", browseName="ns=auto_id;OpticalVerifierScanResult", dataType=o6.String, value="OpticalVerifierScanResult")
o6.reference(o6.ns["ns=auto_id;i=5052"], "i=39", o6.ns["ns=auto_id;i=6229"])
autoID = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=auto_id;i=6016",
    browseName="ns=auto_id;AutoID",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/AutoID/.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6017", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/AutoID/")),
        o6.hasComponent(o6.ns["ns=auto_id;i=6020"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6022"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6025"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6032"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6034"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6037"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6044"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6046"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6086"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6088"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6122"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6131"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6138"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6142"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6189"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6212"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6220"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6222"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6229"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/AutoID/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/AutoID/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="AccessResult">\n  <opc:Documentation>Result values of an AutoID Identifier access.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="CodeTypeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="IdentifierSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="TimestampSpecified"/>\n  <opc:Field Length="29" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field SwitchField="CodeTypeSpecified" TypeName="opc:CharArray" Name="CodeType"/>\n  <opc:Field SwitchField="IdentifierSpecified" TypeName="tns:ScanData" Name="Identifier"/>\n  <opc:Field SwitchField="TimestampSpecified" TypeName="opc:DateTime" Name="Timestamp"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:AccessResult" Name="RfidAccessResult">\n  <opc:Documentation>Additional result values of an Rfid Transponder access.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="CodeTypeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="IdentifierSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="TimestampSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="CodeTypeRWDataSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="RWDataSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="AntennaSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="CurrentPowerLevelSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PCSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PolarizationSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="StrengthSpecified"/>\n  <opc:Field Length="22" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field SwitchField="CodeTypeSpecified" SourceType="tns:AccessResult" TypeName="opc:CharArray" Name="CodeType"/>\n  <opc:Field SwitchField="IdentifierSpecified" SourceType="tns:AccessResult" TypeName="tns:ScanData" Name="Identifier"/>\n  <opc:Field SwitchField="TimestampSpecified" SourceType="tns:AccessResult" TypeName="opc:DateTime" Name="Timestamp"/>\n  <opc:Field SwitchField="CodeTypeRWDataSpecified" TypeName="opc:CharArray" Name="CodeTypeRWData"/>\n  <opc:Field SwitchField="RWDataSpecified" TypeName="tns:ScanData" Name="RWData"/>\n  <opc:Field SwitchField="AntennaSpecified" TypeName="opc:Int32" Name="Antenna"/>\n  <opc:Field SwitchField="CurrentPowerLevelSpecified" TypeName="opc:Int32" Name="CurrentPowerLevel"/>\n  <opc:Field SwitchField="PCSpecified" TypeName="opc:UInt16" Name="PC"/>\n  <opc:Field SwitchField="PolarizationSpecified" TypeName="opc:CharArray" Name="Polarization"/>\n  <opc:Field SwitchField="StrengthSpecified" TypeName="opc:Int32" Name="Strength"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="AntennaNameIdPair">\n  <opc:Field TypeName="opc:Int32" Name="AntennaId"/>\n  <opc:Field TypeName="opc:CharArray" Name="AntennaName"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="DhcpGeoConfCoordinate">\n  <opc:Field TypeName="opc:Byte" Name="LaRes"/>\n  <opc:Field TypeName="opc:Int16" Name="LatitudeInteger"/>\n  <opc:Field TypeName="opc:Int32" Name="LatitudeFraction"/>\n  <opc:Field TypeName="opc:Byte" Name="LoRes"/>\n  <opc:Field TypeName="opc:Int16" Name="LongitudeInteger"/>\n  <opc:Field TypeName="opc:Int32" Name="LongitudeFraction"/>\n  <opc:Field TypeName="opc:Byte" Name="AT"/>\n  <opc:Field TypeName="opc:Byte" Name="AltRes"/>\n  <opc:Field TypeName="opc:Int32" Name="AltitudeInteger"/>\n  <opc:Field TypeName="opc:Int16" Name="AltitudeFraction"/>\n  <opc:Field TypeName="opc:Byte" Name="Datum"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="LocalCoordinate">\n  <opc:Field TypeName="opc:Double" Name="X"/>\n  <opc:Field TypeName="opc:Double" Name="Y"/>\n  <opc:Field TypeName="opc:Double" Name="Z"/>\n  <opc:Field TypeName="opc:DateTime" Name="Timestamp"/>\n  <opc:Field TypeName="opc:Double" Name="DilutionOfPrecision"/>\n  <opc:Field TypeName="opc:Int32" Name="UsefulPrecision"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="Position">\n  <opc:Field TypeName="opc:Int32" Name="PositionX"/>\n  <opc:Field TypeName="opc:Int32" Name="PositionY"/>\n  <opc:Field TypeName="opc:Int32" Name="SizeX"/>\n  <opc:Field TypeName="opc:Int32" Name="SizeY"/>\n  <opc:Field TypeName="opc:Int32" Name="Rotation"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RfidSighting">\n  <opc:Field TypeName="opc:Int32" Name="Antenna"/>\n  <opc:Field TypeName="opc:Int32" Name="Strength"/>\n  <opc:Field TypeName="opc:DateTime" Name="Timestamp"/>\n  <opc:Field TypeName="opc:Int32" Name="CurrentPowerLevel"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="Rotation">\n  <opc:Field TypeName="opc:Double" Name="Yaw"/>\n  <opc:Field TypeName="opc:Double" Name="Pitch"/>\n  <opc:Field TypeName="opc:Double" Name="Roll"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ScanDataEpc">\n  <opc:Field TypeName="opc:UInt16" Name="PC"/>\n  <opc:Field TypeName="opc:ByteString" Name="UId"/>\n  <opc:Field TypeName="opc:UInt16" Name="XPC_W1"/>\n  <opc:Field TypeName="opc:UInt16" Name="XPC_W2"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ScanResult">\n  <opc:Field TypeName="opc:Bit" Name="LocationSpecified"/>\n  <opc:Field Length="31" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="CodeType"/>\n  <opc:Field TypeName="tns:ScanData" Name="ScanData"/>\n  <opc:Field TypeName="opc:DateTime" Name="Timestamp"/>\n  <opc:Field SwitchField="LocationSpecified" TypeName="tns:Location" Name="Location"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ScanResult" Name="OcrScanResult">\n  <opc:Field TypeName="opc:Bit" Name="LocationSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="FontSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="DecodingTimeSpecified"/>\n  <opc:Field Length="29" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field SourceType="tns:ScanResult" TypeName="opc:CharArray" Name="CodeType"/>\n  <opc:Field SourceType="tns:ScanResult" TypeName="tns:ScanData" Name="ScanData"/>\n  <opc:Field SourceType="tns:ScanResult" TypeName="opc:DateTime" Name="Timestamp"/>\n  <opc:Field SwitchField="LocationSpecified" SourceType="tns:ScanResult" TypeName="tns:Location" Name="Location"/>\n  <opc:Field TypeName="ua:NodeId" Name="ImageId"/>\n  <opc:Field TypeName="opc:Byte" Name="Quality"/>\n  <opc:Field TypeName="tns:Position" Name="Position"/>\n  <opc:Field SwitchField="FontSpecified" TypeName="opc:CharArray" Name="Font"/>\n  <opc:Field SwitchField="DecodingTimeSpecified" TypeName="opc:DateTime" Name="DecodingTime"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ScanResult" Name="OpticalScanResult">\n  <opc:Field TypeName="opc:Bit" Name="LocationSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="GradeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PositionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SymbologySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ImageIdSpecified"/>\n  <opc:Field Length="27" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field SourceType="tns:ScanResult" TypeName="opc:CharArray" Name="CodeType"/>\n  <opc:Field SourceType="tns:ScanResult" TypeName="tns:ScanData" Name="ScanData"/>\n  <opc:Field SourceType="tns:ScanResult" TypeName="opc:DateTime" Name="Timestamp"/>\n  <opc:Field SwitchField="LocationSpecified" SourceType="tns:ScanResult" TypeName="tns:Location" Name="Location"/>\n  <opc:Field SwitchField="GradeSpecified" TypeName="opc:Float" Name="Grade"/>\n  <opc:Field SwitchField="PositionSpecified" TypeName="tns:Position" Name="Position"/>\n  <opc:Field SwitchField="SymbologySpecified" TypeName="opc:CharArray" Name="Symbology"/>\n  <opc:Field SwitchField="ImageIdSpecified" TypeName="ua:NodeId" Name="ImageId"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:OpticalScanResult" Name="OpticalVerifierScanResult">\n  <opc:Field TypeName="opc:Bit" Name="LocationSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="GradeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PositionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SymbologySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ImageIdSpecified"/>\n  <opc:Field Length="27" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field SourceType="tns:ScanResult" TypeName="opc:CharArray" Name="CodeType"/>\n  <opc:Field SourceType="tns:ScanResult" TypeName="tns:ScanData" Name="ScanData"/>\n  <opc:Field SourceType="tns:ScanResult" TypeName="opc:DateTime" Name="Timestamp"/>\n  <opc:Field SwitchField="LocationSpecified" SourceType="tns:ScanResult" TypeName="tns:Location" Name="Location"/>\n  <opc:Field SwitchField="GradeSpecified" SourceType="tns:OpticalScanResult" TypeName="opc:Float" Name="Grade"/>\n  <opc:Field SwitchField="PositionSpecified" SourceType="tns:OpticalScanResult" TypeName="tns:Position" Name="Position"/>\n  <opc:Field SwitchField="SymbologySpecified" SourceType="tns:OpticalScanResult" TypeName="opc:CharArray" Name="Symbology"/>\n  <opc:Field SwitchField="ImageIdSpecified" SourceType="tns:OpticalScanResult" TypeName="ua:NodeId" Name="ImageId"/>\n  <opc:Field TypeName="opc:CharArray" Name="IsoGrade"/>\n  <opc:Field TypeName="opc:Int16" Name="RMin"/>\n  <opc:Field TypeName="opc:Int16" Name="SymbolContrast"/>\n  <opc:Field TypeName="opc:Int16" Name="ECMin"/>\n  <opc:Field TypeName="opc:Int16" Name="Modulation"/>\n  <opc:Field TypeName="opc:Int16" Name="Defects"/>\n  <opc:Field TypeName="opc:Int16" Name="Decodability"/>\n  <opc:Field TypeName="opc:Int16" Name="Decode"/>\n  <opc:Field TypeName="opc:Int16" Name="PrintGain"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ScanResult" Name="RfidScanResult">\n  <opc:Field TypeName="opc:Bit" Name="LocationSpecified"/>\n  <opc:Field Length="31" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field SourceType="tns:ScanResult" TypeName="opc:CharArray" Name="CodeType"/>\n  <opc:Field SourceType="tns:ScanResult" TypeName="tns:ScanData" Name="ScanData"/>\n  <opc:Field SourceType="tns:ScanResult" TypeName="opc:DateTime" Name="Timestamp"/>\n  <opc:Field SwitchField="LocationSpecified" SourceType="tns:ScanResult" TypeName="tns:Location" Name="Location"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfSighting"/>\n  <opc:Field LengthField="NoOfSighting" TypeName="tns:RfidSighting" Name="Sighting"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ScanResult" Name="RtlsLocationResult">\n  <opc:Field TypeName="opc:Bit" Name="LocationSpecified"/>\n  <opc:Field Length="31" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field SourceType="tns:ScanResult" TypeName="opc:CharArray" Name="CodeType"/>\n  <opc:Field SourceType="tns:ScanResult" TypeName="tns:ScanData" Name="ScanData"/>\n  <opc:Field SourceType="tns:ScanResult" TypeName="opc:DateTime" Name="Timestamp"/>\n  <opc:Field SwitchField="LocationSpecified" SourceType="tns:ScanResult" TypeName="tns:Location" Name="Location"/>\n  <opc:Field TypeName="opc:Double" Name="Speed"/>\n  <opc:Field TypeName="opc:Double" Name="Heading"/>\n  <opc:Field TypeName="tns:Rotation" Name="Rotation"/>\n  <opc:Field TypeName="opc:DateTime" Name="ReceiveTime"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ScanSettings">\n  <opc:Field TypeName="opc:Bit" Name="LocationTypeSpecified"/>\n  <opc:Field Length="31" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:Double" Name="Duration"/>\n  <opc:Field TypeName="opc:Int32" Name="Cycles"/>\n  <opc:Field TypeName="opc:Boolean" Name="DataAvailable"/>\n  <opc:Field SwitchField="LocationTypeSpecified" TypeName="tns:LocationTypeEnumeration" Name="LocationType"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:Union" Name="Location">\n  <opc:Field TypeName="opc:UInt32" Name="SwitchField"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:CharArray" SwitchValue="1" Name="NMEA"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:LocalCoordinate" SwitchValue="2" Name="Local"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:WGS84Coordinate" SwitchValue="3" Name="WGS84"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:CharArray" SwitchValue="4" Name="Name"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:Union" Name="ScanData">\n  <opc:Field TypeName="opc:UInt32" Name="SwitchField"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:ByteString" SwitchValue="1" Name="ByteString"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:CharArray" SwitchValue="2" Name="String"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:ScanDataEpc" SwitchValue="3" Name="Epc"/>\n  <opc:Field SwitchField="SwitchField" TypeName="ua:Variant" SwitchValue="4" Name="Custom"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="WGS84Coordinate">\n  <opc:Field TypeName="opc:CharArray" Name="N/S Hemisphere"/>\n  <opc:Field TypeName="opc:Double" Name="Latitude"/>\n  <opc:Field TypeName="opc:CharArray" Name="E/W Hemisphere"/>\n  <opc:Field TypeName="opc:Double" Name="Longitude"/>\n  <opc:Field TypeName="opc:Double" Name="Altitude"/>\n  <opc:Field TypeName="opc:DateTime" Name="Timestamp"/>\n  <opc:Field TypeName="opc:Double" Name="DilutionOfPrecision"/>\n  <opc:Field TypeName="opc:Int32" Name="UsefulPrecisionLatLon"/>\n  <opc:Field TypeName="opc:Int32" Name="UsefulPrecisionAlt"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="AutoIdOperationStatusEnumeration">\n  <opc:EnumeratedValue Name="SUCCESS" Value="0"/>\n  <opc:EnumeratedValue Name="MISC_ERROR_TOTAL" Value="1"/>\n  <opc:EnumeratedValue Name="MISC_ERROR_PARTIAL" Value="2"/>\n  <opc:EnumeratedValue Name="PERMISSON_ERROR" Value="3"/>\n  <opc:EnumeratedValue Name="PASSWORD_ERROR" Value="4"/>\n  <opc:EnumeratedValue Name="REGION_NOT_FOUND_ERROR" Value="5"/>\n  <opc:EnumeratedValue Name="OP_NOT_POSSIBLE_ERROR" Value="6"/>\n  <opc:EnumeratedValue Name="OUT_OF_RANGE_ERROR" Value="7"/>\n  <opc:EnumeratedValue Name="NO_IDENTIFIER" Value="8"/>\n  <opc:EnumeratedValue Name="MULTIPLE_IDENTIFIERS" Value="9"/>\n  <opc:EnumeratedValue Name="READ_ERROR" Value="10"/>\n  <opc:EnumeratedValue Name="DECODING_ERROR" Value="11"/>\n  <opc:EnumeratedValue Name="MATCH_ERROR" Value="12"/>\n  <opc:EnumeratedValue Name="CODE_NOT_SUPPORTED" Value="13"/>\n  <opc:EnumeratedValue Name="WRITE_ERROR" Value="14"/>\n  <opc:EnumeratedValue Name="NOT_SUPPORTED_BY_DEVICE" Value="15"/>\n  <opc:EnumeratedValue Name="NOT_SUPPORTED_BY_TAG" Value="16"/>\n  <opc:EnumeratedValue Name="DEVICE_NOT_READY" Value="17"/>\n  <opc:EnumeratedValue Name="INVALID_CONFIGURATION" Value="18"/>\n  <opc:EnumeratedValue Name="RF_COMMUNICATION_ERROR" Value="19"/>\n  <opc:EnumeratedValue Name="DEVICE_FAULT" Value="20"/>\n  <opc:EnumeratedValue Name="TAG_HAS_LOW_BATTERY" Value="21"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="DeviceStatusEnumeration">\n  <opc:EnumeratedValue Name="Idle" Value="0"/>\n  <opc:EnumeratedValue Name="Error" Value="1"/>\n  <opc:EnumeratedValue Name="Scanning" Value="2"/>\n  <opc:EnumeratedValue Name="Busy" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="LocationTypeEnumeration">\n  <opc:EnumeratedValue Name="NMEA" Value="0"/>\n  <opc:EnumeratedValue Name="LOCAL" Value="1"/>\n  <opc:EnumeratedValue Name="WGS84" Value="2"/>\n  <opc:EnumeratedValue Name="NAME" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="RfidLockOperationEnumeration">\n  <opc:EnumeratedValue Name="Lock" Value="0"/>\n  <opc:EnumeratedValue Name="Unlock" Value="1"/>\n  <opc:EnumeratedValue Name="PermanentLock" Value="2"/>\n  <opc:EnumeratedValue Name="PermanentUnlock" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="RfidLockRegionEnumeration">\n  <opc:EnumeratedValue Name="Kill" Value="0"/>\n  <opc:EnumeratedValue Name="Access" Value="1"/>\n  <opc:EnumeratedValue Name="EPC" Value="2"/>\n  <opc:EnumeratedValue Name="TID" Value="3"/>\n  <opc:EnumeratedValue Name="User" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="RfidPasswordTypeEnumeration">\n  <opc:EnumeratedValue Name="Access" Value="0"/>\n  <opc:EnumeratedValue Name="Kill" Value="1"/>\n  <opc:EnumeratedValue Name="Read" Value="2"/>\n  <opc:EnumeratedValue Name="Write" Value="3"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=auto_id;i=6230", browseName="ns=auto_id;OpticalVerifierScanResult", dataType=o6.String, value="//xs:element[@name='OpticalVerifierScanResult']"
)
o6.reference(o6.ns["ns=auto_id;i=5053"], "i=39", o6.ns["ns=auto_id;i=6230"])
autoID_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=auto_id;i=6018",
    browseName="ns=auto_id;AutoID",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/AutoID/.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6019", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/AutoID/Types.xsd")),
        o6.hasComponent(o6.ns["ns=auto_id;i=6021"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6023"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6033"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6035"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6036"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6038"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6045"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6047"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6087"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6089"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6123"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6132"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6139"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6143"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6190"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6213"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6221"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6223"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=6230"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/AutoID/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/AutoID/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="AutoIdOperationStatusEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="SUCCESS_0"/>\n   <xs:enumeration value="MISC_ERROR_TOTAL_1"/>\n   <xs:enumeration value="MISC_ERROR_PARTIAL_2"/>\n   <xs:enumeration value="PERMISSON_ERROR_3"/>\n   <xs:enumeration value="PASSWORD_ERROR_4"/>\n   <xs:enumeration value="REGION_NOT_FOUND_ERROR_5"/>\n   <xs:enumeration value="OP_NOT_POSSIBLE_ERROR_6"/>\n   <xs:enumeration value="OUT_OF_RANGE_ERROR_7"/>\n   <xs:enumeration value="NO_IDENTIFIER_8"/>\n   <xs:enumeration value="MULTIPLE_IDENTIFIERS_9"/>\n   <xs:enumeration value="READ_ERROR_10"/>\n   <xs:enumeration value="DECODING_ERROR_11"/>\n   <xs:enumeration value="MATCH_ERROR_12"/>\n   <xs:enumeration value="CODE_NOT_SUPPORTED_13"/>\n   <xs:enumeration value="WRITE_ERROR_14"/>\n   <xs:enumeration value="NOT_SUPPORTED_BY_DEVICE_15"/>\n   <xs:enumeration value="NOT_SUPPORTED_BY_TAG_16"/>\n   <xs:enumeration value="DEVICE_NOT_READY_17"/>\n   <xs:enumeration value="INVALID_CONFIGURATION_18"/>\n   <xs:enumeration value="RF_COMMUNICATION_ERROR_19"/>\n   <xs:enumeration value="DEVICE_FAULT_20"/>\n   <xs:enumeration value="TAG_HAS_LOW_BATTERY_21"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:AutoIdOperationStatusEnumeration" name="AutoIdOperationStatusEnumeration"/>\n <xs:complexType name="ListOfAutoIdOperationStatusEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AutoIdOperationStatusEnumeration" name="AutoIdOperationStatusEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAutoIdOperationStatusEnumeration" name="ListOfAutoIdOperationStatusEnumeration" nillable="true"/>\n <xs:simpleType name="DeviceStatusEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Idle_0"/>\n   <xs:enumeration value="Error_1"/>\n   <xs:enumeration value="Scanning_2"/>\n   <xs:enumeration value="Busy_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:DeviceStatusEnumeration" name="DeviceStatusEnumeration"/>\n <xs:complexType name="ListOfDeviceStatusEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:DeviceStatusEnumeration" name="DeviceStatusEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfDeviceStatusEnumeration" name="ListOfDeviceStatusEnumeration" nillable="true"/>\n <xs:simpleType name="LocationTypeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="NMEA_0"/>\n   <xs:enumeration value="LOCAL_1"/>\n   <xs:enumeration value="WGS84_2"/>\n   <xs:enumeration value="NAME_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:LocationTypeEnumeration" name="LocationTypeEnumeration"/>\n <xs:complexType name="ListOfLocationTypeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:LocationTypeEnumeration" name="LocationTypeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfLocationTypeEnumeration" name="ListOfLocationTypeEnumeration" nillable="true"/>\n <xs:simpleType name="RfidLockOperationEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Lock_0"/>\n   <xs:enumeration value="Unlock_1"/>\n   <xs:enumeration value="PermanentLock_2"/>\n   <xs:enumeration value="PermanentUnlock_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:RfidLockOperationEnumeration" name="RfidLockOperationEnumeration"/>\n <xs:complexType name="ListOfRfidLockOperationEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RfidLockOperationEnumeration" name="RfidLockOperationEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRfidLockOperationEnumeration" name="ListOfRfidLockOperationEnumeration" nillable="true"/>\n <xs:simpleType name="RfidLockRegionEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Kill_0"/>\n   <xs:enumeration value="Access_1"/>\n   <xs:enumeration value="EPC_2"/>\n   <xs:enumeration value="TID_3"/>\n   <xs:enumeration value="User_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:RfidLockRegionEnumeration" name="RfidLockRegionEnumeration"/>\n <xs:complexType name="ListOfRfidLockRegionEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RfidLockRegionEnumeration" name="RfidLockRegionEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRfidLockRegionEnumeration" name="ListOfRfidLockRegionEnumeration" nillable="true"/>\n <xs:simpleType name="RfidPasswordTypeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Access_0"/>\n   <xs:enumeration value="Kill_1"/>\n   <xs:enumeration value="Read_2"/>\n   <xs:enumeration value="Write_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:RfidPasswordTypeEnumeration" name="RfidPasswordTypeEnumeration"/>\n <xs:complexType name="ListOfRfidPasswordTypeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RfidPasswordTypeEnumeration" name="RfidPasswordTypeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRfidPasswordTypeEnumeration" name="ListOfRfidPasswordTypeEnumeration" nillable="true"/>\n <xs:complexType name="AccessResult">\n  <xs:annotation>\n   <xs:documentation>Result values of an AutoID Identifier access.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="CodeType"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ScanData" name="Identifier"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="Timestamp"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:AccessResult" name="AccessResult"/>\n <xs:complexType name="ListOfAccessResult">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AccessResult" name="AccessResult" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAccessResult" name="ListOfAccessResult" nillable="true"/>\n <xs:complexType name="RfidAccessResult">\n  <xs:annotation>\n   <xs:documentation>Additional result values of an Rfid Transponder access.</xs:documentation>\n  </xs:annotation>\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:AccessResult">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="CodeTypeRWData"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="tns:ScanData" name="RWData"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="Antenna"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="CurrentPowerLevel"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedShort" name="PC"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Polarization"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="Strength"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:RfidAccessResult" name="RfidAccessResult"/>\n <xs:complexType name="ListOfRfidAccessResult">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RfidAccessResult" name="RfidAccessResult" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRfidAccessResult" name="ListOfRfidAccessResult" nillable="true"/>\n <xs:complexType name="AntennaNameIdPair">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="AntennaId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="AntennaName"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:AntennaNameIdPair" name="AntennaNameIdPair"/>\n <xs:complexType name="ListOfAntennaNameIdPair">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AntennaNameIdPair" name="AntennaNameIdPair" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAntennaNameIdPair" name="ListOfAntennaNameIdPair" nillable="true"/>\n <xs:complexType name="DhcpGeoConfCoordinate">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="LaRes"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:short" name="LatitudeInteger"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="LatitudeFraction"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="LoRes"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:short" name="LongitudeInteger"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="LongitudeFraction"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="AT"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="AltRes"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="AltitudeInteger"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:short" name="AltitudeFraction"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="Datum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:DhcpGeoConfCoordinate" name="DhcpGeoConfCoordinate"/>\n <xs:complexType name="ListOfDhcpGeoConfCoordinate">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:DhcpGeoConfCoordinate" name="DhcpGeoConfCoordinate" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfDhcpGeoConfCoordinate" name="ListOfDhcpGeoConfCoordinate" nillable="true"/>\n <xs:complexType name="LocalCoordinate">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="X"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Y"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Z"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="Timestamp"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="DilutionOfPrecision"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="UsefulPrecision"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:LocalCoordinate" name="LocalCoordinate"/>\n <xs:complexType name="ListOfLocalCoordinate">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:LocalCoordinate" name="LocalCoordinate" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfLocalCoordinate" name="ListOfLocalCoordinate" nillable="true"/>\n <xs:complexType name="Position">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="PositionX"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="PositionY"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="SizeX"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="SizeY"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="Rotation"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:Position" name="Position"/>\n <xs:complexType name="ListOfPosition">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:Position" name="Position" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPosition" name="ListOfPosition" nillable="true"/>\n <xs:complexType name="RfidSighting">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="Antenna"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="Strength"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="Timestamp"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="CurrentPowerLevel"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RfidSighting" name="RfidSighting"/>\n <xs:complexType name="ListOfRfidSighting">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RfidSighting" name="RfidSighting" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRfidSighting" name="ListOfRfidSighting" nillable="true"/>\n <xs:complexType name="Rotation">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Yaw"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Pitch"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Roll"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:Rotation" name="Rotation"/>\n <xs:complexType name="ListOfRotation">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:Rotation" name="Rotation" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRotation" name="ListOfRotation" nillable="true"/>\n <xs:complexType name="ScanDataEpc">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedShort" name="PC"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:base64Binary" name="UId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedShort" name="XPC_W1"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedShort" name="XPC_W2"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ScanDataEpc" name="ScanDataEpc"/>\n <xs:complexType name="ListOfScanDataEpc">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ScanDataEpc" name="ScanDataEpc" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfScanDataEpc" name="ListOfScanDataEpc" nillable="true"/>\n <xs:complexType name="ScanResult">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="CodeType"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ScanData" name="ScanData"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="Timestamp"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:Location" name="Location"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ScanResult" name="ScanResult"/>\n <xs:complexType name="ListOfScanResult">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ScanResult" name="ScanResult" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfScanResult" name="ListOfScanResult" nillable="true"/>\n <xs:complexType name="OcrScanResult">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:ScanResult">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:NodeId" name="ImageId"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="Quality"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="tns:Position" name="Position"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Font"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="DecodingTime"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:OcrScanResult" name="OcrScanResult"/>\n <xs:complexType name="ListOfOcrScanResult">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OcrScanResult" name="OcrScanResult" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOcrScanResult" name="ListOfOcrScanResult" nillable="true"/>\n <xs:complexType name="OpticalScanResult">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:ScanResult">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="Grade"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="tns:Position" name="Position"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Symbology"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:NodeId" name="ImageId"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:OpticalScanResult" name="OpticalScanResult"/>\n <xs:complexType name="ListOfOpticalScanResult">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OpticalScanResult" name="OpticalScanResult" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOpticalScanResult" name="ListOfOpticalScanResult" nillable="true"/>\n <xs:complexType name="OpticalVerifierScanResult">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:OpticalScanResult">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="IsoGrade"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:short" name="RMin"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:short" name="SymbolContrast"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:short" name="ECMin"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:short" name="Modulation"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:short" name="Defects"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:short" name="Decodability"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:short" name="Decode"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:short" name="PrintGain"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:OpticalVerifierScanResult" name="OpticalVerifierScanResult"/>\n <xs:complexType name="ListOfOpticalVerifierScanResult">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OpticalVerifierScanResult" name="OpticalVerifierScanResult" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOpticalVerifierScanResult" name="ListOfOpticalVerifierScanResult" nillable="true"/>\n <xs:complexType name="RfidScanResult">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:ScanResult">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfRfidSighting" name="Sighting"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:RfidScanResult" name="RfidScanResult"/>\n <xs:complexType name="ListOfRfidScanResult">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RfidScanResult" name="RfidScanResult" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRfidScanResult" name="ListOfRfidScanResult" nillable="true"/>\n <xs:complexType name="RtlsLocationResult">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:ScanResult">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Speed"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Heading"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="tns:Rotation" name="Rotation"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="ReceiveTime"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:RtlsLocationResult" name="RtlsLocationResult"/>\n <xs:complexType name="ListOfRtlsLocationResult">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RtlsLocationResult" name="RtlsLocationResult" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRtlsLocationResult" name="ListOfRtlsLocationResult" nillable="true"/>\n <xs:complexType name="ScanSettings">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Duration"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="Cycles"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="DataAvailable"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:LocationTypeEnumeration" name="LocationType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ScanSettings" name="ScanSettings"/>\n <xs:complexType name="ListOfScanSettings">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ScanSettings" name="ScanSettings" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfScanSettings" name="ListOfScanSettings" nillable="true"/>\n <xs:complexType name="Location">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="SwitchField"/>\n   <xs:choice>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="NMEA"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:LocalCoordinate" name="Local"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:WGS84Coordinate" name="WGS84"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Name"/>\n   </xs:choice>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:Location" name="Location"/>\n <xs:complexType name="ListOfLocation">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:Location" name="Location" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfLocation" name="ListOfLocation" nillable="true"/>\n <xs:complexType name="ScanData">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="SwitchField"/>\n   <xs:choice>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:base64Binary" name="ByteString"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="String"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:ScanDataEpc" name="Epc"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="ua:Variant" name="Custom"/>\n   </xs:choice>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ScanData" name="ScanData"/>\n <xs:complexType name="ListOfScanData">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ScanData" name="ScanData" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfScanData" name="ListOfScanData" nillable="true"/>\n <xs:complexType name="WGS84Coordinate">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="N/S Hemisphere"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Latitude"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="E/W Hemisphere"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Longitude"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Altitude"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="Timestamp"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="DilutionOfPrecision"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="UsefulPrecisionLatLon"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="UsefulPrecisionAlt"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:WGS84Coordinate" name="WGS84Coordinate"/>\n <xs:complexType name="ListOfWGS84Coordinate">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WGS84Coordinate" name="WGS84Coordinate" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWGS84Coordinate" name="ListOfWGS84Coordinate" nillable="true"/>\n</xs:schema>\n',
)


ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6002",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=auto_id;i=7002", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6002"]))

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6003",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6004",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=auto_id;i=7003", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6003"]), outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6004"]))

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6005",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6006",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=auto_id;i=7004", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6005"]), outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6006"]))

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6008",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6009",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=auto_id;i=7005", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6008"]), outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6009"]))

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6010",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=auto_id;i=7006", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6010"]))

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6014",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=auto_id;i=7007", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6014"]))

ns0.objtypes.FileType(
    nodeId="ns=auto_id;i=5020",
    browseName="ns=auto_id;<ImageName>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6007", browseName="OpenCount", description="The current number of open file handles.", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6011", browseName="Size", description="The size of the file in bytes.", dataType=o6.UInt64)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6012", browseName="UserWritable", description="Whether the file is writable by the current user.", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6013", browseName="Writable", description="Whether the file is writable.", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=auto_id;i=7002"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=7003"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=7004"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=7005"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=7006"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=7007"]),
    ],
)
ns0.objtypes.FolderType(nodeId="ns=auto_id;i=5001", browseName="ns=auto_id;Images", modellingRule="Optional", references=[o6.organizes(o6.ns["ns=auto_id;i=5020"])])
o6.reference(auto_id_objtypes.OpticalReaderDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=auto_id;i=5001"])


ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6072",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=auto_id;i=7011", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6072"]))

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6073",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6074",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=auto_id;i=7012", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6073"]), outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6074"]))

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6075",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6077",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=auto_id;i=7019", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6075"]), outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6077"]))

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6079",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6080",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=auto_id;i=7020", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6079"]), outputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6080"]))

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6081",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=auto_id;i=7021", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6081"]))

ns0.vartypes.PropertyType(
    nodeId="ns=auto_id;i=6085",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=auto_id;i=7022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=auto_id;i=7022", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=auto_id;i=6085"]))

ns0.objtypes.FileType(
    nodeId="ns=auto_id;i=5021",
    browseName="ns=auto_id;<ImageName>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6078", browseName="OpenCount", description="The current number of open file handles.", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6082", browseName="Size", description="The size of the file in bytes.", dataType=o6.UInt64)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6083", browseName="UserWritable", description="Whether the file is writable by the current user.", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=auto_id;i=6084", browseName="Writable", description="Whether the file is writable.", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=auto_id;i=7011"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=7012"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=7019"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=7020"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=7021"]),
        o6.hasComponent(o6.ns["ns=auto_id;i=7022"]),
    ],
)
ns0.objtypes.FolderType(nodeId="ns=auto_id;i=5006", browseName="ns=auto_id;Images", modellingRule="Optional", references=[o6.organizes(o6.ns["ns=auto_id;i=5021"])])
o6.reference(auto_id_objtypes.OcrReaderDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=auto_id;i=5006"])


del Any, TYPE_CHECKING, uuid, o6, di, ns0, auto_id_datypes, auto_id_vartypes, auto_id_objtypes
