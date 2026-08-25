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

"""Generated OPC UA plastics_extrusion_line namespace declarations."""

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
from . import datatypes as plastics_extrusion_line_datypes
from . import objtypes as plastics_extrusion_line_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_extrusion_line;i=5007", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_extrusion_line;i=5008", browseName="Default XML")
o6.hasEncoding(plastics_extrusion_line_datypes.MaterialMappingType, o6.ns["ns=plastics_extrusion_line;i=5008"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_extrusion_line;i=5009", browseName="Default JSON")
o6.hasEncoding(plastics_extrusion_line_datypes.MaterialMappingType, o6.ns["ns=plastics_extrusion_line;i=5009"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6002",
    browseName="ns=plastics_extrusion_line;Throughput",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6003", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_extrusion_line_objtypes.ProductionParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_line;i=6002"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6005",
    browseName="ns=plastics_extrusion_line;ProductWeight",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6006", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_extrusion_line_objtypes.ProductionParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_line;i=6005"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6007",
    browseName="ns=plastics_extrusion_line;LineSpeed",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6008", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_extrusion_line_objtypes.ProductionParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_line;i=6007"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6009",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6010", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6011",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6012", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6013",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6014", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6015",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6016", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_extrusion_line;i=5017",
    browseName="ns=plastics_extrusion_line;ElectricalEnergy",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6009"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6011"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6013"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_line;i=6017", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
o6.reference(plastics_extrusion_line_objtypes.ProductionParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_line;i=5017"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6018",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6021", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6022",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6024", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_extrusion_line;i=5016",
    browseName="ns=plastics_extrusion_line;FluidEnergy",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6015"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6018"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6022"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_line;i=6025", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
o6.reference(plastics_extrusion_line_objtypes.ProductionParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_line;i=5016"])
plastics_rubber.objtypes.MachineMESConfigurationType(
    nodeId="ns=plastics_extrusion_line;i=5003",
    browseName="ns=plastics_extrusion_line;MachineMESConfiguration",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_line;i=6046",
                browseName="ns=plastics_rubber;StandstillReasons",
                description="List of the standstill reasons from which one is selected by the operator in the case of a standstill",
                dataType=plastics_rubber.datatypes.StandstillReasonType,
                valueRank=1,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_line;i=6047",
                browseName="ns=plastics_rubber;StandstillReasonsLockedByMES",
                description="Indication if the list StandstillReasons has been modified by the MES and may not be changed by the machine",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_line;i=6053",
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
o6.reference(plastics_extrusion_line_objtypes.ExtrusionLine_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_line;i=5003"])
plastics_rubber.objtypes.MESMessageType(
    nodeId="ns=plastics_extrusion_line;i=5004",
    browseName="ns=plastics_extrusion_line;MESMessage",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6054", browseName="ns=plastics_rubber;Id", description="Id of the message", dataType=o6.String, value="")
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_line;i=6055", browseName="ns=plastics_rubber;Message", description="Text of the message", dataType=o6.String, value=""
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6056", browseName="Severity", description="Severity of the message", dataType=o6.UInt16, value=0)
        ),
    ],
)
o6.reference(plastics_extrusion_line_objtypes.ExtrusionLine_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_line;i=5004"])
plastics_rubber.objtypes.UsersType(
    nodeId="ns=plastics_extrusion_line;i=5005",
    browseName="ns=plastics_extrusion_line;Users",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6059", browseName="NodeVersion", dataType=o6.String, value=""))],
)
o6.reference(plastics_extrusion_line_objtypes.ExtrusionLine_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_line;i=5005"])
o6.reference(o6.ns["ns=plastics_extrusion_line;i=5005"], "i=41", "i=2133")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6019",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6061", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6020",
    browseName="ns=plastics_extrusion_line;LineSpeed",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6063", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6062",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6066", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6067",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6068", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6023",
    browseName="ns=plastics_extrusion_line;ProductWeight",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6069", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6071",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6072", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6004",
    browseName="ns=plastics_extrusion_line;Throughput",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6075", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6064",
    browseName="ns=plastics_extrusion_line;ElectricalEnergyConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6076", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_extrusion_line;i=6114", browseName="ns=plastics_extrusion_line;MaterialMappingType", dataType=o6.String, value="MaterialMappingType"
)
o6.reference(o6.ns["ns=plastics_extrusion_line;i=5007"], "i=39", o6.ns["ns=plastics_extrusion_line;i=6114"])
oPC40084_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_extrusion_line;i=6027",
    browseName="ns=plastics_extrusion_line;OPC40084_2",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/ExtrusionLine/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_line;i=6028",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/ExtrusionLine/",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6114"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/ExtrusionLine/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/ExtrusionLine/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="MaterialMappingType">\n  <opc:Field TypeName="opc:CharArray" Name="MaterialId"/>\n  <opc:Field TypeName="opc:CharArray" Name="MaterialLot"/>\n  <opc:Field TypeName="opc:CharArray" Name="HopperId"/>\n </opc:StructuredType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_extrusion_line;i=6115", browseName="ns=plastics_extrusion_line;MaterialMappingType", dataType=o6.String, value="//xs:element[@name='MaterialMappingType']"
)
o6.reference(o6.ns["ns=plastics_extrusion_line;i=5008"], "i=39", o6.ns["ns=plastics_extrusion_line;i=6115"])
oPC40084_2_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_extrusion_line;i=6029",
    browseName="ns=plastics_extrusion_line;OPC40084_2",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/ExtrusionLine/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_line;i=6030",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/ExtrusionLine/Types.xsd",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6115"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/ExtrusionLine/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/ExtrusionLine/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:complexType name="MaterialMappingType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="MaterialId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="MaterialLot"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="HopperId"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:MaterialMappingType" name="MaterialMappingType"/>\n <xs:complexType name="ListOfMaterialMappingType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:MaterialMappingType" name="MaterialMappingType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfMaterialMappingType" name="ListOfMaterialMappingType" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6131",
    browseName="ns=plastics_extrusion_line;Throughput",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6132", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(plastics_extrusion_line_objtypes.JobType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_line;i=6131"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6134",
    browseName="ns=plastics_extrusion_line;ProductWeight",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6135", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(plastics_extrusion_line_objtypes.JobType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_line;i=6134"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6137",
    browseName="ns=plastics_extrusion_line;LineSpeed",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6138", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(plastics_extrusion_line_objtypes.JobType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_line;i=6137"])
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_extrusion_line;i=5018",
    browseName="ns=plastics_extrusion_line;PressureAir",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6062"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6067"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6071"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_line;i=6140", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
o6.reference(plastics_extrusion_line_objtypes.ProductionParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_line;i=5018"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6141",
    browseName="ns=plastics_extrusion_line;FluidEnergyConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6147", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6152",
    browseName="ns=plastics_extrusion_line;ElectricalEnergyConsumption",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6070", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(plastics_extrusion_line_objtypes.JobGroupType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_line;i=6152"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6153",
    browseName="ns=plastics_extrusion_line;FluidEnergyConsumption",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6144", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(plastics_extrusion_line_objtypes.JobGroupType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_line;i=6153"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6065",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6181", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6182",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6183", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_extrusion_line;i=5019",
    browseName="ns=plastics_extrusion_line;ElectricalEnergy",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6019"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6065"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6182"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_line;i=6184", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6185",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6186", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6154",
    browseName="ns=plastics_extrusion_line;PressureAirConsumption",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6211", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(plastics_extrusion_line_objtypes.JobGroupType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_line;i=6154"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6210",
    browseName="ns=plastics_extrusion_line;PressureAirConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6212", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6226",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6227", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6228",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6229", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6230",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6231", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_extrusion_line;i=5022",
    browseName="ns=plastics_extrusion_line;FluidEnergy",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6185"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6226"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6228"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_line;i=6232", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6233",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6234", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6235",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6236", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_extrusion_line;i=5023",
    browseName="ns=plastics_extrusion_line;PressureAir",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6230"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6233"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6235"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_line;i=6237", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
plastics_extrusion_line_objtypes.ProductionParametersType(
    nodeId="ns=plastics_extrusion_line;i=5006",
    browseName="ns=plastics_extrusion_line;ProductionParameters",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=5019"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=5022"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=5023"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6004"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6020"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6023"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_line;i=6060", browseName="ns=plastics_extrusion_line;GoodProduct", dataType=o6.Boolean, value=False)
        ),
    ],
)
o6.reference(plastics_extrusion_line_objtypes.ExtrusionLine_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_line;i=5006"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6139",
    browseName="ns=plastics_extrusion_line;LineSpeed",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6256", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6136",
    browseName="ns=plastics_extrusion_line;ProductWeight",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6258", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_line;i=6133",
    browseName="ns=plastics_extrusion_line;Throughput",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6260", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
plastics_extrusion_line_objtypes.JobType(
    nodeId="ns=plastics_extrusion_line;i=5010",
    browseName="ns=plastics_extrusion_line;Job_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6158", browseName="ns=plastics_extrusion_line;CustomerName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6159", browseName="ns=plastics_extrusion_line;Description", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6160", browseName="ns=plastics_extrusion_line;Id", dataType=o6.String, value="")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6161", browseName="ns=plastics_extrusion_line;LotSize", dataType=o6.Double)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_line;i=6162",
                browseName="ns=plastics_extrusion_line;ParameterSetting",
                dataType=plastics_rubber.datatypes.ParameterSettingType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6163", browseName="ns=plastics_extrusion_line;ProductDescription", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6164", browseName="ns=plastics_extrusion_line;ProductId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6167", browseName="ns=plastics_extrusion_line;Sequence", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6168", browseName="ns=plastics_extrusion_line;SetOutput", dataType=o6.Double)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_line;i=6169", browseName="ns=plastics_extrusion_line;Status", dataType=plastics_rubber.datatypes.JobStatusEnumeration
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6170", browseName="ns=plastics_extrusion_line;Strand", dataType=o6.UInt32)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_line;i=6130", browseName="ns=plastics_extrusion_line;GoodProduct", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6133"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6136"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6139"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_line;i=6155", browseName="ns=plastics_extrusion_line;ActualLot", dataType=o6.UInt32)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_line;i=6156", browseName="ns=plastics_extrusion_line;ActualOutput", dataType=o6.Double)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_line;i=6157", browseName="ns=plastics_extrusion_line;ActualOutputRate", dataType=o6.Double)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_line;i=6172", browseName="ns=plastics_extrusion_line;ActualBadOutput", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_line;i=6178", browseName="ns=plastics_extrusion_line;ActualGoodOutput", dataType=o6.Double, value=0.0)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_extrusion_line;i=6179", browseName="ns=plastics_extrusion_line;ActualLotName", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_line;i=6180", browseName="ns=plastics_extrusion_line;ActualSampleOutput", dataType=o6.Double, value=0.0)
        ),
    ],
)
o6.reference(plastics_extrusion_line_objtypes.JobGroupType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_line;i=5010"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPlasticsRubberSlashExtrusion_v2SlashExtrusionLineSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=plastics_extrusion_line;i=5024",
    browseName="ns=plastics_extrusion_line;http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/ExtrusionLine/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6257", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_line;i=6259", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2022-05-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_line;i=6261",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/ExtrusionLine/",
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6262", browseName="NamespaceVersion", dataType=o6.String, value="2.00")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_line;i=6263",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_line;i=6264", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6265", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6271", browseName="NodeVersion", dataType=o6.String, value="")
o6.reference(o6.ns["ns=plastics_extrusion_line;i=6271"], "i=41", plastics_extrusion_line_objtypes.JobStatusChangedEventType)
o6.reference(o6.ns["ns=plastics_extrusion_line;i=6271"], "i=41", plastics_extrusion_line_objtypes.UnitFinishedEventType)
o6.reference(o6.ns["ns=plastics_extrusion_line;i=6271"], "i=41", plastics_extrusion_line_objtypes.LotFinishedEventType)
o6.reference(o6.ns["ns=plastics_extrusion_line;i=6271"], "i=41", plastics_extrusion_line_objtypes.JobGroupStatusChangedEventType)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_line;i=6191",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_line;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[10],
    value=[
        ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Description", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="CustomerName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ProductName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ProductDescription", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Strand", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="Sequence", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ParameterSetting", dataType=o6.NodeId("ns=plastics_rubber;i=3026"), valueRank=1),
        ns0.datatypes.Argument(name="SetOutput", dataType=o6.Double, valueRank=-1),
        ns0.datatypes.Argument(name="LotSize", dataType=o6.Double, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_line;i=6192",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_line;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="JobNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_line;i=7011",
    browseName="ns=plastics_extrusion_line;AddJob",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_line;i=6191"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_line;i=6192"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_line;i=6166",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_line;i=7021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Name", dataType=o6.LocalizedText, valueRank=-1),
        ns0.datatypes.Argument(name="Density", dataType=o6.Double, valueRank=-1),
    ],
)
o6.call(nodeId="ns=plastics_extrusion_line;i=7021", browseName="ns=plastics_rubber;AddMaterial", inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_line;i=6166"]))

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_line;i=6279",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_line;i=7022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=plastics_extrusion_line;i=7022", browseName="ns=plastics_rubber;RemoveMaterialById", inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_line;i=6279"]))

plastics_rubber.objtypes.MaterialListType(
    nodeId="ns=plastics_extrusion_line;i=5020",
    browseName="ns=plastics_extrusion_line;MaterialList",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6145", browseName="ns=plastics_rubber;DensityUnit", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6146", browseName="NodeVersion", dataType=o6.String, value="")),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=7021"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=7022"]),
    ],
)
o6.reference(plastics_extrusion_line_objtypes.ExtrusionLine_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_line;i=5020"])
o6.reference(o6.ns["ns=plastics_extrusion_line;i=5020"], "i=41", plastics_extrusion_line_objtypes.RequestAddMaterialEventType)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_line;i=6196",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_line;i=7023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=plastics_extrusion_line;i=7023", browseName="ns=plastics_extrusion_line;FinishJobById", inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_line;i=6196"]))

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_line;i=6198",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_line;i=7024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=plastics_extrusion_line;i=7024", browseName="ns=plastics_extrusion_line;InterruptJobById", inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_line;i=6198"]))

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_line;i=6207",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_line;i=7025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=plastics_extrusion_line;i=7025", browseName="ns=plastics_extrusion_line;RemoveJobById", inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_line;i=6207"]))

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_line;i=6208",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_line;i=7026",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=plastics_extrusion_line;i=7026", browseName="ns=plastics_extrusion_line;StartJobById", inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_line;i=6208"]))

