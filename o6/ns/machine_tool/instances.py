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

"""Generated OPC UA machine_tool namespace declarations."""

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
from . import datatypes as machine_tool_datypes
from . import vartypes as machine_tool_vartypes
from . import objtypes as machine_tool_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

machine_tool_objtypes.EquipmentType(
    nodeId="ns=machine_tool;i=131",
    browseName="ns=machine_tool;Equipment",
    modellingRule="Mandatory",
    references=[o6.hasComponent(machine_tool_objtypes.ToolListType(nodeId="ns=machine_tool;i=146", browseName="ns=machine_tool;Tools"))],
)
o6.reference(machine_tool_objtypes.MachineToolType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=131"])
ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=190",
    browseName="EnumValues",
    parent="ns=machine_tool;i=62",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("CapabilityUnavailable"),
            description=o6.LocalizedText("The machine tool is not able to give a statement about process irregularities.", "en"),
        ),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Detected"), description=o6.LocalizedText("A process irregularity has been detected.", "en")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("NotDetected"), description=o6.LocalizedText("There was no process irregularity detected.", "en")),
        ns0.datatypes.EnumValueType(
            value=3, displayName=o6.LocalizedText("NotYetDetermined"), description=o6.LocalizedText("A statement about the process irregularity is to be expected.", "en")
        ),
    ],
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=machine_tool;i=192",
    browseName="ns=machine_tool;RunsPlanned",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=188", browseName="ns=machine_tool;IsValid", dataType=o6.Boolean))],
    dataType=o6.UInt32,
)
o6.reference(machine_tool_objtypes.ProductionJobType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=192"])
machine_tool_objtypes.SoftwareIdentificationType(
    nodeId="ns=machine_tool;i=103",
    browseName="ns=machine_tool;<SoftwareItem>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=187", browseName="ns=di;SoftwareRevision", dataType=o6.String, value="0")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=205", browseName="ns=machine_tool;Identifier", dataType=o6.String, value="0")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_tool;i=85", browseName="ns=machine_tool;SoftwareIdentification", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=machine_tool;i=103"])]
)
o6.reference(machine_tool_objtypes.MachineToolIdentificationType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=85"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=machine_tool;i=221",
    browseName="ns=machine_tool;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/MachineTool/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=222", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/MachineTool/"))
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/MachineTool/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/MachineTool/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:EnumeratedType LengthInBits="32" Name="ChannelMode">\n  <opc:EnumeratedValue Name="Automatic" Value="0"/>\n  <opc:EnumeratedValue Name="MdaMdi" Value="1"/>\n  <opc:EnumeratedValue Name="JogManual" Value="2"/>\n  <opc:EnumeratedValue Name="JogIncrement" Value="3"/>\n  <opc:EnumeratedValue Name="TeachingHandle" Value="4"/>\n  <opc:EnumeratedValue Name="Remote" Value="5"/>\n  <opc:EnumeratedValue Name="Reference" Value="6"/>\n  <opc:EnumeratedValue Name="Other" Value="7"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ChannelState">\n  <opc:EnumeratedValue Name="Active" Value="0"/>\n  <opc:EnumeratedValue Name="Interrupted" Value="1"/>\n  <opc:EnumeratedValue Name="Reset" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="EDMGeneratorState">\n  <opc:EnumeratedValue Name="Undefined" Value="0"/>\n  <opc:EnumeratedValue Name="Ready" Value="1"/>\n  <opc:EnumeratedValue Name="Active_Low_Voltage" Value="2"/>\n  <opc:EnumeratedValue Name="Active_High_Voltage" Value="3"/>\n  <opc:EnumeratedValue Name="Error" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="LaserState">\n  <opc:EnumeratedValue Name="Undefined" Value="0"/>\n  <opc:EnumeratedValue Name="Ready" Value="1"/>\n  <opc:EnumeratedValue Name="Active" Value="2"/>\n  <opc:EnumeratedValue Name="Error" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="MachineOperationMode">\n  <opc:EnumeratedValue Name="Manual" Value="0"/>\n  <opc:EnumeratedValue Name="Automatic" Value="1"/>\n  <opc:EnumeratedValue Name="Setup" Value="2"/>\n  <opc:EnumeratedValue Name="AutoWithManualIntervention" Value="3"/>\n  <opc:EnumeratedValue Name="Service" Value="4"/>\n  <opc:EnumeratedValue Name="Other" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PartQuality">\n  <opc:EnumeratedValue Name="CapabilityUnavailable" Value="0"/>\n  <opc:EnumeratedValue Name="Good" Value="1"/>\n  <opc:EnumeratedValue Name="Bad" Value="2"/>\n  <opc:EnumeratedValue Name="NotYetMeasured" Value="3"/>\n  <opc:EnumeratedValue Name="WillNotBeMeasured" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ProcessIrregularity">\n  <opc:EnumeratedValue Name="CapabilityUnavailable" Value="0"/>\n  <opc:EnumeratedValue Name="Detected" Value="1"/>\n  <opc:EnumeratedValue Name="NotDetected" Value="2"/>\n  <opc:EnumeratedValue Name="NotYetDetermined" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ToolLifeIndication">\n  <opc:EnumeratedValue Name="Time" Value="0"/>\n  <opc:EnumeratedValue Name="NumberOfParts" Value="1"/>\n  <opc:EnumeratedValue Name="NumberOfUsages" Value="2"/>\n  <opc:EnumeratedValue Name="Feed_Distance" Value="3"/>\n  <opc:EnumeratedValue Name="Cutting_Distance" Value="4"/>\n  <opc:EnumeratedValue Name="Length" Value="5"/>\n  <opc:EnumeratedValue Name="Diameter" Value="6"/>\n  <opc:EnumeratedValue Name="Other" Value="7"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ToolLocked">\n  <opc:EnumeratedValue Name="CapabilityUnavailable" Value="0"/>\n  <opc:EnumeratedValue Name="ByOperator" Value="1"/>\n  <opc:EnumeratedValue Name="ToolBreak" Value="2"/>\n  <opc:EnumeratedValue Name="ToolLife" Value="3"/>\n  <opc:EnumeratedValue Name="MeasurementError" Value="4"/>\n  <opc:EnumeratedValue Name="Other" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ToolManagement">\n  <opc:EnumeratedValue Name="NumberBased" Value="0"/>\n  <opc:EnumeratedValue Name="GroupBased" Value="1"/>\n  <opc:EnumeratedValue Name="Other" Value="2"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=machine_tool;i=223",
    browseName="ns=machine_tool;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/MachineTool/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=224", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/MachineTool/Types.xsd")
        )
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/MachineTool/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/MachineTool/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="ChannelMode">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Automatic_0"/>\n   <xs:enumeration value="MdaMdi_1"/>\n   <xs:enumeration value="JogManual_2"/>\n   <xs:enumeration value="JogIncrement_3"/>\n   <xs:enumeration value="TeachingHandle_4"/>\n   <xs:enumeration value="Remote_5"/>\n   <xs:enumeration value="Reference_6"/>\n   <xs:enumeration value="Other_7"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ChannelMode" name="ChannelMode"/>\n <xs:complexType name="ListOfChannelMode">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ChannelMode" name="ChannelMode" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfChannelMode" name="ListOfChannelMode" nillable="true"/>\n <xs:simpleType name="ChannelState">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Active_0"/>\n   <xs:enumeration value="Interrupted_1"/>\n   <xs:enumeration value="Reset_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ChannelState" name="ChannelState"/>\n <xs:complexType name="ListOfChannelState">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ChannelState" name="ChannelState" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfChannelState" name="ListOfChannelState" nillable="true"/>\n <xs:simpleType name="EDMGeneratorState">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Undefined_0"/>\n   <xs:enumeration value="Ready_1"/>\n   <xs:enumeration value="Active_Low_Voltage_2"/>\n   <xs:enumeration value="Active_High_Voltage_3"/>\n   <xs:enumeration value="Error_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:EDMGeneratorState" name="EDMGeneratorState"/>\n <xs:complexType name="ListOfEDMGeneratorState">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:EDMGeneratorState" name="EDMGeneratorState" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfEDMGeneratorState" name="ListOfEDMGeneratorState" nillable="true"/>\n <xs:simpleType name="LaserState">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Undefined_0"/>\n   <xs:enumeration value="Ready_1"/>\n   <xs:enumeration value="Active_2"/>\n   <xs:enumeration value="Error_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:LaserState" name="LaserState"/>\n <xs:complexType name="ListOfLaserState">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:LaserState" name="LaserState" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfLaserState" name="ListOfLaserState" nillable="true"/>\n <xs:simpleType name="MachineOperationMode">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Manual_0"/>\n   <xs:enumeration value="Automatic_1"/>\n   <xs:enumeration value="Setup_2"/>\n   <xs:enumeration value="AutoWithManualIntervention_3"/>\n   <xs:enumeration value="Service_4"/>\n   <xs:enumeration value="Other_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:MachineOperationMode" name="MachineOperationMode"/>\n <xs:complexType name="ListOfMachineOperationMode">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:MachineOperationMode" name="MachineOperationMode" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfMachineOperationMode" name="ListOfMachineOperationMode" nillable="true"/>\n <xs:simpleType name="PartQuality">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="CapabilityUnavailable_0"/>\n   <xs:enumeration value="Good_1"/>\n   <xs:enumeration value="Bad_2"/>\n   <xs:enumeration value="NotYetMeasured_3"/>\n   <xs:enumeration value="WillNotBeMeasured_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PartQuality" name="PartQuality"/>\n <xs:complexType name="ListOfPartQuality">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PartQuality" name="PartQuality" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPartQuality" name="ListOfPartQuality" nillable="true"/>\n <xs:simpleType name="ProcessIrregularity">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="CapabilityUnavailable_0"/>\n   <xs:enumeration value="Detected_1"/>\n   <xs:enumeration value="NotDetected_2"/>\n   <xs:enumeration value="NotYetDetermined_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ProcessIrregularity" name="ProcessIrregularity"/>\n <xs:complexType name="ListOfProcessIrregularity">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ProcessIrregularity" name="ProcessIrregularity" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfProcessIrregularity" name="ListOfProcessIrregularity" nillable="true"/>\n <xs:simpleType name="ToolLifeIndication">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Time_0"/>\n   <xs:enumeration value="NumberOfParts_1"/>\n   <xs:enumeration value="NumberOfUsages_2"/>\n   <xs:enumeration value="Feed_Distance_3"/>\n   <xs:enumeration value="Cutting_Distance_4"/>\n   <xs:enumeration value="Length_5"/>\n   <xs:enumeration value="Diameter_6"/>\n   <xs:enumeration value="Other_7"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ToolLifeIndication" name="ToolLifeIndication"/>\n <xs:complexType name="ListOfToolLifeIndication">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ToolLifeIndication" name="ToolLifeIndication" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfToolLifeIndication" name="ListOfToolLifeIndication" nillable="true"/>\n <xs:simpleType name="ToolLocked">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="CapabilityUnavailable_0"/>\n   <xs:enumeration value="ByOperator_1"/>\n   <xs:enumeration value="ToolBreak_2"/>\n   <xs:enumeration value="ToolLife_3"/>\n   <xs:enumeration value="MeasurementError_4"/>\n   <xs:enumeration value="Other_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ToolLocked" name="ToolLocked"/>\n <xs:complexType name="ListOfToolLocked">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ToolLocked" name="ToolLocked" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfToolLocked" name="ListOfToolLocked" nillable="true"/>\n <xs:simpleType name="ToolManagement">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="NumberBased_0"/>\n   <xs:enumeration value="GroupBased_1"/>\n   <xs:enumeration value="Other_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ToolManagement" name="ToolManagement"/>\n <xs:complexType name="ListOfToolManagement">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ToolManagement" name="ToolManagement" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfToolManagement" name="ListOfToolManagement" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=227",
    browseName="EnumValues",
    parent="ns=machine_tool;i=63",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("CapabilityUnavailable"),
            description=o6.LocalizedText("The machine tool is not able to give a statement about the part quality.", "en"),
        ),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Good"), description=o6.LocalizedText("The part quality is determined good.", "en")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Bad"), description=o6.LocalizedText("The part quality is determined bad.", "en")),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("NotYetMeasured"),
            description=o6.LocalizedText("The PartQuality will still be determined in the machine tool to be either Good or Bad.", "en"),
        ),
        ns0.datatypes.EnumValueType(
            value=4, displayName=o6.LocalizedText("WillNotBeMeasured"), description=o6.LocalizedText("The machine tool will not give a statement about the part quality.", "en")
        ),
    ],
)
machine_tool_objtypes.ProductionPartSetType(
    nodeId="ns=machine_tool;i=94",
    browseName="ns=machine_tool;<PartSet>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=217", browseName="ns=machine_tool;ContainsMixedParts", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=228", browseName="ns=machine_tool;PartsCompletedPerRun", dataType=o6.UInt32)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=229", browseName="ns=machine_tool;PartsPlannedPerRun", dataType=o6.UInt32)),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_tool;i=72", browseName="ns=machine_tool;PartSets", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=machine_tool;i=94"])]
)
o6.reference(machine_tool_objtypes.ProductionJobType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=72"])
machine_tool_objtypes.ProductionStatisticsType(
    nodeId="ns=machine_tool;i=134",
    browseName="ns=machine_tool;Statistics",
    modellingRule="Optional",
    references=[o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=236", browseName="ns=machine_tool;PartsProducedInLifetime", dataType=o6.UInt32))],
)
o6.reference(machine_tool_objtypes.ProductionType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=134"])
machine_tool_objtypes.PrognosisType(
    nodeId="ns=machine_tool;i=89",
    browseName="ns=machine_tool;<Prognosis>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_tool;i=240", browseName="ns=machine_tool;PredictedTime", dataType=ns0.datatypes.UtcTime, value=o6.DateTime("2000-01-01T00:00:00Z")
            )
        )
    ],
    _allow_abstract=True,
)
o6.reference(machine_tool_objtypes.PrognosisListType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=89"])
machine_tool_objtypes.ProductionProgramType(
    nodeId="ns=machine_tool;i=77",
    browseName="<OrderedObject>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=197", browseName="ns=machine_tool;Name", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=242", browseName="NumberInList", dataType=o6.UInt16)),
    ],
)
ns0.objtypes.OrderedListType(
    nodeId="ns=machine_tool;i=75", browseName="ns=machine_tool;ProductionPrograms", modellingRule="Mandatory", references=[o6.hasOrderedComponent(o6.ns["ns=machine_tool;i=77"])]
)
o6.reference(machine_tool_objtypes.ProductionJobType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=75"])
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=machine_tool;i=233",
    browseName="ns=machine_tool;FeedOverride",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=237", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=252", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
o6.reference(machine_tool_objtypes.MachineOperationMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=233"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=machine_tool;i=245",
    browseName="ns=machine_tool;RunsPlanned",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=253", browseName="ns=machine_tool;IsValid", dataType=o6.Boolean))],
    dataType=o6.UInt32,
)
machine_tool_objtypes.ProductionProgramType(
    nodeId="ns=machine_tool;i=93",
    browseName="<OrderedObject>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=214", browseName="ns=machine_tool;Name", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=255", browseName="NumberInList", dataType=o6.UInt16)),
    ],
)
ns0.objtypes.OrderedListType(nodeId="ns=machine_tool;i=76", browseName="ns=machine_tool;ProductionPrograms", references=[o6.hasOrderedComponent(o6.ns["ns=machine_tool;i=93"])])
machine_tool_objtypes.ProductionPartType(
    nodeId="ns=machine_tool;i=112",
    browseName="ns=machine_tool;<Part>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=164", browseName="ns=machine_tool;Name", dataType=o6.String)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=168", browseName="ns=machine_tool;PartQuality", dataType=machine_tool_datypes.PartQuality)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=257", browseName="ns=machine_tool;ProcessIrregularity", dataType=machine_tool_datypes.ProcessIrregularity)
        ),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_tool;i=111", browseName="ns=machine_tool;PartsPerRun", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=machine_tool;i=112"])]
)
o6.reference(machine_tool_objtypes.ProductionPartSetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=111"])
machine_tool_objtypes.MachineToolIdentificationType(
    nodeId="ns=machine_tool;i=83",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=182", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=258", browseName="ns=di;ProductInstanceUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=259", browseName="ns=di;SerialNumber", dataType=o6.String)),
    ],
)
o6.reference(machine_tool_objtypes.MachineToolType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_tool;i=83"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_tool;i=239",
    browseName="CurrentState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=256", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=260", browseName="Number", dataType=o6.UInt32)),
    ],
    dataType=o6.LocalizedText,
)
machine_tool_objtypes.ProductionPartStateMachineType(
    nodeId="ns=machine_tool;i=101", browseName="ns=machine_tool;State", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=machine_tool;i=239"])]
)
o6.reference(machine_tool_objtypes.ProductionPartType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=101"])
ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=266",
    browseName="EnumValues",
    parent="ns=machine_tool;i=64",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("Active"), description=o6.LocalizedText("There is an active command being executed by the NC channel.", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("Interrupted"),
            description=o6.LocalizedText("The NC execution is interrupted. Execution of a program in the channel can be restarted.", "en"),
        ),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("Reset"), description=o6.LocalizedText("No NC command is active in the NC channel. E.g. channel is idle.", "en")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=268",
    browseName="EnumValues",
    parent="ns=machine_tool;i=69",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("NumberBased"), description=o6.LocalizedText("The tool is addressed using a single identifier.", "en")),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("GroupBased"),
            description=o6.LocalizedText("The tool is addressed using an identifier for the group and a second one for the tool within the group.", "en"),
        ),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("The tool is addressed by a different, custom defined system.", "en")
        ),
    ],
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_tool;i=270",
    browseName="CurrentState",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=271", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=274", browseName="Number", dataType=o6.UInt32)),
    ],
    dataType=o6.LocalizedText,
    value=o6.LocalizedText(),
)
o6.reference(machine_tool_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=270"])
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=machine_tool;i=241",
    browseName="ns=machine_tool;Override",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=246", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=275", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(machine_tool_objtypes.SpindleMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=241"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=machine_tool;i=179",
    browseName="ns=machine_tool;Locked",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=277", browseName="ns=machine_tool;ReasonForLocking", dataType=machine_tool_datypes.ToolLocked))],
    dataType=o6.Boolean,
    value=False,
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=machine_tool;i=272",
    browseName="LastTransition",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=273", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=278", browseName="Number", dataType=o6.UInt32)),
    ],
    dataType=o6.LocalizedText,
    value=o6.LocalizedText(),
)
o6.reference(machine_tool_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=272"])
machine_tool_objtypes.ElementMonitoringType(
    nodeId="ns=machine_tool;i=126",
    browseName="ns=machine_tool;<MonitoredElement>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=284", browseName="ns=machine_tool;Name", dataType=o6.String))],
    _allow_abstract=True,
)
o6.reference(machine_tool_objtypes.MonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=126"])
ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=288",
    browseName="EnumValues",
    parent="ns=machine_tool;i=67",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("Automatic"), description=o6.LocalizedText("NC channel mode Automatic &#8211; execute CNC part programs.", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("MdaMdi"), description=o6.LocalizedText("NC channel mode Mda/Mdi &#8211; manual data input and execution.", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("JogManual"), description=o6.LocalizedText("NC channel mode Jog Manual &#8211; axis movement triggered by user.", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("JogIncrement"),
            description=o6.LocalizedText("NC channel mode Jog Increment &#8211; incremental axis movement triggered by user.", "en"),
        ),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("TeachingHandle"),
            description=o6.LocalizedText("NC channel mode Teaching Handle &#8211; teaching a machine tool by moving axes of the machine tool by hand.", "en"),
        ),
        ns0.datatypes.EnumValueType(
            value=5,
            displayName=o6.LocalizedText("Remote"),
            description=o6.LocalizedText("NC channel mode Remote &#8211; the machine tool can receive CNC files via a remote access mechanism.", "en"),
        ),
        ns0.datatypes.EnumValueType(
            value=6,
            displayName=o6.LocalizedText("Reference"),
            description=o6.LocalizedText("NC channel mode Reference &#8211; The machine tool returns to its reference point/ zero position.", "en"),
        ),
        ns0.datatypes.EnumValueType(
            value=7, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("NC channel mode is different from the values defined in this enumeration.", "en")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=289",
    browseName="EnumValues",
    parent="ns=machine_tool;i=71",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Undefined"), description=o6.LocalizedText("The EDM spark generator state cannot be indicated.", "en")),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("Ready"), description=o6.LocalizedText("Generator is initialized and can receive a set of technology parameters.", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("Active_Low_Voltage"),
            description=o6.LocalizedText(
                "Generator is switched on and is supplying pulses respecting the low voltage (&#8804; 25 V AC or &#8804; 60 V DC) requirements of safety standard (ISO 28881).",
                "en",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("Active_High_Voltage"),
            description=o6.LocalizedText("Generator is switched on and is supplying pulse at high voltage (&gt; 25 V AC or &gt; 60 V DC).", "en"),
        ),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Error"), description=o6.LocalizedText("Generator is in an error state.", "en")),
    ],
)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=91",
    browseName="ns=machine_tool;InitializingToRunning",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=291", browseName="TransitionNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(machine_tool_objtypes.ProductionProgramStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=91"])
o6.reference(o6.ns["ns=machine_tool;i=91"], "i=54", machine_tool_objtypes.ProductionProgramTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=92",
    browseName="ns=machine_tool;RunningToEnded",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=292", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(machine_tool_objtypes.ProductionProgramStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=92"])
o6.reference(o6.ns["ns=machine_tool;i=92"], "i=54", machine_tool_objtypes.ProductionProgramTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=95",
    browseName="ns=machine_tool;InterruptedToRunning",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=294", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(machine_tool_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=95"])
ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=295",
    browseName="EnumValues",
    parent="ns=machine_tool;i=68",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("Time"),
            description=o6.LocalizedText(
                "The tool life indicates the time the tool has been in use or can still be used. The value shall be given in hours (decimal value).", "en"
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("NumberOfParts"),
            description=o6.LocalizedText(
                "The tool life indicates the total number of parts that have been produced or can still be produced using the tool. The unit shall be &#8220;one&#8221;.", "en"
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("NumberOfUsages"),
            description=o6.LocalizedText(
                "The tool life indicates counting the process steps this tool has been used or can still be used (for example usages of a punching tool). The unit shall be &#8220;one&#8221;.",
                "en",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("Feed_Distance"),
            description=o6.LocalizedText(
                "The tool life indicates the sum of the feed path covered by the tool and the workpiece relative to each other during machining. This value shall be given in one of the following units: millimetres, metres, kilometres.",
                "en",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("Cutting_Distance"),
            description=o6.LocalizedText(
                "The tool life indicates the sum of the lengths that the cutting knife works in the workpiece. If the knife is not fixed, this includes the lengths of the arc segments of the knife path. This value shall be given in one of the following units: millimetres, metres, kilometres. This value is likely only available for serial production with clearly defined machining conditions.",
                "en",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=5,
            displayName=o6.LocalizedText("Length"),
            description=o6.LocalizedText(
                "The tool life indicates the abraded length of the tool. This value shall be given in one of the following units: micrometres, millimetres, metres, kilometres.",
                "en",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=6,
            displayName=o6.LocalizedText("Diameter"),
            description=o6.LocalizedText(
                "The tool life indicates the abraded diameter of the tool. This value shall be given in one of the following units: micrometres, millimetres, metres, kilometres.",
                "en",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=7, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("The tool life is indicated in a way not covered by the remaining enum values.", "en")
        ),
    ],
)
machine_tool_objtypes.ToolType(
    nodeId="ns=machine_tool;i=73",
    browseName="ns=machine_tool;<Tool>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=machine_tool;i=179"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=293", browseName="ns=machine_tool;ControlIdentifier1", dataType=o6.UInt32)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_tool;i=297", browseName="ns=machine_tool;ControlIdentifierInterpretation", dataType=machine_tool_datypes.ToolManagement
            )
        ),
    ],
)
o6.reference(machine_tool_objtypes.MultiToolType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=73"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=97",
    browseName="ns=machine_tool;InterruptedToAborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=298", browseName="TransitionNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(machine_tool_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=97"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=99",
    browseName="ns=machine_tool;EndedToInitializing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=299", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(machine_tool_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=99"])
ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=308",
    browseName="EnumValues",
    parent="ns=machine_tool;i=70",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("Undefined"),
            description=o6.LocalizedText(
                "The laser state cannot be indicated, for example because the device does not provide this information or because it is currently unavailable. This can be e.g. during the startup phase.",
                "en",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("Ready"),
            description=o6.LocalizedText("The laser is ready and laser programs can be started. No error state is active. In this state, laser emission is prohibited.", "en"),
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("Active"),
            description=o6.LocalizedText(
                "In this state, safety clearances have to be set for processing and emission can be activated. For devices that can run programs themselves it indicates that a program is running on the laser device.",
                "en",
            ),
        ),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Error"), description=o6.LocalizedText("An error state is reported from the laser device.", "en")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=309",
    browseName="EnumValues",
    parent="ns=machine_tool;i=66",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("CapabilityUnavailable"), description=o6.LocalizedText("The reason for locking the tool cannot be given.", "en")
        ),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ByOperator"), description=o6.LocalizedText("The tool is locked by an operator.", "en")),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("ToolBreak"), description=o6.LocalizedText("The tool is locked because a tool break has been detected.", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=3, displayName=o6.LocalizedText("ToolLife"), description=o6.LocalizedText("The tool is locked because it reached a tool life limit.", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=4, displayName=o6.LocalizedText("MeasurementError"), description=o6.LocalizedText("The tool is locked due to a measurement error of the tool.", "en")
        ),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("Other"), description=o6.LocalizedText("The tool is locked for another reason.", "en")),
    ],
)
ia.objtypes.StackElementLightType(
    nodeId="ns=machine_tool;i=117",
    browseName="<OrderedObject>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_tool;i=226",
                browseName="NumberInList",
                description="Enumerate the stacklight elements counting upwards beginning from the base of the stacklight.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_tool;i=310",
                browseName="ns=ia;SignalOn",
                description="Indicates if the signal emitted by the stack element is currently switched on or not.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_tool;i=290",
                browseName="ns=ia;SignalColor",
                description="Indicates the colour the lamp element has when switched on.",
                dataType=ia.datatypes.SignalColor,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_tool;i=303",
                browseName="ns=ia;SignalMode",
                description="Shows in what way the lamp is used (continuous light, flashing, blinking) when switched on.",
                dataType=ia.datatypes.SignalModeLight,
            )
        ),
    ],
)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=102",
    browseName="ns=machine_tool;AbortedToInitializing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=311", browseName="TransitionNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(machine_tool_objtypes.ProductionProgramStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=102"])
