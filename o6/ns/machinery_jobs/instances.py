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

"""Generated OPC UA machinery_jobs namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.ns0 as ns0
from . import datatypes as machinery_jobs_datypes
from . import objtypes as machinery_jobs_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=machinery_jobs;i=5003", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machinery_jobs;i=5004", browseName="Default XML")
o6.hasEncoding(machinery_jobs_datypes.OutputInformationDataType, o6.ns["ns=machinery_jobs;i=5004"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machinery_jobs;i=5005", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machinery_jobs;i=5006", browseName="Default XML")
o6.hasEncoding(machinery_jobs_datypes.BOMComponentInformationDataType, o6.ns["ns=machinery_jobs;i=5006"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machinery_jobs;i=5007", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machinery_jobs;i=5008", browseName="Default XML")
o6.hasEncoding(machinery_jobs_datypes.BOMInformationDataType, o6.ns["ns=machinery_jobs;i=5008"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machinery_jobs;i=5009", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machinery_jobs;i=5010", browseName="Default XML")
o6.hasEncoding(machinery_jobs_datypes.OutputPerformanceInfoDataType, o6.ns["ns=machinery_jobs;i=5010"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machinery_jobs;i=6009",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_jobs;i=6010", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
isa95_jobcontrol_v2.objtypes.ISA95JobOrderReceiverObjectType(
    nodeId="ns=machinery_jobs;i=5001",
    browseName="ns=machinery_jobs;JobOrderControl",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_jobs;i=6005", browseName="ns=isa95_jobcontrol_v2;MaxDownloadableJobOrders", dataType=o6.UInt16)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_jobs;i=6001",
                browseName="ns=isa95_jobcontrol_v2;EquipmentID",
                description="Defines a read-only set of Equipment Class IDs and Equipment IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_jobs;i=6002",
                browseName="ns=isa95_jobcontrol_v2;JobOrderList",
                description="Defines a read-only list of job order information available from the server.",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95JobOrderAndStateDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_jobs;i=6003",
                browseName="ns=isa95_jobcontrol_v2;MaterialClassID",
                description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_jobs;i=6004",
                browseName="ns=isa95_jobcontrol_v2;MaterialDefinitionID",
                description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_jobs;i=6006",
                browseName="ns=isa95_jobcontrol_v2;PersonnelID",
                description="Defines a read-only set of Personnel IDs and Person IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_jobs;i=6007",
                browseName="ns=isa95_jobcontrol_v2;PhysicalAssetID",
                description="Defines a read-only set of Physical Asset Class IDs and Physical Asset IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_jobs;i=6008",
                browseName="ns=isa95_jobcontrol_v2;WorkMaster",
                description="Defines a read-only set of work master IDs that may be specified in a job order, and the read-only set of parameters that may be specified for a specific work master.",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95WorkMasterDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(o6.ns["ns=machinery_jobs;i=6009"]),
    ],
)
o6.reference(machinery_jobs_objtypes.JobManagementType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_jobs;i=5001"])
ns0.vartypes.PropertyType(
    nodeId="ns=machinery_jobs;i=6014",
    browseName="EnumValues",
    parent="ns=machinery_jobs;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("SimulationMode"), description=o6.LocalizedText("Machine running in simulation mode with no workpiece involved.")
        ),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("TestMode"), description=o6.LocalizedText("Machine running in test mode with a workpiece involved.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("ProductionMode"), description=o6.LocalizedText("Machine running in production mode.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machinery_jobs;i=6019",
    browseName="EnumValues",
    parent="ns=machinery_jobs;i=3006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("Unknown"), description=o6.LocalizedText("Unknown state. Used when result is not known, e.g. because job order is still running.")
        ),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Successful"), description=o6.LocalizedText("Job order was executed successful")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Unsuccessful"), description=o6.LocalizedText("Job order was not executed successful.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machinery_jobs;i=6020",
    browseName="OptionSetValues",
    parent="ns=machinery_jobs;i=3009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("OrderNumber"), o6.LocalizedText("LotNumber"), o6.LocalizedText("SerialNumber")],
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machinery_jobs;i=6021", browseName="ns=machinery_jobs;OutputInformationDataType", dataType=o6.String, value="OutputInformationDataType"
)
o6.reference(o6.ns["ns=machinery_jobs;i=5003"], "i=39", o6.ns["ns=machinery_jobs;i=6021"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machinery_jobs;i=6022", browseName="ns=machinery_jobs;OutputInformationDataType", dataType=o6.String, value="//xs:element[@name='OutputInformationDataType']"
)
o6.reference(o6.ns["ns=machinery_jobs;i=5004"], "i=39", o6.ns["ns=machinery_jobs;i=6022"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machinery_jobs;i=6023", browseName="ns=machinery_jobs;BOMComponentInformationDataType", dataType=o6.String, value="BOMComponentInformationDataType"
)
o6.reference(o6.ns["ns=machinery_jobs;i=5005"], "i=39", o6.ns["ns=machinery_jobs;i=6023"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machinery_jobs;i=6024",
    browseName="ns=machinery_jobs;BOMComponentInformationDataType",
    dataType=o6.String,
    value="//xs:element[@name='BOMComponentInformationDataType']",
)
o6.reference(o6.ns["ns=machinery_jobs;i=5006"], "i=39", o6.ns["ns=machinery_jobs;i=6024"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=machinery_jobs;i=6025", browseName="ns=machinery_jobs;BOMInformationDataType", dataType=o6.String, value="BOMInformationDataType")
o6.reference(o6.ns["ns=machinery_jobs;i=5007"], "i=39", o6.ns["ns=machinery_jobs;i=6025"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machinery_jobs;i=6026", browseName="ns=machinery_jobs;BOMInformationDataType", dataType=o6.String, value="//xs:element[@name='BOMInformationDataType']"
)
o6.reference(o6.ns["ns=machinery_jobs;i=5008"], "i=39", o6.ns["ns=machinery_jobs;i=6026"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machinery_jobs;i=6027", browseName="ns=machinery_jobs;OutputPerformanceInfoDataType", dataType=o6.String, value="OutputPerformanceInfoDataType"
)
o6.reference(o6.ns["ns=machinery_jobs;i=5009"], "i=39", o6.ns["ns=machinery_jobs;i=6027"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=machinery_jobs;i=6015",
    browseName="ns=machinery_jobs;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Machinery/Jobs/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machinery_jobs;i=6016", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Machinery/Jobs/")
        ),
        o6.hasComponent(o6.ns["ns=machinery_jobs;i=6021"]),
        o6.hasComponent(o6.ns["ns=machinery_jobs;i=6023"]),
        o6.hasComponent(o6.ns["ns=machinery_jobs;i=6025"]),
        o6.hasComponent(o6.ns["ns=machinery_jobs;i=6027"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/Machinery/Jobs/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ns1="http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/Machinery/Jobs/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:Import Namespace="http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BOMComponentInformationDataType">\n  <opc:Field TypeName="tns:OutputInformationDataType" Name="Identification"/>\n  <opc:Field TypeName="opc:Double" Name="Quantity"/>\n  <opc:Field TypeName="ua:EUInformation" Name="EngineeringUnits"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BOMInformationDataType">\n  <opc:Field TypeName="tns:OutputInformationDataType" Name="Identification"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfComponentInformation"/>\n  <opc:Field LengthField="NoOfComponentInformation" TypeName="tns:BOMComponentInformationDataType" Name="ComponentInformation"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="OutputInformationDataType">\n  <opc:Field TypeName="opc:Bit" Name="OrderNumberSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="LotNumberSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SerialNumberSpecified"/>\n  <opc:Field Length="29" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="ItemNumber"/>\n  <opc:Field TypeName="tns:OutputInfoType" Name="OutputInfo"/>\n  <opc:Field SwitchField="OrderNumberSpecified" TypeName="opc:CharArray" Name="OrderNumber"/>\n  <opc:Field SwitchField="LotNumberSpecified" TypeName="opc:CharArray" Name="LotNumber"/>\n  <opc:Field SwitchField="SerialNumberSpecified" TypeName="opc:CharArray" Name="SerialNumber"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="OutputPerformanceInfoDataType">\n  <opc:Field TypeName="opc:Bit" Name="StartTimeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="EndTimeSpecified"/>\n  <opc:Field Length="30" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="tns:OutputInformationDataType" Name="Identification"/>\n  <opc:Field SwitchField="StartTimeSpecified" TypeName="opc:DateTime" Name="StartTime"/>\n  <opc:Field SwitchField="EndTimeSpecified" TypeName="opc:DateTime" Name="EndTime"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfParameters"/>\n  <opc:Field LengthField="NoOfParameters" TypeName="ns1:ISA95ParameterDataType" Name="Parameters"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="JobExecutionMode">\n  <opc:EnumeratedValue Name="SimulationMode" Value="0"/>\n  <opc:EnumeratedValue Name="TestMode" Value="1"/>\n  <opc:EnumeratedValue Name="ProductionMode" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="JobResult">\n  <opc:EnumeratedValue Name="Unknown" Value="0"/>\n  <opc:EnumeratedValue Name="Successful" Value="1"/>\n  <opc:EnumeratedValue Name="Unsuccessful" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ProcessIrregularity">\n  <opc:EnumeratedValue Name="CapabilityUnavailable" Value="0"/>\n  <opc:EnumeratedValue Name="Detected" Value="1"/>\n  <opc:EnumeratedValue Name="NotDetected" Value="2"/>\n  <opc:EnumeratedValue Name="NotYetDetermined" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="8" Name="OutputInfoType" IsOptionSet="true">\n  <opc:EnumeratedValue Name="OrderNumber" Value="0"/>\n  <opc:EnumeratedValue Name="LotNumber" Value="1"/>\n  <opc:EnumeratedValue Name="SerialNumber" Value="2"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machinery_jobs;i=6028", browseName="ns=machinery_jobs;OutputPerformanceInfoDataType", dataType=o6.String, value="//xs:element[@name='OutputPerformanceInfoDataType']"
)
o6.reference(o6.ns["ns=machinery_jobs;i=5010"], "i=39", o6.ns["ns=machinery_jobs;i=6028"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=machinery_jobs;i=6017",
    browseName="ns=machinery_jobs;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Machinery/Jobs/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_jobs;i=6018", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Machinery/Jobs/Types.xsd"
            )
        ),
        o6.hasComponent(o6.ns["ns=machinery_jobs;i=6022"]),
        o6.hasComponent(o6.ns["ns=machinery_jobs;i=6024"]),
        o6.hasComponent(o6.ns["ns=machinery_jobs;i=6026"]),
        o6.hasComponent(o6.ns["ns=machinery_jobs;i=6028"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/Machinery/Jobs/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/Machinery/Jobs/Types.xsd" xmlns:ns1="http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:import namespace="http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/Types.xsd"/>\n <xs:simpleType name="JobExecutionMode">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="SimulationMode_0"/>\n   <xs:enumeration value="TestMode_1"/>\n   <xs:enumeration value="ProductionMode_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:JobExecutionMode" name="JobExecutionMode"/>\n <xs:complexType name="ListOfJobExecutionMode">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:JobExecutionMode" name="JobExecutionMode" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfJobExecutionMode" name="ListOfJobExecutionMode" nillable="true"/>\n <xs:simpleType name="JobResult">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Unknown_0"/>\n   <xs:enumeration value="Successful_1"/>\n   <xs:enumeration value="Unsuccessful_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:JobResult" name="JobResult"/>\n <xs:complexType name="ListOfJobResult">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:JobResult" name="JobResult" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfJobResult" name="ListOfJobResult" nillable="true"/>\n <xs:simpleType name="ProcessIrregularity">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="CapabilityUnavailable_0"/>\n   <xs:enumeration value="Detected_1"/>\n   <xs:enumeration value="NotDetected_2"/>\n   <xs:enumeration value="NotYetDetermined_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ProcessIrregularity" name="ProcessIrregularity"/>\n <xs:complexType name="ListOfProcessIrregularity">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ProcessIrregularity" name="ProcessIrregularity" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfProcessIrregularity" name="ListOfProcessIrregularity" nillable="true"/>\n <xs:complexType name="BOMComponentInformationDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:OutputInformationDataType" name="Identification"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Quantity"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:EUInformation" name="EngineeringUnits"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BOMComponentInformationDataType" name="BOMComponentInformationDataType"/>\n <xs:complexType name="ListOfBOMComponentInformationDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BOMComponentInformationDataType" name="BOMComponentInformationDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBOMComponentInformationDataType" name="ListOfBOMComponentInformationDataType" nillable="true"/>\n <xs:complexType name="BOMInformationDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:OutputInformationDataType" name="Identification"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfBOMComponentInformationDataType" name="ComponentInformation"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BOMInformationDataType" name="BOMInformationDataType"/>\n <xs:complexType name="ListOfBOMInformationDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BOMInformationDataType" name="BOMInformationDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBOMInformationDataType" name="ListOfBOMInformationDataType" nillable="true"/>\n <xs:complexType name="OutputInformationDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ItemNumber"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="OutputInfo"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="OrderNumber"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="LotNumber"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="SerialNumber"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:OutputInformationDataType" name="OutputInformationDataType"/>\n <xs:complexType name="ListOfOutputInformationDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OutputInformationDataType" name="OutputInformationDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOutputInformationDataType" name="ListOfOutputInformationDataType" nillable="true"/>\n <xs:complexType name="OutputPerformanceInfoDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:OutputInformationDataType" name="Identification"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="StartTime"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="EndTime"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ns1:ListOfISA95ParameterDataType" name="Parameters"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:OutputPerformanceInfoDataType" name="OutputPerformanceInfoDataType"/>\n <xs:complexType name="ListOfOutputPerformanceInfoDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OutputPerformanceInfoDataType" name="OutputPerformanceInfoDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOutputPerformanceInfoDataType" name="ListOfOutputPerformanceInfoDataType" nillable="true"/>\n</xs:schema>\n',
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMachinerySlashJobsSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=machinery_jobs;i=5011",
    browseName="ns=machinery_jobs;http://opcfoundation.org/UA/Machinery/Jobs/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_jobs;i=6029", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machinery_jobs;i=6030", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2024-05-01T00:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machinery_jobs;i=6031", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Machinery/Jobs/")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_jobs;i=6032", browseName="NamespaceVersion", dataType=o6.String, value="1.0.1")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_jobs;i=6033",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_jobs;i=6034", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_jobs;i=6035", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.PropertyType(
    nodeId="ns=machinery_jobs;i=6036",
    browseName="EnumValues",
    parent="ns=machinery_jobs;i=3004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("CapabilityUnavailable"),
            description=o6.LocalizedText("The machine is not able to give a statement about process irregularities."),
        ),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Detected"), description=o6.LocalizedText("A process irregularity has been detected.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("NotDetected"), description=o6.LocalizedText("There was no process irregularity detected.")),
        ns0.datatypes.EnumValueType(
            value=3, displayName=o6.LocalizedText("NotYetDetermined"), description=o6.LocalizedText("A statement about the process irregularity is to be expected.")
        ),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=machinery_jobs;i=6011",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_jobs;i=7001",
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
    nodeId="ns=machinery_jobs;i=6012",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_jobs;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobResponse",
            dataType=o6.NodeId("ns=amb;i=3013"),
            valueRank=-1,
            description=o6.LocalizedText(
                "Contains information about the execution of a job order, such as the current status of the job, actual material consumed, actual material produced, actual equipment used, and job specific data."
            ),
        ),
        ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")),
    ],
)
o6.call(
    nodeId="ns=machinery_jobs;i=7001",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderID",
    inputArgs=o6.hasProperty(o6.ns["ns=machinery_jobs;i=6011"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machinery_jobs;i=6012"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machinery_jobs;i=6037",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_jobs;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="JobOrderState",
            dataType=o6.NodeId("ns=amb;i=3006"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "Contains a job status of the JobResponse to be returned. The array shall provide at least one entry representing the top level state and potentially additional entries representing substates. The first entry shall be the top level entry, having the BrowsePath set to null. The order of the substates is not defined."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machinery_jobs;i=6038",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_jobs;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobResponses",
            dataType=o6.NodeId("ns=amb;i=3013"),
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
    nodeId="ns=machinery_jobs;i=7002",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderState",
    inputArgs=o6.hasProperty(o6.ns["ns=machinery_jobs;i=6037"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machinery_jobs;i=6038"]),
)

isa95_jobcontrol_v2.objtypes.ISA95JobResponseProviderObjectType(
    nodeId="ns=machinery_jobs;i=5002",
    browseName="ns=machinery_jobs;JobOrderResults",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=machinery_jobs;i=7001"]), o6.hasComponent(o6.ns["ns=machinery_jobs;i=7002"])],
)
o6.reference(machinery_jobs_objtypes.JobManagementType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_jobs;i=5002"])


del Any, TYPE_CHECKING, uuid, o6, isa95_jobcontrol_v2, ns0, machinery_jobs_datypes, machinery_jobs_objtypes
