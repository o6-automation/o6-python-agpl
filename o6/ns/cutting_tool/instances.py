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

"""Generated OPC UA cutting_tool namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.gms as gms
import o6.ns.ia as ia
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machine_tool as machine_tool
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.machinery_result as machinery_result
import o6.ns.ns0 as ns0
from . import datatypes as cutting_tool_datypes
from . import objtypes as cutting_tool_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=cutting_tool;i=5021", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=cutting_tool;i=5022", browseName="Default XML")
o6.hasEncoding(cutting_tool_datypes.FileFormatDataType, o6.ns["ns=cutting_tool;i=5022"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=cutting_tool;i=5023", browseName="Default JSON")
o6.hasEncoding(cutting_tool_datypes.FileFormatDataType, o6.ns["ns=cutting_tool;i=5023"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=cutting_tool;i=6015",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cutting_tool;i=6016", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=cutting_tool;i=6035",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cutting_tool;i=6039", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
isa95_jobcontrol_v2.objtypes.ISA95JobOrderReceiverObjectType(
    nodeId="ns=cutting_tool;i=5003",
    browseName="ns=machinery_jobs;JobOrderControl",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cutting_tool;i=6044", browseName="ns=isa95_jobcontrol_v2;MaxDownloadableJobOrders", dataType=o6.UInt16)),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=6035"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cutting_tool;i=6040",
                browseName="ns=isa95_jobcontrol_v2;EquipmentID",
                description="Defines a read-only set of Equipment Class IDs and Equipment IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cutting_tool;i=6041",
                browseName="ns=isa95_jobcontrol_v2;JobOrderList",
                description="Defines a read-only list of job order information available from the server.",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95JobOrderAndStateDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cutting_tool;i=6042",
                browseName="ns=isa95_jobcontrol_v2;MaterialClassID",
                description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cutting_tool;i=6043",
                browseName="ns=isa95_jobcontrol_v2;MaterialDefinitionID",
                description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cutting_tool;i=6045",
                browseName="ns=isa95_jobcontrol_v2;PersonnelID",
                description="Defines a read-only set of Personnel IDs and Person IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cutting_tool;i=6046",
                browseName="ns=isa95_jobcontrol_v2;PhysicalAssetID",
                description="Defines a read-only set of Physical Asset Class IDs and Physical Asset IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cutting_tool;i=6047",
                browseName="ns=isa95_jobcontrol_v2;WorkMaster",
                description="Defines a read-only set of work master IDs that may be specified in a job order, and the read-only set of parameters that may be specified for a specific work master.",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95WorkMasterDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
    ],
)
isa95_jobcontrol_v2.objtypes.ISA95JobOrderReceiverObjectType(
    nodeId="ns=cutting_tool;i=5008",
    browseName="ns=machinery_jobs;JobOrderControl",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cutting_tool;i=6021", browseName="ns=isa95_jobcontrol_v2;MaxDownloadableJobOrders", dataType=o6.UInt16)),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=6015"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cutting_tool;i=6017",
                browseName="ns=isa95_jobcontrol_v2;EquipmentID",
                description="Defines a read-only set of Equipment Class IDs and Equipment IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cutting_tool;i=6018",
                browseName="ns=isa95_jobcontrol_v2;JobOrderList",
                description="Defines a read-only list of job order information available from the server.",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95JobOrderAndStateDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cutting_tool;i=6019",
                browseName="ns=isa95_jobcontrol_v2;MaterialClassID",
                description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cutting_tool;i=6020",
                browseName="ns=isa95_jobcontrol_v2;MaterialDefinitionID",
                description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cutting_tool;i=6022",
                browseName="ns=isa95_jobcontrol_v2;PersonnelID",
                description="Defines a read-only set of Personnel IDs and Person IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cutting_tool;i=6023",
                browseName="ns=isa95_jobcontrol_v2;PhysicalAssetID",
                description="Defines a read-only set of Physical Asset Class IDs and Physical Asset IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=cutting_tool;i=6051",
                browseName="ns=isa95_jobcontrol_v2;WorkMaster",
                description="Defines a read-only set of work master IDs that may be specified in a job order, and the read-only set of parameters that may be specified for a specific work master.",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95WorkMasterDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
    ],
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashCuttingToolSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=cutting_tool;i=5016",
    browseName="ns=cutting_tool;http://opcfoundation.org/UA/CuttingTool/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=cutting_tool;i=6063", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cutting_tool;i=6064", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2024-11-01T00:00:00Z"))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cutting_tool;i=6065", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/CuttingTool/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cutting_tool;i=6066", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cutting_tool;i=6067",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cutting_tool;i=6068", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cutting_tool;i=6069", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=cutting_tool;i=6086", browseName="ns=cutting_tool;FileFormatDataType", dataType=o6.String, value="FileFormatDataType")
o6.reference(o6.ns["ns=cutting_tool;i=5021"], "i=39", o6.ns["ns=cutting_tool;i=6086"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=cutting_tool;i=6079",
    browseName="ns=cutting_tool;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/CuttingTool/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cutting_tool;i=6083", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/CuttingTool/")),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=6086"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/CuttingTool/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/CuttingTool/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="FileFormatDataType">\n  <opc:Field TypeName="opc:CharArray" Name="Name"/>\n  <opc:Field TypeName="opc:CharArray" Name="FileExtension"/>\n  <opc:Field TypeName="opc:CharArray" Name="Version"/>\n </opc:StructuredType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=cutting_tool;i=6087", browseName="ns=cutting_tool;FileFormatDataType", dataType=o6.String, value="//xs:element[@name='FileFormatDataType']"
)
o6.reference(o6.ns["ns=cutting_tool;i=5022"], "i=39", o6.ns["ns=cutting_tool;i=6087"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=cutting_tool;i=6084",
    browseName="ns=cutting_tool;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/CuttingTool/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cutting_tool;i=6085", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/CuttingTool/Types.xsd")
        ),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=6087"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/CuttingTool/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/CuttingTool/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:complexType name="FileFormatDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Name"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="FileExtension"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Version"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:FileFormatDataType" name="FileFormatDataType"/>\n <xs:complexType name="ListOfFileFormatDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:FileFormatDataType" name="FileFormatDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfFileFormatDataType" name="ListOfFileFormatDataType" nillable="true"/>\n</xs:schema>\n',
)


ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6001",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DirectoryName", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6002",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DirectoryNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=cutting_tool;i=7001",
    browseName="CreateDirectory",
    inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6001"]),
    outputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6002"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6003",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileName", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="RequestFileOpen", dataType=o6.Boolean, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6004",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=cutting_tool;i=7002", browseName="CreateFile", inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6003"]), outputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6004"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6005",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ObjectToDelete", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=cutting_tool;i=7003", browseName="Delete", inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6005"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6006",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7004",
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
    nodeId="ns=cutting_tool;i=6007",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NewNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=cutting_tool;i=7004", browseName="MoveOrCopy", inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6006"]), outputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6007"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6008",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DirectoryName", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6009",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DirectoryNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=cutting_tool;i=7005",
    browseName="CreateDirectory",
    inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6008"]),
    outputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6009"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6010",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileName", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="RequestFileOpen", dataType=o6.Boolean, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6011",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=cutting_tool;i=7006", browseName="CreateFile", inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6010"]), outputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6011"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6012",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ObjectToDelete", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=cutting_tool;i=7007", browseName="Delete", inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6012"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6013",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7008",
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
    nodeId="ns=cutting_tool;i=6014",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NewNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=cutting_tool;i=7008", browseName="MoveOrCopy", inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6013"]), outputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6014"])
)

ns0.objtypes.FileDirectoryType(
    nodeId="ns=cutting_tool;i=5005",
    browseName="ns=machine_tool;WorkMasters",
    references=[
        o6.hasComponent(o6.ns["ns=cutting_tool;i=7005"]),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=7006"]),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=7007"]),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=7008"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6024",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DirectoryName", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6025",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DirectoryNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=cutting_tool;i=7009",
    browseName="CreateDirectory",
    inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6024"]),
    outputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6025"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6026",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileName", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="RequestFileOpen", dataType=o6.Boolean, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6027",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=cutting_tool;i=7010", browseName="CreateFile", inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6026"]), outputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6027"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6028",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ObjectToDelete", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=cutting_tool;i=7011", browseName="Delete", inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6028"]))

ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6029",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7012",
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
    nodeId="ns=cutting_tool;i=6030",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NewNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=cutting_tool;i=7012", browseName="MoveOrCopy", inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6029"]), outputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6030"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6031",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DirectoryName", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6032",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DirectoryNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=cutting_tool;i=7013",
    browseName="CreateDirectory",
    inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6031"]),
    outputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6032"]),
)
o6.reference(o6.ns["ns=cutting_tool;i=7013"], "i=46", o6.ns["ns=cutting_tool;i=6024"])
o6.reference(o6.ns["ns=cutting_tool;i=7013"], "i=46", o6.ns["ns=cutting_tool;i=6025"])

ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6033",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileName", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="RequestFileOpen", dataType=o6.Boolean, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6034",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=cutting_tool;i=7014", browseName="CreateFile", inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6033"]), outputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6034"])
)
o6.reference(o6.ns["ns=cutting_tool;i=7014"], "i=46", o6.ns["ns=cutting_tool;i=6026"])
o6.reference(o6.ns["ns=cutting_tool;i=7014"], "i=46", o6.ns["ns=cutting_tool;i=6027"])

ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6036",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ObjectToDelete", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=cutting_tool;i=7015", browseName="Delete", inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6036"]))
o6.reference(o6.ns["ns=cutting_tool;i=7015"], "i=46", o6.ns["ns=cutting_tool;i=6028"])

ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6037",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7016",
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
    nodeId="ns=cutting_tool;i=6038",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NewNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=cutting_tool;i=7016", browseName="MoveOrCopy", inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6037"]), outputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6038"])
)
o6.reference(o6.ns["ns=cutting_tool;i=7016"], "i=46", o6.ns["ns=cutting_tool;i=6029"])
o6.reference(o6.ns["ns=cutting_tool;i=7016"], "i=46", o6.ns["ns=cutting_tool;i=6030"])

ns0.objtypes.FileDirectoryType(
    nodeId="ns=cutting_tool;i=5018",
    browseName="ns=machine_tool;WorkMasters",
    references=[
        o6.hasComponent(o6.ns["ns=cutting_tool;i=7013"]),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=7014"]),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=7015"]),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=7016"]),
    ],
)
ns0.objtypes.FileDirectoryType(
    nodeId="ns=cutting_tool;i=5017",
    browseName="FileSystem",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=cutting_tool;i=5018"]),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=7009"]),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=7010"]),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=7011"]),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=7012"]),
    ],
)
o6.reference(cutting_tool_objtypes.ToolManufacturingMachineType, ns0.reftypes.HasComponent, o6.ns["ns=cutting_tool;i=5017"])


ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6048",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7017",
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
    nodeId="ns=cutting_tool;i=6049",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobResponse",
            dataType=o6.NodeId("ns=isa95_jobcontrol_v2;i=3013"),
            valueRank=-1,
            description=o6.LocalizedText(
                "Contains information about the execution of a job order, such as the current status of the job, actual material consumed, actual material produced, actual equipment used, and job specific data."
            ),
        ),
        ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")),
    ],
)
o6.call(
    nodeId="ns=cutting_tool;i=7017",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderID",
    inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6048"]),
    outputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6049"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6052",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7018",
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
    nodeId="ns=cutting_tool;i=6053",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobResponse",
            dataType=o6.NodeId("ns=isa95_jobcontrol_v2;i=3013"),
            valueRank=-1,
            description=o6.LocalizedText(
                "Contains information about the execution of a job order, such as the current status of the job, actual material consumed, actual material produced, actual equipment used, and job specific data."
            ),
        ),
        ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")),
    ],
)
o6.call(
    nodeId="ns=cutting_tool;i=7018",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderID",
    inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6052"]),
    outputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6053"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6054",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="JobOrderState",
            dataType=o6.NodeId("ns=isa95_jobcontrol_v2;i=3006"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "Contains a job status of the JobResponse to be returned. The array shall provide at least one entry representing the top level state and potentially additional entries representing substates. The first entry shall be the top level entry, having the BrowsePath set to null. The order of the substates is not defined."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6055",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobResponses",
            dataType=o6.NodeId("ns=isa95_jobcontrol_v2;i=3013"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "Contains a list of information about the execution of a job order, such as the current status of the job, actual material consumed, actual material produced, actual equipment used, and job specific data."
            ),
        ),
        ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")),
    ],
)
o6.call(
    nodeId="ns=cutting_tool;i=7019",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderState",
    inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6054"]),
    outputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6055"]),
)

isa95_jobcontrol_v2.objtypes.ISA95JobResponseProviderObjectType(
    nodeId="ns=cutting_tool;i=5009",
    browseName="ns=machinery_jobs;JobOrderResults",
    references=[o6.hasComponent(o6.ns["ns=cutting_tool;i=7018"]), o6.hasComponent(o6.ns["ns=cutting_tool;i=7019"])],
)
machinery_jobs.objtypes.JobManagementType(
    nodeId="ns=cutting_tool;i=5007",
    browseName="ns=machinery_jobs;JobManagement",
    references=[o6.hasComponent(o6.ns["ns=cutting_tool;i=5008"]), o6.hasComponent(o6.ns["ns=cutting_tool;i=5009"])],
)
ns0.objtypes.FolderType(
    nodeId="ns=cutting_tool;i=5006", browseName="ns=machinery;MachineryBuildingBlocks", modellingRule="Mandatory", references=[o6.hasAddIn(o6.ns["ns=cutting_tool;i=5007"])]
)
o6.reference(cutting_tool_objtypes.ToolManufacturingMachineType, ns0.reftypes.HasComponent, o6.ns["ns=cutting_tool;i=5006"])


ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6050",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="JobOrderState",
            dataType=o6.NodeId("ns=isa95_jobcontrol_v2;i=3006"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "Contains a job status of the JobResponse to be returned. The array shall provide at least one entry representing the top level state and potentially additional entries representing substates. The first entry shall be the top level entry, having the BrowsePath set to null. The order of the substates is not defined."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6056",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobResponses",
            dataType=o6.NodeId("ns=isa95_jobcontrol_v2;i=3013"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "Contains a list of information about the execution of a job order, such as the current status of the job, actual material consumed, actual material produced, actual equipment used, and job specific data."
            ),
        ),
        ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")),
    ],
)
o6.call(
    nodeId="ns=cutting_tool;i=7020",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderState",
    inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6050"]),
    outputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6056"]),
)

isa95_jobcontrol_v2.objtypes.ISA95JobResponseProviderObjectType(
    nodeId="ns=cutting_tool;i=5004",
    browseName="ns=machinery_jobs;JobOrderResults",
    references=[o6.hasComponent(o6.ns["ns=cutting_tool;i=7017"]), o6.hasComponent(o6.ns["ns=cutting_tool;i=7020"])],
)
machinery_jobs.objtypes.JobManagementType(
    nodeId="ns=cutting_tool;i=5002",
    browseName="ns=machinery_jobs;JobManagement",
    references=[o6.hasComponent(o6.ns["ns=cutting_tool;i=5003"]), o6.hasComponent(o6.ns["ns=cutting_tool;i=5004"])],
)
ns0.objtypes.FolderType(
    nodeId="ns=cutting_tool;i=5011", browseName="ns=machinery;MachineryBuildingBlocks", modellingRule="Mandatory", references=[o6.hasAddIn(o6.ns["ns=cutting_tool;i=5002"])]
)
o6.reference(cutting_tool_objtypes.ToolMeasuringMachineType, ns0.reftypes.HasComponent, o6.ns["ns=cutting_tool;i=5011"])


ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6074",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DirectoryName", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6075",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DirectoryNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=cutting_tool;i=7022",
    browseName="CreateDirectory",
    inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6074"]),
    outputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6075"]),
)
o6.reference(o6.ns["ns=cutting_tool;i=7022"], "i=46", o6.ns["ns=cutting_tool;i=6001"])
o6.reference(o6.ns["ns=cutting_tool;i=7022"], "i=46", o6.ns["ns=cutting_tool;i=6002"])

ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6076",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileName", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="RequestFileOpen", dataType=o6.Boolean, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6077",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=cutting_tool;i=7023", browseName="CreateFile", inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6076"]), outputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6077"])
)
o6.reference(o6.ns["ns=cutting_tool;i=7023"], "i=46", o6.ns["ns=cutting_tool;i=6003"])
o6.reference(o6.ns["ns=cutting_tool;i=7023"], "i=46", o6.ns["ns=cutting_tool;i=6004"])

ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6080",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ObjectToDelete", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=cutting_tool;i=7024", browseName="Delete", inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6080"]))
o6.reference(o6.ns["ns=cutting_tool;i=7024"], "i=46", o6.ns["ns=cutting_tool;i=6005"])

ns0.vartypes.PropertyType(
    nodeId="ns=cutting_tool;i=6081",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7025",
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
    nodeId="ns=cutting_tool;i=6082",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=cutting_tool;i=7025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NewNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=cutting_tool;i=7025", browseName="MoveOrCopy", inputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6081"]), outputArgs=o6.hasProperty(o6.ns["ns=cutting_tool;i=6082"])
)
o6.reference(o6.ns["ns=cutting_tool;i=7025"], "i=46", o6.ns["ns=cutting_tool;i=6006"])
o6.reference(o6.ns["ns=cutting_tool;i=7025"], "i=46", o6.ns["ns=cutting_tool;i=6007"])

ns0.objtypes.FileDirectoryType(
    nodeId="ns=cutting_tool;i=5015",
    browseName="ns=cutting_tool;Results",
    references=[
        o6.hasComponent(o6.ns["ns=cutting_tool;i=7022"]),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=7023"]),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=7024"]),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=7025"]),
    ],
)
ns0.objtypes.FileDirectoryType(
    nodeId="ns=cutting_tool;i=5001",
    browseName="FileSystem",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=cutting_tool;i=5005"]),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=5015"]),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=7001"]),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=7002"]),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=7003"]),
        o6.hasComponent(o6.ns["ns=cutting_tool;i=7004"]),
    ],
)
o6.reference(cutting_tool_objtypes.ToolMeasuringMachineType, ns0.reftypes.HasComponent, o6.ns["ns=cutting_tool;i=5001"])


del Any, TYPE_CHECKING, uuid, o6, di, gms, ia, isa95_jobcontrol_v2, machine_tool, machinery, machinery_jobs, machinery_result, ns0, cutting_tool_datypes, cutting_tool_objtypes