o6.reference(o6.ns["ns=machine_tool;i=102"], "i=54", machine_tool_objtypes.ProductionProgramTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=104",
    browseName="ns=machine_tool;InitializingToAborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=313", browseName="TransitionNumber", dataType=o6.UInt32, value=9))],
)
o6.reference(machine_tool_objtypes.ProductionProgramStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=104"])
o6.reference(o6.ns["ns=machine_tool;i=104"], "i=54", machine_tool_objtypes.ProductionProgramTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=105",
    browseName="ns=machine_tool;InterruptedToAborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=314", browseName="TransitionNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(machine_tool_objtypes.ProductionProgramStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=105"])
o6.reference(o6.ns["ns=machine_tool;i=105"], "i=54", machine_tool_objtypes.ProductionProgramTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=106",
    browseName="ns=machine_tool;EndedToInitializing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=315", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(machine_tool_objtypes.ProductionProgramStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=106"])
o6.reference(o6.ns["ns=machine_tool;i=106"], "i=54", machine_tool_objtypes.ProductionProgramTransitionEventType)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_tool;i=118",
    browseName="ns=machine_tool;Location",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=312", browseName="ns=machine_tool;Name", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=318", browseName="ns=machine_tool;PlaceNumber", dataType=o6.UInt16)),
    ],
)
o6.reference(machine_tool_objtypes.BaseToolType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=118"])
ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=320",
    browseName="EnumValues",
    parent="ns=machine_tool;i=65",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("Manual"),
            description=o6.LocalizedText(
                "The machine tool is controlled manually, by the operator. Depending on technology specific norms, the maximum axis movement speeds of the machine tool are limited.",
                "en",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("Automatic"),
            description=o6.LocalizedText(
                "Operating mode for the automatic, programmed and continuous operation of the machine. Manual loading and unloading workpieces are possible when the automatic program is stopped. Axis movement speeds are fully available to the machine tool&#8217;s ability.",
                "en",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("Setup"),
            description=o6.LocalizedText(
                "Depending on technology specific norms, the maximum axis movement speeds of the machine tool are limited. In this mode, the operator can make settings for the subsequent work processes.",
                "en",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("AutoWithManualIntervention"),
            description=o6.LocalizedText(
                "Operating mode with the possibility of manual interventions in the machining process as well as limited automatic operation started by the operator. Depending on technology specific norms, the maximum axis movement speeds of the machine tool are limited.",
                "en",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("Service"),
            description=o6.LocalizedText(
                "Operating mode for service purposes. This mode shall not be used for manufacturing any parts. This mode shall only be used by authorized personnel.", "en"
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=5,
            displayName=o6.LocalizedText("Other"),
            description=o6.LocalizedText("The machine operation mode is different from the values defined in this enumeration.", "en"),
        ),
    ],
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=machine_tool;i=321",
    browseName="ns=machine_tool;Locked",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=269", browseName="ns=machine_tool;ReasonForLocking", dataType=machine_tool_datypes.ToolLocked))],
    dataType=o6.Boolean,
    value=False,
)
o6.reference(machine_tool_objtypes.ToolType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=321"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=107",
    browseName="ns=machine_tool;InterruptedToRunning",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=327", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(machine_tool_objtypes.ProductionProgramStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=107"])
o6.reference(o6.ns["ns=machine_tool;i=107"], "i=54", machine_tool_objtypes.ProductionProgramTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=108",
    browseName="ns=machine_tool;RunningToAborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=328", browseName="TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(machine_tool_objtypes.ProductionProgramStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=108"])
o6.reference(o6.ns["ns=machine_tool;i=108"], "i=54", machine_tool_objtypes.ProductionProgramTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=114",
    browseName="ns=machine_tool;AbortedToInitializing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=329", browseName="TransitionNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(machine_tool_objtypes.ProductionPartStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=114"])
