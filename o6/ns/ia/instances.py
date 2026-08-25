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

"""Generated OPC UA ia namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as ia_reftypes
from . import datatypes as ia_datypes
from . import vartypes as ia_vartypes
from . import objtypes as ia_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=ia;i=5009", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ia;i=5014", browseName="Default XML")
o6.hasEncoding(ia_datypes.RGBWDataType, o6.ns["ns=ia;i=5014"])
ns0.vartypes.PropertyType(
    nodeId="ns=ia;i=6001",
    browseName="EnumValues",
    parent="ns=ia;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Dimmed"), description=o6.LocalizedText("Uses dimming to display fractions.", "en")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Blinking"), description=o6.LocalizedText("Uses blinking to display fractions.", "en")),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("Display fractions in a way not defined in this version of the specification.", "en")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ia;i=6006",
    browseName="EnumValues",
    parent="ns=ia;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Segmented"), description=o6.LocalizedText("Stacklight is used as stack of individual lights", "en")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Levelmeter"), description=o6.LocalizedText("Stacklight is used as level meter", "en")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Running_Light"), description=o6.LocalizedText("The whole stack acts as a running light", "en")),
        ns0.datatypes.EnumValueType(
            value=3, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("Stacklight is used in a way not defined in this version of the specification", "en")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ia;i=6007",
    browseName="EnumValues",
    parent="ns=ia;i=3004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Off"), description=o6.LocalizedText("Element is disabled.", "en")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Red"), description=o6.LocalizedText("This value indicates a red lamp colour.", "en")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Green"), description=o6.LocalizedText("This value indicates a green lamp colour.", "en")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Blue"), description=o6.LocalizedText("This value indicates a blue lamp colour.", "en")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Yellow"), description=o6.LocalizedText("This value indicates a yellow lamp colour (R+G).", "en")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("Purple"), description=o6.LocalizedText("This value indicates a purple lamp colour (R+B).", "en")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("Cyan"), description=o6.LocalizedText("This value indicates a cyan lamp colour (G+B).", "en")),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("White"), description=o6.LocalizedText("This value indicates a white lamp colour (R+G+B).", "en")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ia;i=6008",
    browseName="EnumValues",
    parent="ns=ia;i=3005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Continuous"), description=o6.LocalizedText("This value indicates a continuous light.", "en")),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("Blinking"),
            description=o6.LocalizedText("This value indicates a blinking light (blinking in regular intervals with equally long on and off times).", "en"),
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("Flashing"),
            description=o6.LocalizedText(
                "This value indicates a flashing light (blinking in intervals with longer off times than on times, per interval multiple on times are possible).", "en"
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=3, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("The light is handled in a way not defined in this version of the specification.", "en")
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=ia;i=6010",
    browseName="ns=ia;LevelPercent",
    description="Shows the percentual value the stacklight is representing. The mandatory EURange Property of the Variable indicates the lowest and highest value and thereby allows to calculate the percentage represented by the value. The lowest value is interpreted as 0 percent, the highest is interpreted as 100 percent.",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6011", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ia_objtypes.StackLevelType, ns0.reftypes.HasComponent, o6.ns["ns=ia;i=6010"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=ia;i=6018",
    browseName="ns=ia;Intensity",
    description="Intensity of the lamp, thus its brightness. The mandatory EURange Property of the Variable indicates the lowest and highest value and thereby allows to calculate the percentage represented by the value. The lowest value is interpreted as 0 percent, the highest is interpreted as 100 percent.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6019", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ia_objtypes.StackElementLightType, ns0.reftypes.HasComponent, o6.ns["ns=ia;i=6018"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=ia;i=6021",
    browseName="ns=ia;Intensity",
    description="Indicates the sound pressure level of the acoustic signal when switched on. This value shall only have positive values. The mandatory EURange Property of the Variable indicates the lowest and highest value and thereby allows to calculate the percentage represented by the value. The lowest value is interpreted as 0 percent, the highest is interpreted as 100 percent.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6022", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ia_objtypes.StackElementAcousticType, ns0.reftypes.HasComponent, o6.ns["ns=ia;i=6021"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=ia;i=6026",
    browseName="ns=ia;Intensity",
    description="Shows the channel’s intensity, thus its brightness. The mandatory EURange Property of the Variable indicates the lowest and highest value and thereby allows to calculate the percentage represented by the value. The lowest value is interpreted as 0 percent, the highest is interpreted as 100 percent.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6027", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ia_objtypes.ControlChannelType, ns0.reftypes.HasComponent, o6.ns["ns=ia;i=6026"])
ia_objtypes.AcousticSignalType(
    nodeId="ns=ia;i=5004",
    browseName="<OrderedObject>",
    description="Represents an acoustic signal.",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ia;i=6030",
                browseName="NumberInList",
                description="Enumerate the acoustic signals. Instances of StackElementAcousticType index into this number using the OperationMode Property.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
)
ns0.objtypes.OrderedListType(
    nodeId="ns=ia;i=5003",
    browseName="ns=ia;AcousticSignals",
    description="Contains a list of audio signals used by this acoustic stacklight element.",
    modellingRule="Mandatory",
    references=[o6.hasOrderedComponent(o6.ns["ns=ia;i=5004"])],
)
o6.reference(ia_objtypes.StackElementAcousticType, ns0.reftypes.HasComponent, o6.ns["ns=ia;i=5003"])
ia_objtypes.ControlChannelType(
    nodeId="ns=ia;i=5002",
    browseName="ns=ia;<ControlChannel>",
    description="The list of <ControlChannel> instances shows the control information for each independent colour channel of the stacked element.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ia;i=6033", browseName="ns=ia;SignalOn", description="Indicates if the colour is switched on.", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ia;i=6031",
                browseName="ns=ia;ChannelColor",
                description="Indicates in what mode (continuously on, blinking, flashing) the channel operates when switched on.",
                dataType=ia_datypes.SignalColor,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ia;i=6032",
                browseName="ns=ia;SignalMode",
                description="Contains a list of audio signals used by this acoustic stacklight element.",
                dataType=ia_datypes.SignalModeLight,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(ia_objtypes.StackElementLightType, ns0.reftypes.HasComponent, o6.ns["ns=ia;i=5002"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=ia;i=6035",
    browseName="ns=ia;LevelPercent",
    description="Shows the percentual value the stacklight is representing. The mandatory EURange Property of the Variable indicates the lowest and highest value and thereby allows to calculate the percentage represented by the value. The lowest value is interpreted as 0 percent, the highest is interpreted as 100 percent.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6036", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
ia_objtypes.StackLevelType(
    nodeId="ns=ia;i=5001",
    browseName="ns=ia;StackLevel",
    description="Valid if the stacklight is used in “Levelmeter” StacklightMode. If so, the whole stack is controlled by a single percentual value. In this case, the SignalOn parameter of any stack element of StackElementLightType has no meaning.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ia;i=6034",
                browseName="ns=ia;DisplayMode",
                description="Indicates in what way the percentual value is displayed with the stacklight.",
                dataType=ia_datypes.LevelDisplayMode,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=ia;i=6035"]),
    ],
)
o6.reference(ia_objtypes.BasicStacklightType, ns0.reftypes.HasComponent, o6.ns["ns=ia;i=5001"])
ia_objtypes.StackElementType(
    nodeId="ns=ia;i=5006",
    browseName="<OrderedObject>",
    description="Represent the stack elements (lamps and acoustic elements) the stacklight is composed of. The HasOrderedComponent Reference shall represent the ordering from the base of the stacklight.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ia;i=6037",
                browseName="NumberInList",
                description="Enumerate the stacklight elements counting upwards beginning from the base of the stacklight.",
                dataType=ns0.datatypes.UInteger,
            )
        )
    ],
    _allow_abstract=True,
)
o6.reference(ia_objtypes.BasicStacklightType, ns0.reftypes.HasOrderedComponent, o6.ns["ns=ia;i=5006"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashIASlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=ia;i=5008",
    browseName="ns=ia;http://opcfoundation.org/UA/IA/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=ia;i=6039", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6040", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2025-05-23T00:00:00Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6041", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/IA/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6042", browseName="NamespaceVersion", dataType=o6.String, value="1.01.4")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ia;i=6043", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=ia;i=6044", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6045", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ia;i=6050", browseName="ns=ia;RGBWDataType", dataType=o6.String, value="RGBWDataType")
o6.reference(o6.ns["ns=ia;i=5009"], "i=39", o6.ns["ns=ia;i=6050"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ia;i=6051", browseName="ns=ia;RGBWDataType", dataType=o6.String, value="//xs:element[@name='RGBWDataType']")
o6.reference(o6.ns["ns=ia;i=5014"], "i=39", o6.ns["ns=ia;i=6051"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=ia;i=6002",
    browseName="ns=ia;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/IA",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6003", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/IA/")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=ia;i=6053",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=ia;i=6050"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:opc="http://opcfoundation.org/BinarySchema/" DefaultByteOrder="LittleEndian" TargetNamespace="http://opcfoundation.org/UA/IA/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ua="http://opcfoundation.org/UA/" xmlns:tns="http://opcfoundation.org/UA/IA/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RGBWDataType">\n  <opc:Field Name="WhiteSpecified" TypeName="opc:Bit"/>\n  <opc:Field Length="31" Name="Reserved1" TypeName="opc:Bit"/>\n  <opc:Field Name="Red" TypeName="opc:Byte"/>\n  <opc:Field Name="Green" TypeName="opc:Byte"/>\n  <opc:Field Name="Blue" TypeName="opc:Byte"/>\n  <opc:Field SwitchField="WhiteSpecified" Name="White" TypeName="opc:Byte"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="LevelDisplayMode">\n  <opc:Documentation>Contains the values used to indicate how a percentual value is displayed if the stacklight unit works in Levelmeter mode.</opc:Documentation>\n  <opc:EnumeratedValue Value="0" Name="Dimmed"/>\n  <opc:EnumeratedValue Value="1" Name="Blinking"/>\n  <opc:EnumeratedValue Value="2" Name="Other"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="SignalColor">\n  <opc:Documentation>Holds the possible colour values for stacklight lamps.</opc:Documentation>\n  <opc:EnumeratedValue Value="0" Name="Off"/>\n  <opc:EnumeratedValue Value="1" Name="Red"/>\n  <opc:EnumeratedValue Value="2" Name="Green"/>\n  <opc:EnumeratedValue Value="3" Name="Blue"/>\n  <opc:EnumeratedValue Value="4" Name="Yellow"/>\n  <opc:EnumeratedValue Value="5" Name="Purple"/>\n  <opc:EnumeratedValue Value="6" Name="Cyan"/>\n  <opc:EnumeratedValue Value="7" Name="White"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="SignalModeLight">\n  <opc:Documentation>Contains the values used to indicate in what way a lamp behaves when switched on.</opc:Documentation>\n  <opc:EnumeratedValue Value="0" Name="Continuous"/>\n  <opc:EnumeratedValue Value="1" Name="Blinking"/>\n  <opc:EnumeratedValue Value="2" Name="Flashing"/>\n  <opc:EnumeratedValue Value="3" Name="Other"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="StacklightOperationMode">\n  <opc:Documentation>Contains the values used to indicate how a stacklight (as a whole unit) is used.</opc:Documentation>\n  <opc:EnumeratedValue Value="0" Name="Segmented"/>\n  <opc:EnumeratedValue Value="1" Name="Levelmeter"/>\n  <opc:EnumeratedValue Value="2" Name="Running_Light"/>\n  <opc:EnumeratedValue Value="3" Name="Other"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=ia;i=6004",
    browseName="ns=ia;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/IA",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6005", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/IA/Types.xsd")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=ia;i=6054",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=ia;i=6051"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/IA/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema" targetNamespace="http://opcfoundation.org/UA/IA/Types.xsd">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="LevelDisplayMode">\n  <xs:annotation>\n   <xs:documentation>Contains the values used to indicate how a percentual value is displayed if the stacklight unit works in Levelmeter mode.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Dimmed_0"/>\n   <xs:enumeration value="Blinking_1"/>\n   <xs:enumeration value="Other_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:LevelDisplayMode" name="LevelDisplayMode"/>\n <xs:complexType name="ListOfLevelDisplayMode">\n  <xs:sequence>\n   <xs:element type="tns:LevelDisplayMode" nillable="true" name="LevelDisplayMode" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfLevelDisplayMode" nillable="true" name="ListOfLevelDisplayMode"/>\n <xs:simpleType name="SignalColor">\n  <xs:annotation>\n   <xs:documentation>Holds the possible colour values for stacklight lamps.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Off_0"/>\n   <xs:enumeration value="Red_1"/>\n   <xs:enumeration value="Green_2"/>\n   <xs:enumeration value="Blue_3"/>\n   <xs:enumeration value="Yellow_4"/>\n   <xs:enumeration value="Purple_5"/>\n   <xs:enumeration value="Cyan_6"/>\n   <xs:enumeration value="White_7"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:SignalColor" name="SignalColor"/>\n <xs:complexType name="ListOfSignalColor">\n  <xs:sequence>\n   <xs:element type="tns:SignalColor" nillable="true" name="SignalColor" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSignalColor" nillable="true" name="ListOfSignalColor"/>\n <xs:simpleType name="SignalModeLight">\n  <xs:annotation>\n   <xs:documentation>Contains the values used to indicate in what way a lamp behaves when switched on.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Continuous_0"/>\n   <xs:enumeration value="Blinking_1"/>\n   <xs:enumeration value="Flashing_2"/>\n   <xs:enumeration value="Other_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:SignalModeLight" name="SignalModeLight"/>\n <xs:complexType name="ListOfSignalModeLight">\n  <xs:sequence>\n   <xs:element type="tns:SignalModeLight" nillable="true" name="SignalModeLight" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSignalModeLight" nillable="true" name="ListOfSignalModeLight"/>\n <xs:simpleType name="StacklightOperationMode">\n  <xs:annotation>\n   <xs:documentation>Contains the values used to indicate how a stacklight (as a whole unit) is used.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Segmented_0"/>\n   <xs:enumeration value="Levelmeter_1"/>\n   <xs:enumeration value="Running_Light_2"/>\n   <xs:enumeration value="Other_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:StacklightOperationMode" name="StacklightOperationMode"/>\n <xs:complexType name="ListOfStacklightOperationMode">\n  <xs:sequence>\n   <xs:element type="tns:StacklightOperationMode" nillable="true" name="StacklightOperationMode" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfStacklightOperationMode" nillable="true" name="ListOfStacklightOperationMode"/>\n <xs:complexType name="RGBWDataType">\n  <xs:sequence>\n   <xs:element type="xs:unsignedInt" name="EncodingMask" minOccurs="0"/>\n   <xs:element type="xs:unsignedByte" name="Red" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:unsignedByte" name="Green" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:unsignedByte" name="Blue" minOccurs="0" maxOccurs="1"/>\n   <xs:element type="xs:unsignedByte" name="White" minOccurs="0" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RGBWDataType" name="RGBWDataType"/>\n <xs:complexType name="ListOfRGBWDataType">\n  <xs:sequence>\n   <xs:element type="tns:RGBWDataType" nillable="true" name="RGBWDataType" minOccurs="0" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRGBWDataType" nillable="true" name="ListOfRGBWDataType"/>\n</xs:schema>\n',
)
ia_vartypes.CalibrationValueType(
    nodeId="ns=ia;i=6064",
    browseName="ns=ia;<CalibrationValue>",
    description="A calibration value indicates the value the calibration target provides for calibration and includes its quantity and engineering unit.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6065", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3, userAccessLevel=1))
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ia_vartypes.CapacityRangeType(
    nodeId="ns=ia;i=6066",
    browseName="ns=ia;<CapacityRange>",
    description="A capacity range indicates a range (low and high value) as well as a resolution, and thus defines a number of values the calibration target provides for calibration and includes the quantity and engineering unit.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6067", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6068", browseName="ns=ia;Resolution", dataType=o6.Double, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=ns0.datatypes.Range,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(
    nodeId="ns=ia;i=5013",
    browseName="ns=ia;CalibrationTargetFeatures",
    description="A folder containing information about the features of a calibration target, that is, what can be calibrated with the calibration target.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=ia;i=6064"]), o6.hasComponent(o6.ns["ns=ia;i=6066"])],
)
o6.reference(ia_objtypes.CalibrationTargetType, ns0.reftypes.HasComponent, o6.ns["ns=ia;i=5013"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=ia;i=5010",
    browseName="ns=di;Identification",
    description="Provides identification information.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6069", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6070", browseName="ns=di;ManufacturerUri", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6071", browseName="ns=di;Model", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6072", browseName="ns=di;ProductCode", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6073", browseName="ns=di;HardwareRevision", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6074", browseName="ns=di;SoftwareRevision", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6075", browseName="ns=di;DeviceRevision", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6076", browseName="ns=di;DeviceClass", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6077", browseName="ns=di;SerialNumber", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6078", browseName="ns=di;ProductInstanceUri", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6079", browseName="ns=di;RevisionCounter", dataType=o6.Int32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6080", browseName="ns=di;AssetId", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6081", browseName="ns=di;ComponentName", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ia;i=6082", browseName="ns=di;DeviceManual", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
)
o6.reference(ia_objtypes.CalibrationTargetType, ns0.reftypes.HasComponent, o6.ns["ns=ia;i=5010"])
o6.reference(o6.ns["ns=ia;i=5010"], "i=17603", "ns=di;i=15035")
o6.reference(o6.ns["ns=ia;i=5010"], "i=17603", "ns=di;i=15048")


del Any, TYPE_CHECKING, uuid, o6, di, ns0, ia_reftypes, ia_datypes, ia_vartypes, ia_objtypes
