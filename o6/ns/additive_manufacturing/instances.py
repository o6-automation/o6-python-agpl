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

"""Generated OPC UA additive_manufacturing namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.irdi as irdi
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machine_tool as machine_tool
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.machinery_processvalues as machinery_processvalues
import o6.ns.ns0 as ns0
import o6.ns.padim as padim
from . import datatypes as additive_manufacturing_datypes
from . import objtypes as additive_manufacturing_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

additive_manufacturing_objtypes.EquipmentAMType(
    nodeId="ns=additive_manufacturing;i=5007",
    browseName="ns=machine_tool;Equipment",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(additive_manufacturing_objtypes.FeedstockListType(nodeId="ns=additive_manufacturing;i=5005", browseName="ns=additive_manufacturing;Feedstock")),
        o6.hasComponent(machine_tool.objtypes.ToolListType(nodeId="ns=additive_manufacturing;i=5015", browseName="ns=machine_tool;Tools")),
    ],
)
o6.reference(additive_manufacturing_objtypes.AdditiveManufacturingType, ns0.reftypes.HasComponent, o6.ns["ns=additive_manufacturing;i=5007"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=additive_manufacturing;i=5036", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=additive_manufacturing;i=5037", browseName="Default XML")
o6.hasEncoding(additive_manufacturing_datypes.RunInfoDataType, o6.ns["ns=additive_manufacturing;i=5037"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=additive_manufacturing;i=5038", browseName="Default JSON")
o6.hasEncoding(additive_manufacturing_datypes.RunInfoDataType, o6.ns["ns=additive_manufacturing;i=5038"])
ns0.vartypes.PropertyType(
    nodeId="ns=additive_manufacturing;i=6001",
    browseName="EnumValues",
    parent="ns=additive_manufacturing;i=3000",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Undefined"), description=o6.LocalizedText("The function of the feedstock is unknown.", "en")),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("Main"), description=o6.LocalizedText("The feedstock is used for production and is part of the finished part.", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("Ancillary"), description=o6.LocalizedText("The feedstock is used for production but removed before the part is finished.", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=3, displayName=o6.LocalizedText("Consumable"), description=o6.LocalizedText("The feedstock is consumed during the production e.g., process gas.")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=additive_manufacturing;i=6006",
    browseName="EnumValues",
    parent="ns=additive_manufacturing;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("Info"), description=o6.LocalizedText("This sensor&#8217;s current value is not critical for the overall production.", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("Critical"), description=o6.LocalizedText("This sensor&#8217;s current value is critical for the overall production.", "en")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=additive_manufacturing;i=6007",
    browseName="EnumValues",
    parent="ns=additive_manufacturing;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("MachineHealth"),
            description=o6.LocalizedText("The sensor is mainly relevant to indicate the current AM machine&#8217;s health.", "en"),
        ),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("MaintenanceTracking"), description=o6.LocalizedText("The sensor is mainly relevant to track serviceable components.", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("ProcessMonitoring"), description=o6.LocalizedText("The sensor is mainly relevant to monitor the production operability.", "en")
        ),
    ],
)
machine_tool.objtypes.MachineOperationMonitoringType(
    nodeId="ns=additive_manufacturing;i=5006",
    browseName="ns=machine_tool;MachineTool",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=additive_manufacturing;i=6016", browseName="ns=machine_tool;OperationMode", dataType=machine_tool.datatypes.MachineOperationMode
            )
        )
    ],
)
machine_tool.objtypes.MonitoringType(
    nodeId="ns=additive_manufacturing;i=5001",
    browseName="ns=machine_tool;Monitoring",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=additive_manufacturing;i=5006"]),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=additive_manufacturing;i=5009", browseName="ns=machinery;Process")),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=additive_manufacturing;i=5010", browseName="ns=machinery;Health")),
    ],
)
o6.reference(additive_manufacturing_objtypes.AdditiveManufacturingType, ns0.reftypes.HasComponent, o6.ns["ns=additive_manufacturing;i=5001"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=additive_manufacturing;i=6017",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=additive_manufacturing;i=6018", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=additive_manufacturing;i=6014",
    browseName="ns=additive_manufacturing;RemainingQuantity",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=additive_manufacturing;i=6033", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(additive_manufacturing_objtypes.FeedstockType, ns0.reftypes.HasComponent, o6.ns["ns=additive_manufacturing;i=6014"])
additive_manufacturing_objtypes.FeedstockType(
    nodeId="ns=additive_manufacturing;i=5004",
    browseName="ns=additive_manufacturing;Feedstock",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=additive_manufacturing;i=6065", browseName="ns=additive_manufacturing;Identifier", dataType=o6.String, accessLevel=3, userAccessLevel=1
            )
        )
    ],
)
additive_manufacturing_objtypes.FeedstockListType(
    nodeId="ns=additive_manufacturing;i=5003",
    browseName="ns=additive_manufacturing;Feedstock",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=additive_manufacturing;i=5004"])],
)
o6.reference(additive_manufacturing_objtypes.EquipmentAMType, ns0.reftypes.HasComponent, o6.ns["ns=additive_manufacturing;i=5003"])
isa95_jobcontrol_v2.objtypes.ISA95JobOrderReceiverObjectType(
    nodeId="ns=additive_manufacturing;i=5013",
    browseName="ns=machinery_jobs;JobOrderControl",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=additive_manufacturing;i=6023", browseName="ns=isa95_jobcontrol_v2;MaxDownloadableJobOrders", dataType=o6.UInt16)),
        o6.hasComponent(o6.ns["ns=additive_manufacturing;i=6017"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=additive_manufacturing;i=6019",
                browseName="ns=isa95_jobcontrol_v2;EquipmentID",
                description="Defines a read-only set of Equipment Class IDs and Equipment IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=additive_manufacturing;i=6020",
                browseName="ns=isa95_jobcontrol_v2;JobOrderList",
                description="Defines a read-only list of job order information available from the server.",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95JobOrderAndStateDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=additive_manufacturing;i=6021",
                browseName="ns=isa95_jobcontrol_v2;MaterialClassID",
                description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=additive_manufacturing;i=6022",
                browseName="ns=isa95_jobcontrol_v2;MaterialDefinitionID",
                description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=additive_manufacturing;i=6024",
                browseName="ns=isa95_jobcontrol_v2;PersonnelID",
                description="Defines a read-only set of Personnel IDs and Person IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=additive_manufacturing;i=6025",
                browseName="ns=isa95_jobcontrol_v2;PhysicalAssetID",
                description="Defines a read-only set of Physical Asset Class IDs and Physical Asset IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=additive_manufacturing;i=6066",
                browseName="ns=isa95_jobcontrol_v2;WorkMaster",
                description="Defines a read-only set of work master IDs that may be specified in a job order, and the read-only set of parameters that may be specified for a specific work master.",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95WorkMasterDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
    ],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=additive_manufacturing;i=6071", browseName="ns=additive_manufacturing;RunInfoDataType", dataType=o6.String, value="RunInfoDataType")
o6.reference(o6.ns["ns=additive_manufacturing;i=5036"], "i=39", o6.ns["ns=additive_manufacturing;i=6071"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=additive_manufacturing;i=6002",
    browseName="ns=additive_manufacturing;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/AdditiveManufacturing/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=additive_manufacturing;i=6003", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/AdditiveManufacturing/"
            )
        ),
        o6.hasComponent(o6.ns["ns=additive_manufacturing;i=6071"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/AdditiveManufacturing/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ns1="http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/AdditiveManufacturing/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:Import Namespace="http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RunInfoDataType">\n  <opc:Field TypeName="opc:Bit" Name="CurrentLayerSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="RemainingTimeSpecified"/>\n  <opc:Field Length="30" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field SwitchField="CurrentLayerSpecified" TypeName="opc:UInt32" Name="CurrentLayer"/>\n  <opc:Field TypeName="opc:CharArray" Name="Identifier"/>\n  <opc:Field TypeName="ns1:ISA95StateDataType" Name="State"/>\n  <opc:Field SwitchField="RemainingTimeSpecified" TypeName="opc:Double" Name="RemainingTime"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="FeedstockFunction">\n  <opc:Documentation>This enumeration indicates the function of a specific feedstock.</opc:Documentation>\n  <opc:EnumeratedValue Name="Undefined" Value="0"/>\n  <opc:EnumeratedValue Name="Main" Value="1"/>\n  <opc:EnumeratedValue Name="Ancillary" Value="2"/>\n  <opc:EnumeratedValue Name="Consumable" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="SensorCategory">\n  <opc:Documentation>This enumeration indicates the severity of a specific sensor.</opc:Documentation>\n  <opc:EnumeratedValue Name="MachineHealth" Value="0"/>\n  <opc:EnumeratedValue Name="MaintenanceTracking" Value="1"/>\n  <opc:EnumeratedValue Name="ProcessMonitoring" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="SensorSeverity">\n  <opc:Documentation>This enumeration indicates the severity of a specific sensor.</opc:Documentation>\n  <opc:EnumeratedValue Name="Info" Value="0"/>\n  <opc:EnumeratedValue Name="Critical" Value="1"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=additive_manufacturing;i=6072", browseName="ns=additive_manufacturing;RunInfoDataType", dataType=o6.String, value="//xs:element[@name='RunInfoDataType']"
)
o6.reference(o6.ns["ns=additive_manufacturing;i=5037"], "i=39", o6.ns["ns=additive_manufacturing;i=6072"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=additive_manufacturing;i=6004",
    browseName="ns=additive_manufacturing;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/AdditiveManufacturing/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=additive_manufacturing;i=6005", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/AdditiveManufacturing/Types.xsd"
            )
        ),
        o6.hasComponent(o6.ns["ns=additive_manufacturing;i=6072"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/AdditiveManufacturing/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/AdditiveManufacturing/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:ns7="http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:import namespace="http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/Types.xsd"/>\n <xs:simpleType name="FeedstockFunction">\n  <xs:annotation>\n   <xs:documentation>This enumeration indicates the function of a specific feedstock.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Undefined_0"/>\n   <xs:enumeration value="Main_1"/>\n   <xs:enumeration value="Ancillary_2"/>\n   <xs:enumeration value="Consumable_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:FeedstockFunction" name="FeedstockFunction"/>\n <xs:complexType name="ListOfFeedstockFunction">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:FeedstockFunction" name="FeedstockFunction" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfFeedstockFunction" name="ListOfFeedstockFunction" nillable="true"/>\n <xs:simpleType name="SensorCategory">\n  <xs:annotation>\n   <xs:documentation>This enumeration indicates the severity of a specific sensor.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="MachineHealth_0"/>\n   <xs:enumeration value="MaintenanceTracking_1"/>\n   <xs:enumeration value="ProcessMonitoring_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:SensorCategory" name="SensorCategory"/>\n <xs:complexType name="ListOfSensorCategory">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SensorCategory" name="SensorCategory" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSensorCategory" name="ListOfSensorCategory" nillable="true"/>\n <xs:simpleType name="SensorSeverity">\n  <xs:annotation>\n   <xs:documentation>This enumeration indicates the severity of a specific sensor.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Info_0"/>\n   <xs:enumeration value="Critical_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:SensorSeverity" name="SensorSeverity"/>\n <xs:complexType name="ListOfSensorSeverity">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SensorSeverity" name="SensorSeverity" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSensorSeverity" name="ListOfSensorSeverity" nillable="true"/>\n <xs:complexType name="RunInfoDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="CurrentLayer"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Identifier"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ns7:ISA95StateDataType" name="State"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="RemainingTime"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RunInfoDataType" name="RunInfoDataType"/>\n <xs:complexType name="ListOfRunInfoDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RunInfoDataType" name="RunInfoDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRunInfoDataType" name="ListOfRunInfoDataType" nillable="true"/>\n</xs:schema>\n',
)
additive_manufacturing_objtypes.MachineIdentificationAMType(
    nodeId="ns=additive_manufacturing;i=5008",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=additive_manufacturing;i=6079", browseName="ns=additive_manufacturing;AMTechnologyIdentifier", dataType=o6.String, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=additive_manufacturing;i=6080",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=additive_manufacturing;i=6081",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=additive_manufacturing;i=6082",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(additive_manufacturing_objtypes.AdditiveManufacturingType, ns0.reftypes.HasAddIn, o6.ns["ns=additive_manufacturing;i=5008"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=additive_manufacturing;i=6077",
    browseName="ns=additive_manufacturing;RemainingQuantity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=additive_manufacturing;i=6099", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
additive_manufacturing_objtypes.FeedstockType(
    nodeId="ns=additive_manufacturing;i=5002",
    browseName="ns=additive_manufacturing;<Feedstock>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=additive_manufacturing;i=6026", browseName="ns=additive_manufacturing;Identifier", dataType=o6.String, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=additive_manufacturing;i=6028", browseName="ns=additive_manufacturing;ExternalIdentifier", dataType=o6.String, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=additive_manufacturing;i=6030", browseName="ns=additive_manufacturing;Manufacturer", dataType=o6.String, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=additive_manufacturing;i=6031", browseName="ns=additive_manufacturing;Name", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=additive_manufacturing;i=6027", browseName="ns=additive_manufacturing;Cycle", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=additive_manufacturing;i=6029",
                browseName="ns=additive_manufacturing;Function",
                dataType=additive_manufacturing_datypes.FeedstockFunction,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=additive_manufacturing;i=6032", browseName="ns=additive_manufacturing;ReadyForProduction", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=additive_manufacturing;i=6077"]),
    ],
)
o6.reference(additive_manufacturing_objtypes.FeedstockListType, ns0.reftypes.HasComponent, o6.ns["ns=additive_manufacturing;i=5002"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashAdditiveManufacturingSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=additive_manufacturing;i=5016",
    browseName="ns=additive_manufacturing;http://opcfoundation.org/UA/AdditiveManufacturing/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=additive_manufacturing;i=6100", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=additive_manufacturing;i=6101", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2025-02-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=additive_manufacturing;i=6102", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/AdditiveManufacturing/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=additive_manufacturing;i=6104", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=additive_manufacturing;i=6105",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=additive_manufacturing;i=6106", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=additive_manufacturing;i=6107", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)


ns0.vartypes.PropertyType(
    nodeId="ns=additive_manufacturing;i=6067",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=additive_manufacturing;i=7001",
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
    nodeId="ns=additive_manufacturing;i=6068",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=additive_manufacturing;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobResponse",
            dataType=o6.NodeId("ns=dexpi;i=3013"),
            valueRank=-1,
            description=o6.LocalizedText(
                "Contains information about the execution of a job order, such as the current status of the job, actual material consumed, actual material produced, actual equipment used, and job specific data."
            ),
        ),
        ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")),
    ],
)
o6.call(
    nodeId="ns=additive_manufacturing;i=7001",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderID",
    inputArgs=o6.hasProperty(o6.ns["ns=additive_manufacturing;i=6067"]),
    outputArgs=o6.hasProperty(o6.ns["ns=additive_manufacturing;i=6068"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=additive_manufacturing;i=6069",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=additive_manufacturing;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="JobOrderState",
            dataType=o6.NodeId("ns=dexpi;i=3006"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "Contains a job status of the JobResponse to be returned. The array shall provide at least one entry representing the top level state and potentially additional entries representing substates. The first entry shall be the top level entry, having the BrowsePath set to null. The order of the substates is not defined."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=additive_manufacturing;i=6070",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=additive_manufacturing;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobResponses",
            dataType=o6.NodeId("ns=dexpi;i=3013"),
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
    nodeId="ns=additive_manufacturing;i=7002",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderState",
    inputArgs=o6.hasProperty(o6.ns["ns=additive_manufacturing;i=6069"]),
    outputArgs=o6.hasProperty(o6.ns["ns=additive_manufacturing;i=6070"]),
)

isa95_jobcontrol_v2.objtypes.ISA95JobResponseProviderObjectType(
    nodeId="ns=additive_manufacturing;i=5014",
    browseName="ns=machinery_jobs;JobOrderResults",
    references=[o6.hasComponent(o6.ns["ns=additive_manufacturing;i=7001"]), o6.hasComponent(o6.ns["ns=additive_manufacturing;i=7002"])],
)
machinery_jobs.objtypes.JobManagementType(
    nodeId="ns=additive_manufacturing;i=5012",
    browseName="ns=machinery_jobs;JobManagement",
    references=[o6.hasComponent(o6.ns["ns=additive_manufacturing;i=5013"]), o6.hasComponent(o6.ns["ns=additive_manufacturing;i=5014"])],
)
ns0.objtypes.FolderType(
    nodeId="ns=additive_manufacturing;i=5011",
    browseName="ns=machinery;MachineryBuildingBlocks",
    modellingRule="Optional",
    references=[o6.hasAddIn(o6.ns["ns=additive_manufacturing;i=5012"])],
)
o6.reference(additive_manufacturing_objtypes.AdditiveManufacturingType, ns0.reftypes.HasComponent, o6.ns["ns=additive_manufacturing;i=5011"])


del (
    Any,
    TYPE_CHECKING,
    uuid,
    o6,
    di,
    ia,
    irdi,
    isa95_jobcontrol_v2,
    machine_tool,
    machinery,
    machinery_jobs,
    machinery_processvalues,
    ns0,
    padim,
    additive_manufacturing_datypes,
    additive_manufacturing_objtypes,
)
