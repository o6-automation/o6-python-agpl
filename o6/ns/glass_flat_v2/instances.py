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

"""Generated OPC UA glass_flat_v2 namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.ns0 as ns0
from . import datatypes as glass_flat_v2_datypes
from . import objtypes as glass_flat_v2_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat_v2;i=5003", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat_v2;i=5004", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat_v2;i=5005", browseName="Default XML")
o6.hasEncoding(glass_flat_v2_datypes.ProcessingParameterDataType, o6.ns["ns=glass_flat_v2;i=5005"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat_v2;i=5006", browseName="Default JSON")
o6.hasEncoding(glass_flat_v2_datypes.ProcessingParameterDataType, o6.ns["ns=glass_flat_v2;i=5006"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat_v2;i=5007", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat_v2;i=5008", browseName="Default XML")
o6.hasEncoding(glass_flat_v2_datypes.ReasonDescriptionType, o6.ns["ns=glass_flat_v2;i=5008"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat_v2;i=5010", browseName="Default XML")
o6.hasEncoding(glass_flat_v2_datypes.ProcessingCategoryDataType, o6.ns["ns=glass_flat_v2;i=5010"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat_v2;i=5012", browseName="Default JSON")
o6.hasEncoding(glass_flat_v2_datypes.ProcessingCategoryDataType, o6.ns["ns=glass_flat_v2;i=5012"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat_v2;i=5013", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat_v2;i=5014", browseName="Default XML")
o6.hasEncoding(glass_flat_v2_datypes.EClassTermDataType, o6.ns["ns=glass_flat_v2;i=5014"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat_v2;i=5018", browseName="Default JSON")
o6.hasEncoding(glass_flat_v2_datypes.EClassTermDataType, o6.ns["ns=glass_flat_v2;i=5018"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat_v2;i=5019", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat_v2;i=5020", browseName="Default XML")
o6.hasEncoding(glass_flat_v2_datypes.ValueDataType, o6.ns["ns=glass_flat_v2;i=5020"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat_v2;i=5021", browseName="Default JSON")
o6.hasEncoding(glass_flat_v2_datypes.ValueDataType, o6.ns["ns=glass_flat_v2;i=5021"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat_v2;i=5027", browseName="Default JSON")
o6.hasEncoding(glass_flat_v2_datypes.ReasonDescriptionType, o6.ns["ns=glass_flat_v2;i=5027"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat_v2;i=5037", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat_v2;i=5038", browseName="Default XML")
o6.hasEncoding(glass_flat_v2_datypes.FileFormatDataType, o6.ns["ns=glass_flat_v2;i=5038"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat_v2;i=5039", browseName="Default JSON")
o6.hasEncoding(glass_flat_v2_datypes.FileFormatDataType, o6.ns["ns=glass_flat_v2;i=5039"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat_v2;i=5082", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat_v2;i=5083", browseName="Default XML")
o6.hasEncoding(glass_flat_v2_datypes.UserProfileDataType, o6.ns["ns=glass_flat_v2;i=5083"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat_v2;i=5084", browseName="Default JSON")
o6.hasEncoding(glass_flat_v2_datypes.UserProfileDataType, o6.ns["ns=glass_flat_v2;i=5084"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=glass_flat_v2;i=6001",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat_v2;i=6002", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=glass_flat_v2;i=5022", browseName="ns=machinery;MachineryItemState", references=[o6.hasComponent(o6.ns["ns=glass_flat_v2;i=6001"])]
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=glass_flat_v2;i=6004", browseName="ns=glass_flat_v2;ReasonDescriptionType", dataType=o6.String, value="ReasonDescriptionType")
o6.reference(o6.ns["ns=glass_flat_v2;i=5003"], "i=39", o6.ns["ns=glass_flat_v2;i=6004"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=glass_flat_v2;i=6005", browseName="ns=glass_flat_v2;ReasonDescriptionType", dataType=o6.String, value="//xs:element[@name='ReasonDescriptionType']"
)
o6.reference(o6.ns["ns=glass_flat_v2;i=5008"], "i=39", o6.ns["ns=glass_flat_v2;i=6005"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=glass_flat_v2;i=6003",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat_v2;i=6017", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryOperationModeStateMachineType(
    nodeId="ns=glass_flat_v2;i=5023", browseName="ns=machinery;MachineryOperationMode", references=[o6.hasComponent(o6.ns["ns=glass_flat_v2;i=6003"])]
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=glass_flat_v2;i=6018",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat_v2;i=6019", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
isa95_jobcontrol_v2.objtypes.ISA95JobOrderReceiverObjectType(
    nodeId="ns=glass_flat_v2;i=5024",
    browseName="ns=machinery_jobs;JobOrderControl",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat_v2;i=6025", browseName="ns=isa95_jobcontrol_v2;MaxDownloadableJobOrders", dataType=o6.UInt16)),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=6018"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=glass_flat_v2;i=6020",
                browseName="ns=isa95_jobcontrol_v2;EquipmentID",
                description="Defines a read-only set of Equipment Class IDs and Equipment IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=glass_flat_v2;i=6021",
                browseName="ns=isa95_jobcontrol_v2;JobOrderList",
                description="Defines a read-only list of job order information available from the server.",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95JobOrderAndStateDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=glass_flat_v2;i=6022",
                browseName="ns=isa95_jobcontrol_v2;MaterialClassID",
                description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=glass_flat_v2;i=6023",
                browseName="ns=isa95_jobcontrol_v2;MaterialDefinitionID",
                description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=glass_flat_v2;i=6026",
                browseName="ns=isa95_jobcontrol_v2;PersonnelID",
                description="Defines a read-only set of Personnel IDs and Person IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=glass_flat_v2;i=6027",
                browseName="ns=isa95_jobcontrol_v2;PhysicalAssetID",
                description="Defines a read-only set of Physical Asset Class IDs and Physical Asset IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=glass_flat_v2;i=6028",
                browseName="ns=isa95_jobcontrol_v2;WorkMaster",
                description="Defines a read-only set of work master IDs that may be specified in a job order, and the read-only set of parameters that may be specified for a specific work master.",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95WorkMasterDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
    ],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=glass_flat_v2;i=6035", browseName="ns=glass_flat_v2;EClassTermDataType", dataType=o6.String, value="EClassTermDataType")
o6.reference(o6.ns["ns=glass_flat_v2;i=5013"], "i=39", o6.ns["ns=glass_flat_v2;i=6035"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=glass_flat_v2;i=6036", browseName="ns=glass_flat_v2;EClassTermDataType", dataType=o6.String, value="//xs:element[@name='EClassTermDataType']"
)
o6.reference(o6.ns["ns=glass_flat_v2;i=5014"], "i=39", o6.ns["ns=glass_flat_v2;i=6036"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=glass_flat_v2;i=6037", browseName="ns=glass_flat_v2;FileFormatDataType", dataType=o6.String, value="FileFormatDataType")
o6.reference(o6.ns["ns=glass_flat_v2;i=5037"], "i=39", o6.ns["ns=glass_flat_v2;i=6037"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=glass_flat_v2;i=6038", browseName="ns=glass_flat_v2;FileFormatDataType", dataType=o6.String, value="//xs:element[@name='FileFormatDataType']"
)
o6.reference(o6.ns["ns=glass_flat_v2;i=5038"], "i=39", o6.ns["ns=glass_flat_v2;i=6038"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=glass_flat_v2;i=6039", browseName="ns=glass_flat_v2;ProcessingCategoryDataType", dataType=o6.String, value="ProcessingCategoryDataType"
)
o6.reference(o6.ns["ns=glass_flat_v2;i=5007"], "i=39", o6.ns["ns=glass_flat_v2;i=6039"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=glass_flat_v2;i=6040", browseName="ns=glass_flat_v2;ProcessingCategoryDataType", dataType=o6.String, value="//xs:element[@name='ProcessingCategoryDataType']"
)
o6.reference(o6.ns["ns=glass_flat_v2;i=5010"], "i=39", o6.ns["ns=glass_flat_v2;i=6040"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=glass_flat_v2;i=6041", browseName="ns=glass_flat_v2;ProcessingParameterDataType", dataType=o6.String, value="ProcessingParameterDataType"
)
o6.reference(o6.ns["ns=glass_flat_v2;i=5004"], "i=39", o6.ns["ns=glass_flat_v2;i=6041"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=glass_flat_v2;i=6042", browseName="ns=glass_flat_v2;ProcessingParameterDataType", dataType=o6.String, value="//xs:element[@name='ProcessingParameterDataType']"
)
o6.reference(o6.ns["ns=glass_flat_v2;i=5005"], "i=39", o6.ns["ns=glass_flat_v2;i=6042"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=glass_flat_v2;i=6043", browseName="ns=glass_flat_v2;UserProfileDataType", dataType=o6.String, value="UserProfileDataType")
o6.reference(o6.ns["ns=glass_flat_v2;i=5082"], "i=39", o6.ns["ns=glass_flat_v2;i=6043"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=glass_flat_v2;i=6044", browseName="ns=glass_flat_v2;UserProfileDataType", dataType=o6.String, value="//xs:element[@name='UserProfileDataType']"
)
o6.reference(o6.ns["ns=glass_flat_v2;i=5083"], "i=39", o6.ns["ns=glass_flat_v2;i=6044"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=glass_flat_v2;i=6045", browseName="ns=glass_flat_v2;ValueDataType", dataType=o6.String, value="ValueDataType")
o6.reference(o6.ns["ns=glass_flat_v2;i=5019"], "i=39", o6.ns["ns=glass_flat_v2;i=6045"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=glass_flat_v2;i=6031",
    browseName="ns=glass_flat_v2;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Glass/Flat/v2/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=glass_flat_v2;i=6032", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Glass/Flat/v2/")
        ),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=6004"]),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=6035"]),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=6037"]),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=6039"]),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=6041"]),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=6043"]),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=6045"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/Glass/Flat/v2/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/Glass/Flat/v2/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="EClassTermDataType">\n  <opc:Field TypeName="opc:CharArray" Name="ID"/>\n  <opc:Field TypeName="opc:CharArray" Name="Description"/>\n  <opc:Field TypeName="opc:CharArray" Name="EClass"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="FileFormatDataType">\n  <opc:Field TypeName="opc:CharArray" Name="Name"/>\n  <opc:Field TypeName="opc:CharArray" Name="FileExtension"/>\n  <opc:Field TypeName="opc:CharArray" Name="Version"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ProcessingCategoryDataType">\n  <opc:Field TypeName="opc:CharArray" Name="ID"/>\n  <opc:Field TypeName="opc:CharArray" Name="Description"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfSupportedParameter"/>\n  <opc:Field LengthField="NoOfSupportedParameter" TypeName="tns:ProcessingParameterDataType" Name="SupportedParameter"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfSupportedAssignment"/>\n  <opc:Field LengthField="NoOfSupportedAssignment" TypeName="opc:CharArray" Name="SupportedAssignment"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfSupportedVariable"/>\n  <opc:Field LengthField="NoOfSupportedVariable" TypeName="tns:ProcessingParameterDataType" Name="SupportedVariable"/>\n  <opc:Field TypeName="opc:Int32" Name="SupportsTransformation"/>\n  <opc:Field TypeName="opc:Int32" Name="SupportsSubProcessing"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ProcessingParameterDataType">\n  <opc:Field TypeName="opc:CharArray" Name="Name"/>\n  <opc:Field TypeName="opc:CharArray" Name="Description"/>\n  <opc:Field TypeName="tns:ValueDataType" Name="ValueType"/>\n  <opc:Field TypeName="opc:CharArray" Name="TypicalValue"/>\n  <opc:Field TypeName="opc:Boolean" Name="Mandatory"/>\n  <opc:Field TypeName="tns:EClassTermDataType" Name="EClass"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ReasonDescriptionType">\n  <opc:Field TypeName="opc:Bit" Name="ReferenceSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="CategorySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="VendorCodeSpecified"/>\n  <opc:Field Length="29" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="ua:LocalizedText" Name="Description"/>\n  <opc:Field SwitchField="ReferenceSpecified" TypeName="opc:CharArray" Name="Reference"/>\n  <opc:Field SwitchField="CategorySpecified" TypeName="opc:CharArray" Name="Category"/>\n  <opc:Field SwitchField="VendorCodeSpecified" TypeName="opc:CharArray" Name="VendorCode"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="UserProfileDataType">\n  <opc:Field TypeName="opc:CharArray" Name="Name"/>\n  <opc:Field TypeName="opc:DateTime" Name="LoginTime"/>\n  <opc:Field TypeName="opc:CharArray" Name="Language"/>\n  <opc:Field TypeName="opc:CharArray" Name="MeasurementFormat"/>\n  <opc:Field TypeName="opc:CharArray" Name="AccessLevel"/>\n  <opc:Field TypeName="opc:Boolean" Name="OpcUaUser"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ValueDataType">\n  <opc:Field TypeName="opc:CharArray" Name="Name"/>\n  <opc:Field TypeName="opc:CharArray" Name="Description"/>\n  <opc:Field TypeName="opc:CharArray" Name="BaseUnit"/>\n  <opc:Field TypeName="opc:CharArray" Name="PossibleValue"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="CoatingClassEnumeration">\n  <opc:EnumeratedValue Name="HardCoating" Value="0"/>\n  <opc:EnumeratedValue Name="SoftCoating" Value="1"/>\n  <opc:EnumeratedValue Name="CoatedWithFoilProtection" Value="2"/>\n  <opc:EnumeratedValue Name="UserDefined" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="CoordinateSystemEnumeration">\n  <opc:EnumeratedValue Name="Unknown" Value="0"/>\n  <opc:EnumeratedValue Name="System1" Value="1"/>\n  <opc:EnumeratedValue Name="System2" Value="2"/>\n  <opc:EnumeratedValue Name="System3" Value="3"/>\n  <opc:EnumeratedValue Name="System4" Value="4"/>\n  <opc:EnumeratedValue Name="System5" Value="5"/>\n  <opc:EnumeratedValue Name="System6" Value="6"/>\n  <opc:EnumeratedValue Name="System7" Value="7"/>\n  <opc:EnumeratedValue Name="System8" Value="8"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="SignificantSideEnumeration">\n  <opc:EnumeratedValue Name="Indifferent" Value="0"/>\n  <opc:EnumeratedValue Name="Top" Value="1"/>\n  <opc:EnumeratedValue Name="Down" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="SpacerMaterialClass">\n  <opc:EnumeratedValue Name="Other" Value="0"/>\n  <opc:EnumeratedValue Name="Metallic" Value="1"/>\n  <opc:EnumeratedValue Name="TPS" Value="2"/>\n  <opc:EnumeratedValue Name="Plastic" Value="3"/>\n  <opc:EnumeratedValue Name="Elastic" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="StructureAlignmentEnumeration">\n  <opc:EnumeratedValue Name="Indifferent" Value="0"/>\n  <opc:EnumeratedValue Name="Longitudinal" Value="1"/>\n  <opc:EnumeratedValue Name="Transverse" Value="2"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=glass_flat_v2;i=6046", browseName="ns=glass_flat_v2;ValueDataType", dataType=o6.String, value="//xs:element[@name='ValueDataType']")
o6.reference(o6.ns["ns=glass_flat_v2;i=5020"], "i=39", o6.ns["ns=glass_flat_v2;i=6046"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=glass_flat_v2;i=6033",
    browseName="ns=glass_flat_v2;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Glass/Flat/v2/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=glass_flat_v2;i=6034", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Glass/Flat/v2/Types.xsd")
        ),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=6005"]),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=6036"]),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=6038"]),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=6040"]),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=6042"]),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=6044"]),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=6046"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/Glass/Flat/v2/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/Glass/Flat/v2/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="CoatingClassEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="HardCoating_0"/>\n   <xs:enumeration value="SoftCoating_1"/>\n   <xs:enumeration value="CoatedWithFoilProtection_2"/>\n   <xs:enumeration value="UserDefined_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:CoatingClassEnumeration" name="CoatingClassEnumeration"/>\n <xs:complexType name="ListOfCoatingClassEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CoatingClassEnumeration" name="CoatingClassEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCoatingClassEnumeration" name="ListOfCoatingClassEnumeration" nillable="true"/>\n <xs:simpleType name="CoordinateSystemEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Unknown_0"/>\n   <xs:enumeration value="System1_1"/>\n   <xs:enumeration value="System2_2"/>\n   <xs:enumeration value="System3_3"/>\n   <xs:enumeration value="System4_4"/>\n   <xs:enumeration value="System5_5"/>\n   <xs:enumeration value="System6_6"/>\n   <xs:enumeration value="System7_7"/>\n   <xs:enumeration value="System8_8"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:CoordinateSystemEnumeration" name="CoordinateSystemEnumeration"/>\n <xs:complexType name="ListOfCoordinateSystemEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CoordinateSystemEnumeration" name="CoordinateSystemEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCoordinateSystemEnumeration" name="ListOfCoordinateSystemEnumeration" nillable="true"/>\n <xs:simpleType name="SignificantSideEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Indifferent_0"/>\n   <xs:enumeration value="Top_1"/>\n   <xs:enumeration value="Down_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:SignificantSideEnumeration" name="SignificantSideEnumeration"/>\n <xs:complexType name="ListOfSignificantSideEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SignificantSideEnumeration" name="SignificantSideEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSignificantSideEnumeration" name="ListOfSignificantSideEnumeration" nillable="true"/>\n <xs:simpleType name="SpacerMaterialClass">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Other_0"/>\n   <xs:enumeration value="Metallic_1"/>\n   <xs:enumeration value="TPS_2"/>\n   <xs:enumeration value="Plastic_3"/>\n   <xs:enumeration value="Elastic_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:SpacerMaterialClass" name="SpacerMaterialClass"/>\n <xs:complexType name="ListOfSpacerMaterialClass">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SpacerMaterialClass" name="SpacerMaterialClass" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSpacerMaterialClass" name="ListOfSpacerMaterialClass" nillable="true"/>\n <xs:simpleType name="StructureAlignmentEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Indifferent_0"/>\n   <xs:enumeration value="Longitudinal_1"/>\n   <xs:enumeration value="Transverse_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:StructureAlignmentEnumeration" name="StructureAlignmentEnumeration"/>\n <xs:complexType name="ListOfStructureAlignmentEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:StructureAlignmentEnumeration" name="StructureAlignmentEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfStructureAlignmentEnumeration" name="ListOfStructureAlignmentEnumeration" nillable="true"/>\n <xs:complexType name="EClassTermDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Description"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="EClass"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:EClassTermDataType" name="EClassTermDataType"/>\n <xs:complexType name="ListOfEClassTermDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:EClassTermDataType" name="EClassTermDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfEClassTermDataType" name="ListOfEClassTermDataType" nillable="true"/>\n <xs:complexType name="FileFormatDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Name"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="FileExtension"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Version"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:FileFormatDataType" name="FileFormatDataType"/>\n <xs:complexType name="ListOfFileFormatDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:FileFormatDataType" name="FileFormatDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfFileFormatDataType" name="ListOfFileFormatDataType" nillable="true"/>\n <xs:complexType name="ProcessingCategoryDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Description"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfProcessingParameterDataType" name="SupportedParameter"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="SupportedAssignment"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfProcessingParameterDataType" name="SupportedVariable"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="SupportsTransformation"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="SupportsSubProcessing"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ProcessingCategoryDataType" name="ProcessingCategoryDataType"/>\n <xs:complexType name="ListOfProcessingCategoryDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ProcessingCategoryDataType" name="ProcessingCategoryDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfProcessingCategoryDataType" name="ListOfProcessingCategoryDataType" nillable="true"/>\n <xs:complexType name="ProcessingParameterDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Name"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Description"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ValueDataType" name="ValueType"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="TypicalValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="Mandatory"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:EClassTermDataType" name="EClass"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ProcessingParameterDataType" name="ProcessingParameterDataType"/>\n <xs:complexType name="ListOfProcessingParameterDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ProcessingParameterDataType" name="ProcessingParameterDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfProcessingParameterDataType" name="ListOfProcessingParameterDataType" nillable="true"/>\n <xs:complexType name="ReasonDescriptionType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="Description"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Reference"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Category"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="VendorCode"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ReasonDescriptionType" name="ReasonDescriptionType"/>\n <xs:complexType name="ListOfReasonDescriptionType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ReasonDescriptionType" name="ReasonDescriptionType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfReasonDescriptionType" name="ListOfReasonDescriptionType" nillable="true"/>\n <xs:complexType name="UserProfileDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Name"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="LoginTime"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Language"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="MeasurementFormat"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="AccessLevel"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="OpcUaUser"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:UserProfileDataType" name="UserProfileDataType"/>\n <xs:complexType name="ListOfUserProfileDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:UserProfileDataType" name="UserProfileDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfUserProfileDataType" name="ListOfUserProfileDataType" nillable="true"/>\n <xs:complexType name="ValueDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Name"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Description"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="BaseUnit"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="PossibleValue"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ValueDataType" name="ValueDataType"/>\n <xs:complexType name="ListOfValueDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ValueDataType" name="ValueDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfValueDataType" name="ListOfValueDataType" nillable="true"/>\n</xs:schema>\n',
)
glass_flat_v2_objtypes.GlassMachineIdentificationType(
    nodeId="ns=glass_flat_v2;i=5001",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat_v2;i=6030",
                browseName="ns=glass_flat_v2;ProcessingCategories",
                dataType=glass_flat_v2_datypes.ProcessingCategoryDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat_v2;i=6057",
                browseName="ns=glass_flat_v2;LoggedInProfiles",
                dataType=glass_flat_v2_datypes.UserProfileDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat_v2;i=6058",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat_v2;i=6061",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat_v2;i=6062",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(glass_flat_v2_objtypes.GlassMachineType, ns0.reftypes.HasAddIn, o6.ns["ns=glass_flat_v2;i=5001"])
glass_flat_v2_objtypes.ConfigurationRulesType(
    nodeId="ns=glass_flat_v2;i=5029",
    browseName="ns=glass_flat_v2;ConfigurationRules",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat_v2;i=6067",
                browseName="ns=glass_flat_v2;MachineProcessingCoordinateSystem",
                dataType=glass_flat_v2_datypes.CoordinateSystemEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
)
o6.reference(glass_flat_v2_objtypes.GlassMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat_v2;i=5029"])
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6162",
    browseName="EnumStrings",
    parent="ns=glass_flat_v2;i=3005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[5],
    value=[o6.LocalizedText("Other"), o6.LocalizedText("Metallic"), o6.LocalizedText("TPS"), o6.LocalizedText("Plastic"), o6.LocalizedText("Elastic")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6189",
    browseName="EnumStrings",
    parent="ns=glass_flat_v2;i=3008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[9],
    value=[
        o6.LocalizedText("Unknown"),
        o6.LocalizedText("System1"),
        o6.LocalizedText("System2"),
        o6.LocalizedText("System3"),
        o6.LocalizedText("System4"),
        o6.LocalizedText("System5"),
        o6.LocalizedText("System6"),
        o6.LocalizedText("System7"),
        o6.LocalizedText("System8"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6229",
    browseName="EnumStrings",
    parent="ns=glass_flat_v2;i=3009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("HardCoating"), o6.LocalizedText("SoftCoating"), o6.LocalizedText("CoatedWithFoilProtection"), o6.LocalizedText("UserDefined")],
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashGlassSlashFlatSlashV2Slash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=glass_flat_v2;i=5041",
    browseName="ns=glass_flat_v2;http://opcfoundation.org/UA/Glass/Flat/v2/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat_v2;i=6262", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=glass_flat_v2;i=6263", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2024-10-01T00:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=glass_flat_v2;i=6264", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Glass/Flat/v2/")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat_v2;i=6265", browseName="NamespaceVersion", dataType=o6.String, value="2.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat_v2;i=6266",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat_v2;i=6267", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat_v2;i=6268", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6372",
    browseName="EnumStrings",
    parent="ns=glass_flat_v2;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("Indifferent"), o6.LocalizedText("Top"), o6.LocalizedText("Down")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6377",
    browseName="EnumStrings",
    parent="ns=glass_flat_v2;i=3004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("Indifferent"), o6.LocalizedText("Longitudinal"), o6.LocalizedText("Transverse")],
)


ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6081",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat_v2;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat_v2;i=7001", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat_v2;i=6081"]))

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6082",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat_v2;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6083",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat_v2;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(
    nodeId="ns=glass_flat_v2;i=7002",
    browseName="GetPosition",
    inputArgs=o6.hasProperty(o6.ns["ns=glass_flat_v2;i=6082"]),
    outputArgs=o6.hasProperty(o6.ns["ns=glass_flat_v2;i=6083"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6047",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat_v2;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="JobOrderID", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Contains an ID of the job order, as specified by the method caller.")
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6048",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat_v2;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobResponse",
            dataType=o6.NodeId("ns=aml;i=3013"),
            valueRank=-1,
            description=o6.LocalizedText(
                "Contains information about the execution of a job order, such as the current status of the job, actual material consumed, actual material produced, actual equipment used, and job specific data."
            ),
        ),
        ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")),
    ],
)
o6.call(
    nodeId="ns=glass_flat_v2;i=7003",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderID",
    inputArgs=o6.hasProperty(o6.ns["ns=glass_flat_v2;i=6047"]),
    outputArgs=o6.hasProperty(o6.ns["ns=glass_flat_v2;i=6048"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6049",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat_v2;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="JobOrderState",
            dataType=o6.NodeId("ns=aml;i=3006"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "Contains a job status of the JobResponse to be returned. The array shall provide at least one entry representing the top level state and potentially additional entries representing substates. The first entry shall be the top level entry, having the BrowsePath set to null. The order of the substates is not defined."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6050",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat_v2;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobResponses",
            dataType=o6.NodeId("ns=aml;i=3013"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "Contains a list of information about the execution of a job order, such as the current status of the job, actual material consumed, actual material produced, actual equipment used, and job specific data. "
            ),
        ),
        ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")),
    ],
)
o6.call(
    nodeId="ns=glass_flat_v2;i=7004",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderState",
    inputArgs=o6.hasProperty(o6.ns["ns=glass_flat_v2;i=6049"]),
    outputArgs=o6.hasProperty(o6.ns["ns=glass_flat_v2;i=6050"]),
)

isa95_jobcontrol_v2.objtypes.ISA95JobResponseProviderObjectType(
    nodeId="ns=glass_flat_v2;i=5025",
    browseName="ns=machinery_jobs;JobOrderResults",
    references=[o6.hasComponent(o6.ns["ns=glass_flat_v2;i=7003"]), o6.hasComponent(o6.ns["ns=glass_flat_v2;i=7004"])],
)
machinery_jobs.objtypes.JobManagementType(
    nodeId="ns=glass_flat_v2;i=5015",
    browseName="ns=machinery_jobs;JobManagement",
    references=[o6.hasComponent(o6.ns["ns=glass_flat_v2;i=5024"]), o6.hasComponent(o6.ns["ns=glass_flat_v2;i=5025"])],
)
ns0.objtypes.FolderType(
    nodeId="ns=glass_flat_v2;i=5030",
    browseName="ns=machinery;MachineryBuildingBlocks",
    modellingRule="Mandatory",
    references=[o6.hasAddIn(o6.ns["ns=glass_flat_v2;i=5015"]), o6.hasAddIn(o6.ns["ns=glass_flat_v2;i=5022"]), o6.hasAddIn(o6.ns["ns=glass_flat_v2;i=5023"])],
)
o6.reference(glass_flat_v2_objtypes.GlassMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat_v2;i=5030"])
o6.reference(o6.ns["ns=glass_flat_v2;i=5030"], "i=17604", o6.ns["ns=glass_flat_v2;i=5026"])


ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6084",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat_v2;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6085",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat_v2;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=glass_flat_v2;i=7005", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat_v2;i=6084"]), outputArgs=o6.hasProperty(o6.ns["ns=glass_flat_v2;i=6085"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6124",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat_v2;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6139",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat_v2;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(
    nodeId="ns=glass_flat_v2;i=7012", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat_v2;i=6124"]), outputArgs=o6.hasProperty(o6.ns["ns=glass_flat_v2;i=6139"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6140",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat_v2;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat_v2;i=7013", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat_v2;i=6140"]))

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6175",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat_v2;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat_v2;i=7014", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat_v2;i=6175"]))

ns0.objtypes.FileType(
    nodeId="ns=glass_flat_v2;i=5017",
    browseName="ns=glass_flat_v2;<LocalManuals>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat_v2;i=6086", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat_v2;i=6157", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat_v2;i=6158", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat_v2;i=6172", browseName="Writable", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=7001"]),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=7002"]),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=7005"]),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=7012"]),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=7013"]),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=7014"]),
    ],
)
o6.reference(glass_flat_v2_objtypes.ManualFolderType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat_v2;i=5017"])


ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6112",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat_v2;i=7024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DirectoryName", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6113",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat_v2;i=7024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DirectoryNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=glass_flat_v2;i=7024",
    browseName="CreateDirectory",
    inputArgs=o6.hasProperty(o6.ns["ns=glass_flat_v2;i=6112"]),
    outputArgs=o6.hasProperty(o6.ns["ns=glass_flat_v2;i=6113"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6153",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat_v2;i=7025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileName", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="RequestFileOpen", dataType=o6.Boolean, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6179",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat_v2;i=7025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=glass_flat_v2;i=7025",
    browseName="CreateFile",
    inputArgs=o6.hasProperty(o6.ns["ns=glass_flat_v2;i=6153"]),
    outputArgs=o6.hasProperty(o6.ns["ns=glass_flat_v2;i=6179"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6180",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat_v2;i=7026",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ObjectToDelete", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat_v2;i=7026", browseName="Delete", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat_v2;i=6180"]))

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6187",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat_v2;i=7031",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="ObjectToMoveOrCopy", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="TargetDirectory", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="CreateCopy", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="NewName", dataType=o6.String, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat_v2;i=6190",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat_v2;i=7031",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NewNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=glass_flat_v2;i=7031",
    browseName="MoveOrCopy",
    inputArgs=o6.hasProperty(o6.ns["ns=glass_flat_v2;i=6187"]),
    outputArgs=o6.hasProperty(o6.ns["ns=glass_flat_v2;i=6190"]),
)

ns0.objtypes.FileDirectoryType(
    nodeId="ns=glass_flat_v2;i=5016",
    browseName="FileSystem",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=7024"]),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=7025"]),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=7026"]),
        o6.hasComponent(o6.ns["ns=glass_flat_v2;i=7031"]),
    ],
)
o6.reference(glass_flat_v2_objtypes.GlassMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat_v2;i=5016"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, ns0, glass_flat_v2_datypes, glass_flat_v2_objtypes
