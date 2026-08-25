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

"""Generated OPC UA plastics_hot_runner namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_hot_runner_datypes
from . import objtypes as plastics_hot_runner_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

defaultSpaceBinary = ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_hot_runner;i=5028", browseName="Default Binary")
defaultSpaceXML = ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_hot_runner;i=5029", browseName="Default XML")
defaultSpaceJSON = ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_hot_runner;i=5030", browseName="Default JSON")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_hot_runner;i=5037", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_hot_runner;i=5038", browseName="Default XML")
o6.hasEncoding(plastics_hot_runner_datypes.TimeMethodPIDParametersDataType, o6.ns["ns=plastics_hot_runner;i=5038"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_hot_runner;i=5039", browseName="Default JSON")
o6.hasEncoding(plastics_hot_runner_datypes.TimeMethodPIDParametersDataType, o6.ns["ns=plastics_hot_runner;i=5039"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6005",
    browseName="ns=plastics_hot_runner;SetValueTemperatureChange",
    description="Specification of the set value change",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6006", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6007", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_hot_runner_objtypes.TemperatureRiseMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=6005"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6009",
    browseName="ns=plastics_hot_runner;SetValueManualOutputLimit",
    description="This pre-defined maximum output (in percent) is valid until the SetValueTemperature is reached.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6010", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6014", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_hot_runner_objtypes.HeatUpType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=6009"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6011",
    browseName="ns=plastics_hot_runner;SetValueTemperature",
    description="If ManualOutputLimitActive is set, SetValueManualOutputLimit is active until this nominal temperature value is reached.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6012", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6015", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_hot_runner_objtypes.HeatUpType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=6011"])
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_hot_runner;i=6016",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=plastics_hot_runner;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        o6.LocalizedText("CLOSED_LOOP_CONTROL"),
        o6.LocalizedText("MANUAL"),
        o6.LocalizedText("SYNCHRONOUS_ZONE"),
        o6.LocalizedText("CASCADE"),
        o6.LocalizedText("COOL_ZONE"),
        o6.LocalizedText("MEASURING_ZONE"),
        o6.LocalizedText("NOT_USED"),
    ],
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_hot_runner;i=6040", browseName="ns=plastics_hot_runner;TimeMethodPIDParametersDataType", dataType=o6.String, value="TimeMethodPIDParametersDataType"
)
o6.reference(o6.ns["ns=plastics_hot_runner;i=5037"], "i=39", o6.ns["ns=plastics_hot_runner;i=6040"])
oPC40082_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_hot_runner;i=6017",
    browseName="ns=plastics_hot_runner;OPC40082_2",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/HotRunner/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6018", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PlasticsRubber/HotRunner/"
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6040"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/HotRunner/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/PlasticsRubber/HotRunner/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="TimeMethodPIDParametersDataType">\n  <opc:Field TypeName="opc:Double" Name="Xp"/>\n  <opc:Field TypeName="opc:Double" Name="Tn"/>\n  <opc:Field TypeName="opc:Double" Name="Tv"/>\n  <opc:Field TypeName="opc:Double" Name="Ts"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="ControllerTypeEnumeration">\n  <opc:EnumeratedValue Name="CLOSED_LOOP_CONTROL" Value="0"/>\n  <opc:EnumeratedValue Name="MANUAL" Value="1"/>\n  <opc:EnumeratedValue Name="SYNCHRONOUS_ZONE" Value="2"/>\n  <opc:EnumeratedValue Name="CASCADE" Value="3"/>\n  <opc:EnumeratedValue Name="COOL_ZONE" Value="4"/>\n  <opc:EnumeratedValue Name="MEASURING_ZONE" Value="5"/>\n  <opc:EnumeratedValue Name="NOT_USED" Value="6"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ZoneStatusEnumeration">\n  <opc:EnumeratedValue Name="OTHER" Value="0"/>\n  <opc:EnumeratedValue Name="GOOD" Value="1"/>\n  <opc:EnumeratedValue Name="SENSOR_FAULT" Value="2"/>\n  <opc:EnumeratedValue Name="TEMPERATURE_SENSOR_BROKEN" Value="3"/>\n  <opc:EnumeratedValue Name="TEMPERATURE_SENSOR_REVERSED" Value="4"/>\n  <opc:EnumeratedValue Name="POWER_UNIT_FAILED" Value="5"/>\n  <opc:EnumeratedValue Name="HEATING_OUTPUT_TO_LOW" Value="6"/>\n  <opc:EnumeratedValue Name="ERROR" Value="7"/>\n  <opc:EnumeratedValue Name="WARNING" Value="8"/>\n  <opc:EnumeratedValue Name="LEAKAGE_DETECTED" Value="9"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6038",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6039", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6043", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6034",
    browseName="ns=plastics_hot_runner;ActualOutput",
    description="Indicates the currently active output in percent",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6035", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6044", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_hot_runner_objtypes.ControllerType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=6034"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6036",
    browseName="ns=plastics_hot_runner;AverageControllerOutput",
    description="Indicates the average output which can be used when a sensor is broken",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6037", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6045", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_hot_runner_objtypes.ControllerType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=6036"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6028",
    browseName="ns=plastics_hot_runner;LowerOutput",
    description="Limitation of the minimum output in closed-loop control in %",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6029", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6046", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_hot_runner_objtypes.ControllerType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=6028"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6032",
    browseName="ns=plastics_hot_runner;SetValueManualOutput",
    description="Manually given output in percent if SetValueType = MANUAL is selected",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6033", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6047", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_hot_runner_objtypes.ControllerType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=6032"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6026",
    browseName="ns=plastics_hot_runner;UpperOutput",
    description="Limitation of the maximum output in closed-loop control in %",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6027", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6048", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_hot_runner_objtypes.ControllerType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=6026"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6041",
    browseName="ns=plastics_hot_runner;UpperSetValueCascade",
    description="If the two controllers are cascaded, the master defines to which nominal temperature value the slave is to control to. With this parameter, the upper limit for the slave is defined.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6042", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6049", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_hot_runner_objtypes.ControllerType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=6041"])
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_hot_runner;i=6050",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=plastics_hot_runner;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[10],
    value=[
        o6.LocalizedText("OTHER"),
        o6.LocalizedText("GOOD"),
        o6.LocalizedText("SENSOR_FAULT"),
        o6.LocalizedText("TEMPERATURE_SENSOR_BROKEN"),
        o6.LocalizedText("TEMPERATURE_SENSOR_REVERSED"),
        o6.LocalizedText("POWER_UNIT_FAILED"),
        o6.LocalizedText("HEATING_OUTPUT_TO_LOW"),
        o6.LocalizedText("ERROR"),
        o6.LocalizedText("WARNING"),
        o6.LocalizedText("LEAKAGE_DETECTED"),
    ],
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6023",
    browseName="ns=plastics_hot_runner;SetValueType",
    description="Set value for the controller type used by the zone",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6024", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6062", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_hot_runner_objtypes.ControllerType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=6023"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_hot_runner;i=6093",
    browseName="ns=plastics_hot_runner;TimeMethodPIDParametersDataType",
    dataType=o6.String,
    value="//xs:element[@name='TimeMethodPIDParametersDataType']",
)
o6.reference(o6.ns["ns=plastics_hot_runner;i=5038"], "i=39", o6.ns["ns=plastics_hot_runner;i=6093"])
oPC40082_2_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_hot_runner;i=6019",
    browseName="ns=plastics_hot_runner;OPC40082_2",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/HotRunner/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6020", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PlasticsRubber/HotRunner/Types.xsd"
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6093"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/PlasticsRubber/HotRunner/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/HotRunner/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="ControllerTypeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="CLOSED_LOOP_CONTROL_0"/>\n   <xs:enumeration value="MANUAL_1"/>\n   <xs:enumeration value="SYNCHRONOUS_ZONE_2"/>\n   <xs:enumeration value="CASCADE_3"/>\n   <xs:enumeration value="COOL_ZONE_4"/>\n   <xs:enumeration value="MEASURING_ZONE_5"/>\n   <xs:enumeration value="NOT_USED_6"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ControllerTypeEnumeration" name="ControllerTypeEnumeration"/>\n <xs:complexType name="ListOfControllerTypeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ControllerTypeEnumeration" name="ControllerTypeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfControllerTypeEnumeration" name="ListOfControllerTypeEnumeration" nillable="true"/>\n <xs:simpleType name="ZoneStatusEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OTHER_0"/>\n   <xs:enumeration value="GOOD_1"/>\n   <xs:enumeration value="SENSOR_FAULT_2"/>\n   <xs:enumeration value="TEMPERATURE_SENSOR_BROKEN_3"/>\n   <xs:enumeration value="TEMPERATURE_SENSOR_REVERSED_4"/>\n   <xs:enumeration value="POWER_UNIT_FAILED_5"/>\n   <xs:enumeration value="HEATING_OUTPUT_TO_LOW_6"/>\n   <xs:enumeration value="ERROR_7"/>\n   <xs:enumeration value="WARNING_8"/>\n   <xs:enumeration value="LEAKAGE_DETECTED_9"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ZoneStatusEnumeration" name="ZoneStatusEnumeration"/>\n <xs:complexType name="ListOfZoneStatusEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ZoneStatusEnumeration" name="ZoneStatusEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfZoneStatusEnumeration" name="ListOfZoneStatusEnumeration" nillable="true"/>\n <xs:complexType name="TimeMethodPIDParametersDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Xp"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Tn"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Tv"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Ts"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:TimeMethodPIDParametersDataType" name="TimeMethodPIDParametersDataType"/>\n <xs:complexType name="ListOfTimeMethodPIDParametersDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:TimeMethodPIDParametersDataType" name="TimeMethodPIDParametersDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfTimeMethodPIDParametersDataType" name="ListOfTimeMethodPIDParametersDataType" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6094",
    browseName="ns=plastics_hot_runner;UpperOutput",
    description="Limitation of the maximum output in closed-loop control in %",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6063", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6095", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6081",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6082", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6106", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6057",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6058", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6125", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6104",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6105", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6126", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6123",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6124", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6127", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6087",
    browseName="ns=plastics_hot_runner;LowerOutput",
    description="Limitation of the minimum output in closed-loop control in %",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6088", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6142", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6091",
    browseName="ns=plastics_hot_runner;SetValueManualOutput",
    description="Manually given output in percent if SetValueType = MANUAL is selected",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6092", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6143", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6053",
    browseName="ns=plastics_hot_runner;ThermocoupleType",
    description="Type of connected external temperature sensor",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6054", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6151", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_hot_runner_objtypes.ZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=6053"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6175",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6176", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6177", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6189",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6190", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6191", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6100",
    browseName="ns=plastics_hot_runner;SetValueManualOutputLimit",
    description="This pre-defined maximum output (in percent) is valid until the SetValueTemperature is reached.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6101", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6207", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6102",
    browseName="ns=plastics_hot_runner;SetValueTemperature",
    description="If ManualOutputLimitActive is set, SetValueManualOutputLimit is active until this nominal temperature value is reached.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6103", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6208", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6171",
    browseName="ns=plastics_hot_runner;SetValueManualOutputLimit",
    description="This pre-defined maximum output (in percent) is valid until the SetValueTemperature is reached.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6172", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6209", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6173",
    browseName="ns=plastics_hot_runner;SetValueTemperature",
    description="If ManualOutputLimitActive is set, SetValueManualOutputLimit is active until this nominal temperature value is reached.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6174", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6210", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6133",
    browseName="ns=plastics_hot_runner;SetValueTemperatureChange",
    description="Specification of the set value change",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6134", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6211", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_hot_runner_objtypes.TemperatureRiseMonitoringType(
    nodeId="ns=plastics_hot_runner;i=5004",
    browseName="ns=plastics_hot_runner;TemperatureRiseMonitoring",
    description="Additional monitoring for the process temperature",
    modellingRule="Optional",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6064",
                browseName="ns=plastics_hot_runner;ErrorDetected",
                description="Result of the TemperatureRiseMonitoring",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6065",
                browseName="ns=plastics_hot_runner;SetValueActive",
                description="On / Off for the TemperatureRiseMonitoring",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6135",
                browseName="ns=plastics_hot_runner;SupervisionTime",
                description="Specification of the time within the temperature must have changed",
                dataType=ns0.datatypes.Duration,
                value=0.0,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6133"]),
    ],
)
o6.reference(plastics_hot_runner_objtypes.ZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=5004"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6203",
    browseName="ns=plastics_hot_runner;SetValueTemperatureChange",
    description="Specification of the set value change",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6204", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6212", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_hot_runner_objtypes.TemperatureRiseMonitoringType(
    nodeId="ns=plastics_hot_runner;i=5013",
    browseName="ns=plastics_hot_runner;TemperatureRiseMonitoring",
    description="Additional monitoring for the process temperature",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6148",
                browseName="ns=plastics_hot_runner;ErrorDetected",
                description="Result of the TemperatureRiseMonitoring",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6149",
                browseName="ns=plastics_hot_runner;SetValueActive",
                description="On / Off for the TemperatureRiseMonitoring",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6205",
                browseName="ns=plastics_hot_runner;SupervisionTime",
                description="Specification of the time within the temperature must have changed",
                dataType=ns0.datatypes.Duration,
                value=0.0,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6203"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6083",
    browseName="ns=plastics_hot_runner;ActualOutput",
    description="Indicates the currently active output in percent",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6084", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6232", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6085",
    browseName="ns=plastics_hot_runner;AverageControllerOutput",
    description="Indicates the average output which can be used when a sensor is broken",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6086", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6233", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_hot_runner_objtypes.HeatUpType(
    nodeId="ns=plastics_hot_runner;i=5003",
    browseName="ns=plastics_hot_runner;HeatUp",
    description="Setting for heat up procedure",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6098",
                browseName="ns=plastics_hot_runner;EvenHeatUpEnabled",
                description="Enables even heat-up process until nominal SetValue of Temperature of ZoneType is reached",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6099",
                browseName="ns=plastics_hot_runner;ManualOutputLimitActive",
                description="Activates heat-up process with pre-defined SetValueManualOutputLimit until SetValueTemperature is reached",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6145",
                browseName="ns=plastics_hot_runner;RelayHeatingGroup",
                description="Number of the heating group for relay heating",
                dataType=o6.Byte,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6234",
                browseName="ns=plastics_hot_runner;RelayHeatingTime",
                description="Time for relay heating of the zone. When RelayHeatingTime of all zones of a heating group have expired, the next group starts heating.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6100"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6102"]),
    ],
)
o6.reference(plastics_hot_runner_objtypes.ZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=5003"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6206",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6235", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6236", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6077",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6078", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6250", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6253",
    browseName="ns=plastics_hot_runner;SecondSetValue",
    description="Second set value for fast switch-over",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6254", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6256", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_hot_runner_objtypes.HRDTemperatureType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=6253"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6268",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6269", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6270", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6282",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6283", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6284", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6296",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6297", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6298", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6096",
    browseName="ns=plastics_hot_runner;UpperSetValueCascade",
    description="If the two controllers are cascaded, the master defines to which nominal temperature value the slave is to control to. With this parameter, the upper limit for the slave is defined.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6097", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6305", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6306",
    browseName="ns=plastics_hot_runner;SetValueType",
    description="Set value for the controller type used by the zone",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6307", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6308", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6165",
    browseName="ns=plastics_hot_runner;UpperOutput",
    description="Limitation of the maximum output in closed-loop control in %",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6166", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6309", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6158",
    browseName="ns=plastics_hot_runner;LowerOutput",
    description="Limitation of the minimum output in closed-loop control in %",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6159", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6310", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6162",
    browseName="ns=plastics_hot_runner;SetValueManualOutput",
    description="Manually given output in percent if SetValueType = MANUAL is selected",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6163", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6311", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6154",
    browseName="ns=plastics_hot_runner;ActualOutput",
    description="Indicates the currently active output in percent",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6155", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6312", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6156",
    browseName="ns=plastics_hot_runner;AverageControllerOutput",
    description="Indicates the average output which can be used when a sensor is broken",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6157", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6313", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6167",
    browseName="ns=plastics_hot_runner;UpperSetValueCascade",
    description="If the two controllers are cascaded, the master defines to which nominal temperature value the slave is to control to. With this parameter, the upper limit for the slave is defined.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6168", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6315", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6316",
    browseName="ns=plastics_hot_runner;SetValueType",
    description="Set value for the controller type used by the zone",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6317", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6318", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6119",
    browseName="ns=plastics_hot_runner;UpperOutput",
    description="Limitation of the maximum output in closed-loop control in %",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6120", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6319", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6112",
    browseName="ns=plastics_hot_runner;LowerOutput",
    description="Limitation of the minimum output in closed-loop control in %",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6113", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6320", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6116",
    browseName="ns=plastics_hot_runner;SetValueManualOutput",
    description="Manually given output in percent if SetValueType = MANUAL is selected",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6117", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6321", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6108",
    browseName="ns=plastics_hot_runner;ActualOutput",
    description="Indicates the currently active output in percent",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6109", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6322", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6110",
    browseName="ns=plastics_hot_runner;AverageControllerOutput",
    description="Indicates the average output which can be used when a sensor is broken",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6111", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6323", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6121",
    browseName="ns=plastics_hot_runner;UpperSetValueCascade",
    description="If the two controllers are cascaded, the master defines to which nominal temperature value the slave is to control to. With this parameter, the upper limit for the slave is defined.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6122", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6325", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6326",
    browseName="ns=plastics_hot_runner;SetValueType",
    description="Set value for the controller type used by the zone",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6327", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6328", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6079",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6080", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6330", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6248",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6249", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6331", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6070",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6071", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6363", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6343",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6344", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6364", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6350",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6351", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6365", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6352",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6353", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6366", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6354",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6355", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6367", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6072",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6073", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6368", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6345",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6346", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6369", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6074",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6075", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6370", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6347",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6348", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6371", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6333",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6334", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6372", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6335",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6336", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6373", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6337",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6338", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6374", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6357",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6358", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6375", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6359",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6360", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6376", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6361",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6362", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6377", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6380",
    browseName="ns=plastics_hot_runner;CommunicationProtocolType",
    description="Used communication protocol between the sensor and the control system of the HRD",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6381", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6383", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_hot_runner_objtypes.ZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=6380"])
plastics_hot_runner_objtypes.HeatUpType(
    nodeId="ns=plastics_hot_runner;i=5011",
    browseName="ns=plastics_hot_runner;HeatUp",
    description="Setting for heat up procedure",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6169",
                browseName="ns=plastics_hot_runner;EvenHeatUpEnabled",
                description="Enables even heat-up process until nominal SetValue of Temperature of ZoneType is reached",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6170",
                browseName="ns=plastics_hot_runner;ManualOutputLimitActive",
                description="Activates heat-up process with pre-defined SetValueManualOutputLimit until SetValueTemperature is reached",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6384",
                browseName="ns=plastics_hot_runner;RelayHeatingGroup",
                description="Number of the heating group for relay heating",
                dataType=o6.Byte,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6385",
                browseName="ns=plastics_hot_runner;RelayHeatingTime",
                description="Time for relay heating of the zone. When RelayHeatingTime of all zones of a heating group have expired, the next group starts heating.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6171"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6173"]),
    ],
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6382",
    browseName="ns=plastics_hot_runner;CommunicationProtocolType",
    description="Used communication protocol between the sensor and the control system of the HRD",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6386", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6387", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6150",
    browseName="ns=plastics_hot_runner;ThermocoupleType",
    description="Type of connected external temperature sensor",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6391", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6392", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6217",
    browseName="ns=plastics_hot_runner;ActiveSetValues",
    description="Central selection of the used set temperature for the temperature zones",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6393", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6394", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_hot_runner_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=6217"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6252",
    browseName="ns=plastics_hot_runner;ActiveSetValues",
    description="Central selection of the used set temperature for the temperature zones",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6395", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6396", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6184",
    browseName="ns=plastics_hot_runner;SecondSetValue",
    description="Second set value for fast switch-over",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6185", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6397", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6179",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6180", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6407", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6181",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6182", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6408", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6183",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6186", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6409", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6263",
    browseName="ns=plastics_hot_runner;SecondSetValue",
    description="Second set value for fast switch-over",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6264", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6410", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6187",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6188", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6411", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6192",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6193", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6412", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6194",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6195", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6413", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6196",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6197", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6414", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6198",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6199", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6415", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6201",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6202", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6416", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6258",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6259", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6417", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6260",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6261", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6418", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6262",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6265", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6419", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6266",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6267", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6420", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6271",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6272", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6421", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6273",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6274", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6422", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6291",
    browseName="ns=plastics_hot_runner;SecondSetValue",
    description="Second set value for fast switch-over",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6292", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6423", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6275",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6276", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6424", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6277",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6278", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6425", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6280",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6281", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6426", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6286",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6287", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6427", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6288",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6289", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6428", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6290",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6293", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6429", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6294",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6295", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6430", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6299",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6300", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6431", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6301",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6302", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6432", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6401",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6402", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6433", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6403",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6404", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6434", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6405",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6406", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6435", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6132",
    browseName="ns=plastics_hot_runner;BoostSetValue",
    description="Set value for boost mode",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6200", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6436", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_hot_runner_objtypes.HRDTemperatureType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=6132"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6255",
    browseName="ns=plastics_hot_runner;StandbySetValue",
    description="Set value for standby mode",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6279", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6437", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_hot_runner_objtypes.HRDTemperatureType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=6255"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6440",
    browseName="ns=plastics_hot_runner;SetValueManualOutputLimit",
    description="This pre-defined maximum output (in percent) is valid until the SetValueTemperature is reached.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6441", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6442", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6443",
    browseName="ns=plastics_hot_runner;SetValueTemperature",
    description="If ManualOutputLimitActive is set, SetValueManualOutputLimit is active until this nominal temperature value is reached.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6444", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6445", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6446",
    browseName="ns=plastics_hot_runner;SetValueTemperatureChange",
    description="Specification of the set value change",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6447", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6448", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_hot_runner_objtypes.TemperatureRiseMonitoringType(
    nodeId="ns=plastics_hot_runner;i=5032",
    browseName="ns=plastics_hot_runner;TemperatureRiseMonitoring",
    description="Additional monitoring for the process temperature",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6389",
                browseName="ns=plastics_hot_runner;ErrorDetected",
                description="Result of the TemperatureRiseMonitoring",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6390",
                browseName="ns=plastics_hot_runner;SetValueActive",
                description="On / Off for the TemperatureRiseMonitoring",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6449",
                browseName="ns=plastics_hot_runner;SupervisionTime",
                description="Specification of the time within the temperature must have changed",
                dataType=ns0.datatypes.Duration,
                value=0.0,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6446"]),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6450",
    browseName="ns=plastics_hot_runner;BoostSetValue",
    description="Set value for boost mode",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6451", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6462", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6452",
    browseName="ns=plastics_hot_runner;StandbySetValue",
    description="Set value for standby mode",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6453", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6463", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6454",
    browseName="ns=plastics_hot_runner;BoostSetValue",
    description="Set value for boost mode",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6455", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6464", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6456",
    browseName="ns=plastics_hot_runner;StandbySetValue",
    description="Set value for standby mode",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6457", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6465", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6458",
    browseName="ns=plastics_hot_runner;BoostSetValue",
    description="Set value for boost mode",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6459", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6466", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6460",
    browseName="ns=plastics_hot_runner;StandbySetValue",
    description="Set value for standby mode",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6461", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6467", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_hot_runner_objtypes.HeatUpType(
    nodeId="ns=plastics_hot_runner;i=5031",
    browseName="ns=plastics_hot_runner;HeatUp",
    description="Setting for heat up procedure",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6438",
                browseName="ns=plastics_hot_runner;EvenHeatUpEnabled",
                description="Enables even heat-up process until nominal SetValue of Temperature of ZoneType is reached",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6439",
                browseName="ns=plastics_hot_runner;ManualOutputLimitActive",
                description="Activates heat-up process with pre-defined SetValueManualOutputLimit until SetValueTemperature is reached",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6468",
                browseName="ns=plastics_hot_runner;RelayHeatingGroup",
                description="Number of the heating group for relay heating",
                dataType=o6.Byte,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6469",
                browseName="ns=plastics_hot_runner;RelayHeatingTime",
                description="Time for relay heating of the zone. When RelayHeatingTime of all zones of a heating group have expired, the next group starts heating.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6440"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6443"]),
    ],
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6471",
    browseName="ns=plastics_hot_runner;CommunicationProtocolType",
    description="Used communication protocol between the sensor and the control system of the HRD",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6472", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6473", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6474",
    browseName="ns=plastics_hot_runner;ThermocoupleType",
    description="Type of connected external temperature sensor",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6475", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6476", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPlasticsRubberSlashHotRunnerSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=plastics_hot_runner;i=5033",
    browseName="ns=plastics_hot_runner;http://opcfoundation.org/UA/PlasticsRubber/HotRunner/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6477", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6478", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2021-05-10T12:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6479", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PlasticsRubber/HotRunner/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6480", browseName="NamespaceVersion", dataType=o6.String, value="1.00")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6481",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6482", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6483", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
plastics_rubber.objtypes.IdentificationType(
    nodeId="ns=plastics_hot_runner;i=5015",
    browseName="ns=plastics_hot_runner;Identification",
    description="Identification of the device",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6218",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose a certain device is used",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6219",
                browseName="ns=di;Manufacturer",
                description="Provides the name of the manufacturer of the machine",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6220", browseName="ns=di;Model", description="Represents the name of the machine type", dataType=o6.LocalizedText
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6221",
                browseName="ns=di;SerialNumber",
                description="Represents the serial number of the machine (unique ID given by the manufacturer)",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6241", browseName="ns=di;AssetId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6242", browseName="ns=di;ComponentName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6243", browseName="ns=di;DeviceManual", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6486", browseName="ns=di;DeviceRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6487", browseName="ns=di;HardwareRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6488", browseName="ns=di;ManufacturerUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6489", browseName="ns=di;ProductCode", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6490", browseName="ns=di;ProductInstanceUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6491", browseName="ns=di;RevisionCounter", dataType=o6.Int32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6492", browseName="ns=di;SoftwareRevision", dataType=o6.String)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6493",
                browseName="ns=plastics_rubber;YearOfConstruction",
                description="Represents the year of construction of the machine",
                dataType=o6.UInt16,
            )
        ),
    ],
)
o6.reference(plastics_hot_runner_objtypes.HRD_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=5015"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6494",
    browseName="ns=plastics_hot_runner;ReactionOnDisconnect",
    description="Selection of the set temperature for the temperature zones in case of a disconnection from the OPC UA client",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6495", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6496", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
o6.reference(plastics_hot_runner_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=6494"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6497",
    browseName="ns=plastics_hot_runner;ReactionOnDisconnect",
    description="Selection of the set temperature for the temperature zones in case of a disconnection from the OPC UA client",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6498", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6499", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6513",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6514", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6515", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6152",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6153", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6526", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6304",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6314", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6527", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6324",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6510", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6528", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6511",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6512", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6529", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6516",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6517", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6530", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6518",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6519", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6531", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6520",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6521", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6532", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6522",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6523", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6533", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6524",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6525", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6534", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6535",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6536", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6542", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6543",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6544", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6545", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6547",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6548", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6549", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6550",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6551", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6552", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6553",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6554", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6555", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6556",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6557", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6558", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6559",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6560", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6561", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6562",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6563", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6564", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6565",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6566", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6567", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6568",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6569", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6570", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6571",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6572", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6573", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6574",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6575", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6576", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6537",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6538", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6577", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6578",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6579", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6580", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6582",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6583", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6584", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6585",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6586", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6587", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6588",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6589", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6590", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6591",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6592", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6593", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6594",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6595", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6596", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6597",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6598", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6599", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6600",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6601", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6602", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6603",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6604", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6605", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6606",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6607", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6608", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6609",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6610", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6611", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6539",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6540", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6612", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6613",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6614", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6615", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6617",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6618", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6619", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6620",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6621", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6622", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6623",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6624", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6625", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6626",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6627", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6628", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6629",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6630", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6631", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6632",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6633", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6634", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6635",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6636", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6637", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6638",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6639", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6640", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6641",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6642", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6643", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6644",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6645", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6646", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6506",
    browseName="ns=plastics_hot_runner;EvenHeatUpMaxTemperatureDifference",
    description="Definition of the maximum temperature difference of all zones during even heat-up",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6507", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6647", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_hot_runner_objtypes.OperationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=6506"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6508",
    browseName="ns=plastics_hot_runner;EvenHeatUpMaxTemperatureDifference",
    description="Definition of the maximum temperature difference of all zones during even heat-up",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6509", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6648", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6653",
    browseName="ns=plastics_hot_runner;ActiveSetValue",
    description="Current active set temperature for the temperature zone",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6654", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6655", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
o6.reference(plastics_hot_runner_objtypes.HRDTemperatureType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=6653"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6656",
    browseName="ns=plastics_hot_runner;ActiveSetValue",
    description="Current active set temperature for the temperature zone",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6657", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6658", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6659",
    browseName="ns=plastics_hot_runner;ActiveSetValue",
    description="Current active set temperature for the temperature zone",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6660", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6661", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6662",
    browseName="ns=plastics_hot_runner;ActiveSetValue",
    description="Current active set temperature for the temperature zone",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6663", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6664", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6665",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6666", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6667", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6668",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6669", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6670", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6680",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6681", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6682", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6672",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6673", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6693", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6674",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6675", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6694", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6676",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6677", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6695", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6678",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6679", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6696", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6683",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6684", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6697", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6685",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6686", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6698", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6687",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6688", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6699", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6689",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6690", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6700", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6691",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6692", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6701", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6485",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6702", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6703", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6704",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6705", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6706", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6707",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6708", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6709", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6710",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6711", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6712", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6713",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6714", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6715", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6716",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6717", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6718", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6719",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6720", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6721", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_hot_runner;i=6722",
    browseName="ns=plastics_rubber;Status",
    description="Information if the ActualValue is within the tolerances or has passed a tolerance or min/max value",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6723", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6724", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6725",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6726", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_hot_runner;i=5045",
    browseName="ns=plastics_hot_runner;LoadPower",
    description="Information about the load power in Watt",
    references=[o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6725"])],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6727",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6728", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_hot_runner;i=5046",
    browseName="ns=plastics_hot_runner;LoadPower",
    description="Information about the load power in Watt",
    references=[o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6727"])],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_hot_runner;i=6729",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6730", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_hot_runner;i=5047",
    browseName="ns=plastics_hot_runner;LoadPower",
    description="Information about the load power in Watt",
    references=[o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6729"])],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_hot_runner;i=5005",
    browseName="ns=plastics_hot_runner;Heating",
    description="Information about the maintenance status of the heating",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6066",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6076",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6077"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6079"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6248"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_hot_runner;i=7001", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0")
        ),
    ],
)
o6.reference(plastics_hot_runner_objtypes.MaintenanceInformationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=5005"])
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_hot_runner;i=5006",
    browseName="ns=plastics_hot_runner;SafetyTest",
    description="Information about the maintenance status of the safety test",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6067",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6332",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6333"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6335"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6337"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_hot_runner;i=7002", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0")
        ),
    ],
)
o6.reference(plastics_hot_runner_objtypes.MaintenanceInformationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=5006"])
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_hot_runner;i=5007",
    browseName="ns=plastics_hot_runner;CoolingFan",
    description="Information about the maintenance status of the cooling fan",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6068",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6069",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6070"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6072"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6074"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_hot_runner;i=7003", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0")
        ),
    ],
)
o6.reference(plastics_hot_runner_objtypes.MaintenanceInformationType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=5007"])
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_hot_runner;i=5021",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6128",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6129",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6130",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_hot_runner;i=7004",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_hot_runner;i=7005", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_hot_runner;i=6223",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_hot_runner;i=7008",
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
    nodeId="ns=plastics_hot_runner;i=7008",
    browseName="ns=plastics_rubber;SetMachineTime",
    description="Method for setting the server time together with TimeZoneOffset",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_hot_runner;i=6223"]),
)

plastics_rubber.objtypes.DiagnosticsType(
    nodeId="ns=plastics_hot_runner;i=5022",
    browseName="ns=plastics_hot_runner;Diagnostics",
    description="Diagnosis functions to check, for example, the wiring to the heating system or the sensor and heater allocation",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6237", browseName="ns=plastics_rubber;Status", dataType=plastics_rubber.datatypes.DiagnosticsStatusEnumeration
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_hot_runner;i=7009", browseName="ns=plastics_rubber;RunDiagnostics")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_hot_runner;i=7010", browseName="ns=plastics_rubber;StopDiagnostics")),
    ],
)
o6.reference(plastics_hot_runner_objtypes.HRD_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=5022"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_hot_runner;i=6244",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_hot_runner;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="VisualisationUnit", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_hot_runner;i=6245",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_hot_runner;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Page", dataType=ns0.datatypes.Image, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_hot_runner;i=7011",
    browseName="ns=plastics_rubber;GetCurrentPage",
    description="Method for retrieving a screenshot of the control system with the currently shown contents",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_hot_runner;i=6244"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_hot_runner;i=6245"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_hot_runner;i=6246",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_hot_runner;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_hot_runner;i=6247",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_hot_runner;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Page", dataType=ns0.datatypes.Image, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_hot_runner;i=7012",
    browseName="ns=plastics_rubber;GetPage",
    description="Method for retrieving the image of a page of the control system",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_hot_runner;i=6246"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_hot_runner;i=6247"]),
)

plastics_rubber.objtypes.MachineConfigurationType(
    nodeId="ns=plastics_hot_runner;i=5016",
    browseName="ns=plastics_hot_runner;MachineConfiguration",
    description="Current configuration of the hot runner device",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6222",
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
                nodeId="ns=plastics_hot_runner;i=6224",
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
                nodeId="ns=plastics_hot_runner;i=6225",
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
                nodeId="ns=plastics_hot_runner;i=6329",
                browseName="ns=plastics_rubber;PageDirectory",
                description="List of the pages that are implemented in the machine control system and are shown on the screen of the machine",
                dataType=plastics_rubber.datatypes.PageEntryDataType,
                valueRank=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=7008"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=7011"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=7012"]),
    ],
)
o6.reference(plastics_hot_runner_objtypes.HRD_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=5016"])
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_hot_runner;i=5024",
    browseName="ns=plastics_hot_runner;CoolingFan",
    description="Information about the maintenance status of the cooling fan",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6339",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6342",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6343"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6345"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6347"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_hot_runner;i=7013", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0")
        ),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_hot_runner;i=5025",
    browseName="ns=plastics_hot_runner;Heating",
    description="Information about the maintenance status of the heating",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6340",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6349",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6350"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6352"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6354"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_hot_runner;i=7014", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0")
        ),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_hot_runner;i=5026",
    browseName="ns=plastics_hot_runner;SafetyTest",
    description="Information about the maintenance status of the safety test",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6341",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6356",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6357"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6359"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6361"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_hot_runner;i=7015", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0")
        ),
    ],
)
plastics_hot_runner_objtypes.MaintenanceInformationType(
    nodeId="ns=plastics_hot_runner;i=5023",
    browseName="ns=plastics_hot_runner;MaintenanceInformation",
    description="Information about the maintenance status of various parts of a hot runner device",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=5024"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=5025"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=5026"]),
    ],
)
o6.reference(plastics_hot_runner_objtypes.HRD_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=5023"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_hot_runner;i=6379",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_hot_runner;i=7020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_hot_runner;i=7020",
    browseName="ns=plastics_hot_runner;ResetErrorById",
    description="Method to reset one error of the device",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_hot_runner;i=6379"]),
)

plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_hot_runner;i=5014",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6398",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6399",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6400",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_hot_runner;i=7021",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_hot_runner;i=7022", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_hot_runner;i=5027",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6131",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6146",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6147",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_hot_runner;i=7018",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_hot_runner;i=7023", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
plastics_hot_runner_objtypes.HRDTemperatureType(
    nodeId="ns=plastics_hot_runner;i=5001",
    browseName="ns=plastics_hot_runner;Temperature",
    description="Setting and monitoring of the temperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6178",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6470",
                browseName="ns=plastics_hot_runner;BoostTime",
                description="Duration of the boost mode after which the set value which was active before boost is becoming active again",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6501",
                browseName="ns=plastics_hot_runner;TimeMethodPIDParameters",
                description="Setting of PID parameters with time method",
                dataType=plastics_hot_runner_datypes.TimeMethodPIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=5014"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6057"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6175"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6179"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6181"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6183"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6184"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6187"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6189"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6192"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6194"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6196"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6198"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6201"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6450"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6452"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6656"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6704"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_hot_runner;i=7024",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_hot_runner_objtypes.ZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=5001"])
plastics_hot_runner_objtypes.HRDTemperatureType(
    nodeId="ns=plastics_hot_runner;i=5008",
    browseName="ns=plastics_hot_runner;Temperature",
    description="Setting and monitoring of the temperature",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6257",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6502",
                browseName="ns=plastics_hot_runner;BoostTime",
                description="Duration of the boost mode after which the set value which was active before boost is becoming active again",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6503",
                browseName="ns=plastics_hot_runner;TimeMethodPIDParameters",
                description="Setting of PID parameters with time method",
                dataType=plastics_hot_runner_datypes.TimeMethodPIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=5021"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6104"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6206"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6258"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6260"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6262"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6263"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6266"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6268"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6271"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6273"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6275"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6277"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6280"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6454"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6456"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6659"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6707"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_hot_runner;i=7025",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_hot_runner_objtypes.HRDTemperatureType(
    nodeId="ns=plastics_hot_runner;i=5012",
    browseName="ns=plastics_hot_runner;Temperature",
    description="Setting and monitoring of the temperature",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6285",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6504",
                browseName="ns=plastics_hot_runner;BoostTime",
                description="Duration of the boost mode after which the set value which was active before boost is becoming active again",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6505",
                browseName="ns=plastics_hot_runner;TimeMethodPIDParameters",
                description="Setting of PID parameters with time method",
                dataType=plastics_hot_runner_datypes.TimeMethodPIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=5027"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6123"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6282"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6286"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6288"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6290"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6291"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6294"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6296"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6299"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6301"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6401"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6403"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6405"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6458"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6460"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6662"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6710"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_hot_runner;i=7026",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_hot_runner;i=5040",
    browseName="ns=plastics_hot_runner;LoadCurrent",
    description="Information about the load current in Ampere",
    modellingRule="Optional",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6107",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6038"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6081"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6152"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6304"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6324"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6511"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6513"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6516"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6518"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6520"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6522"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6524"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6713"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_hot_runner;i=7027",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_hot_runner_objtypes.ControllerType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=5040"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_hot_runner;i=5041",
    browseName="ns=plastics_hot_runner;LoadCurrent",
    description="Information about the load current in Ampere",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6546",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6535"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6543"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6547"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6550"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6553"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6556"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6559"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6562"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6565"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6568"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6571"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6574"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6716"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_hot_runner;i=7028",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_hot_runner_objtypes.ControllerType(
    nodeId="ns=plastics_hot_runner;i=5002",
    browseName="ns=plastics_hot_runner;Controller",
    description="Setting and monitoring of the controller",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6056",
                browseName="ns=plastics_hot_runner;AutomaticReferenceZoneSelection",
                description="If true, the HRD selects automatically the reference zone.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6059",
                browseName="ns=plastics_hot_runner;ActualType",
                description="Actual value for the controller type used by the zone",
                dataType=plastics_hot_runner_datypes.ControllerTypeEnumeration,
                value=plastics_hot_runner_datypes.ControllerTypeEnumeration.CLOSED_LOOP_CONTROL,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6060",
                browseName="ns=plastics_hot_runner;ActualValueActive",
                description="Indicates the current status of the controller",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6061",
                browseName="ns=plastics_hot_runner;SetValueActive",
                description="A control zone is switched on and off with this parameter.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6089",
                browseName="ns=plastics_hot_runner;OutputTime",
                description="Time basis for operating the actuator",
                dataType=ns0.datatypes.Duration,
                value=0.0,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6090",
                browseName="ns=plastics_hot_runner;ReferenceZone",
                description="If zones are to operate parallel to a control zone, the reference relation can be realised with this parameter.",
                dataType=o6.UInt32,
                value=0,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=5041"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=5045"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6083"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6085"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6087"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6091"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6094"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6096"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6306"]),
    ],
)
o6.reference(plastics_hot_runner_objtypes.ZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=5002"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_hot_runner;i=5042",
    browseName="ns=plastics_hot_runner;LoadCurrent",
    description="Information about the load current in Ampere",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6581",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6537"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6578"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6582"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6585"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6588"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6591"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6594"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6597"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6600"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6603"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6606"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6609"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6719"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_hot_runner;i=7029",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_hot_runner_objtypes.ControllerType(
    nodeId="ns=plastics_hot_runner;i=5010",
    browseName="ns=plastics_hot_runner;Controller",
    description="Setting and monitoring of the controller",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6137",
                browseName="ns=plastics_hot_runner;AutomaticReferenceZoneSelection",
                description="If true, the HRD selects automatically the reference zone.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6139",
                browseName="ns=plastics_hot_runner;ActualType",
                description="Actual value for the controller type used by the zone",
                dataType=plastics_hot_runner_datypes.ControllerTypeEnumeration,
                value=plastics_hot_runner_datypes.ControllerTypeEnumeration.CLOSED_LOOP_CONTROL,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6140",
                browseName="ns=plastics_hot_runner;ActualValueActive",
                description="Indicates the current status of the controller",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6141",
                browseName="ns=plastics_hot_runner;SetValueActive",
                description="A control zone is switched on and off with this parameter.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6160",
                browseName="ns=plastics_hot_runner;OutputTime",
                description="Time basis for operating the actuator",
                dataType=ns0.datatypes.Duration,
                value=0.0,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6161",
                browseName="ns=plastics_hot_runner;ReferenceZone",
                description="If zones are to operate parallel to a control zone, the reference relation can be realised with this parameter.",
                dataType=o6.UInt32,
                value=0,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=5042"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=5046"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6154"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6156"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6158"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6162"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6165"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6167"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6316"]),
    ],
)
plastics_hot_runner_objtypes.ZoneType(
    nodeId="ns=plastics_hot_runner;i=5009",
    browseName="ns=plastics_hot_runner;Zone_<Nr>",
    description="A HRD zone",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6055",
                browseName="ns=plastics_hot_runner;HighestActiveAlarmSeverity",
                description="Indicates the severity of the highest active alarm related to the current zone",
                dataType=o6.UInt16,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6144",
                browseName="ns=plastics_hot_runner;Name",
                description="A user given name of the zone",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=5008"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=5010"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=5011"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=5013"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6150"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6382"]),
    ],
)
o6.reference(plastics_hot_runner_objtypes.ZonesType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=5009"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_hot_runner;i=5043",
    browseName="ns=plastics_hot_runner;LoadCurrent",
    description="Information about the load current in Ampere",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6616",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6539"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6613"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6617"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6620"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6623"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6626"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6629"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6632"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6635"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6638"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6641"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6644"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6722"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_hot_runner;i=7030",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_hot_runner_objtypes.ControllerType(
    nodeId="ns=plastics_hot_runner;i=5020",
    browseName="ns=plastics_hot_runner;Controller",
    description="Setting and monitoring of the controller",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6114",
                browseName="ns=plastics_hot_runner;OutputTime",
                description="Time basis for operating the actuator",
                dataType=ns0.datatypes.Duration,
                value=0.0,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6115",
                browseName="ns=plastics_hot_runner;ReferenceZone",
                description="If zones are to operate parallel to a control zone, the reference relation can be realised with this parameter.",
                dataType=o6.UInt32,
                value=0,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6138",
                browseName="ns=plastics_hot_runner;AutomaticReferenceZoneSelection",
                description="If true, the HRD selects automatically the reference zone.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6229",
                browseName="ns=plastics_hot_runner;ActualType",
                description="Actual value for the controller type used by the zone",
                dataType=plastics_hot_runner_datypes.ControllerTypeEnumeration,
                value=plastics_hot_runner_datypes.ControllerTypeEnumeration.CLOSED_LOOP_CONTROL,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6230",
                browseName="ns=plastics_hot_runner;ActualValueActive",
                description="Indicates the current status of the controller",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6231",
                browseName="ns=plastics_hot_runner;SetValueActive",
                description="A control zone is switched on and off with this parameter.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=5043"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=5047"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6108"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6110"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6112"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6116"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6119"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6121"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6326"]),
    ],
)
plastics_hot_runner_objtypes.ZoneType(
    nodeId="ns=plastics_hot_runner;i=5019",
    browseName="ns=plastics_hot_runner;Zone_<Nr>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6388",
                browseName="ns=plastics_hot_runner;Name",
                description="A user given name of the zone",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6541",
                browseName="ns=plastics_hot_runner;HighestActiveAlarmSeverity",
                description="Indicates the severity of the highest active alarm related to the current zone",
                dataType=o6.UInt16,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=5012"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=5020"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=5031"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=5032"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6471"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6474"]),
    ],
)
plastics_hot_runner_objtypes.ZonesType(
    nodeId="ns=plastics_hot_runner;i=5018",
    browseName="ns=plastics_hot_runner;Zones",
    description="Container for the zones",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6228", browseName="NodeVersion", dataType=o6.String, value="\n      ")),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=5019"]),
    ],
)
o6.reference(plastics_hot_runner_objtypes.HRD_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=5018"])
o6.reference(o6.ns["ns=plastics_hot_runner;i=5018"], "i=41", "i=2133")


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_hot_runner;i=6652",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_hot_runner;i=7032",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReactionOnDisconnect", dataType=o6.UInt16, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_hot_runner;i=7032",
    browseName="ns=plastics_hot_runner;SetReactionOnDisconnect",
    description="Method to set ReactionOnDisconnect and SessionNameForReactionOnDisconnect",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_hot_runner;i=6652"]),
)

plastics_hot_runner_objtypes.OperationType(
    nodeId="ns=plastics_hot_runner;i=5017",
    browseName="ns=plastics_hot_runner;Operation",
    description="Contains components which are necessary to operate the HRD",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6226",
                browseName="ns=plastics_hot_runner;DeviceMappingNumber",
                description="Unique identifier/address/number for devices of the same DeviceType within a local network",
                dataType=o6.UInt32,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6251",
                browseName="ns=plastics_hot_runner;EnablePower",
                description="Global power control switch for all zone controllers",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6303",
                browseName="ns=plastics_hot_runner;HighestActiveAlarmSeverity",
                description="Indication of the severity of the highest active alarm",
                dataType=o6.UInt16,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6650",
                browseName="ns=plastics_hot_runner;SessionNameForReactionOnDisconnect",
                description="Contains the sessionName of the connection with the client relevant for ReactionOnDisconnect",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_hot_runner;i=6227",
                browseName="ns=plastics_hot_runner;ActiveErrors",
                description="List of the active errors of the device",
                dataType=plastics_rubber.datatypes.ClassifiedActiveErrorDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6252"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6497"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6508"]),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_hot_runner;i=7016", browseName="ns=plastics_hot_runner;ResetAllErrors", description="Method to reset all errors of the device")
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_hot_runner;i=7017",
                browseName="ns=plastics_hot_runner;IdentifyDevice",
                description="The peripheral device on which this method is called shows itself by e.g. activation of a LED.",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=7020"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=7032"]),
    ],
)
o6.reference(plastics_hot_runner_objtypes.HRD_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=5017"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_hot_runner;i=5044",
    browseName="ns=plastics_hot_runner;LoadPower",
    description="Information about the load power in Watt",
    modellingRule="Optional",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_hot_runner;i=6671",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6485"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6665"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6668"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6672"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6674"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6676"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6678"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6680"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6683"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6685"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6687"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6689"]),
        o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=6691"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_hot_runner;i=7033",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_hot_runner_objtypes.ControllerType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_hot_runner;i=5044"])


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_rubber, plastics_hot_runner_datypes, plastics_hot_runner_objtypes