plastics_extrusion_line_objtypes.JobGroupType(
    nodeId="ns=plastics_extrusion_line;i=5021",
    browseName="ns=plastics_extrusion_line;JobGroup_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_line;i=6193",
                browseName="ns=plastics_extrusion_line;ConfigurationParameters",
                dataType=plastics_rubber.datatypes.ConfigurationParameterType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6194", browseName="ns=plastics_extrusion_line;Description", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6195", browseName="ns=plastics_extrusion_line;EquipmentDescription", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6197", browseName="ns=plastics_extrusion_line;Id", dataType=o6.String, value="")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6199", browseName="ns=plastics_extrusion_line;LatestEnd", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6200", browseName="ns=plastics_extrusion_line;PlannedProductionTime", dataType=ns0.datatypes.Duration)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6201", browseName="ns=plastics_extrusion_line;PlannedSetUpTime", dataType=ns0.datatypes.Duration)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6202", browseName="ns=plastics_extrusion_line;PlannedStart", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6203", browseName="ns=plastics_extrusion_line;Priority", dataType=o6.UInt32)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_line;i=6204",
                browseName="ns=plastics_extrusion_line;MaterialMapping",
                dataType=plastics_extrusion_line_datypes.MaterialMappingType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6205", browseName="NodeVersion", dataType=o6.String, value="")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_line;i=6206", browseName="ns=plastics_extrusion_line;ProductionDatasetName", dataType=o6.String)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_line;i=6209", browseName="ns=plastics_extrusion_line;Status", dataType=plastics_rubber.datatypes.JobStatusEnumeration
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6064"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6141"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=6210"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=7011"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=7023"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=7024"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=7025"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=7026"]),
    ],
)
o6.reference(plastics_extrusion_line_objtypes.JobGroupsType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_line;i=5021"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_line;i=6269",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_line;i=7034",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[10],
    value=[
        ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Description", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="EquipmentDescription", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ProductionDatasetName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="MaterialMapping", dataType=o6.NodeId("ns=plastics_extrusion_line;i=3003"), valueRank=1),
        ns0.datatypes.Argument(name="Priority", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="PlannedStart", dataType=ns0.datatypes.UtcTime, valueRank=-1),
        ns0.datatypes.Argument(name="PlannedProductionTime", dataType=ns0.datatypes.Duration, valueRank=-1),
        ns0.datatypes.Argument(name="PlannedSetUpTime", dataType=ns0.datatypes.Duration, valueRank=-1),
        ns0.datatypes.Argument(name="LatestEnd", dataType=ns0.datatypes.UtcTime, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_line;i=6270",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_line;i=7034",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="JobGroupNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_line;i=7034",
    browseName="ns=plastics_extrusion_line;AddJobGroup",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_line;i=6269"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_line;i=6270"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_line;i=6272",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_line;i=7035",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_line;i=7035", browseName="ns=plastics_extrusion_line;RemoveJobGroupById", inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_line;i=6272"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_line;i=6273",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_line;i=7036",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_line;i=7036", browseName="ns=plastics_extrusion_line;FinishJobGroupById", inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_line;i=6273"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_line;i=6274",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_line;i=7037",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_line;i=7037", browseName="ns=plastics_extrusion_line;InterruptJobGroupById", inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_line;i=6274"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_line;i=6275",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_line;i=7038",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=plastics_extrusion_line;i=7038", browseName="ns=plastics_extrusion_line;StartJobGroupById", inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_line;i=6275"]))

plastics_extrusion_line_objtypes.JobGroupsType(
    nodeId="ns=plastics_extrusion_line;i=5025",
    browseName="ns=plastics_extrusion_line;JobGroups",
    modellingRule="Optional",
    references=[
        o6.hasProperty(o6.ns["ns=plastics_extrusion_line;i=6271"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=7034"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=7035"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=7036"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=7037"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_line;i=7038"]),
    ],
)
o6.reference(plastics_extrusion_line_objtypes.ExtrusionLine_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_line;i=5025"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, plastics_extrusion, plastics_rubber, plastics_extrusion_line_datypes, plastics_extrusion_line_objtypes
