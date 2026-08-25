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

"""Generated OPC UA paefs namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.irdi as irdi
import o6.ns.machinery as machinery
import o6.ns.machinery_processvalues as machinery_processvalues
import o6.ns.ns0 as ns0
import o6.ns.padim as padim
from . import reftypes as paefs_reftypes
from . import datatypes as paefs_datypes
from . import objtypes as paefs_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6001",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6002", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6003", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5026",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6004", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6001"]),
    ],
)
o6.reference(paefs_objtypes.SensorMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5026"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=paefs;i=5033",
    browseName="ns=di;Identification",
    description="Data to identify the sensor (OPC 40001-1).",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6005",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6006",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(paefs_objtypes.SensorMonitoringType, ns0.reftypes.HasAddIn, o6.ns["ns=paefs;i=5033"])
o6.reference(o6.ns["ns=paefs;i=5105"], "i=17604", o6.ns["ns=paefs;i=5033"])
ns0.vartypes.PropertyType(
    nodeId="ns=paefs;i=6009",
    browseName="EnumStrings",
    parent="ns=paefs;i=3006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("DeviceActive"), o6.LocalizedText("DeviceInactive"), o6.LocalizedText("FillingActive"), o6.LocalizedText("DischargeActive")],
)
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=paefs;i=6010",
    browseName="ns=paefs;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PAEFS/",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6011", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PAEFS/"))],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/PAEFS/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/PAEFS/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:EnumeratedType LengthInBits="32" Name="AirConnectionOpenEnum">\n  <opc:Documentation>Describes whether the air connection is open, i.e., it is in a state in which air can be passed through</opc:Documentation>\n  <opc:EnumeratedValue Name="Open" Value="0"/>\n  <opc:EnumeratedValue Name="Closed" Value="1"/>\n  <opc:EnumeratedValue Name="Opening" Value="2"/>\n  <opc:EnumeratedValue Name="Closing" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="AnalogDigitalEnum">\n  <opc:Documentation>Specifies the type of a sensor</opc:Documentation>\n  <opc:EnumeratedValue Name="Analog" Value="0"/>\n  <opc:EnumeratedValue Name="Digital" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ControlModeEnum">\n  <opc:Documentation>Describes the possibility of controlling the system externally</opc:Documentation>\n  <opc:EnumeratedValue Name="Automatic" Value="0"/>\n  <opc:EnumeratedValue Name="Manual" Value="1"/>\n  <opc:EnumeratedValue Name="Other" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="FilterAidDeviceStatusEnum">\n  <opc:Documentation>Describes the action performed by the device for filter aid</opc:Documentation>\n  <opc:EnumeratedValue Name="DeviceActive" Value="0"/>\n  <opc:EnumeratedValue Name="DeviceInactive" Value="1"/>\n  <opc:EnumeratedValue Name="FillingActive" Value="2"/>\n  <opc:EnumeratedValue Name="DischargeActive" Value="3"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=paefs;i=6012",
    browseName="ns=paefs;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PAEFS/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6013", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PAEFS/Types.xsd"))
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/PAEFS/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/PAEFS/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="AirConnectionOpenEnum">\n  <xs:annotation>\n   <xs:documentation>Describes whether the air connection is open, i.e., it is in a state in which air can be passed through</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Open_0"/>\n   <xs:enumeration value="Closed_1"/>\n   <xs:enumeration value="Opening_2"/>\n   <xs:enumeration value="Closing_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:AirConnectionOpenEnum" name="AirConnectionOpenEnum"/>\n <xs:complexType name="ListOfAirConnectionOpenEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AirConnectionOpenEnum" name="AirConnectionOpenEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAirConnectionOpenEnum" name="ListOfAirConnectionOpenEnum" nillable="true"/>\n <xs:simpleType name="AnalogDigitalEnum">\n  <xs:annotation>\n   <xs:documentation>Specifies the type of a sensor</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Analog_0"/>\n   <xs:enumeration value="Digital_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:AnalogDigitalEnum" name="AnalogDigitalEnum"/>\n <xs:complexType name="ListOfAnalogDigitalEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AnalogDigitalEnum" name="AnalogDigitalEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAnalogDigitalEnum" name="ListOfAnalogDigitalEnum" nillable="true"/>\n <xs:simpleType name="ControlModeEnum">\n  <xs:annotation>\n   <xs:documentation>Describes the possibility of controlling the system externally</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Automatic_0"/>\n   <xs:enumeration value="Manual_1"/>\n   <xs:enumeration value="Other_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ControlModeEnum" name="ControlModeEnum"/>\n <xs:complexType name="ListOfControlModeEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ControlModeEnum" name="ControlModeEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfControlModeEnum" name="ListOfControlModeEnum" nillable="true"/>\n <xs:simpleType name="FilterAidDeviceStatusEnum">\n  <xs:annotation>\n   <xs:documentation>Describes the action performed by the device for filter aid</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="DeviceActive_0"/>\n   <xs:enumeration value="DeviceInactive_1"/>\n   <xs:enumeration value="FillingActive_2"/>\n   <xs:enumeration value="DischargeActive_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:FilterAidDeviceStatusEnum" name="FilterAidDeviceStatusEnum"/>\n <xs:complexType name="ListOfFilterAidDeviceStatusEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:FilterAidDeviceStatusEnum" name="FilterAidDeviceStatusEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfFilterAidDeviceStatusEnum" name="ListOfFilterAidDeviceStatusEnum" nillable="true"/>\n</xs:schema>\n',
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6008",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6014", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6015", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5034",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6017", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6008"]),
    ],
)
paefs_objtypes.SensorMonitoringType(
    nodeId="ns=paefs;i=5001",
    browseName="ns=paefs;FilterMediumState",
    description="The state of the filter medium; e.g., pressure difference or gas loading.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5034"])],
)
o6.reference(paefs_objtypes.SeparatorType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5001"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6018",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6019", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6022", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5050",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6023", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6018"]),
    ],
)
paefs_objtypes.SensorMonitoringType(
    nodeId="ns=paefs;i=5003",
    browseName="ns=paefs;Humidity",
    description="The current humidity in the separator.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5050"])],
)
o6.reference(paefs_objtypes.SeparatorType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5003"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6024",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6025", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6026", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5052",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6027", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6024"]),
    ],
)
paefs_objtypes.SensorMonitoringType(
    nodeId="ns=paefs;i=5009",
    browseName="ns=paefs;FillingLevel",
    description="The filling level describes the amount of filter aid in the pre-storage reservoir.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5052"])],
)
o6.reference(paefs_objtypes.FilterAidDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5009"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=paefs;i=6016",
    browseName="ns=paefs;LifetimeConsumption",
    description="Consumption over total machine lifetime. The AnalogUnitType variables InstrumentRange and EURange must not be used.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6030", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(paefs_objtypes.ConsumptionType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=6016"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6028",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6029", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6031", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5053",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6032", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6028"]),
    ],
)
paefs_objtypes.SensorMonitoringType(
    nodeId="ns=paefs;i=5011",
    browseName="ns=paefs;IonizerOutput",
    description="Describes the current flow or the voltage to the ionizer.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5053"])],
)
o6.reference(paefs_objtypes.IonizerType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5011"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6033",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6035", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6038", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5056",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6040", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6033"]),
    ],
)
paefs_objtypes.SensorMonitoringType(
    nodeId="ns=paefs;i=5012",
    browseName="ns=paefs;Airflow",
    description="Value of the air flow sensor",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5056"])],
)
o6.reference(paefs_objtypes.AirConnectionType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5012"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6041",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6042", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6043", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6045",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6051", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6052", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5058",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6053", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6045"]),
    ],
)
paefs_objtypes.SensorMonitoringType(
    nodeId="ns=paefs;i=5014",
    browseName="ns=paefs;Pressure",
    description="Value of the pressure sensor",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5058"])],
)
o6.reference(paefs_objtypes.AirConnectionType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5014"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6055",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6056", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6057", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5059",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6063", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6055"]),
    ],
)
paefs_objtypes.SensorMonitoringType(
    nodeId="ns=paefs;i=5015",
    browseName="ns=paefs;CurrentConsumption",
    description="The current consumption of the device.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5059"])],
)
o6.reference(paefs_objtypes.ConsumptionType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5015"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6064",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6065", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6066", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5060",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6067", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6064"]),
    ],
)
paefs_objtypes.SensorMonitoringType(
    nodeId="ns=paefs;i=5016",
    browseName="ns=paefs;PressureLoss",
    description="Specification of the current total pressure loss of the filter system between the device intake connection on the raw gas side and the device outlet on the clean gas side.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5060"])],
)
o6.reference(paefs_objtypes.FilterSystemType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5016"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6068",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6069", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6070", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5061",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6071", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6068"]),
    ],
)
paefs_objtypes.SensorMonitoringType(
    nodeId="ns=paefs;i=5025",
    browseName="ns=paefs;Temperature",
    description="The current temperature in the separator.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5061"])],
)
o6.reference(paefs_objtypes.SeparatorType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5025"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6072",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6073", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6074", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5062",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6075", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6072"]),
    ],
)
paefs_objtypes.SensorMonitoringType(
    nodeId="ns=paefs;i=5027",
    browseName="ns=paefs;CollectorOutput",
    description="Describes the current flow or the voltage to the collector.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5062"])],
)
o6.reference(paefs_objtypes.CollectorType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5027"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6076",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6077", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6078", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5063",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6079", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6076"]),
    ],
)
paefs_objtypes.SensorMonitoringType(
    nodeId="ns=paefs;i=5028",
    browseName="ns=paefs;PressureLoss",
    description="The specification of the total pressure loss of the filter unit between the device intake connection on the raw gas side and the device outlet on the clean gas side.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5063"])],
)
o6.reference(paefs_objtypes.FilterUnitType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5028"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6080",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6083", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6084", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=paefs;i=6088",
    browseName="ns=paefs;CurrentOutput",
    description="Current output of the high voltage unit.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6089", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6090", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
o6.reference(paefs_objtypes.HighVoltageUnitType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=6088"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6086",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6094", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6095", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5069",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6096", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6086"]),
    ],
)
paefs_objtypes.SensorMonitoringType(
    nodeId="ns=paefs;i=5038",
    browseName="ns=paefs;PressureLoss",
    description="The specification of the total pressure loss of the filter unit between the device intake connection on the raw gas side and the device outlet on the clean gas side.",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5069"])],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6097",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6099", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6100", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5070",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6101", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6097"]),
    ],
)
paefs_objtypes.SensorMonitoringType(
    nodeId="ns=paefs;i=5040",
    browseName="ns=paefs;IonizerOutput",
    description="Describes the current flow or the voltage to the ionizer.",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5070"])],
)
paefs_objtypes.IonizerType(
    nodeId="ns=paefs;i=5039",
    browseName="ns=paefs;<Ionizer>",
    description="The ionizers of the high voltage unit.",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5040"])],
)
o6.reference(paefs_objtypes.HighVoltageUnitType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5039"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6102",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6103", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6104", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5071",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6105", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6102"]),
    ],
)
paefs_objtypes.SensorMonitoringType(
    nodeId="ns=paefs;i=5042",
    browseName="ns=paefs;CollectorOutput",
    description="Describes the current flow or the voltage to the collector.",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5071"])],
)
paefs_objtypes.CollectorType(
    nodeId="ns=paefs;i=5041",
    browseName="ns=paefs;<Collector>",
    description="The collectors of the high voltage unit.",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5042"])],
)
o6.reference(paefs_objtypes.HighVoltageUnitType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5041"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=paefs;i=5045",
    browseName="ns=di;Identification",
    description="Data for component identification (OPC 40001-1).",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6034",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6107",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(paefs_objtypes.TemperatureRegulatorType, ns0.reftypes.HasAddIn, o6.ns["ns=paefs;i=5045"])
o6.reference(o6.ns["ns=paefs;i=5110"], "i=17604", o6.ns["ns=paefs;i=5045"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6106",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6108", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6109", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6112",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6113", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6114", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6116",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6117", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6118", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6120",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6121", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6122", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5075",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6123", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6120"]),
    ],
)
paefs_objtypes.SensorMonitoringType(
    nodeId="ns=paefs;i=5055",
    browseName="ns=paefs;FillingLevel",
    description="Filling level of the device.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5075"])],
)
o6.reference(paefs_objtypes.DischargeSystemType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5055"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6124",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6125", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6126", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5076",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6127", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6124"]),
    ],
)
paefs_objtypes.SensorMonitoringType(
    nodeId="ns=paefs;i=5064",
    browseName="ns=paefs;GasQuality",
    description="Value of the gas quality sensor",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5076"])],
)
o6.reference(paefs_objtypes.AirConnectionType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5064"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6128",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6129", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6130", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5096",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6131", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6128"]),
    ],
)
paefs_objtypes.SensorMonitoringType(
    nodeId="ns=paefs;i=5066",
    browseName="ns=paefs;Humidity",
    description="Value of the humidity sensor",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5096"])],
)
o6.reference(paefs_objtypes.AirConnectionType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5066"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPAEFSSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=paefs;i=5032",
    browseName="ns=paefs;http://opcfoundation.org/UA/PAEFS/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6132", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6133", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2025-02-01T00:00:00Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6134", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PAEFS/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6135", browseName="NamespaceVersion", dataType=o6.String, value="1.0.1")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6136", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6137", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6138", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=paefs;i=6111",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6150", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=paefs;i=5046",
    browseName="ns=machinery;MachineryItemState",
    description="StateMachine representing the operating state of the temperature regulator (OPC 40001-1).",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=6111"])],
)
o6.reference(paefs_objtypes.TemperatureRegulatorType, ns0.reftypes.HasAddIn, o6.ns["ns=paefs;i=5046"])
o6.reference(o6.ns["ns=paefs;i=5110"], "i=17604", o6.ns["ns=paefs;i=5046"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6148",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6149", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6151", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5097",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6152", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6148"]),
    ],
)
paefs_objtypes.SensorMonitoringType(
    nodeId="ns=paefs;i=5067",
    browseName="ns=paefs;Temperature",
    description="Value of the temperature sensor",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5097"])],
)
o6.reference(paefs_objtypes.AirConnectionType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5067"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6153",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6154", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6155", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6157",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6158", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6159", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6162",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6163", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6164", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5100",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6165", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6162"]),
    ],
)
paefs_objtypes.SensorSetpointReadType(
    nodeId="ns=paefs;i=5093",
    browseName="ns=paefs;Airflow",
    description="Setpoint for the airflow that flows through the filter unit.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5100"])],
)
o6.reference(paefs_objtypes.FilterUnitType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5093"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6166",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6167", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6168", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5101",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6169", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6166"]),
    ],
)
paefs_objtypes.SensorSetpointReadType(
    nodeId="ns=paefs;i=5094",
    browseName="ns=paefs;Pressure",
    description="Setpoint for the negative pressure at the filter unit. Describes the setpoint value for the pressure difference of the raw gas side compared to the environment.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5101"])],
)
o6.reference(paefs_objtypes.FilterUnitType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5094"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6170",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6171", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6172", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5102",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6173", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6170"]),
    ],
)
paefs_objtypes.SensorSetpointReadType(
    nodeId="ns=paefs;i=5095",
    browseName="ns=paefs;RotationalSpeed",
    description='Setpoint for the rotational speed of a "virtual" fan. This value is a setpoint. In reality, the filter system can have several fans.',
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5102"])],
)
o6.reference(paefs_objtypes.FilterUnitType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5095"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=paefs;i=6174",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6175", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6183", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.vartypes.ProcessValueSetpointVariableType(
    nodeId="ns=paefs;i=6185",
    browseName="ns=machinery_processvalues;ProcessValueSetpoint",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6188", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6189", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5099",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6160", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6157"]),
        o6.hasComponent(o6.ns["ns=paefs;i=6185"]),
    ],
)
o6.reference(paefs_objtypes.SensorSetpointReadType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5099"])
machinery_processvalues.vartypes.ProcessValueSetpointVariableType(
    nodeId="ns=paefs;i=6190",
    browseName="ns=machinery_processvalues;ProcessValueSetpoint",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6191", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6192", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5057",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6044", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6041"]),
        o6.hasComponent(o6.ns["ns=paefs;i=6190"]),
    ],
)
o6.reference(paefs_objtypes.SensorSetpointWriteType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5057"])
machinery_processvalues.vartypes.ProcessValueSetpointVariableType(
    nodeId="ns=paefs;i=6193",
    browseName="ns=machinery_processvalues;ProcessValueSetpoint",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6196", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6197", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5068",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6085", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6080"]),
        o6.hasComponent(o6.ns["ns=paefs;i=6193"]),
    ],
)
paefs_objtypes.SensorSetpointWriteType(
    nodeId="ns=paefs;i=5013",
    browseName="ns=paefs;RotationalSpeed",
    description="Measured rotational speed of the fan.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5068"])],
)
o6.reference(paefs_objtypes.FanType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5013"])
paefs_objtypes.CleaningUnitValveType(
    nodeId="ns=paefs;i=5049",
    browseName="ns=paefs;<Valve>",
    description="The valves that are part of the cleaning unit.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6195",
                browseName="ns=paefs;Malfunction",
                description="Indicates that the cleaning unit valve is malfunctioning. True in case of error. Malfunctions can be, for example, that the valve does not open or close.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6198", browseName="ns=paefs;Open", description="Indicates that the valve is open.", dataType=o6.Boolean)),
    ],
)
o6.reference(paefs_objtypes.CleaningUnitType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5049"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=paefs;i=5051",
    browseName="ns=di;Identification",
    description="Data for machine identification (OPC 40001-1).",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6199",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6200",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(paefs_objtypes.CleaningUnitType, ns0.reftypes.HasAddIn, o6.ns["ns=paefs;i=5051"])
o6.reference(o6.ns["ns=paefs;i=5114"], "i=17604", o6.ns["ns=paefs;i=5051"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=paefs;i=5088",
    browseName="ns=di;Identification",
    description="Data for machine identification (OPC 40001-1).",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6194",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6201",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=paefs;i=5089",
    browseName="ns=di;Identification",
    description="Data for component identification (OPC 40001-1).",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6202",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6203",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(paefs_objtypes.SafetySystemType, ns0.reftypes.HasAddIn, o6.ns["ns=paefs;i=5089"])
o6.reference(o6.ns["ns=paefs;i=5111"], "i=17604", o6.ns["ns=paefs;i=5089"])
machinery_processvalues.vartypes.ProcessValueSetpointVariableType(
    nodeId="ns=paefs;i=6205",
    browseName="ns=machinery_processvalues;ProcessValueSetpoint",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6207", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6209", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5072",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6110", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6106"]),
        o6.hasComponent(o6.ns["ns=paefs;i=6205"]),
    ],
)
paefs_objtypes.SensorSetpointWriteType(
    nodeId="ns=paefs;i=5031",
    browseName="ns=paefs;DosageAmount",
    description="The amount of filter aid that is added per cycle.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5072"])],
)
o6.reference(paefs_objtypes.FilterAidDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5031"])
machinery_processvalues.vartypes.ProcessValueSetpointVariableType(
    nodeId="ns=paefs;i=6210",
    browseName="ns=machinery_processvalues;ProcessValueSetpoint",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6211", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6212", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5073",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6115", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6112"]),
        o6.hasComponent(o6.ns["ns=paefs;i=6210"]),
    ],
)
paefs_objtypes.SensorSetpointWriteType(
    nodeId="ns=paefs;i=5043",
    browseName="ns=paefs;ReservoirPressure",
    description="Describes the pressure of the compressed gas reservoir of the system.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5073"])],
)
o6.reference(paefs_objtypes.CleaningUnitType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5043"])
machinery_processvalues.vartypes.ProcessValueSetpointVariableType(
    nodeId="ns=paefs;i=6213",
    browseName="ns=machinery_processvalues;ProcessValueSetpoint",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6214", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6215", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5074",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6119", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6116"]),
        o6.hasComponent(o6.ns["ns=paefs;i=6213"]),
    ],
)
paefs_objtypes.SensorSetpointWriteType(
    nodeId="ns=paefs;i=5047",
    browseName="ns=paefs;Temperature",
    description="Temperature of the process gas.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5074"])],
)
o6.reference(paefs_objtypes.TemperatureRegulatorType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5047"])
machinery_processvalues.vartypes.ProcessValueSetpointVariableType(
    nodeId="ns=paefs;i=6216",
    browseName="ns=machinery_processvalues;ProcessValueSetpoint",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6217", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6218", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5098",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6156", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6153"]),
        o6.hasComponent(o6.ns["ns=paefs;i=6216"]),
    ],
)
paefs_objtypes.SensorSetpointWriteType(
    nodeId="ns=paefs;i=5048",
    browseName="ns=paefs;FilterCleaningEffect",
    description="The filter cleaning effect describes the change in state of the separator after the last cleaning cycle has been run through. This can be, for example, a change in the pressure difference before and after the cleaning cycle.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5098"])],
)
o6.reference(paefs_objtypes.CleaningUnitType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5048"])
machinery_processvalues.vartypes.ProcessValueSetpointVariableType(
    nodeId="ns=paefs;i=6221",
    browseName="ns=machinery_processvalues;ProcessValueSetpoint",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6222", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6223", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=paefs;i=5103",
    browseName="ns=paefs;Signal",
    description="Value of the signal. This includes min/max ranges, unit and other meta information. The optional setpoint should be implemented only for SensorSetpointReadType and SensorSetpointWriteType types.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6184", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6174"]),
        o6.hasComponent(o6.ns["ns=paefs;i=6221"]),
    ],
)
paefs_objtypes.SensorSetpointWriteType(
    nodeId="ns=paefs;i=5077",
    browseName="ns=paefs;CleaningInterval",
    description="Time between cleaning cycles.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=5103"])],
)
o6.reference(paefs_objtypes.CleaningUnitType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5077"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=paefs;i=6236",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6237", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=paefs;i=5104",
    browseName="ns=machinery;MachineryItemState",
    description="StateMachine representing the operating state of the separator (OPC 40001-1).",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=6236"])],
)
o6.reference(paefs_objtypes.SeparatorType, ns0.reftypes.HasAddIn, o6.ns["ns=paefs;i=5104"])
o6.reference(o6.ns["ns=paefs;i=5113"], "i=17604", o6.ns["ns=paefs;i=5104"])
ns0.vartypes.PropertyType(
    nodeId="ns=paefs;i=6240",
    browseName="EnumStrings",
    parent="ns=paefs;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("Analog"), o6.LocalizedText("Digital")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=paefs;i=6241",
    browseName="EnumStrings",
    parent="ns=paefs;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("Automatic"), o6.LocalizedText("Manual"), o6.LocalizedText("Other")],
)
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=paefs;i=5087",
    browseName="ns=di;Identification",
    description="Data for component identification (OPC 40001-1).",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6020",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6242",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(paefs_objtypes.DischargeSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=paefs;i=5087"])
o6.reference(o6.ns["ns=paefs;i=5115"], "i=17604", o6.ns["ns=paefs;i=5087"])
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=paefs;i=6244",
    browseName="ns=paefs;RatedPower",
    description="The rated power of the filter system is the nominal electrical power of the unit under operating conditions specified by the manufacturer.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6245", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6246", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=paefs;i=6247",
    browseName="ns=paefs;NominalAirflow",
    description="The nominal airflow of the filter system is the value specified by the manufacturer which defines the nominal extraction capacity of a unit under operating conditions.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6248", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6249", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
machinery.objtypes.MachineIdentificationType(
    nodeId="ns=paefs;i=5084",
    browseName="ns=di;Identification",
    description="Data for identification (OPC 40001-1): The FilterSystem should only have an Identification folder if the system as a whole is considered a machine. If the individual filter units are considered machines, the FilterSystem should not have an Identification folder.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6177",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6178",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6179",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6243",
                browseName="ns=paefs;ExIdentification",
                description="The marking on the type plate of the filter system regarding explosion protection.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6244"]),
        o6.hasComponent(o6.ns["ns=paefs;i=6247"]),
    ],
)
o6.reference(paefs_objtypes.FilterSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=paefs;i=5084"])
o6.reference(o6.ns["ns=paefs;i=5107"], "i=17604", o6.ns["ns=paefs;i=5084"])
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=paefs;i=6253",
    browseName="ns=paefs;NominalAirflow",
    description="The nominal airflow of the filter unit is the value specified by the manufacturer which defines the nominal extraction capacity of a filter unit under operating conditions.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6254", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6255", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=paefs;i=6256",
    browseName="ns=paefs;RatedPower",
    description="The rated power of the filter unit is the nominal electrical power of the filter unit under operating conditions specified by the manufacturer.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6257", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6258", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=paefs;i=6259",
    browseName="ns=paefs;RatedPower",
    description="The rated power of the filter unit is the nominal electrical power of the filter unit under operating conditions specified by the manufacturer.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6260", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6261", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=paefs;i=6262",
    browseName="ns=paefs;NominalAirflow",
    description="The nominal airflow of the filter unit is the value specified by the manufacturer which defines the nominal extraction capacity of a filter unit under operating conditions.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6263", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6264", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.PropertyType(
    nodeId="ns=paefs;i=6266",
    browseName="EnumStrings",
    parent="ns=paefs;i=3005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("Open"), o6.LocalizedText("Closed"), o6.LocalizedText("Opening"), o6.LocalizedText("Closing")],
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=paefs;i=6429",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6431", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=paefs;i=5209",
    browseName="ns=machinery;MachineryItemState",
    description="StateMachine representing the operating state of the unit (OPC 40001-1).",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=6429"])],
)
o6.reference(paefs_objtypes.SafetySystemType, ns0.reftypes.HasAddIn, o6.ns["ns=paefs;i=5209"])
o6.reference(o6.ns["ns=paefs;i=5111"], "i=17604", o6.ns["ns=paefs;i=5209"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=paefs;i=5080",
    browseName="ns=di;Identification",
    description="Data for component identification (OPC 40001-1).",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6433",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6434",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(paefs_objtypes.FanType, ns0.reftypes.HasAddIn, o6.ns["ns=paefs;i=5080"])
o6.reference(o6.ns["ns=paefs;i=5109"], "i=17604", o6.ns["ns=paefs;i=5080"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=paefs;i=5081",
    browseName="ns=di;Identification",
    description="Data for component identification (OPC 40001-1).",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6435",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6436",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=paefs;i=6437",
    browseName="ns=paefs;NominalAirflow",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6438", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6439", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(paefs_objtypes.FilterMachineIdentificationType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=6437"])
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=paefs;i=6441",
    browseName="ns=paefs;RatedPower",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6442", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6443", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(paefs_objtypes.FilterMachineIdentificationType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=6441"])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=paefs;i=5082",
    browseName="ns=di;Identification",
    description="Data for machine identification (OPC 40001-1): The Identification folder can have either the concrete type MachineIdentificationType or MachineryComponentType. If the filter unit is considered a component of a larger filter machine, MachineryComponentType is used. If the filter unit is considered a machine by itself, MachineIdentificationType is used.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6252",
                browseName="ns=paefs;ExIdentification",
                description="The marking on the type plate of the filter unit regarding explosion protection.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6444",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6445",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6253"]),
        o6.hasComponent(o6.ns["ns=paefs;i=6256"]),
    ],
    _allow_abstract=True,
)
o6.reference(paefs_objtypes.FilterUnitType, ns0.reftypes.HasAddIn, o6.ns["ns=paefs;i=5082"])
o6.reference(o6.ns["ns=paefs;i=5108"], "i=17604", o6.ns["ns=paefs;i=5082"])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=paefs;i=5083",
    browseName="ns=di;Identification",
    description="Data for machine identification (OPC 40001-1): The Identification folder can have either the concrete type MachineIdentificationType or MachineryComponentType. If the filter unit is considered a component of a larger filter machine, MachineryComponentType is used. If the filter unit is considered a machine by itself, MachineIdentificationType is used.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6446",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6447",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=6259"]),
        o6.hasComponent(o6.ns["ns=paefs;i=6262"]),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=paefs;i=5085",
    browseName="ns=di;Identification",
    description="Data for machine identification (OPC 40001-1).",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6462",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6463",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(paefs_objtypes.FilterAidDeviceType, ns0.reftypes.HasAddIn, o6.ns["ns=paefs;i=5085"])
o6.reference(o6.ns["ns=paefs;i=5112"], "i=17604", o6.ns["ns=paefs;i=5085"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=paefs;i=5086",
    browseName="ns=di;Identification",
    description="Data for machine identification (OPC 40001-1).",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6464",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6465",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=paefs;i=5090",
    browseName="ns=di;Identification",
    description="Data for component identification (OPC 40001-1).",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6466",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6467",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=paefs;i=5091",
    browseName="ns=di;Identification",
    description="Data for machine identification (OPC 40001-1).",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6468",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6469",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(paefs_objtypes.SeparatorType, ns0.reftypes.HasAddIn, o6.ns["ns=paefs;i=5091"])
o6.reference(o6.ns["ns=paefs;i=5113"], "i=17604", o6.ns["ns=paefs;i=5091"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=paefs;i=6470",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=6471", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=paefs;i=5092",
    browseName="ns=machinery;MachineryItemState",
    description="StateMachine representing the operating state of the filter unit (OPC 40001-1).",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=6470"])],
)
o6.reference(paefs_objtypes.FilterUnitType, ns0.reftypes.HasAddIn, o6.ns["ns=paefs;i=5092"])
o6.reference(o6.ns["ns=paefs;i=5108"], "i=17604", o6.ns["ns=paefs;i=5092"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=paefs;i=6407",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=8422", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=paefs;i=5199",
    browseName="ns=machinery;MachineryItemState",
    description="StateMachine representing the operating state of the unit (OPC 40001-1).",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=6407"])],
)
o6.reference(paefs_objtypes.CleaningUnitType, ns0.reftypes.HasAddIn, o6.ns["ns=paefs;i=5199"])
o6.reference(o6.ns["ns=paefs;i=5114"], "i=17604", o6.ns["ns=paefs;i=5199"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=paefs;i=8429",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=8430", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=paefs;i=5200",
    browseName="ns=machinery;MachineryItemState",
    description="StateMachine representing the operating state of the unit (OPC 40001-1).",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=8429"])],
)
paefs_objtypes.CleaningUnitType(
    nodeId="ns=paefs;i=5044",
    browseName="ns=paefs;<CleaningUnit>",
    description="The cleaning units that are part of the filter unit.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6206", browseName="ns=paefs;CleaningActive", description="Describes that the unit is currently in a cleaning cycle.", dataType=o6.Boolean
            )
        ),
        o6.hasAddIn(o6.ns["ns=paefs;i=5088"]),
        o6.hasAddIn(o6.ns["ns=paefs;i=5200"]),
    ],
)
o6.reference(paefs_objtypes.FilterUnitType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5044"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=paefs;i=6419",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=8431", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=paefs;i=5201",
    browseName="ns=machinery;MachineryItemState",
    description="StateMachine representing the operating state of the discharge system (OPC 40001-1).",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=6419"])],
)
o6.reference(paefs_objtypes.DischargeSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=paefs;i=5201"])
o6.reference(o6.ns["ns=paefs;i=5115"], "i=17604", o6.ns["ns=paefs;i=5201"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=paefs;i=8432",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=8433", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=paefs;i=5202",
    browseName="ns=machinery;MachineryItemState",
    description="StateMachine representing the operating state of the discharge system (OPC 40001-1).",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=8432"])],
)
paefs_objtypes.DischargeSystemType(
    nodeId="ns=paefs;i=5022",
    browseName="ns=paefs;<DischargeSystem>",
    description="The discharge systems that are part of the filter unit.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6425",
                browseName="ns=paefs;MaintenanceSwitchOn",
                description="Status of a physical maintenance switch on the discharge system. True when the switch is on.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasAddIn(o6.ns["ns=paefs;i=5202"]),
    ],
)
o6.reference(paefs_objtypes.FilterUnitType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5022"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=paefs;i=6396",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=8434", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=paefs;i=5203",
    browseName="ns=machinery;MachineryItemState",
    description="StateMachine representing the operating state of the fan (OPC 40001-1).",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=6396"])],
)
o6.reference(paefs_objtypes.FanType, ns0.reftypes.HasAddIn, o6.ns["ns=paefs;i=5203"])
o6.reference(o6.ns["ns=paefs;i=5109"], "i=17604", o6.ns["ns=paefs;i=5203"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=paefs;i=8435",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=8436", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=paefs;i=5204",
    browseName="ns=machinery;MachineryItemState",
    description="StateMachine representing the operating state of the fan (OPC 40001-1).",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=8435"])],
)
paefs_objtypes.FanType(
    nodeId="ns=paefs;i=5007",
    browseName="ns=paefs;<Fan>",
    description="All fans used on the server.",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=paefs;i=5081"]), o6.hasAddIn(o6.ns["ns=paefs;i=5204"])],
)
o6.reference(paefs_objtypes.FilterSystemType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5007"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=paefs;i=6147",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=8437", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=paefs;i=5205",
    browseName="ns=machinery;MachineryItemState",
    description="StateMachine representing the operating state of the device (OPC 40001-1).",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=6147"])],
)
o6.reference(paefs_objtypes.FilterAidDeviceType, ns0.reftypes.HasAddIn, o6.ns["ns=paefs;i=5205"])
o6.reference(o6.ns["ns=paefs;i=5112"], "i=17604", o6.ns["ns=paefs;i=5205"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=paefs;i=8438",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=8439", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=paefs;i=5206",
    browseName="ns=machinery;MachineryItemState",
    description="StateMachine representing the operating state of the device (OPC 40001-1).",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=8438"])],
)
paefs_objtypes.FilterAidDeviceType(
    nodeId="ns=paefs;i=5004",
    browseName="ns=paefs;<FilterAidDevice>",
    description="All filter aid devices that are used on the server.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6235",
                browseName="ns=paefs;Malfunction",
                description="Indicates that the filter aid device is malfunctioning. True in case of error. Malfunctions can be, for example, that there is no more filter aid or that there is a malfunction in the subsystems of the filter aid device.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasAddIn(o6.ns["ns=paefs;i=5086"]),
        o6.hasAddIn(o6.ns["ns=paefs;i=5206"]),
    ],
)
o6.reference(paefs_objtypes.FilterSystemType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5004"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=paefs;i=8440",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=8441", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=paefs;i=5207",
    browseName="ns=machinery;MachineryItemState",
    description="StateMachine representing the operating state of the filter system (OPC 40001-1).",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=8440"])],
)
o6.reference(paefs_objtypes.FilterSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=paefs;i=5207"])
o6.reference(o6.ns["ns=paefs;i=5107"], "i=17604", o6.ns["ns=paefs;i=5207"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=paefs;i=8442",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=8443", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=paefs;i=5208",
    browseName="ns=machinery;MachineryItemState",
    description="StateMachine representing the operating state of the filter unit (OPC 40001-1).",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=8442"])],
)
paefs_objtypes.FilterUnitType(
    nodeId="ns=paefs;i=5018",
    browseName="ns=paefs;<FilterUnit>",
    description="All filter units of the system.",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6037",
                browseName="ns=paefs;MaintenanceRequested",
                description="The maintenance request allows the manufacturer to inform the operator that the system requires maintenance. True = maintenance requested by system. False = no maintenance requested.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6452",
                browseName="ns=paefs;Malfunction",
                description="One or more subsystems of the filter unit have a malfunction. True in case of error.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            paefs_objtypes.SeparatorType(
                nodeId="ns=paefs;i=5019",
                browseName="ns=paefs;<Separator>",
                description="The separators that are part of the filter unit.",
                modellingRule="MandatoryPlaceholder",
                _allow_abstract=True,
            )
        ),
        o6.hasComponent(
            paefs_objtypes.AirConnectionType(
                nodeId="ns=paefs;i=5020",
                browseName="ns=paefs;AirIntakeConnection",
                description="The connection to the ducting system from which the polluted process gas enters the filter unit.",
            )
        ),
        o6.hasComponent(
            paefs_objtypes.AirConnectionType(
                nodeId="ns=paefs;i=5021",
                browseName="ns=paefs;AirOutletConnection",
                description="The connection to the ducting system through which the cleaned process gas leaves the filter unit.",
            )
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=5038"]),
        o6.hasAddIn(o6.ns["ns=paefs;i=5083"]),
        o6.hasAddIn(o6.ns["ns=paefs;i=5208"]),
    ],
)
o6.reference(paefs_objtypes.FilterSystemType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5018"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=paefs;i=8444",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=8445", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=paefs;i=5210",
    browseName="ns=machinery;MachineryItemState",
    description="StateMachine representing the operating state of the unit (OPC 40001-1).",
    references=[o6.hasComponent(o6.ns["ns=paefs;i=8444"])],
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=paefs;i=8446",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=paefs;i=8447", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(nodeId="ns=paefs;i=5211", browseName="ns=paefs;MachineryState", references=[o6.hasComponent(o6.ns["ns=paefs;i=8446"])])
paefs_objtypes.SafetySystemType(
    nodeId="ns=paefs;i=5006",
    browseName="ns=paefs;<SafetySystem>",
    description="All safety systems used on the server.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6220",
                browseName="ns=paefs;Triggered",
                description="Indicates that the safety system has been triggered. If true the safety system has been triggered.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=paefs;i=6432",
                browseName="ns=paefs;Malfunction",
                description="Indicates that the safety system is malfunctioning. True in case of error.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=paefs;i=5211"]),
        o6.hasAddIn(o6.ns["ns=paefs;i=5090"]),
        o6.hasAddIn(o6.ns["ns=paefs;i=5210"]),
    ],
)
o6.reference(paefs_objtypes.FilterSystemType, ns0.reftypes.HasComponent, o6.ns["ns=paefs;i=5006"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, irdi, machinery, machinery_processvalues, ns0, padim, paefs_reftypes, paefs_datypes, paefs_objtypes
