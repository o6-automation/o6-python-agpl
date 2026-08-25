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

"""Generated OPC UA plastics_imm2mes namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_imm2mes_datypes
from . import objtypes as plastics_imm2mes_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6003",
    browseName="ns=plastics_rubber;NominalParts",
    description="Total number (sum of all cavities) of parts that shall be produced by the job",
    dataType=o6.UInt64,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=plastics_imm2mes;i=6003"], "i=41", "ns=plastics_rubber;i=1025")
plastics_rubber.objtypes.UsersType(
    nodeId="ns=plastics_imm2mes;i=5010",
    browseName="ns=plastics_rubber;Users",
    description="Container for the user(s) of the machine",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6009", browseName="NodeVersion", dataType=o6.String, value="\n      "))],
)
oPC40077 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_imm2mes;i=6012",
    browseName="ns=plastics_imm2mes;OPC40077",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/IMM2MES/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6013",
                browseName="NamespaceUri",
                description="A URI that uniquely identifies the dictionary.",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/IMM2MES/",
            )
        )
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/IMM2MES/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/PlasticsRubber/IMM2MES/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:EnumeratedType LengthInBits="32" Name="IMMMessageClassificationEnumeration">\n  <opc:Documentation>This Enumeration specifies the values to be used in the Classification property in the MessageConditionType and related logbook events of OPC 40083</opc:Documentation>\n  <opc:EnumeratedValue Name="OTHER" Value="0"/>\n  <opc:EnumeratedValue Name="IMM_INJECTION_UNIT" Value="100"/>\n  <opc:EnumeratedValue Name="IMM_CLAMPING_UNIT" Value="101"/>\n  <opc:EnumeratedValue Name="IMM_HARDWARE" Value="102"/>\n  <opc:EnumeratedValue Name="IMM_COMPRESSED_AIR_CONTROL" Value="103"/>\n  <opc:EnumeratedValue Name="IMM_MACHINE_MONITORING" Value="104"/>\n  <opc:EnumeratedValue Name="IMM_MOULD" Value="105"/>\n  <opc:EnumeratedValue Name="IMM_EJECTOR" Value="106"/>\n  <opc:EnumeratedValue Name="IMM_CORE_PULL" Value="107"/>\n  <opc:EnumeratedValue Name="IMM_TABLE" Value="108"/>\n  <opc:EnumeratedValue Name="IMM_INJECTION_PROGRAM" Value="109"/>\n  <opc:EnumeratedValue Name="IMM_HYDRAULIC_TEMPERATURE_CONTROL" Value="110"/>\n  <opc:EnumeratedValue Name="IMM_CYLINDER_TEMPERATURE_CONTROL" Value="111"/>\n  <opc:EnumeratedValue Name="IMM_MOULD_TEMPERATURE_CONTROL" Value="112"/>\n  <opc:EnumeratedValue Name="IMM_HOT_RUNNER" Value="113"/>\n  <opc:EnumeratedValue Name="IMM_INTERFACES" Value="114"/>\n  <opc:EnumeratedValue Name="IMM_MEASURING_SYSTEM" Value="115"/>\n  <opc:EnumeratedValue Name="IMM_ROBOTIC_SYSTEM_INTERFACE" Value="116"/>\n  <opc:EnumeratedValue Name="IMM_SPECIAL_PURPOSE_SIGNALS" Value="117"/>\n  <opc:EnumeratedValue Name="IMM_REAL_TIME_ETHERNET_SYSTEM" Value="118"/>\n  <opc:EnumeratedValue Name="IMM_MACHINE_CONTROLLER" Value="119"/>\n  <opc:EnumeratedValue Name="IMM_SOFTWARE_MONITORING" Value="120"/>\n  <opc:EnumeratedValue Name="PERIPHERAL_EXTERNAL_DEVICE_INTERFACE" Value="200"/>\n  <opc:EnumeratedValue Name="PERIPHERAL_TEMPERATURE_CONTROL_UNIT" Value="201"/>\n  <opc:EnumeratedValue Name="PERIPHERAL_ROBOTICS_SYSTEM" Value="202"/>\n  <opc:EnumeratedValue Name="PERIPHERAL_LSR" Value="203"/>\n  <opc:EnumeratedValue Name="PERIPHERAL_STRIPPER_UNIT" Value="204"/>\n  <opc:EnumeratedValue Name="PERIPHERAL_DRYER" Value="205"/>\n  <opc:EnumeratedValue Name="PERIPHERAL_CONVEYOR_BELT" Value="206"/>\n  <opc:EnumeratedValue Name="PERIPHERAL_SORTER_UNIT" Value="207"/>\n  <opc:EnumeratedValue Name="PERIPHERAL_COLOURING_UNIT" Value="208"/>\n  <opc:EnumeratedValue Name="PERIPHERAL_FEEDING" Value="209"/>\n  <opc:EnumeratedValue Name="PERIPHERAL_EXTERNAL_ALARMS" Value="210"/>\n  <opc:EnumeratedValue Name="PERIPHERAL_VACUUM_CONTROL" Value="211"/>\n  <opc:EnumeratedValue Name="PERIPHERAL_PRINTER_INTERFACE" Value="212"/>\n  <opc:EnumeratedValue Name="OPERATION_QUALITY_MONITORING" Value="300"/>\n  <opc:EnumeratedValue Name="OPERATION_MANUAL_OPERATION" Value="301"/>\n  <opc:EnumeratedValue Name="OPERATION_EMERGENCY_STOP" Value="302"/>\n  <opc:EnumeratedValue Name="OPERATION_JOB_STATUS" Value="303"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
plastics_rubber.objtypes.MESMessageType(
    nodeId="ns=plastics_imm2mes;i=5012",
    browseName="ns=plastics_rubber;MESMessage",
    description="Text message sent from the MES to be shown on the machine",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6010", browseName="ns=plastics_rubber;Id", description="Id of the message", dataType=o6.String, value="\n      "
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6011", browseName="ns=plastics_rubber;Message", description="Text of the message", dataType=o6.String, value="\n      "
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6014", browseName="Severity", description="Severity of the message", dataType=o6.UInt16, value=0)),
    ],
)
o6.reference(o6.ns["ns=plastics_imm2mes;i=5012"], "i=41", "ns=plastics_rubber;i=1004")
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6049",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=3004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[39],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OTHER")),
        ns0.datatypes.EnumValueType(value=100, displayName=o6.LocalizedText("IMM_INJECTION_UNIT")),
        ns0.datatypes.EnumValueType(value=101, displayName=o6.LocalizedText("IMM_CLAMPING_UNIT")),
        ns0.datatypes.EnumValueType(value=102, displayName=o6.LocalizedText("IMM_HARDWARE")),
        ns0.datatypes.EnumValueType(value=103, displayName=o6.LocalizedText("IMM_COMPRESSED_AIR_CONTROL")),
        ns0.datatypes.EnumValueType(value=104, displayName=o6.LocalizedText("IMM_MACHINE_MONITORING")),
        ns0.datatypes.EnumValueType(value=105, displayName=o6.LocalizedText("IMM_MOULD")),
        ns0.datatypes.EnumValueType(value=106, displayName=o6.LocalizedText("IMM_EJECTOR")),
        ns0.datatypes.EnumValueType(value=107, displayName=o6.LocalizedText("IMM_CORE_PULL")),
        ns0.datatypes.EnumValueType(value=108, displayName=o6.LocalizedText("IMM_TABLE")),
        ns0.datatypes.EnumValueType(value=109, displayName=o6.LocalizedText("IMM_INJECTION_PROGRAM")),
        ns0.datatypes.EnumValueType(value=110, displayName=o6.LocalizedText("IMM_HYDRAULIC_TEMPERATURE_CONTROL")),
        ns0.datatypes.EnumValueType(value=111, displayName=o6.LocalizedText("IMM_CYLINDER_TEMPERATURE_CONTROL")),
        ns0.datatypes.EnumValueType(value=112, displayName=o6.LocalizedText("IMM_MOULD_TEMPERATURE_CONTROL")),
        ns0.datatypes.EnumValueType(value=113, displayName=o6.LocalizedText("IMM_HOT_RUNNER")),
        ns0.datatypes.EnumValueType(value=114, displayName=o6.LocalizedText("IMM_INTERFACES")),
        ns0.datatypes.EnumValueType(value=115, displayName=o6.LocalizedText("IMM_MEASURING_SYSTEM")),
        ns0.datatypes.EnumValueType(value=116, displayName=o6.LocalizedText("IMM_ROBOTIC_SYSTEM_INTERFACE")),
        ns0.datatypes.EnumValueType(value=117, displayName=o6.LocalizedText("IMM_SPECIAL_PURPOSE_SIGNALS")),
        ns0.datatypes.EnumValueType(value=118, displayName=o6.LocalizedText("IMM_REAL_TIME_ETHERNET_SYSTEM")),
        ns0.datatypes.EnumValueType(value=119, displayName=o6.LocalizedText("IMM_MACHINE_CONTROLLER")),
        ns0.datatypes.EnumValueType(value=120, displayName=o6.LocalizedText("IMM_SOFTWARE_MONITORING")),
        ns0.datatypes.EnumValueType(value=200, displayName=o6.LocalizedText("PERIPHERAL_EXTERNAL_DEVICE_INTERFACE")),
        ns0.datatypes.EnumValueType(value=201, displayName=o6.LocalizedText("PERIPHERAL_TEMPERATURE_CONTROL_UNIT")),
        ns0.datatypes.EnumValueType(value=202, displayName=o6.LocalizedText("PERIPHERAL_ROBOTICS_SYSTEM")),
        ns0.datatypes.EnumValueType(value=203, displayName=o6.LocalizedText("PERIPHERAL_LSR")),
        ns0.datatypes.EnumValueType(value=204, displayName=o6.LocalizedText("PERIPHERAL_STRIPPER_UNIT")),
        ns0.datatypes.EnumValueType(value=205, displayName=o6.LocalizedText("PERIPHERAL_DRYER")),
        ns0.datatypes.EnumValueType(value=206, displayName=o6.LocalizedText("PERIPHERAL_CONVEYOR_BELT")),
        ns0.datatypes.EnumValueType(value=207, displayName=o6.LocalizedText("PERIPHERAL_SORTER_UNIT")),
        ns0.datatypes.EnumValueType(value=208, displayName=o6.LocalizedText("PERIPHERAL_COLOURING_UNIT")),
        ns0.datatypes.EnumValueType(value=209, displayName=o6.LocalizedText("PERIPHERAL_FEEDING")),
        ns0.datatypes.EnumValueType(value=210, displayName=o6.LocalizedText("PERIPHERAL_EXTERNAL_ALARMS")),
        ns0.datatypes.EnumValueType(value=211, displayName=o6.LocalizedText("PERIPHERAL_VACUUM_CONTROL")),
        ns0.datatypes.EnumValueType(value=212, displayName=o6.LocalizedText("PERIPHERAL_PRINTER_INTERFACE")),
        ns0.datatypes.EnumValueType(value=300, displayName=o6.LocalizedText("OPERATION_QUALITY_MONITORING")),
        ns0.datatypes.EnumValueType(value=301, displayName=o6.LocalizedText("OPERATION_MANUAL_OPERATION")),
        ns0.datatypes.EnumValueType(value=302, displayName=o6.LocalizedText("OPERATION_EMERGENCY_STOP")),
        ns0.datatypes.EnumValueType(value=303, displayName=o6.LocalizedText("OPERATION_JOB_STATUS")),
    ],
)
oPC40077_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_imm2mes;i=6050",
    browseName="ns=plastics_imm2mes;OPC40077",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/IMM2MES/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6051",
                browseName="NamespaceUri",
                description="A URI that uniquely identifies the dictionary.",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/IMM2MES/Types.xsd",
            )
        )
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/PlasticsRubber/IMM2MES/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/IMM2MES/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="IMMMessageClassificationEnumeration">\n  <xs:annotation>\n   <xs:documentation>This Enumeration specifies the values to be used in the Classification property in the MessageConditionType and related logbook events of OPC 40083</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OTHER_0"/>\n   <xs:enumeration value="IMM_INJECTION_UNIT_100"/>\n   <xs:enumeration value="IMM_CLAMPING_UNIT_101"/>\n   <xs:enumeration value="IMM_HARDWARE_102"/>\n   <xs:enumeration value="IMM_COMPRESSED_AIR_CONTROL_103"/>\n   <xs:enumeration value="IMM_MACHINE_MONITORING_104"/>\n   <xs:enumeration value="IMM_MOULD_105"/>\n   <xs:enumeration value="IMM_EJECTOR_106"/>\n   <xs:enumeration value="IMM_CORE_PULL_107"/>\n   <xs:enumeration value="IMM_TABLE_108"/>\n   <xs:enumeration value="IMM_INJECTION_PROGRAM_109"/>\n   <xs:enumeration value="IMM_HYDRAULIC_TEMPERATURE_CONTROL_110"/>\n   <xs:enumeration value="IMM_CYLINDER_TEMPERATURE_CONTROL_111"/>\n   <xs:enumeration value="IMM_MOULD_TEMPERATURE_CONTROL_112"/>\n   <xs:enumeration value="IMM_HOT_RUNNER_113"/>\n   <xs:enumeration value="IMM_INTERFACES_114"/>\n   <xs:enumeration value="IMM_MEASURING_SYSTEM_115"/>\n   <xs:enumeration value="IMM_ROBOTIC_SYSTEM_INTERFACE_116"/>\n   <xs:enumeration value="IMM_SPECIAL_PURPOSE_SIGNALS_117"/>\n   <xs:enumeration value="IMM_REAL_TIME_ETHERNET_SYSTEM_118"/>\n   <xs:enumeration value="IMM_MACHINE_CONTROLLER_119"/>\n   <xs:enumeration value="IMM_SOFTWARE_MONITORING_120"/>\n   <xs:enumeration value="PERIPHERAL_EXTERNAL_DEVICE_INTERFACE_200"/>\n   <xs:enumeration value="PERIPHERAL_TEMPERATURE_CONTROL_UNIT_201"/>\n   <xs:enumeration value="PERIPHERAL_ROBOTICS_SYSTEM_202"/>\n   <xs:enumeration value="PERIPHERAL_LSR_203"/>\n   <xs:enumeration value="PERIPHERAL_STRIPPER_UNIT_204"/>\n   <xs:enumeration value="PERIPHERAL_DRYER_205"/>\n   <xs:enumeration value="PERIPHERAL_CONVEYOR_BELT_206"/>\n   <xs:enumeration value="PERIPHERAL_SORTER_UNIT_207"/>\n   <xs:enumeration value="PERIPHERAL_COLOURING_UNIT_208"/>\n   <xs:enumeration value="PERIPHERAL_FEEDING_209"/>\n   <xs:enumeration value="PERIPHERAL_EXTERNAL_ALARMS_210"/>\n   <xs:enumeration value="PERIPHERAL_VACUUM_CONTROL_211"/>\n   <xs:enumeration value="PERIPHERAL_PRINTER_INTERFACE_212"/>\n   <xs:enumeration value="OPERATION_QUALITY_MONITORING_300"/>\n   <xs:enumeration value="OPERATION_MANUAL_OPERATION_301"/>\n   <xs:enumeration value="OPERATION_EMERGENCY_STOP_302"/>\n   <xs:enumeration value="OPERATION_JOB_STATUS_303"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:IMMMessageClassificationEnumeration" name="IMMMessageClassificationEnumeration"/>\n <xs:complexType name="ListOfIMMMessageClassificationEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:IMMMessageClassificationEnumeration" name="IMMMessageClassificationEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfIMMMessageClassificationEnumeration" name="ListOfIMMMessageClassificationEnumeration" nillable="true"/>\n</xs:schema>\n',
)
plastics_rubber.objtypes.StandstillMessageType(
    nodeId="ns=plastics_imm2mes;i=5016",
    browseName="ns=plastics_rubber;StandstillMessage",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6052", browseName="ns=plastics_rubber;Classification", description="Classification of the message", dataType=ns0.datatypes.Enumeration
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6053", browseName="ns=plastics_rubber;Id", description="Id of the message", dataType=o6.String, value="\n      "
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6054", browseName="Message", description="Text of the message", dataType=o6.LocalizedText, value=o6.LocalizedText()
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6055", browseName="Severity", description="Severity of the message", dataType=o6.UInt16, value=0)),
    ],
)
o6.reference(o6.ns["ns=plastics_imm2mes;i=5016"], "i=41", "ns=plastics_rubber;i=1004")
plastics_imm2mes_objtypes.InjectionUnitsType(
    nodeId="ns=plastics_imm2mes;i=5029",
    browseName="ns=plastics_imm2mes;InjectionUnits",
    description="Container for the injection units",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6056", browseName="NodeVersion", dataType=o6.String, value="\n      "))],
)
o6.reference(plastics_imm2mes_objtypes.IMM_MES_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=5029"])
plastics_rubber.objtypes.TemperatureZonesType(
    nodeId="ns=plastics_imm2mes;i=5017",
    browseName="ns=plastics_imm2mes;TemperatureZones",
    description="container for the barrel temperature zones of the injection unit",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6057", browseName="NodeVersion", dataType=o6.String, value="\n      "))],
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=5017"])
plastics_rubber.objtypes.TemperatureZonesType(
    nodeId="ns=plastics_imm2mes;i=5018",
    browseName="ns=plastics_imm2mes;TemperatureZones",
    description="container for the barrel temperature zones of the injection unit",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6058", browseName="NodeVersion", dataType=o6.String, value="\n      "))],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6061",
    browseName="ns=plastics_imm2mes;InjectionSpeedMaximum",
    description="Maximum injection speed (e.g. mm/s)",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6032", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6062", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6061"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6065",
    browseName="ns=plastics_imm2mes;InjectionSpeedAverage",
    description="Average injection speed (e.g. mm/s)",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6016", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6066", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6065"])
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6073",
    browseName="ns=plastics_rubber;StandstillReasonId",
    description="Id of the StandstillReason set by the operator after a standstill occurs",
    dataType=o6.String,
    value="\n      ",
)
o6.reference(o6.ns["ns=plastics_imm2mes;i=6073"], "i=41", "ns=plastics_rubber;i=1004")
plastics_rubber.objtypes.MouldsType(
    nodeId="ns=plastics_imm2mes;i=5035",
    browseName="ns=plastics_imm2mes;Moulds",
    description="Container for the moulds",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6074", browseName="NodeVersion", dataType=o6.String, value="\n      "))],
)
o6.reference(plastics_imm2mes_objtypes.IMM_MES_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=5035"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6067",
    browseName="ns=plastics_imm2mes;PlastificationSpecificPressureAverage",
    description="Average plastification pressure in front of the screw tip",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6068", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6081", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6067"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6069",
    browseName="ns=plastics_imm2mes;PlastificationSpecificPressureMaximum",
    description="Maximum plastification pressure in front of the screw tip",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6070", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6082", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6069"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6071",
    browseName="ns=plastics_imm2mes;TransferStroke",
    description="Switch-over point to the holding pressure via stroke",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6072", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6083", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6071"])
plastics_rubber.objtypes.MachineMESConfigurationType(
    nodeId="ns=plastics_imm2mes;i=5009",
    browseName="ns=plastics_imm2mes;MachineMESConfiguration",
    description="Current configuration of a machine related to a Manufacturing Execution System (MES)",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6043",
                browseName="ns=plastics_rubber;StandstillReasons",
                description="List of the standstill reasons from which one is selected by the operator in the case of a standstill",
                dataType=plastics_rubber.datatypes.StandstillReasonType,
                valueRank=1,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6044",
                browseName="ns=plastics_rubber;StandstillReasonsLockedByMES",
                description="Indication if the list StandstillReasons has been modified by the MES and may not be changed by the machine",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6085",
                browseName="ns=plastics_rubber;MESUrl",
                description="URL to display a webpage generated by the MES in a web browser integrated in the machine",
                dataType=o6.String,
                value="0",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(plastics_imm2mes_objtypes.IMM_MES_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=5009"])
plastics_rubber.objtypes.PowerUnitsType(
    nodeId="ns=plastics_imm2mes;i=5054",
    browseName="ns=plastics_imm2mes;PowerUnits",
    description="Container for the power units",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6086", browseName="NodeVersion", dataType=o6.String, value="\n      "))],
)
o6.reference(plastics_imm2mes_objtypes.IMM_MES_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=5054"])
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6094",
    browseName="ns=plastics_rubber;NominalParts",
    description="Total number (sum of all cavities) of parts that shall be produced by the job",
    dataType=o6.UInt64,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=plastics_imm2mes;i=6094"], "i=41", "ns=plastics_rubber;i=1025")
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6118",
    browseName="ns=plastics_imm2mes;BackPressure",
    description="Back pressure is the melt-pressure against the screw movement during dosage",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6119", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6120",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6118"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6093",
    browseName="ns=plastics_imm2mes;CushionStroke",
    description="Stroke position at cushion",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6121", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6122", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6093"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPlasticsRubberSlashIMM2MESSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=plastics_imm2mes;i=5021",
    browseName="ns=plastics_imm2mes;http://opcfoundation.org/UA/PlasticsRubber/IMM2MES/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6141", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6142", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2020-06-01T00:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6143", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PlasticsRubber/IMM2MES/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6154", browseName="NamespaceVersion", dataType=o6.String, value="1.01")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6155",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6158", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6159", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6160",
    browseName="ns=plastics_imm2mes;FlowIndex",
    description="Flow index",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6163", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6168", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6160"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6164",
    browseName="ns=plastics_imm2mes;InjectionStartPosition",
    description="Start position of the injection",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6165", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6169", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6164"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6166",
    browseName="ns=plastics_imm2mes;VPChangeOverPosition",
    description="Screw position at switching between injection (V) and holding pressure (P)",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6167", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6170", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6166"])
plastics_rubber.objtypes.MachineInformationType(
    nodeId="ns=plastics_imm2mes;i=5001",
    browseName="ns=plastics_imm2mes;MachineInformation",
    description="General description of the machine",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6001",
                browseName="ns=plastics_rubber;ControllerName",
                description="Name of the machine controller",
                dataType=o6.String,
                value="\n      ",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6002",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose a device is used.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6004", browseName="ns=di;Manufacturer", description="Name of the company that manufactured the device", dataType=o6.LocalizedText
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6005", browseName="ns=di;Model", description="Model name of the device", dataType=o6.LocalizedText)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6017",
                browseName="ns=di;SerialNumber",
                description="Identifier that uniquely identifies, within a manufacturer, a device instance",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6021",
                browseName="ns=plastics_rubber;SupportedLogbookEvents",
                description="Information which LogbookEvents are supported by the machine",
                dataType=plastics_rubber.datatypes.LogbookEventsEnumeration,
                valueRank=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6022", browseName="ns=di;AssetId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6023", browseName="ns=di;ComponentName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6024", browseName="ns=di;DeviceManual", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6025", browseName="ns=di;DeviceRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6084", browseName="ns=di;HardwareRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6161", browseName="ns=di;ManufacturerUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6171", browseName="ns=di;ProductCode", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6172", browseName="ns=di;ProductInstanceUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6173", browseName="ns=di;RevisionCounter", dataType=o6.Int32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6174", browseName="ns=di;SoftwareRevision", dataType=o6.String)),
    ],
)
o6.reference(plastics_imm2mes_objtypes.IMM_MES_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=5001"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6180",
    browseName="ns=plastics_imm2mes;MaxScrewStroke",
    description="maximum stroke of the screw installed in the injection unit",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6181", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6182", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6186",
    browseName="ns=plastics_imm2mes;ScrewVolume",
    description="volume of the screw installed in the injection unit",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6031",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6187", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6194",
    browseName="ns=plastics_imm2mes;PlastificationHydraulicPressureAverage",
    description="Average plastification pressure in cylinder",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6080", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6195", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6194"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6104",
    browseName="ns=plastics_imm2mes;ScrewVolume",
    description="volume of the screw installed in the injection unit",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6105", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6251",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6104"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6183",
    browseName="ns=plastics_imm2mes;ScrewDiameter",
    description="diameter of the screw installed in the injection unit",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6184", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6252",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_imm2mes_objtypes.InjectionUnitType(
    nodeId="ns=plastics_imm2mes;i=5027",
    browseName="ns=plastics_imm2mes;InjectionUnit_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6018",
                browseName="ns=plastics_imm2mes;BarrelId",
                description="Id (e.g. serial number) of the barrel",
                dataType=o6.String,
                value="\n      ",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6157", browseName="ns=plastics_imm2mes;Index", description="Number of the injection unit", dataType=o6.UInt32, value=0
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6178",
                browseName="ns=plastics_imm2mes;InProduction",
                description="information if the injection unit is used in the current running production",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6179",
                browseName="ns=plastics_imm2mes;IsPresent",
                description="Information if the injection unit is physically installed on the injection machines",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6185",
                browseName="ns=plastics_imm2mes;ScrewId",
                description="Id of the screw installed in the injection unit",
                dataType=o6.String,
                value="\n      ",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=5018"]),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=6180"]),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=6183"]),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=6186"]),
    ],
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitsType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=5027"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6117",
    browseName="ns=plastics_imm2mes;TransferCavityPressure",
    description="Cavity pressure in the mould during switch-over to the holding pressure",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6128", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6428",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6117"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6129",
    browseName="ns=plastics_imm2mes;CavityPressureMaximum",
    description="Maximum pressure during the injection process in the cavity or mould",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6130", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6448",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6129"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6131",
    browseName="ns=plastics_imm2mes;DecompressionVolumeAfterPlastification",
    description="Decompression after plastification is the movement of the screw in the opposite direction to injection",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6132", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6449",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6131"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6064",
    browseName="ns=plastics_imm2mes;DecompressionVolumeBeforePlastification",
    description="Decompression before plastification is the movement of the screw in the opposite direction to injection",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6136", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6450",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6064"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6146",
    browseName="ns=plastics_imm2mes;HoldHydraulicPressureAverage",
    description="Average holding pressure in the hydraulic cylinder",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6147", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6454",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6146"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6148",
    browseName="ns=plastics_imm2mes;HoldHydraulicPressureMaximum",
    description="Maximum holding pressure in the hydraulic cylinder",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6149", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6455",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6148"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6150",
    browseName="ns=plastics_imm2mes;HoldSpecificPressureAverage",
    description="Average holding pressure in front of the screw",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6151", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6456",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6150"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6152",
    browseName="ns=plastics_imm2mes;HoldSpecificPressureMaximum",
    description="Maximum holding pressure in front of the screw",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6153", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6457",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6152"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6156",
    browseName="ns=plastics_imm2mes;TransferHydraulicPressure",
    description="Hydraulic pressure in the cylinder during switch-over to the holding pressure",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6162", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6458",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6156"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6188",
    browseName="ns=plastics_imm2mes;HydraulicPressureMaximum",
    description="Maximum pressure in the hydraulic cylinder",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6191", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6459",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6188"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6197",
    browseName="ns=plastics_imm2mes;PlastificationHydraulicPressureMaximum",
    description="Maximum plastification pressure in cylinder",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6206", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6471",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6197"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6208",
    browseName="ns=plastics_imm2mes;PlastificationCircumferentialSpeedAverage",
    description="Average screw circumferential speed for plastification (e.g. mm/s)",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6210", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6472",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6208"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6211",
    browseName="ns=plastics_imm2mes;PlastificationCircumferentialSpeedMaximum",
    description="Maximum screw circumferential speed for plastification (e.g. mm/s)",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6214", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6473",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6211"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6223",
    browseName="ns=plastics_imm2mes;PlastificationRotationalSpeedAverage",
    description="Average plastification speed of the injection unit (RPM)",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6224", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6474",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6223"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6441",
    browseName="ns=plastics_imm2mes;CushionVolume",
    description="Material volume remained in front of the screw after injection and holding pressure",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6442", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6475", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6441"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6225",
    browseName="ns=plastics_imm2mes;PlastificationRotationalSpeedMaximum",
    description="Maximum plastification speed of the injection unit (RPM)",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6226", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6476",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6225"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6063",
    browseName="ns=plastics_imm2mes;PlastificationVolume",
    description="Volume dosed by the machine for the next injection shot",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6227", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6477",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6063"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6228",
    browseName="ns=plastics_imm2mes;TransferSpecificPressure",
    description="Pressure in front of the screw tip during switch-over to the holding pressure",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6246", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6478",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6228"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6247",
    browseName="ns=plastics_imm2mes;SpecificPressureMaximum",
    description="Pressure in front of the screw tip",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6248", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6479",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6247"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6254",
    browseName="ns=plastics_imm2mes;TransferVolume",
    description="Switch-over point to the holding pressure via volume",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6427", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6481",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitCycleParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6254"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6102",
    browseName="ns=plastics_imm2mes;MaxScrewStroke",
    description="maximum stroke of the screw installed in the injection unit",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6103", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6689", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6102"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_imm2mes;i=6100",
    browseName="ns=plastics_imm2mes;ScrewDiameter",
    description="diameter of the screw installed in the injection unit",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6101", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6691",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_imm2mes_objtypes.InjectionUnitType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=6100"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6027",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6028",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_imm2mes;i=7001",
    browseName="CloseAndCommit",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6027"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6028"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6041",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=plastics_rubber;i=3007"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6042",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=plastics_imm2mes;i=7002",
    browseName="GenerateFileForRead",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6041"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6042"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6116",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=plastics_rubber;i=3004"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6123",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_imm2mes;i=7003",
    browseName="GenerateFileForWrite",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6116"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6123"]),
)

ns0.objtypes.TemporaryFileTransferType(
    nodeId="ns=plastics_imm2mes;i=5008",
    browseName="ns=plastics_rubber;ProductionDatasetTransfer",
    description="Transfer of production datasets between server and client",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_imm2mes;i=6026", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=7001"]),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=7002"]),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=7003"]),
    ],
    eventNotifier=1,
)
o6.reference(o6.ns["ns=plastics_imm2mes;i=5008"], "i=41", "ns=plastics_rubber;i=1006")
o6.reference(o6.ns["ns=plastics_imm2mes;i=5008"], "i=41", "ns=plastics_rubber;i=1007")
o6.reference(o6.ns["ns=plastics_imm2mes;i=5008"], "i=41", "ns=plastics_rubber;i=1040")


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6124",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="fileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6125",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Information", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_imm2mes;i=7004",
    browseName="ns=plastics_rubber;GetProductionDatasetInformation",
    description="This Method allows reading the description of a production dataset during the file transfer from the server to the client with ProductionDatasetTransfer",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6124"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6125"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6030",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="DateTime", dataType=o6.DateTime, valueRank=-1),
        ns0.datatypes.Argument(name="TimeZoneOffset", dataType=ns0.datatypes.TimeZoneDataType, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=plastics_imm2mes;i=7005",
    browseName="ns=plastics_rubber;SetMachineTime",
    description="Method for setting the server time together with TimeZoneOffset",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6030"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6048",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Message", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Severity", dataType=o6.UInt16, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=plastics_imm2mes;i=7009",
    browseName="ns=plastics_rubber;SetMESMessage",
    description="Method for setting the MESMessage",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6048"]),
)

plastics_rubber.objtypes.MachineStatusType(
    nodeId="ns=plastics_imm2mes;i=5006",
    browseName="ns=plastics_imm2mes;MachineStatus",
    description="Information on the current status of the machine",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6007",
                browseName="ns=plastics_rubber;IsPresent",
                description="Indication if the machine is physically present and connected",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6008",
                browseName="ns=plastics_rubber;MachineMode",
                description="Current machine mode (as defined by mode selector on the machine)",
                dataType=plastics_rubber.datatypes.MachineModeEnumeration,
                value=plastics_rubber.datatypes.MachineModeEnumeration.OTHER,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=5010"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_imm2mes;i=7010", browseName="ns=plastics_rubber;ActivateSleepMode", description="Method for activation of sleep mode")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_imm2mes;i=7011", browseName="ns=plastics_rubber;DeactivateSleepMode", description="Method for deactivation of sleep mode")),
    ],
)
o6.reference(plastics_imm2mes_objtypes.IMM_MES_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=5006"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6137",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="NameFilter", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="MouldId", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6138",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductionDatasetList", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=1)],
)
o6.call(
    nodeId="ns=plastics_imm2mes;i=7012",
    browseName="ns=plastics_rubber;GetProductionDatasetList",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6137"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6138"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6139",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductionDatasetList", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=1)],
)
o6.call(nodeId="ns=plastics_imm2mes;i=7013", browseName="ns=plastics_rubber;SendProductionDatasetList", inputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6139"]))

plastics_rubber.objtypes.ProductionDatasetListsType(
    nodeId="ns=plastics_imm2mes;i=5020",
    browseName="ns=plastics_rubber;ProductionDatasetLists",
    description="Functions for exchanging information on the available production datasets on client and server",
    references=[o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=7012"]), o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=7013"])],
    eventNotifier=1,
)
o6.reference(o6.ns["ns=plastics_imm2mes;i=5020"], "i=41", "ns=plastics_rubber;i=1040")


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6114",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="JobList", dataType=o6.NodeId("ns=plastics_rubber;i=3022"), valueRank=1)],
)
o6.call(
    nodeId="ns=plastics_imm2mes;i=7017",
    browseName="ns=plastics_rubber;SendCyclicJobList",
    description="Sends a list of jobs for cyclic processes available on the client to the server",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6114"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6140",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="fileHandle", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="Information", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=plastics_imm2mes;i=7018",
    browseName="ns=plastics_rubber;SendProductionDatasetInformation",
    description="This Method allows sending of the description of a production dataset during the file transfer from the client to the server with ProductionDatasetTransfer",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6140"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6019",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[14],
    value=[
        ns0.datatypes.Argument(name="JobName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="JobDescription", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="CustomerName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ProductionDatasetName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ProductionDatasetDescription", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Material", dataType=o6.String, valueRank=1),
        ns0.datatypes.Argument(name="ProductName", dataType=o6.String, valueRank=1),
        ns0.datatypes.Argument(name="ProductDescription", dataType=o6.String, valueRank=1),
        ns0.datatypes.Argument(name="ContinueAtJobEnd", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="NominalParts", dataType=o6.UInt64, valueRank=-1),
        ns0.datatypes.Argument(name="NominalBoxParts", dataType=o6.UInt64, valueRank=-1),
        ns0.datatypes.Argument(name="ExpectedCycleTime", dataType=ns0.datatypes.Duration, valueRank=-1),
        ns0.datatypes.Argument(name="MouldId", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="NumCavities", dataType=o6.UInt32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=plastics_imm2mes;i=7019",
    browseName="ns=plastics_rubber;SetCyclicJobData",
    description="Method for setting the data for cyclic jobs",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6019"]),
)

plastics_rubber.objtypes.CyclicJobInformationType(
    nodeId="ns=plastics_imm2mes;i=5002",
    browseName="ns=plastics_rubber;ActiveJob",
    description="Job that is currently active on the machine",
    references=[
        o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6003"]),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6035",
                browseName="ns=plastics_rubber;ContinueAtJobEnd",
                description="Indication if the machine continues the production even if the nominal output has been reached",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6036",
                browseName="ns=plastics_rubber;CustomerName",
                description="Name of the cumstomer for that the job is produced",
                dataType=o6.String,
                value="\n      ",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6037", browseName="ns=plastics_rubber;JobDescription", description="Description of the job", dataType=o6.String, value="\n      "
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6038", browseName="ns=plastics_rubber;JobName", description="Name of the job", dataType=o6.String, value="\n      "
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6039",
                browseName="ns=plastics_rubber;Material",
                description="Array of material names used for the job",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[1],
                value=["\n        "],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6040",
                browseName="ns=plastics_rubber;ProductDescription",
                description="Array of descriptions of the products produced by the job",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[1],
                value=["\n        "],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6045",
                browseName="ns=plastics_rubber;ProductionDatasetDescription",
                description="Additional description of the production dataset which is needed for the job",
                dataType=o6.String,
                value="\n      ",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6087",
                browseName="ns=plastics_rubber;ProductionDatasetName",
                description="Name of the production dataset which is needed for the job",
                dataType=o6.String,
                value="\n      ",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6088",
                browseName="ns=plastics_rubber;ProductName",
                description="Array of product names produced by the job",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[1],
                value=["\n        "],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6175",
                browseName="ns=plastics_rubber;ExpectedCycleTime",
                description="Calculated cycle time for the job",
                dataType=ns0.datatypes.Duration,
                value=0.0,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6176", browseName="ns=plastics_rubber;MouldId", description="Id of the Mould used for the job", dataType=o6.String, value="\n      "
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6177",
                browseName="ns=plastics_rubber;NominalBoxParts",
                description="Number of parts that shall be put into one box",
                dataType=o6.UInt64,
                value=0,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6189",
                browseName="ns=plastics_rubber;NumCavities",
                description="Number of cavities in the Mould used for production",
                dataType=o6.UInt32,
                value=0,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=7019"]),
    ],
)
o6.reference(o6.ns["ns=plastics_imm2mes;i=5002"], "i=41", "ns=plastics_rubber;i=1025")
plastics_rubber.objtypes.ActiveCyclicJobValuesType(
    nodeId="ns=plastics_imm2mes;i=5013",
    browseName="ns=plastics_rubber;ActiveJobValues",
    description="Status of the job",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6133",
                browseName="ns=plastics_rubber;CurrentLotName",
                description="Name of the current production lot",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6134",
                browseName="ns=plastics_rubber;JobStatus",
                description="Current status of the job",
                dataType=plastics_rubber.datatypes.JobStatusEnumeration,
                value=plastics_rubber.datatypes.JobStatusEnumeration.OTHER,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6196",
                browseName="ns=plastics_rubber;BoxId",
                description="Id of the box in which the current production is put in",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_imm2mes;i=6089",
                browseName="ns=plastics_rubber;JobBadPartsCounter",
                description="Number of bad parts produced in the current job",
                dataType=o6.UInt64,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_imm2mes;i=6090",
                browseName="ns=plastics_rubber;JobCycleCounter",
                description="Number of finished cycles in the job",
                dataType=o6.UInt64,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_imm2mes;i=6091",
                browseName="ns=plastics_rubber;JobGoodPartsCounter",
                description="Number of good parts produced in the current job",
                dataType=o6.UInt64,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_imm2mes;i=6092",
                browseName="ns=plastics_rubber;JobPartsCounter",
                description="Total number of parts produced in the current job",
                dataType=o6.UInt64,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_imm2mes;i=6115",
                browseName="ns=plastics_rubber;JobTestSamplesCounter",
                description="Number of test sample parts produced in the current job",
                dataType=o6.UInt64,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_imm2mes;i=6127",
                browseName="ns=plastics_rubber;LastCycleTime",
                description="Time of the recently finished cycle",
                dataType=ns0.datatypes.Duration,
                value=0.0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_imm2mes;i=6135", browseName="ns=plastics_rubber;AverageCycleTime", description="Average cycle time", dataType=ns0.datatypes.Duration, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_imm2mes;i=6190",
                browseName="ns=plastics_rubber;BoxBadPartsCounter",
                description="Number of bad parts produced in the current box",
                dataType=o6.UInt64,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_imm2mes;i=6192",
                browseName="ns=plastics_rubber;BoxCycleCounter",
                description="Number of finished cycles for the current box",
                dataType=o6.UInt64,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_imm2mes;i=6193",
                browseName="ns=plastics_rubber;BoxGoodPartsCounter",
                description="Number of good parts produced in the current box",
                dataType=o6.UInt64,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_imm2mes;i=6198",
                browseName="ns=plastics_rubber;BoxPartsCounter",
                description="Total number of parts produced in the current box",
                dataType=o6.UInt64,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_imm2mes;i=6199",
                browseName="ns=plastics_rubber;BoxTestSamplesCounter",
                description="Number of test sample parts produced in the current box",
                dataType=o6.UInt64,
                value=0,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_imm2mes;i=6200",
                browseName="ns=plastics_rubber;LastPartId",
                description="Id(s) of the parts produced in the recently finished cycle",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[1],
                value=["\n        "],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_imm2mes;i=6201",
                browseName="ns=plastics_rubber;MachineCycleCounter",
                description="Number of finished cycles in the machine life time",
                dataType=o6.UInt64,
                value=0,
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_imm2mes;i=7014", browseName="ns=plastics_rubber;ResetJobCounters", description="Setting the cycle and parts counters for the job to 0")
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_imm2mes;i=7015", browseName="ns=plastics_rubber;StopAtCycleEnd", description="Directs the machine to stop at the end of the current cycle")
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_imm2mes;i=7016",
                browseName="ns=plastics_rubber;FinishJob",
                description="With this Method the client (e.g. MES) requests the machine to change the JobStatus to JOB_FINISHED_8",
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_imm2mes;i=7020",
                browseName="ns=plastics_rubber;InterruptJob",
                description="With this Method the client (e.g. MES) requests the machine to change the JobStatus to JOB_INTERRUPTED_7",
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_imm2mes;i=7021",
                browseName="ns=plastics_rubber;StartJob",
                description="With this Method the client (e.g. MES) request the machine to change the JobStatus to JOB_IN_PRODUCTION_6",
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_imm2mes;i=7022",
                browseName="ns=plastics_rubber;ResetAverageCycleTime",
                description="Initiates a new calculation of the average cycle time for the job",
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_imm2mes;i=7023", browseName="ns=plastics_rubber;ResetBoxCounters", description="Setting the cycle and parts counters for the current box to 0"
            )
        ),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6095",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7026",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[14],
    value=[
        ns0.datatypes.Argument(name="JobName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="JobDescription", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="CustomerName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ProductionDatasetName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ProductionDatasetDescription", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Material", dataType=o6.String, valueRank=1),
        ns0.datatypes.Argument(name="ProductName", dataType=o6.String, valueRank=1),
        ns0.datatypes.Argument(name="ProductDescription", dataType=o6.String, valueRank=1),
        ns0.datatypes.Argument(name="ContinueAtJobEnd", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="NominalParts", dataType=o6.UInt64, valueRank=-1),
        ns0.datatypes.Argument(name="NominalBoxParts", dataType=o6.UInt64, valueRank=-1),
        ns0.datatypes.Argument(name="ExpectedCycleTime", dataType=ns0.datatypes.Duration, valueRank=-1),
        ns0.datatypes.Argument(name="MouldId", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="NumCavities", dataType=o6.UInt32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=plastics_imm2mes;i=7026",
    browseName="ns=plastics_rubber;SetCyclicJobData",
    description="Method for setting the data for cyclic jobs",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6095"]),
)

plastics_rubber.objtypes.CyclicJobInformationType(
    nodeId="ns=plastics_imm2mes;i=5019",
    browseName="ns=plastics_rubber;JobInPreparation",
    description="Job in a preparation layer of the machine",
    references=[
        o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6094"]),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6096",
                browseName="ns=plastics_rubber;ContinueAtJobEnd",
                description="Indication if the machine continues the production even if the nominal output has been reached",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6108",
                browseName="ns=plastics_rubber;CustomerName",
                description="Name of the cumstomer for that the job is produced",
                dataType=o6.String,
                value="\n      ",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6109", browseName="ns=plastics_rubber;JobDescription", description="Description of the job", dataType=o6.String, value="\n      "
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6110", browseName="ns=plastics_rubber;JobName", description="Name of the job", dataType=o6.String, value="\n      "
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6111",
                browseName="ns=plastics_rubber;Material",
                description="Array of material names used for the job",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[1],
                value=["\n        "],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6112",
                browseName="ns=plastics_rubber;ProductDescription",
                description="Array of descriptions of the products produced by the job",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[1],
                value=["\n        "],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6113",
                browseName="ns=plastics_rubber;ProductionDatasetDescription",
                description="Additional description of the production dataset which is needed for the job",
                dataType=o6.String,
                value="\n      ",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6144",
                browseName="ns=plastics_rubber;ProductionDatasetName",
                description="Name of the production dataset which is needed for the job",
                dataType=o6.String,
                value="\n      ",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6145",
                browseName="ns=plastics_rubber;ProductName",
                description="Array of product names produced by the job",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[1],
                value=["\n        "],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6202",
                browseName="ns=plastics_rubber;ExpectedCycleTime",
                description="Calculated cycle time for the job",
                dataType=ns0.datatypes.Duration,
                value=0.0,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6203", browseName="ns=plastics_rubber;MouldId", description="Id of the Mould used for the job", dataType=o6.String, value="\n      "
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6204",
                browseName="ns=plastics_rubber;NominalBoxParts",
                description="Number of parts that shall be put into one box",
                dataType=o6.UInt64,
                value=0,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6205",
                browseName="ns=plastics_rubber;NumCavities",
                description="Number of cavities in the Mould used for production",
                dataType=o6.UInt32,
                value=0,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=7026"]),
    ],
)
o6.reference(o6.ns["ns=plastics_imm2mes;i=5019"], "i=41", "ns=plastics_rubber;i=1025")
plastics_rubber.objtypes.JobsType(
    nodeId="ns=plastics_imm2mes;i=5004",
    browseName="ns=plastics_imm2mes;Jobs",
    description="Management of production jobs on the machine and information on their status including process parameters",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=5002"]),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=5013"]),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=5019"]),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=7017"]),
    ],
    eventNotifier=1,
)
o6.reference(plastics_imm2mes_objtypes.IMM_MES_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=5004"])
o6.reference(o6.ns["ns=plastics_imm2mes;i=5004"], "i=41", "ns=plastics_rubber;i=1028")


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6209",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7027",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="WatchDogTime", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_imm2mes;i=7027",
    browseName="ns=plastics_rubber;SetWatchDogTime",
    description="Release of production for a given time",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6209"]),
)

plastics_rubber.objtypes.ProductionControlType(
    nodeId="ns=plastics_imm2mes;i=5015",
    browseName="ns=plastics_rubber;ProductionControl",
    description="Control of the production of the machine by MES",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6015",
                browseName="ns=plastics_rubber;AutomaticRunEnabled",
                description="Indication if semi-automatic and automatic run of the machine is allowed by MES",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6046",
                browseName="ns=plastics_rubber;ProductionReleasedByMES",
                description="Indication if ProductionStatus may have the value PRODUCTION_4",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6047",
                browseName="ns=plastics_rubber;ProductionStatus",
                description="Production status when the machine is in automatic or semi-automatic mode",
                dataType=plastics_rubber.datatypes.ProductionStatusEnumeration,
                value=plastics_rubber.datatypes.ProductionStatusEnumeration.OTHER,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6207",
                browseName="ns=plastics_rubber;ProductionOnlyWithMES",
                description="Indication if production with the machine is only allowed when the MES is active",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_imm2mes;i=7007",
                browseName="ns=plastics_rubber;DisableAutomaticRun",
                description="Method for disabling the semi-automatic and automatic run of the machine",
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_imm2mes;i=7008",
                browseName="ns=plastics_rubber;EnableAutomaticRun",
                description="Method for enabling the semi-automatic and automatic run of the machine",
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_imm2mes;i=7024",
                browseName="ns=plastics_rubber;RequestTestSample",
                description="The machine shall separate a test sample (e.g. for quality check). The size of the test sample depends on the product/machine configuration.",
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_imm2mes;i=7025",
                browseName="ns=plastics_rubber;ResetWatchDog",
                description="Setting the watch dog timer to the value set by the last calling of SetWatchDogTime",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=7027"]),
    ],
)
o6.reference(o6.ns["ns=plastics_imm2mes;i=5015"], "i=41", "ns=plastics_rubber;i=1004")
plastics_rubber.objtypes.MachineMESStatusType(
    nodeId="ns=plastics_imm2mes;i=5011",
    browseName="ns=plastics_imm2mes;MachineMESStatus",
    description="Current status of a machine related to the MES",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6073"]),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=5012"]),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=5015"]),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=5016"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_imm2mes;i=7006", browseName="ns=plastics_rubber;ClearMESMessage", description="Method for clearing the MESMessage")),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=7009"]),
    ],
    eventNotifier=1,
)
o6.reference(plastics_imm2mes_objtypes.IMM_MES_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=5011"])
o6.reference(o6.ns["ns=plastics_imm2mes;i=5011"], "i=41", "ns=plastics_rubber;i=1004")


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6213",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7028",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="Components", dataType=o6.UInt16, valueRank=1)],
)
o6.call(
    nodeId="ns=plastics_imm2mes;i=7028",
    browseName="ns=plastics_rubber;Load",
    description="Loads a production dataset from the file system of the machine to the control of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6213"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6075",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="VisualisationUnit", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6076",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Page", dataType=ns0.datatypes.Image, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_imm2mes;i=7029",
    browseName="ns=plastics_rubber;GetCurrentPage",
    description="Method for retrieving a screenshot of the control system with the currently shown contents",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6075"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6076"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6077",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6078",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Page", dataType=ns0.datatypes.Image, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_imm2mes;i=7030",
    browseName="ns=plastics_rubber;GetPage",
    description="Method for retrieving the image of a page of the control system",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6077"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6078"]),
)

plastics_rubber.objtypes.MachineConfigurationType(
    nodeId="ns=plastics_imm2mes;i=5005",
    browseName="ns=plastics_imm2mes;MachineConfiguration",
    description="Current configuration of the machine",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6029",
                browseName="ns=plastics_rubber;LocationName",
                description="Description of the location of the machine given by the machine operator or OPC client",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6033",
                browseName="ns=plastics_rubber;TimeZoneOffset",
                description="Difference of the local time to Coordinated Universal Time (UTC) given by the machine operator or OPC client",
                dataType=ns0.datatypes.TimeZoneDataType,
                value=ns0.datatypes.TimeZoneDataType(offset=0, daylightSavingInOffset=False),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6034",
                browseName="ns=plastics_rubber;UserMachineName",
                description="Description of the machine given by the machine operator or OPC client",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6079",
                browseName="ns=plastics_rubber;PageDirectory",
                description="List of the pages that are implemented in the machine control system and are shown on the screen of the machine",
                dataType=plastics_rubber.datatypes.PageEntryDataType,
                valueRank=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=7005"]),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=7029"]),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=7030"]),
    ],
)
o6.reference(plastics_imm2mes_objtypes.IMM_MES_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=5005"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6216",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7031",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_imm2mes;i=7031",
    browseName="ns=plastics_rubber;Save",
    description="Stores a production dataset from the control of the machine to the file system of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6216"]),
)

plastics_rubber.objtypes.ProductionDatasetStatusType(
    nodeId="ns=plastics_imm2mes;i=5007",
    browseName="ns=plastics_rubber;ActiveProductionDatasetStatus",
    description="Status of the active production dataset",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6020",
                browseName="ns=plastics_rubber;Information",
                description="Set of information on the production dataset",
                dataType=plastics_rubber.datatypes.ProductionDatasetInformationType,
                value=plastics_rubber.datatypes.ProductionDatasetInformationType(
                    name="",
                    description="",
                    mESId="",
                    creationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    lastModificationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    lastSaveTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    userName="",
                    components=[],
                    manufacturer="",
                    serialNumber="",
                    model="",
                    controllerName="",
                    userMachineName="",
                    locationName="",
                    productName=[],
                    mouldId="",
                    numCavities=0,
                ),
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6212",
                browseName="ns=plastics_rubber;Frozen",
                description="Indication if changes on the machine in the production dataset are allowed",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6215",
                browseName="ns=plastics_rubber;Modified",
                description="Indication if the production dataset has been changed after the last storage",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=7028"]),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=7031"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6218",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7032",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="Components", dataType=o6.UInt16, valueRank=1)],
)
o6.call(
    nodeId="ns=plastics_imm2mes;i=7032",
    browseName="ns=plastics_rubber;Load",
    description="Loads a production dataset from the file system of the machine to the control of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6218"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_imm2mes;i=6220",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_imm2mes;i=7033",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_imm2mes;i=7033",
    browseName="ns=plastics_rubber;Save",
    description="Stores a production dataset from the control of the machine to the file system of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_imm2mes;i=6220"]),
)

plastics_rubber.objtypes.ProductionDatasetStatusType(
    nodeId="ns=plastics_imm2mes;i=5014",
    browseName="ns=plastics_rubber;ProductionDatasetInPreparationStatus",
    description="Status of the production dataset in the preparation layer",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6126",
                browseName="ns=plastics_rubber;Information",
                description="Set of information on the production dataset",
                dataType=plastics_rubber.datatypes.ProductionDatasetInformationType,
                value=plastics_rubber.datatypes.ProductionDatasetInformationType(
                    name="",
                    description="",
                    mESId="",
                    creationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    lastModificationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    lastSaveTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    userName="",
                    components=[],
                    manufacturer="",
                    serialNumber="",
                    model="",
                    controllerName="",
                    userMachineName="",
                    locationName="",
                    productName=[],
                    mouldId="",
                    numCavities=0,
                ),
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6217",
                browseName="ns=plastics_rubber;Frozen",
                description="Indication if changes on the machine in the production dataset are allowed",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_imm2mes;i=6219",
                browseName="ns=plastics_rubber;Modified",
                description="Indication if the production dataset has been changed after the last storage",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=7032"]),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=7033"]),
    ],
)
plastics_rubber.objtypes.ProductionDatasetManagementType(
    nodeId="ns=plastics_imm2mes;i=5003",
    browseName="ns=plastics_imm2mes;ProductionDatasetManagement",
    description="Management of production datasets",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=5007"]),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=5008"]),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=5014"]),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=5020"]),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=7004"]),
        o6.hasComponent(o6.ns["ns=plastics_imm2mes;i=7018"]),
    ],
)
o6.reference(plastics_imm2mes_objtypes.IMM_MES_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_imm2mes;i=5003"])


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_rubber, plastics_imm2mes_datypes, plastics_imm2mes_objtypes