o6.reference(o6.ns["ns=machine_tool;i=114"], "i=54", machine_tool_objtypes.ProductionPartTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=115",
    browseName="ns=machine_tool;EndedToInitializing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=330", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(machine_tool_objtypes.ProductionPartStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=115"])
o6.reference(o6.ns["ns=machine_tool;i=115"], "i=54", machine_tool_objtypes.ProductionPartTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=124",
    browseName="ns=machine_tool;InterruptedToAborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=331", browseName="TransitionNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(machine_tool_objtypes.ProductionPartStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=124"])
o6.reference(o6.ns["ns=machine_tool;i=124"], "i=54", machine_tool_objtypes.ProductionPartTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=125",
    browseName="ns=machine_tool;InterruptedToRunning",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=333", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(machine_tool_objtypes.ProductionPartStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=125"])
o6.reference(o6.ns["ns=machine_tool;i=125"], "i=54", machine_tool_objtypes.ProductionPartTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=136",
    browseName="ns=machine_tool;AbortedToInitializing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=334", browseName="TransitionNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(machine_tool_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=136"])
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=machine_tool;i=276",
    browseName="ns=machine_tool;FeedOverride",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=335", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=336", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(machine_tool_objtypes.ChannelMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=276"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=127",
    browseName="ns=machine_tool;RunningToInterrupted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=337", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(machine_tool_objtypes.ProductionPartStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=127"])
o6.reference(o6.ns["ns=machine_tool;i=127"], "i=54", machine_tool_objtypes.ProductionPartTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=109",
    browseName="ns=machine_tool;RunningToInterrupted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=339", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(machine_tool_objtypes.ProductionProgramStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=109"])
o6.reference(o6.ns["ns=machine_tool;i=109"], "i=54", machine_tool_objtypes.ProductionProgramTransitionEventType)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=machine_tool;i=287",
    browseName="ns=machine_tool;RapidOverride",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=342", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=343", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(machine_tool_objtypes.ChannelMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=287"])
ns0.objtypes.InitialStateType(
    nodeId="ns=machine_tool;i=135",
    browseName="ns=machine_tool;Initializing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=345", browseName="StateNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(machine_tool_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=135"])
o6.reference(o6.ns["ns=machine_tool;i=99"], "i=52", o6.ns["ns=machine_tool;i=135"])
o6.reference(o6.ns["ns=machine_tool;i=136"], "i=52", o6.ns["ns=machine_tool;i=135"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=138",
    browseName="ns=machine_tool;Running",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=346", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(machine_tool_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=138"])
o6.reference(o6.ns["ns=machine_tool;i=95"], "i=52", o6.ns["ns=machine_tool;i=138"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=139",
    browseName="ns=machine_tool;Interrupted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=347", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(machine_tool_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=139"])
o6.reference(o6.ns["ns=machine_tool;i=95"], "i=51", o6.ns["ns=machine_tool;i=139"])
o6.reference(o6.ns["ns=machine_tool;i=97"], "i=51", o6.ns["ns=machine_tool;i=139"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=140",
    browseName="ns=machine_tool;Ended",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=349", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(machine_tool_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=140"])
o6.reference(o6.ns["ns=machine_tool;i=99"], "i=51", o6.ns["ns=machine_tool;i=140"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=141",
    browseName="ns=machine_tool;Aborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=350", browseName="StateNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(machine_tool_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=141"])
o6.reference(o6.ns["ns=machine_tool;i=97"], "i=52", o6.ns["ns=machine_tool;i=141"])
o6.reference(o6.ns["ns=machine_tool;i=136"], "i=51", o6.ns["ns=machine_tool;i=141"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=142",
    browseName="ns=machine_tool;InitializingToRunning",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=352", browseName="TransitionNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(machine_tool_objtypes.ProductionJobStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=142"])
o6.reference(o6.ns["ns=machine_tool;i=142"], "i=54", machine_tool_objtypes.ProductionJobTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=143",
    browseName="ns=machine_tool;RunningToEnded",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=353", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(machine_tool_objtypes.ProductionJobStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=143"])
o6.reference(o6.ns["ns=machine_tool;i=143"], "i=54", machine_tool_objtypes.ProductionJobTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=144",
    browseName="ns=machine_tool;RunningToAborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=354", browseName="TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(machine_tool_objtypes.ProductionJobStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=144"])
o6.reference(o6.ns["ns=machine_tool;i=144"], "i=54", machine_tool_objtypes.ProductionJobTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=145",
    browseName="ns=machine_tool;RunningToInterrupted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=355", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(machine_tool_objtypes.ProductionJobStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=145"])
o6.reference(o6.ns["ns=machine_tool;i=145"], "i=54", machine_tool_objtypes.ProductionJobTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=147",
    browseName="ns=machine_tool;InterruptedToRunning",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=356", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(machine_tool_objtypes.ProductionJobStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=147"])
o6.reference(o6.ns["ns=machine_tool;i=147"], "i=54", machine_tool_objtypes.ProductionJobTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=148",
    browseName="ns=machine_tool;InterruptedToAborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=357", browseName="TransitionNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(machine_tool_objtypes.ProductionJobStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=148"])
o6.reference(o6.ns["ns=machine_tool;i=148"], "i=54", machine_tool_objtypes.ProductionJobTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=137",
    browseName="ns=machine_tool;RunningToRunning",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=358", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(machine_tool_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=137"])
o6.reference(o6.ns["ns=machine_tool;i=137"], "i=51", o6.ns["ns=machine_tool;i=138"])
o6.reference(o6.ns["ns=machine_tool;i=137"], "i=52", o6.ns["ns=machine_tool;i=138"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=133",
    browseName="ns=machine_tool;RunningToRunning",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=359", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(machine_tool_objtypes.ProductionProgramStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=133"])
o6.reference(o6.ns["ns=machine_tool;i=133"], "i=54", machine_tool_objtypes.ProductionProgramTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=149",
    browseName="ns=machine_tool;EndedToInitializing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=360", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(machine_tool_objtypes.ProductionJobStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=149"])
o6.reference(o6.ns["ns=machine_tool;i=149"], "i=54", machine_tool_objtypes.ProductionJobTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=151",
    browseName="ns=machine_tool;RunningToRunning",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=372", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(machine_tool_objtypes.ProductionJobStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=151"])
o6.reference(o6.ns["ns=machine_tool;i=151"], "i=54", machine_tool_objtypes.ProductionJobTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=152",
    browseName="ns=machine_tool;InitializingToAborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=373", browseName="TransitionNumber", dataType=o6.UInt32, value=9))],
)
o6.reference(machine_tool_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=152"])
o6.reference(o6.ns["ns=machine_tool;i=152"], "i=51", o6.ns["ns=machine_tool;i=135"])
o6.reference(o6.ns["ns=machine_tool;i=152"], "i=52", o6.ns["ns=machine_tool;i=141"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=157",
    browseName="ns=machine_tool;RunningToEnded",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=374", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(machine_tool_objtypes.ProductionPartStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=157"])
o6.reference(o6.ns["ns=machine_tool;i=157"], "i=54", machine_tool_objtypes.ProductionPartTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=153",
    browseName="ns=machine_tool;InitializingToRunning",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=375", browseName="TransitionNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(machine_tool_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=153"])
o6.reference(o6.ns["ns=machine_tool;i=153"], "i=51", o6.ns["ns=machine_tool;i=135"])
o6.reference(o6.ns["ns=machine_tool;i=153"], "i=52", o6.ns["ns=machine_tool;i=138"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=150",
    browseName="ns=machine_tool;AbortedToInitializing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=376", browseName="TransitionNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(machine_tool_objtypes.ProductionJobStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=150"])
o6.reference(o6.ns["ns=machine_tool;i=150"], "i=54", machine_tool_objtypes.ProductionJobTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=158",
    browseName="ns=machine_tool;InitializingToRunning",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=377", browseName="TransitionNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(machine_tool_objtypes.ProductionPartStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=158"])
o6.reference(o6.ns["ns=machine_tool;i=158"], "i=54", machine_tool_objtypes.ProductionPartTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=154",
    browseName="ns=machine_tool;RunningToAborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=378", browseName="TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(machine_tool_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=154"])
o6.reference(o6.ns["ns=machine_tool;i=154"], "i=51", o6.ns["ns=machine_tool;i=138"])
o6.reference(o6.ns["ns=machine_tool;i=154"], "i=52", o6.ns["ns=machine_tool;i=141"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=159",
    browseName="ns=machine_tool;InitializingToAborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=379", browseName="TransitionNumber", dataType=o6.UInt32, value=9))],
)
o6.reference(machine_tool_objtypes.ProductionPartStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=159"])
o6.reference(o6.ns["ns=machine_tool;i=159"], "i=54", machine_tool_objtypes.ProductionPartTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=160",
    browseName="ns=machine_tool;RunningToAborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=380", browseName="TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(machine_tool_objtypes.ProductionPartStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=160"])
o6.reference(o6.ns["ns=machine_tool;i=160"], "i=54", machine_tool_objtypes.ProductionPartTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=155",
    browseName="ns=machine_tool;RunningToEnded",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=381", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(machine_tool_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=155"])
o6.reference(o6.ns["ns=machine_tool;i=155"], "i=51", o6.ns["ns=machine_tool;i=138"])
o6.reference(o6.ns["ns=machine_tool;i=155"], "i=52", o6.ns["ns=machine_tool;i=140"])
machine_tool_objtypes.ChannelModifierType(
    nodeId="ns=machine_tool;i=113",
    browseName="ns=machine_tool;ChannelModifiers",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=361", browseName="ns=machine_tool;DryRun", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=364", browseName="ns=machine_tool;OptionalStop", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=366", browseName="ns=machine_tool;TestMode", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=367", browseName="ns=machine_tool;SingleStep", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=383", browseName="ns=machine_tool;BlockSkip", dataType=o6.Boolean)),
    ],
)
o6.reference(machine_tool_objtypes.ChannelMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=113"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=132",
    browseName="ns=machine_tool;InitializingToAborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=385", browseName="TransitionNumber", dataType=o6.UInt32, value=9))],
)
o6.reference(machine_tool_objtypes.ProductionJobStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=132"])
o6.reference(o6.ns["ns=machine_tool;i=132"], "i=54", machine_tool_objtypes.ProductionJobTransitionEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=156",
    browseName="ns=machine_tool;RunningToInterrupted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=386", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(machine_tool_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=156"])
o6.reference(o6.ns["ns=machine_tool;i=156"], "i=51", o6.ns["ns=machine_tool;i=138"])
o6.reference(o6.ns["ns=machine_tool;i=156"], "i=52", o6.ns["ns=machine_tool;i=139"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=161",
    browseName="ns=machine_tool;RunningToRunning",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=410", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(machine_tool_objtypes.ProductionPartStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=161"])
o6.reference(o6.ns["ns=machine_tool;i=161"], "i=54", machine_tool_objtypes.ProductionPartTransitionEventType)
machine_tool_vartypes.ToolLifeType(
    nodeId="ns=machine_tool;i=283",
    browseName="ns=machine_tool;<ToolLifeEntry>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=307", browseName="ns=machine_tool;EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=388", browseName="ns=machine_tool;Indication", dataType=machine_tool_datypes.ToolLifeIndication)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=413", browseName="ns=machine_tool;IsCountingUp", dataType=o6.Boolean)),
    ],
    dataType=ns0.datatypes.Number,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_tool;i=88", browseName="ns=machine_tool;ToolLife", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=machine_tool;i=283"])]
)
o6.reference(machine_tool_objtypes.ToolType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=88"])
ia.objtypes.BasicStacklightType(
    nodeId="ns=machine_tool;i=121",
    browseName="ns=machine_tool;Stacklight",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_tool;i=415",
                browseName="ns=ia;StacklightMode",
                description="Shows in what way (stack of individual lights, level meter, running light) the stacklight unit is used.",
                dataType=ia.datatypes.StacklightOperationMode,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasOrderedComponent(o6.ns["ns=machine_tool;i=117"]),
    ],
)
o6.reference(machine_tool_objtypes.MonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=121"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=machine_tool;i=419",
    browseName="ns=machine_tool;RunsPlanned",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=392", browseName="ns=machine_tool;IsValid", dataType=o6.Boolean))],
    dataType=o6.UInt32,
)
o6.reference(machine_tool_objtypes.ProductionJobTransitionEventType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=419"])
machine_tool_objtypes.MessagesType(nodeId="ns=machine_tool;i=5001", browseName="ns=machine_tool;Messages", eventNotifier=1)
o6.reference(o6.ns["ns=machine_tool;i=5001"], "i=41", machine_tool_objtypes.NotificationEventType)
o6.reference(o6.ns["ns=machine_tool;i=5001"], "i=41", machine_tool_objtypes.AlertType)
machine_tool_objtypes.NotificationType(
    nodeId="ns=machine_tool;i=128",
    browseName="ns=machine_tool;Notification",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(machine_tool_objtypes.PrognosisListType(nodeId="ns=machine_tool;i=130", browseName="ns=machine_tool;Prognoses")),
        o6.hasComponent(o6.ns["ns=machine_tool;i=5001"]),
    ],
)
o6.reference(machine_tool_objtypes.MachineToolType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=128"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_tool;i=5077", browseName="ns=machine_tool;MachineTool_v102", description="Machine Tool Version 1.02 deprecates objects referencing here."
)
o6.reference(machine_tool_objtypes.ProductionProgramStateMachineType, "i=23562", "ns=machine_tool;i=5077")
o6.reference(machine_tool_objtypes.ProductionProgramTransitionEventType, "i=23562", "ns=machine_tool;i=5077")
o6.reference(machine_tool_objtypes.ProductionStatisticsType, "i=23562", "ns=machine_tool;i=5077")
o6.reference(machine_tool_objtypes.ProductionType, "i=23562", "ns=machine_tool;i=5077")
o6.reference(machine_tool_objtypes.ProductionStateMachineType, "i=23562", "ns=machine_tool;i=5077")
o6.reference(machine_tool_objtypes.ProductionPartTransitionEventType, "i=23562", "ns=machine_tool;i=5077")
o6.reference(machine_tool_objtypes.ProductionJobStateMachineType, "i=23562", "ns=machine_tool;i=5077")
o6.reference(machine_tool_objtypes.ProductionJobType, "i=23562", "ns=machine_tool;i=5077")
o6.reference(machine_tool_objtypes.ProductionJobListType, "i=23562", "ns=machine_tool;i=5077")
o6.reference(machine_tool_objtypes.ProductionJobTransitionEventType, "i=23562", "ns=machine_tool;i=5077")
o6.reference(machine_tool_objtypes.ProductionActiveProgramType, "i=23562", "ns=machine_tool;i=5077")
o6.reference(machine_tool_objtypes.ProductionPartSetType, "i=23562", "ns=machine_tool;i=5077")
o6.reference(machine_tool_objtypes.ProductionJobEndPrognosisType, "i=23562", "ns=machine_tool;i=5077")
o6.reference(machine_tool_objtypes.ProductionPartStateMachineType, "i=23562", "ns=machine_tool;i=5077")
o6.reference(machine_tool_objtypes.ProductionPartType, "i=23562", "ns=machine_tool;i=5077")
o6.reference(machine_tool_objtypes.ProductionProgramType, "i=23562", "ns=machine_tool;i=5077")
o6.reference(o6.ns["ns=machine_tool;i=81"], "i=23562", o6.ns["ns=machine_tool;i=5077"])
o6.reference(o6.ns["ns=machine_tool;i=190"], "i=23562", o6.ns["ns=machine_tool;i=5077"])
o6.reference(o6.ns["ns=machine_tool;i=227"], "i=23562", o6.ns["ns=machine_tool;i=5077"])
o6.reference(o6.ns["ns=machine_tool;i=261"], "i=23562", o6.ns["ns=machine_tool;i=5077"])
o6.reference(o6.ns["ns=machine_tool;i=395"], "i=23562", o6.ns["ns=machine_tool;i=5077"])
o6.reference(o6.ns["ns=machine_tool;i=401"], "i=23562", o6.ns["ns=machine_tool;i=5077"])
o6.reference(o6.ns["ns=machine_tool;i=414"], "i=23562", o6.ns["ns=machine_tool;i=5077"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMachineToolSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=machine_tool;i=120",
    browseName="ns=machine_tool;http://opcfoundation.org/UA/MachineTool/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=396", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=397", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2024-11-01T00:00:00Z"))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=398", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/MachineTool/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=399", browseName="NamespaceVersion", dataType=o6.String, value="1.02.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_tool;i=400",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=406", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=407", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=machine_tool;i=5077"]),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_tool;i=6001",
    browseName="CurrentState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6002", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6003", browseName="Number", dataType=o6.UInt32)),
    ],
    dataType=o6.LocalizedText,
)
machine_tool_objtypes.ProductionJobStateMachineType(
    nodeId="ns=machine_tool;i=5002", browseName="ns=machine_tool;State", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=machine_tool;i=6001"])]
)
o6.reference(machine_tool_objtypes.ProductionJobType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5002"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_tool;i=6004",
    browseName="CurrentState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6005", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6006", browseName="Number", dataType=o6.UInt32)),
    ],
    dataType=o6.LocalizedText,
)
machine_tool_objtypes.ProductionJobStateMachineType(
    nodeId="ns=machine_tool;i=5003", browseName="ns=machine_tool;State", references=[o6.hasComponent(o6.ns["ns=machine_tool;i=6004"])]
)
machine_tool_objtypes.ProductionJobType(
    nodeId="ns=machine_tool;i=74",
    browseName="<OrderedObject>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=195", browseName="ns=machine_tool;Identifier", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=215", browseName="NumberInList", dataType=o6.UInt16)),
        o6.hasComponent(o6.ns["ns=machine_tool;i=76"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=206", browseName="ns=machine_tool;RunsCompleted", dataType=o6.UInt32)),
        o6.hasComponent(o6.ns["ns=machine_tool;i=245"]),
        o6.hasComponent(o6.ns["ns=machine_tool;i=5003"]),
    ],
)
o6.reference(machine_tool_objtypes.ProductionJobListType, ns0.reftypes.HasOrderedComponent, o6.ns["ns=machine_tool;i=74"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_tool;i=6007",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6008", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=machine_tool;i=5006", browseName="ns=machinery;MachineryItemState", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=machine_tool;i=6007"])]
)
o6.reference(machine_tool_objtypes.MachineOperationMonitoringType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_tool;i=5006"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_tool;i=6009",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6010", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machine_tool_objtypes.MachineOperationModeStateMachineType(
    nodeId="ns=machine_tool;i=5007", browseName="ns=machinery;MachineryOperationMode", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=machine_tool;i=6009"])]
)
o6.reference(machine_tool_objtypes.MachineOperationMonitoringType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_tool;i=5007"])
machine_tool_objtypes.ObligationType(
    nodeId="ns=machine_tool;i=5008",
    browseName="ns=machine_tool;Obligation",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=6013", browseName="ns=machine_tool;EndUserObligated", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=6014", browseName="ns=machine_tool;MachineBuilderObligated", dataType=o6.Boolean)),
    ],
)
o6.reference(machine_tool_objtypes.MachineOperationMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5008"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_tool;i=6017",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6019", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=machine_tool;i=5009", browseName="ns=machinery;MachineryItemState", references=[o6.hasComponent(o6.ns["ns=machine_tool;i=6017"])]
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_tool;i=6018",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6021", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
isa95_jobcontrol_v2.objtypes.ISA95JobOrderReceiverObjectType(
    nodeId="ns=machine_tool;i=5023",
    browseName="ns=machinery_jobs;JobOrderControl",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6026", browseName="ns=isa95_jobcontrol_v2;MaxDownloadableJobOrders", dataType=o6.UInt16)),
        o6.hasComponent(o6.ns["ns=machine_tool;i=6018"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_tool;i=6022",
                browseName="ns=isa95_jobcontrol_v2;EquipmentID",
                description="Defines a read-only set of Equipment Class IDs and Equipment IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_tool;i=6023",
                browseName="ns=isa95_jobcontrol_v2;JobOrderList",
                description="Defines a read-only list of job order information available from the server.",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95JobOrderAndStateDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_tool;i=6024",
                browseName="ns=isa95_jobcontrol_v2;MaterialClassID",
                description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_tool;i=6025",
                browseName="ns=isa95_jobcontrol_v2;MaterialDefinitionID",
                description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_tool;i=6027",
                browseName="ns=isa95_jobcontrol_v2;PersonnelID",
                description="Defines a read-only set of Personnel IDs and Person IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_tool;i=6028",
                browseName="ns=isa95_jobcontrol_v2;PhysicalAssetID",
                description="Defines a read-only set of Physical Asset Class IDs and Physical Asset IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_tool;i=6029",
                browseName="ns=isa95_jobcontrol_v2;WorkMaster",
                description="Defines a read-only set of work master IDs that may be specified in a job order, and the read-only set of parameters that may be specified for a specific work master.",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95WorkMasterDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
    ],
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_tool;i=6032",
    browseName="CurrentState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6033", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6034", browseName="Number", dataType=o6.UInt32)),
    ],
    dataType=o6.LocalizedText,
    value=o6.LocalizedText(),
)
machine_tool_objtypes.ProductionProgramStateMachineType(
    nodeId="ns=machine_tool;i=5033", browseName="ns=machine_tool;State", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=machine_tool;i=6032"])]
)
o6.reference(machine_tool_objtypes.ProductionActiveProgramType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5033"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_tool;i=6036",
    browseName="CurrentState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6037", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6038", browseName="Number", dataType=o6.UInt32)),
    ],
    dataType=o6.LocalizedText,
    value=o6.LocalizedText(),
)
machine_tool_objtypes.ProductionProgramStateMachineType(
    nodeId="ns=machine_tool;i=5034", browseName="ns=machine_tool;State", references=[o6.hasComponent(o6.ns["ns=machine_tool;i=6036"])]
)
machine_tool_objtypes.ProductionActiveProgramType(
    nodeId="ns=machine_tool;i=84",
    browseName="ns=machine_tool;ActiveProgram",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=174", browseName="ns=machine_tool;Name", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=175", browseName="NumberInList", dataType=o6.UInt16)),
        o6.hasComponent(o6.ns["ns=machine_tool;i=5034"]),
    ],
)
machine_tool_objtypes.ProductionType(
    nodeId="ns=machine_tool;i=82", browseName="ns=machine_tool;Production", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=machine_tool;i=84"])]
)
o6.reference(machine_tool_objtypes.MachineToolType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=82"])
o6.reference(o6.ns["ns=machine_tool;i=82"], "i=23562", o6.ns["ns=machine_tool;i=5077"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_tool;i=6031",
    browseName="CurrentState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6035", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6039", browseName="Number", dataType=o6.UInt32)),
    ],
    dataType=o6.LocalizedText,
)
machine_tool_objtypes.ProductionProgramStateMachineType(
    nodeId="ns=machine_tool;i=5032", browseName="ns=machine_tool;State", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=machine_tool;i=6031"])]
)
o6.reference(machine_tool_objtypes.ProductionProgramType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5032"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_tool;i=6040",
    browseName="CurrentState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6041", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6042", browseName="Number", dataType=o6.UInt32)),
    ],
    dataType=o6.LocalizedText,
    value=o6.LocalizedText(),
)
machine_tool_objtypes.ProductionProgramStateMachineType(
    nodeId="ns=machine_tool;i=5035", browseName="ns=machine_tool;State", references=[o6.hasComponent(o6.ns["ns=machine_tool;i=6040"])]
)
machine_tool_objtypes.ProductionActiveProgramType(
    nodeId="ns=machine_tool;i=87",
    browseName="ns=machine_tool;ActiveProgram",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=250", browseName="NumberInList", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=326", browseName="ns=machine_tool;Name", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=machine_tool;i=5035"]),
    ],
)
o6.reference(machine_tool_objtypes.ProductionType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=87"])
o6.reference(o6.ns["ns=machine_tool;i=87"], "i=23562", o6.ns["ns=machine_tool;i=5077"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_tool;i=6020",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6043", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machine_tool_objtypes.MachineOperationModeStateMachineType(
    nodeId="ns=machine_tool;i=5010", browseName="ns=machinery;MachineryOperationMode", references=[o6.hasComponent(o6.ns["ns=machine_tool;i=6020"])]
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_tool;i=6044",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6045", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=machine_tool;i=5011", browseName="ns=machinery;MachineryItemState", references=[o6.hasComponent(o6.ns["ns=machine_tool;i=6044"])]
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_tool;i=6046",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6047", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machine_tool_objtypes.MachineOperationModeStateMachineType(
    nodeId="ns=machine_tool;i=5012", browseName="ns=machinery;MachineryOperationMode", references=[o6.hasComponent(o6.ns["ns=machine_tool;i=6046"])]
)
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=5013",
    browseName="ns=machine_tool;Aborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6048", browseName="StateNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(machine_tool_objtypes.ProductionJobStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5013"])
o6.reference(o6.ns["ns=machine_tool;i=132"], "i=52", o6.ns["ns=machine_tool;i=5013"])
o6.reference(o6.ns["ns=machine_tool;i=144"], "i=52", o6.ns["ns=machine_tool;i=5013"])
o6.reference(o6.ns["ns=machine_tool;i=148"], "i=52", o6.ns["ns=machine_tool;i=5013"])
o6.reference(o6.ns["ns=machine_tool;i=150"], "i=51", o6.ns["ns=machine_tool;i=5013"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=5014",
    browseName="ns=machine_tool;Ended",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6049", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(machine_tool_objtypes.ProductionJobStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5014"])
o6.reference(o6.ns["ns=machine_tool;i=143"], "i=52", o6.ns["ns=machine_tool;i=5014"])
o6.reference(o6.ns["ns=machine_tool;i=149"], "i=51", o6.ns["ns=machine_tool;i=5014"])
ns0.objtypes.InitialStateType(
    nodeId="ns=machine_tool;i=5015",
    browseName="ns=machine_tool;Initializing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6050", browseName="StateNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(machine_tool_objtypes.ProductionJobStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5015"])
o6.reference(o6.ns["ns=machine_tool;i=132"], "i=51", o6.ns["ns=machine_tool;i=5015"])
o6.reference(o6.ns["ns=machine_tool;i=142"], "i=51", o6.ns["ns=machine_tool;i=5015"])
o6.reference(o6.ns["ns=machine_tool;i=149"], "i=52", o6.ns["ns=machine_tool;i=5015"])
o6.reference(o6.ns["ns=machine_tool;i=150"], "i=52", o6.ns["ns=machine_tool;i=5015"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=5016",
    browseName="ns=machine_tool;Interrupted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6051", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(machine_tool_objtypes.ProductionJobStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5016"])
o6.reference(o6.ns["ns=machine_tool;i=145"], "i=52", o6.ns["ns=machine_tool;i=5016"])
o6.reference(o6.ns["ns=machine_tool;i=147"], "i=51", o6.ns["ns=machine_tool;i=5016"])
o6.reference(o6.ns["ns=machine_tool;i=148"], "i=51", o6.ns["ns=machine_tool;i=5016"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=5017",
    browseName="ns=machine_tool;Running",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6052", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(machine_tool_objtypes.ProductionJobStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5017"])
o6.reference(o6.ns["ns=machine_tool;i=142"], "i=52", o6.ns["ns=machine_tool;i=5017"])
o6.reference(o6.ns["ns=machine_tool;i=143"], "i=51", o6.ns["ns=machine_tool;i=5017"])
o6.reference(o6.ns["ns=machine_tool;i=144"], "i=51", o6.ns["ns=machine_tool;i=5017"])
o6.reference(o6.ns["ns=machine_tool;i=145"], "i=51", o6.ns["ns=machine_tool;i=5017"])
o6.reference(o6.ns["ns=machine_tool;i=147"], "i=52", o6.ns["ns=machine_tool;i=5017"])
o6.reference(o6.ns["ns=machine_tool;i=151"], "i=51", o6.ns["ns=machine_tool;i=5017"])
o6.reference(o6.ns["ns=machine_tool;i=151"], "i=52", o6.ns["ns=machine_tool;i=5017"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=5018",
    browseName="ns=machine_tool;Aborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6053", browseName="StateNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(machine_tool_objtypes.ProductionPartStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5018"])
o6.reference(o6.ns["ns=machine_tool;i=114"], "i=51", o6.ns["ns=machine_tool;i=5018"])
o6.reference(o6.ns["ns=machine_tool;i=124"], "i=52", o6.ns["ns=machine_tool;i=5018"])
o6.reference(o6.ns["ns=machine_tool;i=159"], "i=52", o6.ns["ns=machine_tool;i=5018"])
o6.reference(o6.ns["ns=machine_tool;i=160"], "i=52", o6.ns["ns=machine_tool;i=5018"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=5019",
    browseName="ns=machine_tool;Ended",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6054", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(machine_tool_objtypes.ProductionPartStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5019"])
o6.reference(o6.ns["ns=machine_tool;i=115"], "i=51", o6.ns["ns=machine_tool;i=5019"])
o6.reference(o6.ns["ns=machine_tool;i=157"], "i=52", o6.ns["ns=machine_tool;i=5019"])
ns0.objtypes.InitialStateType(
    nodeId="ns=machine_tool;i=5020",
    browseName="ns=machine_tool;Initializing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6055", browseName="StateNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(machine_tool_objtypes.ProductionPartStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5020"])
o6.reference(o6.ns["ns=machine_tool;i=114"], "i=52", o6.ns["ns=machine_tool;i=5020"])
o6.reference(o6.ns["ns=machine_tool;i=115"], "i=52", o6.ns["ns=machine_tool;i=5020"])
o6.reference(o6.ns["ns=machine_tool;i=158"], "i=51", o6.ns["ns=machine_tool;i=5020"])
o6.reference(o6.ns["ns=machine_tool;i=159"], "i=51", o6.ns["ns=machine_tool;i=5020"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=5021",
    browseName="ns=machine_tool;Interrupted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6056", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(machine_tool_objtypes.ProductionPartStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5021"])
o6.reference(o6.ns["ns=machine_tool;i=124"], "i=51", o6.ns["ns=machine_tool;i=5021"])
o6.reference(o6.ns["ns=machine_tool;i=125"], "i=51", o6.ns["ns=machine_tool;i=5021"])
o6.reference(o6.ns["ns=machine_tool;i=127"], "i=52", o6.ns["ns=machine_tool;i=5021"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=5036",
    browseName="ns=machine_tool;Running",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6057", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(machine_tool_objtypes.ProductionPartStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5036"])
o6.reference(o6.ns["ns=machine_tool;i=125"], "i=52", o6.ns["ns=machine_tool;i=5036"])
o6.reference(o6.ns["ns=machine_tool;i=127"], "i=51", o6.ns["ns=machine_tool;i=5036"])
o6.reference(o6.ns["ns=machine_tool;i=157"], "i=51", o6.ns["ns=machine_tool;i=5036"])
o6.reference(o6.ns["ns=machine_tool;i=158"], "i=52", o6.ns["ns=machine_tool;i=5036"])
o6.reference(o6.ns["ns=machine_tool;i=160"], "i=51", o6.ns["ns=machine_tool;i=5036"])
o6.reference(o6.ns["ns=machine_tool;i=161"], "i=51", o6.ns["ns=machine_tool;i=5036"])
o6.reference(o6.ns["ns=machine_tool;i=161"], "i=52", o6.ns["ns=machine_tool;i=5036"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=5037",
    browseName="ns=machine_tool;Aborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6058", browseName="StateNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(machine_tool_objtypes.ProductionProgramStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5037"])
o6.reference(o6.ns["ns=machine_tool;i=102"], "i=51", o6.ns["ns=machine_tool;i=5037"])
o6.reference(o6.ns["ns=machine_tool;i=104"], "i=52", o6.ns["ns=machine_tool;i=5037"])
o6.reference(o6.ns["ns=machine_tool;i=105"], "i=52", o6.ns["ns=machine_tool;i=5037"])
o6.reference(o6.ns["ns=machine_tool;i=108"], "i=52", o6.ns["ns=machine_tool;i=5037"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=5038",
    browseName="ns=machine_tool;Ended",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6059", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(machine_tool_objtypes.ProductionProgramStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5038"])
o6.reference(o6.ns["ns=machine_tool;i=92"], "i=52", o6.ns["ns=machine_tool;i=5038"])
o6.reference(o6.ns["ns=machine_tool;i=106"], "i=51", o6.ns["ns=machine_tool;i=5038"])
ns0.objtypes.InitialStateType(
    nodeId="ns=machine_tool;i=5039",
    browseName="ns=machine_tool;Initializing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6060", browseName="StateNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(machine_tool_objtypes.ProductionProgramStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5039"])
o6.reference(o6.ns["ns=machine_tool;i=91"], "i=51", o6.ns["ns=machine_tool;i=5039"])
o6.reference(o6.ns["ns=machine_tool;i=102"], "i=52", o6.ns["ns=machine_tool;i=5039"])
o6.reference(o6.ns["ns=machine_tool;i=104"], "i=51", o6.ns["ns=machine_tool;i=5039"])
o6.reference(o6.ns["ns=machine_tool;i=106"], "i=52", o6.ns["ns=machine_tool;i=5039"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=5040",
    browseName="ns=machine_tool;Interrupted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6061", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(machine_tool_objtypes.ProductionProgramStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5040"])
o6.reference(o6.ns["ns=machine_tool;i=105"], "i=51", o6.ns["ns=machine_tool;i=5040"])
o6.reference(o6.ns["ns=machine_tool;i=107"], "i=51", o6.ns["ns=machine_tool;i=5040"])
o6.reference(o6.ns["ns=machine_tool;i=109"], "i=52", o6.ns["ns=machine_tool;i=5040"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=5041",
    browseName="ns=machine_tool;Running",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6062", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(machine_tool_objtypes.ProductionProgramStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5041"])
o6.reference(o6.ns["ns=machine_tool;i=91"], "i=52", o6.ns["ns=machine_tool;i=5041"])
o6.reference(o6.ns["ns=machine_tool;i=92"], "i=51", o6.ns["ns=machine_tool;i=5041"])
o6.reference(o6.ns["ns=machine_tool;i=107"], "i=52", o6.ns["ns=machine_tool;i=5041"])
o6.reference(o6.ns["ns=machine_tool;i=108"], "i=51", o6.ns["ns=machine_tool;i=5041"])
o6.reference(o6.ns["ns=machine_tool;i=109"], "i=51", o6.ns["ns=machine_tool;i=5041"])
o6.reference(o6.ns["ns=machine_tool;i=133"], "i=51", o6.ns["ns=machine_tool;i=5041"])
o6.reference(o6.ns["ns=machine_tool;i=133"], "i=52", o6.ns["ns=machine_tool;i=5041"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=5042",
    browseName="ns=machinery;FromMaintenanceToMaintenance",
    description="Transition from state Maintenance to state Maintenance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6064", browseName="TransitionNumber", dataType=o6.UInt32, value=13))],
)
o6.reference(machine_tool_objtypes.MachineOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5042"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=5043",
    browseName="ns=machinery;FromMaintenanceToNone",
    description="Transition from state Maintenance to state None",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6065", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(machine_tool_objtypes.MachineOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5043"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=5044",
    browseName="ns=machinery;FromMaintenanceToProcessing",
    description="Transition from state Maintenance to state Processing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6066", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(machine_tool_objtypes.MachineOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5044"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=5045",
    browseName="ns=machinery;FromMaintenanceToSetup",
    description="Transition from state Maintenance to state Setup",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6067", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(machine_tool_objtypes.MachineOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5045"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=5046",
    browseName="ns=machinery;FromNoneToMaintenance",
    description="Transition from state None to state Maintenance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6068", browseName="TransitionNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(machine_tool_objtypes.MachineOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5046"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=5047",
    browseName="ns=machinery;FromNoneToNone",
    description="Transition from state None to state None",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6069", browseName="TransitionNumber", dataType=o6.UInt32, value=12))],
)
o6.reference(machine_tool_objtypes.MachineOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5047"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=5048",
    browseName="ns=machinery;FromNoneToProcessing",
    description="Transition from state None to state Processing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6070", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(machine_tool_objtypes.MachineOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5048"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=5049",
    browseName="ns=machinery;FromNoneToSetup",
    description="Transition from state None to state Setup",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6071", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(machine_tool_objtypes.MachineOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5049"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=5050",
    browseName="ns=machinery;FromProcessingToMaintenance",
    description="Transition from state Processing to state Maintenance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6072", browseName="TransitionNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(machine_tool_objtypes.MachineOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5050"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=5051",
    browseName="ns=machinery;FromProcessingToNone",
    description="Transition from state Processing to state None",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6073", browseName="TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(machine_tool_objtypes.MachineOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5051"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=5052",
    browseName="ns=machinery;FromProcessingToProcessing",
    description="Transition from state Processing to state Processing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6074", browseName="TransitionNumber", dataType=o6.UInt32, value=14))],
)
o6.reference(machine_tool_objtypes.MachineOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5052"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=5053",
    browseName="ns=machinery;FromProcessingToSetup",
    description="Transition from state Processing to state Setup",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6075", browseName="TransitionNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(machine_tool_objtypes.MachineOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5053"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=5054",
    browseName="ns=machinery;FromSetupToMaintenance",
    description="Transition from state Setup to state Maintenance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6076", browseName="TransitionNumber", dataType=o6.UInt32, value=10))],
)
o6.reference(machine_tool_objtypes.MachineOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5054"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=5055",
    browseName="ns=machinery;FromSetupToNone",
    description="Transition from state Setup to state None",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6077", browseName="TransitionNumber", dataType=o6.UInt32, value=9))],
)
o6.reference(machine_tool_objtypes.MachineOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5055"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=5056",
    browseName="ns=machinery;FromSetupToProcessing",
    description="Transition from state Setup to state Processing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6078", browseName="TransitionNumber", dataType=o6.UInt32, value=11))],
)
o6.reference(machine_tool_objtypes.MachineOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5056"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_tool;i=5057",
    browseName="ns=machinery;FromSetupToSetup",
    description="Transition from state Setup to state Setup",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6079", browseName="TransitionNumber", dataType=o6.UInt32, value=15))],
)
o6.reference(machine_tool_objtypes.MachineOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5057"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=5058",
    browseName="ns=machinery;Maintenance",
    description="MachineryItem is set into maintenance mode with the intention to carry out maintenance or servicing activities",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6080", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(machine_tool_objtypes.MachineOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5058"])
