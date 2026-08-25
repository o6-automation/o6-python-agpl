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

"""Generated OPC UA pnenc namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import datatypes as pnenc_datypes
from . import objtypes as pnenc_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnenc;i=5002", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnenc;i=5003", browseName="Default XML")
o6.hasEncoding(pnenc_datypes.LogEntryDataType, o6.ns["ns=pnenc;i=5003"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnenc;i=5004", browseName="Default JSON")
o6.hasEncoding(pnenc_datypes.LogEntryDataType, o6.ns["ns=pnenc;i=5004"])
ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6004",
    browseName="EnumValues",
    parent="ns=pnenc;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[11],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("NORMAL_OPERATION"), description=o6.LocalizedText("The position feedback interface operates normally")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ERROR_ACKNOWLEDGEMENT"), description=o6.LocalizedText("Error acknowledgement is being processed")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("ERROR"), description=o6.LocalizedText("There is an error present")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("REFERENCE_VALUE_Gx_XIST2"), description=o6.LocalizedText("The reference value is loaded in Gx_XIST2")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("WAIT_FOR_REFERENCE_MARKS"), description=o6.LocalizedText("The reference mark is expected")),
        ns0.datatypes.EnumValueType(
            value=5, displayName=o6.LocalizedText("SET_SHIFT_HOME_POSITION"), description=o6.LocalizedText("Gx_XIST1 and Gx_XIST2 are set or shifted by a predefined preset value")
        ),
        ns0.datatypes.EnumValueType(
            value=6, displayName=o6.LocalizedText("WAIT_FOR_MEASURED_VALUE"), description=o6.LocalizedText("Measurement task active, waiting for measurement values")
        ),
        ns0.datatypes.EnumValueType(
            value=7, displayName=o6.LocalizedText("MEASURED_VALUE_IN_XIST2"), description=o6.LocalizedText("The requested measured value is loaded into Gx_XIST2")
        ),
        ns0.datatypes.EnumValueType(
            value=8,
            displayName=o6.LocalizedText("PARKING"),
            description=o6.LocalizedText("The position feedback interface is inactive and does not deliver a valid Gx_XIST1 value"),
        ),
        ns0.datatypes.EnumValueType(
            value=9, displayName=o6.LocalizedText("PARKING_ERROR"), description=o6.LocalizedText("There is an error present and Gx_XIST1 is signaled invalid")
        ),
        ns0.datatypes.EnumValueType(
            value=10, displayName=o6.LocalizedText("PARKING_ERROR_ACK"), description=o6.LocalizedText("Error acknowledgement is being processed and Gx_XIST1 is signaled invalid")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6021",
    browseName="EnumValues",
    parent="ns=pnenc;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("FAULT"), description=o6.LocalizedText("The log entry indicates a malfunction of the encoder, e.g. position fault")
        ),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("WARNING"), description=o6.LocalizedText("The log entry is a warning, e.g. for battery status")),
        ns0.datatypes.EnumValueType(
            value=255,
            displayName=o6.LocalizedText("UNSPECIFIED"),
            description=o6.LocalizedText(
                "No information about the type of the event is given.  The intended purpose for the definition is usage by the GetFilteredLogbookEntries Method to specify &#8220;don&#8217;t care&#8221; for the EventType parameter. Must not be used for log entries and encoder diagnosis events as EncoderDiagnosisEventType and LogbookEventType"
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6022",
    browseName="EnumValues",
    parent="ns=pnenc;i=3005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("INCREASING_CLOCKWISE"),
            description=o6.LocalizedText("Increasing position values with clockwise rotation (viewed from shaft side)"),
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("INCREASING_COUNTERCLOCKWISE"),
            description=o6.LocalizedText("Increasing position values with counterclockwise rotation (viewed from shaft side)"),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6023",
    browseName="EnumValues",
    parent="ns=pnenc;i=3004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("ROTARY"), description=o6.LocalizedText("Rotating Axis")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("LINEAR"), description=o6.LocalizedText("Linear Axis")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6024",
    browseName="EnumValues",
    parent="ns=pnenc;i=3008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("SINGLETURN"), description=o6.LocalizedText("Singleturn sensor absolute type")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("MULTITURN"), description=o6.LocalizedText("Multiturn sensor absolute type")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6025",
    browseName="EnumValues",
    parent="ns=pnenc;i=3006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("ALARM_CHANNEL_DISABLED"), description=o6.LocalizedText("No Profile specific diagnosis (default)")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ALARM_CHANNEL_ENABLED"), description=o6.LocalizedText("Profile specific diagnosis is switched-on")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6026",
    browseName="EnumValues",
    parent="ns=pnenc;i=3007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("ENABLE_PRESET_CONTROL"), description=o6.LocalizedText("G1_XIST1 is affected by a Set-/Shift home position function command")
        ),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("DISABLE_PRESET_CONTROL"), description=o6.LocalizedText("Set-/Shift home position function does not affect G1_XIST1")
        ),
    ],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnenc;i=6027", browseName="ns=pnenc;LogEntryDataType", dataType=o6.String, value="LogEntryDataType")
o6.reference(o6.ns["ns=pnenc;i=5002"], "i=39", o6.ns["ns=pnenc;i=6027"])
pNENC = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=pnenc;i=6005",
    browseName="ns=pnenc;PNENC",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PNENC/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6006", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PNENC/")),
        o6.hasComponent(o6.ns["ns=pnenc;i=6027"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/PNENC/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/PNENC/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="LogEntryDataType">\n  <opc:Field TypeName="opc:Byte" Name="FaultSituationNumber"/>\n  <opc:Field TypeName="opc:UInt32" Name="EventNumber"/>\n  <opc:Field TypeName="tns:EventTypeEnumeration" Name="EventType"/>\n  <opc:Field TypeName="opc:Int32" Name="EventCode"/>\n  <opc:Field TypeName="ua:LocalizedText" Name="EventText"/>\n  <opc:Field TypeName="opc:DateTime" Name="EventComing"/>\n  <opc:Field TypeName="opc:DateTime" Name="EventGoing"/>\n  <opc:Field TypeName="opc:DateTime" Name="EventAcknowledged"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="EncoderAlarmChannelControlEnumeration">\n  <opc:EnumeratedValue Name="ALARM_CHANNEL_DISABLED" Value="0"/>\n  <opc:EnumeratedValue Name="ALARM_CHANNEL_ENABLED" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="EncoderAxisTypeEnumeration">\n  <opc:EnumeratedValue Name="ROTARY" Value="0"/>\n  <opc:EnumeratedValue Name="LINEAR" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="EncoderChannelStateEnumeration">\n  <opc:EnumeratedValue Name="NORMAL_OPERATION" Value="0"/>\n  <opc:EnumeratedValue Name="ERROR_ACKNOWLEDGEMENT" Value="1"/>\n  <opc:EnumeratedValue Name="ERROR" Value="2"/>\n  <opc:EnumeratedValue Name="REFERENCE_VALUE_Gx_XIST2" Value="3"/>\n  <opc:EnumeratedValue Name="WAIT_FOR_REFERENCE_MARKS" Value="4"/>\n  <opc:EnumeratedValue Name="SET_SHIFT_HOME_POSITION" Value="5"/>\n  <opc:EnumeratedValue Name="WAIT_FOR_MEASURED_VALUE" Value="6"/>\n  <opc:EnumeratedValue Name="MEASURED_VALUE_IN_XIST2" Value="7"/>\n  <opc:EnumeratedValue Name="PARKING" Value="8"/>\n  <opc:EnumeratedValue Name="PARKING_ERROR" Value="9"/>\n  <opc:EnumeratedValue Name="PARKING_ERROR_ACK" Value="10"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="EncoderCodeSequenceEnumeration">\n  <opc:EnumeratedValue Name="INCREASING_CLOCKWISE" Value="0"/>\n  <opc:EnumeratedValue Name="INCREASING_COUNTERCLOCKWISE" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="EncoderConfigParameterResultEnumeration">\n  <opc:EnumeratedValue Name="INVALID" Value="0"/>\n  <opc:EnumeratedValue Name="NOT_SUPPORTED" Value="1"/>\n  <opc:EnumeratedValue Name="READ_ONLY" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="EncoderConfigTypeEnumeration">\n  <opc:EnumeratedValue Name="STATIC" Value="0"/>\n  <opc:EnumeratedValue Name="DYNAMIC" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="EncoderDiagnosisReasonEnumeration">\n  <opc:EnumeratedValue Name="ALL_DISAPPEARS" Value="0"/>\n  <opc:EnumeratedValue Name="APPEARS" Value="1"/>\n  <opc:EnumeratedValue Name="DISAPPEARS" Value="2"/>\n  <opc:EnumeratedValue Name="DISAPPEARS_OTHER_REMAIN" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="EncoderPresetControlEnumeration">\n  <opc:EnumeratedValue Name="ENABLE_PRESET_CONTROL" Value="0"/>\n  <opc:EnumeratedValue Name="DISABLE_PRESET_CONTROL" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="EncoderSensorAbsoluteTypeEnumeration">\n  <opc:EnumeratedValue Name="SINGLETURN" Value="0"/>\n  <opc:EnumeratedValue Name="MULTITURN" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="EncoderSignalTypeEnumeration">\n  <opc:EnumeratedValue Name="OTHER" Value="0"/>\n  <opc:EnumeratedValue Name="BISS_C" Value="1"/>\n  <opc:EnumeratedValue Name="ENDAT2.1" Value="2"/>\n  <opc:EnumeratedValue Name="ENDAT2.2" Value="3"/>\n  <opc:EnumeratedValue Name="HIPERFACE" Value="4"/>\n  <opc:EnumeratedValue Name="HIPERFACE_DSL" Value="5"/>\n  <opc:EnumeratedValue Name="SSI_BINARY" Value="6"/>\n  <opc:EnumeratedValue Name="SSI_GRAY_CODE" Value="7"/>\n  <opc:EnumeratedValue Name="SINCOS_1VSS" Value="8"/>\n  <opc:EnumeratedValue Name="SCS_OPEN_LINK" Value="9"/>\n  <opc:EnumeratedValue Name="DRIVEClIQ" Value="10"/>\n  <opc:EnumeratedValue Name="BISS_LINE" Value="11"/>\n  <opc:EnumeratedValue Name="FANUC_37BIT_SERIAL_COMM" Value="12"/>\n  <opc:EnumeratedValue Name="MITSUBISHI_40BIT_SERIAL_COMM" Value="13"/>\n  <opc:EnumeratedValue Name="OMRON/PANASONIC_48BIT_SERIAL_COMM" Value="14"/>\n  <opc:EnumeratedValue Name="YASKAWA_36BIT_SERIAL_COMM" Value="15"/>\n  <opc:EnumeratedValue Name="RS422_5V_TTL" Value="16"/>\n  <opc:EnumeratedValue Name="RS422_5..30V" Value="17"/>\n  <opc:EnumeratedValue Name="SINCOS_1VPP" Value="18"/>\n  <opc:EnumeratedValue Name="RESOLVER" Value="19"/>\n  <opc:EnumeratedValue Name="HTL_PUSH-PULL" Value="20"/>\n  <opc:EnumeratedValue Name="RS485" Value="21"/>\n  <opc:EnumeratedValue Name="RS485_SINCOS" Value="22"/>\n  <opc:EnumeratedValue Name="RS485_HTL" Value="23"/>\n  <opc:EnumeratedValue Name="RS485_TTL" Value="24"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="EventTypeEnumeration">\n  <opc:EnumeratedValue Name="FAULT" Value="0"/>\n  <opc:EnumeratedValue Name="WARNING" Value="1"/>\n  <opc:EnumeratedValue Name="UNSPECIFIED" Value="255"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6028",
    browseName="EnumValues",
    parent="ns=pnenc;i=3009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[25],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OTHER"), description=o6.LocalizedText("Other encoder protocol")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("BISS_C"), description=o6.LocalizedText("BiSS interface continuous mode")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("ENDAT2.1"), description=o6.LocalizedText("EnDat (Encoder Data), operating mode 2.1")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("ENDAT2.2"), description=o6.LocalizedText("EnDat (Encoder Data), operating mode 2.2")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("HIPERFACE"), description=o6.LocalizedText("Hiperface")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("HIPERFACE_DSL"), description=o6.LocalizedText("Hiperface DSL (Digital Servo Link)")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("SSI_BINARY"), description=o6.LocalizedText("Binary synchronous serial output (SSI)")),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("SSI_GRAY_CODE"), description=o6.LocalizedText("Gray code synchronous serial output (SSI)")),
        ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("SINCOS_1VSS"), description=o6.LocalizedText("SinCos, 1 Vss output level")),
        ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("SCS_OPEN_LINK"), description=o6.LocalizedText("Single cable solution (SCS open link)")),
        ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("DRIVEClIQ"), description=o6.LocalizedText("DRIVE-CLiQ")),
        ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("BISS_LINE"), description=o6.LocalizedText("BiSS Line")),
        ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("FANUC_37BIT_SERIAL_COMM"), description=o6.LocalizedText("Fanuc 37-bit serial interface")),
        ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("MITSUBISHI_40BIT_SERIAL_COMM"), description=o6.LocalizedText("Mitsubishi 40-bit serial interface")),
        ns0.datatypes.EnumValueType(
            value=14, displayName=o6.LocalizedText("OMRON/PANASONIC_48BIT_SERIAL_COMM"), description=o6.LocalizedText("OMRON/Panasonic 48-bit serial interface")
        ),
        ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("YASKAWA_36BIT_SERIAL_COMM"), description=o6.LocalizedText("Yaskawa 36-bit serial interface")),
        ns0.datatypes.EnumValueType(
            value=16, displayName=o6.LocalizedText("RS422_5V_TTL"), description=o6.LocalizedText("RS422 (TTL - Transistor Transistor Logic), 5 V signal level")
        ),
        ns0.datatypes.EnumValueType(value=17, displayName=o6.LocalizedText("RS422_5..30V"), description=o6.LocalizedText("RS422 signal level depend on entry level 5 V to 30V")),
        ns0.datatypes.EnumValueType(value=18, displayName=o6.LocalizedText("SINCOS_1VPP"), description=o6.LocalizedText("SinCos, 1 Vss output level")),
        ns0.datatypes.EnumValueType(value=19, displayName=o6.LocalizedText("RESOLVER"), description=o6.LocalizedText("Resolver signal")),
        ns0.datatypes.EnumValueType(
            value=20, displayName=o6.LocalizedText("HTL_PUSH-PULL"), description=o6.LocalizedText("High Threshold Logic (HTL), typically voltage ranges from 5 to 30 VDC")
        ),
        ns0.datatypes.EnumValueType(
            value=21, displayName=o6.LocalizedText("RS485"), description=o6.LocalizedText("RS-485, signal is transmitted over a Sig+ line and a Sig- line")
        ),
        ns0.datatypes.EnumValueType(value=22, displayName=o6.LocalizedText("RS485_SINCOS"), description=o6.LocalizedText("RS-485, Sin-/Cos-Signal")),
        ns0.datatypes.EnumValueType(value=23, displayName=o6.LocalizedText("RS485_HTL"), description=o6.LocalizedText("RS-485, High Threshold Logic (HTL) signal")),
        ns0.datatypes.EnumValueType(value=24, displayName=o6.LocalizedText("RS485_TTL"), description=o6.LocalizedText("RS-485, Transistor Transistor Logic (TTL) signal")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6029",
    browseName="EnumValues",
    parent="ns=pnenc;i=3010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("INVALID"), description=o6.LocalizedText("The value is not accepted as configuration value")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("NOT_SUPPORTED"), description=o6.LocalizedText("The configuration value is not supported by the Server")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("READ_ONLY"), description=o6.LocalizedText("The configuration value is not writable")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6030",
    browseName="EnumValues",
    parent="ns=pnenc;i=3011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("STATIC"), description=o6.LocalizedText("Static configuration type")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("DYNAMIC"), description=o6.LocalizedText("Dynamic configuration type")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6031",
    browseName="EnumValues",
    parent="ns=pnenc;i=3012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("ALL_DISAPPEARS"), description=o6.LocalizedText("No diagnosis condition of any severity is persisting")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("APPEARS"), description=o6.LocalizedText("The diagnosis condition indicated arises and/or persists")),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("DISAPPEARS"),
            description=o6.LocalizedText(
                "The diagnosis condition indicated does not longer persist. No diagnosis condition of the same severity is persisting for the affected channel"
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("DISAPPEARS_OTHER_REMAIN"),
            description=o6.LocalizedText("The diagnosis condition indicated does not longer persist. Other diagnosis conditions of the same severity are persisting"),
        ),
    ],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnenc;i=6032", browseName="ns=pnenc;LogEntryDataType", dataType=o6.String, value="//xs:element[@name='LogEntryDataType']")
o6.reference(o6.ns["ns=pnenc;i=5003"], "i=39", o6.ns["ns=pnenc;i=6032"])
pNENC_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=pnenc;i=6007",
    browseName="ns=pnenc;PNENC",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PNENC/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6008", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PNENC/Types.xsd")),
        o6.hasComponent(o6.ns["ns=pnenc;i=6032"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/PNENC/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/PNENC/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="EncoderAlarmChannelControlEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="ALARM_CHANNEL_DISABLED_0"/>\n   <xs:enumeration value="ALARM_CHANNEL_ENABLED_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:EncoderAlarmChannelControlEnumeration" name="EncoderAlarmChannelControlEnumeration"/>\n <xs:complexType name="ListOfEncoderAlarmChannelControlEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:EncoderAlarmChannelControlEnumeration" name="EncoderAlarmChannelControlEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfEncoderAlarmChannelControlEnumeration" name="ListOfEncoderAlarmChannelControlEnumeration" nillable="true"/>\n <xs:simpleType name="EncoderAxisTypeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="ROTARY_0"/>\n   <xs:enumeration value="LINEAR_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:EncoderAxisTypeEnumeration" name="EncoderAxisTypeEnumeration"/>\n <xs:complexType name="ListOfEncoderAxisTypeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:EncoderAxisTypeEnumeration" name="EncoderAxisTypeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfEncoderAxisTypeEnumeration" name="ListOfEncoderAxisTypeEnumeration" nillable="true"/>\n <xs:simpleType name="EncoderChannelStateEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="NORMAL_OPERATION_0"/>\n   <xs:enumeration value="ERROR_ACKNOWLEDGEMENT_1"/>\n   <xs:enumeration value="ERROR_2"/>\n   <xs:enumeration value="REFERENCE_VALUE_Gx_XIST2_3"/>\n   <xs:enumeration value="WAIT_FOR_REFERENCE_MARKS_4"/>\n   <xs:enumeration value="SET_SHIFT_HOME_POSITION_5"/>\n   <xs:enumeration value="WAIT_FOR_MEASURED_VALUE_6"/>\n   <xs:enumeration value="MEASURED_VALUE_IN_XIST2_7"/>\n   <xs:enumeration value="PARKING_8"/>\n   <xs:enumeration value="PARKING_ERROR_9"/>\n   <xs:enumeration value="PARKING_ERROR_ACK_10"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:EncoderChannelStateEnumeration" name="EncoderChannelStateEnumeration"/>\n <xs:complexType name="ListOfEncoderChannelStateEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:EncoderChannelStateEnumeration" name="EncoderChannelStateEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfEncoderChannelStateEnumeration" name="ListOfEncoderChannelStateEnumeration" nillable="true"/>\n <xs:simpleType name="EncoderCodeSequenceEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="INCREASING_CLOCKWISE_0"/>\n   <xs:enumeration value="INCREASING_COUNTERCLOCKWISE_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:EncoderCodeSequenceEnumeration" name="EncoderCodeSequenceEnumeration"/>\n <xs:complexType name="ListOfEncoderCodeSequenceEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:EncoderCodeSequenceEnumeration" name="EncoderCodeSequenceEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfEncoderCodeSequenceEnumeration" name="ListOfEncoderCodeSequenceEnumeration" nillable="true"/>\n <xs:simpleType name="EncoderConfigParameterResultEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="INVALID_0"/>\n   <xs:enumeration value="NOT_SUPPORTED_1"/>\n   <xs:enumeration value="READ_ONLY_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:EncoderConfigParameterResultEnumeration" name="EncoderConfigParameterResultEnumeration"/>\n <xs:complexType name="ListOfEncoderConfigParameterResultEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:EncoderConfigParameterResultEnumeration" name="EncoderConfigParameterResultEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfEncoderConfigParameterResultEnumeration" name="ListOfEncoderConfigParameterResultEnumeration" nillable="true"/>\n <xs:simpleType name="EncoderConfigTypeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="STATIC_0"/>\n   <xs:enumeration value="DYNAMIC_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:EncoderConfigTypeEnumeration" name="EncoderConfigTypeEnumeration"/>\n <xs:complexType name="ListOfEncoderConfigTypeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:EncoderConfigTypeEnumeration" name="EncoderConfigTypeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfEncoderConfigTypeEnumeration" name="ListOfEncoderConfigTypeEnumeration" nillable="true"/>\n <xs:simpleType name="EncoderDiagnosisReasonEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="ALL_DISAPPEARS_0"/>\n   <xs:enumeration value="APPEARS_1"/>\n   <xs:enumeration value="DISAPPEARS_2"/>\n   <xs:enumeration value="DISAPPEARS_OTHER_REMAIN_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:EncoderDiagnosisReasonEnumeration" name="EncoderDiagnosisReasonEnumeration"/>\n <xs:complexType name="ListOfEncoderDiagnosisReasonEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:EncoderDiagnosisReasonEnumeration" name="EncoderDiagnosisReasonEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfEncoderDiagnosisReasonEnumeration" name="ListOfEncoderDiagnosisReasonEnumeration" nillable="true"/>\n <xs:simpleType name="EncoderPresetControlEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="ENABLE_PRESET_CONTROL_0"/>\n   <xs:enumeration value="DISABLE_PRESET_CONTROL_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:EncoderPresetControlEnumeration" name="EncoderPresetControlEnumeration"/>\n <xs:complexType name="ListOfEncoderPresetControlEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:EncoderPresetControlEnumeration" name="EncoderPresetControlEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfEncoderPresetControlEnumeration" name="ListOfEncoderPresetControlEnumeration" nillable="true"/>\n <xs:simpleType name="EncoderSensorAbsoluteTypeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="SINGLETURN_0"/>\n   <xs:enumeration value="MULTITURN_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:EncoderSensorAbsoluteTypeEnumeration" name="EncoderSensorAbsoluteTypeEnumeration"/>\n <xs:complexType name="ListOfEncoderSensorAbsoluteTypeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:EncoderSensorAbsoluteTypeEnumeration" name="EncoderSensorAbsoluteTypeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfEncoderSensorAbsoluteTypeEnumeration" name="ListOfEncoderSensorAbsoluteTypeEnumeration" nillable="true"/>\n <xs:simpleType name="EncoderSignalTypeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OTHER_0"/>\n   <xs:enumeration value="BISS_C_1"/>\n   <xs:enumeration value="ENDAT2.1_2"/>\n   <xs:enumeration value="ENDAT2.2_3"/>\n   <xs:enumeration value="HIPERFACE_4"/>\n   <xs:enumeration value="HIPERFACE_DSL_5"/>\n   <xs:enumeration value="SSI_BINARY_6"/>\n   <xs:enumeration value="SSI_GRAY_CODE_7"/>\n   <xs:enumeration value="SINCOS_1VSS_8"/>\n   <xs:enumeration value="SCS_OPEN_LINK_9"/>\n   <xs:enumeration value="DRIVEClIQ_10"/>\n   <xs:enumeration value="BISS_LINE_11"/>\n   <xs:enumeration value="FANUC_37BIT_SERIAL_COMM_12"/>\n   <xs:enumeration value="MITSUBISHI_40BIT_SERIAL_COMM_13"/>\n   <xs:enumeration value="OMRON/PANASONIC_48BIT_SERIAL_COMM_14"/>\n   <xs:enumeration value="YASKAWA_36BIT_SERIAL_COMM_15"/>\n   <xs:enumeration value="RS422_5V_TTL_16"/>\n   <xs:enumeration value="RS422_5..30V_17"/>\n   <xs:enumeration value="SINCOS_1VPP_18"/>\n   <xs:enumeration value="RESOLVER_19"/>\n   <xs:enumeration value="HTL_PUSH-PULL_20"/>\n   <xs:enumeration value="RS485_21"/>\n   <xs:enumeration value="RS485_SINCOS_22"/>\n   <xs:enumeration value="RS485_HTL_23"/>\n   <xs:enumeration value="RS485_TTL_24"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:EncoderSignalTypeEnumeration" name="EncoderSignalTypeEnumeration"/>\n <xs:complexType name="ListOfEncoderSignalTypeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:EncoderSignalTypeEnumeration" name="EncoderSignalTypeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfEncoderSignalTypeEnumeration" name="ListOfEncoderSignalTypeEnumeration" nillable="true"/>\n <xs:simpleType name="EventTypeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="FAULT_0"/>\n   <xs:enumeration value="WARNING_1"/>\n   <xs:enumeration value="UNSPECIFIED_255"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:EventTypeEnumeration" name="EventTypeEnumeration"/>\n <xs:complexType name="ListOfEventTypeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:EventTypeEnumeration" name="EventTypeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfEventTypeEnumeration" name="ListOfEventTypeEnumeration" nillable="true"/>\n <xs:complexType name="LogEntryDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="FaultSituationNumber"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="EventNumber"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:EventTypeEnumeration" name="EventType"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="EventCode"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="EventText"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="EventComing"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="EventGoing"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="EventAcknowledged"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:LogEntryDataType" name="LogEntryDataType"/>\n <xs:complexType name="ListOfLogEntryDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:LogEntryDataType" name="LogEntryDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfLogEntryDataType" name="ListOfLogEntryDataType" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=pnenc;i=6106",
    browseName="ns=pnenc;Acceleration",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6107", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6108", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
)
o6.reference(pnenc_objtypes.EncoderChannelType, ns0.reftypes.HasComponent, o6.ns["ns=pnenc;i=6106"])
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=pnenc;i=6110",
    browseName="ns=pnenc;Temperature",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6111", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6112", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
)
o6.reference(pnenc_objtypes.EncoderChannelType, ns0.reftypes.HasComponent, o6.ns["ns=pnenc;i=6110"])
pnenc_objtypes.LogbookType(
    nodeId="ns=pnenc;i=5010",
    browseName="ns=pnenc;Logbook",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6113", browseName="ns=pnenc;LogbookSize", dataType=o6.UInt16)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=pnenc;i=6114",
                browseName="ns=pnenc;LogEntries",
                dataType=pnenc_datypes.LogEntryDataType,
                valueRank=1,
                arrayDimensions=[1],
                value=[
                    pnenc_datypes.LogEntryDataType(
                        faultSituationNumber=0,
                        eventNumber=0,
                        eventType=pnenc_datypes.EventTypeEnumeration.FAULT,
                        eventCode=0,
                        eventText=o6.LocalizedText(),
                        eventComing=o6.DateTime("1900-01-01T00:00:00Z"),
                        eventGoing=o6.DateTime("1900-01-01T00:00:00Z"),
                        eventAcknowledged=o6.DateTime("1900-01-01T00:00:00Z"),
                    )
                ],
            )
        ),
    ],
)
o6.reference(pnenc_objtypes.EncoderChannelType, ns0.reftypes.HasComponent, o6.ns["ns=pnenc;i=5010"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPNENCSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=pnenc;i=5013",
    browseName="ns=pnenc;http://opcfoundation.org/UA/PNENC/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6115", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6116", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2022-10-21T00:00:00Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6117", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PNENC/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6118", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pnenc;i=6119", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6120", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6121", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=pnenc;i=6100",
    browseName="ns=pnenc;Position",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6101", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6102", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6123", browseName="ns=pnenc;AbsolutePositionRange", dataType=ns0.datatypes.Range)),
        o6.hasComponent(ns0.vartypes.BaseAnalogType(nodeId="ns=pnenc;i=6122", browseName="ns=pnenc;Resolution", dataType=o6.Double)),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(pnenc_objtypes.EncoderChannelType, ns0.reftypes.HasComponent, o6.ns["ns=pnenc;i=6100"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=pnenc;i=6092",
    browseName="ns=pnenc;G1_XIST1",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6124", browseName="ns=pnenc;ShiftFactorXIST1", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6125", browseName="ns=pnenc;XIST1PresetControl", dataType=pnenc_datypes.EncoderPresetControlEnumeration)),
    ],
    dataType=o6.UInt32,
    value=0,
)
o6.reference(pnenc_objtypes.EncoderChannelType, ns0.reftypes.HasComponent, o6.ns["ns=pnenc;i=6092"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=pnenc;i=6093",
    browseName="ns=pnenc;G1_XIST2",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6126", browseName="ns=pnenc;ShiftFactorXIST2", dataType=o6.UInt16))],
    dataType=o6.UInt32,
    value=0,
)
o6.reference(pnenc_objtypes.EncoderChannelType, ns0.reftypes.HasComponent, o6.ns["ns=pnenc;i=6093"])
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=pnenc;i=6103",
    browseName="ns=pnenc;Velocity",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6104", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6105", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasComponent(ns0.vartypes.BaseAnalogType(nodeId="ns=pnenc;i=6127", browseName="ns=pnenc;Damping", dataType=o6.Float)),
    ],
    dataType=o6.Float,
    value=0.0,
)
o6.reference(pnenc_objtypes.EncoderChannelType, ns0.reftypes.HasComponent, o6.ns["ns=pnenc;i=6103"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=pnenc;i=6109",
    browseName="ns=pnenc;PositionSensorSignalValue",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6128", browseName="ns=pnenc;SignalType", dataType=pnenc_datypes.EncoderSignalTypeEnumeration))],
    dataType=ns0.datatypes.Number,
)
o6.reference(pnenc_objtypes.EncoderChannelType, ns0.reftypes.HasComponent, o6.ns["ns=pnenc;i=6109"])
pnenc_objtypes.EncoderSensorType(
    nodeId="ns=pnenc;i=5011",
    browseName="ns=pnenc;Sensor",
    modellingRule="Mandatory",
    references=[o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pnenc;i=6129", browseName="ns=pnenc;PositionOffset", dataType=ns0.datatypes.Number))],
)
o6.reference(pnenc_objtypes.EncoderChannelType, ns0.reftypes.HasComponent, o6.ns["ns=pnenc;i=5011"])
pnenc_objtypes.EncoderProbeType(
    nodeId="ns=pnenc;i=5006",
    browseName="ns=pnenc;<Probex>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pnenc;i=6130", browseName="ns=pnenc;LastLatchedPos", dataType=ns0.datatypes.Number))],
)
o6.reference(pnenc_objtypes.EncoderProbesType, ns0.reftypes.HasComponent, o6.ns["ns=pnenc;i=5006"])


ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6010",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pnenc;i=7002", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6010"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6011",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pnenc;i=7003", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6011"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6012",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6013",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pnenc;i=7004", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6012"]), outputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6013"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6018",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pnenc;i=7005", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6018"]))

di.objtypes.LockingServicesType(
    nodeId="ns=pnenc;i=5001",
    browseName="ns=pnenc;Lock",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6014", browseName="ns=di;Locked", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6015", browseName="ns=di;LockingClient", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6016", browseName="ns=di;LockingUser", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6017", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=pnenc;i=7002"]),
        o6.hasComponent(o6.ns["ns=pnenc;i=7003"]),
        o6.hasComponent(o6.ns["ns=pnenc;i=7004"]),
        o6.hasComponent(o6.ns["ns=pnenc;i=7005"]),
    ],
)
o6.reference(pnenc_objtypes.EncoderChannelType, ns0.reftypes.HasComponent, o6.ns["ns=pnenc;i=5001"])


ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6075",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pnenc;i=7014", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6075"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6076",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pnenc;i=7015", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6076"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6077",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6078",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pnenc;i=7016", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6077"]), outputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6078"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6083",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pnenc;i=7017", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6083"]))

di.objtypes.LockingServicesType(
    nodeId="ns=pnenc;i=5005",
    browseName="ns=pnenc;Lock",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6079", browseName="ns=di;Locked", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6080", browseName="ns=di;LockingClient", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6081", browseName="ns=di;LockingUser", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6082", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=pnenc;i=7014"]),
        o6.hasComponent(o6.ns["ns=pnenc;i=7015"]),
        o6.hasComponent(o6.ns["ns=pnenc;i=7016"]),
        o6.hasComponent(o6.ns["ns=pnenc;i=7017"]),
    ],
)
o6.reference(pnenc_objtypes.EncoderProbeType, ns0.reftypes.HasComponent, o6.ns["ns=pnenc;i=5005"])


del Any, TYPE_CHECKING, uuid, o6, di, ns0, pnenc_datypes, pnenc_objtypes
