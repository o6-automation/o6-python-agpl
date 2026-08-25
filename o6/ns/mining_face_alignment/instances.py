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

"""Generated OPC UA mining_face_alignment namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.mining as mining
import o6.ns.ns0 as ns0
from . import objtypes as mining_face_alignment_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=mining_face_alignment;i=6003",
    browseName="ns=mining_face_alignment;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Mining/PELOServices/FaceAlignmentSystem/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_face_alignment;i=6004",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/Mining/PELOServices/FaceAlignmentSystem/",
            )
        )
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/Mining/PELOServices/FaceAlignmentSystem/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/Mining/PELOServices/FaceAlignmentSystem/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n</opc:TypeDictionary>\n',
)
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=mining_face_alignment;i=6005",
    browseName="ns=mining_face_alignment;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Mining/PELOServices/FaceAlignmentSystem/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_face_alignment;i=6006",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/Mining/PELOServices/FaceAlignmentSystem/Types.xsd",
            )
        )
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/Mining/PELOServices/FaceAlignmentSystem/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/Mining/PELOServices/FaceAlignmentSystem/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n</xs:schema>\n',
)
mining.vartypes.LongwallShieldOffsetArrayItemType(
    nodeId="ns=mining_face_alignment;i=6001",
    browseName="ns=mining_face_alignment;Offsets",
    description="The Offsets variable describes the offsets calculated by the FAS which have to be considered by the RSS for optimal shield alignment in areal view.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_face_alignment;i=6002",
                browseName="ns=mining;EngineeringUnits",
                description="This is the EngineeringUnit of the offsets.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5067858, displayName=o6.LocalizedText("m"), description=o6.LocalizedText("metre")
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_face_alignment;i=6007",
                browseName="ns=mining;EURange",
                description="This is the EURange of the offsets.",
                dataType=ns0.datatypes.Range,
                value=ns0.datatypes.Range(low=-20.0, high=20.0),
            )
        ),
    ],
    dataType=mining.datatypes.LongwallShieldOffsetDataType,
    valueRank=1,
    arrayDimensions=[0],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=mining_face_alignment;i=5001",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=mining_face_alignment;i=6001"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=mining_face_alignment;i=6009",
                browseName="ns=mining_face_alignment;CurrentSequenceNumber",
                description="The CurrentSequenceNumber variable describes the current sequence number on which the offset values are applicable. It is being increased when offset values change",
                dataType=o6.UInt16,
                value=0,
            )
        ),
    ],
)
o6.reference(mining_face_alignment_objtypes.FaceAlignmentSystemType, ns0.reftypes.HasComponent, o6.ns["ns=mining_face_alignment;i=5001"])
mining.objtypes.MiningEquipmentIdentificationType(
    nodeId="ns=mining_face_alignment;i=5002",
    browseName="ns=mining;MiningEquipmentIdentification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_face_alignment;i=6008",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose the MachineryItem is used.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_face_alignment;i=6010",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_face_alignment;i=6011",
                browseName="ns=di;ManufacturerUri",
                description="A globally unique identifier of the manufacturer of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_face_alignment;i=6012",
                browseName="ns=di;Model",
                description="A human-readable, localized name of the model of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_face_alignment;i=6013",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_face_alignment;i=6014",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(mining_face_alignment_objtypes.FaceAlignmentSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=mining_face_alignment;i=5002"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMiningSlashPELOServicesSlashFaceAlignmentSystemSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=mining_face_alignment;i=5004",
    browseName="ns=mining_face_alignment;http://opcfoundation.org/UA/Mining/PELOServices/FaceAlignmentSystem/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=mining_face_alignment;i=6015", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_face_alignment;i=6016", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2022-09-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_face_alignment;i=6017",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/Mining/PELOServices/FaceAlignmentSystem/",
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_face_alignment;i=6018", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_face_alignment;i=6019",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[2],
                value=[ns0.datatypes.IdType.NUMERIC, ns0.datatypes.IdType.STRING],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_face_alignment;i=6020", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_face_alignment;i=6021", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, mining, ns0, mining_face_alignment_objtypes
