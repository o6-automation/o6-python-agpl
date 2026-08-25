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

"""Generated OPC UA ijt_tightening namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.amb as amb
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.ijt_base as ijt_base
import o6.ns.machinery as machinery
import o6.ns.machinery_result as machinery_result
import o6.ns.ns0 as ns0
from . import objtypes as ijt_tightening_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=ijt_tightening;i=6005",
    browseName="ns=ijt_tightening;DesignType",
    description="DesignType provides information on the design of the Tool.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_tightening;i=6006",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[6],
                value=[
                    o6.LocalizedText("OTHER"),
                    o6.LocalizedText("PISTOL"),
                    o6.LocalizedText("ANGLE"),
                    o6.LocalizedText("STRAIGHT"),
                    o6.LocalizedText("OFFSET"),
                    o6.LocalizedText("REVERSE_OFFSET"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
    value=0,
)
o6.reference(ijt_tightening_objtypes.ITighteningToolParametersType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_tightening;i=6005"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashIJTSlashTighteningSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=ijt_tightening;i=5004",
    browseName="ns=ijt_tightening;http://opcfoundation.org/UA/IJT/Tightening/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=ijt_tightening;i=6007", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=ijt_tightening;i=6008", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2025-10-06T00:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=ijt_tightening;i=6009", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/IJT/Tightening/")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ijt_tightening;i=6010", browseName="NamespaceVersion", dataType=o6.String, value="2.00.1")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=ijt_tightening;i=6011", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[0], value=[])
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_tightening;i=6012", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0], value=[]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ijt_tightening;i=6013", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=ijt_tightening;i=6014",
    browseName="ns=ijt_tightening;DriveMethod",
    description="DriveMethod provides information on the drive method of the motor of the Tool.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_tightening;i=6015",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[8],
                value=[
                    o6.LocalizedText("OTHER"),
                    o6.LocalizedText("CONTINUOUS"),
                    o6.LocalizedText("PULSE"),
                    o6.LocalizedText("RATCHETING"),
                    o6.LocalizedText("TENSIONING"),
                    o6.LocalizedText("MANUAL"),
                    o6.LocalizedText("INERTIA"),
                    o6.LocalizedText("HYBRID"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
    value=0,
)
o6.reference(ijt_tightening_objtypes.ITighteningToolParametersType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_tightening;i=6014"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=ijt_tightening;i=6016",
    browseName="ns=ijt_tightening;DriveType",
    description="DriveType provides information on the drive type of the Tool.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_tightening;i=6017",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[5],
                value=[o6.LocalizedText("OTHER"), o6.LocalizedText("ELECTRIC"), o6.LocalizedText("HYDRAULIC"), o6.LocalizedText("PNEUMATIC"), o6.LocalizedText("MANUAL")],
            )
        )
    ],
    dataType=o6.Byte,
    value=0,
)
o6.reference(ijt_tightening_objtypes.ITighteningToolParametersType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_tightening;i=6016"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=ijt_tightening;i=6018",
    browseName="ns=ijt_tightening;ShutOffMethod",
    description="ShutOffMethod provides information on the shutoff method of the tool.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_tightening;i=6019",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[4],
                value=[o6.LocalizedText("OTHER"), o6.LocalizedText("MECHANICAL"), o6.LocalizedText("CURRENT"), o6.LocalizedText("TRANSDUCER")],
            )
        )
    ],
    dataType=o6.Byte,
    value=0,
)
o6.reference(ijt_tightening_objtypes.ITighteningToolParametersType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_tightening;i=6018"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=ijt_tightening;i=6026",
    browseName="ns=ijt_base;PhysicalQuantity",
    description="PhysicalQuantity is to determine the type of the physical quantity associated to a given value(s).",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_tightening;i=6027",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[29],
                value=[
                    o6.LocalizedText("OTHER"),
                    o6.LocalizedText("TIME"),
                    o6.LocalizedText("TORQUE"),
                    o6.LocalizedText("ANGLE"),
                    o6.LocalizedText("IMPULSE"),
                    o6.LocalizedText("DISTANCE"),
                    o6.LocalizedText("AREA"),
                    o6.LocalizedText("VOLUME"),
                    o6.LocalizedText("FORCE"),
                    o6.LocalizedText("PRESSURE"),
                    o6.LocalizedText("VOLTAGE"),
                    o6.LocalizedText("CURRENT"),
                    o6.LocalizedText("RESISTANCE"),
                    o6.LocalizedText("POWER"),
                    o6.LocalizedText("ENERGY"),
                    o6.LocalizedText("MASS"),
                    o6.LocalizedText("TEMPERATURE"),
                    o6.LocalizedText("FREQUENCY"),
                    o6.LocalizedText("JOLT"),
                    o6.LocalizedText("VIBRATION"),
                    o6.LocalizedText("NUMBER"),
                    o6.LocalizedText("LINEAR_SPEED"),
                    o6.LocalizedText("ANGULAR_SPEED"),
                    o6.LocalizedText("LINEAR_ACCELERATION"),
                    o6.LocalizedText("ANGULAR_ACCELERATION"),
                    o6.LocalizedText("TORQUE_SPEED"),
                    o6.LocalizedText("TORQUE_ACCELERATION"),
                    o6.LocalizedText("TORQUE_PER_ANGLE_GRADIENT"),
                    o6.LocalizedText("TORQUE_PER_ANGLE_GRADIENT2"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
    value=0,
)
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=ijt_tightening;i=6001",
    browseName="ns=ijt_tightening;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/IJT/Tightening/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=ijt_tightening;i=6002", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/IJT/Tightening/")
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_tightening;i=6030",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
            )
        ),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ua="http://opcfoundation.org/UA/" DefaultByteOrder="LittleEndian" xmlns:tns="http://opcfoundation.org/UA/IJT/Tightening/" TargetNamespace="http://opcfoundation.org/UA/IJT/Tightening/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n</opc:TypeDictionary>\n',
)
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=ijt_tightening;i=6003",
    browseName="ns=ijt_tightening;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/IJT/Tightening/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_tightening;i=6004", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/IJT/Tightening/Types.xsd"
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_tightening;i=6031",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
            )
        ),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" targetNamespace="http://opcfoundation.org/UA/IJT/Tightening/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/IJT/Tightening/Types.xsd" elementFormDefault="qualified">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n</xs:schema>\n',
)
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=ijt_tightening;i=6029",
    browseName="ns=ijt_base;PhysicalQuantity",
    description="PhysicalQuantity is to determine the type of the physical quantity associated to a given value(s).",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_tightening;i=6032",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[29],
                value=[
                    o6.LocalizedText("OTHER"),
                    o6.LocalizedText("TIME"),
                    o6.LocalizedText("TORQUE"),
                    o6.LocalizedText("ANGLE"),
                    o6.LocalizedText("IMPULSE"),
                    o6.LocalizedText("DISTANCE"),
                    o6.LocalizedText("AREA"),
                    o6.LocalizedText("VOLUME"),
                    o6.LocalizedText("FORCE"),
                    o6.LocalizedText("PRESSURE"),
                    o6.LocalizedText("VOLTAGE"),
                    o6.LocalizedText("CURRENT"),
                    o6.LocalizedText("RESISTANCE"),
                    o6.LocalizedText("POWER"),
                    o6.LocalizedText("ENERGY"),
                    o6.LocalizedText("MASS"),
                    o6.LocalizedText("TEMPERATURE"),
                    o6.LocalizedText("FREQUENCY"),
                    o6.LocalizedText("JOLT"),
                    o6.LocalizedText("VIBRATION"),
                    o6.LocalizedText("NUMBER"),
                    o6.LocalizedText("LINEAR_SPEED"),
                    o6.LocalizedText("ANGULAR_SPEED"),
                    o6.LocalizedText("LINEAR_ACCELERATION"),
                    o6.LocalizedText("ANGULAR_ACCELERATION"),
                    o6.LocalizedText("TORQUE_SPEED"),
                    o6.LocalizedText("TORQUE_ACCELERATION"),
                    o6.LocalizedText("TORQUE_PER_ANGLE_GRADIENT"),
                    o6.LocalizedText("TORQUE_PER_ANGLE_GRADIENT2"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
    value=0,
)
ijt_base.vartypes.JoiningDataVariableType(
    nodeId="ns=ijt_tightening;i=6020",
    browseName="ns=ijt_tightening;MaxTorque",
    description="MaxTorque is the maximum allowed torque for which the tool may be used for tightening processes. For Click Wrenches, it may not be available.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_tightening;i=6028",
                browseName="ns=ijt_base;EngineeringUnits",
                description="0:EngineeringUnits defines the engineering unit of the values.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
        o6.hasComponent(o6.ns["ns=ijt_tightening;i=6029"]),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(ijt_tightening_objtypes.ITighteningToolParametersType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_tightening;i=6020"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=ijt_tightening;i=6025",
    browseName="ns=ijt_base;PhysicalQuantity",
    description="PhysicalQuantity is to determine the type of the physical quantity associated to a given value(s).",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_tightening;i=6033",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[29],
                value=[
                    o6.LocalizedText("OTHER"),
                    o6.LocalizedText("TIME"),
                    o6.LocalizedText("TORQUE"),
                    o6.LocalizedText("ANGLE"),
                    o6.LocalizedText("IMPULSE"),
                    o6.LocalizedText("DISTANCE"),
                    o6.LocalizedText("AREA"),
                    o6.LocalizedText("VOLUME"),
                    o6.LocalizedText("FORCE"),
                    o6.LocalizedText("PRESSURE"),
                    o6.LocalizedText("VOLTAGE"),
                    o6.LocalizedText("CURRENT"),
                    o6.LocalizedText("RESISTANCE"),
                    o6.LocalizedText("POWER"),
                    o6.LocalizedText("ENERGY"),
                    o6.LocalizedText("MASS"),
                    o6.LocalizedText("TEMPERATURE"),
                    o6.LocalizedText("FREQUENCY"),
                    o6.LocalizedText("JOLT"),
                    o6.LocalizedText("VIBRATION"),
                    o6.LocalizedText("NUMBER"),
                    o6.LocalizedText("LINEAR_SPEED"),
                    o6.LocalizedText("ANGULAR_SPEED"),
                    o6.LocalizedText("LINEAR_ACCELERATION"),
                    o6.LocalizedText("ANGULAR_ACCELERATION"),
                    o6.LocalizedText("TORQUE_SPEED"),
                    o6.LocalizedText("TORQUE_ACCELERATION"),
                    o6.LocalizedText("TORQUE_PER_ANGLE_GRADIENT"),
                    o6.LocalizedText("TORQUE_PER_ANGLE_GRADIENT2"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
    value=0,
)
ijt_base.vartypes.JoiningDataVariableType(
    nodeId="ns=ijt_tightening;i=6021",
    browseName="ns=ijt_tightening;MinTorque",
    description="MinTorque is the minimum allowed torque for which the tool may be used for tightening processes.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_tightening;i=6024",
                browseName="ns=ijt_base;EngineeringUnits",
                description="0:EngineeringUnits defines the engineering unit of the values.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
        o6.hasComponent(o6.ns["ns=ijt_tightening;i=6025"]),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(ijt_tightening_objtypes.ITighteningToolParametersType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_tightening;i=6021"])
ijt_base.vartypes.JoiningDataVariableType(
    nodeId="ns=ijt_tightening;i=6022",
    browseName="ns=ijt_tightening;MaxSpeed",
    description="MaxSpeed is the maximum rotation speed of the driving shaft.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ijt_tightening;i=6036",
                browseName="ns=ijt_base;EngineeringUnits",
                description="0:EngineeringUnits defines the engineering unit of the values.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
        o6.hasComponent(o6.ns["ns=ijt_tightening;i=6026"]),
    ],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(ijt_tightening_objtypes.ITighteningToolParametersType, ns0.reftypes.HasComponent, o6.ns["ns=ijt_tightening;i=6022"])


del Any, TYPE_CHECKING, uuid, o6, amb, di, ia, ijt_base, machinery, machinery_result, ns0, ijt_tightening_objtypes
