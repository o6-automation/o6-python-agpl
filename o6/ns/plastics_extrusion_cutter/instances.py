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

"""Generated OPC UA plastics_extrusion_cutter namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
import o6.ns.plastics_extrusion as plastics_extrusion
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_extrusion_cutter_datypes
from . import objtypes as plastics_extrusion_cutter_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_cutter;i=6004",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_cutter;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("NO"), o6.LocalizedText("FRONT"), o6.LocalizedText("END"), o6.LocalizedText("BOTH")],
)
oPC40084_9 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_extrusion_cutter;i=6005",
    browseName="ns=plastics_extrusion_cutter;OPC40084_9",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/Cutter/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_cutter;i=6006", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/Cutter/"
            )
        )
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/Cutter/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/Cutter/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:EnumeratedType LengthInBits="32" Name="WallThickeningEnumeration">\n  <opc:EnumeratedValue Name="NO" Value="0"/>\n  <opc:EnumeratedValue Name="FRONT" Value="1"/>\n  <opc:EnumeratedValue Name="END" Value="2"/>\n  <opc:EnumeratedValue Name="BOTH" Value="3"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
oPC40084_9_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_extrusion_cutter;i=6007",
    browseName="ns=plastics_extrusion_cutter;OPC40084_9",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/Cutter/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_cutter;i=6008",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/Cutter/Types.xsd",
            )
        )
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/Cutter/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/Cutter/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="WallThickeningEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="NO_0"/>\n   <xs:enumeration value="FRONT_1"/>\n   <xs:enumeration value="END_2"/>\n   <xs:enumeration value="BOTH_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:WallThickeningEnumeration" name="WallThickeningEnumeration"/>\n <xs:complexType name="ListOfWallThickeningEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WallThickeningEnumeration" name="WallThickeningEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWallThickeningEnumeration" name="ListOfWallThickeningEnumeration" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_cutter;i=6010",
    browseName="ns=plastics_extrusion_cutter;Length",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6011", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_extrusion_cutter_objtypes.CuttingProductType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_cutter;i=6010"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_cutter;i=6012",
    browseName="ns=plastics_extrusion_cutter;LengthCorrection",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6013", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_extrusion_cutter_objtypes.CuttingProductType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_cutter;i=6012"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_cutter;i=6016",
    browseName="ns=plastics_extrusion_cutter;WallThickeningLength",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6017", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_extrusion_cutter_objtypes.CuttingProductType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_cutter;i=6016"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_cutter;i=6014",
    browseName="ns=plastics_extrusion_cutter;Length",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6025", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_cutter;i=6026",
    browseName="ns=plastics_extrusion_cutter;Length",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6035", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_cutter;i=6015",
    browseName="ns=plastics_extrusion_cutter;LengthCorrection",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6036", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_cutter;i=6041",
    browseName="ns=plastics_extrusion_cutter;SampleCuttingLength",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6042", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_extrusion_cutter_objtypes.Cutter_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_cutter;i=6041"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_cutter;i=6045",
    browseName="ns=plastics_extrusion_cutter;WasteCuttingLength",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6046", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(plastics_extrusion_cutter_objtypes.Cutter_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_cutter;i=6045"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_cutter;i=6018",
    browseName="ns=plastics_extrusion_cutter;WallThickeningLength",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6047", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_cutter;i=6048",
    browseName="ns=plastics_extrusion_cutter;TotalWasteLength",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6043", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(plastics_extrusion_cutter_objtypes.Cutter_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_cutter;i=6048"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_cutter;i=6030",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6031", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6051", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_cutter;i=6052",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6053", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6054", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_cutter;i=6064",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6065", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6066", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_cutter;i=6056",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6057", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6077", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_cutter;i=6058",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6059", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6078", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_cutter;i=6060",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6061", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6079", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_cutter;i=6062",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6063", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6080", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_cutter;i=6067",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6068", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6081", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_cutter;i=6069",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6070", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6082", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_cutter;i=6071",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6072", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6083", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_cutter;i=6073",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6074", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6084", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_cutter;i=6075",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6076", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6085", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPlasticsRubberSlashExtrusion_v2SlashCutterSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=plastics_extrusion_cutter;i=5006",
    browseName="ns=plastics_extrusion_cutter;http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/Cutter/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6049", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_cutter;i=6050", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2022-05-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_cutter;i=6086", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/Cutter/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6087", browseName="NamespaceVersion", dataType=o6.String, value="2.00")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_cutter;i=6088",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_cutter;i=6089", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6090", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_cutter;i=6092",
    browseName="ns=plastics_extrusion_cutter;LengthCorrection",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6093", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_cutter;i=6094",
    browseName="ns=plastics_extrusion_cutter;WallThickeningLength",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6095", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_cutter;i=5002",
    browseName="ns=plastics_extrusion_cutter;ProductSpeed",
    modellingRule="Optional",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_cutter;i=6055",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_cutter;i=6030"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_cutter;i=6052"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_cutter;i=6056"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_cutter;i=6058"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_cutter;i=6060"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_cutter;i=6062"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_cutter;i=6064"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_cutter;i=6067"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_cutter;i=6069"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_cutter;i=6071"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_cutter;i=6073"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_cutter;i=6075"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_cutter;i=7004",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_cutter_objtypes.Cutter_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_cutter;i=5002"])
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_cutter;i=5005",
    browseName="ns=plastics_extrusion_cutter;CuttingProgram",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_cutter;i=6040",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_cutter;i=6097", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_cutter;i=7005", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_cutter;i=7006", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
o6.reference(plastics_extrusion_cutter_objtypes.Cutter_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_cutter;i=5005"])
plastics_extrusion_cutter_objtypes.CuttingProductType(
    nodeId="ns=plastics_extrusion_cutter;i=5001",
    browseName="ns=plastics_extrusion_cutter;CuttingProduct_<Nr>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6024", browseName="ns=plastics_extrusion_cutter;Id", dataType=o6.String)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_cutter;i=6091",
                browseName="ns=plastics_extrusion_cutter;WallThickeningPosition",
                dataType=plastics_extrusion_cutter_datypes.WallThickeningEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_cutter;i=6014"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_cutter;i=6015"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_cutter;i=6018"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_cutter;i=6023", browseName="ns=plastics_extrusion_cutter;ActualOutput", dataType=o6.UInt64)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_extrusion_cutter;i=6027", browseName="ns=plastics_extrusion_cutter;SetOutput", dataType=o6.UInt64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_cutter;i=6028", browseName="ns=plastics_extrusion_cutter;TotalOutput", dataType=o6.UInt64)),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_cutter;i=7007", browseName="ns=plastics_extrusion_cutter;ResetOutput")),
    ],
)
o6.reference(plastics_extrusion_cutter_objtypes.CuttingProductsType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_cutter;i=5001"])
plastics_extrusion_cutter_objtypes.CuttingProductType(
    nodeId="ns=plastics_extrusion_cutter;i=5004",
    browseName="ns=plastics_extrusion_cutter;CuttingProduct_<Nr>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_cutter;i=6034", browseName="ns=plastics_extrusion_cutter;Id", dataType=o6.String)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_cutter;i=6096",
                browseName="ns=plastics_extrusion_cutter;WallThickeningPosition",
                dataType=plastics_extrusion_cutter_datypes.WallThickeningEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_cutter;i=6026"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_cutter;i=6033", browseName="ns=plastics_extrusion_cutter;ActualOutput", dataType=o6.UInt64)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_extrusion_cutter;i=6037", browseName="ns=plastics_extrusion_cutter;SetOutput", dataType=o6.UInt64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_cutter;i=6038", browseName="ns=plastics_extrusion_cutter;TotalOutput", dataType=o6.UInt64)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_cutter;i=6092"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_cutter;i=6094"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_cutter;i=7008", browseName="ns=plastics_extrusion_cutter;ResetOutput")),
    ],
)
plastics_extrusion_cutter_objtypes.CuttingProductsType(
    nodeId="ns=plastics_extrusion_cutter;i=5003",
    browseName="ns=plastics_extrusion_cutter;CuttingProducts",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_cutter;i=5004"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_extrusion_cutter;i=6032", browseName="ns=plastics_extrusion_cutter;ActualCuttingProductId", dataType=o6.String, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
)
o6.reference(plastics_extrusion_cutter_objtypes.Cutter_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_cutter;i=5003"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, plastics_extrusion, plastics_rubber, plastics_extrusion_cutter_datypes, plastics_extrusion_cutter_objtypes
