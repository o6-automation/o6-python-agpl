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

"""Generated OPC UA profinet namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as profinet_reftypes
from . import datatypes as profinet_datypes
from . import objtypes as profinet_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=profinet;i=5001", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=profinet;i=5002", browseName="Default XML")
o6.hasEncoding(profinet_datypes.PnDeviceRoleOptionSet, o6.ns["ns=profinet;i=5002"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=profinet;i=5003", browseName="Default JSON")
o6.hasEncoding(profinet_datypes.PnDeviceRoleOptionSet, o6.ns["ns=profinet;i=5003"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=profinet;i=5004", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=profinet;i=5005", browseName="Default XML")
o6.hasEncoding(profinet_datypes.PnDeviceDiagnosisDataType, o6.ns["ns=profinet;i=5005"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=profinet;i=5006", browseName="Default JSON")
o6.hasEncoding(profinet_datypes.PnDeviceDiagnosisDataType, o6.ns["ns=profinet;i=5006"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=profinet;i=5007", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=profinet;i=5008", browseName="Default XML")
o6.hasEncoding(profinet_datypes.PnIM5DataType, o6.ns["ns=profinet;i=5008"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=profinet;i=5009", browseName="Default JSON")
o6.hasEncoding(profinet_datypes.PnIM5DataType, o6.ns["ns=profinet;i=5009"])
profinet_objtypes.NetworkComponentType(nodeId="ns=profinet;i=5015", browseName="ns=profinet;<ComponentName>", modellingRule="OptionalPlaceholder", _allow_abstract=True)
o6.reference(profinet_objtypes.NetworkComponentType, profinet_reftypes.CommLinkTo, o6.ns["ns=profinet;i=5015"])
profinet_objtypes.EthernetPortType(nodeId="ns=profinet;i=5016", browseName="ns=profinet;<EthernetPort>", modellingRule="Optional")
o6.reference(profinet_objtypes.EthernetPortType, profinet_reftypes.CommLinkTo, o6.ns["ns=profinet;i=5016"])
ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6001",
    browseName="OptionSetValues",
    modellingRule="Mandatory",
    parent="ns=profinet;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[5],
    value=[o6.LocalizedText("IO_DEVICE"), o6.LocalizedText("IO_CONTROLLER"), o6.LocalizedText("IO_MULTIDEVICE"), o6.LocalizedText("IO_SUPERVISOR"), o6.LocalizedText("IO_CIM")],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=profinet;i=6006", browseName="ns=profinet;PnDeviceRoleOptionSet", dataType=o6.String, value="PnDeviceRoleOptionSet")
o6.reference(o6.ns["ns=profinet;i=5001"], "i=39", o6.ns["ns=profinet;i=6006"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=profinet;i=6007", browseName="ns=profinet;PnDeviceRoleOptionSet", dataType=o6.String, value="//xs:element[@name='PnDeviceRoleOptionSet']"
)
o6.reference(o6.ns["ns=profinet;i=5002"], "i=39", o6.ns["ns=profinet;i=6007"])
ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6008",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=profinet;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("OFFLINE"),
            description=o6.LocalizedText(
                "The device is not online, or no information is available. The device is offline if no ARs other than possible Device Access AR&#8217;s exist."
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("OFFLINE_DOCKING"), description=o6.LocalizedText("The device is a docking device and currently not online.")
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("ONLINE"),
            description=o6.LocalizedText("The device is online. This is the case if at least one AR other than possible Device Access AR&#8217;s exists."),
        ),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("ONLINE_DOCKING"), description=o6.LocalizedText("The device is a docking device and currently online.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6009",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=profinet;i=3004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("CONNECTED"), description=o6.LocalizedText("The AR connection to the device is established")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("UNCONNECTED"), description=o6.LocalizedText("The AR connection to the device is not established")),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("UNCONNECTED_ERR_DEVICE_NOT_FOUND"),
            description=o6.LocalizedText("The AR connection to the device is not established because the device is not available in the network"),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("UNCONNECTED_ERR_DUPLICATE_IP"),
            description=o6.LocalizedText("The AR connection to the device is not established because the IP address of the device exists multiple times"),
        ),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("UNCONNECTED_ERR_DUPLICATE_NOS"),
            description=o6.LocalizedText("The AR connection to the device is not established because the Name of Station of the device exists multiple times"),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6010",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=profinet;i=3005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("IOCARSingle")),
        ns0.datatypes.EnumValueType(
            value=6,
            displayName=o6.LocalizedText("IOSAR"),
            description=o6.LocalizedText("The supervisor AR is a special form of the IOCARSingle allowing takeover of the ownership of a submodule"),
        ),
        ns0.datatypes.EnumValueType(
            value=16,
            displayName=o6.LocalizedText("IOCARSingleUsingRT_CLASS_3"),
            description=o6.LocalizedText("This is a special form of the IOCARSingle indicating RT_CLASS_3 communication"),
        ),
        ns0.datatypes.EnumValueType(
            value=32,
            displayName=o6.LocalizedText("IOCARSR"),
            description=o6.LocalizedText("The SR AR is a special form of the IOCARSingle indicating system redundancy or dynamic reconfiguration usage"),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6011",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=profinet;i=3006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("NO_MODULE"), description=o6.LocalizedText("For example module not plugged")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("WRONG_MODULE"), description=o6.LocalizedText("For example ModuleIdentNumber wrong")),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("PROPER_MODULE"), description=o6.LocalizedText("Module is okay but at least one submodule is locked, wrong or missing")
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("SUBSTITUTE"),
            description=o6.LocalizedText("Module is not the same as requested &#8211; but the IO device was able to adapt by its own knowledge"),
        ),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("OK"), description=o6.LocalizedText("Default state")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6012",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=profinet;i=3007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("NO_ADD_INFO")),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("TAKEOVER_NOT_ALLOWED"), description=o6.LocalizedText("This Submodule is not available for takeover by IOSAR.")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6013",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=profinet;i=3008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OWN"), description=o6.LocalizedText("This AR is owner of the submodule")),
        ns0.datatypes.EnumValueType(
            value=128,
            displayName=o6.LocalizedText("APPLICATION_READY_PENDING"),
            description=o6.LocalizedText("This AR is owner of the submodule but it is blocked. For example parameter checking pending"),
        ),
        ns0.datatypes.EnumValueType(
            value=256,
            displayName=o6.LocalizedText("SUPERORDINATED_LOCKED"),
            description=o6.LocalizedText("This AR is not owner of the submodule. It is blocked by superordinated means"),
        ),
        ns0.datatypes.EnumValueType(
            value=384, displayName=o6.LocalizedText("LOCKED_BY_IO_CONTROLLER"), description=o6.LocalizedText("This AR is not owner of the submodule. It is owned by another IOAR")
        ),
        ns0.datatypes.EnumValueType(
            value=512, displayName=o6.LocalizedText("LOCKED_BY_IO_SUPERVISOR"), description=o6.LocalizedText("This AR is not owner of the submodule. It is owned by another IOSAR")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6014",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=profinet;i=3009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OK"), description=o6.LocalizedText("OK")),
        ns0.datatypes.EnumValueType(value=2048, displayName=o6.LocalizedText("SUBSTITUTE"), description=o6.LocalizedText("Substitute (SU)")),
        ns0.datatypes.EnumValueType(value=4096, displayName=o6.LocalizedText("WRONG"), description=o6.LocalizedText("Wrong (WR)")),
        ns0.datatypes.EnumValueType(value=6144, displayName=o6.LocalizedText("NO_SUBMODULE"), description=o6.LocalizedText("NoSubmodule (NO)")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6015",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=profinet;i=3010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("UNSPECIFIC"),
            description=o6.LocalizedText(
                "Shall be used if the field ChannelNumber contains the value 0x8000 (submodule)\nFurthermore, it shall be used if none of the below defined types are appropriate.\n"
            ),
        ),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("1BIT"), description=o6.LocalizedText("The data length of this channel is 1 Bit.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("2BIT"), description=o6.LocalizedText("The data length of this channel is 2 Bit.")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("4BIT"), description=o6.LocalizedText("The data length of this channel is 4 Bit.")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("8BIT"), description=o6.LocalizedText("The data length of this channel is 8 Bit.")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("16BIT"), description=o6.LocalizedText("The data length of this channel is 16 Bit.")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("32BIT"), description=o6.LocalizedText("The data length of this channel is 32 Bit.")),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("64BIT"), description=o6.LocalizedText("The data length of this channel is 64 Bit.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6016",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=profinet;i=3011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("SINGLE"), description=o6.LocalizedText("Single channel \nDiagnosis only for the reported channel\n")),
        ns0.datatypes.EnumValueType(
            value=256, displayName=o6.LocalizedText("ACCUMULATIVE"), description=o6.LocalizedText("Multiple channel \nAccumulative diagnosis from more than one channel\n")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6017",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=profinet;i=3012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("FAULT"), description=o6.LocalizedText("Fault")),
        ns0.datatypes.EnumValueType(value=512, displayName=o6.LocalizedText("MAINTENANCE_REQUIRED"), description=o6.LocalizedText("Maintenance required")),
        ns0.datatypes.EnumValueType(value=1024, displayName=o6.LocalizedText("MAINTENANCE_DEMANDED"), description=o6.LocalizedText("Maintenance demanded")),
        ns0.datatypes.EnumValueType(
            value=1536, displayName=o6.LocalizedText("USE_QUALIFIED_CHANNEL_QUALIFIER"), description=o6.LocalizedText("Use QualifiedChannelQualifier variable")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6018",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=profinet;i=3013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("ALL_DISAPPEARS"),
            description=o6.LocalizedText("The Diagnosis ASE contains no longer any entries (of any severity) for this channel"),
        ),
        ns0.datatypes.EnumValueType(
            value=2048,
            displayName=o6.LocalizedText("APPEARS"),
            description=o6.LocalizedText("An event appears and/or exists further\nThe Diagnosis ASE contains this and possible other entries for this channel.\n"),
        ),
        ns0.datatypes.EnumValueType(
            value=4096,
            displayName=o6.LocalizedText("DISAPPEARS"),
            description=o6.LocalizedText("An event disappears and/or exists no longer\nThe Diagnosis ASE contains no longer any entries of the same severity for this channel\n"),
        ),
        ns0.datatypes.EnumValueType(
            value=6144,
            displayName=o6.LocalizedText("DISAPPEARS_OTHER_REMAIN"),
            description=o6.LocalizedText("An event disappears\nThe Diagnosis ASE still contains other entries of the same severity for this channel\n"),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6019",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=profinet;i=3014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("MANUFACTURER_SPECIFIC"), description=o6.LocalizedText("Manufacturer specific")),
        ns0.datatypes.EnumValueType(value=8192, displayName=o6.LocalizedText("INPUT_CHANNEL"), description=o6.LocalizedText("Input")),
        ns0.datatypes.EnumValueType(value=16384, displayName=o6.LocalizedText("OUTPUT_CHANNEL"), description=o6.LocalizedText("Output")),
        ns0.datatypes.EnumValueType(value=24576, displayName=o6.LocalizedText("BIDIRECTIONAL_CHANNEL"), description=o6.LocalizedText("Input/Output")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6020",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=profinet;i=3015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("DEVICE"), description=o6.LocalizedText("Device")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("MODULE"), description=o6.LocalizedText("Real Module")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("SUBMODULE"), description=o6.LocalizedText("Real Submodule")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("ASSET"), description=o6.LocalizedText("Asset")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6021",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=profinet;i=3016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("INSERTED"), description=o6.LocalizedText("Asset has been added")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("REMOVED"), description=o6.LocalizedText("Asset has been removed")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("CHANGED"), description=o6.LocalizedText("Asset has been changed")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6022",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=profinet;i=3017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("UP"), description=o6.LocalizedText("Ready to pass packets")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("DOWN"), description=o6.LocalizedText("No packets are passed")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("TESTING"), description=o6.LocalizedText("In some test mode")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("UNKNOWN"), description=o6.LocalizedText("Status cannot be determined")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("DORMANT"), description=o6.LocalizedText("In pending state waiting  for some external event")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("NOT_PRESENT"), description=o6.LocalizedText("Port not present")),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("LOWER_LAYER_DOWN"), description=o6.LocalizedText("Down due to lower layer")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6023",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=profinet;i=3018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("UNKNOWN"), description=o6.LocalizedText("Status cannot be determined")),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("DISABLED_DISCARDING"), description=o6.LocalizedText("The port is administratively disabled and discarding frames")
        ),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("BLOCKING"), description=o6.LocalizedText("The port blocks incoming frames")),
        ns0.datatypes.EnumValueType(
            value=3, displayName=o6.LocalizedText("LISTENING"), description=o6.LocalizedText("The port is listening to and sending BPDUs (Bridge Protocol Data Units).")
        ),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("LEARNING")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("FORWARDING")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("BROKEN")),
    ],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=profinet;i=6042", browseName="ns=profinet;PnDeviceDiagnosisDataType", dataType=o6.String, value="PnDeviceDiagnosisDataType")
o6.reference(o6.ns["ns=profinet;i=5004"], "i=39", o6.ns["ns=profinet;i=6042"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=profinet;i=6043", browseName="ns=profinet;PnDeviceDiagnosisDataType", dataType=o6.String, value="//xs:element[@name='PnDeviceDiagnosisDataType']"
)
o6.reference(o6.ns["ns=profinet;i=5005"], "i=39", o6.ns["ns=profinet;i=6043"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=profinet;i=6044", browseName="ns=profinet;PnIM5DataType", dataType=o6.String, value="PnIM5DataType")
o6.reference(o6.ns["ns=profinet;i=5007"], "i=39", o6.ns["ns=profinet;i=6044"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=profinet;i=6002",
    browseName="ns=profinet;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PROFINET/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6003", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PROFINET/")),
        o6.hasComponent(o6.ns["ns=profinet;i=6006"]),
        o6.hasComponent(o6.ns["ns=profinet;i=6042"]),
        o6.hasComponent(o6.ns["ns=profinet;i=6044"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/PROFINET/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/PROFINET/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:OptionSet" Name="PnDeviceRoleOptionSet">\n  <opc:Field TypeName="opc:ByteString" Name="Value"/>\n  <opc:Field TypeName="opc:ByteString" Name="ValidBits"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="PnDeviceDiagnosisDataType">\n  <opc:Field TypeName="opc:UInt32" Name="API"/>\n  <opc:Field TypeName="opc:UInt16" Name="Slot"/>\n  <opc:Field TypeName="opc:UInt16" Name="Subslot"/>\n  <opc:Field TypeName="opc:UInt16" Name="ChannelNumber"/>\n  <opc:Field TypeName="tns:PnChannelTypeEnumeration" Name="Type"/>\n  <opc:Field TypeName="tns:PnChannelAccumulativeEnumeration" Name="Accumulative"/>\n  <opc:Field TypeName="tns:PnChannelMaintenanceEnumeration" Name="Maintenance"/>\n  <opc:Field TypeName="tns:PnChannelSpecifierEnumeration" Name="Specifier"/>\n  <opc:Field TypeName="tns:PnChannelDirectionEnumeration" Name="Direction"/>\n  <opc:Field TypeName="opc:UInt16" Name="UserStructureIdentifier"/>\n  <opc:Field TypeName="opc:UInt16" Name="ChannelErrorType"/>\n  <opc:Field TypeName="opc:UInt16" Name="ExtChannelErrorType"/>\n  <opc:Field TypeName="opc:UInt32" Name="ExtChannelAddValue"/>\n  <opc:Field TypeName="opc:UInt32" Name="QualifiedChannelQualifier"/>\n  <opc:Field TypeName="opc:ByteString" Name="ManufacturerData"/>\n  <opc:Field TypeName="ua:LocalizedText" Name="Message"/>\n  <opc:Field TypeName="ua:LocalizedText" Name="HelpText"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="PnIM5DataType">\n  <opc:Documentation>Contains the fields of the APDU element I&amp;M5 | I&amp;M5Data</opc:Documentation>\n  <opc:Field TypeName="opc:CharArray" Name="Annotation"/>\n  <opc:Field TypeName="opc:CharArray" Name="OrderId"/>\n  <opc:Field TypeName="opc:UInt16" Name="VendorId"/>\n  <opc:Field TypeName="opc:CharArray" Name="SerialNumber"/>\n  <opc:Field TypeName="opc:CharArray" Name="HardwareRevision"/>\n  <opc:Field TypeName="opc:CharArray" Name="SoftwareRevision"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="IMTagSelectorEnumeration">\n  <opc:EnumeratedValue Name="FUNCTION" Value="0"/>\n  <opc:EnumeratedValue Name="LOCATION" Value="1"/>\n  <opc:EnumeratedValue Name="BOTH" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PnARStateEnumeration">\n  <opc:EnumeratedValue Name="CONNECTED" Value="0"/>\n  <opc:EnumeratedValue Name="UNCONNECTED" Value="1"/>\n  <opc:EnumeratedValue Name="UNCONNECTED_ERR_DEVICE_NOT_FOUND" Value="2"/>\n  <opc:EnumeratedValue Name="UNCONNECTED_ERR_DUPLICATE_IP" Value="3"/>\n  <opc:EnumeratedValue Name="UNCONNECTED_ERR_DUPLICATE_NOS" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PnARTypeEnumeration">\n  <opc:EnumeratedValue Name="IOCARSingle" Value="0"/>\n  <opc:EnumeratedValue Name="IOSAR" Value="6"/>\n  <opc:EnumeratedValue Name="IOCARSingleUsingRT_CLASS_3" Value="16"/>\n  <opc:EnumeratedValue Name="IOCARSR" Value="32"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PnAssetChangeEnumeration">\n  <opc:EnumeratedValue Name="INSERTED" Value="0"/>\n  <opc:EnumeratedValue Name="REMOVED" Value="1"/>\n  <opc:EnumeratedValue Name="CHANGED" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PnAssetTypeEnumeration">\n  <opc:EnumeratedValue Name="DEVICE" Value="0"/>\n  <opc:EnumeratedValue Name="MODULE" Value="1"/>\n  <opc:EnumeratedValue Name="SUBMODULE" Value="2"/>\n  <opc:EnumeratedValue Name="ASSET" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PnChannelAccumulativeEnumeration">\n  <opc:EnumeratedValue Name="SINGLE" Value="0"/>\n  <opc:EnumeratedValue Name="ACCUMULATIVE" Value="256"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PnChannelDirectionEnumeration">\n  <opc:EnumeratedValue Name="MANUFACTURER_SPECIFIC" Value="0"/>\n  <opc:EnumeratedValue Name="INPUT_CHANNEL" Value="8192"/>\n  <opc:EnumeratedValue Name="OUTPUT_CHANNEL" Value="16384"/>\n  <opc:EnumeratedValue Name="BIDIRECTIONAL_CHANNEL" Value="24576"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PnChannelMaintenanceEnumeration">\n  <opc:EnumeratedValue Name="FAULT" Value="0"/>\n  <opc:EnumeratedValue Name="MAINTENANCE_REQUIRED" Value="512"/>\n  <opc:EnumeratedValue Name="MAINTENANCE_DEMANDED" Value="1024"/>\n  <opc:EnumeratedValue Name="USE_QUALIFIED_CHANNEL_QUALIFIER" Value="1536"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PnChannelSpecifierEnumeration">\n  <opc:EnumeratedValue Name="ALL_DISAPPEARS" Value="0"/>\n  <opc:EnumeratedValue Name="APPEARS" Value="2048"/>\n  <opc:EnumeratedValue Name="DISAPPEARS" Value="4096"/>\n  <opc:EnumeratedValue Name="DISAPPEARS_OTHER_REMAIN" Value="6144"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PnChannelTypeEnumeration">\n  <opc:EnumeratedValue Name="UNSPECIFIC" Value="0"/>\n  <opc:EnumeratedValue Name="1BIT" Value="1"/>\n  <opc:EnumeratedValue Name="2BIT" Value="2"/>\n  <opc:EnumeratedValue Name="4BIT" Value="3"/>\n  <opc:EnumeratedValue Name="8BIT" Value="4"/>\n  <opc:EnumeratedValue Name="16BIT" Value="5"/>\n  <opc:EnumeratedValue Name="32BIT" Value="6"/>\n  <opc:EnumeratedValue Name="64BIT" Value="7"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PnDeviceStateEnumeration">\n  <opc:EnumeratedValue Name="OFFLINE" Value="0"/>\n  <opc:EnumeratedValue Name="OFFLINE_DOCKING" Value="1"/>\n  <opc:EnumeratedValue Name="ONLINE" Value="2"/>\n  <opc:EnumeratedValue Name="ONLINE_DOCKING" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PnLinkStateEnumeration">\n  <opc:EnumeratedValue Name="UP" Value="1"/>\n  <opc:EnumeratedValue Name="DOWN" Value="2"/>\n  <opc:EnumeratedValue Name="TESTING" Value="3"/>\n  <opc:EnumeratedValue Name="UNKNOWN" Value="4"/>\n  <opc:EnumeratedValue Name="DORMANT" Value="5"/>\n  <opc:EnumeratedValue Name="NOT_PRESENT" Value="6"/>\n  <opc:EnumeratedValue Name="LOWER_LAYER_DOWN" Value="7"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PnModuleStateEnumeration">\n  <opc:EnumeratedValue Name="NO_MODULE" Value="0"/>\n  <opc:EnumeratedValue Name="WRONG_MODULE" Value="1"/>\n  <opc:EnumeratedValue Name="PROPER_MODULE" Value="2"/>\n  <opc:EnumeratedValue Name="SUBSTITUTE" Value="3"/>\n  <opc:EnumeratedValue Name="OK" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PnPortStateEnumeration">\n  <opc:EnumeratedValue Name="UNKNOWN" Value="0"/>\n  <opc:EnumeratedValue Name="DISABLED_DISCARDING" Value="1"/>\n  <opc:EnumeratedValue Name="BLOCKING" Value="2"/>\n  <opc:EnumeratedValue Name="LISTENING" Value="3"/>\n  <opc:EnumeratedValue Name="LEARNING" Value="4"/>\n  <opc:EnumeratedValue Name="FORWARDING" Value="5"/>\n  <opc:EnumeratedValue Name="BROKEN" Value="6"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PnSubmoduleAddInfoEnumeration">\n  <opc:EnumeratedValue Name="NO_ADD_INFO" Value="0"/>\n  <opc:EnumeratedValue Name="TAKEOVER_NOT_ALLOWED" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PnSubmoduleARInfoEnumeration">\n  <opc:EnumeratedValue Name="OWN" Value="0"/>\n  <opc:EnumeratedValue Name="APPLICATION_READY_PENDING" Value="128"/>\n  <opc:EnumeratedValue Name="SUPERORDINATED_LOCKED" Value="256"/>\n  <opc:EnumeratedValue Name="LOCKED_BY_IO_CONTROLLER" Value="384"/>\n  <opc:EnumeratedValue Name="LOCKED_BY_IO_SUPERVISOR" Value="512"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PnSubmoduleIdentInfoEnumeration">\n  <opc:EnumeratedValue Name="OK" Value="0"/>\n  <opc:EnumeratedValue Name="SUBSTITUTE" Value="2048"/>\n  <opc:EnumeratedValue Name="WRONG" Value="4096"/>\n  <opc:EnumeratedValue Name="NO_SUBMODULE" Value="6144"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=profinet;i=6045", browseName="ns=profinet;PnIM5DataType", dataType=o6.String, value="//xs:element[@name='PnIM5DataType']")
o6.reference(o6.ns["ns=profinet;i=5008"], "i=39", o6.ns["ns=profinet;i=6045"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=profinet;i=6004",
    browseName="ns=profinet;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PROFINET/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6005", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PROFINET/Types.xsd")
        ),
        o6.hasComponent(o6.ns["ns=profinet;i=6007"]),
        o6.hasComponent(o6.ns["ns=profinet;i=6043"]),
        o6.hasComponent(o6.ns["ns=profinet;i=6045"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/PROFINET/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/PROFINET/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="IMTagSelectorEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="FUNCTION_0"/>\n   <xs:enumeration value="LOCATION_1"/>\n   <xs:enumeration value="BOTH_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:IMTagSelectorEnumeration" name="IMTagSelectorEnumeration"/>\n <xs:complexType name="ListOfIMTagSelectorEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:IMTagSelectorEnumeration" name="IMTagSelectorEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfIMTagSelectorEnumeration" name="ListOfIMTagSelectorEnumeration" nillable="true"/>\n <xs:simpleType name="PnARStateEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="CONNECTED_0"/>\n   <xs:enumeration value="UNCONNECTED_1"/>\n   <xs:enumeration value="UNCONNECTED_ERR_DEVICE_NOT_FOUND_2"/>\n   <xs:enumeration value="UNCONNECTED_ERR_DUPLICATE_IP_3"/>\n   <xs:enumeration value="UNCONNECTED_ERR_DUPLICATE_NOS_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PnARStateEnumeration" name="PnARStateEnumeration"/>\n <xs:complexType name="ListOfPnARStateEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PnARStateEnumeration" name="PnARStateEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPnARStateEnumeration" name="ListOfPnARStateEnumeration" nillable="true"/>\n <xs:simpleType name="PnARTypeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="IOCARSingle_0"/>\n   <xs:enumeration value="IOSAR_6"/>\n   <xs:enumeration value="IOCARSingleUsingRT_CLASS_3_16"/>\n   <xs:enumeration value="IOCARSR_32"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PnARTypeEnumeration" name="PnARTypeEnumeration"/>\n <xs:complexType name="ListOfPnARTypeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PnARTypeEnumeration" name="PnARTypeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPnARTypeEnumeration" name="ListOfPnARTypeEnumeration" nillable="true"/>\n <xs:simpleType name="PnAssetChangeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="INSERTED_0"/>\n   <xs:enumeration value="REMOVED_1"/>\n   <xs:enumeration value="CHANGED_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PnAssetChangeEnumeration" name="PnAssetChangeEnumeration"/>\n <xs:complexType name="ListOfPnAssetChangeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PnAssetChangeEnumeration" name="PnAssetChangeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPnAssetChangeEnumeration" name="ListOfPnAssetChangeEnumeration" nillable="true"/>\n <xs:simpleType name="PnAssetTypeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="DEVICE_0"/>\n   <xs:enumeration value="MODULE_1"/>\n   <xs:enumeration value="SUBMODULE_2"/>\n   <xs:enumeration value="ASSET_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PnAssetTypeEnumeration" name="PnAssetTypeEnumeration"/>\n <xs:complexType name="ListOfPnAssetTypeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PnAssetTypeEnumeration" name="PnAssetTypeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPnAssetTypeEnumeration" name="ListOfPnAssetTypeEnumeration" nillable="true"/>\n <xs:simpleType name="PnChannelAccumulativeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="SINGLE_0"/>\n   <xs:enumeration value="ACCUMULATIVE_256"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PnChannelAccumulativeEnumeration" name="PnChannelAccumulativeEnumeration"/>\n <xs:complexType name="ListOfPnChannelAccumulativeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PnChannelAccumulativeEnumeration" name="PnChannelAccumulativeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPnChannelAccumulativeEnumeration" name="ListOfPnChannelAccumulativeEnumeration" nillable="true"/>\n <xs:simpleType name="PnChannelDirectionEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="MANUFACTURER_SPECIFIC_0"/>\n   <xs:enumeration value="INPUT_CHANNEL_8192"/>\n   <xs:enumeration value="OUTPUT_CHANNEL_16384"/>\n   <xs:enumeration value="BIDIRECTIONAL_CHANNEL_24576"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PnChannelDirectionEnumeration" name="PnChannelDirectionEnumeration"/>\n <xs:complexType name="ListOfPnChannelDirectionEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PnChannelDirectionEnumeration" name="PnChannelDirectionEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPnChannelDirectionEnumeration" name="ListOfPnChannelDirectionEnumeration" nillable="true"/>\n <xs:simpleType name="PnChannelMaintenanceEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="FAULT_0"/>\n   <xs:enumeration value="MAINTENANCE_REQUIRED_512"/>\n   <xs:enumeration value="MAINTENANCE_DEMANDED_1024"/>\n   <xs:enumeration value="USE_QUALIFIED_CHANNEL_QUALIFIER_1536"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PnChannelMaintenanceEnumeration" name="PnChannelMaintenanceEnumeration"/>\n <xs:complexType name="ListOfPnChannelMaintenanceEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PnChannelMaintenanceEnumeration" name="PnChannelMaintenanceEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPnChannelMaintenanceEnumeration" name="ListOfPnChannelMaintenanceEnumeration" nillable="true"/>\n <xs:simpleType name="PnChannelSpecifierEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="ALL_DISAPPEARS_0"/>\n   <xs:enumeration value="APPEARS_2048"/>\n   <xs:enumeration value="DISAPPEARS_4096"/>\n   <xs:enumeration value="DISAPPEARS_OTHER_REMAIN_6144"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PnChannelSpecifierEnumeration" name="PnChannelSpecifierEnumeration"/>\n <xs:complexType name="ListOfPnChannelSpecifierEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PnChannelSpecifierEnumeration" name="PnChannelSpecifierEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPnChannelSpecifierEnumeration" name="ListOfPnChannelSpecifierEnumeration" nillable="true"/>\n <xs:simpleType name="PnChannelTypeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="UNSPECIFIC_0"/>\n   <xs:enumeration value="1BIT_1"/>\n   <xs:enumeration value="2BIT_2"/>\n   <xs:enumeration value="4BIT_3"/>\n   <xs:enumeration value="8BIT_4"/>\n   <xs:enumeration value="16BIT_5"/>\n   <xs:enumeration value="32BIT_6"/>\n   <xs:enumeration value="64BIT_7"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PnChannelTypeEnumeration" name="PnChannelTypeEnumeration"/>\n <xs:complexType name="ListOfPnChannelTypeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PnChannelTypeEnumeration" name="PnChannelTypeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPnChannelTypeEnumeration" name="ListOfPnChannelTypeEnumeration" nillable="true"/>\n <xs:simpleType name="PnDeviceStateEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OFFLINE_0"/>\n   <xs:enumeration value="OFFLINE_DOCKING_1"/>\n   <xs:enumeration value="ONLINE_2"/>\n   <xs:enumeration value="ONLINE_DOCKING_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PnDeviceStateEnumeration" name="PnDeviceStateEnumeration"/>\n <xs:complexType name="ListOfPnDeviceStateEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PnDeviceStateEnumeration" name="PnDeviceStateEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPnDeviceStateEnumeration" name="ListOfPnDeviceStateEnumeration" nillable="true"/>\n <xs:simpleType name="PnLinkStateEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="UP_1"/>\n   <xs:enumeration value="DOWN_2"/>\n   <xs:enumeration value="TESTING_3"/>\n   <xs:enumeration value="UNKNOWN_4"/>\n   <xs:enumeration value="DORMANT_5"/>\n   <xs:enumeration value="NOT_PRESENT_6"/>\n   <xs:enumeration value="LOWER_LAYER_DOWN_7"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PnLinkStateEnumeration" name="PnLinkStateEnumeration"/>\n <xs:complexType name="ListOfPnLinkStateEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PnLinkStateEnumeration" name="PnLinkStateEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPnLinkStateEnumeration" name="ListOfPnLinkStateEnumeration" nillable="true"/>\n <xs:simpleType name="PnModuleStateEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="NO_MODULE_0"/>\n   <xs:enumeration value="WRONG_MODULE_1"/>\n   <xs:enumeration value="PROPER_MODULE_2"/>\n   <xs:enumeration value="SUBSTITUTE_3"/>\n   <xs:enumeration value="OK_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PnModuleStateEnumeration" name="PnModuleStateEnumeration"/>\n <xs:complexType name="ListOfPnModuleStateEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PnModuleStateEnumeration" name="PnModuleStateEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPnModuleStateEnumeration" name="ListOfPnModuleStateEnumeration" nillable="true"/>\n <xs:simpleType name="PnPortStateEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="UNKNOWN_0"/>\n   <xs:enumeration value="DISABLED_DISCARDING_1"/>\n   <xs:enumeration value="BLOCKING_2"/>\n   <xs:enumeration value="LISTENING_3"/>\n   <xs:enumeration value="LEARNING_4"/>\n   <xs:enumeration value="FORWARDING_5"/>\n   <xs:enumeration value="BROKEN_6"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PnPortStateEnumeration" name="PnPortStateEnumeration"/>\n <xs:complexType name="ListOfPnPortStateEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PnPortStateEnumeration" name="PnPortStateEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPnPortStateEnumeration" name="ListOfPnPortStateEnumeration" nillable="true"/>\n <xs:simpleType name="PnSubmoduleAddInfoEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="NO_ADD_INFO_0"/>\n   <xs:enumeration value="TAKEOVER_NOT_ALLOWED_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PnSubmoduleAddInfoEnumeration" name="PnSubmoduleAddInfoEnumeration"/>\n <xs:complexType name="ListOfPnSubmoduleAddInfoEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PnSubmoduleAddInfoEnumeration" name="PnSubmoduleAddInfoEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPnSubmoduleAddInfoEnumeration" name="ListOfPnSubmoduleAddInfoEnumeration" nillable="true"/>\n <xs:simpleType name="PnSubmoduleARInfoEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OWN_0"/>\n   <xs:enumeration value="APPLICATION_READY_PENDING_128"/>\n   <xs:enumeration value="SUPERORDINATED_LOCKED_256"/>\n   <xs:enumeration value="LOCKED_BY_IO_CONTROLLER_384"/>\n   <xs:enumeration value="LOCKED_BY_IO_SUPERVISOR_512"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PnSubmoduleARInfoEnumeration" name="PnSubmoduleARInfoEnumeration"/>\n <xs:complexType name="ListOfPnSubmoduleARInfoEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PnSubmoduleARInfoEnumeration" name="PnSubmoduleARInfoEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPnSubmoduleARInfoEnumeration" name="ListOfPnSubmoduleARInfoEnumeration" nillable="true"/>\n <xs:simpleType name="PnSubmoduleIdentInfoEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OK_0"/>\n   <xs:enumeration value="SUBSTITUTE_2048"/>\n   <xs:enumeration value="WRONG_4096"/>\n   <xs:enumeration value="NO_SUBMODULE_6144"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PnSubmoduleIdentInfoEnumeration" name="PnSubmoduleIdentInfoEnumeration"/>\n <xs:complexType name="ListOfPnSubmoduleIdentInfoEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PnSubmoduleIdentInfoEnumeration" name="PnSubmoduleIdentInfoEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPnSubmoduleIdentInfoEnumeration" name="ListOfPnSubmoduleIdentInfoEnumeration" nillable="true"/>\n <xs:complexType name="PnDeviceRoleOptionSet">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:OptionSet">\n    <xs:sequence/>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:PnDeviceRoleOptionSet" name="PnDeviceRoleOptionSet"/>\n <xs:complexType name="ListOfPnDeviceRoleOptionSet">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PnDeviceRoleOptionSet" name="PnDeviceRoleOptionSet" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPnDeviceRoleOptionSet" name="ListOfPnDeviceRoleOptionSet" nillable="true"/>\n <xs:complexType name="PnDeviceDiagnosisDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="API"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedShort" name="Slot"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedShort" name="Subslot"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedShort" name="ChannelNumber"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:PnChannelTypeEnumeration" name="Type"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:PnChannelAccumulativeEnumeration" name="Accumulative"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:PnChannelMaintenanceEnumeration" name="Maintenance"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:PnChannelSpecifierEnumeration" name="Specifier"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:PnChannelDirectionEnumeration" name="Direction"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedShort" name="UserStructureIdentifier"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedShort" name="ChannelErrorType"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedShort" name="ExtChannelErrorType"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="ExtChannelAddValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="QualifiedChannelQualifier"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:base64Binary" name="ManufacturerData"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="Message"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="HelpText"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:PnDeviceDiagnosisDataType" name="PnDeviceDiagnosisDataType"/>\n <xs:complexType name="ListOfPnDeviceDiagnosisDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PnDeviceDiagnosisDataType" name="PnDeviceDiagnosisDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPnDeviceDiagnosisDataType" name="ListOfPnDeviceDiagnosisDataType" nillable="true"/>\n <xs:complexType name="PnIM5DataType">\n  <xs:annotation>\n   <xs:documentation>Contains the fields of the APDU element I&amp;M5 | I&amp;M5Data</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Annotation"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="OrderId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedShort" name="VendorId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="SerialNumber"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="HardwareRevision"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="SoftwareRevision"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:PnIM5DataType" name="PnIM5DataType"/>\n <xs:complexType name="ListOfPnIM5DataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PnIM5DataType" name="PnIM5DataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPnIM5DataType" name="ListOfPnIM5DataType" nillable="true"/>\n</xs:schema>\n',
)
profinet_objtypes.PnAssetType(
    nodeId="ns=profinet;i=5010",
    browseName="ns=profinet;<Assets>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6077", browseName="ns=profinet;Annotation", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6078", browseName="ns=profinet;DeviceId", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6079", browseName="ns=profinet;DeviceSubId", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6080", browseName="ns=profinet;Location", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6081", browseName="ns=profinet;OrderId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6082", browseName="ns=profinet;Organization", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6083", browseName="ns=profinet;SerialNumber", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6084", browseName="ns=profinet;TypeIdentification", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6085", browseName="ns=profinet;UniqueIdentifier", dataType=o6.Guid)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6086", browseName="ns=profinet;VendorId", dataType=o6.UInt16)),
    ],
)
o6.reference(profinet_objtypes.PnAssetContainerType, profinet_reftypes.HasPnAsset, o6.ns["ns=profinet;i=5010"])
profinet_objtypes.EthernetInterfaceType(
    nodeId="ns=profinet;i=5011",
    browseName="ns=profinet;EthernetInterface",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6115", browseName="ns=profinet;MacAddress", dataType=o6.Byte, valueRank=1, arrayDimensions=[6]))
    ],
)
o6.reference(profinet_objtypes.IPnInterfaceType, profinet_reftypes.CommLinkTo, o6.ns["ns=profinet;i=5011"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPROFINETSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=profinet;i=5022",
    browseName="ns=profinet;http://opcfoundation.org/UA/PROFINET/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6116", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6117", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2021-04-13T00:00:00Z"))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6118", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PROFINET/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6119", browseName="NamespaceVersion", dataType=o6.String, value="1.0.1")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=profinet;i=6120", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=profinet;i=6121", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["1:2147483647"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6122", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
profinet_objtypes.PnIdentificationType(
    nodeId="ns=profinet;i=5023",
    browseName="ns=profinet;IM",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6135", browseName="ns=profinet;HardwareRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6136", browseName="ns=profinet;OrderId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6137", browseName="ns=profinet;ProfileId", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6138", browseName="ns=profinet;ProfileSpecificType", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6139", browseName="ns=profinet;SerialNumber", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6140", browseName="ns=profinet;SoftwareRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6141", browseName="ns=profinet;VendorId", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6142", browseName="ns=profinet;Version", dataType=o6.String)),
    ],
)
o6.reference(profinet_objtypes.IPnRealSubmoduleType, ns0.reftypes.HasComponent, o6.ns["ns=profinet;i=5023"])
profinet_objtypes.PnIdentificationType(
    nodeId="ns=profinet;i=5029",
    browseName="ns=profinet;IM",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6148", browseName="ns=profinet;HardwareRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6149", browseName="ns=profinet;OrderId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6150", browseName="ns=profinet;ProfileId", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6151", browseName="ns=profinet;ProfileSpecificType", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6152", browseName="ns=profinet;SerialNumber", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6153", browseName="ns=profinet;SoftwareRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6154", browseName="ns=profinet;VendorId", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6155", browseName="ns=profinet;Version", dataType=o6.String)),
    ],
)
o6.reference(profinet_objtypes.IPnRealModuleType, ns0.reftypes.HasComponent, o6.ns["ns=profinet;i=5029"])
profinet_objtypes.PnApplicationRelationType(
    nodeId="ns=profinet;i=5035",
    browseName="ns=profinet;<ARs>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6164", browseName="ns=profinet;Id", dataType=o6.Guid)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6166", browseName="ns=profinet;Type", dataType=profinet_datypes.PnARTypeEnumeration)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=profinet;i=6165", browseName="ns=profinet;State", dataType=profinet_datypes.PnARStateEnumeration, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
)
o6.reference(profinet_objtypes.PnApplicationRelationContainerType, profinet_reftypes.HasPnApplicationRelation, o6.ns["ns=profinet;i=5035"])
profinet_objtypes.PnIdentificationType(
    nodeId="ns=profinet;i=5040",
    browseName="ns=profinet;IM",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6167", browseName="ns=profinet;HardwareRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6168", browseName="ns=profinet;OrderId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6169", browseName="ns=profinet;ProfileId", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6170", browseName="ns=profinet;ProfileSpecificType", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6171", browseName="ns=profinet;SerialNumber", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6172", browseName="ns=profinet;SoftwareRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6173", browseName="ns=profinet;VendorId", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6174", browseName="ns=profinet;Version", dataType=o6.String)),
    ],
)
o6.reference(profinet_objtypes.IPnEquipmentType, ns0.reftypes.HasComponent, o6.ns["ns=profinet;i=5040"])
ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6194",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=profinet;i=3021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("FUNCTION"), o6.LocalizedText("LOCATION"), o6.LocalizedText("BOTH")],
)
profinet_objtypes.PnIdentificationType(
    nodeId="ns=profinet;i=5048",
    browseName="ns=profinet;IM",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6195", browseName="ns=profinet;HardwareRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6196", browseName="ns=profinet;OrderId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6197", browseName="ns=profinet;ProfileId", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6198", browseName="ns=profinet;ProfileSpecificType", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6199", browseName="ns=profinet;SerialNumber", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6200", browseName="ns=profinet;SoftwareRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6201", browseName="ns=profinet;VendorId", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6202", browseName="ns=profinet;Version", dataType=o6.String)),
    ],
)
profinet_objtypes.PnIdentificationType(
    nodeId="ns=profinet;i=5051",
    browseName="ns=profinet;IM",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6207", browseName="ns=profinet;HardwareRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6208", browseName="ns=profinet;OrderId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6209", browseName="ns=profinet;ProfileId", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6210", browseName="ns=profinet;ProfileSpecificType", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6211", browseName="ns=profinet;SerialNumber", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6212", browseName="ns=profinet;SoftwareRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6213", browseName="ns=profinet;VendorId", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6214", browseName="ns=profinet;Version", dataType=o6.String)),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=profinet;i=5031",
    browseName="ns=profinet;<Modules>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6098", browseName="ns=profinet;Slot", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6180", browseName="ns=profinet;IdentNumber", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6205", browseName="ns=profinet;GSDName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6206", browseName="ns=profinet;GSDDescription", dataType=o6.String)),
        o6.hasComponent(profinet_objtypes.PnRealSubmoduleContainerType(nodeId="ns=profinet;i=5050", browseName="ns=profinet;Submodules")),
        o6.hasComponent(o6.ns["ns=profinet;i=5051"]),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=profinet;i=5052", browseName="ns=profinet;Alarms")),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=profinet;i=6215", browseName="ns=profinet;Diagnosis", dataType=profinet_datypes.PnDeviceDiagnosisDataType, valueRank=1, arrayDimensions=[0]
            )
        ),
    ],
)
o6.reference(profinet_objtypes.PnRealModuleContainerType, profinet_reftypes.HasPnRealModule, o6.ns["ns=profinet;i=5031"])
o6.reference(o6.ns["ns=profinet;i=5031"], "i=41", profinet_objtypes.PnDiagnosisAlarmType)
o6.reference(o6.ns["ns=profinet;i=5031"], "i=41", profinet_objtypes.PnAssetChangedEventType)
o6.reference(o6.ns["ns=profinet;i=5031"], "i=17603", profinet_objtypes.IPnRealModuleType)
ns0.objtypes.BaseObjectType(
    nodeId="ns=profinet;i=5033",
    browseName="ns=profinet;<Modules>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6181", browseName="ns=profinet;Slot", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6182", browseName="ns=profinet;IdentNumber", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6216", browseName="ns=profinet;GSDName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6217", browseName="ns=profinet;GSDDescription", dataType=o6.String)),
        o6.hasComponent(profinet_objtypes.PnExpectedSubmoduleContainerType(nodeId="ns=profinet;i=5053", browseName="ns=profinet;Submodules")),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6183", browseName="ns=profinet;State", dataType=profinet_datypes.PnModuleStateEnumeration)),
    ],
)
o6.reference(profinet_objtypes.PnExpectedModuleContainerType, profinet_reftypes.HasPnExpectedModule, o6.ns["ns=profinet;i=5033"])
o6.reference(o6.ns["ns=profinet;i=5033"], "i=17603", profinet_objtypes.IPnExpectedModuleType)
profinet_objtypes.PnIdentificationType(
    nodeId="ns=profinet;i=5054",
    browseName="ns=profinet;IM",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6220", browseName="ns=profinet;HardwareRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6221", browseName="ns=profinet;OrderId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6222", browseName="ns=profinet;ProfileId", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6223", browseName="ns=profinet;ProfileSpecificType", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6224", browseName="ns=profinet;SerialNumber", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6225", browseName="ns=profinet;SoftwareRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6226", browseName="ns=profinet;VendorId", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6227", browseName="ns=profinet;Version", dataType=o6.String)),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=profinet;i=5025",
    browseName="ns=profinet;<Submodules>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6184", browseName="ns=profinet;API", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6185", browseName="ns=profinet;Subslot", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6186", browseName="ns=profinet;IdentNumber", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6218", browseName="ns=profinet;GSDName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6219", browseName="ns=profinet;GSDDescription", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=profinet;i=5054"]),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=profinet;i=5055", browseName="ns=profinet;Alarms")),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=profinet;i=6228", browseName="ns=profinet;Diagnosis", dataType=profinet_datypes.PnDeviceDiagnosisDataType, valueRank=1, arrayDimensions=[0]
            )
        ),
    ],
)
o6.reference(profinet_objtypes.PnRealSubmoduleContainerType, profinet_reftypes.HasPnRealSubmodule, o6.ns["ns=profinet;i=5025"])
o6.reference(o6.ns["ns=profinet;i=5025"], "i=41", profinet_objtypes.PnDiagnosisAlarmType)
o6.reference(o6.ns["ns=profinet;i=5025"], "i=41", profinet_objtypes.PnAssetChangedEventType)
o6.reference(o6.ns["ns=profinet;i=5025"], "i=17603", profinet_objtypes.IPnRealSubmoduleType)
ns0.objtypes.BaseObjectType(
    nodeId="ns=profinet;i=5027",
    browseName="ns=profinet;<Submodules>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6187", browseName="ns=profinet;API", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6188", browseName="ns=profinet;Subslot", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6189", browseName="ns=profinet;IdentNumber", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6229", browseName="ns=profinet;GSDName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6230", browseName="ns=profinet;GSDDescription", dataType=o6.String)),
        o6.hasComponent(profinet_objtypes.PnSubmoduleStateType(nodeId="ns=profinet;i=5056", browseName="ns=profinet;State")),
    ],
)
o6.reference(profinet_objtypes.PnExpectedSubmoduleContainerType, profinet_reftypes.HasPnExpectedSubmodule, o6.ns["ns=profinet;i=5027"])
o6.reference(o6.ns["ns=profinet;i=5027"], "i=17603", profinet_objtypes.IPnExpectedSubmoduleType)
profinet_objtypes.EthernetInterfaceType(
    nodeId="ns=profinet;i=5057",
    browseName="ns=profinet;EthernetInterface",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6235", browseName="ns=profinet;MacAddress", dataType=o6.Byte, valueRank=1, arrayDimensions=[6]))
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=profinet;i=5042",
    browseName="ns=profinet;<PnEquipments>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6203", browseName="ns=profinet;Vendor", dataType=o6.String)),
        o6.hasComponent(profinet_objtypes.PnInterfaceContainerType(nodeId="ns=profinet;i=5044", browseName="ns=profinet;Interfaces")),
        o6.hasComponent(profinet_objtypes.PnRealModuleContainerType(nodeId="ns=profinet;i=5046", browseName="ns=profinet;Modules")),
        o6.hasComponent(profinet_objtypes.PnAssetContainerType(nodeId="ns=profinet;i=5047", browseName="ns=profinet;Assets")),
        o6.hasComponent(o6.ns["ns=profinet;i=5048"]),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=profinet;i=5049", browseName="ns=profinet;Alarms")),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=profinet;i=6204", browseName="ns=profinet;Diagnosis", dataType=profinet_datypes.PnDeviceDiagnosisDataType, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=profinet;i=7006", browseName="ns=profinet;ShowLocation")),
    ],
)
o6.reference(profinet_objtypes.PnEquipmentContainerType, ns0.reftypes.HasComponent, o6.ns["ns=profinet;i=5042"])
o6.reference(o6.ns["ns=profinet;i=5042"], "i=41", profinet_objtypes.PnDiagnosisAlarmType)
o6.reference(o6.ns["ns=profinet;i=5042"], "i=41", profinet_objtypes.PnAssetChangedEventType)
o6.reference(o6.ns["ns=profinet;i=5042"], "i=17603", profinet_objtypes.IPnEquipmentType)


ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6236",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=profinet;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="NameOfStation",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "String containing the new NameOfStation to be written remanent to the device. The maximum length shall be limited to 240 characters (See [PN Protocol] for details).\n"
            ),
        )
    ],
)
o6.call(nodeId="ns=profinet;i=7007", browseName="ns=profinet;SetNameOfStation", inputArgs=o6.hasProperty(o6.ns["ns=profinet;i=6236"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=profinet;i=5012",
    browseName="ns=profinet;<Interfaces>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6190", browseName="ns=profinet;NameOfStation", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6191", browseName="ns=profinet;DeviceRole", dataType=profinet_datypes.PnDeviceRoleOptionSet)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6192", browseName="ns=profinet;VendorId", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6193", browseName="ns=profinet;DeviceId", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6231", browseName="ns=profinet;DeviceVendor", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6232", browseName="ns=profinet;DeviceInstance", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6233", browseName="ns=profinet;OEMVendorId", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6234", browseName="ns=profinet;OEMDeviceId", dataType=o6.UInt16)),
        o6.hasComponent(profinet_objtypes.PnPortContainerType(nodeId="ns=profinet;i=5045", browseName="ns=profinet;Ports")),
        o6.hasComponent(profinet_objtypes.PnPortStatisticType(nodeId="ns=profinet;i=5058", browseName="ns=profinet;Statistic")),
        o6.hasComponent(o6.ns["ns=profinet;i=7007"]),
        o6.reference(o6.ns["ns=profinet;i=5057"], "ns=profinet;i=4015"),
    ],
)
o6.reference(profinet_objtypes.PnInterfaceContainerType, profinet_reftypes.HasPnInterface, o6.ns["ns=profinet;i=5012"])
o6.reference(o6.ns["ns=profinet;i=5012"], "i=17603", profinet_objtypes.IPnInterfaceType)


del Any, TYPE_CHECKING, uuid, o6, ns0, profinet_reftypes, profinet_datypes, profinet_objtypes
