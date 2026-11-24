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

"""Generated OPC UA cnc namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import datatypes as cnc_datypes
from . import vartypes as cnc_vartypes
from . import objtypes as cnc_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=cnc;i=5001", browseName="Default Binary")
axes = ns0.objtypes.FolderType(nodeId="ns=cnc;i=5004", browseName="ns=cnc;Axes")
spindles = ns0.objtypes.FolderType(nodeId="ns=cnc;i=5005", browseName="ns=cnc;Spindles")
channels = ns0.objtypes.FolderType(nodeId="ns=cnc;i=5006", browseName="ns=cnc;Channels")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=cnc;i=5007", browseName="Default XML")
o6.hasEncoding(cnc_datypes.CncPositionDataType, o6.ns["ns=cnc;i=5007"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6005",
    browseName="ns=cnc;ActFeedrate",
    description="Feedrate actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6006", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6010",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4732977,
                    displayName=o6.LocalizedText("mm/min"),
                    description=o6.LocalizedText("millimetre per minute"),
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncChannelType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6005"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6001",
    browseName="ns=cnc;ActOverride",
    description="Axis override actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6002", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6011",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncChannelType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6001"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6007",
    browseName="ns=cnc;CmdFeedrate",
    description="Feedrate setpoint value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6008", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6012",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4732977,
                    displayName=o6.LocalizedText("mm/min"),
                    description=o6.LocalizedText("millimetre per minute"),
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncChannelType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6007"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6003",
    browseName="ns=cnc;CmdOverride",
    description="Override setpoint value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6004", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6013",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncChannelType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6003"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6024",
    browseName="ns=cnc;DryRunFeed",
    description="Test feedrate.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6014",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4732977,
                    displayName=o6.LocalizedText("mm/min"),
                    description=o6.LocalizedText("millimetre per minute"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6025", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncChannelType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6024"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=cnc;i=6042", browseName="ns=cnc;CncPositionDataType", dataType=o6.String, value="CncPositionDataType")
o6.reference(o6.ns["ns=cnc;i=5001"], "i=39", o6.ns["ns=cnc;i=6042"])
cncSystems = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=cnc;i=6022",
    browseName="ns=cnc;CncSystems",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/CNC",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6035", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/CNC")),
        o6.hasComponent(o6.ns["ns=cnc;i=6042"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/CNC" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/CNC">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="CncPositionDataType">\n  <opc:Documentation>Structure of position elements.</opc:Documentation>\n  <opc:Field TypeName="opc:Double" Name="ActPos"/>\n  <opc:Field TypeName="opc:Double" Name="CmdPos"/>\n  <opc:Field TypeName="opc:Double" Name="RemDist"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="CncAxisStatus">\n  <opc:Documentation>Status of a CNC axis.</opc:Documentation>\n  <opc:EnumeratedValue Name="InPosition" Value="0"/>\n  <opc:EnumeratedValue Name="Moving" Value="1"/>\n  <opc:EnumeratedValue Name="Parked" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="CncChannelProgramStatus">\n  <opc:Documentation>Status of program execution within a channel.</opc:Documentation>\n  <opc:EnumeratedValue Name="Stopped" Value="0"/>\n  <opc:EnumeratedValue Name="Running" Value="1"/>\n  <opc:EnumeratedValue Name="Waiting" Value="2"/>\n  <opc:EnumeratedValue Name="Interrupted" Value="3"/>\n  <opc:EnumeratedValue Name="Canceled" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="CncChannelStatus">\n  <opc:Documentation>Status of a CNC channel.</opc:Documentation>\n  <opc:EnumeratedValue Name="Active" Value="0"/>\n  <opc:EnumeratedValue Name="Interrupted" Value="1"/>\n  <opc:EnumeratedValue Name="Reset" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="CncOperationMode">\n  <opc:Documentation>Modes of operation.</opc:Documentation>\n  <opc:EnumeratedValue Name="Manual" Value="0"/>\n  <opc:EnumeratedValue Name="MDA" Value="1"/>\n  <opc:EnumeratedValue Name="Automatic" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="CncSpindleStatus">\n  <opc:Documentation>Status of a CNC spindle.</opc:Documentation>\n  <opc:EnumeratedValue Name="Stopped" Value="0"/>\n  <opc:EnumeratedValue Name="InTargetArea" Value="1"/>\n  <opc:EnumeratedValue Name="Accelerating" Value="2"/>\n  <opc:EnumeratedValue Name="Decelerating" Value="3"/>\n  <opc:EnumeratedValue Name="Parked" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="CncSpindleTurnDirection">\n  <opc:Documentation>Turn direction of a CNC spindle.</opc:Documentation>\n  <opc:EnumeratedValue Name="None" Value="0"/>\n  <opc:EnumeratedValue Name="CW" Value="1"/>\n  <opc:EnumeratedValue Name="CCW" Value="2"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=cnc;i=6043", browseName="ns=cnc;CncPositionDataType", dataType=o6.String, value="//xs:element[@name='CncPositionDataType']")
o6.reference(o6.ns["ns=cnc;i=5007"], "i=39", o6.ns["ns=cnc;i=6043"])
cncSystems_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=cnc;i=6038",
    browseName="ns=cnc;CncSystems",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/CNC",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6040", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/CNC/Types.xsd")),
        o6.hasComponent(o6.ns["ns=cnc;i=6043"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/CNC/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/CNC/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="CncAxisStatus">\n  <xs:annotation>\n   <xs:documentation>Status of a CNC axis.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="InPosition_0"/>\n   <xs:enumeration value="Moving_1"/>\n   <xs:enumeration value="Parked_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:CncAxisStatus" name="CncAxisStatus"/>\n <xs:complexType name="ListOfCncAxisStatus">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CncAxisStatus" name="CncAxisStatus" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCncAxisStatus" name="ListOfCncAxisStatus" nillable="true"/>\n <xs:simpleType name="CncChannelProgramStatus">\n  <xs:annotation>\n   <xs:documentation>Status of program execution within a channel.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Stopped_0"/>\n   <xs:enumeration value="Running_1"/>\n   <xs:enumeration value="Waiting_2"/>\n   <xs:enumeration value="Interrupted_3"/>\n   <xs:enumeration value="Canceled_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:CncChannelProgramStatus" name="CncChannelProgramStatus"/>\n <xs:complexType name="ListOfCncChannelProgramStatus">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CncChannelProgramStatus" name="CncChannelProgramStatus" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCncChannelProgramStatus" name="ListOfCncChannelProgramStatus" nillable="true"/>\n <xs:simpleType name="CncChannelStatus">\n  <xs:annotation>\n   <xs:documentation>Status of a CNC channel.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Active_0"/>\n   <xs:enumeration value="Interrupted_1"/>\n   <xs:enumeration value="Reset_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:CncChannelStatus" name="CncChannelStatus"/>\n <xs:complexType name="ListOfCncChannelStatus">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CncChannelStatus" name="CncChannelStatus" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCncChannelStatus" name="ListOfCncChannelStatus" nillable="true"/>\n <xs:simpleType name="CncOperationMode">\n  <xs:annotation>\n   <xs:documentation>Modes of operation.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Manual_0"/>\n   <xs:enumeration value="MDA_1"/>\n   <xs:enumeration value="Automatic_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:CncOperationMode" name="CncOperationMode"/>\n <xs:complexType name="ListOfCncOperationMode">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CncOperationMode" name="CncOperationMode" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCncOperationMode" name="ListOfCncOperationMode" nillable="true"/>\n <xs:simpleType name="CncSpindleStatus">\n  <xs:annotation>\n   <xs:documentation>Status of a CNC spindle.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Stopped_0"/>\n   <xs:enumeration value="InTargetArea_1"/>\n   <xs:enumeration value="Accelerating_2"/>\n   <xs:enumeration value="Decelerating_3"/>\n   <xs:enumeration value="Parked_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:CncSpindleStatus" name="CncSpindleStatus"/>\n <xs:complexType name="ListOfCncSpindleStatus">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CncSpindleStatus" name="CncSpindleStatus" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCncSpindleStatus" name="ListOfCncSpindleStatus" nillable="true"/>\n <xs:simpleType name="CncSpindleTurnDirection">\n  <xs:annotation>\n   <xs:documentation>Turn direction of a CNC spindle.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="None_0"/>\n   <xs:enumeration value="CW_1"/>\n   <xs:enumeration value="CCW_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:CncSpindleTurnDirection" name="CncSpindleTurnDirection"/>\n <xs:complexType name="ListOfCncSpindleTurnDirection">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CncSpindleTurnDirection" name="CncSpindleTurnDirection" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCncSpindleTurnDirection" name="ListOfCncSpindleTurnDirection" nillable="true"/>\n <xs:complexType name="CncPositionDataType">\n  <xs:annotation>\n   <xs:documentation>Structure of position elements.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="ActPos"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="CmdPos"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="RemDist"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:CncPositionDataType" name="CncPositionDataType"/>\n <xs:complexType name="ListOfCncPositionDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CncPositionDataType" name="CncPositionDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCncPositionDataType" name="ListOfCncPositionDataType" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6060",
    browseName="ns=cnc;ActLoad",
    description="Drive load actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6015",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6061", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncDriveType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6060"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6062",
    browseName="ns=cnc;ActPower",
    description="Drive power actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6018",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6063", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncDriveType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6062"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6064",
    browseName="ns=cnc;ActTorque",
    description="Drive torque actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6021",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6065", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncDriveType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6064"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6066",
    browseName="ns=cnc;CmdTorque",
    description="Drive torque setpoint value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6036",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6067", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0)
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncDriveType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6066"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6077",
    browseName="ns=cnc;ActSpeed",
    description="Speed actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6078",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4405556,
                    displayName=o6.LocalizedText("min⁻¹"),
                    description=o6.LocalizedText("reciprocal minute"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6079", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6072",
    browseName="ns=cnc;AnglePos",
    description="Spindle angular position values in case of interpolated (position controlled) spindle movement. Returns zeros in case of regular spindle operation (velocity controlled).",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6083", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6084", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6073", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6074", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6085", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncSpindleType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6072"])
test = cnc_objtypes.CncInterfaceType(
    nodeId="ns=cnc;i=5008",
    browseName="ns=cnc;test",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6075",
                browseName="ns=cnc;VendorName",
                description="Name of CNC system vendor. Format and content may be chosen by vendor.",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6093",
                browseName="ns=cnc;VendorRevision",
                description="Vendor revision of CNC interface. Format and content may be chosen by vendor.",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6094",
                browseName="ns=cnc;Version",
                description="Version of CNC interface - corresponds to version of OPC UA companion standard.",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
            )
        ),
        o6.hasComponent(cnc_objtypes.CncAxisListType(nodeId="ns=cnc;i=5009", browseName="ns=cnc;CncAxisList", description="List of CNC axis objects.")),
        o6.hasComponent(cnc_objtypes.CncChannelListType(nodeId="ns=cnc;i=5010", browseName="ns=cnc;CncChannelList", description="List of CNC channel objects.")),
        o6.hasComponent(cnc_objtypes.CncSpindleListType(nodeId="ns=cnc;i=5016", browseName="ns=cnc;CncSpindleList", description="List of CNC spindle objects.")),
    ],
    parent="i=85",
    referenceType=ns0.reftypes.Organizes,
)
o6.reference(test, "i=41", cnc_objtypes.CncAlarmType)
o6.reference(test, "i=41", cnc_objtypes.CncMessageType)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6096",
    browseName="ns=cnc;CmdSpeed",
    description="Speed setpoint value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6097",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4405556,
                    displayName=o6.LocalizedText("min⁻¹"),
                    description=o6.LocalizedText("reciprocal minute"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6103", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6105",
    browseName="ns=cnc;ActLoad",
    description="Drive load actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6106",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6107", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6108",
    browseName="ns=cnc;ActPower",
    description="Drive power actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6109",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6110", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6111",
    browseName="ns=cnc;ActTorque",
    description="Drive torque actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6112",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6113", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6114",
    browseName="ns=cnc;CmdTorque",
    description="Drive torque setpoint value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6115",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6116", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0)
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6119",
    browseName="ns=cnc;ActFeedrate",
    description="Feedrate actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6129",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4732977,
                    displayName=o6.LocalizedText("mm/min"),
                    description=o6.LocalizedText("millimetre per minute"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6131", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6139",
    browseName="ns=cnc;ActJogIncrement",
    description="Active JOG increment.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6142",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5066068, displayName=o6.LocalizedText("mm"), description=o6.LocalizedText("millimetre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6145", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=cnc;i=6146",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cnc;i=3001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("None"), description=o6.LocalizedText("No rotation", "en")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("CW"), description=o6.LocalizedText("Clockwise", "en")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("CCW"), description=o6.LocalizedText("Counter Clockwise", "en")),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6151",
    browseName="ns=cnc;ActOverride",
    description="Axis override actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6152",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6153", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6100",
    browseName="ns=cnc;ZeroOffset",
    description="Active axis zero offset.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6101", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6154",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5066068, displayName=o6.LocalizedText("mm"), description=o6.LocalizedText("millimetre")
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncAxisType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6100"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6026",
    browseName="ns=cnc;ActJogIncrement",
    description="Active JOG increment.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6027", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6155",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5066068, displayName=o6.LocalizedText("mm"), description=o6.LocalizedText("millimetre")
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncChannelType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6026"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6120",
    browseName="ns=cnc;ActSpeed",
    description="Speed actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6121", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6161",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4405556,
                    displayName=o6.LocalizedText("min⁻¹"),
                    description=o6.LocalizedText("reciprocal minute"),
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncSpindleType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6120"])
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6124",
    browseName="ns=cnc;AnglePos",
    description="Spindle angular position values in case of interpolated (position controlled) spindle movement. Returns zeros in case of regular spindle operation (velocity controlled).",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6127", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6157", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6125", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6126", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6165", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6122",
    browseName="ns=cnc;CmdSpeed",
    description="Speed setpoint value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6123", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6169",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4405556,
                    displayName=o6.LocalizedText("min⁻¹"),
                    description=o6.LocalizedText("reciprocal minute"),
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncSpindleType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6122"])
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6039",
    browseName="ns=cnc;PosIndirect",
    description="Position actual value referring to axis' indirect measurement system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6204", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6213", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6086", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6087", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6218", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncAxisType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6039"])
ns0.vartypes.PropertyType(
    nodeId="ns=cnc;i=6223",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cnc;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Active"), description=o6.LocalizedText("Channel active", "en")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Interrupted"), description=o6.LocalizedText("Channel interrupted", "en")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Reset"), description=o6.LocalizedText("Channel resetting", "en")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cnc;i=6224",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cnc;i=3005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Stopped"), description=o6.LocalizedText("Spindle stopped", "en")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("InTargetArea"), description=o6.LocalizedText("Spindle reached commanded velocity", "en")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Accelerating"), description=o6.LocalizedText("Spindle accelerating", "en")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Decelerating"), description=o6.LocalizedText("Spindle decelerating", "en")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Parked"), description=o6.LocalizedText("Spindle configured but not active", "en")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cnc;i=6225",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cnc;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Stopped"), description=o6.LocalizedText("Channel program stopped", "en")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Running"), description=o6.LocalizedText("Channel program running", "en")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Waiting"), description=o6.LocalizedText("Channel program in waiting state", "en")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Interrupted"), description=o6.LocalizedText("Channel program interrupted", "en")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Canceled"), description=o6.LocalizedText("Channel program canceled", "en")),
    ],
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6041",
    browseName="ns=cnc;PosDirect",
    description="Position actual value referring to axis' direct measurement system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6226", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6227", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6088", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6089", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6228", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncAxisType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6041"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6247",
    browseName="ns=cnc;ZeroOffset",
    description="Active axis zero offset.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6248",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5066068, displayName=o6.LocalizedText("mm"), description=o6.LocalizedText("millimetre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6249", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6251",
    browseName="ns=cnc;ActLoad",
    description="Drive load actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6252",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6253", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6254",
    browseName="ns=cnc;ActPower",
    description="Drive power actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6255",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6256", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6257",
    browseName="ns=cnc;ActTorque",
    description="Drive torque actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6258",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6259", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6260",
    browseName="ns=cnc;CmdTorque",
    description="Drive torque setpoint value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6261",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6262", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0))),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6265",
    browseName="ns=cnc;PosDirect",
    description="Position actual value referring to axis' direct measurement system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6268", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6269", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6266", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6267", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6270", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6289",
    browseName="ns=cnc;ZeroOffset",
    description="Active axis zero offset.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6290",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5066068, displayName=o6.LocalizedText("mm"), description=o6.LocalizedText("millimetre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6291", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6293",
    browseName="ns=cnc;ActLoad",
    description="Drive load actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6294",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6295", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6296",
    browseName="ns=cnc;ActPower",
    description="Drive power actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6297",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6298", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6299",
    browseName="ns=cnc;ActTorque",
    description="Drive torque actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6300",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6301", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6302",
    browseName="ns=cnc;CmdTorque",
    description="Drive torque setpoint value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6303",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6304", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0))),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6307",
    browseName="ns=cnc;PosIndirect",
    description="Position actual value referring to axis' indirect measurement system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6310", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6311", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6308", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6309", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6312", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
x = cnc_objtypes.CncAxisType(
    nodeId="ns=cnc;i=5011",
    browseName="ns=cnc;X",
    references=[
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6232",
                browseName="ns=cnc;ActStatus",
                description="Actual axis state.",
                dataType=cnc_datypes.CncAxisStatus,
                value=cnc_datypes.CncAxisStatus.IN_POSITION,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6245",
                browseName="ns=cnc;IsReferenced",
                description="Axis reference state (true in case of successfully refereneced axis, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6246",
                browseName="ns=cnc;IsRotational",
                description="Axis type (true in case of rotational axis, in case of linear type or other false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6247"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6250",
                browseName="ns=cnc;ActChannel",
                description="NodeId of the channel object (CncChannelType) that administrates this drive to expose drive’s channel affiliation.",
                dataType=o6.NodeId,
                value=o6.NodeId("i=0"),
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6251"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6254"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6257"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6260"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6263",
                browseName="ns=cnc;IsInactive",
                description="Drive inactive state (true in case of inactive drive, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6264",
                browseName="ns=cnc;IsVirtual",
                description="Virtual axis (no hardware present; true in case of virtual axis, else fals).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6265"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6307"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6331",
    browseName="ns=cnc;ZeroOffset",
    description="Active axis zero offset.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6332",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5066068, displayName=o6.LocalizedText("mm"), description=o6.LocalizedText("millimetre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6333", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6335",
    browseName="ns=cnc;ActLoad",
    description="Drive load actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6336",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6337", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6338",
    browseName="ns=cnc;ActPower",
    description="Drive power actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6339",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6340", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6341",
    browseName="ns=cnc;ActTorque",
    description="Drive torque actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6342",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6343", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6344",
    browseName="ns=cnc;CmdTorque",
    description="Drive torque setpoint value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6345",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6346", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0))),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6349",
    browseName="ns=cnc;PosDirect",
    description="Position actual value referring to axis' direct measurement system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6352", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6353", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6350", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6351", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6354", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6373",
    browseName="ns=cnc;ZeroOffset",
    description="Active axis zero offset.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6374",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5066068, displayName=o6.LocalizedText("mm"), description=o6.LocalizedText("millimetre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6375", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6377",
    browseName="ns=cnc;ActLoad",
    description="Drive load actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6378",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6379", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6380",
    browseName="ns=cnc;ActPower",
    description="Drive power actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6381",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6382", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6383",
    browseName="ns=cnc;ActTorque",
    description="Drive torque actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6384",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6385", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6386",
    browseName="ns=cnc;CmdTorque",
    description="Drive torque setpoint value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6387",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6388", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0))),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6391",
    browseName="ns=cnc;PosIndirect",
    description="Position actual value referring to axis' indirect measurement system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6394", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6395", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6392", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6393", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6396", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
y = cnc_objtypes.CncAxisType(
    nodeId="ns=cnc;i=5012",
    browseName="ns=cnc;Y",
    references=[
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6274",
                browseName="ns=cnc;ActStatus",
                description="Actual axis state.",
                dataType=cnc_datypes.CncAxisStatus,
                value=cnc_datypes.CncAxisStatus.IN_POSITION,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6287",
                browseName="ns=cnc;IsReferenced",
                description="Axis reference state (true in case of successfully refereneced axis, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6288",
                browseName="ns=cnc;IsRotational",
                description="Axis type (true in case of rotational axis, in case of linear type or other false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6289"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6292",
                browseName="ns=cnc;ActChannel",
                description="NodeId of the channel object (CncChannelType) that administrates this drive to expose drive’s channel affiliation.",
                dataType=o6.NodeId,
                value=o6.NodeId("i=0"),
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6293"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6296"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6299"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6302"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6305",
                browseName="ns=cnc;IsInactive",
                description="Drive inactive state (true in case of inactive drive, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6306",
                browseName="ns=cnc;IsVirtual",
                description="Virtual axis (no hardware present; true in case of virtual axis, else fals).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6349"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6391"]),
    ],
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6399",
    browseName="ns=cnc;PosDirect",
    description="Position actual value referring to axis' direct measurement system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6402", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6403", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6400", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6401", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6404", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6421",
    browseName="ns=cnc;ZeroOffset",
    description="Active axis zero offset.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6422",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5066068, displayName=o6.LocalizedText("mm"), description=o6.LocalizedText("millimetre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6423", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6425",
    browseName="ns=cnc;ActLoad",
    description="Drive load actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6426",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6427", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6428",
    browseName="ns=cnc;ActPower",
    description="Drive power actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6429",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6430", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6431",
    browseName="ns=cnc;ActTorque",
    description="Drive torque actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6432",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6433", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6434",
    browseName="ns=cnc;CmdTorque",
    description="Drive torque setpoint value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6435",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6436", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0))),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6437",
    browseName="ns=cnc;PosIndirect",
    description="Position actual value referring to axis' indirect measurement system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6440", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6441", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6438", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6439", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6442", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
z = cnc_objtypes.CncAxisType(
    nodeId="ns=cnc;i=5013",
    browseName="ns=cnc;Z",
    references=[
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6316",
                browseName="ns=cnc;ActStatus",
                description="Actual axis state.",
                dataType=cnc_datypes.CncAxisStatus,
                value=cnc_datypes.CncAxisStatus.IN_POSITION,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6329",
                browseName="ns=cnc;IsReferenced",
                description="Axis reference state (true in case of successfully refereneced axis, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6330",
                browseName="ns=cnc;IsRotational",
                description="Axis type (true in case of rotational axis, in case of linear type or other false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6331"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6334",
                browseName="ns=cnc;ActChannel",
                description="NodeId of the channel object (CncChannelType) that administrates this drive to expose drive’s channel affiliation.",
                dataType=o6.NodeId,
                value=o6.NodeId("i=0"),
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6335"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6338"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6341"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6344"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6347",
                browseName="ns=cnc;IsInactive",
                description="Drive inactive state (true in case of inactive drive, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6348",
                browseName="ns=cnc;IsVirtual",
                description="Virtual axis (no hardware present; true in case of virtual axis, else fals).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6399"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6437"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6444",
    browseName="ns=cnc;CmdFeedrate",
    description="Feedrate setpoint value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6445",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4732977,
                    displayName=o6.LocalizedText("mm/min"),
                    description=o6.LocalizedText("millimetre per minute"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6453", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6459",
    browseName="ns=cnc;ZeroOffset",
    description="Active axis zero offset.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6460",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5066068, displayName=o6.LocalizedText("mm"), description=o6.LocalizedText("millimetre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6461", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6463",
    browseName="ns=cnc;ActLoad",
    description="Drive load actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6464",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6465", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6466",
    browseName="ns=cnc;ActPower",
    description="Drive power actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6467",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6468", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6469",
    browseName="ns=cnc;ActTorque",
    description="Drive torque actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6470",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6471", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6472",
    browseName="ns=cnc;CmdTorque",
    description="Drive torque setpoint value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6473",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6474", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0))),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6475",
    browseName="ns=cnc;PosDirect",
    description="Position actual value referring to axis' direct measurement system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6478", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6479", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6476", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6477", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6480", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6497",
    browseName="ns=cnc;ZeroOffset",
    description="Active axis zero offset.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6498",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5066068, displayName=o6.LocalizedText("mm"), description=o6.LocalizedText("millimetre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6499", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6501",
    browseName="ns=cnc;ActLoad",
    description="Drive load actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6502",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6503", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6504",
    browseName="ns=cnc;ActPower",
    description="Drive power actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6505",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6506", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6507",
    browseName="ns=cnc;ActTorque",
    description="Drive torque actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6508",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6509", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6510",
    browseName="ns=cnc;CmdTorque",
    description="Drive torque setpoint value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6511",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6512", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0))),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6513",
    browseName="ns=cnc;ActFeedrate",
    description="Feedrate actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6514",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4732977,
                    displayName=o6.LocalizedText("mm/min"),
                    description=o6.LocalizedText("millimetre per minute"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6515", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6520",
    browseName="ns=cnc;ActJogIncrement",
    description="Active JOG increment.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6521",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5066068, displayName=o6.LocalizedText("mm"), description=o6.LocalizedText("millimetre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6522", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6525",
    browseName="ns=cnc;ActOverride",
    description="Axis override actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6526",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6527", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6533",
    browseName="ns=cnc;CmdFeedrate",
    description="Feedrate setpoint value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6534",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4732977,
                    displayName=o6.LocalizedText("mm/min"),
                    description=o6.LocalizedText("millimetre per minute"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6535", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6536",
    browseName="ns=cnc;CmdOverride",
    description="Override setpoint value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6537",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6538", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6539",
    browseName="ns=cnc;DryRunFeed",
    description="Test feedrate.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6540",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4732977,
                    displayName=o6.LocalizedText("mm/min"),
                    description=o6.LocalizedText("millimetre per minute"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6541", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6546",
    browseName="ns=cnc;ActFeedrate",
    description="Feedrate actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6547",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4732977,
                    displayName=o6.LocalizedText("mm/min"),
                    description=o6.LocalizedText("millimetre per minute"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6548", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6553",
    browseName="ns=cnc;ActJogIncrement",
    description="Active JOG increment.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6554",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5066068, displayName=o6.LocalizedText("mm"), description=o6.LocalizedText("millimetre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6555", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6558",
    browseName="ns=cnc;ActOverride",
    description="Axis override actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6559",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6560", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6566",
    browseName="ns=cnc;CmdFeedrate",
    description="Feedrate setpoint value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6567",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4732977,
                    displayName=o6.LocalizedText("mm/min"),
                    description=o6.LocalizedText("millimetre per minute"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6568", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6569",
    browseName="ns=cnc;CmdOverride",
    description="Override setpoint value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6570",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6571", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6572",
    browseName="ns=cnc;DryRunFeed",
    description="Test feedrate.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6573",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4732977,
                    displayName=o6.LocalizedText("mm/min"),
                    description=o6.LocalizedText("millimetre per minute"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6574", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6584",
    browseName="ns=cnc;ActSpeed",
    description="Speed actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6585",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4405556,
                    displayName=o6.LocalizedText("min⁻¹"),
                    description=o6.LocalizedText("reciprocal minute"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6586", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6579",
    browseName="ns=cnc;AnglePos",
    description="Spindle angular position values in case of interpolated (position controlled) spindle movement. Returns zeros in case of regular spindle operation (velocity controlled).",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6592", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6593", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6580", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6581", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6594", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6598",
    browseName="ns=cnc;CmdSpeed",
    description="Speed setpoint value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6599",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4405556,
                    displayName=o6.LocalizedText("min⁻¹"),
                    description=o6.LocalizedText("reciprocal minute"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6600", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6602",
    browseName="ns=cnc;ActLoad",
    description="Drive load actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6603",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6604", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6605",
    browseName="ns=cnc;ActPower",
    description="Drive power actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6606",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6607", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6608",
    browseName="ns=cnc;ActTorque",
    description="Drive torque actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6609",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6610", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6611",
    browseName="ns=cnc;CmdTorque",
    description="Drive torque setpoint value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6612",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6613", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0))),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6596",
    browseName="ns=cnc;CmdOverride",
    description="Override setpoint value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6597",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6622", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6623",
    browseName="ns=cnc;DryRunFeed",
    description="Test feedrate.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6624",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4732977,
                    displayName=o6.LocalizedText("mm/min"),
                    description=o6.LocalizedText("millimetre per minute"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6625", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6630",
    browseName="ns=cnc;PosIndirect",
    description="Position actual value referring to axis' indirect measurement system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6633", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6634", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6631", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6632", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6635", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
x2 = cnc_objtypes.CncAxisType(
    nodeId="ns=cnc;i=5014",
    browseName="ns=cnc;X2",
    references=[
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6358",
                browseName="ns=cnc;ActStatus",
                description="Actual axis state.",
                dataType=cnc_datypes.CncAxisStatus,
                value=cnc_datypes.CncAxisStatus.IN_POSITION,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6371",
                browseName="ns=cnc;IsReferenced",
                description="Axis reference state (true in case of successfully refereneced axis, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6372",
                browseName="ns=cnc;IsRotational",
                description="Axis type (true in case of rotational axis, in case of linear type or other false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6373"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6376",
                browseName="ns=cnc;ActChannel",
                description="NodeId of the channel object (CncChannelType) that administrates this drive to expose drive’s channel affiliation.",
                dataType=o6.NodeId,
                value=o6.NodeId("i=0"),
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6377"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6380"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6383"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6386"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6389",
                browseName="ns=cnc;IsInactive",
                description="Drive inactive state (true in case of inactive drive, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6390",
                browseName="ns=cnc;IsVirtual",
                description="Virtual axis (no hardware present; true in case of virtual axis, else fals).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6475"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6630"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6651",
    browseName="ns=cnc;ZeroOffset",
    description="Active axis zero offset.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6652",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5066068, displayName=o6.LocalizedText("mm"), description=o6.LocalizedText("millimetre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6653", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6655",
    browseName="ns=cnc;ActLoad",
    description="Drive load actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6656",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6657", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6658",
    browseName="ns=cnc;ActPower",
    description="Drive power actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6659",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6660", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6661",
    browseName="ns=cnc;ActTorque",
    description="Drive torque actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6662",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6664", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6665",
    browseName="ns=cnc;CmdTorque",
    description="Drive torque setpoint value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6666",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6667", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0)
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6700",
    browseName="ns=cnc;ActOverride",
    description="Override actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6045", browseName="EngineeringUnits", modellingRule="Optional", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6701", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncSpindleType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6700"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6702",
    browseName="ns=cnc;CmdOverride",
    description="Override setpoint value.",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6706", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncSpindleType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6702"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6707",
    browseName="ns=cnc;ActOverride",
    description="Override actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6051", browseName="EngineeringUnits", modellingRule="Optional", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6708", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6710",
    browseName="ns=cnc;CmdOverride",
    description="Override setpoint value.",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6711", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6712",
    browseName="ns=cnc;ActFeedrate",
    description="Feedrate actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6713",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4732977,
                    displayName=o6.LocalizedText("mm/min"),
                    description=o6.LocalizedText("millimetre per minute"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6714", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6721",
    browseName="ns=cnc;ActJogIncrement",
    description="Active JOG increment.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6722",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5066068, displayName=o6.LocalizedText("mm"), description=o6.LocalizedText("millimetre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6723", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6733",
    browseName="ns=cnc;ZeroOffset",
    description="Active axis zero offset.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6734",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5066068, displayName=o6.LocalizedText("mm"), description=o6.LocalizedText("millimetre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6735", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6737",
    browseName="ns=cnc;ActLoad",
    description="Drive load actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6738",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6739", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6740",
    browseName="ns=cnc;ActPower",
    description="Drive power actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6741",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6742", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6743",
    browseName="ns=cnc;ActTorque",
    description="Drive torque actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6744",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6745", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6746",
    browseName="ns=cnc;CmdTorque",
    description="Drive torque setpoint value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6747",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6748", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0))),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6037",
    browseName="ns=cnc;PosTcpBcsA",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6830", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6882", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6052", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6053", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6054", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncChannelType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6037"])
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6058",
    browseName="ns=cnc;PosTcpBcsA",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6831", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6883", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6068", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6069", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6070", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6140",
    browseName="ns=cnc;PosTcpWcsX",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6832", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6884", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6160", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6171", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6209", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncChannelType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6140"])
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6159",
    browseName="ns=cnc;PosTcpBcsB",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6833", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6885", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6162", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6163", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6164", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncChannelType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6159"])
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6166",
    browseName="ns=cnc;PosTcpBcsC",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6834", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6886", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6167", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6178", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6184", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncChannelType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6166"])
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6168",
    browseName="ns=cnc;PosTcpBcsX",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6835", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6887", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6170", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6192", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6193", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncChannelType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6168"])
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6172",
    browseName="ns=cnc;PosTcpBcsY",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6836", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6888", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6181", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6203", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6229", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncChannelType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6172"])
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6173",
    browseName="ns=cnc;PosTcpWcsY",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6837", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6889", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6210", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6212", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6217", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncChannelType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6173"])
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6174",
    browseName="ns=cnc;PosTcpWcsZ",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6838", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6890", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6221", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6222", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6272", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncChannelType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6174"])
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6175",
    browseName="ns=cnc;PosTcpWcsA",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6839", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6891", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6190", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6191", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6239", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncChannelType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6175"])
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6176",
    browseName="ns=cnc;PosTcpWcsB",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6840", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6892", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6198", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6199", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6240", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncChannelType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6176"])
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6183",
    browseName="ns=cnc;PosTcpBcsZ",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6841", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6893", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6188", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6230", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6231", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncChannelType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6183"])
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6201",
    browseName="ns=cnc;PosTcpWcsC",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6842", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6894", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6202", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6241", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6271", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
o6.reference(cnc_objtypes.CncChannelType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=6201"])
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6273",
    browseName="ns=cnc;PosTcpBcsB",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6843", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6895", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6313", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6314", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6315", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6323",
    browseName="ns=cnc;PosTcpBcsC",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6844", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6896", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6324", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6325", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6355", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6356",
    browseName="ns=cnc;PosTcpBcsX",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6845", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6897", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6357", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6397", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6398", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6405",
    browseName="ns=cnc;PosTcpBcsY",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6846", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6898", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6406", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6407", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6415", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6416",
    browseName="ns=cnc;PosTcpBcsZ",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6847", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6899", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6417", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6443", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6454", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6455",
    browseName="ns=cnc;PosTcpWcsA",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6848", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6900", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6481", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6482", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6483", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6491",
    browseName="ns=cnc;PosTcpWcsB",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6849", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6901", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6492", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6493", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6516", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6544",
    browseName="ns=cnc;PosTcpWcsC",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6850", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6902", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6577", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6587", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6595", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6619",
    browseName="ns=cnc;PosTcpWcsX",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6851", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6903", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6628", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6638", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6639", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6640",
    browseName="ns=cnc;PosTcpWcsY",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6852", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6904", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6670", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6671", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6672", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6673",
    browseName="ns=cnc;PosTcpWcsZ",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6853", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6905", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6674", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6675", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6676", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_objtypes.CncChannelType(
    nodeId="ns=cnc;i=5003",
    browseName="ns=cnc;<CncChannel>",
    description="CNC channel object.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6017",
                browseName="ns=cnc;Id",
                description="Unique numeric channel identifier.",
                modellingRule="Mandatory",
                dataType=o6.UInt32,
                value=0,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6058"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6119"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6133",
                browseName="ns=cnc;ActProgramName",
                description="Name of active CNC program (main or subprogram).",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6137",
                browseName="ns=cnc;ActProgramFileOffset",
                description="File offset of active CNC program file (main or subprogram).",
                modellingRule="Optional",
                dataType=o6.UInt32,
                value=0,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6138",
                browseName="ns=cnc;ActGFunctions",
                description="Array of active G functions; there can be several G functions active at a time (modal and non-modal G functions).",
                modellingRule="Mandatory",
                dataType=o6.UInt32,
                valueRank=1,
                arrayDimensions=[0],
                value=[],
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6139"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6148",
                browseName="ns=cnc;ActMainProgramName",
                description="Name of active CNC main program.",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6149",
                browseName="ns=cnc;ActMFunctions",
                description="Array of active M functions: there can be several M functions active at a time (modal and non-modal M functions).",
                modellingRule="Mandatory",
                dataType=o6.UInt32,
                valueRank=1,
                arrayDimensions=[0],
                value=[],
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6150",
                browseName="ns=cnc;ActModalOffsetFunction",
                description="Active zero offset function.",
                modellingRule="Mandatory",
                dataType=o6.UInt32,
                value=0,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6151"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6273"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6281",
                browseName="ns=cnc;ActProgramBlock",
                description="Block of lines containing the previous, actual and subsequent lines of a CNC part program.",
                modellingRule="Mandatory",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[3],
                value=[],
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6282",
                browseName="ns=cnc;ActProgramLine",
                description="Line number of active CNC program (main or subprogram).",
                modellingRule="Optional",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6283",
                browseName="ns=cnc;ActProgramFile",
                description="Path of active CNC program file (main or subprogram).",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6323"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6356"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6365",
                browseName="ns=cnc;ActProgramStatus",
                description="Active channel program status",
                modellingRule="Mandatory",
                dataType=cnc_datypes.CncChannelProgramStatus,
                value=cnc_datypes.CncChannelProgramStatus.RUNNING,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6366",
                browseName="ns=cnc;ActStatus",
                description="Active status of channel.",
                modellingRule="Mandatory",
                dataType=cnc_datypes.CncChannelStatus,
                value=cnc_datypes.CncChannelStatus.RESET,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6367",
                browseName="ns=cnc;BlockMode",
                description="Block mode status (true in case of block mode is active, else false).",
                modellingRule="Mandatory",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6405"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6416"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6444"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6455"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6491"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6544"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6596"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6619"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6623"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6626",
                browseName="ns=cnc;FeedHold",
                description="Feed status (true in case of feed hold active, else false).",
                modellingRule="Mandatory",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6629",
                browseName="ns=cnc;ToolId",
                description="ID of active tool; returns zero if no tool is present.",
                modellingRule="Mandatory",
                dataType=o6.UInt32,
                value=0,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6640"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6673"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6683",
                browseName="ns=cnc;ActMainProgramFile",
                description="Path of active CNC main program.",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6689",
                browseName="ns=cnc;ActMainProgramLine",
                description="Line number of active CNC main program.",
                modellingRule="Optional",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6695",
                browseName="ns=cnc;ActMainProgramFileOffset",
                description="File offset of active CNC main program file.",
                modellingRule="Optional",
                dataType=o6.UInt32,
                value=0,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6782",
                browseName="ns=cnc;ActOperationMode",
                description="Channel's active mode of operation.",
                modellingRule="Mandatory",
                dataType=cnc_datypes.CncOperationMode,
                value=cnc_datypes.CncOperationMode.MANUAL,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6816",
                browseName="ns=cnc;CmdOperationMode",
                description="Channel’s mode of operation setpoint value.",
                modellingRule="Mandatory",
                dataType=cnc_datypes.CncOperationMode,
                value=cnc_datypes.CncOperationMode.MANUAL,
                accessLevel=3,
            )
        ),
    ],
)
o6.reference(cnc_objtypes.CncChannelListType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=5003"])
o6.reference(o6.ns["ns=cnc;i=5003"], "i=41", "i=2133")
o6.reference(o6.ns["ns=cnc;i=5003"], "i=41", cnc_objtypes.CncMessageType)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6071",
    browseName="ns=cnc;PosTcpBcsA",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6855", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6906", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6080", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6090", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6136", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6677",
    browseName="ns=cnc;PosTcpBcsB",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6856", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6907", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6678", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6679", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6680", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6681",
    browseName="ns=cnc;PosTcpBcsC",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6857", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6908", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6684", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6685", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6690", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6691",
    browseName="ns=cnc;PosTcpBcsX",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6858", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6909", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6696", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6697", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6703", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6704",
    browseName="ns=cnc;PosTcpBcsY",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6859", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6910", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6705", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6709", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6727", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6751",
    browseName="ns=cnc;PosTcpBcsZ",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6860", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6911", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6752", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6753", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6754", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6755",
    browseName="ns=cnc;PosTcpWcsA",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6861", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6912", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6756", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6757", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6758", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6759",
    browseName="ns=cnc;PosTcpWcsB",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6863", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6913", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6760", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6761", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6762", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6763",
    browseName="ns=cnc;PosTcpWcsC",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6864", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6914", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6764", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6765", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6766", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6767",
    browseName="ns=cnc;PosTcpWcsX",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6866", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6915", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6768", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6769", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6770", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6771",
    browseName="ns=cnc;PosTcpWcsY",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6867", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6916", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6772", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6773", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6774", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6775",
    browseName="ns=cnc;PosTcpWcsZ",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6868", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6917", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6776", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6777", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6778", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6141",
    browseName="ns=cnc;PosTcpBcsA",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6869", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6918", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6143", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6156", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6158", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6779",
    browseName="ns=cnc;PosTcpBcsB",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6870", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6919", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6780", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6781", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6783", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6784",
    browseName="ns=cnc;PosTcpBcsC",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6871", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6920", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6785", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6786", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6787", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6788",
    browseName="ns=cnc;PosTcpBcsX",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6872", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6921", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6789", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6790", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6791", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6792",
    browseName="ns=cnc;PosTcpBcsY",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6873", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6922", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6793", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6794", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6795", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6796",
    browseName="ns=cnc;PosTcpBcsZ",
    description="Actual position of the tool center point in machine’s Cartesian base coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6874", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6923", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6797", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6798", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6799", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6800",
    browseName="ns=cnc;PosTcpWcsA",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6875", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6924", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6801", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6802", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6803", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6804",
    browseName="ns=cnc;PosTcpWcsB",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6876", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6925", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6805", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6806", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6807", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6808",
    browseName="ns=cnc;PosTcpWcsC",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6877", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6926", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6809", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6810", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6811", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6812",
    browseName="ns=cnc;PosTcpWcsX",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6878", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6927", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6813", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6814", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6815", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6817",
    browseName="ns=cnc;PosTcpWcsY",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6879", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6928", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6818", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6819", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6820", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6821",
    browseName="ns=cnc;PosTcpWcsZ",
    description="Actual position of the tool center point in machine’s Cartesian workpiece coordinate system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6880", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6929", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6822", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6823", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6824", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6825",
    browseName="ns=cnc;PosDirect",
    description="Position actual value referring to axis' direct measurement system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6828", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6930", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6826", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6827", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6931", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6932",
    browseName="ns=cnc;PosIndirect",
    description="Position actual value referring to axis' indirect measurement system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6935", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6936", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6933", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6934", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6937", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
y2 = cnc_objtypes.CncAxisType(
    nodeId="ns=cnc;i=5015",
    browseName="ns=cnc;Y2",
    references=[
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6549",
                browseName="ns=cnc;ActStatus",
                description="Actual axis state.",
                dataType=cnc_datypes.CncAxisStatus,
                value=cnc_datypes.CncAxisStatus.IN_POSITION,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6731",
                browseName="ns=cnc;IsReferenced",
                description="Axis reference state (true in case of successfully refereneced axis, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6732",
                browseName="ns=cnc;IsRotational",
                description="Axis type (true in case of rotational axis, in case of linear type or other false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6733"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6736",
                browseName="ns=cnc;ActChannel",
                description="NodeId of the channel object (CncChannelType) that administrates this drive to expose drive’s channel affiliation.",
                dataType=o6.NodeId,
                value=o6.NodeId("i=0"),
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6737"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6740"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6743"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6746"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6749",
                browseName="ns=cnc;IsInactive",
                description="Drive inactive state (true in case of inactive drive, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6750",
                browseName="ns=cnc;IsVirtual",
                description="Virtual axis (no hardware present; true in case of virtual axis, else fals).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6825"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6932"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6948",
    browseName="ns=cnc;CmdFeedrate",
    description="feedrate setpoint value",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6949",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4732977,
                    displayName=o6.LocalizedText("mm/min"),
                    description=o6.LocalizedText("millimetre per minute"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6950", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=6951",
    browseName="ns=cnc;DryRunFeed",
    description="test feedrate",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=6952",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4732977,
                    displayName=o6.LocalizedText("mm/min"),
                    description=o6.LocalizedText("millimetre per minute"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6953", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6938",
    browseName="ns=cnc;PosDirect",
    description="Position actual value referring to axis' direct measurement system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6941", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6942", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6939", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6940", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6955", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_objtypes.CncSpindleType(
    nodeId="ns=cnc;i=5002",
    browseName="ns=cnc;<CncSpindle>",
    description="CNC spindle object.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6076", browseName="ns=cnc;ActGear", description="Gear stage actual value.", modellingRule="Mandatory", dataType=o6.UInt32, value=0, accessLevel=3
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6077"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6081",
                browseName="ns=cnc;ActStatus",
                description="Actual spindle state.",
                modellingRule="Mandatory",
                dataType=cnc_datypes.CncSpindleStatus,
                value=cnc_datypes.CncSpindleStatus.STOPPED,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6082",
                browseName="ns=cnc;ActTurnDirection",
                description="Turn direction actual value.",
                modellingRule="Mandatory",
                dataType=cnc_datypes.CncSpindleTurnDirection,
                value=cnc_datypes.CncSpindleTurnDirection.NONE,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6091", browseName="ns=cnc;CmdGear", description="Gear stage setpoint value.", modellingRule="Mandatory", dataType=o6.UInt32, value=0, accessLevel=3
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6096"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6104",
                browseName="ns=cnc;ActChannel",
                description="NodeId of the channel object (CncChannelType) that administrates this drive to expose drive’s channel affiliation.",
                modellingRule="Mandatory",
                dataType=o6.NodeId,
                value=o6.NodeId("i=0"),
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6105"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6108"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6111"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6114"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6117",
                browseName="ns=cnc;IsInactive",
                description="Drive inactive state (true in case of inactive drive, else false).",
                modellingRule="Mandatory",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6118",
                browseName="ns=cnc;IsVirtual",
                description="Virtual axis (no hardware present; true in case of virtual axis, else fals).",
                modellingRule="Mandatory",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6124"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(nodeId="ns=cnc;i=6576", browseName="ns=cnc;ActOperationMode", modellingRule="Mandatory", dataType=cnc_datypes.CncOperationMode, accessLevel=3)
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(nodeId="ns=cnc;i=6627", browseName="ns=cnc;CmdOperationMode", modellingRule="Mandatory", dataType=cnc_datypes.CncOperationMode, accessLevel=3)
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6707"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6710"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6712"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6715",
                browseName="ns=cnc;ActMainProgramFile",
                description="Path of active CNC main program.",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6716",
                browseName="ns=cnc;ActMainProgramFileOffset",
                description="File offset of active CNC main program file.",
                modellingRule="Mandatory",
                dataType=o6.UInt32,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6717",
                browseName="ns=cnc;ActMainProgramLine",
                description="Line number of active CNC main program.",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="\n      ",
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6718",
                browseName="ns=cnc;ActProgramName",
                description="Name of active CNC program (main or subprogram).",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="\n      ",
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6719",
                browseName="ns=cnc;ActProgramFileOffset",
                description="File offset of active CNC program file (main or subprogram).",
                modellingRule="Mandatory",
                dataType=o6.UInt32,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6720",
                browseName="ns=cnc;ActGFunctions",
                description="Active G function.",
                modellingRule="Mandatory",
                dataType=o6.UInt32,
                valueRank=1,
                arrayDimensions=[0],
                value=[],
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6721"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6724",
                browseName="ns=cnc;ActMainProgramName",
                description="Name of active CNC main program.",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="\n      ",
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6725",
                browseName="ns=cnc;ActMFunctions",
                description="Active M function.",
                modellingRule="Mandatory",
                dataType=o6.UInt32,
                valueRank=1,
                arrayDimensions=[0],
                value=[],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6726",
                browseName="ns=cnc;ActModalOffsetFunction",
                description="active zero offset function",
                modellingRule="Mandatory",
                dataType=o6.UInt32,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6943",
                browseName="ns=cnc;ActProgramBlock",
                description="previous, actual and subsequent CNC program lines",
                modellingRule="Mandatory",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[3],
                value=[],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6944",
                browseName="ns=cnc;ActProgramLine",
                description="Line number of active CNC program (main or subprogram).",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="\n      ",
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6945",
                browseName="ns=cnc;ActProgramFile",
                description="Path of active CNC program file (main or subprogram).",
                modellingRule="Mandatory",
                dataType=o6.String,
                value="\n      ",
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6946",
                browseName="ns=cnc;ActProgramStatus",
                description="Active channel program status",
                displayName="ActProgStatus",
                modellingRule="Mandatory",
                dataType=cnc_datypes.CncChannelProgramStatus,
                value=cnc_datypes.CncChannelProgramStatus.RUNNING,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6947", browseName="ns=cnc;BlockMode", description="block mode active", modellingRule="Mandatory", dataType=o6.Boolean, value=False
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6948"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6951"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6954", browseName="ns=cnc;FeedHold", description="feed hold active", modellingRule="Mandatory", dataType=o6.Boolean, value=False
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(nodeId="ns=cnc;i=6957", browseName="ns=cnc;ToolId", description="active tool ID", modellingRule="Mandatory", dataType=o6.UInt32, value=0)
        ),
    ],
)
o6.reference(cnc_objtypes.CncSpindleListType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=5002"])
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6956",
    browseName="ns=cnc;PosIndirect",
    description="Position actual value referring to axis' indirect measurement system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6960", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6961", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6958", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6959", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=6962", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_objtypes.CncAxisType(
    nodeId="ns=cnc;i=5019",
    browseName="ns=cnc;<CncAxis>",
    description="CNC axis object.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6636",
                browseName="ns=cnc;ActStatus",
                description="Actual axis state.",
                modellingRule="Mandatory",
                dataType=cnc_datypes.CncAxisStatus,
                value=cnc_datypes.CncAxisStatus.IN_POSITION,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6649",
                browseName="ns=cnc;IsReferenced",
                description="Axis reference state (true in case of successfully refereneced axis, else false).",
                modellingRule="Mandatory",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6650",
                browseName="ns=cnc;IsRotational",
                description="Axis type (true in case of rotational axis, in case of linear type or other false).",
                modellingRule="Mandatory",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6651"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6654",
                browseName="ns=cnc;ActChannel",
                description="NodeId of the channel object (CncChannelType) that administrates this drive to expose drive’s channel affiliation.",
                modellingRule="Mandatory",
                dataType=o6.NodeId,
                value=o6.NodeId("i=0"),
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6655"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6658"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6661"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6665"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6668",
                browseName="ns=cnc;IsInactive",
                description="Drive inactive state (true in case of inactive drive, else false).",
                modellingRule="Mandatory",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6669",
                browseName="ns=cnc;IsVirtual",
                description="Virtual axis (no hardware present; true in case of virtual axis, else fals).",
                modellingRule="Mandatory",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6938"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6956"]),
    ],
)
o6.reference(cnc_objtypes.CncAxisListType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=5019"])
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6963",
    browseName="ns=cnc;PosDirect",
    description="Position actual value referring to axis' direct measurement system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6966", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6967", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6964", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6965", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6968", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6969",
    browseName="ns=cnc;PosIndirect",
    description="Position actual value referring to axis' indirect measurement system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6972", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6973", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6970", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6971", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6974", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
x_2 = cnc_objtypes.CncAxisType(
    nodeId="ns=cnc;i=5020",
    browseName="ns=cnc;X",
    description="X Axis",
    references=[
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6185",
                browseName="ns=cnc;IsReferenced",
                description="Axis reference state (true in case of successfully refereneced axis, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6194",
                browseName="ns=cnc;IsVirtual",
                description="Virtual axis (no hardware present; true in case of virtual axis, else fals).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6205",
                browseName="ns=cnc;IsInactive",
                description="Drive inactive state (true in case of inactive drive, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6214",
                browseName="ns=cnc;IsRotational",
                description="Axis type (true in case of rotational axis, in case of linear type or other false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6408",
                browseName="ns=cnc;ActStatus",
                description="Actual axis state.",
                dataType=cnc_datypes.CncAxisStatus,
                value=cnc_datypes.CncAxisStatus.IN_POSITION,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6421"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6424",
                browseName="ns=cnc;ActChannel",
                description="NodeId of the channel object (CncChannelType) that administrates this drive to expose drive’s channel affiliation.",
                dataType=o6.NodeId,
                value=o6.NodeId("i=0"),
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6425"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6428"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6431"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6434"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6963"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6969"]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cnc;i=6976",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=cnc;i=3004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("InPosition"), description=o6.LocalizedText("Axis reached commanded position", "en")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Moving"), description=o6.LocalizedText("Axis is moving to reach commanded position", "en")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Parked"), description=o6.LocalizedText("Axis is configured but not active", "en")),
    ],
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6975",
    browseName="ns=cnc;PosDirect",
    description="Position actual value referring to axis' direct measurement system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6979", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6980", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6977", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6978", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6981", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6982",
    browseName="ns=cnc;PosIndirect",
    description="Position actual value referring to axis' indirect measurement system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6985", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6986", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6983", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6984", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6987", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
y_2 = cnc_objtypes.CncAxisType(
    nodeId="ns=cnc;i=5021",
    browseName="ns=cnc;Y",
    description="Y Axis",
    references=[
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6186",
                browseName="ns=cnc;IsReferenced",
                description="Axis reference state (true in case of successfully refereneced axis, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6195",
                browseName="ns=cnc;IsVirtual",
                description="Virtual axis (no hardware present; true in case of virtual axis, else fals).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6206",
                browseName="ns=cnc;IsInactive",
                description="Drive inactive state (true in case of inactive drive, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6215",
                browseName="ns=cnc;IsRotational",
                description="Axis type (true in case of rotational axis, in case of linear type or other false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6446",
                browseName="ns=cnc;ActStatus",
                description="Actual axis state.",
                dataType=cnc_datypes.CncAxisStatus,
                value=cnc_datypes.CncAxisStatus.IN_POSITION,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6459"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6462",
                browseName="ns=cnc;ActChannel",
                description="NodeId of the channel object (CncChannelType) that administrates this drive to expose drive’s channel affiliation.",
                dataType=o6.NodeId,
                value=o6.NodeId("i=0"),
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6463"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6466"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6469"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6472"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6975"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6982"]),
    ],
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6988",
    browseName="ns=cnc;PosDirect",
    description="Position actual value referring to axis' direct measurement system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6991", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6992", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6989", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6990", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6993", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=6994",
    browseName="ns=cnc;PosIndirect",
    description="Position actual value referring to axis' indirect measurement system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6997", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6998", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6995", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6996", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=6999", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
z_2 = cnc_objtypes.CncAxisType(
    nodeId="ns=cnc;i=5022",
    browseName="ns=cnc;Z",
    description="Z Axis",
    references=[
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6187",
                browseName="ns=cnc;IsReferenced",
                description="Axis reference state (true in case of successfully refereneced axis, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6196",
                browseName="ns=cnc;IsVirtual",
                description="Virtual axis (no hardware present; true in case of virtual axis, else fals).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6207",
                browseName="ns=cnc;IsInactive",
                description="Drive inactive state (true in case of inactive drive, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6216",
                browseName="ns=cnc;IsRotational",
                description="Axis type (true in case of rotational axis, in case of linear type or other false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6484",
                browseName="ns=cnc;ActStatus",
                description="Actual axis state.",
                dataType=cnc_datypes.CncAxisStatus,
                value=cnc_datypes.CncAxisStatus.IN_POSITION,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6497"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6500",
                browseName="ns=cnc;ActChannel",
                description="NodeId of the channel object (CncChannelType) that administrates this drive to expose drive’s channel affiliation.",
                dataType=o6.NodeId,
                value=o6.NodeId("i=0"),
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6501"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6504"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6507"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6510"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6988"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6994"]),
    ],
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=7000",
    browseName="ns=cnc;PosDirect",
    description="Position actual value referring to axis' direct measurement system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7003", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7004", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=7001", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=7002", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=7005", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=7006",
    browseName="ns=cnc;PosIndirect",
    description="Position actual value referring to axis' indirect measurement system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7009", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7010", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=7007", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=7008", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=7011", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=7012",
    browseName="ns=cnc;AnglePos",
    description="Spindle angular position values in case of interpolated (position controlled) spindle movement. Returns zeros in case of regular spindle operation (velocity controlled).",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7015", browseName="ns=cnc;EngineeringUnits", modellingRule="Mandatory", dataType=ns0.datatypes.EUInformation, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7016", browseName="ns=cnc;EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=7013", browseName="ns=cnc;ActPos", description="Position current value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=7014", browseName="ns=cnc;CmdPos", description="Position setpoint value.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;i=7017", browseName="ns=cnc;RemDist", description="Remaining distance to go.", modellingRule="Mandatory", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=7028",
    browseName="ns=cnc;ActOverride",
    description="Override actual value.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7029", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=7030",
    browseName="ns=cnc;CmdOverride",
    description="Override setpoint value.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7031", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
q = cnc_objtypes.CncSpindleType(
    nodeId="ns=cnc;i=5025",
    browseName="ns=cnc;Q",
    references=[
        o6.hasComponent(
            ns0.vartypes.DataItemType(nodeId="ns=cnc;i=6144", browseName="ns=cnc;CmdGear", description="Gear stage setpoint value.", dataType=o6.UInt32, value=0, accessLevel=3)
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6147",
                browseName="ns=cnc;ActTurnDirection",
                description="Turn direction actual value.",
                dataType=cnc_datypes.CncSpindleTurnDirection,
                value=cnc_datypes.CncSpindleTurnDirection.NONE,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6197",
                browseName="ns=cnc;IsVirtual",
                description="Virtual axis (no hardware present; true in case of virtual axis, else fals).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6208",
                browseName="ns=cnc;IsInactive",
                description="Drive inactive state (true in case of inactive drive, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6579"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(nodeId="ns=cnc;i=6583", browseName="ns=cnc;ActGear", description="Gear stage actual value.", dataType=o6.UInt32, value=0, accessLevel=3)
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6584"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6588",
                browseName="ns=cnc;ActStatus",
                description="Actual spindle state.",
                dataType=cnc_datypes.CncSpindleStatus,
                value=cnc_datypes.CncSpindleStatus.STOPPED,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6598"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6601",
                browseName="ns=cnc;ActChannel",
                description="NodeId of the channel object (CncChannelType) that administrates this drive to expose drive’s channel affiliation.",
                dataType=o6.NodeId,
                value=o6.NodeId("i=0"),
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6602"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6605"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6608"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6611"]),
        o6.hasComponent(o6.ns["ns=cnc;i=7028"]),
        o6.hasComponent(o6.ns["ns=cnc;i=7030"]),
    ],
)
channel_1 = cnc_objtypes.CncChannelType(
    nodeId="ns=cnc;i=5023",
    browseName="ns=cnc;Channel_1",
    references=[
        o6.organizes(x_2),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6019", browseName="ns=cnc;Id", description="Unique numeric channel identifier.", dataType=o6.UInt32, value=0, accessLevel=3)
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6071"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6179",
                browseName="ns=cnc;ActMFunctions",
                description="Array of active M functions: there can be several M functions active at a time (modal and non-modal M functions).",
                dataType=o6.UInt32,
                valueRank=1,
                arrayDimensions=[0],
                value=[],
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6219",
                browseName="ns=cnc;ActProgramStatus",
                description="Active channel program status",
                dataType=cnc_datypes.CncChannelProgramStatus,
                value=cnc_datypes.CncChannelProgramStatus.RUNNING,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6513"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6517",
                browseName="ns=cnc;ActProgramName",
                description="Name of active CNC program (main or subprogram).",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6518",
                browseName="ns=cnc;ActProgramFileOffset",
                description="File offset of active CNC program file (main or subprogram).",
                dataType=o6.UInt32,
                value=0,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6519",
                browseName="ns=cnc;ActGFunctions",
                description="Array of active G functions; there can be several G functions active at a time (modal and non-modal G functions).",
                dataType=o6.UInt32,
                valueRank=1,
                arrayDimensions=[0],
                value=[],
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6520"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6523", browseName="ns=cnc;ActMainProgramName", description="Name of active CNC main program.", dataType=o6.String, value="\n      ", accessLevel=3
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6524", browseName="ns=cnc;ActModalOffsetFunction", description="Active zero offset function.", dataType=o6.UInt32, value=0, accessLevel=3
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6525"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6528",
                browseName="ns=cnc;ActProgramBlock",
                description="Block of lines containing the previous, actual and subsequent lines of a CNC part program.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[3],
                value=[],
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6529",
                browseName="ns=cnc;ActProgramLine",
                description="Line number of active CNC program (main or subprogram).",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6530",
                browseName="ns=cnc;ActProgramFile",
                description="Path of active CNC program file (main or subprogram).",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6531",
                browseName="ns=cnc;ActStatus",
                description="Active status of channel.",
                dataType=cnc_datypes.CncChannelStatus,
                value=cnc_datypes.CncChannelStatus.RESET,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6532",
                browseName="ns=cnc;BlockMode",
                description="Block mode status (true in case of block mode is active, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6533"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6536"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6539"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6542",
                browseName="ns=cnc;FeedHold",
                description="Feed status (true in case of feed hold active, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6545", browseName="ns=cnc;ToolId", description="ID of active tool; returns zero if no tool is present.", dataType=o6.UInt32, value=0, accessLevel=3
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6677"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6681"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6686", browseName="ns=cnc;ActMainProgramFile", description="Path of active CNC main program.", dataType=o6.String, value="\n      ", accessLevel=3
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6691"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6692",
                browseName="ns=cnc;ActMainProgramLine",
                description="Line number of active CNC main program.",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6698",
                browseName="ns=cnc;ActMainProgramFileOffset",
                description="File offset of active CNC main program file.",
                dataType=o6.UInt32,
                value=0,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6704"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6751"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6755"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6759"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6763"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6767"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6771"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6775"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7098",
                browseName="ns=cnc;ActOperationMode",
                description="Channel's active mode of operation.",
                dataType=cnc_datypes.CncOperationMode,
                value=cnc_datypes.CncOperationMode.MANUAL,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7100",
                browseName="ns=cnc;CmdOperationMode",
                description="Channel’s mode of operation setpoint value.",
                dataType=cnc_datypes.CncOperationMode,
                value=cnc_datypes.CncOperationMode.MANUAL,
                accessLevel=3,
            )
        ),
    ],
)
o6.reference(channel_1, "i=41", "i=2133")
o6.reference(channel_1, "i=41", cnc_objtypes.CncMessageType)
channel_2 = cnc_objtypes.CncChannelType(
    nodeId="ns=cnc;i=5024",
    browseName="ns=cnc;Channel_2",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6020", browseName="ns=cnc;Id", description="Unique numeric channel identifier.", dataType=o6.UInt32, value=0, accessLevel=3)
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6141"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6180",
                browseName="ns=cnc;ActMFunctions",
                description="Array of active M functions: there can be several M functions active at a time (modal and non-modal M functions).",
                dataType=o6.UInt32,
                valueRank=1,
                arrayDimensions=[0],
                value=[],
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6220",
                browseName="ns=cnc;ActProgramStatus",
                description="Active channel program status",
                dataType=cnc_datypes.CncChannelProgramStatus,
                value=cnc_datypes.CncChannelProgramStatus.RUNNING,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6546"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6550",
                browseName="ns=cnc;ActProgramName",
                description="Name of active CNC program (main or subprogram).",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6551",
                browseName="ns=cnc;ActProgramFileOffset",
                description="File offset of active CNC program file (main or subprogram).",
                dataType=o6.UInt32,
                value=0,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6552",
                browseName="ns=cnc;ActGFunctions",
                description="Array of active G functions; there can be several G functions active at a time (modal and non-modal G functions).",
                dataType=o6.UInt32,
                valueRank=1,
                arrayDimensions=[0],
                value=[],
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6553"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6556", browseName="ns=cnc;ActMainProgramName", description="Name of active CNC main program.", dataType=o6.String, value="\n      ", accessLevel=3
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6557", browseName="ns=cnc;ActModalOffsetFunction", description="Active zero offset function.", dataType=o6.UInt32, value=0, accessLevel=3
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6558"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6561",
                browseName="ns=cnc;ActProgramBlock",
                description="Block of lines containing the previous, actual and subsequent lines of a CNC part program.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[3],
                value=[],
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6562",
                browseName="ns=cnc;ActProgramLine",
                description="Line number of active CNC program (main or subprogram).",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6563",
                browseName="ns=cnc;ActProgramFile",
                description="Path of active CNC program file (main or subprogram).",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6564",
                browseName="ns=cnc;ActStatus",
                description="Active status of channel.",
                dataType=cnc_datypes.CncChannelStatus,
                value=cnc_datypes.CncChannelStatus.RESET,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6565",
                browseName="ns=cnc;BlockMode",
                description="Block mode status (true in case of block mode is active, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6566"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6569"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6572"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6575",
                browseName="ns=cnc;FeedHold",
                description="Feed status (true in case of feed hold active, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6578", browseName="ns=cnc;ToolId", description="ID of active tool; returns zero if no tool is present.", dataType=o6.UInt32, value=0, accessLevel=3
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6687", browseName="ns=cnc;ActMainProgramFile", description="Path of active CNC main program.", dataType=o6.String, value="\n      ", accessLevel=3
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6693",
                browseName="ns=cnc;ActMainProgramLine",
                description="Line number of active CNC main program.",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=6699",
                browseName="ns=cnc;ActMainProgramFileOffset",
                description="File offset of active CNC main program file.",
                dataType=o6.UInt32,
                value=0,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=6779"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6784"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6788"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6792"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6796"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6800"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6804"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6808"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6812"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6817"]),
        o6.hasComponent(o6.ns["ns=cnc;i=6821"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7101",
                browseName="ns=cnc;ActOperationMode",
                description="Channel's active mode of operation.",
                dataType=cnc_datypes.CncOperationMode,
                value=cnc_datypes.CncOperationMode.MANUAL,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7103",
                browseName="ns=cnc;CmdOperationMode",
                description="Channel’s mode of operation setpoint value.",
                dataType=cnc_datypes.CncOperationMode,
                value=cnc_datypes.CncOperationMode.MANUAL,
                accessLevel=3,
            )
        ),
    ],
)
o6.reference(channel_2, "i=41", "i=2133")
o6.reference(channel_2, "i=41", cnc_objtypes.CncMessageType)
ns0.vartypes.PropertyType(
    nodeId="ns=cnc;i=7106",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=cnc;i=3006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("Manual"), o6.LocalizedText("MDA"), o6.LocalizedText("Automatic")],
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=7123",
    browseName="ns=cnc;PosDirect",
    description="Position actual value referring to axis' direct measurement system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7126", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7127", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=7124", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=7125", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=7128", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;i=7129",
    browseName="ns=cnc;PosIndirect",
    description="Position actual value referring to axis' indirect measurement system.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7133", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7134", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=7130", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=7131", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=cnc;i=7135", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0)
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=7136",
    browseName="ns=cnc;ZeroOffset",
    description="Active axis zero offset.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=7137",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5066068, displayName=o6.LocalizedText("mm"), description=o6.LocalizedText("millimetre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7138", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=7144",
    browseName="ns=cnc;ZeroOffset",
    description="Active axis zero offset.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=7145",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5066068, displayName=o6.LocalizedText("mm"), description=o6.LocalizedText("millimetre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7146", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=7148",
    browseName="ns=cnc;ActLoad",
    description="Drive load actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=7149",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7150", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=7151",
    browseName="ns=cnc;ActPower",
    description="Drive power actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=7152",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7153", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=7154",
    browseName="ns=cnc;ActTorque",
    description="Drive torque actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=7155",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7156", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=7157",
    browseName="ns=cnc;CmdTorque",
    description="Drive torque setpoint value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=7158",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=7159", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0)
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
cnc_objtypes.CncAxisType(
    nodeId="ns=cnc;i=5029",
    browseName="ns=cnc;<CncAxis>",
    description="Optional place holder for CNC axis objects.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=cnc;i=7000"]),
        o6.hasComponent(o6.ns["ns=cnc;i=7006"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7132",
                browseName="ns=cnc;ActStatus",
                description="Actual axis state.",
                modellingRule="Mandatory",
                dataType=cnc_datypes.CncAxisStatus,
                value=cnc_datypes.CncAxisStatus.IN_POSITION,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7142",
                browseName="ns=cnc;IsReferenced",
                description="Axis reference state (true in case of successfully refereneced axis, else false).",
                modellingRule="Mandatory",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7143",
                browseName="ns=cnc;IsRotational",
                description="Axis type (true in case of rotational axis, in case of linear type or other false).",
                modellingRule="Mandatory",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=7144"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7147",
                browseName="ns=cnc;ActChannel",
                description="NodeId of the channel object (CncChannelType) that administrates this drive to expose drive’s channel affiliation.",
                modellingRule="Mandatory",
                dataType=o6.NodeId,
                value=o6.NodeId("i=0"),
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=7148"]),
        o6.hasComponent(o6.ns["ns=cnc;i=7151"]),
        o6.hasComponent(o6.ns["ns=cnc;i=7154"]),
        o6.hasComponent(o6.ns["ns=cnc;i=7157"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7160",
                browseName="ns=cnc;IsInactive",
                description="Drive inactive state (true in case of inactive drive, else false).",
                modellingRule="Mandatory",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7161",
                browseName="ns=cnc;IsVirtual",
                description="Virtual axis (no hardware present; true in case of virtual axis, else fals).",
                modellingRule="Mandatory",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
    ],
)
o6.reference(cnc_objtypes.CncChannelType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=5029"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=7140",
    browseName="ns=cnc;ActLoad",
    description="Drive load actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=7141",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7162", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=7167",
    browseName="ns=cnc;ActOverride",
    description="Override actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6057", browseName="EngineeringUnits", modellingRule="Optional", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7168", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=7169",
    browseName="ns=cnc;ActSpeed",
    description="Speed actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=7170",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4405556,
                    displayName=o6.LocalizedText("min⁻¹"),
                    description=o6.LocalizedText("reciprocal minute"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7171", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=7163",
    browseName="ns=cnc;ActPower",
    description="Drive power actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=7164",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7172", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=7175",
    browseName="ns=cnc;ActTorque",
    description="Drive torque actual value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=7176",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7177", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=7179",
    browseName="ns=cnc;CmdOverride",
    description="Override setpoint value.",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7180", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=7181",
    browseName="ns=cnc;CmdSpeed",
    description="Speed setpoint value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=7182",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4405556,
                    displayName=o6.LocalizedText("min⁻¹"),
                    description=o6.LocalizedText("reciprocal minute"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7183", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=7185",
    browseName="ns=cnc;ActLoad",
    description="Drive load actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=7186",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7187", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=7188",
    browseName="ns=cnc;ActPower",
    description="Drive power actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=7189",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7190", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=7191",
    browseName="ns=cnc;ActTorque",
    description="Drive torque actual value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=7192",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7193", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=7194",
    browseName="ns=cnc;CmdTorque",
    description="Drive torque setpoint value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=7195",
                browseName="EngineeringUnits",
                modellingRule="Mandatory",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=7196", browseName="EURange", modellingRule="Mandatory", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0)
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
cnc_objtypes.CncSpindleType(
    nodeId="ns=cnc;i=5030",
    browseName="ns=cnc;<CncSpindle>",
    description="Optional place holder for CNC spindle objects.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=cnc;i=7012"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7166", browseName="ns=cnc;ActGear", description="Gear stage actual value.", modellingRule="Mandatory", dataType=o6.UInt32, value=0, accessLevel=3
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=7167"]),
        o6.hasComponent(o6.ns["ns=cnc;i=7169"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7173",
                browseName="ns=cnc;ActStatus",
                description="Actual spindle state.",
                modellingRule="Mandatory",
                dataType=cnc_datypes.CncSpindleStatus,
                value=cnc_datypes.CncSpindleStatus.STOPPED,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7174",
                browseName="ns=cnc;ActTurnDirection",
                description="Turn direction actual value.",
                modellingRule="Mandatory",
                dataType=cnc_datypes.CncSpindleTurnDirection,
                value=cnc_datypes.CncSpindleTurnDirection.NONE,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7178", browseName="ns=cnc;CmdGear", description="Gear stage setpoint value.", modellingRule="Mandatory", dataType=o6.UInt32, value=0, accessLevel=3
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=7179"]),
        o6.hasComponent(o6.ns["ns=cnc;i=7181"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7184",
                browseName="ns=cnc;ActChannel",
                description="NodeId of the channel object (CncChannelType) that administrates this drive to expose drive’s channel affiliation.",
                modellingRule="Mandatory",
                dataType=o6.NodeId,
                value=o6.NodeId("i=0"),
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=7185"]),
        o6.hasComponent(o6.ns["ns=cnc;i=7188"]),
        o6.hasComponent(o6.ns["ns=cnc;i=7191"]),
        o6.hasComponent(o6.ns["ns=cnc;i=7194"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7197",
                browseName="ns=cnc;IsInactive",
                description="Drive inactive state (true in case of inactive drive, else false).",
                modellingRule="Mandatory",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7198",
                browseName="ns=cnc;IsVirtual",
                description="Virtual axis (no hardware present; true in case of virtual axis, else fals).",
                modellingRule="Mandatory",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
    ],
)
o6.reference(cnc_objtypes.CncChannelType, ns0.reftypes.HasComponent, o6.ns["ns=cnc;i=5030"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;i=7199",
    browseName="ns=cnc;CmdTorque",
    description="Drive torque setpoint value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;i=7200",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;i=7201", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0))),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
x_3 = cnc_objtypes.CncAxisType(
    nodeId="ns=cnc;i=5032",
    browseName="ns=cnc;X",
    references=[
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7120",
                browseName="ns=cnc;ActStatus",
                description="Actual axis state.",
                dataType=cnc_datypes.CncAxisStatus,
                value=cnc_datypes.CncAxisStatus.IN_POSITION,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7121",
                browseName="ns=cnc;IsReferenced",
                description="Axis reference state (true in case of successfully refereneced axis, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7122",
                browseName="ns=cnc;IsRotational",
                description="Axis type (true in case of rotational axis, in case of linear type or other false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=7123"]),
        o6.hasComponent(o6.ns["ns=cnc;i=7129"]),
        o6.hasComponent(o6.ns["ns=cnc;i=7136"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7139",
                browseName="ns=cnc;ActChannel",
                description="NodeId of the channel object (CncChannelType) that administrates this drive to expose drive’s channel affiliation.",
                dataType=o6.NodeId,
                value=o6.NodeId("i=0"),
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;i=7140"]),
        o6.hasComponent(o6.ns["ns=cnc;i=7163"]),
        o6.hasComponent(o6.ns["ns=cnc;i=7175"]),
        o6.hasComponent(o6.ns["ns=cnc;i=7199"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7202",
                browseName="ns=cnc;IsInactive",
                description="Drive inactive state (true in case of inactive drive, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;i=7203",
                browseName="ns=cnc;IsVirtual",
                description="Virtual axis (no hardware present; true in case of virtual axis, else fals).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;s=CncInterface.CncAxisList.X.ActLoad",
    browseName="ns=cnc;ActLoad",
    description="Drive load actual value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;s=CncInterface.CncAxisList.X.ActLoad.EURange", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;s=CncInterface.CncAxisList.X.ActLoad.EngineeringUnits",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;s=CncInterface.CncAxisList.X.ActPower",
    browseName="ns=cnc;ActPower",
    description="Drive power actual value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;s=CncInterface.CncAxisList.X.ActPower.EURange", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;s=CncInterface.CncAxisList.X.ActPower.EngineeringUnits",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;s=CncInterface.CncAxisList.X.ActTorque",
    browseName="ns=cnc;ActTorque",
    description="Drive torque actual value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;s=CncInterface.CncAxisList.X.ActTorque.EURange", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;s=CncInterface.CncAxisList.X.ActTorque.EngineeringUnits",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;s=CncInterface.CncAxisList.X.CmdTorque",
    browseName="ns=cnc;CmdTorque",
    description="Drive torque setpoint value.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;s=CncInterface.CncAxisList.X.CmdTorque.EURange", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0)
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;s=CncInterface.CncAxisList.X.CmdTorque.EngineeringUnits",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20053, displayName=o6.LocalizedText("N·m"), description=o6.LocalizedText("newton metre")
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;s=CncInterface.CncAxisList.X.PosDirect",
    browseName="ns=cnc;PosDirect",
    description="Position actual value referring to axis' direct measurement system.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;s=CncInterface.CncAxisList.X.PosDirect.EURange", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;s=CncInterface.CncAxisList.X.PosDirect.EngineeringUnits", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;s=CncInterface.CncAxisList.X.PosDirect.ActPos", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;s=CncInterface.CncAxisList.X.PosDirect.CmdPos", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;s=CncInterface.CncAxisList.X.PosDirect.RemDist", browseName="ns=cnc;RemDist", description="Remaining distance to go.", dataType=o6.Double, value=0.0
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
cnc_vartypes.CncPositionVariableType(
    nodeId="ns=cnc;s=CncInterface.CncAxisList.X.PosIndirect",
    browseName="ns=cnc;PosIndirect",
    description="Position actual value referring to axis' indirect measurement system.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cnc;s=CncInterface.CncAxisList.X.PosIndirect.EURange", browseName="ns=cnc;EURange", dataType=ns0.datatypes.Range, accessLevel=3)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;s=CncInterface.CncAxisList.X.PosIndirect.EngineeringUnits", browseName="ns=cnc;EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;s=CncInterface.CncAxisList.X.PosIndirect.ActPos", browseName="ns=cnc;ActPos", description="Position current value.", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;s=CncInterface.CncAxisList.X.PosIndirect.CmdPos", browseName="ns=cnc;CmdPos", description="Position setpoint value.", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cnc;s=CncInterface.CncAxisList.X.PosIndirect.RemDist",
                browseName="ns=cnc;RemDist",
                description="Remaining distance to go.",
                dataType=o6.Double,
                value=0.0,
            )
        ),
    ],
    dataType=cnc_datypes.CncPositionDataType,
    value=cnc_datypes.CncPositionDataType(actPos=0.0, cmdPos=0.0, remDist=0.0),
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=cnc;s=CncInterface.CncAxisList.X.ZeroOffset",
    browseName="ns=cnc;ZeroOffset",
    description="Active axis zero offset.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cnc;s=CncInterface.CncAxisList.X.ZeroOffset.EURange", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cnc;s=CncInterface.CncAxisList.X.ZeroOffset.EngineeringUnits",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5066068, displayName=o6.LocalizedText("mm"), description=o6.LocalizedText("millimetre")
                ),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
)
x_4 = cnc_objtypes.CncAxisType(
    nodeId="ns=cnc;s=CncInterface.CncAxisList.X",
    browseName="ns=cnc;X",
    references=[
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;s=CncInterface.CncAxisList.X.ActChannel",
                browseName="ns=cnc;ActChannel",
                description="NodeId of the channel object (CncChannelType) that administrates this drive to expose drive’s channel affiliation.",
                dataType=o6.NodeId,
                value=o6.NodeId("i=0"),
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;s=CncInterface.CncAxisList.X.ActLoad"]),
        o6.hasComponent(o6.ns["ns=cnc;s=CncInterface.CncAxisList.X.ActPower"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;s=CncInterface.CncAxisList.X.ActStatus",
                browseName="ns=cnc;ActStatus",
                description="Actual axis state.",
                dataType=cnc_datypes.CncAxisStatus,
                value=cnc_datypes.CncAxisStatus.IN_POSITION,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;s=CncInterface.CncAxisList.X.ActTorque"]),
        o6.hasComponent(o6.ns["ns=cnc;s=CncInterface.CncAxisList.X.CmdTorque"]),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;s=CncInterface.CncAxisList.X.IsInactive",
                browseName="ns=cnc;IsInactive",
                description="Drive inactive state (true in case of inactive drive, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;s=CncInterface.CncAxisList.X.IsReferenced",
                browseName="ns=cnc;IsReferenced",
                description="Axis reference state (true in case of successfully refereneced axis, else false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;s=CncInterface.CncAxisList.X.IsRotational",
                browseName="ns=cnc;IsRotational",
                description="Axis type (true in case of rotational axis, in case of linear type or other false).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.DataItemType(
                nodeId="ns=cnc;s=CncInterface.CncAxisList.X.IsVirtual",
                browseName="ns=cnc;IsVirtual",
                description="Virtual axis (no hardware present; true in case of virtual axis, else fals).",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
            )
        ),
        o6.hasComponent(o6.ns["ns=cnc;s=CncInterface.CncAxisList.X.PosDirect"]),
        o6.hasComponent(o6.ns["ns=cnc;s=CncInterface.CncAxisList.X.PosIndirect"]),
        o6.hasComponent(o6.ns["ns=cnc;s=CncInterface.CncAxisList.X.ZeroOffset"]),
    ],
)


del Any, TYPE_CHECKING, uuid, o6, ns0, cnc_datypes, cnc_vartypes, cnc_objtypes
