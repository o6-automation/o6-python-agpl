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

"""Generated OPC UA gpos namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
import o6.ns.rsl as rsl
from . import datatypes as gpos_datypes
from . import vartypes as gpos_vartypes
from . import objtypes as gpos_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=gpos;i=5001", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=gpos;i=5002", browseName="Default XML")
o6.hasEncoding(gpos_datypes.GlobalPositionDataType, o6.ns["ns=gpos;i=5002"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=gpos;i=5004", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=gpos;i=5005", browseName="Default XML")
o6.hasEncoding(gpos_datypes.GlobalLocationDataType, o6.ns["ns=gpos;i=5005"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=gpos;i=5008", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=gpos;i=5009", browseName="Default XML")
o6.hasEncoding(gpos_datypes.GroundControlPointDataType, o6.ns["ns=gpos;i=5009"])
globalLocations = ns0.objtypes.FolderType(nodeId="ns=gpos;i=5013", browseName="ns=gpos;GlobalLocations", parent="i=31915", referenceType=ns0.reftypes.Organizes)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=gpos;i=5014", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=gpos;i=5015", browseName="Default XML")
o6.hasEncoding(gpos_datypes.ThreeDGeographicCoordinateDataType, o6.ns["ns=gpos;i=5015"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=gpos;i=6007", browseName="ns=gpos;3DGeographicCoordinateDataType", dataType=o6.String, value="3DGeographicCoordinateDataType")
o6.reference(o6.ns["ns=gpos;i=5014"], "i=39", o6.ns["ns=gpos;i=6007"])
ns0.vartypes.ThreeDOrientationType(
    nodeId="ns=gpos;i=6008",
    browseName="ns=rsl;Orientation",
    description="Informs about an orientation typically with respect to a position. In mathematics, orientation defines a geometric notion.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=gpos;i=6014", browseName="A", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=gpos;i=6015", browseName="B", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=gpos;i=6016", browseName="C", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.ThreeDOrientation,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gpos_vartypes.GlobalLocationType, ns0.reftypes.HasComponent, o6.ns["ns=gpos;i=6008"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=gpos;i=6017", browseName="ns=gpos;3DGeographicCoordinateDataType", dataType=o6.String, value="//xs:element[@name='3DGeographicCoordinateDataType']"
)
o6.reference(o6.ns["ns=gpos;i=5015"], "i=39", o6.ns["ns=gpos;i=6017"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=gpos;i=6018", browseName="ns=gpos;GlobalPositionDataType", dataType=o6.String, value="GlobalPositionDataType")
o6.reference(o6.ns["ns=gpos;i=5001"], "i=39", o6.ns["ns=gpos;i=6018"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashGPOSSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=gpos;i=5007",
    browseName="ns=gpos;http://opcfoundation.org/UA/GPOS/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=gpos;i=6019", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gpos;i=6020", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2025-09-25T00:00:00Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gpos;i=6021", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/GPOS/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gpos;i=6022", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gpos;i=6023", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gpos;i=6024", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0], value=[]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gpos;i=6025", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=gpos;i=6033",
    browseName="ns=gpos;CoordinateReferenceSystem",
    description="A projection identifier defining the projection of the provided location coordinate. The CoordinateReferenceSystem shall be either a valid EPSG identifier (https://epsg.io) or 'local' if the location is provided as a relative coordinate of the floor plan. For best interoperability and worldwide coverage, WGS84 (EPSG:4326) should be the preferred projection (as used also by GPS).",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gpos;i=6034",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[122],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("local")),
                    ns0.datatypes.EnumValueType(value=4326, displayName=o6.LocalizedText("GPS")),
                    ns0.datatypes.EnumValueType(value=32601, displayName=o6.LocalizedText("UTM zone 1N")),
                    ns0.datatypes.EnumValueType(value=32602, displayName=o6.LocalizedText("UTM zone 2N")),
                    ns0.datatypes.EnumValueType(value=32603, displayName=o6.LocalizedText("UTM zone 3N")),
                    ns0.datatypes.EnumValueType(value=32604, displayName=o6.LocalizedText("UTM zone 4N")),
                    ns0.datatypes.EnumValueType(value=32605, displayName=o6.LocalizedText("UTM zone 5N")),
                    ns0.datatypes.EnumValueType(value=32606, displayName=o6.LocalizedText("UTM zone 6N")),
                    ns0.datatypes.EnumValueType(value=32607, displayName=o6.LocalizedText("UTM zone 7N")),
                    ns0.datatypes.EnumValueType(value=32608, displayName=o6.LocalizedText("UTM zone 8N")),
                    ns0.datatypes.EnumValueType(value=32609, displayName=o6.LocalizedText("UTM zone 9N")),
                    ns0.datatypes.EnumValueType(value=32610, displayName=o6.LocalizedText("UTM zone 10N")),
                    ns0.datatypes.EnumValueType(value=32611, displayName=o6.LocalizedText("UTM zone 11N")),
                    ns0.datatypes.EnumValueType(value=32612, displayName=o6.LocalizedText("UTM zone 12N")),
                    ns0.datatypes.EnumValueType(value=32613, displayName=o6.LocalizedText("UTM zone 13N")),
                    ns0.datatypes.EnumValueType(value=32614, displayName=o6.LocalizedText("UTM zone 14N")),
                    ns0.datatypes.EnumValueType(value=32615, displayName=o6.LocalizedText("UTM zone 15N")),
                    ns0.datatypes.EnumValueType(value=32616, displayName=o6.LocalizedText("UTM zone 16N")),
                    ns0.datatypes.EnumValueType(value=32617, displayName=o6.LocalizedText("UTM zone 17N")),
                    ns0.datatypes.EnumValueType(value=32618, displayName=o6.LocalizedText("UTM zone 18N")),
                    ns0.datatypes.EnumValueType(value=32619, displayName=o6.LocalizedText("UTM zone 19N")),
                    ns0.datatypes.EnumValueType(value=32620, displayName=o6.LocalizedText("UTM zone 20N")),
                    ns0.datatypes.EnumValueType(value=32621, displayName=o6.LocalizedText("UTM zone 21N")),
                    ns0.datatypes.EnumValueType(value=32622, displayName=o6.LocalizedText("UTM zone 22N")),
                    ns0.datatypes.EnumValueType(value=32623, displayName=o6.LocalizedText("UTM zone 23N")),
                    ns0.datatypes.EnumValueType(value=32624, displayName=o6.LocalizedText("UTM zone 24N")),
                    ns0.datatypes.EnumValueType(value=32625, displayName=o6.LocalizedText("UTM zone 25N")),
                    ns0.datatypes.EnumValueType(value=32626, displayName=o6.LocalizedText("UTM zone 26N")),
                    ns0.datatypes.EnumValueType(value=32627, displayName=o6.LocalizedText("UTM zone 27N")),
                    ns0.datatypes.EnumValueType(value=32628, displayName=o6.LocalizedText("UTM zone 28N")),
                    ns0.datatypes.EnumValueType(value=32629, displayName=o6.LocalizedText("UTM zone 29N")),
                    ns0.datatypes.EnumValueType(value=32630, displayName=o6.LocalizedText("UTM zone 30N")),
                    ns0.datatypes.EnumValueType(value=32631, displayName=o6.LocalizedText("UTM zone 31N")),
                    ns0.datatypes.EnumValueType(value=32632, displayName=o6.LocalizedText("UTM zone 32N")),
                    ns0.datatypes.EnumValueType(value=32633, displayName=o6.LocalizedText("UTM zone 33N")),
                    ns0.datatypes.EnumValueType(value=32634, displayName=o6.LocalizedText("UTM zone 34N")),
                    ns0.datatypes.EnumValueType(value=32635, displayName=o6.LocalizedText("UTM zone 35N")),
                    ns0.datatypes.EnumValueType(value=32636, displayName=o6.LocalizedText("UTM zone 36N")),
                    ns0.datatypes.EnumValueType(value=32637, displayName=o6.LocalizedText("UTM zone 37N")),
                    ns0.datatypes.EnumValueType(value=32638, displayName=o6.LocalizedText("UTM zone 38N")),
                    ns0.datatypes.EnumValueType(value=32639, displayName=o6.LocalizedText("UTM zone 39N")),
                    ns0.datatypes.EnumValueType(value=32640, displayName=o6.LocalizedText("UTM zone 40N")),
                    ns0.datatypes.EnumValueType(value=32641, displayName=o6.LocalizedText("UTM zone 41N")),
                    ns0.datatypes.EnumValueType(value=32642, displayName=o6.LocalizedText("UTM zone 42N")),
                    ns0.datatypes.EnumValueType(value=32643, displayName=o6.LocalizedText("UTM zone 43N")),
                    ns0.datatypes.EnumValueType(value=32644, displayName=o6.LocalizedText("UTM zone 44N")),
                    ns0.datatypes.EnumValueType(value=32645, displayName=o6.LocalizedText("UTM zone 45N")),
                    ns0.datatypes.EnumValueType(value=32646, displayName=o6.LocalizedText("UTM zone 46N")),
                    ns0.datatypes.EnumValueType(value=32647, displayName=o6.LocalizedText("UTM zone 47N")),
                    ns0.datatypes.EnumValueType(value=32648, displayName=o6.LocalizedText("UTM zone 48N")),
                    ns0.datatypes.EnumValueType(value=32649, displayName=o6.LocalizedText("UTM zone 49N")),
                    ns0.datatypes.EnumValueType(value=32650, displayName=o6.LocalizedText("UTM zone 50N")),
                    ns0.datatypes.EnumValueType(value=32651, displayName=o6.LocalizedText("UTM zone 51N")),
                    ns0.datatypes.EnumValueType(value=32652, displayName=o6.LocalizedText("UTM zone 52N")),
                    ns0.datatypes.EnumValueType(value=32653, displayName=o6.LocalizedText("UTM zone 53N")),
                    ns0.datatypes.EnumValueType(value=32654, displayName=o6.LocalizedText("UTM zone 54N")),
                    ns0.datatypes.EnumValueType(value=32655, displayName=o6.LocalizedText("UTM zone 55N")),
                    ns0.datatypes.EnumValueType(value=32656, displayName=o6.LocalizedText("UTM zone 56N")),
                    ns0.datatypes.EnumValueType(value=32657, displayName=o6.LocalizedText("UTM zone 57N")),
                    ns0.datatypes.EnumValueType(value=32658, displayName=o6.LocalizedText("UTM zone 58N")),
                    ns0.datatypes.EnumValueType(value=32659, displayName=o6.LocalizedText("UTM zone 59N")),
                    ns0.datatypes.EnumValueType(value=32661, displayName=o6.LocalizedText("UPS North (N,E)")),
                    ns0.datatypes.EnumValueType(value=32701, displayName=o6.LocalizedText("UTM zone 1S")),
                    ns0.datatypes.EnumValueType(value=32702, displayName=o6.LocalizedText("UTM zone 2S")),
                    ns0.datatypes.EnumValueType(value=32703, displayName=o6.LocalizedText("UTM zone 3S")),
                    ns0.datatypes.EnumValueType(value=32704, displayName=o6.LocalizedText("UTM zone 4S")),
                    ns0.datatypes.EnumValueType(value=32705, displayName=o6.LocalizedText("UTM zone 5S")),
                    ns0.datatypes.EnumValueType(value=32706, displayName=o6.LocalizedText("UTM zone 6S")),
                    ns0.datatypes.EnumValueType(value=32707, displayName=o6.LocalizedText("UTM zone 7S")),
                    ns0.datatypes.EnumValueType(value=32708, displayName=o6.LocalizedText("UTM zone 8S")),
                    ns0.datatypes.EnumValueType(value=32709, displayName=o6.LocalizedText("UTM zone 9S")),
                    ns0.datatypes.EnumValueType(value=32710, displayName=o6.LocalizedText("UTM zone 10S")),
                    ns0.datatypes.EnumValueType(value=32711, displayName=o6.LocalizedText("UTM zone 11S")),
                    ns0.datatypes.EnumValueType(value=32712, displayName=o6.LocalizedText("UTM zone 12S")),
                    ns0.datatypes.EnumValueType(value=32713, displayName=o6.LocalizedText("UTM zone 13S")),
                    ns0.datatypes.EnumValueType(value=32714, displayName=o6.LocalizedText("UTM zone 14S")),
                    ns0.datatypes.EnumValueType(value=32715, displayName=o6.LocalizedText("UTM zone 15S")),
                    ns0.datatypes.EnumValueType(value=32716, displayName=o6.LocalizedText("UTM zone 16S")),
                    ns0.datatypes.EnumValueType(value=32717, displayName=o6.LocalizedText("UTM zone 17S")),
                    ns0.datatypes.EnumValueType(value=32718, displayName=o6.LocalizedText("UTM zone 18S")),
                    ns0.datatypes.EnumValueType(value=32719, displayName=o6.LocalizedText("UTM zone 19S")),
                    ns0.datatypes.EnumValueType(value=32720, displayName=o6.LocalizedText("UTM zone 20S")),
                    ns0.datatypes.EnumValueType(value=32721, displayName=o6.LocalizedText("UTM zone 21S")),
                    ns0.datatypes.EnumValueType(value=32722, displayName=o6.LocalizedText("UTM zone 22S")),
                    ns0.datatypes.EnumValueType(value=32723, displayName=o6.LocalizedText("UTM zone 23S")),
                    ns0.datatypes.EnumValueType(value=32724, displayName=o6.LocalizedText("UTM zone 24S")),
                    ns0.datatypes.EnumValueType(value=32725, displayName=o6.LocalizedText("UTM zone 25S")),
                    ns0.datatypes.EnumValueType(value=32726, displayName=o6.LocalizedText("UTM zone 26S")),
                    ns0.datatypes.EnumValueType(value=32727, displayName=o6.LocalizedText("UTM zone 27S")),
                    ns0.datatypes.EnumValueType(value=32728, displayName=o6.LocalizedText("UTM zone 28S")),
                    ns0.datatypes.EnumValueType(value=32729, displayName=o6.LocalizedText("UTM zone 29S")),
                    ns0.datatypes.EnumValueType(value=32730, displayName=o6.LocalizedText("UTM zone 30S")),
                    ns0.datatypes.EnumValueType(value=32731, displayName=o6.LocalizedText("UTM zone 31S")),
                    ns0.datatypes.EnumValueType(value=32732, displayName=o6.LocalizedText("UTM zone 32S")),
                    ns0.datatypes.EnumValueType(value=32733, displayName=o6.LocalizedText("UTM zone 33S")),
                    ns0.datatypes.EnumValueType(value=32734, displayName=o6.LocalizedText("UTM zone 34S")),
                    ns0.datatypes.EnumValueType(value=32735, displayName=o6.LocalizedText("UTM zone 35S")),
                    ns0.datatypes.EnumValueType(value=32736, displayName=o6.LocalizedText("UTM zone 36S")),
                    ns0.datatypes.EnumValueType(value=32737, displayName=o6.LocalizedText("UTM zone 37S")),
                    ns0.datatypes.EnumValueType(value=32738, displayName=o6.LocalizedText("UTM zone 38S")),
                    ns0.datatypes.EnumValueType(value=32739, displayName=o6.LocalizedText("UTM zone 39S")),
                    ns0.datatypes.EnumValueType(value=32740, displayName=o6.LocalizedText("UTM zone 40S")),
                    ns0.datatypes.EnumValueType(value=32741, displayName=o6.LocalizedText("UTM zone 41S")),
                    ns0.datatypes.EnumValueType(value=32742, displayName=o6.LocalizedText("UTM zone 42S")),
                    ns0.datatypes.EnumValueType(value=32743, displayName=o6.LocalizedText("UTM zone 43S")),
                    ns0.datatypes.EnumValueType(value=32744, displayName=o6.LocalizedText("UTM zone 44S")),
                    ns0.datatypes.EnumValueType(value=32745, displayName=o6.LocalizedText("UTM zone 45S")),
                    ns0.datatypes.EnumValueType(value=32746, displayName=o6.LocalizedText("UTM zone 46S")),
                    ns0.datatypes.EnumValueType(value=32747, displayName=o6.LocalizedText("UTM zone 47S")),
                    ns0.datatypes.EnumValueType(value=32748, displayName=o6.LocalizedText("UTM zone 48S")),
                    ns0.datatypes.EnumValueType(value=32749, displayName=o6.LocalizedText("UTM zone 49S")),
                    ns0.datatypes.EnumValueType(value=32750, displayName=o6.LocalizedText("UTM zone 50S")),
                    ns0.datatypes.EnumValueType(value=32751, displayName=o6.LocalizedText("UTM zone 51S")),
                    ns0.datatypes.EnumValueType(value=32752, displayName=o6.LocalizedText("UTM zone 52S")),
                    ns0.datatypes.EnumValueType(value=32753, displayName=o6.LocalizedText("UTM zone 53S")),
                    ns0.datatypes.EnumValueType(value=32754, displayName=o6.LocalizedText("UTM zone 54S")),
                    ns0.datatypes.EnumValueType(value=32755, displayName=o6.LocalizedText("UTM zone 55S")),
                    ns0.datatypes.EnumValueType(value=32756, displayName=o6.LocalizedText("UTM zone 56S")),
                    ns0.datatypes.EnumValueType(value=32757, displayName=o6.LocalizedText("UTM zone 57S")),
                    ns0.datatypes.EnumValueType(value=32758, displayName=o6.LocalizedText("UTM zone 58S")),
                    ns0.datatypes.EnumValueType(value=32759, displayName=o6.LocalizedText("UTM zone 59S")),
                    ns0.datatypes.EnumValueType(value=32761, displayName=o6.LocalizedText("UPS South (N,E)")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gpos;i=6035", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gpos_vartypes.GlobalPositionType, ns0.reftypes.HasComponent, o6.ns["ns=gpos;i=6033"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=gpos;i=6040", browseName="ns=gpos;GlobalPositionDataType", dataType=o6.String, value="//xs:element[@name='GlobalPositionDataType']")
o6.reference(o6.ns["ns=gpos;i=5002"], "i=39", o6.ns["ns=gpos;i=6040"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=gpos;i=6041", browseName="ns=gpos;GlobalLocationDataType", dataType=o6.String, value="GlobalLocationDataType")
o6.reference(o6.ns["ns=gpos;i=5004"], "i=39", o6.ns["ns=gpos;i=6041"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=gpos;i=6042", browseName="ns=gpos;GlobalLocationDataType", dataType=o6.String, value="//xs:element[@name='GlobalLocationDataType']")
o6.reference(o6.ns["ns=gpos;i=5005"], "i=39", o6.ns["ns=gpos;i=6042"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=gpos;i=6044", browseName="ns=gpos;GroundControlPointDataType", dataType=o6.String, value="GroundControlPointDataType")
o6.reference(o6.ns["ns=gpos;i=5008"], "i=39", o6.ns["ns=gpos;i=6044"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=gpos;i=6001",
    browseName="ns=gpos;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/GPOS/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gpos;i=6002", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/GPOS/")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=gpos;i=6003",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=gpos;i=6007"]),
        o6.hasComponent(o6.ns["ns=gpos;i=6018"]),
        o6.hasComponent(o6.ns["ns=gpos;i=6041"]),
        o6.hasComponent(o6.ns["ns=gpos;i=6044"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:ua="http://opcfoundation.org/UA/" DefaultByteOrder="LittleEndian" xmlns:tns="http://opcfoundation.org/UA/GPOS/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" TargetNamespace="http://opcfoundation.org/UA/GPOS/" xmlns:opc="http://opcfoundation.org/BinarySchema/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="3DGeographicCoordinateDataType">\n  <opc:Documentation>Represents a geographic coordinate</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="ElevationSpecified"/>\n  <opc:Field Length="31" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:Double" Name="Longitude"/>\n  <opc:Field TypeName="opc:Double" Name="Latitude"/>\n  <opc:Field SwitchField="ElevationSpecified" TypeName="opc:Double" Name="Elevation"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:3DGeographicCoordinateDataType" Name="GlobalPositionDataType">\n  <opc:Documentation>Represents a global position</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="ElevationSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="AccuracySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="FloorSpecified"/>\n  <opc:Field Length="29" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:Double" SourceType="tns:3DGeographicCoordinateDataType" Name="Longitude"/>\n  <opc:Field TypeName="opc:Double" SourceType="tns:3DGeographicCoordinateDataType" Name="Latitude"/>\n  <opc:Field SwitchField="ElevationSpecified" TypeName="opc:Double" SourceType="tns:3DGeographicCoordinateDataType" Name="Elevation"/>\n  <opc:Field SwitchField="AccuracySpecified" TypeName="opc:Double" Name="Accuracy"/>\n  <opc:Field SwitchField="FloorSpecified" TypeName="opc:Float" Name="Floor"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="GlobalLocationDataType">\n  <opc:Documentation>Represents a global location</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="OrientationSpecified"/>\n  <opc:Field Length="31" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="tns:GlobalPositionDataType" Name="Position"/>\n  <opc:Field SwitchField="OrientationSpecified" TypeName="ua:3DOrientation" Name="Orientation"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="GroundControlPointDataType">\n  <opc:Documentation>Defines a pair of coordinates - local and global - to allow geo-references from local coordinate to a global coordinate system</opc:Documentation>\n  <opc:Field TypeName="tns:3DGeographicCoordinateDataType" Name="GlobalPosition"/>\n  <opc:Field TypeName="ua:3DCartesianCoordinates" Name="LocalPosition"/>\n </opc:StructuredType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=gpos;i=6036",
    browseName="ns=gpos;CoordinateReferenceSystem",
    description="A projection identifier defining the projection of the provided location coordinate. The CoordinateReferenceSystem shall be either a valid EPSG identifier (https://epsg.io) or 'local' if the location is provided as a relative coordinate of the floor plan. For best interoperability and worldwide coverage, WGS84 (EPSG:4326) should be the preferred projection (as used also by GPS).",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gpos;i=6037",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[2],
                value=[ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("local")), ns0.datatypes.EnumValueType(value=4326, displayName=o6.LocalizedText("GPS"))],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gpos;i=6048", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
gpos_vartypes.GlobalPositionType(
    nodeId="ns=gpos;i=6009",
    browseName="ns=rsl;Position",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gpos;i=6039",
                browseName="ns=gpos;SourceId",
                description="Reference to the zone or provider calculating the position",
                dataType=o6.NodeId,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=gpos;i=6031",
                browseName="ns=gpos;Longitude",
                description="MUST be interpreted according to the CoordinateReferenceSystem",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=gpos;i=6032",
                browseName="ns=gpos;Latitude",
                description="MUST be interpreted according to the CoordinateReferenceSystem",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=gpos;i=6036"]),
    ],
    dataType=gpos_datypes.GlobalPositionDataType,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gpos_vartypes.GlobalLocationType, ns0.reftypes.HasComponent, o6.ns["ns=gpos;i=6009"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=gpos;i=6049",
    browseName="ns=gpos;ElevationReference",
    description="An elevation reference hint for the position's Elevation. If present it shall be either 'floor' or 'wgs84'. If set to 'floor' the Elevation shall be assumed to be relative to the floor level in meter. If set to 'wgs84' the Elevation shall be treated as WGS84 ellipsoidal height. For the majority of applications an accurate geographic height may not be available. Therefore ElevationReference shall be assumed 'floor' by default if it is not present.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gpos;i=6050",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[2],
                value=[ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("floor")), ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("wgs84"))],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gpos;i=6051", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.Byte,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gpos_vartypes.GlobalPositionType, ns0.reftypes.HasComponent, o6.ns["ns=gpos;i=6049"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=gpos;i=6052", browseName="ns=gpos;GroundControlPointDataType", dataType=o6.String, value="//xs:element[@name='GroundControlPointDataType']"
)
o6.reference(o6.ns["ns=gpos;i=5009"], "i=39", o6.ns["ns=gpos;i=6052"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=gpos;i=6004",
    browseName="ns=gpos;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/GPOS/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gpos;i=6005", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/GPOS/Types.xsd")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=gpos;i=6006",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=gpos;i=6017"]),
        o6.hasComponent(o6.ns["ns=gpos;i=6040"]),
        o6.hasComponent(o6.ns["ns=gpos;i=6042"]),
        o6.hasComponent(o6.ns["ns=gpos;i=6052"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/GPOS/Types.xsd" targetNamespace="http://opcfoundation.org/UA/GPOS/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:complexType name="3DGeographicCoordinateDataType">\n  <xs:annotation>\n   <xs:documentation>Represents a geographic coordinate</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:unsignedInt" minOccurs="0" name="EncodingMask"/>\n   <xs:element type="xs:double" minOccurs="0" maxOccurs="1" name="Longitude"/>\n   <xs:element type="xs:double" minOccurs="0" maxOccurs="1" name="Latitude"/>\n   <xs:element type="xs:double" minOccurs="0" maxOccurs="1" name="Elevation"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:3DGeographicCoordinateDataType" name="3DGeographicCoordinateDataType"/>\n <xs:complexType name="ListOf3DGeographicCoordinateDataType">\n  <xs:sequence>\n   <xs:element nillable="true" type="tns:3DGeographicCoordinateDataType" minOccurs="0" maxOccurs="unbounded" name="3DGeographicCoordinateDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element nillable="true" type="tns:ListOf3DGeographicCoordinateDataType" name="ListOf3DGeographicCoordinateDataType"/>\n <xs:complexType name="GlobalPositionDataType">\n  <xs:annotation>\n   <xs:documentation>Represents a global position</xs:documentation>\n  </xs:annotation>\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:3DGeographicCoordinateDataType">\n    <xs:sequence>\n     <xs:element type="xs:double" minOccurs="0" maxOccurs="1" name="Accuracy"/>\n     <xs:element type="xs:float" minOccurs="0" maxOccurs="1" name="Floor"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:GlobalPositionDataType" name="GlobalPositionDataType"/>\n <xs:complexType name="ListOfGlobalPositionDataType">\n  <xs:sequence>\n   <xs:element nillable="true" type="tns:GlobalPositionDataType" minOccurs="0" maxOccurs="unbounded" name="GlobalPositionDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element nillable="true" type="tns:ListOfGlobalPositionDataType" name="ListOfGlobalPositionDataType"/>\n <xs:complexType name="GlobalLocationDataType">\n  <xs:annotation>\n   <xs:documentation>Represents a global location</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="xs:unsignedInt" minOccurs="0" name="EncodingMask"/>\n   <xs:element type="tns:GlobalPositionDataType" minOccurs="0" maxOccurs="1" name="Position"/>\n   <xs:element type="ua:3DOrientation" minOccurs="0" maxOccurs="1" name="Orientation"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:GlobalLocationDataType" name="GlobalLocationDataType"/>\n <xs:complexType name="ListOfGlobalLocationDataType">\n  <xs:sequence>\n   <xs:element nillable="true" type="tns:GlobalLocationDataType" minOccurs="0" maxOccurs="unbounded" name="GlobalLocationDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element nillable="true" type="tns:ListOfGlobalLocationDataType" name="ListOfGlobalLocationDataType"/>\n <xs:complexType name="GroundControlPointDataType">\n  <xs:annotation>\n   <xs:documentation>Defines a pair of coordinates - local and global - to allow geo-references from local coordinate to a global coordinate system</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element type="tns:3DGeographicCoordinateDataType" minOccurs="0" maxOccurs="1" name="GlobalPosition"/>\n   <xs:element type="ua:3DCartesianCoordinates" minOccurs="0" maxOccurs="1" name="LocalPosition"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:GroundControlPointDataType" name="GroundControlPointDataType"/>\n <xs:complexType name="ListOfGroundControlPointDataType">\n  <xs:sequence>\n   <xs:element nillable="true" type="tns:GroundControlPointDataType" minOccurs="0" maxOccurs="unbounded" name="GroundControlPointDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element nillable="true" type="tns:ListOfGroundControlPointDataType" name="ListOfGroundControlPointDataType"/>\n</xs:schema>\n',
)


del Any, TYPE_CHECKING, uuid, o6, ns0, rsl, gpos_datypes, gpos_vartypes, gpos_objtypes
