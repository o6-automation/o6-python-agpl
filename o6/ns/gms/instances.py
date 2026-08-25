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

"""Generated OPC UA gms namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machine_tool as machine_tool
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.machinery_result as machinery_result
import o6.ns.ns0 as ns0
from . import datatypes as gms_datypes
from . import vartypes as gms_vartypes
from . import objtypes as gms_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=gms;i=5007", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=gms;i=5008", browseName="Default XML")
o6.hasEncoding(gms_datypes.CartesianWorkspaceType, o6.ns["ns=gms;i=5008"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=gms;i=5009", browseName="Default JSON")
o6.hasEncoding(gms_datypes.CartesianWorkspaceType, o6.ns["ns=gms;i=5009"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=gms;i=5013", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=gms;i=5014", browseName="Default XML")
o6.hasEncoding(gms_datypes.CylindricalWorkspaceType, o6.ns["ns=gms;i=5014"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=gms;i=5020", browseName="Default JSON")
o6.hasEncoding(gms_datypes.CylindricalWorkspaceType, o6.ns["ns=gms;i=5020"])
gms_objtypes.GMSEquipmentType(
    nodeId="ns=gms;i=5010",
    browseName="ns=machine_tool;Equipment",
    modellingRule="Mandatory",
    references=[o6.hasComponent(machine_tool.objtypes.ToolListType(nodeId="ns=gms;i=5022", browseName="ns=machine_tool;Tools"))],
)
o6.reference(gms_objtypes.GMSType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=5010"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=gms;i=6006",
    browseName="CurrentState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6007", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6008", browseName="Number", dataType=o6.UInt32)),
    ],
    dataType=o6.LocalizedText,
    value=o6.LocalizedText(),
)
machine_tool.objtypes.ProductionProgramStateMachineType(nodeId="ns=gms;i=5006", browseName="ns=machine_tool;State", references=[o6.hasComponent(o6.ns["ns=gms;i=6006"])])
machine_tool.objtypes.ProductionActiveProgramType(
    nodeId="ns=gms;i=5005",
    browseName="ns=machine_tool;ActiveProgram",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6004", browseName="ns=machine_tool;Name", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6005", browseName="NumberInList", dataType=o6.UInt16)),
        o6.hasComponent(o6.ns["ns=gms;i=5006"]),
    ],
)
machine_tool.objtypes.ProductionType(
    nodeId="ns=gms;i=5012", browseName="ns=machine_tool;Production", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=gms;i=5005"])]
)
o6.reference(gms_objtypes.GMSType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=5012"])
machine_tool.objtypes.MachineOperationMonitoringType(
    nodeId="ns=gms;i=5027",
    browseName="ns=machine_tool;MachineTool",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=gms;i=6017", browseName="ns=machine_tool;OperationMode", dataType=machine_tool.datatypes.MachineOperationMode))
    ],
)
gms_objtypes.GMSMonitoringType(nodeId="ns=gms;i=5026", browseName="ns=machine_tool;Monitoring", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=gms;i=5027"])])
o6.reference(gms_objtypes.GMSType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=5026"])
ns0.vartypes.PropertyType(
    nodeId="ns=gms;i=6022",
    browseName="EnumStrings",
    parent="ns=gms;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("Qualified"), o6.LocalizedText("Imprecise"), o6.LocalizedText("NotQualified")],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=gms;i=6044",
    browseName="ns=gms;Nominal",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6045", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gms_objtypes.CharacteristicType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=6044"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=gms;i=6048",
    browseName="ns=gms;Class",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6049",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[12],
                value=[
                    o6.LocalizedText("Other", "0"),
                    o6.LocalizedText("NoTool", "1"),
                    o6.LocalizedText("UnDefTool"),
                    o6.LocalizedText("TactileTouchTrigger"),
                    o6.LocalizedText("TactileMeasuring"),
                    o6.LocalizedText("Optical-1D"),
                    o6.LocalizedText("Optical-2D"),
                    o6.LocalizedText("Optical-3D"),
                    o6.LocalizedText("Roughness"),
                    o6.LocalizedText("Eddy Current Sensor"),
                    o6.LocalizedText("TemperatureProbing"),
                    o6.LocalizedText("PtMeas"),
                ],
            )
        )
    ],
    dataType=ns0.datatypes.UInteger,
    accessLevel=3,
    userAccessLevel=1,
)
# WARNING: The source NodeSet value does not match the declared DataType.
# It is intentionally omitted; the server supplies a typed default.
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=gms;i=6054",
    browseName="ns=machine_tool;Locked",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6055", browseName="ns=machine_tool;ReasonForLocking", dataType=machine_tool.datatypes.ToolLocked))],
    dataType=o6.Boolean,
)
gms_objtypes.SensorType(
    nodeId="ns=gms;i=5023",
    browseName="ns=gms;<Tool>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(ns0.objtypes.BaseObjectType(nodeId="ns=gms;i=5045", browseName="ns=machine_tool;ToolLife")),
        o6.hasComponent(o6.ns["ns=gms;i=6048"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=gms;i=6052", browseName="ns=machine_tool;ControlIdentifier1", dataType=o6.UInt32)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=gms;i=6053", browseName="ns=machine_tool;ControlIdentifierInterpretation", dataType=machine_tool.datatypes.ToolManagement)
        ),
        o6.hasComponent(o6.ns["ns=gms;i=6054"]),
    ],
)
o6.reference(gms_objtypes.MultiSensorType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=5023"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=gms;i=6056",
    browseName="ns=gms;Class",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6057",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[12],
                value=[
                    o6.LocalizedText("Other", "0"),
                    o6.LocalizedText("NoTool", "1"),
                    o6.LocalizedText("UnDefTool"),
                    o6.LocalizedText("TactileTouchTrigger"),
                    o6.LocalizedText("TactileMeasuring"),
                    o6.LocalizedText("Optical-1D"),
                    o6.LocalizedText("Optical-2D"),
                    o6.LocalizedText("Optical-3D"),
                    o6.LocalizedText("Roughness"),
                    o6.LocalizedText("Eddy Current Sensor"),
                    o6.LocalizedText("TemperatureProbing"),
                    o6.LocalizedText("PtMeas"),
                ],
            )
        )
    ],
    dataType=ns0.datatypes.UInteger,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gms_objtypes.SensorType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=6056"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=gms;i=6039",
    browseName="ns=gms;ResultValue",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6059", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gms_objtypes.CharacteristicType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=6039"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=gms;i=6066", browseName="ns=gms;CartesianWorkspaceType", dataType=o6.String, value="CartesianWorkspaceType")
o6.reference(o6.ns["ns=gms;i=5007"], "i=39", o6.ns["ns=gms;i=6066"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=gms;i=6067", browseName="ns=gms;CartesianWorkspaceType", dataType=o6.String, value="//xs:element[@name='CartesianWorkspaceType']")
o6.reference(o6.ns["ns=gms;i=5008"], "i=39", o6.ns["ns=gms;i=6067"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=gms;i=6069", browseName="ns=gms;CylindricalWorkspaceType", dataType=o6.String, value="CylindricalWorkspaceType")
o6.reference(o6.ns["ns=gms;i=5013"], "i=39", o6.ns["ns=gms;i=6069"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=gms;i=6023",
    browseName="ns=gms;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/GMS/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6024", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/GMS/")),
        o6.hasComponent(o6.ns["ns=gms;i=6066"]),
        o6.hasComponent(o6.ns["ns=gms;i=6069"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/GMS/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/GMS/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="WorkspaceType"/>\n <opc:StructuredType BaseType="tns:WorkspaceType" Name="CartesianWorkspaceType">\n  <opc:Field TypeName="opc:Double" Name="Length"/>\n  <opc:Field TypeName="opc:Double" Name="Width"/>\n  <opc:Field TypeName="opc:Double" Name="Height"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:WorkspaceType" Name="CylindricalWorkspaceType">\n  <opc:Field TypeName="opc:Double" Name="Length"/>\n  <opc:Field TypeName="opc:Double" Name="Radius"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="MeasurementReasonEnum">\n  <opc:EnumeratedValue Name="ContinuousMeasurements" Value="0"/>\n  <opc:EnumeratedValue Name="SpecialMeasurement" Value="1"/>\n  <opc:EnumeratedValue Name="AuditMeasurement" Value="2"/>\n  <opc:EnumeratedValue Name="MinMastering" Value="3"/>\n  <opc:EnumeratedValue Name="MedMastering" Value="4"/>\n  <opc:EnumeratedValue Name="MaxMastering" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ToleranceLimitEnum">\n  <opc:EnumeratedValue Name="NoLimit" Value="0"/>\n  <opc:EnumeratedValue Name="LimitValue" Value="1"/>\n  <opc:EnumeratedValue Name="NaturalLimit" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ToolAlignmentState">\n  <opc:EnumeratedValue Name="Fixed" Value="0"/>\n  <opc:EnumeratedValue Name="Indexed" Value="1"/>\n  <opc:EnumeratedValue Name="Continuous" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ToolIsQualifiedStatus">\n  <opc:EnumeratedValue Name="Qualified" Value="0"/>\n  <opc:EnumeratedValue Name="Imprecise" Value="1"/>\n  <opc:EnumeratedValue Name="NotQualified" Value="2"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=gms;i=6071", browseName="ns=gms;CylindricalWorkspaceType", dataType=o6.String, value="//xs:element[@name='CylindricalWorkspaceType']"
)
o6.reference(o6.ns["ns=gms;i=5014"], "i=39", o6.ns["ns=gms;i=6071"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=gms;i=6025",
    browseName="ns=gms;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/GMS/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6026", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/GMS/Types.xsd")),
        o6.hasComponent(o6.ns["ns=gms;i=6067"]),
        o6.hasComponent(o6.ns["ns=gms;i=6071"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/GMS/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/GMS/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="MeasurementReasonEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="ContinuousMeasurements_0"/>\n   <xs:enumeration value="SpecialMeasurement_1"/>\n   <xs:enumeration value="AuditMeasurement_2"/>\n   <xs:enumeration value="MinMastering_3"/>\n   <xs:enumeration value="MedMastering_4"/>\n   <xs:enumeration value="MaxMastering_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:MeasurementReasonEnum" name="MeasurementReasonEnum"/>\n <xs:complexType name="ListOfMeasurementReasonEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:MeasurementReasonEnum" name="MeasurementReasonEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfMeasurementReasonEnum" name="ListOfMeasurementReasonEnum" nillable="true"/>\n <xs:simpleType name="ToleranceLimitEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="NoLimit_0"/>\n   <xs:enumeration value="LimitValue_1"/>\n   <xs:enumeration value="NaturalLimit_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ToleranceLimitEnum" name="ToleranceLimitEnum"/>\n <xs:complexType name="ListOfToleranceLimitEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ToleranceLimitEnum" name="ToleranceLimitEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfToleranceLimitEnum" name="ListOfToleranceLimitEnum" nillable="true"/>\n <xs:simpleType name="ToolAlignmentState">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Fixed_0"/>\n   <xs:enumeration value="Indexed_1"/>\n   <xs:enumeration value="Continuous_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ToolAlignmentState" name="ToolAlignmentState"/>\n <xs:complexType name="ListOfToolAlignmentState">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ToolAlignmentState" name="ToolAlignmentState" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfToolAlignmentState" name="ListOfToolAlignmentState" nillable="true"/>\n <xs:simpleType name="ToolIsQualifiedStatus">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Qualified_0"/>\n   <xs:enumeration value="Imprecise_1"/>\n   <xs:enumeration value="NotQualified_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ToolIsQualifiedStatus" name="ToolIsQualifiedStatus"/>\n <xs:complexType name="ListOfToolIsQualifiedStatus">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ToolIsQualifiedStatus" name="ToolIsQualifiedStatus" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfToolIsQualifiedStatus" name="ListOfToolIsQualifiedStatus" nillable="true"/>\n <xs:complexType name="WorkspaceType">\n  <xs:sequence/>\n </xs:complexType>\n <xs:element type="tns:WorkspaceType" name="WorkspaceType"/>\n <xs:complexType name="ListOfWorkspaceType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WorkspaceType" name="WorkspaceType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWorkspaceType" name="ListOfWorkspaceType" nillable="true"/>\n <xs:complexType name="CartesianWorkspaceType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Length"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Width"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Height"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CartesianWorkspaceType" name="CartesianWorkspaceType"/>\n <xs:complexType name="ListOfCartesianWorkspaceType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CartesianWorkspaceType" name="CartesianWorkspaceType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCartesianWorkspaceType" name="ListOfCartesianWorkspaceType" nillable="true"/>\n <xs:complexType name="CylindricalWorkspaceType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Length"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Radius"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CylindricalWorkspaceType" name="CylindricalWorkspaceType"/>\n <xs:complexType name="ListOfCylindricalWorkspaceType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CylindricalWorkspaceType" name="CylindricalWorkspaceType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCylindricalWorkspaceType" name="ListOfCylindricalWorkspaceType" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=gms;i=6010",
    browseName="ns=gms;CorrectionValueRelative",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6072", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gms_objtypes.CorrectionType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=6010"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=gms;i=6074",
    browseName="ns=gms;CorrectionValueAbsolute",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6075", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gms_objtypes.CorrectionType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=6074"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=gms;i=6076",
    browseName="ns=gms;UpperControlLimit",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6077", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gms_objtypes.CorrectionType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=6076"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=gms;i=6080",
    browseName="ns=gms;LowerControlLimit",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6081", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gms_objtypes.CorrectionType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=6080"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=gms;i=6019",
    browseName="ns=gms;Capabilities",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6083",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[6],
                value=[
                    o6.LocalizedText("Other"),
                    o6.LocalizedText("PtMeas"),
                    o6.LocalizedText("PtMeasSelfCenter"),
                    o6.LocalizedText("FeatureExtract"),
                    o6.LocalizedText("ProfileScan"),
                    o6.LocalizedText("ArealScan"),
                ],
            )
        )
    ],
    dataType=ns0.datatypes.UInteger,
    valueRank=1,
    arrayDimensions=[0],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gms_objtypes.SensorType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=6019"])
ns0.vartypes.PropertyType(
    nodeId="ns=gms;i=6086",
    browseName="EnumStrings",
    parent="ns=gms;i=3009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        o6.LocalizedText("ContinuousMeasurements"),
        o6.LocalizedText("SpecialMeasurement"),
        o6.LocalizedText("AuditMeasurement"),
        o6.LocalizedText("MinMastering"),
        o6.LocalizedText("MedMastering"),
        o6.LocalizedText("MaxMastering"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gms;i=6103",
    browseName="EnumStrings",
    parent="ns=gms;i=3010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("NoLimit"), o6.LocalizedText("LimitValue"), o6.LocalizedText("NaturalLimit")],
)
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=gms;i=6027",
    browseName="ns=gms;Class",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6104",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[4],
                value=[o6.LocalizedText("Other"), o6.LocalizedText("Temperature"), o6.LocalizedText("Vibration"), o6.LocalizedText("Humidity")],
            )
        )
    ],
    dataType=ns0.datatypes.UInteger,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gms_vartypes.AdditionalSensorType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=6027"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=gms;i=6088",
    browseName="ns=gms;Class",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6105", browseName="EnumStrings", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0], value=[]))],
    dataType=ns0.datatypes.UInteger,
    accessLevel=3,
    userAccessLevel=1,
)
gms_vartypes.AdditionalSensorType(
    nodeId="ns=gms;i=6087",
    browseName="ns=gms;<AdditionalSensor>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6089", browseName="ns=gms;Identifier", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6090", browseName="ns=gms;Name", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6091", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasComponent(o6.ns["ns=gms;i=6088"]),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(nodeId="ns=gms;i=5015", browseName="ns=gms;AdditionalSensor", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=gms;i=6087"])])
o6.reference(gms_objtypes.GMSEquipmentType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=5015"])
gms_objtypes.ToolMonitoringType(
    nodeId="ns=gms;i=5032",
    browseName="ns=gms;ToolMonitoring",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6106", browseName="ns=machine_tool;Name", dataType=o6.String))],
)
o6.reference(gms_objtypes.GMSMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=5032"])
gms_objtypes.CalibrationPrognosisType(
    nodeId="ns=gms;i=5001",
    browseName="ns=gms;Calibration",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6003", browseName="ns=gms;Calibrated", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=gms;i=6011", browseName="ns=gms;CalibrationPreptime", dataType=ns0.datatypes.Duration, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=gms;i=6013", browseName="ns=gms;CalibrationInterval", dataType=ns0.datatypes.Duration, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6014", browseName="ns=gms;DateOfCalibration", dataType=ns0.datatypes.UtcTime, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=gms;i=6015", browseName="ns=machine_tool;PredictedTime", dataType=ns0.datatypes.UtcTime, value=o6.DateTime("2000-01-01T00:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6110", browseName="ns=gms;CalibrationCertificate", dataType=o6.String, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
            )
        ),
    ],
)
machine_tool.objtypes.PrognosisListType(nodeId="ns=gms;i=5030", browseName="ns=machine_tool;Prognoses", references=[o6.hasComponent(o6.ns["ns=gms;i=5001"])])
machine_tool.objtypes.NotificationType(
    nodeId="ns=gms;i=5029", browseName="ns=machine_tool;Notification", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=gms;i=5030"])]
)
o6.reference(gms_objtypes.GMSType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=5029"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=gms;i=6060",
    browseName="ns=gms;LoadStatus",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6112",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[4],
                value=[o6.LocalizedText("Unknown"), o6.LocalizedText("Empty"), o6.LocalizedText("Filled"), o6.LocalizedText("InProgress")],
            )
        )
    ],
    dataType=ns0.datatypes.UInteger,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gms_objtypes.LoadingMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=6060"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=gms;i=6113",
    browseName="ns=gms;LoadStatus",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6115",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[4],
                value=[o6.LocalizedText("Unknown"), o6.LocalizedText("Empty"), o6.LocalizedText("Filled"), o6.LocalizedText("InProgress")],
            )
        )
    ],
    dataType=ns0.datatypes.UInteger,
    accessLevel=3,
    userAccessLevel=1,
)
gms_objtypes.LoadingMonitoringType(
    nodeId="ns=gms;i=5031",
    browseName="ns=gms;LoadingMonitoring",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6070", browseName="ns=machine_tool;Name", dataType=o6.String)), o6.hasComponent(o6.ns["ns=gms;i=6113"])],
)
o6.reference(gms_objtypes.GMSMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=5031"])
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=gms;i=6073",
    browseName="ns=gms;IsInLoadingPosition",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6116", browseName="FalseState", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6117", browseName="TrueState", dataType=o6.LocalizedText)),
    ],
    dataType=o6.Boolean,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gms_objtypes.LoadingMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=6073"])
gms_objtypes.CorrectionType(
    nodeId="ns=gms;i=5018",
    browseName="ns=gms;<Corrections>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6036", browseName="ns=gms;Identifier", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6118", browseName="ns=gms;CharacteristicIdentifier", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
)
gms_objtypes.CorrectionType(
    nodeId="ns=gms;i=5028",
    browseName="ns=gms;<Corrections>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6051", browseName="ns=gms;Identifier", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6120", browseName="ns=gms;CharacteristicIdentifier", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
)
ns0.objtypes.FolderType(nodeId="ns=gms;i=5021", browseName="ns=gms;CorrectionsFolder", references=[o6.hasComponent(o6.ns["ns=gms;i=5028"])])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=gms;i=5036",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6128",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6129",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
o6.reference(gms_objtypes.RotaryTableType, ns0.reftypes.HasAddIn, o6.ns["ns=gms;i=5036"])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=gms;i=5037",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6130",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6131",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
gms_objtypes.RotaryTableType(
    nodeId="ns=gms;i=5035",
    browseName="ns=gms;<RotaryTable>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6108", browseName="ns=gms;IsIntegrated", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6109", browseName="ns=gms;NumberOfAxes", dataType=o6.Byte, accessLevel=3, userAccessLevel=1)),
        o6.hasAddIn(o6.ns["ns=gms;i=5037"]),
    ],
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=gms;i=5038",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6132",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6133",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
o6.reference(gms_objtypes.SensorExchangeRackType, ns0.reftypes.HasAddIn, o6.ns["ns=gms;i=5038"])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=gms;i=5039",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6135",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6136",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
o6.reference(gms_objtypes.TipExchangeRackType, ns0.reftypes.HasAddIn, o6.ns["ns=gms;i=5039"])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=gms;i=5041",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6138",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6139",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
gms_objtypes.SensorExchangeRackType(
    nodeId="ns=gms;i=5040",
    browseName="ns=gms;<SensorExchangeRack>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6140", browseName="ns=gms;IsAvailable", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasAddIn(o6.ns["ns=gms;i=5041"]),
    ],
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=gms;i=5043",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6141",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6142",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
gms_objtypes.TipExchangeRackType(
    nodeId="ns=gms;i=5042",
    browseName="ns=gms;<TipExchangeRack>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6143", browseName="ns=gms;IsAvailable", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasAddIn(o6.ns["ns=gms;i=5043"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=gms;i=5034",
    browseName="ns=gms;Accessories",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=gms;i=5035"]), o6.hasComponent(o6.ns["ns=gms;i=5040"]), o6.hasComponent(o6.ns["ns=gms;i=5042"])],
)
o6.reference(gms_objtypes.GMSEquipmentType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=5034"])
ns0.objtypes.FolderType(
    nodeId="ns=gms;i=5016",
    browseName="ns=gms;CorrectionsFolder",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=gms;i=5018"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=gms;i=6144", browseName="ns=gms;CorrectionCount", dataType=ns0.datatypes.Integer, accessLevel=3, userAccessLevel=1)
        ),
    ],
)
o6.reference(gms_objtypes.GMSResultManagementType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=5016"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=gms;i=6042",
    browseName="ns=gms;LowerToleranceLimit",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6043", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=gms;i=6145", browseName="ns=gms;ToleranceForm", dataType=gms_datypes.ToleranceLimitEnum, accessLevel=3, userAccessLevel=1)
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gms_objtypes.CharacteristicType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=6042"])
machinery_result.vartypes.ResultType(
    nodeId="ns=gms;i=6058",
    browseName="ns=machinery_result;ResultVariable",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=gms;i=6146", browseName="ns=machinery_result;ResultMetaData", dataType=machinery_result.datatypes.ResultMetaDataType, accessLevel=3, userAccessLevel=1
            ),
            "i=24136",
        )
    ],
    dataType=machinery_result.datatypes.ResultDataType,
    value=machinery_result.datatypes.ResultDataType(
        resultMetaData=machinery_result.datatypes.ResultMetaDataType(
            resultId="",
            hasTransferableDataOnFile=None,
            isPartial=None,
            isSimulated=None,
            resultState=None,
            stepId=None,
            partId=None,
            externalRecipeId=None,
            internalRecipeId=None,
            productId=None,
            externalConfigurationId=None,
            internalConfigurationId=None,
            jobId=None,
            creationTime=None,
            processingTimes=None,
            resultUri=[],
            resultEvaluation=None,
            resultEvaluationCode=None,
            resultEvaluationDetails=None,
            fileFormat=[],
        ),
        resultContent=[],
    ),
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(nodeId="ns=gms;i=5025", browseName="ns=machinery_result;Results", references=[o6.hasComponent(o6.ns["ns=gms;i=6058"])])
gms_objtypes.GMSIdentificationType(
    nodeId="ns=gms;i=5044",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6147",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6148",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6149",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(gms_objtypes.GMSType, ns0.reftypes.HasAddIn, o6.ns["ns=gms;i=5044"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=gms;i=6040",
    browseName="ns=gms;UpperToleranceLimit",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6041", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=gms;i=6150", browseName="ns=gms;ToleranceForm", dataType=gms_datypes.ToleranceLimitEnum, accessLevel=3, userAccessLevel=1)
        ),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gms_objtypes.CharacteristicType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=6040"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashGMSSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=gms;i=5057",
    browseName="ns=gms;http://opcfoundation.org/UA/GMS/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=gms;i=6293", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6294", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2023-07-01T00:00:00Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6295", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/GMS/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6296", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6297", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=gms;i=6298", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6299", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.PropertyType(
    nodeId="ns=gms;i=6302",
    browseName="EnumStrings",
    parent="ns=gms;i=3004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("Fixed"), o6.LocalizedText("Indexed"), o6.LocalizedText("Continuous")],
)
gms_vartypes.CatalogType(
    nodeId="ns=gms;i=6316",
    browseName="ns=gms;NestIdentifier",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6317", browseName="ns=gms;CatalogEntry", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6318", browseName="ns=gms;CatalogName", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6319", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6320", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gms_objtypes.GMSPartType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=6316"])
gms_vartypes.CatalogType(
    nodeId="ns=gms;i=6321",
    browseName="ns=gms;Operator",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6322", browseName="ns=gms;CatalogEntry", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6323", browseName="ns=gms;CatalogName", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6324", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6325", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gms_objtypes.GMSPartType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=6321"])
gms_vartypes.CatalogType(
    nodeId="ns=gms;i=6326",
    browseName="ns=gms;ProcessParameter",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6327", browseName="ns=gms;CatalogEntry", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6328", browseName="ns=gms;CatalogName", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6329", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6330", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=1,
    arrayDimensions=[0],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gms_objtypes.GMSPartType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=6326"])
gms_vartypes.CatalogType(
    nodeId="ns=gms;i=6331",
    browseName="ns=gms;PartCarrierIdentifier",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6332", browseName="ns=gms;CatalogEntry", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6333", browseName="ns=gms;CatalogName", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6334", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6335", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gms_objtypes.GMSPartType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=6331"])
gms_vartypes.CatalogType(
    nodeId="ns=gms;i=6336",
    browseName="ns=gms;ProcessingMachineIdentifier",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6337", browseName="ns=gms;CatalogEntry", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6338", browseName="ns=gms;CatalogName", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6339", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6340", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(gms_objtypes.GMSPartType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=6336"])
machine_tool.vartypes.ToolLifeType(
    nodeId="ns=gms;i=6341",
    browseName="ns=gms;Qualified",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6342", browseName="ns=machine_tool;EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=gms;i=6343",
                browseName="ns=machine_tool;Indication",
                dataType=machine_tool.datatypes.ToolLifeIndication,
                value=machine_tool.datatypes.ToolLifeIndication.TIME,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=gms;i=6344", browseName="ns=machine_tool;IsCountingUp", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6345", browseName="ns=machine_tool;LimitValue", dataType=ns0.datatypes.Number)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6346", browseName="ns=machine_tool;StartValue", dataType=ns0.datatypes.Number)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6347", browseName="ns=machine_tool;WarningValue", dataType=ns0.datatypes.Number)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.BaseObjectType(nodeId="ns=gms;i=5065", browseName="ns=machine_tool;ToolLife", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=gms;i=6341"])])
o6.reference(gms_objtypes.SensorType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=5065"])


ns0.vartypes.PropertyType(
    nodeId="ns=gms;i=6032",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gms;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Timeout",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the client can give a hint to the server how long it will need access to the result data.\nA value &gt; 0 indicates an estimated maximum time for processing the data in milliseconds. \nA value = 0 indicates that the client will not need anything besides the data returned by the method call.\nA value &lt; 0 indicates that the client cannot give an estimate.\nThe client cannot rely on the data being available during the indicated time period. The argument is merely a hint allowing the server to optimize its resource management."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gms;i=6033",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gms;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ResultHandle",
            dataType=ns0.datatypes.Handle,
            valueRank=-1,
            description=o6.LocalizedText(
                "The server shall return to each client requesting result data a system-wide unique handle identifying the result set / client combination. This handle should be used by the client to indicate to the server that the result data is no longer needed, allowing the server to optimize its resource handling.\nIf the instance of ResultManagementType does not support the ReleaseResultHandle Method, the resultHandle should always be set to 0.\nIf the error is set to a value other than 0, the resultHandle may be set to 0.\n"
            ),
        ),
        ns0.datatypes.Argument(name="Result", dataType=o6.NodeId("ns=machinery_result;i=3008"), valueRank=-1, description=o6.LocalizedText("The result including metadata.")),
        ns0.datatypes.Argument(
            name="Error",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors.\n"
            ),
        ),
    ],
)
o6.call(
    nodeId="ns=gms;i=7001", browseName="ns=machinery_result;GetLatestResult", inputArgs=o6.hasProperty(o6.ns["ns=gms;i=6032"]), outputArgs=o6.hasProperty(o6.ns["ns=gms;i=6033"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=gms;i=6034",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gms;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ResultId", dataType=ns0.datatypes.TrimmedString, valueRank=-1, description=o6.LocalizedText("System-wide unique identifier for the result.")),
        ns0.datatypes.Argument(
            name="Timeout",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the client can give a hint to the server how long it will need access to the result data.\nA value &gt; 0 indicates an estimated maximum time for processing the data in milliseconds. \nA value = 0 indicates that the client will not need anything besides the data returned by the method call.\nA value &lt; 0 indicates that the client cannot give an estimate.\nThe client cannot rely on the data being available during the indicated time period. The argument is merely a hint allowing the server to optimize its resource management."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gms;i=6037",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gms;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ResultHandle",
            dataType=ns0.datatypes.Handle,
            valueRank=-1,
            description=o6.LocalizedText(
                "The server shall return to each client requesting result data a system-wide unique handle identifying the result set / client combination. This handle should be used by the client to indicate to the server that the result data is no longer needed, allowing the server to optimize its resource handling.\nIf the instance of ResultManagementType does not support the ReleaseResultHandle Method, the resultHandle should always be set to 0.\nIf the error is set to a value other than 0, the resultHandle may be set to 0."
            ),
        ),
        ns0.datatypes.Argument(
            name="Result",
            dataType=o6.NodeId("ns=machinery_result;i=3008"),
            valueRank=-1,
            description=o6.LocalizedText("The result including metadata. May be set to Null, if error is set to a value other than 0."),
        ),
        ns0.datatypes.Argument(
            name="Error",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors."
            ),
        ),
    ],
)
o6.call(
    nodeId="ns=gms;i=7002",
    browseName="ns=machinery_result;GetResultById",
    description="The server shall return to each client requesting result data a system-wide unique handle identifying the result set / client combination. This handle should be used by the client to indicate to the server that the result data is no longer needed, allowing the server to optimize its resource handling.\nIf the instance of ResultManagementType does not support the ReleaseResultHandle Method, the resultHandle should always be set to 0.\nIf the error is set to a value other than 0, the resultHandle may be set to 0.",
    inputArgs=o6.hasProperty(o6.ns["ns=gms;i=6034"]),
    outputArgs=o6.hasProperty(o6.ns["ns=gms;i=6037"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gms;i=6092",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gms;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(
            name="Filter",
            dataType=ns0.datatypes.ContentFilter,
            valueRank=-1,
            description=o6.LocalizedText(
                "Filter used to filter for specific results based on the meta data of the results. Valid BrowsePaths used in the filter can be built from the fields of the ResultReadyEventType, the ResultType VariableType or the ResultDataType or corresponding subtypes."
            ),
        ),
        ns0.datatypes.Argument(
            name="OrderedBy",
            dataType=ns0.datatypes.RelativePath,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "An array of BrowsePaths (as array of QualifiedName) identifying the ordering criteria for the results. If the array is null or empty, no ordering is executed.\nIf several BrowsePaths are provided, the first entry in the array is used as first ordering criteria, etc.\n"
            ),
        ),
        ns0.datatypes.Argument(
            name="MaxResults",
            dataType=o6.UInt32,
            valueRank=-1,
            description=o6.LocalizedText("Defines how many resultIds the Client wants to receive at most. If no maximum should be provided, it is set to 0."),
        ),
        ns0.datatypes.Argument(
            name="Timeout",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the client can give a hint to the server how long it will need access to the result data.\nA value &gt; 0 indicates an estimated maximum time for processing the data in milliseconds. \nA value = 0 indicates that the client will not need anything besides the data returned by the method call.\nA value &lt; 0 indicates that the client cannot give an estimate.\nThe client cannot rely on the data being available during the indicated time period. The argument is merely a hint allowing the server to optimize its resource management."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gms;i=6093",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gms;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ResultHandle",
            dataType=ns0.datatypes.Handle,
            valueRank=-1,
            description=o6.LocalizedText(
                "The server shall return to each client requesting result data a system-wide unique handle identifying the result set / client combination. This handle has to be used by the client to release the result set.\nIf the instance of ResultManagementType does not support the ReleaseResultHandle Method, the resultHandle should always be set to 0.\nIf the error is set to a value other than 0, the resultHandle may be set to 0.\n"
            ),
        ),
        ns0.datatypes.Argument(
            name="ResultIdList",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("List of resultIds of results matching the Filter."),
        ),
        ns0.datatypes.Argument(
            name="Error",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors."
            ),
        ),
    ],
)
o6.call(
    nodeId="ns=gms;i=7003",
    browseName="ns=machinery_result;GetResultIdListFiltered",
    inputArgs=o6.hasProperty(o6.ns["ns=gms;i=6092"]),
    outputArgs=o6.hasProperty(o6.ns["ns=gms;i=6093"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gms;i=6094",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gms;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ResultHandle",
            dataType=ns0.datatypes.Handle,
            valueRank=-1,
            description=o6.LocalizedText("Handle returned by GetResultById or GetResultIdListFiltered, identifying the result set/client combination."),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gms;i=6095",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gms;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Error",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors."
            ),
        )
    ],
)
o6.call(
    nodeId="ns=gms;i=7004",
    browseName="ns=machinery_result;ReleaseResultHandle",
    inputArgs=o6.hasProperty(o6.ns["ns=gms;i=6094"]),
    outputArgs=o6.hasProperty(o6.ns["ns=gms;i=6095"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=gms;i=6097",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gms;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gms;i=6098",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gms;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=gms;i=7005", browseName="CloseAndCommit", inputArgs=o6.hasProperty(o6.ns["ns=gms;i=6097"]), outputArgs=o6.hasProperty(o6.ns["ns=gms;i=6098"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gms;i=6099",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gms;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="GenerateOptions",
            dataType=o6.NodeId("ns=machinery_result;i=3005"),
            valueRank=-1,
            description=o6.LocalizedText("Options how to generate the file, including the resultId of the result the file belongs to. "),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gms;i=6100",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gms;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1, description=o6.LocalizedText("NodeId of the temporary file.")),
        ns0.datatypes.Argument(
            name="FileHandle",
            dataType=o6.UInt32,
            valueRank=-1,
            description=o6.LocalizedText("The FileHandle of the opened TransferFile.\nThe FileHandle can be used to access the TransferFile methods Read and Close.\n"),
        ),
        ns0.datatypes.Argument(
            name="CompletionStateMachine",
            dataType=o6.NodeId,
            valueRank=-1,
            description=o6.LocalizedText(
                "If the creation of the file is completed asynchronously, the parameter returns the NodeId of the corresponding FileTransferStateMachineType Object.\nIf the creation of the file is already completed, the parameter is null.\nIf a FileTransferStateMachineType object NodeId is returned, the Read Method of the file fails until the TransferState changed to ReadTransfer.\n"
            ),
        ),
    ],
)
o6.call(nodeId="ns=gms;i=7006", browseName="GenerateFileForRead", inputArgs=o6.hasProperty(o6.ns["ns=gms;i=6099"]), outputArgs=o6.hasProperty(o6.ns["ns=gms;i=6100"]))

ns0.vartypes.PropertyType(
    nodeId="ns=gms;i=6101",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=gms;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=ns0.datatypes.BaseDataType, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=gms;i=6102",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=gms;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=gms;i=7007", browseName="GenerateFileForWrite", inputArgs=o6.hasProperty(o6.ns["ns=gms;i=6101"]), outputArgs=o6.hasProperty(o6.ns["ns=gms;i=6102"]))

machinery_result.objtypes.ResultTransferType(
    nodeId="ns=gms;i=5024",
    browseName="ns=machinery_result;ResultTransfer",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=gms;i=6096", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=gms;i=7005"]),
        o6.hasComponent(o6.ns["ns=gms;i=7006"]),
        o6.hasComponent(o6.ns["ns=gms;i=7007"]),
    ],
)
gms_objtypes.GMSResultManagementType(
    nodeId="ns=gms;i=5019",
    browseName="ns=gms;ResultManagement",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=gms;i=5021"]),
        o6.hasComponent(o6.ns["ns=gms;i=5024"]),
        o6.hasComponent(o6.ns["ns=gms;i=5025"]),
        o6.hasComponent(o6.ns["ns=gms;i=7001"]),
        o6.hasComponent(o6.ns["ns=gms;i=7002"]),
        o6.hasComponent(o6.ns["ns=gms;i=7003"]),
        o6.hasComponent(o6.ns["ns=gms;i=7004"]),
    ],
)
o6.reference(gms_objtypes.GMSType, ns0.reftypes.HasComponent, o6.ns["ns=gms;i=5019"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machine_tool, machinery, machinery_jobs, machinery_result, ns0, gms_datypes, gms_vartypes, gms_objtypes