o6.reference(o6.ns["ns=machine_tool;i=5042"], "i=51", o6.ns["ns=machine_tool;i=5058"])
o6.reference(o6.ns["ns=machine_tool;i=5042"], "i=52", o6.ns["ns=machine_tool;i=5058"])
o6.reference(o6.ns["ns=machine_tool;i=5043"], "i=51", o6.ns["ns=machine_tool;i=5058"])
o6.reference(o6.ns["ns=machine_tool;i=5044"], "i=51", o6.ns["ns=machine_tool;i=5058"])
o6.reference(o6.ns["ns=machine_tool;i=5045"], "i=51", o6.ns["ns=machine_tool;i=5058"])
o6.reference(o6.ns["ns=machine_tool;i=5046"], "i=52", o6.ns["ns=machine_tool;i=5058"])
o6.reference(o6.ns["ns=machine_tool;i=5050"], "i=52", o6.ns["ns=machine_tool;i=5058"])
o6.reference(o6.ns["ns=machine_tool;i=5054"], "i=52", o6.ns["ns=machine_tool;i=5058"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=5059",
    browseName="ns=machinery;None",
    description="There is currently no operation mode available",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6081", browseName="StateNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(machine_tool_objtypes.MachineOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5059"])
o6.reference(o6.ns["ns=machine_tool;i=5043"], "i=52", o6.ns["ns=machine_tool;i=5059"])
o6.reference(o6.ns["ns=machine_tool;i=5046"], "i=51", o6.ns["ns=machine_tool;i=5059"])
o6.reference(o6.ns["ns=machine_tool;i=5047"], "i=51", o6.ns["ns=machine_tool;i=5059"])
o6.reference(o6.ns["ns=machine_tool;i=5047"], "i=52", o6.ns["ns=machine_tool;i=5059"])
o6.reference(o6.ns["ns=machine_tool;i=5048"], "i=51", o6.ns["ns=machine_tool;i=5059"])
o6.reference(o6.ns["ns=machine_tool;i=5049"], "i=51", o6.ns["ns=machine_tool;i=5059"])
o6.reference(o6.ns["ns=machine_tool;i=5051"], "i=52", o6.ns["ns=machine_tool;i=5059"])
o6.reference(o6.ns["ns=machine_tool;i=5055"], "i=52", o6.ns["ns=machine_tool;i=5059"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=5060",
    browseName="ns=machinery;Processing",
    description="MachineryItem is set into processing mode with the intention to carry out the value adding activities",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6082", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(machine_tool_objtypes.MachineOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5060"])
o6.reference(o6.ns["ns=machine_tool;i=5044"], "i=52", o6.ns["ns=machine_tool;i=5060"])
o6.reference(o6.ns["ns=machine_tool;i=5048"], "i=52", o6.ns["ns=machine_tool;i=5060"])
o6.reference(o6.ns["ns=machine_tool;i=5050"], "i=51", o6.ns["ns=machine_tool;i=5060"])
o6.reference(o6.ns["ns=machine_tool;i=5051"], "i=51", o6.ns["ns=machine_tool;i=5060"])
o6.reference(o6.ns["ns=machine_tool;i=5052"], "i=51", o6.ns["ns=machine_tool;i=5060"])
o6.reference(o6.ns["ns=machine_tool;i=5052"], "i=52", o6.ns["ns=machine_tool;i=5060"])
o6.reference(o6.ns["ns=machine_tool;i=5053"], "i=51", o6.ns["ns=machine_tool;i=5060"])
o6.reference(o6.ns["ns=machine_tool;i=5056"], "i=52", o6.ns["ns=machine_tool;i=5060"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=5061",
    browseName="ns=machinery;Setup",
    description="MachineryItem is set into setup mode with the intention to carry out setup, preparation or postprocessing activities of a production process",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6083", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(machine_tool_objtypes.MachineOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5061"])
o6.reference(o6.ns["ns=machine_tool;i=5045"], "i=52", o6.ns["ns=machine_tool;i=5061"])
o6.reference(o6.ns["ns=machine_tool;i=5049"], "i=52", o6.ns["ns=machine_tool;i=5061"])
o6.reference(o6.ns["ns=machine_tool;i=5053"], "i=52", o6.ns["ns=machine_tool;i=5061"])
o6.reference(o6.ns["ns=machine_tool;i=5054"], "i=51", o6.ns["ns=machine_tool;i=5061"])
o6.reference(o6.ns["ns=machine_tool;i=5055"], "i=51", o6.ns["ns=machine_tool;i=5061"])
o6.reference(o6.ns["ns=machine_tool;i=5056"], "i=51", o6.ns["ns=machine_tool;i=5061"])
o6.reference(o6.ns["ns=machine_tool;i=5057"], "i=51", o6.ns["ns=machine_tool;i=5061"])
o6.reference(o6.ns["ns=machine_tool;i=5057"], "i=52", o6.ns["ns=machine_tool;i=5061"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=5062",
    browseName="ns=machine_tool;Service",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6084", browseName="StateNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(machine_tool_objtypes.MaintenanceModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5062"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=5063",
    browseName="ns=machine_tool;Inspection",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6085", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(machine_tool_objtypes.MaintenanceModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5063"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=5064",
    browseName="ns=machine_tool;Repair",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6086", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(machine_tool_objtypes.MaintenanceModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5064"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=5065",
    browseName="ns=machine_tool;Upgrade",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6087", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(machine_tool_objtypes.MaintenanceModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5065"])
ns0.objtypes.StateType(
    nodeId="ns=machine_tool;i=5066",
    browseName="ns=machine_tool;Other",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6088", browseName="StateNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(machine_tool_objtypes.MaintenanceModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5066"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_tool;i=6089",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6090", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machine_tool_objtypes.MaintenanceModeStateMachineType(
    nodeId="ns=machine_tool;i=5067", browseName="ns=machine_tool;MaintenanceMode", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=machine_tool;i=6089"])]
)
o6.reference(machine_tool_objtypes.MachineOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5067"])
o6.reference(o6.ns["ns=machine_tool;i=5058"], "i=117", o6.ns["ns=machine_tool;i=5067"])
machinery.objtypes.MachineryOperationCounterType(
    nodeId="ns=machine_tool;i=5072",
    browseName="ns=di;OperationCounters",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_tool;i=6094",
                browseName="ns=di;PowerOnDuration",
                description="PowerOnDuration is the duration the MachineryItem has been powered. The main purpose is to determine the time in which degradation of the MachineryItem occurred. The details, when the time is counted, is implementation-specific. Companion specifications might define specific rules. Typically, when the MachineryItem has supply voltage and the main CPU is running, the time is counted. This may include any kind of sleep mode, but may not include pure Wake on LAN. This value shall only increase during the lifetime of the MachineryItem and shall not be reset when it is restarted. The PowerOnDuration is provided as Duration, i.e., in milliseconds or even fractions of a millisecond. However, the Server is not expected to update the value in such a high frequency, but maybe once a minute or once an hour, depending on the application.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
)
machinery.objtypes.MachineryOperationCounterType(
    nodeId="ns=machine_tool;i=5069",
    browseName="ns=di;OperationCounters",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_tool;i=6095",
                browseName="ns=di;PowerOnDuration",
                description="PowerOnDuration is the duration the MachineryItem has been powered. The main purpose is to determine the time in which degradation of the MachineryItem occurred. The details, when the time is counted, is implementation-specific. Companion specifications might define specific rules. Typically, when the MachineryItem has supply voltage and the main CPU is running, the time is counted. This may include any kind of sleep mode, but may not include pure Wake on LAN. This value shall only increase during the lifetime of the MachineryItem and shall not be reset when it is restarted. The PowerOnDuration is provided as Duration, i.e., in milliseconds or even fractions of a millisecond. However, the Server is not expected to update the value in such a high frequency, but maybe once a minute or once an hour, depending on the application.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
)
machine_tool_objtypes.MachineOperationMonitoringType(
    nodeId="ns=machine_tool;i=122",
    browseName="ns=machine_tool;MachineTool",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=263", browseName="ns=machine_tool;OperationMode", dataType=machine_tool_datypes.MachineOperationMode)
        ),
        o6.hasAddIn(o6.ns["ns=machine_tool;i=5011"]),
        o6.hasAddIn(o6.ns["ns=machine_tool;i=5012"]),
        o6.hasAddIn(o6.ns["ns=machine_tool;i=5069"]),
    ],
)
machine_tool_objtypes.MonitoringType(
    nodeId="ns=machine_tool;i=123", browseName="ns=machine_tool;Monitoring", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=machine_tool;i=122"])]
)
o6.reference(machine_tool_objtypes.MachineToolType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=123"])
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=machine_tool;i=6097",
    browseName="ns=machine_tool;FeedOverride",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6098", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=6099", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
machine_tool_objtypes.ObligationType(
    nodeId="ns=machine_tool;i=5068",
    browseName="ns=machine_tool;Obligation",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=6109", browseName="ns=machine_tool;EndUserObligated", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=6110", browseName="ns=machine_tool;MachineBuilderObligated", dataType=o6.Boolean)),
    ],
)
machine_tool_objtypes.MachineOperationMonitoringType(
    nodeId="ns=machine_tool;i=119",
    browseName="ns=machine_tool;MachineTool",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=254", browseName="ns=machine_tool;OperationMode", dataType=machine_tool_datypes.MachineOperationMode)
        ),
        o6.hasComponent(o6.ns["ns=machine_tool;i=5068"]),
        o6.hasComponent(o6.ns["ns=machine_tool;i=6097"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=6106", browseName="ns=machine_tool;IsWarmUp", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=6115", browseName="ns=machine_tool;PowerOnDuration", dataType=o6.UInt32)),
        o6.hasAddIn(o6.ns["ns=machine_tool;i=5009"]),
        o6.hasAddIn(o6.ns["ns=machine_tool;i=5010"]),
        o6.hasAddIn(o6.ns["ns=machine_tool;i=5072"]),
    ],
)
o6.reference(machine_tool_objtypes.MonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=119"])
machinery.objtypes.MachineryOperationCounterType(
    nodeId="ns=machine_tool;i=5078",
    browseName="ns=di;OperationCounters",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_tool;i=6091",
                browseName="ns=di;PowerOnDuration",
                description="PowerOnDuration is the duration the MachineryItem has been powered. The main purpose is to determine the time in which degradation of the MachineryItem occurred. The details, when the time is counted, is implementation-specific. Companion specifications might define specific rules. Typically, when the MachineryItem has supply voltage and the main CPU is running, the time is counted. This may include any kind of sleep mode, but may not include pure Wake on LAN. This value shall only increase during the lifetime of the MachineryItem and shall not be reset when it is restarted. The PowerOnDuration is provided as Duration, i.e., in milliseconds or even fractions of a millisecond. However, the Server is not expected to update the value in such a high frequency, but maybe once a minute or once an hour, depending on the application.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=6118", browseName="ns=machine_tool;PartsProducedInLifetime", dataType=o6.UInt64)),
    ],
)
o6.reference(machine_tool_objtypes.MachineOperationMonitoringType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_tool;i=5078"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=6030",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_tool;i=7001",
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
    nodeId="ns=machine_tool;i=6092",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_tool;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobResponse",
            dataType=o6.NodeId("ns=bacnet;i=3013"),
            valueRank=-1,
            description=o6.LocalizedText(
                "Contains information about the execution of a job order, such as the current status of the job, actual material consumed, actual material produced, actual equipment used, and job specific data."
            ),
        ),
        ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")),
    ],
)
o6.call(
    nodeId="ns=machine_tool;i=7001",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderID",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_tool;i=6030"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_tool;i=6092"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=6093",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_tool;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="JobOrderState",
            dataType=o6.NodeId("ns=bacnet;i=3006"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "Contains a job status of the JobResponse to be returned. The array shall provide at least one entry representing the top level state and potentially additional entries representing substates. The first entry shall be the top level entry, having the BrowsePath set to null. The order of the substates is not defined."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=6096",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_tool;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobResponses",
            dataType=o6.NodeId("ns=bacnet;i=3013"),
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
    nodeId="ns=machine_tool;i=7002",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderState",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_tool;i=6093"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_tool;i=6096"]),
)

isa95_jobcontrol_v2.objtypes.ISA95JobResponseProviderObjectType(
    nodeId="ns=machine_tool;i=5024",
    browseName="ns=machinery_jobs;JobOrderResults",
    references=[o6.hasComponent(o6.ns["ns=machine_tool;i=7001"]), o6.hasComponent(o6.ns["ns=machine_tool;i=7002"])],
)
machinery_jobs.objtypes.JobManagementType(
    nodeId="ns=machine_tool;i=5022",
    browseName="ns=machinery_jobs;JobManagement",
    references=[o6.hasComponent(o6.ns["ns=machine_tool;i=5023"]), o6.hasComponent(o6.ns["ns=machine_tool;i=5024"])],
)
ns0.objtypes.FolderType(
    nodeId="ns=machine_tool;i=5004", browseName="ns=machinery;MachineryBuildingBlocks", modellingRule="Optional", references=[o6.hasAddIn(o6.ns["ns=machine_tool;i=5022"])]
)
o6.reference(machine_tool_objtypes.MachineToolType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5004"])
o6.reference(o6.ns["ns=machine_tool;i=5004"], "i=17604", o6.ns["ns=machine_tool;i=5011"])
o6.reference(o6.ns["ns=machine_tool;i=5004"], "i=17604", o6.ns["ns=machine_tool;i=5012"])
o6.reference(o6.ns["ns=machine_tool;i=5004"], "i=17604", o6.ns["ns=machine_tool;i=5069"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=6100",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_tool;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DirectoryName", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=6101",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_tool;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DirectoryNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_tool;i=7003",
    browseName="CreateDirectory",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_tool;i=6100"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_tool;i=6101"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=6102",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_tool;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileName", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="RequestFileOpen", dataType=o6.Boolean, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=6103",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_tool;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_tool;i=7004", browseName="CreateFile", inputArgs=o6.hasProperty(o6.ns["ns=machine_tool;i=6102"]), outputArgs=o6.hasProperty(o6.ns["ns=machine_tool;i=6103"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=6104",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_tool;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ObjectToDelete", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=machine_tool;i=7005", browseName="Delete", inputArgs=o6.hasProperty(o6.ns["ns=machine_tool;i=6104"]))

ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=6105",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_tool;i=7006",
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
    nodeId="ns=machine_tool;i=6107",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_tool;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NewNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_tool;i=7006", browseName="MoveOrCopy", inputArgs=o6.hasProperty(o6.ns["ns=machine_tool;i=6105"]), outputArgs=o6.hasProperty(o6.ns["ns=machine_tool;i=6107"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=6108",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_tool;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DirectoryName", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=6111",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_tool;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DirectoryNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_tool;i=7007",
    browseName="CreateDirectory",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_tool;i=6108"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_tool;i=6111"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=6112",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_tool;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileName", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="RequestFileOpen", dataType=o6.Boolean, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=6113",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_tool;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_tool;i=7008", browseName="CreateFile", inputArgs=o6.hasProperty(o6.ns["ns=machine_tool;i=6112"]), outputArgs=o6.hasProperty(o6.ns["ns=machine_tool;i=6113"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=6114",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_tool;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ObjectToDelete", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=machine_tool;i=7009", browseName="Delete", inputArgs=o6.hasProperty(o6.ns["ns=machine_tool;i=6114"]))

ns0.vartypes.PropertyType(
    nodeId="ns=machine_tool;i=6116",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_tool;i=7010",
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
    nodeId="ns=machine_tool;i=6117",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_tool;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NewNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_tool;i=7010", browseName="MoveOrCopy", inputArgs=o6.hasProperty(o6.ns["ns=machine_tool;i=6116"]), outputArgs=o6.hasProperty(o6.ns["ns=machine_tool;i=6117"])
)

ns0.objtypes.FileDirectoryType(
    nodeId="ns=machine_tool;i=5026",
    browseName="ns=machine_tool;WorkMasters",
    references=[
        o6.hasComponent(o6.ns["ns=machine_tool;i=7007"]),
        o6.hasComponent(o6.ns["ns=machine_tool;i=7008"]),
        o6.hasComponent(o6.ns["ns=machine_tool;i=7009"]),
        o6.hasComponent(o6.ns["ns=machine_tool;i=7010"]),
    ],
)
ns0.objtypes.FileDirectoryType(
    nodeId="ns=machine_tool;i=5025",
    browseName="FileSystem",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=machine_tool;i=5026"]),
        o6.hasComponent(o6.ns["ns=machine_tool;i=7003"]),
        o6.hasComponent(o6.ns["ns=machine_tool;i=7004"]),
        o6.hasComponent(o6.ns["ns=machine_tool;i=7005"]),
        o6.hasComponent(o6.ns["ns=machine_tool;i=7006"]),
    ],
)
o6.reference(machine_tool_objtypes.MachineToolType, ns0.reftypes.HasComponent, o6.ns["ns=machine_tool;i=5025"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, ns0, machine_tool_datypes, machine_tool_vartypes, machine_tool_objtypes
